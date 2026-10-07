# Minggu 11: Uji Hipotesis Satu Sampel

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Probabilitas dan Statistik (IF52510033) |
| **Minggu ke-** | 11 |
| **Topik** | Hipotesis nol dan alternatif, galat Tipe I/II, uji-z dan uji-t satu sampel, *p-value* |
| **CPL / CPMK** | CPL08 / CPMK081 |
| **Sub-CPMK** | `PS-Sub-CPMK081-1` |
| **Indikator Mingguan** | Merumuskan dan menguji hipotesis satu sampel, serta menafsirkan *p-value* dan galat Tipe I/II |
| **Level Bloom** | C3–C4 (Menerapkan–Menganalisis) |
| **Durasi** | 150 menit tatap muka |
| **Metode** | Kuliah, latihan terbimbing, diskusi etika pelaporan |

---

## Tujuan Pembelajaran

Setelah mengikuti perkuliahan minggu ini, mahasiswa mampu:

1. **Merumuskan** (C3) hipotesis nol dan alternatif dari sebuah pernyataan masalah.
2. **Membedakan** (C2) galat Tipe I dan Tipe II serta menjelaskan konsekuensinya dalam konteks nyata.
3. **Melakukan** (C3) uji-z dan uji-t satu sampel, termasuk memeriksa asumsinya.
4. **Menafsirkan** (C4) *p-value* secara benar dan mengenali lima salah tafsir yang paling umum.
5. **Membedakan** (C4) signifikansi statistik dan signifikansi praktis.

---

## Materi Pembelajaran

### 1. Kerangka Uji Hipotesis

#### 1.1 Logika Dasarnya

Uji hipotesis bekerja dengan **bukti tidak langsung**, mirip praktik peradilan:

```
  PERADILAN                        UJI HIPOTESIS
  ─────────                        ─────────────
  Terdakwa dianggap                H₀ dianggap benar
  tidak bersalah                   sampai ada bukti kuat

  Jaksa menghadirkan bukti         Data dikumpulkan

  "Bukti cukup kuat untuk          "Data cukup ekstrem sehingga
   menolak praduga?"                H₀ sulit dipercaya?"

  Bila ya   → bersalah             Bila ya   → tolak H₀
  Bila tidak→ tidak terbukti       Bila tidak→ gagal menolak H₀
              bersalah                        (BUKAN: H₀ terbukti benar)
```

> **Yang paling sering disalahpahami:** "gagal menolak H₀" **tidak berarti H₀ benar**. Sama seperti "tidak terbukti bersalah" tidak berarti "terbukti tidak bersalah". Bisa saja buktinya memang kurang.

#### 1.2 Merumuskan Hipotesis

| Komponen | Lambang | Sifat |
|----------|---------|-------|
| **Hipotesis nol** | H₀ | Pernyataan "tidak ada efek/perbedaan"; selalu memuat tanda sama dengan |
| **Hipotesis alternatif** | H₁ atau Hₐ | Yang ingin dibuktikan; memuat ≠, >, atau < |

| Jenis Uji | H₀ | H₁ | Kapan dipakai |
|-----------|-----|-----|---------------|
| Dua sisi | μ = μ₀ | μ ≠ μ₀ | Peduli pada perbedaan ke arah mana pun |
| Satu sisi kanan | μ ≤ μ₀ | μ > μ₀ | Hanya peduli bila lebih besar |
| Satu sisi kiri | μ ≥ μ₀ | μ < μ₀ | Hanya peduli bila lebih kecil |

> **Aturan penting:** arah hipotesis harus ditetapkan **sebelum melihat data**. Memilih arah setelah melihat hasil adalah bentuk kecurangan statistik yang disebut *HARKing* (*Hypothesizing After the Results are Known*).

**Contoh perumusan:**

> *Masalah:* Tim klaim bahwa optimasi baru membuat waktu respons API turun di bawah 200 ms. Data lama menunjukkan rata-rata 214 ms.

$$H_0: \mu \ge 200 \text{ ms} \qquad H_1: \mu < 200 \text{ ms}$$

Uji satu sisi kiri, karena klaimnya spesifik tentang penurunan.

---

### 2. Galat Tipe I dan Tipe II

