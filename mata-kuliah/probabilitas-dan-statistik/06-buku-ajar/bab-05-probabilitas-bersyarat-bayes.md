# BAB 5: PROBABILITAS BERSYARAT DAN TEOREMA BAYES

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `PS-Sub-CPMK081-1` | Menerapkan hukum probabilitas total dan Teorema Bayes | C3 |
| `PS-Sub-CPMK081-1` | Menganalisis *base rate fallacy* dan implikasinya pada sistem deteksi | C4 |
| `PS-Sub-CPMK081-1` | Membedakan kejadian saling lepas dan saling bebas | C3–C4 |

---

## 5.1 Hukum Probabilitas Total

### 5.1.1 Gagasan Dasar

Kadang P(A) tidak dapat dihitung langsung, tetapi kita tahu P(A) dalam beberapa **keadaan** berbeda. Hukum probabilitas total menggabungkannya.

Bila B₁, B₂, …, B_k adalah **partisi** ruang sampel (saling lepas dan gabungannya seluruh S):

$$P(A) = \sum_{i=1}^{k} P(B_i) \cdot P(A \mid B_i)$$

```
            S dipartisi menjadi B₁, B₂, B₃
   ┌──────────┬──────────┬──────────┐
   │   B₁     │   B₂     │   B₃     │
   │  ▓▓▓     │  ▓▓▓▓▓   │  ▓       │   ▓ = bagian yang juga A
   └──────────┴──────────┴──────────┘

   P(A) = P(B₁)P(A|B₁) + P(B₂)P(A|B₂) + P(B₃)P(A|B₃)
```

### 5.1.2 Contoh: Tingkat Kegagalan Deployment

> Sebuah tim melakukan *deployment* melalui tiga jalur:

| Jalur | Proporsi | P(gagal) |
|-------|----------|----------|
| CI otomatis | 50% | 2% |
| Manual terjadwal | 30% | 8% |
| Hotfix darurat | 20% | 25% |

$$P(\text{gagal}) = 0{,}50(0{,}02) + 0{,}30(0{,}08) + 0{,}20(0{,}25) = 0{,}084$$

```python
jalur = {
    "CI otomatis":      {"proporsi": 0.50, "p_gagal": 0.02},
    "Manual terjadwal": {"proporsi": 0.30, "p_gagal": 0.08},
    "Hotfix darurat":   {"proporsi": 0.20, "p_gagal": 0.25},
}

p_gagal = sum(d["proporsi"] * d["p_gagal"] for d in jalur.values())
print(f"P(deployment gagal) = {p_gagal:.4f} ({p_gagal*100:.2f}%)\n")

print(f"{'Jalur':<20} {'Kontribusi':>11} {'% kegagalan':>13}")
for nama, d in jalur.items():
    k = d["proporsi"] * d["p_gagal"]
    print(f"{nama:<20} {k:>11.4f} {k/p_gagal*100:>12.1f}%")
```

> **Wawasan yang tidak terlihat dari angka kasar:** hotfix darurat hanya 20% dari *deployment*, tetapi menyumbang **59,5%** dari seluruh kegagalan. Inilah jenis temuan yang membuat probabilitas berguna dalam rekayasa perangkat lunak — ia menunjukkan **di mana perbaikan paling berdampak**.

---

## 5.2 Teorema Bayes

### 5.2.1 Rumus dan Empat Komponennya

$$P(H \mid E) = \frac{P(H) \cdot P(E \mid H)}{P(E)}$$

| Istilah | Lambang | Makna |
|---------|---------|-------|
| **Prior** | P(H) | Keyakinan **sebelum** melihat bukti |
| **Likelihood** | P(E\|H) | Seberapa mungkin bukti muncul bila hipotesis benar |
| **Evidence** | P(E) | Probabilitas bukti muncul secara keseluruhan (normalisasi) |
| **Posterior** | P(H\|E) | Keyakinan **setelah** melihat bukti |

Bentuk lengkap dengan hukum probabilitas total di penyebut:

