#!/usr/bin/env python3
"""Validator konsistensi OBE untuk paket mata kuliah Prodi Informatika UAI.

Menegakkan aturan V1-V13 pada Pedoman OBE & Konvensi (00-pedoman-obe) sec. Q;
skala acuan V13 dibaca dari registri 00-pedoman-obe/konversi-nilai.md:

    V1  Metadata front-matter          V8  Konvensi (footer tagline)
    V2  Keunikan id                    V9  Sitasi regulasi yang dicabut
    V3  Integritas referensial         V10 Tautan relatif
    V4  Pola kode lama                 V11 Pagu ukuran
    V5  Cakupan (constructive align.)  V12 Pengesahan (cpl_status)
    V6  Bobot asesmen = 100%           V13 Skala konversi nilai
    V7  Data induk

V3, V5, V6, dan V7 hanya berlaku untuk mata kuliah yang RPS-nya
ber-front-matter `tipe: rps`; daftar aturan beserta uraiannya dicetak --help.

V10 memeriksa tautan relatif Markdown [teks](target) (bukan http(s):, mailto:,
atau #anchor) terhadap sistem berkas, dengan mengabaikan isi blok kode
berpagar dan kode inline, karena tautan di sana hanya contoh (mis. README
contoh di dalam ```markdown) dan tidak dirender GitHub sebagai tautan. Blok
berpagar dikenali seperti CommonMark/GitHub: dibuka oleh >= 3 backtick atau
tilde (boleh berindentasi, mis. di butir daftar, atau di dalam kutipan ">"),
dan hanya ditutup oleh pagar dari karakter yang sama, minimal sepanjang pagar
pembuka, tanpa info string, pada kedalaman kutipan yang sama. Jadi ```python
di dalam blok ```markdown TIDAK menutup blok itu, tetapi ``` polos sesudahnya
menutupnya (seperti di GitHub), sehingga tautan setelah contoh bersarang
semacam itu tetap diperiksa; contoh bersarang perlu pagar luar ````markdown.
Pagar yang tidak tertutup berlaku sampai akhir berkas (atau akhir
kutipannya). Kode inline: deretan n backtick sampai deretan n backtick
berikutnya pada baris yang sama (kode inline lintas baris dan blok kode
berindentasi 4 spasi tanpa pagar tidak dikenali). Pesan V10 memuat nomor
baris target tautan.

V13 membaca tabel §A konversi-nilai.md (rentang, huruf, bobot) saat dijalankan,
lalu memeriksa setiap tabel Markdown di luar blok kode yang memuat >= 3 baris
berisi sel huruf mutu tersendiri (A, A−/A-, B+, ...) bersama sel rentang 0-100
("81,00 – 100,00", "85-100", "≥ 85", "Nilai Akhir < 40", "75 ≤ N < 78",
"80,99 < N ≤ 100"); operator tegas > dan < digeser satu langkah presisi
registri (0,01), sehingga "> 80" dibaca ≥ 80,01. Setiap baris seperti itu harus
cocok dengan registri: batas bawah dan atas bertoleransi 0,005 (batas atas yang
ditulis dengan presisi lebih rendah, mis. "78-80", dibandingkan dengan batas
resmi yang dipotong ke presisi itu), koma atau titik desimal, "−" atau "-".
Huruf di luar registri (AB, BC, C−, A+, ...) dan huruf resmi yang tidak ada di
tabel (tabel tidak lengkap) juga dilaporkan. Bila tabel punya kolom Bobot/Mutu,
nilainya ikut dicocokkan. Bila registri tidak ditemukan atau tabel §A-nya tidak
terbaca, V13 dilaporkan pada registri. Dikecualikan: konversi-nilai.md,
AUDIT-KESELARASAN-IF2205-IF2206.md (dokumen historis), dan tabel yang dalam lima
baris di atasnya diberi label "skala disederhanakan" (contoh latihan).

Python murni, tanpa dependensi eksternal. Jalankan dari akar repositori:

    python3 tools/validasi-obe.py                       # seluruh repositori
    python3 tools/validasi-obe.py --mk INF-101          # satu MK (kode_mk RPS)
    python3 tools/validasi-obe.py --baseline-tulis b.json   # simpan temuan
    python3 tools/validasi-obe.py --baseline b.json     # hanya temuan baru
    python3 tools/validasi-obe.py --help                # penggunaan + aturan

Mode baseline. --baseline-tulis BERKAS menulis semua pelanggaran saat ini ke
BERKAS sebagai JSON (daftar objek {"aturan", "berkas", "pesan"}, terurut
menurut nomor aturan, berkas, lalu pesan dengan angka dibandingkan sebagai
bilangan) dan keluar 0; berkas tidak ditulis bila ada galat penggunaan, dan
folder tujuan diperiksa sebelum repositori dipindai. --baseline BERKAS hanya
melaporkan pelanggaran yang tidak ada di baseline. Pencocokan memakai kunci
(aturan, berkas, pesan) sebagai multiset (dua temuan identik butuh dua entri
baseline), dua tahap: temuan yang sama persis dipasangkan lebih dulu, lalu
sisanya dicocokkan dengan angka pada "baris N" dan "N baris" di pesan diganti
"#". Dengan begitu pergeseran nomor baris (V10, V13) dan perubahan jumlah baris
berkas yang sudah melampaui pagu (V11) tidak dihitung sebagai temuan baru,
sedangkan temuan yang tidak bergeser tetap dipasangkan dengan entri yang
tepat. Ringkasan menyebut jumlah temuan warisan (cocok dengan baseline),
temuan baru, dan entri baseline yang sudah teratasi. --baseline dapat digabung
dengan --mk; entri baseline untuk berkas di luar cakupan --mk tidak dihitung
sebagai teratasi.

Kode keluar: 0 = tidak ada pelanggaran (mode --baseline: tidak ada temuan baru;
--baseline-tulis: baseline ditulis; --help); 1 = ada pelanggaran (mode
--baseline: ada temuan baru); 2 = galat penggunaan (opsi tidak dikenal, opsi
tanpa argumen, mata kuliah --mk tidak ditemukan, berkas baseline tidak dapat
dibaca/ditulis atau formatnya salah).
"""
import os, re, sys, glob, json, textwrap, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MK   = os.path.join(ROOT, "mata-kuliah")
PEDOMAN = os.path.join(MK, "00-pedoman-obe")