|  | **H₀ sebenarnya BENAR** | **H₀ sebenarnya SALAH** |
|--|--------------------------|--------------------------|
| **Menolak H₀** | ❌ **Galat Tipe I** (α)<br>*false positive* | ✅ Keputusan benar<br>(kuasa uji = 1 − β) |
| **Gagal menolak H₀** | ✅ Keputusan benar | ❌ **Galat Tipe II** (β)<br>*false negative* |

#### 2.1 Konsekuensi dalam Konteks Nyata

| Konteks | Galat Tipe I | Galat Tipe II |
|---------|--------------|---------------|
| Uji obat | Menyetujui obat yang tidak manjur | Menolak obat yang sebenarnya manjur |
| Deteksi penipuan | Memblokir transaksi sah | Meloloskan penipuan |
| Uji fitur baru (A/B test) | Merilis fitur yang tidak lebih baik | Membatalkan fitur yang sebenarnya lebih baik |
| Deteksi kerentanan | Alarm palsu, tim lelah | Kerentanan nyata terlewat |

> **Pilihan α adalah keputusan nilai, bukan keputusan matematis.** Dalam pengujian keamanan penerbangan, galat Tipe II jauh lebih berbahaya, sehingga α dibuat longgar. Dalam uji obat, galat Tipe I lebih berbahaya, sehingga α dibuat ketat. Menetapkan α = 0,05 secara otomatis tanpa memikirkan konteksnya adalah kebiasaan, bukan penalaran.

#### 2.2 Kuasa Uji

**Kuasa uji** = 1 − β = probabilitas menolak H₀ ketika H₀ memang salah.

```python
import numpy as np
from scipy import stats

def kuasa_uji_t(n, efek, sigma, alpha=0.05, dua_sisi=True):
    """Menghitung kuasa uji-t satu sampel.

    efek : selisih sebenarnya antara μ dan μ₀
    """
    se = sigma / np.sqrt(n)
    df = n - 1
    delta = efek / se                       # parameter non-sentralitas
    if dua_sisi:
        t_kritis = stats.t.ppf(1 - alpha/2, df)
        kuasa = (stats.nct.sf(t_kritis, df, delta) +
                 stats.nct.cdf(-t_kritis, df, delta))
    else:
        t_kritis = stats.t.ppf(1 - alpha, df)
        kuasa = stats.nct.sf(t_kritis, df, delta)
    return kuasa

sigma, efek = 35, 10   # ingin mendeteksi selisih 10 ms

print("Kuasa uji menurut ukuran sampel (α = 0,05, efek = 10 ms, σ = 35 ms):")
for n in [10, 20, 30, 50, 100, 200]:
    k = kuasa_uji_t(n, efek, sigma)
    tanda = " ✓" if k >= 0.80 else ""
    print(f"  n = {n:>4}  →  kuasa = {k:.4f}{tanda}")
print("\n→ Konvensi umum: kuasa minimal 0,80 (β ≤ 0,20).")
```

> **Studi dengan kuasa rendah adalah pemborosan.** Bila kuasa hanya 0,30, maka meskipun efeknya nyata, Anda punya 70% kemungkinan tidak menemukannya. Hasil "tidak signifikan" dari studi berkuasa rendah **tidak memberi informasi apa pun**.

---

### 3. Uji-t Satu Sampel

#### 3.1 Prosedur Lengkap

$$t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}, \quad df = n - 1$$

**Enam langkah baku:**

1. Rumuskan H₀ dan H₁ (**sebelum melihat data**).
2. Tetapkan α.
3. **Periksa asumsi.**
4. Hitung statistik uji.
5. Hitung *p-value* atau bandingkan dengan nilai kritis.
6. Ambil keputusan dan **tafsirkan dalam konteks**.

#### 3.2 Asumsi yang Wajib Diperiksa

| Asumsi | Cara memeriksa | Bila dilanggar |
|--------|----------------|----------------|
| Sampel acak dan bebas | Telaah cara pengumpulan data | Tidak ada perbaikan statistik — data harus dikumpulkan ulang |
| Skala interval/rasio | Telaah jenis variabel | Gunakan uji nonparametrik |
| Kenormalan (untuk n kecil) | Q-Q plot, Shapiro-Wilk | Gunakan Wilcoxon signed-rank |
| Tidak ada pencilan ekstrem | Boxplot | Telaah pencilan; pertimbangkan uji robust |