$$P(B_i \mid A) = \frac{P(B_i) \cdot P(A \mid B_i)}{\sum_{j} P(B_j) \cdot P(A \mid B_j)}$$

> **Inti gagasannya:** Teorema Bayes adalah **mesin untuk memperbarui keyakinan secara rasional ketika bukti baru datang**. Prior masuk, bukti diproses, posterior keluar. Dan posterior hari ini menjadi prior esok hari.

### 5.2.2 Mengapa Teorema Ini Diperlukan

Teorema Bayes menjawab satu kebutuhan praktis: kita **punya** P(E|H) tetapi **butuh** P(H|E).

```
   Yang kita TAHU (dari uji laboratorium):
     P(tes positif | benar-benar sakit) = 0,99      ← likelihood

   Yang kita BUTUHKAN (sebagai pasien):
     P(benar-benar sakit | tes positif) = ?         ← posterior

   Keduanya SANGAT BERBEDA. Bayes menjembataninya.
```

### 5.2.3 Contoh Lengkap: Deteksi Penipuan

> Sistem deteksi penipuan sebuah bank:
> - **Sensitivitas** 98% — transaksi penipuan berhasil ditandai
> - **Spesifisitas** 97% — transaksi normal tidak ditandai (alarm palsu 3%)
> - **Prevalensi** 0,4% — proporsi transaksi yang benar-benar penipuan
>
> Sebuah transaksi ditandai sistem. **Berapa probabilitas ia benar-benar penipuan?**

Banyak orang menjawab "sekitar 98%". Mari hitung.

$$P(\text{tandai}) = \underbrace{0{,}004 \times 0{,}98}_{0{,}00392} + \underbrace{0{,}996 \times 0{,}03}_{0{,}02988} = 0{,}0338$$

$$P(\text{penipuan} \mid \text{tandai}) = \frac{0{,}00392}{0{,}0338} = 0{,}116$$

**Hanya 11,6%.** Hampir sembilan dari sepuluh alarm adalah alarm palsu.

```python
def analisis_diagnostik(prevalensi, sensitivitas, spesifisitas,
                        nama="kondisi", populasi=100_000):
    """Analisis lengkap sebuah tes diagnostik."""
    ada, tidak = populasi * prevalensi, populasi * (1 - prevalensi)
    bp = ada * sensitivitas
    sn = ada * (1 - sensitivitas)
    sp = tidak * (1 - spesifisitas)
    bn = tidak * spesifisitas

    ppv = bp / (bp + sp)
    npv = bn / (bn + sn)

    print(f"=== {nama.upper()} ===")
    print(f"{'':>20} {'Tes POSITIF':>13} {'Tes NEGATIF':>13}")
    print(f"{'Kondisi ADA':>20} {bp:>13,.0f} {sn:>13,.0f}")
    print(f"{'Kondisi TIDAK ADA':>20} {sp:>13,.0f} {bn:>13,.0f}")
    print(f"\nPPV — P({nama} | positif) = {ppv:.4f} ({ppv*100:.2f}%)")
    print(f"NPV — P(bukan | negatif)  = {npv:.4f} ({npv*100:.2f}%)")
    print(f"→ Dari {bp+sp:,.0f} alarm, {sp:,.0f} "
          f"({sp/(bp+sp)*100:.1f}%) adalah ALARM PALSU.")
    return ppv, npv

analisis_diagnostik(0.004, 0.98, 0.97, nama="penipuan")
```

---

## 5.3 *Base Rate Fallacy*

### 5.3.1 Mengapa Hasilnya Mengejutkan

Kuncinya ada pada **prevalensi yang sangat rendah**. Bayangkan 100.000 transaksi:

```
  100.000 transaksi
  ├── 400 penipuan (0,4%)
  │    ├── 392 ditandai   ✓ benar positif
  │    └──   8 lolos      ✗ salah negatif
  └── 99.600 normal (99,6%)
       ├──  2.988 ditandai ✗ ALARM PALSU
       └── 96.612 lolos    ✓ benar negatif

  Total ditandai = 392 + 2.988 = 3.380
  Yang benar penipuan = 392 / 3.380 = 11,6%
```

