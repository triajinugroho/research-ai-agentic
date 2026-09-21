# Lab 11: Uji Hipotesis Satu Sampel

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Probabilitas dan Statistik (IF52510033) |
| **Minggu** | 11 |
| **Durasi** | 180 menit (mandiri) |
| **Prasyarat** | Lab 10 selesai; materi Minggu 11 |
| **Sub-CPMK** | `PS-Sub-CPMK102-1` |
| **Bobot** | 1,92% |
| **Berkas data** | `nilai_mahasiswa_if.csv`, `waktu_respons_server.csv` |

---

## Tujuan Praktikum

1. Merumuskan H₀ dan H₁ serta menjalankan uji-t satu sampel dengan pemeriksaan asumsi.
2. Menghitung dan menafsirkan *p-value*, ukuran efek, dan interval kepercayaan.
3. Menunjukkan bahwa *p-value* dipengaruhi ukuran sampel.
4. Menghitung kuasa uji dan merencanakan sampel berdasarkan kuasa.
5. Menunjukkan bahaya *p-hacking* secara empiris.

---

## Persiapan

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(42)
```

---

## Langkah-langkah

### Langkah 1: Fungsi Uji-t Satu Sampel Lengkap

```python
# =============================================
# LANGKAH 1: Uji-t lengkap dengan pemeriksaan asumsi
# =============================================

def uji_t_satu_sampel(data, mu0, alpha=0.05, arah="dua sisi", nama="data"):
    """Uji-t satu sampel: asumsi, statistik, efek, interval, keputusan."""
    data = np.asarray(data, dtype=float)
    data = data[~np.isnan(data)]
    n = len(data)
    x_bar, s = data.mean(), data.std(ddof=1)
    se = s / np.sqrt(n)
    t_stat = (x_bar - mu0) / se
    df = n - 1

    if arah == "dua sisi":
        p = 2 * stats.t.sf(abs(t_stat), df); simbol = "≠"
    elif arah == "kanan":
        p = stats.t.sf(t_stat, df); simbol = ">"
    else:
        p = stats.t.cdf(t_stat, df); simbol = "<"

    d = (x_bar - mu0) / s
    besar = ("sangat kecil" if abs(d) < 0.2 else "kecil" if abs(d) < 0.5
             else "sedang" if abs(d) < 0.8 else "besar")
    t_kritis = stats.t.ppf(1 - alpha/2, df)
    ik = (x_bar - t_kritis*se, x_bar + t_kritis*se)

    print("=" * 60)
    print(f"UJI-T SATU SAMPEL — {nama}")
    print("=" * 60)
    print(f"H₀: μ = {mu0}")
    print(f"H₁: μ {simbol} {mu0}")
    print(f"α  = {alpha}   (ditetapkan SEBELUM melihat data)")

    print(f"\n--- PEMERIKSAAN ASUMSI ---")
    print(f"1. Sampel acak dan bebas : harus ditelaah dari cara pengumpulan data")
    print(f"2. Skala interval/rasio  : harus ditelaah dari jenis variabel")
    if 3 <= n <= 5000:
        _, p_norm = stats.shapiro(data)
        print(f"3. Kenormalan (Shapiro)  : p = {p_norm:.6f} "
              f"{'✓ wajar' if p_norm > alpha else '✗ menyimpang'}")
    if n >= 30:
        print(f"   n = {n} ≥ 30 → CLT memberi ketahanan terhadap")
        print(f"   penyimpangan kenormalan ringan.")
    q1, q3 = np.percentile(data, [25, 75])
    iqr = q3 - q1
    n_out = ((data < q1-1.5*iqr) | (data > q3+1.5*iqr)).sum()
    print(f"4. Pencilan ekstrem      : {n_out} kandidat "
          f"({n_out/n*100:.1f}%)")

    print(f"\n--- STATISTIK ---")
    print(f"n              : {n}")
    print(f"Rata-rata      : {x_bar:.4f}")
    print(f"Simpangan baku : {s:.4f}")
    print(f"Galat baku     : {se:.4f}")
    print(f"t              : {t_stat:.4f}  (df = {df})")
    print(f"p-value        : {p:.8f}")

    print(f"\n--- UKURAN EFEK DAN PRESISI ---")
    print(f"Cohen's d      : {d:.4f}  (efek {besar})")
    print(f"IK {(1-alpha)*100:.0f}%        : [{ik[0]:.4f} , {ik[1]:.4f}]")
    print(f"Selisih dari μ₀: {x_bar - mu0:.4f}")

    print(f"\n--- KEPUTUSAN ---")
    if p < alpha:
        print(f"p = {p:.6f} < α = {alpha}  →  TOLAK H₀")
        print(f"Ada bukti statistik yang cukup untuk menyatakan μ {simbol} {mu0}.")
        if abs(d) < 0.2:
            print("PERINGATAN: ukuran efek sangat kecil. Signifikan secara")
            print("statistik belum tentu bermakna secara praktis.")
    else:
        print(f"p = {p:.6f} ≥ α = {alpha}  →  GAGAL MENOLAK H₀")
        print("Bukti tidak cukup untuk menyatakan ada perbedaan.")
        print("CATATAN: ini BUKAN berarti H₀ terbukti benar.")
    return {"t": t_stat, "p": p, "d": d, "ik": ik, "n": n}