> Untuk n ≥ 30, CLT membuat uji-t cukup tahan terhadap pelanggaran kenormalan ringan. Untuk n kecil, kenormalan benar-benar penting.

#### 3.3 Implementasi Lengkap

```python
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

def uji_t_satu_sampel(data, mu0, alpha=0.05, arah="dua sisi"):
    """Uji-t satu sampel lengkap dengan pemeriksaan asumsi dan ukuran efek."""
    data = np.asarray(data)
    data = data[~np.isnan(data)]
    n = len(data)
    x_bar, s = data.mean(), data.std(ddof=1)
    se = s / np.sqrt(n)
    t_stat = (x_bar - mu0) / se
    df = n - 1

    # p-value sesuai arah hipotesis
    if arah == "dua sisi":
        p = 2 * stats.t.sf(abs(t_stat), df)
    elif arah == "kanan":
        p = stats.t.sf(t_stat, df)
    else:                       # kiri
        p = stats.t.cdf(t_stat, df)

    # Ukuran efek Cohen's d
    d = (x_bar - mu0) / s
    besar_efek = ("kecil" if abs(d) < 0.5 else
                  "sedang" if abs(d) < 0.8 else "besar")

    # Interval kepercayaan
    t_kritis = stats.t.ppf(1 - alpha/2, df)
    ik = (x_bar - t_kritis*se, x_bar + t_kritis*se)

    # Pemeriksaan asumsi kenormalan
    if 3 <= n <= 5000:
        _, p_normal = stats.shapiro(data)
    else:
        p_normal = np.nan

    print("=" * 58)
    print(f"UJI-T SATU SAMPEL  (arah: {arah})")
    print("=" * 58)
    print(f"H₀: μ = {mu0}")
    print(f"H₁: μ {'≠' if arah=='dua sisi' else ('>' if arah=='kanan' else '<')} {mu0}")
    print(f"\n--- PEMERIKSAAN ASUMSI ---")
    print(f"n                    : {n}")
    print(f"Shapiro-Wilk p-value : {p_normal:.4f} "
          f"{'(kenormalan wajar)' if p_normal > 0.05 else '(menyimpang dari Normal)'}")
    if n >= 30:
        print("n ≥ 30, CLT membuat uji-t cukup tahan terhadap penyimpangan ringan.")
    print(f"\n--- HASIL ---")
    print(f"Rata-rata sampel     : {x_bar:.4f}")
    print(f"Simpangan baku       : {s:.4f}")
    print(f"Galat baku           : {se:.4f}")
    print(f"Statistik t          : {t_stat:.4f}  (df = {df})")
    print(f"p-value              : {p:.6f}")
    print(f"IK {(1-alpha)*100:.0f}%              : [{ik[0]:.4f} , {ik[1]:.4f}]")
    print(f"Cohen's d            : {d:.4f}  (efek {besar_efek})")
    print(f"\n--- KEPUTUSAN (α = {alpha}) ---")
    if p < alpha:
        print(f"p = {p:.6f} < α = {alpha}  →  TOLAK H₀")
        print("Ada bukti statistik yang cukup untuk mendukung H₁.")
    else:
        print(f"p = {p:.6f} ≥ α = {alpha}  →  GAGAL MENOLAK H₀")
        print("Bukti tidak cukup untuk mendukung H₁.")
        print("CATATAN: ini BUKAN berarti H₀ terbukti benar.")
    return {"t": t_stat, "p": p, "d": d, "ik": ik}

# Kasus: apakah rata-rata jam belajar berbeda dari 12 jam per minggu?
df_data = pd.read_csv("nilai_mahasiswa_if.csv")
uji_t_satu_sampel(df_data["jam_belajar"], mu0=12, arah="dua sisi")
```

---

### 4. Memahami *p-value* dengan Benar

#### 4.1 Definisi yang Tepat

> ***p-value*** adalah probabilitas memperoleh data **seekstrem ini atau lebih ekstrem**, **bila H₀ benar**.

$$p = P(\text{data seekstrem ini} \mid H_0 \text{ benar})$$

#### 4.2 Lima Salah Tafsir yang Paling Umum