Meskipun tingkat alarm palsu hanya 3%, **3% dari kelompok yang sangat besar** menghasilkan lebih banyak alarm palsu daripada seluruh kasus penipuan yang ada.

> ***Base rate fallacy*** adalah kecenderungan mengabaikan prevalensi dan hanya memperhatikan akurasi tes.
>
> Ini bukan kuriositas akademis. Ini adalah kesalahan penalaran yang menyebabkan **diagnosis medis yang keliru**, **penangkapan salah berbasis pengenalan wajah**, dan **sistem keamanan yang diabaikan karena terlalu sering berteriak serigala**.

### 5.3.2 Pengaruh Prevalensi

```python
import numpy as np
import matplotlib.pyplot as plt

sens, spes = 0.98, 0.97
prev = np.linspace(0.0005, 0.5, 400)
ppv = (prev*sens) / (prev*sens + (1-prev)*(1-spes))

plt.figure(figsize=(10, 5.5))
plt.plot(prev*100, ppv*100, linewidth=2.2, color="steelblue")
plt.axhline(50, color="gray", linestyle=":")
plt.axvline(0.4, color="#c0392b", linestyle="--",
            label="Prevalensi penipuan (0,4%)")
plt.xlabel("Prevalensi kondisi (%)")
plt.ylabel("PPV — P(kondisi | tes positif) (%)")
plt.title("Tes yang SAMA, kepercayaan yang sangat berbeda")
plt.legend(); plt.grid(alpha=0.3); plt.tight_layout(); plt.show()

print(f"{'Prevalensi':>12}  {'PPV':>8}")
for p in [0.001, 0.004, 0.01, 0.05, 0.10, 0.30, 0.50]:
    v = (p*sens) / (p*sens + (1-p)*(1-spes))
    print(f"{p*100:>11.1f}%  {v*100:>7.1f}%")
```

### 5.3.3 Sensitivitas atau Spesifisitas?

Pada prevalensi rendah, mana yang lebih berpengaruh untuk dinaikkan?

```python
import numpy as np

prev = 0.004
sens_dasar, spes_dasar = 0.98, 0.97

def ppv(prev, sens, spes):
    return (prev*sens) / (prev*sens + (1-prev)*(1-spes))

print(f"PPV dasar                      : {ppv(prev, 0.98, 0.97)*100:.2f}%")
print(f"Sensitivitas 0,98 → 0,999      : {ppv(prev, 0.999, 0.97)*100:.2f}%")
print(f"Spesifisitas 0,97 → 0,999      : {ppv(prev, 0.98, 0.999)*100:.2f}%")
print("\n→ Menaikkan SPESIFISITAS jauh lebih berpengaruh.")
```

> **Implikasi perancangan sistem:** menaikkan akurasi model saja tidak cukup bila kejadian yang dicari sangat langka. Anda harus menaikkan **spesifisitas** secara drastis, **atau** menerima bahwa sebagian besar alarm akan palsu dan merancang alur kerja manusia yang sanggup menanganinya.
>
> Topik ini akan Anda temui lagi pada **Dasar Kecerdasan Artifisial dan Pembelajaran Mesin** (Semester 5) dengan nama *precision-recall tradeoff*.

### 5.3.4 Menaikkan Prevalensi: Strategi yang Sering Terlupakan

Ada cara ketiga yang sering lebih murah: **jangan menerapkan tes pada seluruh populasi**.

Bila tes penyakit hanya diberikan kepada orang yang **sudah menunjukkan gejala**, prevalensi pada kelompok itu jauh lebih tinggi — misalnya 20% alih-alih 0,1% — sehingga PPV melonjak dari 9% ke 89% tanpa mengubah tesnya sama sekali.