df = pd.read_csv("nilai_mahasiswa_if.csv")
uji_t_satu_sampel(df["jam_belajar"], mu0=12, nama="Jam belajar per minggu")
```

### Langkah 2: Uji Satu Sisi

```python
# =============================================
# LANGKAH 2: Uji satu sisi
# =============================================

srv = pd.read_csv("waktu_respons_server.csv")
waktu = srv["waktu_ms"]

# Klaim tim: "optimasi baru membuat rata-rata di bawah 250 ms"
print("KLAIM: rata-rata waktu respons < 250 ms\n")
uji_t_satu_sampel(waktu, mu0=250, arah="kiri", nama="Waktu respons API")

print("\n" + "="*60)
print("Bandingkan dengan uji DUA SISI pada data yang sama:")
uji_t_satu_sampel(waktu, mu0=250, arah="dua sisi", nama="Waktu respons API")
```

> **Tulis interpretasi:** *p-value* uji satu sisi tepat separuh uji dua sisi (bila arahnya sesuai). Mengapa **arah hipotesis wajib ditetapkan sebelum melihat data**? Apa nama pelanggaran bila arah dipilih setelah melihat hasil?

### Langkah 3: Pengaruh Ukuran Sampel terhadap *p-value*

```python
# =============================================
# LANGKAH 3: n besar membuat efek sepele jadi "signifikan"
# =============================================

MU_SEBENARNYA, MU0, SIGMA = 200.5, 200, 35   # efek hanya 0,5 ms

print("Efek sebenarnya: 0,5 ms — tidak berarti apa pun dalam praktik.\n")
print(f"{'n':>10}  {'x̄':>9}  {'p-value':>12}  {'Cohen d':>9}  Kesimpulan")
print("-" * 64)
for n in [30, 100, 1_000, 10_000, 100_000, 1_000_000]:
    s = rng.normal(MU_SEBENARNYA, SIGMA, n)
    t, p = stats.ttest_1samp(s, MU0)
    d = (s.mean() - MU0) / s.std(ddof=1)
    status = "SIGNIFIKAN" if p < 0.05 else "tidak signifikan"
    print(f"{n:>10,}  {s.mean():>9.3f}  {p:>12.6f}  {d:>9.4f}  {status}")

print("\n→ Cohen's d tetap ~0,014 (sangat kecil) di semua n.")
print("→ Tetapi p-value terus mengecil seiring n bertambah.")
print("→ KESIMPULAN: SELALU laporkan ukuran efek, bukan hanya p-value.")
```

### Langkah 4: Kuasa Uji

```python
# =============================================
# LANGKAH 4: Kuasa uji dan perencanaan sampel
# =============================================