| No | Pernyataan | Status | Penjelasan |
|----|-----------|--------|------------|
| 1 | "p = 0,03 berarti ada 3% probabilitas H₀ benar" | ❌ **SALAH** | *p-value* adalah P(data \| H₀), bukan P(H₀ \| data). Ini kekeliruan membalik arah persyaratan — sama seperti pada Minggu 5 |
| 2 | "p = 0,03 berarti ada 97% probabilitas H₁ benar" | ❌ **SALAH** | Alasan yang sama |
| 3 | "p < 0,05 berarti efeknya besar dan penting" | ❌ **SALAH** | *p-value* dipengaruhi ukuran sampel. Efek sangat kecil menjadi "signifikan" bila n besar |
| 4 | "p = 0,06 berarti tidak ada efek" | ❌ **SALAH** | Ambang 0,05 bersifat konvensi. p = 0,06 dan p = 0,04 hampir tidak berbeda maknanya |
| 5 | "Hasil yang signifikan pasti dapat direplikasi" | ❌ **SALAH** | *p-value* tidak mengukur replikabilitas |

> ✅ **Tafsir yang benar:** "Bila benar tidak ada perbedaan, maka data seekstrem ini hanya akan muncul pada 3% dari pengulangan penelitian. Karena itu kami menganggap H₀ kurang layak dipercaya."

#### 4.3 Pernyataan ASA 2016

American Statistical Association menerbitkan enam prinsip tentang *p-value*:

1. *p-value* dapat menunjukkan seberapa tidak cocok data dengan model statistik tertentu.
2. *p-value* **bukan** ukuran probabilitas bahwa hipotesis yang diteliti benar.
3. Kesimpulan ilmiah **tidak boleh** hanya didasarkan pada apakah *p-value* melewati ambang tertentu.
4. Inferensi yang baik menuntut **pelaporan yang lengkap dan transparan**.
5. *p-value* **tidak mengukur besarnya efek** maupun pentingnya suatu hasil.
6. *p-value* saja **tidak memberikan ukuran bukti** yang baik tentang sebuah model atau hipotesis.

#### 4.4 Efek Ukuran Sampel terhadap *p-value*

```python
import numpy as np
from scipy import stats

rng = np.random.default_rng(42)

# Efek yang sangat kecil dan tidak penting secara praktis: 0,5 ms
mu_sebenarnya, mu0, sigma = 200.5, 200, 35

print("Efek sebenarnya hanya 0,5 ms — tidak berarti secara praktis.")
print(f"{'n':>8}  {'p-value':>12}  {'Cohen d':>9}  Kesimpulan")
for n in [30, 100, 1_000, 10_000, 100_000, 1_000_000]:
    sampel = rng.normal(mu_sebenarnya, sigma, n)
    t, p = stats.ttest_1samp(sampel, mu0)
    d = (sampel.mean() - mu0) / sampel.std(ddof=1)
    status = "SIGNIFIKAN" if p < 0.05 else "tidak signifikan"
    print(f"{n:>8}  {p:>12.6f}  {d:>9.4f}  {status}")

print("\n→ Dengan n cukup besar, efek 0,5 ms yang tidak berguna")
print("  tetap menjadi 'signifikan secara statistik'.")
print("→ Karena itu SELALU laporkan ukuran efek, bukan hanya p-value.")
```

---

### 5. Signifikansi Statistik vs Signifikansi Praktis

| Aspek | Signifikansi Statistik | Signifikansi Praktis |
|-------|------------------------|----------------------|
| Pertanyaan | "Apakah efeknya nyata, bukan kebetulan?" | "Apakah efeknya cukup besar untuk diperhatikan?" |
| Diukur dengan | *p-value* | Ukuran efek, interval kepercayaan |
| Dipengaruhi n | **Ya, sangat** | Tidak |
| Menentukan keputusan? | Tidak sendirian | Ya, bersama konteks |

**Ukuran efek Cohen's d:**

| \|d\| | Tafsir |
|-------|--------|
| < 0,2 | Sangat kecil |
| 0,2 – 0,5 | Kecil |
| 0,5 – 0,8 | Sedang |
| > 0,8 | Besar |

> **Praktik pelaporan yang baik** menyertakan empat hal sekaligus: statistik uji, *p-value*, **ukuran efek**, dan **interval kepercayaan**. Melaporkan *p-value* saja adalah praktik yang sudah ditinggalkan di banyak bidang ilmu.

---

## Kegiatan Pembelajaran

### Sebelum Kelas (Mandiri — 60 menit)