Padanannya dalam Informatika: **jangan memindai seluruh lalu lintas jaringan dengan model berat**; saring dulu dengan aturan murah, lalu terapkan model pada subkelompok yang sudah mencurigakan.

---

## 5.4 Kebebasan Dua Kejadian

### 5.4.1 Definisi Formal

Dua kejadian A dan B **saling bebas** (*independent*) bila:

$$P(A \cap B) = P(A) \cdot P(B)$$

Setara dengan: **P(A|B) = P(A)** — mengetahui B **tidak mengubah** keyakinan kita tentang A.

### 5.4.2 Bebas ≠ Saling Lepas

| Sifat | Definisi | Makna Intuitif |
|-------|----------|----------------|
| **Saling lepas** | P(A ∩ B) = 0 | Tidak mungkin terjadi bersamaan |
| **Saling bebas** | P(A ∩ B) = P(A)P(B) | Satu tidak memengaruhi yang lain |

> **Fakta yang sering mengejutkan:** dua kejadian berprobabilitas tak nol yang **saling lepas** justru **tidak mungkin saling bebas**.
>
> Sebabnya: bila A terjadi, kita jadi tahu **pasti** B tidak terjadi. Itu jelas memengaruhi.

```python
# Contoh: status HTTP 200 dan 404 pada satu permintaan
p_200, p_404 = 0.90, 0.06
p_irisan = 0.0                     # saling lepas

print(f"Saling lepas? {p_irisan == 0}")
print(f"P(A)P(B) = {p_200*p_404:.4f}, tetapi P(A∩B) = {p_irisan}")
print("→ Saling lepas, TETAPI TIDAK bebas.")
```

### 5.4.3 Keandalan Sistem

Bila n komponen bekerja **secara bebas**, masing-masing dengan keandalan r:

$$P(\text{seri — semua bekerja}) = r^n \qquad P(\text{paralel — cukup satu}) = 1 - (1-r)^n$$

```python
def keandalan(r, n, susunan="seri"):
    return r**n if susunan == "seri" else 1 - (1-r)**n

r = 0.99
print("SERI (semua harus hidup — rantai layanan):")
for n in [1, 2, 3, 5, 10, 20]:
    print(f"  {n:>2} komponen: {keandalan(r, n, 'seri')*100:8.4f}%")

print("\nPARALEL (cukup satu hidup — replika):")
for n in [1, 2, 3, 5]:
    print(f"  {n:>2} komponen: {keandalan(r, n, 'paralel')*100:10.6f}%")
```

**Dua wawasan rekayasa:**

1. Menambah komponen pada susunan **seri menurunkan** keandalan. Sepuluh layanan yang masing-masing andal 99% dan harus semuanya hidup hanya memberi keandalan **90,4%**.
2. Menambah komponen pada susunan **paralel menaikkannya secara dramatis**. Tiga replika 99% memberi 99,9999%.

> **Peringatan yang paling penting.** Perhitungan ini mengandaikan komponen **benar-benar bebas**.
>
> Pada kenyataannya, tiga replika di satu pusat data akan mati bersamaan bila listriknya padam. Ini disebut ***correlated failure***, dan merupakan penyebab banyak kegagalan sistem besar — karena tim merasa "sudah aman" berdasarkan perhitungan yang asumsinya keliru.
>
> Pelajaran: **asumsi kebebasan harus diperiksa, bukan diandaikan.** Sama seperti asumsi statistik lainnya.

---

## 5.5 Penerapan: Penyaring Spam Naive Bayes

### 5.5.1 Gagasannya

Untuk pesan berisi kata-kata w₁, …, wₙ:

$$P(\text{spam} \mid w_1,\ldots,w_n) \propto P(\text{spam}) \times \prod_{i=1}^{n} P(w_i \mid \text{spam})$$

Disebut ***naive*** karena mengandaikan setiap kata **saling bebas** bila kelasnya diketahui — asumsi yang jelas salah (kata "gratis" dan "hadiah" cenderung muncul bersama), tetapi ternyata bekerja sangat baik dalam praktik.