def kuasa_uji_t(n, efek, sigma, alpha=0.05, dua_sisi=True):
    """Kuasa uji-t satu sampel."""
    se = sigma / np.sqrt(n)
    df = n - 1
    delta = efek / se
    if dua_sisi:
        tc = stats.t.ppf(1 - alpha/2, df)
        return stats.nct.sf(tc, df, delta) + stats.nct.cdf(-tc, df, delta)
    tc = stats.t.ppf(1 - alpha, df)
    return stats.nct.sf(tc, df, delta)

sigma = 35
print("Kuasa uji menurut n dan besarnya efek (α = 0,05, σ = 35):\n")
print(f"{'n':>7}", end="")
for efek in [5, 10, 15, 20]:
    print(f"  efek={efek:>2} ms", end="")
print()
for n in [10, 20, 30, 50, 100, 200, 500]:
    print(f"{n:>7}", end="")
    for efek in [5, 10, 15, 20]:
        k = kuasa_uji_t(n, efek, sigma)
        tanda = "*" if k >= 0.80 else " "
        print(f"  {k:>8.4f}{tanda}", end="")
    print()
print("\n* = kuasa memadai (≥ 0,80)")
```

```python
# Kurva kuasa
efek_range = np.linspace(1, 30, 200)
plt.figure(figsize=(10, 5.5))
for n in [20, 50, 100, 200]:
    kuasa = [kuasa_uji_t(n, e, sigma) for e in efek_range]
    plt.plot(efek_range, kuasa, linewidth=2, label=f"n = {n}")
plt.axhline(0.80, color="#c0392b", linestyle="--", label="Kuasa 0,80")
plt.xlabel("Besarnya efek sebenarnya (ms)")
plt.ylabel("Kuasa uji (1 − β)")
plt.title("Kurva kuasa uji-t satu sampel (σ = 35 ms, α = 0,05)")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

> **Tulis interpretasi:** bila sebuah studi dengan n = 20 melaporkan "tidak ada perbedaan signifikan" untuk efek 10 ms, seberapa besar kuasanya? Bolehkah kita menyimpulkan tidak ada efek?

### Langkah 5: Bahaya *p-hacking*

```python
# =============================================
# LANGKAH 5: Mendemonstrasikan p-hacking
# =============================================

print("EKSPERIMEN: menguji 20 variabel yang SEMUANYA tidak berefek.\n")

n_variabel, n_sampel = 20, 50
hasil = []
for i in range(n_variabel):
    s = rng.normal(100, 15, n_sampel)      # H₀ BENAR: μ = 100
    t, p = stats.ttest_1samp(s, 100)
    hasil.append({"variabel": f"var_{i+1:02d}", "p": p,
                  "signifikan": p < 0.05})

tabel = pd.DataFrame(hasil)
print(tabel.to_string(index=False))

n_sig = tabel["signifikan"].sum()
print(f"\n→ {n_sig} dari {n_variabel} variabel 'signifikan' (p < 0,05),")
print(f"  padahal H₀ BENAR untuk semuanya.")
print(f"  Harapan teoretis: {n_variabel * 0.05:.1f} temuan palsu.")
print("\n→ Bila peneliti hanya melaporkan yang signifikan, ia sedang")
print("  melakukan P-HACKING — dan hasilnya tidak bermakna sama sekali.")
```