TIPE_SAH   = {"rps","rtm","modul","lab","bab-buku-ajar","asesmen","rubrik","mutu",
              "pedoman","pedoman-praktikum","analisis-strategis","dataset","readme"}
STATUS_SAH = {"draft","berlaku","arsip"}
LEVEL_AI   = {"understand","apply","create"}
WAJIB      = ["id","tipe","judul","kode_mk","nama_mk","prodi","versi","status","diperbarui"]
PAGU       = {"rps":550,"mutu":180}
FOOTER     = "Problem Solvers in Digital"

RE_FM      = re.compile(r'\A---\n(.*?)\n---\n', re.S)
RE_TANGGAL = re.compile(r'^\d{4}-\d{2}-\d{2}$')
RE_LAMA    = re.compile(r'(?<!Sub-)\bCPMK-\d+\.\d+|\bSub-CPMK \d+\.\d+')
RE_SUB     = re.compile(r'Sub-CPMK-(\d+\.\d+)')
RE_TAUTAN  = re.compile(r'\[[^\]]*\]\(((?!https?:|mailto:|#)[^)]+)\)')
RE_BLOOM   = {"bloom_c": re.compile(r'^C[1-6]$'), "bloom_a": re.compile(r'^A[1-5]$'),
              "bloom_p": re.compile(r'^P[1-5]$')}

masalah = []
def lapor(aturan, berkas, pesan):
    masalah.append((aturan, os.path.relpath(berkas, ROOT), pesan))

def baca_fm(teks):
    """Pengurai front-matter YAML minimal: key: nilai | [a, b] | \"teks\"."""
    m = RE_FM.match(teks)
    if not m: return None, teks
    fm = {}
    for baris in m.group(1).split("\n"):
        if not baris.strip() or baris.lstrip().startswith("#"): continue
        if ":" not in baris: continue
        k, _, v = baris.partition(":")
        k, v = k.strip(), v.strip()
        if v.startswith("[") and v.endswith("]"):
            isi = v[1:-1].strip()
            fm[k] = [x.strip().strip('"\'') for x in isi.split(",")] if isi else []
        else:
            fm[k] = v.strip('"\'')
    return fm, teks[m.end():]

def kumpulkan(pola):
    return sorted(glob.glob(os.path.join(MK, pola), recursive=True))

# ------------------------------------------------------------ argumen & bantuan
ATURAN = {"V1":"Metadata","V2":"Keunikan id","V3":"Integritas referensial","V4":"Pola kode lama",
          "V5":"Cakupan (constructive alignment)","V6":"Bobot asesmen","V7":"Data induk",
          "V8":"Konvensi","V9":"Sitasi","V10":"Tautan","V11":"Pagu ukuran","V12":"Pengesahan",
          "V13":"Skala konversi nilai"}
URAIAN = {
    "V1":  "YAML front-matter ada; field wajib, tipe, status, diperbarui (ISO 8601), "
           "level_ai, bloom_* sah",
    "V2":  "`id` front-matter unik di seluruh repositori",
    "V3":  "Sub-CPMK/CPMK/CPL/BK yang dirujuk terdaftar di RPS, cpl-master.md, "
           "registri bahan kajian (*)",
    "V4":  "tidak ada pola kode lama CPMK-n.m / 'Sub-CPMK n.m' "
           "(kecuali migrasi/ dan 00-pedoman-obe/)",
    "V5":  "setiap Sub-CPMK RPS dirujuk materi dan asesmen; setiap CPMK punya Sub-CPMK (*)",
    "V6":  "bobot asesmen pada §G.1 RPS berjumlah 100% (*)",
    "V7":  "nama_mk/kode_mk sama dengan RPS; SKS hanya ditulis di RPS (*)",
    "V8":  "footer tagline prodi ada",
    "V9":  "tidak mensitasi Permendikbud Nomor 3 Tahun 2020 (sudah dicabut)",
    "V10": "tautan relatif [teks](target) menunjuk berkas yang ada; isi blok kode "
           "berpagar dan kode inline diabaikan",
    "V11": ", ".join(f"tipe {t} <= {n} baris" for t, n in PAGU.items()),
    "V12": "RPS berstatus 'berlaku' tidak boleh ber-cpl_status 'interim'",
    "V13": "tabel huruf mutu <-> rentang 0-100 sama dengan §A "
           "00-pedoman-obe/konversi-nilai.md",
}
OPSI_NILAI = {"--mk": ("KODE_MK", "kode_mk pada front-matter RPS, mis. --mk INF-101"),
              "--baseline": ("BERKAS", "berkas JSON hasil --baseline-tulis"),
              "--baseline-tulis": ("BERKAS", "jalur berkas JSON yang akan ditulis")}