### 5.5.2 Implementasi

```python
from collections import Counter
import math

def latih(dokumen, label):
    """Melatih Naive Bayes dengan penghalusan Laplace."""
    prior, likelihood, total, kosakata = {}, {}, {}, set()
    for k in set(label):
        teks = [d for d, l in zip(dokumen, label) if l == k]
        prior[k] = len(teks) / len(dokumen)
        kata = [w for d in teks for w in d.lower().split()]
        likelihood[k] = Counter(kata)
        total[k] = len(kata)
        kosakata.update(kata)
    return prior, likelihood, total, kosakata

def klasifikasi(pesan, prior, likelihood, total, kosakata, alpha=1.0):
    """Mengklasifikasi pesan; memakai log agar tidak underflow."""
    V = len(kosakata)
    skor = {}
    for k in prior:
        log_p = math.log(prior[k])
        for w in pesan.lower().split():
            p_w = (likelihood[k][w] + alpha) / (total[k] + alpha * V)
            log_p += math.log(p_w)
        skor[k] = log_p
    return max(skor, key=skor.get), skor

dokumen = [
    "selamat anda memenangkan hadiah gratis klik sekarang",
    "promo gratis diskon besar klik tautan ini sekarang",
    "menangkan hadiah undian gratis segera daftar",
    "rapat proyek besok pukul sembilan di ruang lab",
    "tolong kirim laporan praktikum sebelum jumat",
    "jadwal kuliah statistika pindah ke ruang tiga nol satu",
]
label = ["spam"]*3 + ["ham"]*3

model = latih(dokumen, label)
for pesan in ["gratis hadiah klik sekarang", "laporan praktikum besok"]:
    hasil, skor = klasifikasi(pesan, *model)
    print(f'"{pesan}" → {hasil.upper()}')
```

### 5.5.3 Mengapa Penghalusan Laplace Diperlukan

Tanpa penghalusan, satu kata yang tidak pernah muncul dalam kelas tertentu membuat seluruh perkalian menjadi **nol** — sebuah pesan otomatis ditolak dari kelas itu, betapapun kuat bukti dari kata-kata lain.

Penghalusan Laplace menambahkan α (biasanya 1) ke setiap hitungan, sehingga tidak ada probabilitas yang persis nol.

> Pada Semester 5, mata kuliah **Dasar Kecerdasan Artifisial dan Pembelajaran Mesin** akan memakai `sklearn.naive_bayes.MultinomialNB` — yang di dalamnya persis menjalankan perhitungan ini, termasuk parameter `alpha` untuk penghalusan. Memahami mekanismenya sekarang berarti Anda kelak memanggil fungsi itu **dengan sadar**, bukan sebagai kotak hitam.

---

## AI Corner — Tingkat Menengah

### Teorema Bayes adalah Jantung Banyak Sistem AI

Setiap kali Anda melihat sebuah sistem AI memberi skor keyakinan — "87% yakin ini kucing", "risiko penipuan: tinggi" — di baliknya ada penalaran yang secara konseptual bersifat Bayesian: menggabungkan bukti dengan keyakinan awal.

Dan setiap kali sistem seperti itu dievaluasi, **base rate fallacy mengintai**.

### Kasus Nyata: Pengenalan Wajah

> Sebuah sistem pengenalan wajah diklaim akurat 99,9%. Ia dipasang di stasiun untuk mencari 1 buronan di antara 1 juta penumpang per bulan.

```python
prev = 1 / 1_000_000
sens = spes = 0.999

bp = prev * sens
sp = (1 - prev) * (1 - spes)
ppv = bp / (bp + sp)

print(f"Dari 1 juta penumpang:")
print(f"  Buronan tertangkap  : {bp*1_000_000:.4f}")
print(f"  Alarm palsu         : {sp*1_000_000:,.0f}")
print(f"  PPV                 : {ppv*100:.6f}%")
print(f"\n→ Sekitar 1.000 orang tak bersalah dihentikan")
print(f"  untuk setiap 1 buronan yang tertangkap.")
```