1. Membaca [Bab 10 buku ajar](../06-buku-ajar/bab-10-uji-hipotesis-satu-sampel.md).
2. **Mencari satu klaim** dari berita atau iklan yang memakai kata "terbukti secara statistik" atau sejenisnya. Simpan tautannya.

### Di Kelas (150 menit)

| Waktu | Kegiatan |
|-------|----------|
| 0–10' | Pembahasan Kuis 3 |
| 10–40' | Kuliah: kerangka uji hipotesis; analogi peradilan; perumusan H₀ dan H₁ |
| 40–65' | Kuliah: galat Tipe I dan II; kuasa uji; mengapa α bukan angka keramat |
| 65–75' | Istirahat |
| 75–105' | Kuliah + latihan terbimbing: uji-t satu sampel lengkap dengan pemeriksaan asumsi |
| 105–130' | **Bedah klaim:** mahasiswa menyajikan klaim yang ditemukannya; kelas menelaah apakah klaim itu sahih |
| 130–145' | Demo: pengaruh ukuran sampel terhadap *p-value* |
| 145–150' | Penutup, penjelasan Lab 11 |

#### Bedah Klaim "Terbukti Secara Statistik"

Untuk tiap klaim, kelas menelaah:
1. Apa H₀ dan H₁ yang sebenarnya diuji?
2. Berapa ukuran sampelnya? Apakah disebutkan?
3. Apakah ukuran efeknya dilaporkan, atau hanya *p-value*?
4. Apakah kesimpulannya melampaui apa yang didukung data?
5. Adakah kemungkinan *p-hacking* atau pelaporan selektif?

### Setelah Kelas (Mandiri — 180 menit)

1. Mengerjakan [Lab 11](../04-labs/lab-11-uji-hipotesis-satu-sampel.md).
2. Mengerjakan Latihan Soal Bab 10.
3. **Proyek:** merencanakan uji inferensial yang akan dipakai, beserta asumsi yang harus diperiksa.

---

## Penugasan

| Kode | Tugas | Bobot | Batas Waktu |
|------|-------|-------|-------------|
| T-11 | Laporan Lab 11 — Uji hipotesis satu sampel | 1,92% | Sebelum kelas Minggu 12 |

---

## Rangkuman

1. Uji hipotesis bekerja seperti peradilan: H₀ dianggap benar sampai bukti cukup kuat menolaknya.
2. **"Gagal menolak H₀" bukan berarti "H₀ terbukti benar."** Bisa saja buktinya memang kurang.
3. Arah hipotesis harus ditetapkan **sebelum melihat data**. Menyesuaikannya setelah melihat hasil adalah *HARKing*.
4. **Galat Tipe I (α)** = menolak H₀ yang benar; **Tipe II (β)** = gagal menolak H₀ yang salah. Mana yang lebih berbahaya bergantung konteks.
5. **Kuasa uji** = 1 − β. Studi berkuasa rendah yang menghasilkan "tidak signifikan" tidak memberi informasi apa pun.
6. Asumsi uji-t **wajib diperiksa**, bukan diasumsikan. Untuk n ≥ 30, CLT memberi ketahanan terhadap penyimpangan kenormalan ringan.
7. ***p-value* adalah P(data \| H₀), bukan P(H₀ \| data).** Membaliknya adalah kekeliruan yang sama dengan *base rate fallacy* pada Minggu 5.
8. Dengan n cukup besar, **efek sekecil apa pun menjadi "signifikan"**. Karena itu selalu laporkan **ukuran efek dan interval kepercayaan**, bukan hanya *p-value*.

---

## Referensi

1. Walpole, R. E., et al. (2016). *Probability and Statistics for Engineers and Scientists* (9th ed.), Bab 10. Pearson.
2. Wasserstein, R. L., & Lazar, N. A. (2016). The ASA Statement on p-Values: Context, Process, and Purpose. *The American Statistician*, 70(2), 129–133.
3. Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2nd ed.). Lawrence Erlbaum.
4. Greenland, S., et al. (2016). Statistical tests, P values, confidence intervals, and power: a guide to misinterpretations. *European Journal of Epidemiology*, 31(4), 337–350.
5. Kerr, N. L. (1998). HARKing: Hypothesizing After the Results are Known. *Personality and Social Psychology Review*, 2(3), 196–217.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