def bantuan():
    aturan = "\n".join(textwrap.fill(f"{ATURAN[a]} — {URAIAN[a]}", 79, initial_indent=f"  {a:<4} ",
                                     subsequent_indent=" " * 7) for a in ATURAN)
    return f"""Penggunaan: python3 tools/validasi-obe.py [-h] [--mk KODE_MK]
                  [--baseline BERKAS | --baseline-tulis BERKAS]

Validator konsistensi OBE (Pedoman OBE §Q) untuk semua mata-kuliah/**/*.md.
Jalankan dari akar repositori; tanpa dependensi selain Python 3.

Opsi:
  -h, --help               cetak bantuan ini lalu keluar (kode 0)
  --mk KODE_MK             periksa satu mata kuliah saja, dikenali dari
                           kode_mk front-matter RPS (tipe: rps), mis. INF-101;
                           berkas 00-pedoman-obe/ tetap ikut diperiksa
  --baseline BERKAS        laporkan HANYA pelanggaran yang tidak ada di BERKAS
                           (JSON hasil --baseline-tulis), dicocokkan per
                           aturan + berkas + pesan dengan nomor baris
                           diabaikan; kode 0 bila tidak ada temuan baru,
                           1 bila ada
  --baseline-tulis BERKAS  tulis semua pelanggaran saat ini ke BERKAS (JSON
                           terurut: aturan, berkas, pesan) lalu keluar (kode 0)

Aturan (Pedoman OBE §Q):
{aturan}
  (*) hanya untuk mata kuliah yang RPS-nya ber-front-matter `tipe: rps`

Contoh:
  python3 tools/validasi-obe.py --baseline-tulis /tmp/baseline-obe.json
  python3 tools/validasi-obe.py --baseline /tmp/baseline-obe.json

Kode keluar:
  0  tidak ada pelanggaran; --baseline: tidak ada temuan baru;
     --baseline-tulis: baseline ditulis; --help
  1  ada pelanggaran; --baseline: ada temuan baru
  2  galat penggunaan: opsi tidak dikenal, opsi tanpa argumen, mata kuliah
     --mk tidak ditemukan, berkas baseline tidak dapat dibaca/ditulis atau
     formatnya salah"""

def galat(pesan):
    print(f"validasi-obe.py: galat: {pesan}\nGunakan --help untuk melihat penggunaan.",
          file=sys.stderr)
    sys.exit(2)

def urai_argumen(argv):
    if "-h" in argv or "--help" in argv:
        print(bantuan()); sys.exit(0)
    arg, i = {}, 0
    while i < len(argv):
        nama, sama, nilai = argv[i].partition("=")
        if nama not in OPSI_NILAI:
            galat(f"opsi atau argumen tidak dikenal: {argv[i]!r}")
        if sama:
            i += 1
        elif i + 1 < len(argv) and not argv[i + 1].startswith("-"):
            nilai, i = argv[i + 1], i + 2
        else:
            nilai, i = "", i + 1
        if not nilai.strip():
            galat(f"opsi {nama} membutuhkan argumen {OPSI_NILAI[nama][0]} "
                  f"({OPSI_NILAI[nama][1]})")
        if nama in arg:
            galat(f"opsi {nama} diberikan lebih dari sekali")
        arg[nama] = nilai
    if "--baseline" in arg and "--baseline-tulis" in arg:
        galat("--baseline dan --baseline-tulis tidak dapat dipakai bersamaan")
    if "--baseline-tulis" in arg:         # gagal lebih awal, sebelum seluruh repositori diperiksa
        jalur = os.path.abspath(arg["--baseline-tulis"])
        induk = os.path.dirname(jalur)
        if os.path.isdir(jalur) or not os.path.isdir(induk) or not os.access(induk, os.W_OK) \
                or (os.path.exists(jalur) and not os.access(jalur, os.W_OK)):
            galat(f"berkas baseline tidak dapat ditulis: {arg['--baseline-tulis']} "
                  "(folder tidak ada, bukan berkas, atau tanpa izin tulis)")
    return arg

def baca_baseline(jalur):
    """Daftar (aturan, berkas, pesan) dari berkas JSON hasil --baseline-tulis."""
    try:
        with open(jalur, encoding="utf-8") as f:
            data = json.load(f)
    except OSError as e:
        galat(f"berkas baseline tidak dapat dibaca: {jalur} ({e.strerror})")
    except ValueError as e:
        galat(f"berkas baseline bukan JSON yang sah: {jalur} ({e})")
    kunci = ("aturan", "berkas", "pesan")
    if not isinstance(data, list) or not all(
            isinstance(x, dict) and all(isinstance(x.get(k), str) for k in kunci) for x in data):
        galat(f"format baseline tidak dikenal: {jalur} (harus daftar objek "
              '{"aturan", "berkas", "pesan"} hasil --baseline-tulis)')
    return [tuple(x[k] for k in kunci) for x in data]

ARG = urai_argumen(sys.argv[1:])
FILTER = ARG.get("--mk")
BASELINE = baca_baseline(ARG["--baseline"]) if "--baseline" in ARG else None