> **Ini bukan kritik terhadap teknologinya.** Sistemnya memang akurat 99,9%. Yang keliru adalah **penerapannya pada populasi dengan prevalensi sangat rendah**, dan **cara hasilnya dikomunikasikan** kepada publik.
>
> Seorang sarjana Informatika yang memahami Bab ini akan mengajukan pertanyaan yang tepat sebelum sistem seperti itu diterapkan.

### Kesalahan Khas AI pada Soal Bayes

Minta sebuah asisten AI mengerjakan soal deteksi penipuan di §5.2.3. Perhatikan:

1. Apakah ia mengidentifikasi prevalensi sebagai prior dengan benar?
2. Apakah ia menghitung P(E) dengan hukum probabilitas total, atau melewatkan bagian alarm palsu?
3. Apakah ia **memperingatkan** tentang implikasi praktis hasilnya, atau berhenti pada angka?

Model yang baik biasanya benar pada butir 1 dan 2. Butir 3 hampir selalu memerlukan pertanyaan lanjutan dari Anda.

### Pemakaian yang Dianjurkan

```
PROMPT YANG BAIK:
"Saya menghitung PPV = 11,6% untuk sistem deteksi penipuan dengan
 sensitivitas 98%, spesifisitas 97%, prevalensi 0,4%. Apakah perhitungan
 saya benar? Dan menurutmu, apa konsekuensi operasional dari angka itu
 bagi tim yang harus meninjau setiap alarm?"

Mengapa baik: Anda sudah menghitung, dan pertanyaan kedua mendorong
AI keluar dari mode "kalkulator" menuju pertimbangan praktis.
```

---

## Latihan Soal

### Tingkat Dasar

1. Tuliskan Teorema Bayes dan sebutkan keempat komponennya beserta maknanya.

2. Sebuah perusahaan memperoleh laporan bug dari tiga sumber: pengguna (60%, 15% valid), pengujian otomatis (30%, 80% valid), dan tim QA (10%, 95% valid). Hitung P(sebuah laporan valid).

3. Untuk data soal 2, bila sebuah laporan diketahui **valid**, berapa probabilitas ia berasal dari pengguna?

4. Jelaskan perbedaan "saling lepas" dan "saling bebas" dengan satu contoh masing-masing.

5. Tiga server disusun paralel, masing-masing andal 95%. Hitung keandalan sistem. Bandingkan dengan susunan seri.

### Tingkat Menengah

6. Sebuah tes penyakit memiliki sensitivitas 99% dan spesifisitas 99%. Penyakitnya menjangkiti 1 dari 1.000 orang.
   (a) Hitung P(sakit | tes positif).
   (b) Gambarkan diagram pohon dari 100.000 orang.
   (c) Jelaskan mengapa hasilnya jauh di bawah 99%.
   (d) Bila tes hanya diberikan kepada orang bergejala (prevalensi 15%), hitung ulang PPV-nya.
   (e) Bandingkan (a) dan (d). Apa pelajarannya bagi perancangan program skrining?

7. Sebuah sistem pemindai kerentanan memiliki sensitivitas 96% dan spesifisitas 92%. Dari 50.000 berkas dalam basis kode, 1,5% benar-benar rentan.
   (a) Berapa alarm yang akan muncul?
   (b) Berapa persen di antaranya palsu?
   (c) Berapa kerentanan nyata yang terlewat?
   (d) Bila tim hanya sanggup meninjau 200 alarm per minggu, berapa lama waktu yang dibutuhkan?
   (e) Usulkan dua perbaikan dan jelaskan mana yang lebih berdampak.

8. Buktikan bahwa dua kejadian berprobabilitas tak nol yang saling lepas tidak mungkin saling bebas.