```python
# Simulasi berskala besar
def simulasi_p_hacking(n_percobaan=5000, n_variabel=20, alpha=0.05):
    """Berapa persen percobaan menghasilkan sedikitnya satu temuan palsu?"""
    ada_palsu = 0
    for _ in range(n_percobaan):
        ps = [stats.ttest_1samp(rng.normal(100, 15, 50), 100)[1]
              for _ in range(n_variabel)]
        if min(ps) < alpha:
            ada_palsu += 1
    return ada_palsu / n_percobaan

for k in [1, 5, 10, 20]:
    prop = simulasi_p_hacking(1000, k)
    teori = 1 - (1 - 0.05) ** k
    print(f"Menguji {k:>2} variabel → P(sedikitnya satu palsu) = "
          f"{prop:.4f} (teori {teori:.4f})")
```

---

## Tantangan Tambahan

### Tantangan 1: Uji Nonparametrik

```python
# TUGAS ANDA
# 1. Bangkitkan data yang SANGAT tidak Normal (misalnya lognormal)
#    dengan n = 15
# 2. Jalankan uji-t satu sampel dan uji Wilcoxon signed-rank
# 3. Ulangi 2000 kali dengan H₀ BENAR, hitung berapa persen masing-masing
#    uji salah menolak H₀ (seharusnya ~5%)
# 4. Ulangi dengan H₀ SALAH, bandingkan kuasanya
#
# Pertanyaan: pada data sangat menceng dan n kecil, uji mana yang
# lebih andal mengendalikan galat Tipe I?
```

### Tantangan 2: Menguji Klaim Nyata

Pilih satu klaim dari [tugas pra-kelas Minggu 11](../03-modules/week-11-uji-hipotesis-satu-sampel.md) atau buat sendiri.

```python
# TUGAS ANDA
# 1. Rumuskan H₀ dan H₁ secara eksplisit
# 2. Tetapkan α dan JELASKAN alasannya berdasarkan konteks
#    (mana yang lebih berbahaya: galat Tipe I atau Tipe II?)
# 3. Kumpulkan atau simulasikan data yang relevan
# 4. Periksa asumsi
# 5. Jalankan uji
# 6. Laporkan: statistik uji, p-value, ukuran efek, interval kepercayaan
# 7. Tuliskan kesimpulan dalam satu paragraf untuk pembaca non-teknis
```

### Tantangan 3: Kalkulator Ukuran Sampel Berbasis Kuasa

```python
# TUGAS ANDA
# Buat fungsi n_untuk_kuasa(efek, sigma, kuasa_target=0.80, alpha=0.05)
# yang mencari n terkecil agar kuasa mencapai target.
# Petunjuk: iterasi n dari 2 ke atas sampai kuasa_uji_t(n, ...) ≥ target
#
# Terapkan untuk skenario:
#   - Mendeteksi penurunan waktu respons 5 ms (σ = 35)
#   - Mendeteksi kenaikan nilai rata-rata 3 poin (σ = 11)
#   - Mendeteksi perbedaan 0,5 jam belajar (σ = 4,5)
#
# Sajikan dalam tabel dan beri rekomendasi.
```

---

## Refleksi

1. Tuliskan definisi *p-value* dengan kalimat Anda sendiri — tanpa menyebut "probabilitas hipotesis benar".
2. Mengapa "gagal menolak H₀" berbeda dari "H₀ terbukti benar"?
3. Bagaimana nilai **amanah** berlaku dalam pelaporan hasil uji hipotesis?

---

## AI Usage Log

| No | Tanggal | Alat AI | Untuk apa | Prompt (ringkas) | Apa yang saya ubah/verifikasi |
|----|---------|---------|-----------|------------------|-------------------------------|
| 1 | | | | | |

> Nama: ______________  NIM: ______________

---

## Checklist Penyelesaian

- [ ] Notebook dinamai `Lab11_NIM_NamaLengkap.ipynb`
- [ ] Langkah 1–5 selesai
- [ ] Asumsi diperiksa dan dilaporkan pada setiap uji
- [ ] Ukuran efek dilaporkan bersama *p-value*
- [ ] Ketiga tantangan dikerjakan
- [ ] Refleksi terisi
- [ ] AI Usage Log terisi
- [ ] Diunggah ke LMS

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