# ---------------------------------------------------------------- muat berkas
berkas =[p for p in kumpulkan("**/*.md") if "/sumber/" not in p]
dok = {}
for p in berkas:
    teks = open(p, encoding="utf-8").read()
    fm, isi = baca_fm(teks)
    dok[p] = {"fm": fm, "isi": isi, "teks": teks,
              "baris": teks.count("\n") + 1, "subs": set(RE_SUB.findall(teks))}

# ------------------------------------------------- registri CPL & Bahan Kajian
cpl_sah, bk_sah = set(), set()
fcpl = os.path.join(PEDOMAN, "cpl-master.md")
if os.path.exists(fcpl):
    cpl_sah = set(re.findall(r'\*\*(CPL[A-Z0-9\-]*\d)\*\*', open(fcpl, encoding="utf-8").read()))
fbk = os.path.join(PEDOMAN, "registri-bahan-kajian.md")
if os.path.exists(fbk):
    bk_sah = set(re.findall(r'\b(BK\d{2})\b', open(fbk, encoding="utf-8").read()))

# --------------------------------------------- himpunan sah per mata kuliah
mk_daftar = {}
for p, d in dok.items():
    fm = d["fm"]
    if fm and fm.get("tipe") == "rps":
        kode = fm.get("kode_mk", "?")
        isi = d["isi"]
        mk_daftar[kode] = {
            "rps": p,
            "cpmk": set(re.findall(r'\*\*(CPMK-\d+)\*\*', isi)),
            "sub":  set(RE_SUB.findall(isi)),
            "dir":  os.path.dirname(os.path.dirname(p)),
            "sks":  fm.get("sks"),
            "cpl":  fm.get("cpl", []),
            "bk":   fm.get("bk", []),
        }

def mk_dari(path):
    for kode, info in mk_daftar.items():
        if path.startswith(info["dir"] + os.sep): return kode, info
    return None, None

if FILTER:
    info = mk_daftar.get(FILTER)
    if info:
        cakupan = info["dir"] + os.sep
        dok = {p: d for p, d in dok.items()
               if p.startswith(cakupan) or p.startswith(PEDOMAN)}
        mk_daftar = {FILTER: info}
    else:
        galat(f"mata kuliah {FILTER} tidak ditemukan; --mk mengenali kode_mk RPS "
              f"ber-front-matter `tipe: rps`: {', '.join(sorted(mk_daftar)) or '(tidak ada)'}")

# ------------------------------------------------------------------ V1 & V12
terlihat_id = {}
for p, d in dok.items():
    fm = d["fm"]
    if fm is None:
        lapor("V1", p, "tidak ada YAML front-matter"); continue
    wajib = [k for k in WAJIB
             if not (fm.get("tipe") == "pedoman" and k in ("kode_mk", "nama_mk"))]
    for k in wajib:
        if k not in fm: lapor("V1", p, f"field wajib '{k}' tidak ada")
    if fm.get("tipe") not in TIPE_SAH:
        lapor("V1", p, f"tipe tidak sah: {fm.get('tipe')!r}")
    if fm.get("status") not in STATUS_SAH:
        lapor("V1", p, f"status tidak sah: {fm.get('status')!r}")
    if not RE_TANGGAL.match(str(fm.get("diperbarui", ""))):
        lapor("V1", p, f"diperbarui bukan ISO 8601: {fm.get('diperbarui')!r}")
    if "level_ai" in fm and fm["level_ai"] not in LEVEL_AI:
        lapor("V1", p, f"level_ai tidak sah: {fm['level_ai']!r}")
    for k, rx in RE_BLOOM.items():
        for v in fm.get(k, []) or []:
            if not rx.match(v): lapor("V1", p, f"{k} tidak sah: {v!r}")
    # V2
    if "id" in fm:
        if fm["id"] in terlihat_id:
            lapor("V2", p, f"id '{fm['id']}' bertabrakan dengan {os.path.relpath(terlihat_id[fm['id']], ROOT)}")
        terlihat_id[fm["id"]] = p
    # V12
    if fm.get("tipe") == "rps" and fm.get("status") == "berlaku" and fm.get("cpl_status") == "interim":
        lapor("V12", p, "RPS berstatus 'berlaku' padahal cpl_status masih 'interim'")

# ------------------------------------------------------------------ V3 & V4
for p, d in dok.items():
    fm, kode, info = d["fm"], *mk_dari(p)
    # V4 - pola lama dilarang (kecuali berkas migrasi & pedoman yang mendokumentasikannya)
    if "/migrasi/" not in p and not p.startswith(PEDOMAN):
        for temuan in set(RE_LAMA.findall(d["teks"])):
            lapor("V4", p, f"pola kode lama terlarang: '{temuan}'")
    if not info: continue
    # V3 - integritas referensial
    for s in d["subs"] - info["sub"]:
        lapor("V3", p, f"Sub-CPMK-{s} tidak terdaftar di §E RPS {kode}")
    if fm:
        for c in fm.get("cpmk", []) or []:
            if c and c not in info["cpmk"]:
                lapor("V3", p, f"{c} tidak terdaftar di §D RPS {kode}")
        for c in fm.get("cpl", []) or []:
            if c and cpl_sah and c not in cpl_sah:
                lapor("V3", p, f"CPL '{c}' tidak ada di cpl-master.md")
        for b in fm.get("bk", []) or []:
            if b and bk_sah and b not in bk_sah:
                lapor("V3", p, f"Bahan Kajian '{b}' tidak ada di registri")

