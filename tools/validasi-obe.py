#!/usr/bin/env python3
"""Validator konsistensi OBE untuk paket mata kuliah Prodi Informatika UAI.

Menegakkan aturan V1-V12 pada Pedoman OBE & Konvensi (00-pedoman-obe) sec. Q.
Python murni, tanpa dependensi eksternal. Jalankan dari akar repositori:

    python3 tools/validasi-obe.py [--mk INF-101]

Keluar dengan kode 1 bila ada pelanggaran.
"""
import os, re, sys, glob, json

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

# ---------------------------------------------------------------- muat berkas
FILTER = None
if "--mk" in sys.argv:
    FILTER = sys.argv[sys.argv.index("--mk") + 1]
berkas = [p for p in kumpulkan("**/*.md") if "/sumber/" not in p]
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
        print(f"Mata kuliah {FILTER} tidak ditemukan"); sys.exit(2)

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
for p, d in dok.items():
    # buang inline code span agar contoh ilustratif tidak dianggap tautan
    bersih = re.sub(r"`[^`\n]*`", "", d["teks"])
    for tautan in RE_TAUTAN.findall(bersih):
        target = tautan.split("#")[0].strip()
        if not target: continue
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(p), target))):
            lapor("V10", p, f"tautan relatif putus: {target}")

# ------------------------------------------------------------------- laporan
ATURAN = {"V1":"Metadata","V2":"Keunikan id","V3":"Integritas referensial","V4":"Pola kode lama",
          "V5":"Cakupan (constructive alignment)","V6":"Bobot asesmen","V7":"Data induk",
          "V8":"Konvensi","V9":"Sitasi","V10":"Tautan","V11":"Pagu ukuran","V12":"Pengesahan"}
print(f"# Laporan Validasi OBE\n\nBerkas diperiksa: {len(dok)}  |  Mata kuliah: {len(mk_daftar)}\n")
if not masalah:
    print("**Hasil: 0 pelanggaran.**"); sys.exit(0)
per = {}
for a, f, m in masalah: per.setdefault(a, []).append((f, m))
print(f"**Hasil: {len(masalah)} pelanggaran.**\n")
print("| Aturan | Nama | Jumlah |\n|---|---|--:|")
for a in sorted(per, key=lambda x: int(x[1:])):
    print(f"| {a} | {ATURAN.get(a,'')} | {len(per[a])} |")
for a in sorted(per, key=lambda x: int(x[1:])):
    print(f"\n## {a} — {ATURAN.get(a,'')}\n")
    for f, m in per[a][:40]:
        print(f"- `{f}` — {m}")
    if len(per[a]) > 40:
        print(f"- … dan {len(per[a]) - 40} lainnya")
sys.exit(1)