9. Sebuah layanan terdiri dari 8 mikroservis yang harus semuanya hidup. Masing-masing andal 99,5%.
   (a) Hitung keandalan sistem.
   (b) Berapa menit per bulan sistem diperkirakan mati?
   (c) Berapa keandalan minimum tiap mikroservis agar sistem mencapai 99,9%?
   (d) Diskusikan: apakah asumsi kebebasan realistis? Beri satu contoh pelanggarannya.

### Tingkat Mahir

10. Sebuah sistem pengenalan wajah dengan sensitivitas dan spesifisitas 99,9% dipasang untuk mencari 5 buronan di antara 2 juta penumpang bulanan.
    (a) Hitung jumlah alarm, alarm palsu, dan PPV.
    (b) Berapa orang tak bersalah dihentikan per buronan tertangkap?
    (c) Berapa spesifisitas yang dibutuhkan agar PPV mencapai 50%?
    (d) Apakah angka itu realistis secara teknis?
    (e) Tulislah paragraf singkat berisi rekomendasi Anda sebagai konsultan teknis, dengan mempertimbangkan aspek etis.

11. Bangun penyaring Naive Bayes lengkap untuk klasifikasi teks berbahasa Indonesia.
    (a) Implementasikan dari nol dengan penghalusan Laplace.
    (b) Uji pada dataset `email_spam_indonesia.csv` dengan pembagian 80:20.
    (c) Hitung matriks konfusi, presisi, recall, dan F1.
    (d) Bandingkan hasil dengan `sklearn.naive_bayes.MultinomialNB`.
    (e) Jelaskan: mengapa presisi dan recall adalah probabilitas bersyarat dengan arah berbeda? Kaitkan dengan PPV dan sensitivitas.

12. Tulislah esai singkat (400–500 kata): *"Mengapa base rate fallacy adalah masalah etika, bukan sekadar masalah matematika?"* Sertakan sekurang-kurangnya dua contoh nyata dan kaitkan dengan tanggung jawab seorang sarjana Informatika.

---

## Rangkuman

1. **Hukum probabilitas total** menggabungkan probabilitas dari beberapa keadaan yang mempartisi ruang sampel.
2. **Teorema Bayes** membalik arah persyaratan: dari P(E|H) yang kita punya menjadi P(H|E) yang kita butuhkan.
3. Empat komponennya: **prior, likelihood, evidence, posterior**. Posterior hari ini menjadi prior esok hari.
4. ***Base rate fallacy*** membuat tes akurat 98–99% tetap menghasilkan mayoritas alarm palsu bila kejadiannya langka.
5. Pada prevalensi rendah, **menaikkan spesifisitas jauh lebih berpengaruh** daripada sensitivitas.
6. Strategi ketiga yang sering terlupakan: **menaikkan prevalensi** dengan menyaring populasi terlebih dahulu.
7. **Saling lepas ≠ saling bebas.** Dua kejadian berprobabilitas tak nol yang saling lepas pasti tidak bebas.
8. **Keandalan seri menurun**, **paralel meningkat** seiring bertambahnya komponen.
9. Asumsi kebebasan yang keliru (*correlated failure*) adalah penyebab umum kegagalan sistem besar.
10. **Naive Bayes** adalah penerapan langsung Teorema Bayes dengan asumsi kebebasan antar kata — asumsi yang salah tetapi berguna.

---

## Referensi

1. Walpole, R. E., et al. (2016). *Probability and Statistics for Engineers and Scientists* (9th ed.), Bab 2.7–2.8. Pearson.
2. Downey, A. B. (2013). *Think Bayes*. O'Reilly Media.
3. Kahneman, D., & Tversky, A. (1973). On the psychology of prediction. *Psychological Review*, 80(4), 237–251.
4. Gigerenzer, G. (2002). *Calculated Risks: How to Know When Numbers Deceive You*. Simon & Schuster.
5. Buolamwini, J., & Gebru, T. (2018). Gender Shades. *Proceedings of Machine Learning Research*, 81, 1–15.
6. Ross, S. M. (2019). *A First Course in Probability* (10th ed.), Bab 3. Pearson.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