# ---------------------------------------------------------------------- V5
for kode, info in mk_daftar.items():
    materi, asesmen = set(), set()
    for p, d in dok.items():
        if not p.startswith(info["dir"] + os.sep): continue
        t = (d["fm"] or {}).get("tipe")
        if t in ("modul", "lab", "bab-buku-ajar"): materi |= d["subs"]
        elif t in ("asesmen", "rubrik"):           asesmen |= d["subs"]
    for s in sorted(info["sub"], key=lambda x: (int(x.split('.')[0]), int(x.split('.')[1]))):
        if s not in materi:
            lapor("V5", info["rps"], f"Sub-CPMK-{s} tidak dirujuk materi mana pun")
        if s not in asesmen:
            lapor("V5", info["rps"], f"Sub-CPMK-{s} tidak dirujuk asesmen mana pun")
    for c in sorted(info["cpmk"]):
        if not any(s.startswith(c.split("-")[1] + ".") for s in info["sub"]):
            lapor("V5", info["rps"], f"{c} tidak punya Sub-CPMK")

# ---------------------------------------------------------------------- V6
RE_BOBOT = re.compile(r'\|\s*\*{0,2}(\d{1,3})%\*{0,2}\s*\|')
for kode, info in mk_daftar.items():
    isi = dok[info["rps"]]["isi"]
    blok = re.search(r'### G\.1.*?(?=###|\Z)', isi, re.S)
    if blok:
        angka = [int(x) for x in RE_BOBOT.findall(blok.group(0))]
        total = sum(a for a in angka if a != 100)
        if angka and total != 100:
            lapor("V6", info["rps"], f"jumlah bobot asesmen = {total}%, seharusnya 100%")

# ---------------------------------------------------------------------- V7
for p, d in dok.items():
    kode, info = mk_dari(p)
    if not info or not d["fm"]: continue
    for k in ("nama_mk", "kode_mk"):
        if d["fm"].get(k) and d["fm"][k] != dok[info["rps"]]["fm"].get(k):
            lapor("V7", p, f"{k}='{d['fm'][k]}' berbeda dari RPS '{dok[info['rps']]['fm'].get(k)}'")
    if d["fm"].get("tipe") != "rps" and "sks" in d["fm"]:
        lapor("V7", p, "field 'sks' hanya boleh ada di RPS (Pedoman §I.9)")
    if d["fm"].get("tipe") in ("modul", "bab-buku-ajar") and re.search(r'\(\d+ SKS\)', d["teks"]):
        lapor("V7", p, "menyebut SKS di luar RPS (Pedoman §I.9)")

# ------------------------------------------------------------- V8, V9, V11
for p, d in dok.items():
    if FOOTER not in d["teks"]:
        lapor("V8", p, "footer tagline prodi tidak ada")
    if "Nomor 3 Tahun 2020" in d["teks"] and not p.startswith(PEDOMAN) and "/migrasi/" not in p:
        lapor("V9", p, "masih mensitasi Permendikbud Nomor 3 Tahun 2020 (sudah dicabut)")
    t = (d["fm"] or {}).get("tipe")
    if t in PAGU and d["baris"] > PAGU[t]:
        lapor("V11", p, f"{d['baris']} baris melampaui pagu {PAGU[t]} baris")

# --------------------------------------------------------------------- V10
# Tautan di dalam blok kode berpagar atau kode inline hanyalah contoh ilustratif
# (mis. README contoh di dalam ```markdown) dan tidak dirender GitHub sebagai tautan.
RE_PAGAR       = re.compile(r'^\s*((?:>\s?)*)\s*(`{3,}|~{3,})(.*)$')
RE_KUTIPAN     = re.compile(r'^\s*((?:>\s?)*)')
RE_KODE_INLINE = re.compile(r'(?<!`)(`+)(?!`)(.+?)(?<!`)\1(?!`)')

def tanpa_kode(teks):
    """Salinan teks dengan baris blok kode berpagar dikosongkan dan kode inline diganti
    spasi; jumlah baris tetap sehingga nomor baris tetap sahih.
    Seperti CommonMark/GitHub: pagar pembuka = >= 3 backtick atau tilde (info string
    pagar backtick tidak boleh memuat backtick); penutup = karakter yang sama, minimal
    sepanjang pembuka, tanpa info string, pada kedalaman kutipan '>' yang sama. Blok di
    dalam kutipan berakhir bersama kutipannya; pagar tak tertutup berlaku sampai akhir
    berkas. Indentasi pagar tidak dibatasi (pagar di dalam butir daftar)."""
    hasil, pagar = [], None               # pagar = (karakter, panjang, kedalaman kutipan)
    for baris in teks.split("\n"):
        m = RE_PAGAR.match(baris)
        if pagar:
            kutip = RE_KUTIPAN.match(baris).group(1).count(">")
            if m and kutip == pagar[2] and m.group(2)[0] == pagar[0] \
                    and len(m.group(2)) >= pagar[1] and not m.group(3).strip():
                pagar = None; hasil.append(""); continue
            if kutip >= pagar[2]:
                hasil.append(""); continue
            pagar = None                  # kutipan berakhir -> blok kode ikut berakhir
        if m and not (m.group(2)[0] == "`" and "`" in m.group(3)):
            pagar = (m.group(2)[0], len(m.group(2)), m.group(1).count(">"))
            hasil.append(""); continue
        hasil.append(RE_KODE_INLINE.sub(" ", baris))
    return "\n".join(hasil)

for p, d in dok.items():
    bersih = tanpa_kode(d["teks"])
    for m in RE_TAUTAN.finditer(bersih):
        target = m.group(1).split("#")[0].strip()
        if not target: continue
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(p), target))):
            no = bersih.count("\n", 0, m.start(1)) + 1
            lapor("V10", p, f"baris {no}: tautan relatif putus: {target}")

# --------------------------------------------------------------------- V13
# Skala konversi nilai: tabel huruf mutu ↔ rentang 0-100 harus sama dengan
# tabel §A registri konversi-nilai.md (satu-satunya sumber skala).
FKONVERSI   = os.path.join(PEDOMAN, "konversi-nilai.md")
V13_KECUALI = {FKONVERSI, os.path.join(MK, "00-meta", "AUDIT-KESELARASAN-IF2205-IF2206.md")}
_ANGKA      = r'(\d{1,3}(?:[.,]\d+)?)'
RE_V13_HURUF   = re.compile(r'^[A-F](?:[A-F]|[+\-−])?$')     # kandidat sel huruf mutu
RE_V13_RENTANG = re.compile(rf'^{_ANGKA}\s*(?:-{{1,2}}|[–—−]|s\.\s?d\.?|s/d|sampai)\s*{_ANGKA}$', re.I)
_V13_NAMA      = r'[A-Za-z_]+(?:\s+[A-Za-z_]+)*'              # "N", "NA", "Nilai Akhir"
RE_V13_BATAS   = re.compile(rf'^(?:{_V13_NAMA}\s*)?(≥|>=|>|≤|<=|<)\s*{_ANGKA}$')
RE_V13_APIT    = re.compile(rf'^{_ANGKA}\s*(?:(<|≤|<=)\s*{_V13_NAMA}\s*|[-–—−]\s*)(<|≤|<=)\s*{_ANGKA}$')
RE_V13_KOLBOBOT = re.compile(r'bobot|mutu|grade point|indeks', re.I)
V13_LANGKAH    = 0.01      # langkah presisi registri (dua desimal) untuk operator > dan <

def v13_angka(s):
    """'80,99' -> (80.99, 2): nilai dan jumlah desimal yang ditulis."""
    s = s.replace(",", ".")
    return float(s), (len(s.split(".")[1]) if "." in s else 0)

def v13_sel(baris):
    sel = baris.strip().strip("|").split("|")
    return [re.sub(r'\*\*|__|`', "", c).strip() for c in sel]

def v13_rentang(sel):
    """Sel rentang -> (bawah, atas, desimal_atas) atau None.
    Batas yang hanya tersirat ("≥ 85" tanpa atas, "< 40" tanpa bawah) bernilai None
    dan tidak dicocokkan; tabel ambang bawah saja tetap diperiksa batas bawahnya.
    Operator tegas ("> 80", "< 78", "85 < N") digeser satu langkah presisi registri
    (0,01), bukan presisi yang ditulis: "> 80" = ≥ 80,01, "< 78" = ≤ 77,99."""
    m = RE_V13_RENTANG.match(sel)
    if m:
        (a, ka), (b, kb) = v13_angka(m.group(1)), v13_angka(m.group(2))
        return (a, b, kb) if a <= b else (b, a, ka)
    m = RE_V13_APIT.match(sel)
    if m:
        (a, _), (b, kb) = v13_angka(m.group(1)), v13_angka(m.group(4))
        if m.group(2) == "<": a += V13_LANGKAH
        return (a, b - V13_LANGKAH, 2) if m.group(3) == "<" else (a, b, kb)
    m = RE_V13_BATAS.match(sel)
    if m:
        op, (x, k) = m.group(1), v13_angka(m.group(2))
        if op in ("≥", ">="): return (x, None, None)
        if op == ">":         return (x + V13_LANGKAH, None, None)
        if op in ("≤", "<="): return (None, x, k)
        return (None, x - V13_LANGKAH, 2)
    return None

def v13_norm(h):
    return h.replace("−", "-")

def v13_fmt(x):
    return f"{x:.2f}".replace(".", ",")

# registri: huruf -> (bawah, atas, bobot)
skala_resmi, huruf_resmi = {}, []
if os.path.exists(FKONVERSI):
    teks_k = open(FKONVERSI, encoding="utf-8").read()
    bagian = re.search(r'^## A\..*?(?=^## |\Z)', teks_k, re.S | re.M)
    kol = None
    for baris in (bagian.group(0).split("\n") if bagian else []):
        if not baris.lstrip().startswith("|"): continue
        sel = v13_sel(baris)
        if kol is None:
            idx = lambda pola: next((i for i, c in enumerate(sel) if re.search(pola, c, re.I)), None)
            kol = (idx("rentang"), idx("huruf"), idx("bobot"))
            if None in kol[:2]: kol = None
            continue
        if len(sel) <= max(i for i in kol if i is not None): continue
        r = v13_rentang(sel[kol[0]])
        if not r or None in r[:2] or not RE_V13_HURUF.match(sel[kol[1]]): continue
        bobot = v13_angka(sel[kol[2]])[0] if kol[2] is not None and re.match(r'^\d+(?:[.,]\d+)?$', sel[kol[2]]) else None
        skala_resmi[v13_norm(sel[kol[1]])] = (r[0], r[1], bobot)
        huruf_resmi.append(sel[kol[1]])
    if not skala_resmi:
        lapor("V13", FKONVERSI, "tabel §A tidak dapat dibaca (kolom Rentang/Huruf/Bobot)")
else:
    lapor("V13", FKONVERSI, "registri konversi-nilai.md tidak ditemukan; skala nilai tidak dapat diperiksa")

def v13_cocok(bawah, atas, desimal, resmi):
    # toleransi setengah satuan desimal kedua: batas yang meleset 0,01 (mis. 80,99 untuk A,
    # 75,00 sebagai batas atas B) tetap dilaporkan
    if bawah is not None and abs(bawah - resmi[0]) > 0.005: return False
    if atas is None or abs(atas - resmi[1]) <= 0.005: return True
    # batas atas yang ditulis dengan presisi lebih rendah (mis. "78-80" untuk 80,99)
    return desimal < 2 and abs(atas - int(resmi[1] * 10 ** desimal + 1e-9) / 10 ** desimal) <= 1e-9

def v13_teks(bawah, atas):
    if bawah is None: return f"≤ {v13_fmt(atas)}"
    if atas is None:  return f"≥ {v13_fmt(bawah)}"
    return f"{v13_fmt(bawah)} – {v13_fmt(atas)}"

def v13_periksa_tabel(p, tabel):
    """tabel = [(nomor_baris, [sel, ...]), ...] termasuk baris judul."""
    kol_bobot = None
    pemisah = "|".join(tabel[1][1]) if len(tabel) >= 2 else ""
    if re.match(r'^[\s|:\-]*-[\s|:\-]*$', pemisah):     # baris ke-2 = pemisah judul tabel
        kol_bobot = next((i for i, c in enumerate(tabel[0][1])
                          if RE_V13_KOLBOBOT.search(c) and not re.search(r'huruf', c, re.I)), None)
    # baris yang punya sel huruf mutu, lalu pilih SATU kolom rentang 0-100 per tabel
    # (kolom lain, mis. "Total Skor (max 16)" atau IPK 0-4, tidak ikut dicocokkan)
    baris_huruf, kolom = [], {}
    for no, sel in tabel:
        ih = next((i for i, c in enumerate(sel) if RE_V13_HURUF.match(c)), None)
        if ih is None: continue
        baris_huruf.append((no, sel, sel[ih]))
        for i, c in enumerate(sel):
            r = v13_rentang(c) if i != ih else None
            if r and all(0 <= x <= 100 for x in r[:2] if x is not None):
                kolom.setdefault(i, {})[no] = r
    puncak = lambda v: max(x for r in v.values() for x in r[:2] if x is not None)
    calon_kolom = [(len(v), puncak(v), i) for i, v in kolom.items() if puncak(v) >= 50]
    if not calon_kolom: return
    jumlah, _, kr = max(calon_kolom)
    if jumlah < 3: return
    ada = {v13_norm(h) for no, s, h in baris_huruf if no in kolom[kr]}
    hilang = [h for h in huruf_resmi if v13_norm(h) not in ada]
    if hilang:
        lapor("V13", p, f"baris {tabel[0][0]}: tabel konversi tidak lengkap, tanpa {', '.join(hilang)}")
    for no, sel, huruf in baris_huruf:
        if no not in kolom[kr]: continue
        bawah, atas, desimal = kolom[kr][no]
        resmi = skala_resmi.get(v13_norm(huruf))
        if resmi is None:
            lapor("V13", p, f"baris {no}: huruf mutu tidak dikenal '{huruf}' (skala resmi: "
                            f"{', '.join(huruf_resmi)})"); continue
        if not v13_cocok(bawah, atas, desimal, resmi):
            lapor("V13", p, f"baris {no}: {huruf} {v13_teks(bawah, atas)} ≠ resmi "
                            f"{v13_teks(resmi[0], resmi[1])}")
        if kol_bobot is not None and resmi[2] is not None and kol_bobot < len(sel) \
                and re.match(r'^\d(?:[.,]\d+)?$', sel[kol_bobot]):
            b = v13_angka(sel[kol_bobot])[0]
            if b <= 4 and abs(b - resmi[2]) > 0.005:
                lapor("V13", p, f"baris {no}: bobot {huruf} = {sel[kol_bobot]} ≠ resmi {v13_fmt(resmi[2])}")

if skala_resmi:
    for p, d in dok.items():
        if p in V13_KECUALI: continue
        semua, tabel, pagar = d["teks"].split("\n"), [], False
        for no, baris in enumerate(semua + [""], 1):
            if re.match(r'^\s*(```|~~~)', baris): pagar = not pagar
            if not pagar and baris.lstrip().startswith("|"):
                tabel.append((no, v13_sel(baris))); continue
            if tabel:
                # skala yang sengaja disederhanakan untuk latihan dan diberi label eksplisit
                # (mis. "skala disederhanakan untuk latihan ...") tidak diperiksa
                awal = tabel[0][0] - 1
                if "skala disederhanakan" not in " ".join(semua[max(0, awal - 5):awal]).lower():
                    v13_periksa_tabel(p, tabel)
                tabel = []

# ------------------------------------------------------------------- laporan
def no_aturan(a):
    return int(a[1:]) if a[1:].isdigit() else 999

def per_aturan(daftar):
    per = {}
    for a, f, m in daftar: per.setdefault(a, []).append((f, m))
    return per

def cetak_rincian(per, keterangan=""):
    for a in sorted(per, key=no_aturan):
        print(f"\n## {a} — {ATURAN.get(a,'')}{keterangan}\n")
        for f, m in per[a][:40]:
            print(f"- `{f}` — {m}")
        if len(per[a]) > 40:
            print(f"- … dan {len(per[a]) - 40} lainnya")

def ringkas(per):
    return ", ".join(f"{a} {len(per[a])}" for a in sorted(per, key=no_aturan)) or "-"

# kunci pencocokan baseline: berkas bergaya POSIX; kunci longgar mengganti angka pada
# "baris N" / "N baris" dengan "#" agar tahan terhadap pergeseran nomor baris
RE_ANGKA_BARIS = re.compile(r'\bbaris \d+|\b\d+ baris\b')
def kunci_tepat(a, f, m):
    return (a, f.replace(os.sep, "/"), m)

def kunci_baseline(a, f, m):
    return (a, f.replace(os.sep, "/"),
            RE_ANGKA_BARIS.sub(lambda x: re.sub(r'\d+', '#', x.group(0)), m))

def urut_alami(s):
    """'baris 9' < 'baris 34': bagian angka dibandingkan sebagai bilangan."""
    return [int(t) if t.isdigit() else t for t in re.split(r'(\d+)', s)]

print(f"# Laporan Validasi OBE\n\nBerkas diperiksa: {len(dok)}  |  Mata kuliah: {len(mk_daftar)}\n")

if "--baseline-tulis" in ARG:
    jalur = ARG["--baseline-tulis"]
    entri = sorted((kunci_tepat(a, f, m) for a, f, m in masalah),
                   key=lambda x: (no_aturan(x[0]), x[1], urut_alami(x[2])))
    isi = "[\n" + ",\n".join("  " + json.dumps({"aturan": a, "berkas": f, "pesan": m},
                                               ensure_ascii=False) for a, f, m in entri)
    try:
        with open(jalur, "w", encoding="utf-8") as fb:
            fb.write(isi + ("\n]\n" if entri else "]\n"))
    except OSError as e:
        galat(f"berkas baseline tidak dapat ditulis: {jalur} ({e.strerror})")
    print(f"**Baseline ditulis:** `{jalur}` — {len(entri)} pelanggaran "
          f"({ringkas(per_aturan(masalah))}).")
    sys.exit(0)

if BASELINE is not None:
    # tahap 1: pasangkan temuan yang sama persis (termasuk nomor baris) dengan entri baseline;
    # tahap 2: sisanya dipasangkan dengan kunci longgar (nomor baris diabaikan). Keduanya
    # multiset: dua temuan identik butuh dua entri baseline.
    sisa_tepat = collections.Counter(kunci_tepat(a, f, m) for a, f, m in BASELINE)
    cocok = [False] * len(masalah)
    for i, x in enumerate(masalah):
        k = kunci_tepat(*x)
        if sisa_tepat[k] > 0:
            sisa_tepat[k] -= 1; cocok[i] = True
    sisa = collections.Counter()
    for k, n in sisa_tepat.items():
        if n > 0: sisa[kunci_baseline(*k)] += n
    for i, x in enumerate(masalah):
        k = kunci_baseline(*x)
        if not cocok[i] and sisa[k] > 0:
            sisa[k] -= 1; cocok[i] = True
    warisan = [x for x, c in zip(masalah, cocok) if c]
    baru    = [x for x, c in zip(masalah, cocok) if not c]
    # dengan --mk, entri baseline untuk berkas di luar cakupan tidak dihitung teratasi
    diperiksa = {os.path.relpath(p, ROOT).replace(os.sep, "/") for p in dok}
    teratasi = sum(n for (a, f, m), n in sisa.items() if n > 0 and (not FILTER or f in diperiksa))
    per_baru, per_waris = per_aturan(baru), per_aturan(warisan)
    print(f"**Mode baseline:** `{ARG['--baseline']}` — {len(BASELINE)} entri.\n")
    print(f"**Hasil: {len(baru)} temuan baru** (temuan warisan yang cocok dengan baseline: "
          f"{len(warisan)}; entri baseline yang sudah teratasi: {teratasi}).")
    if teratasi:
        print("\nAda entri baseline yang sudah teratasi: perbarui baseline dengan "
              "`--baseline-tulis` agar tidak menutupi temuan serupa di kemudian hari.")
    if per_baru or per_waris:
        print("\n| Aturan | Nama | Baru | Warisan |\n|---|---|--:|--:|")
        for a in sorted(set(per_baru) | set(per_waris), key=no_aturan):
            print(f"| {a} | {ATURAN.get(a,'')} | {len(per_baru.get(a, []))} "
                  f"| {len(per_waris.get(a, []))} |")
    cetak_rincian(per_baru, " (temuan baru)")
    sys.exit(1 if baru else 0)

if not masalah:
    print("**Hasil: 0 pelanggaran.**"); sys.exit(0)
per = per_aturan(masalah)
print(f"**Hasil: {len(masalah)} pelanggaran.**\n")
print("| Aturan | Nama | Jumlah |\n|---|---|--:|")
for a in sorted(per, key=no_aturan):
    print(f"| {a} | {ATURAN.get(a,'')} | {len(per[a])} |")
cetak_rincian(per)
sys.exit(1)
