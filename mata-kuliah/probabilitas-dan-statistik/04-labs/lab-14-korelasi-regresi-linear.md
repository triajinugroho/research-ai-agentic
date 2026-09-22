# Lab 14: Korelasi dan Regresi Linear

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Probabilitas dan Statistik (IF52510033) |
| **Minggu** | 14 |
| **Durasi** | 180 menit (mandiri) |
| **Prasyarat** | Lab 13 selesai; materi Minggu 14 |
| **Sub-CPMK** | `PS-Sub-CPMK102-1` |
| **Bobot** | 2,04% |
| **Berkas data** | `harga_rumah_jabodetabek.csv`, `nilai_mahasiswa_if.csv` |

---

## Tujuan Praktikum

1. Menghitung dan membandingkan korelasi Pearson dan Spearman.
2. Mendemonstrasikan korelasi palsu dan tiga penyebabnya.
3. Membangun model regresi linear sederhana dengan statsmodels.
4. Membaca dan menafsirkan keluaran regresi secara lengkap.
5. Memeriksa asumsi LINE melalui diagnostik residual.

---

## Persiapan

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from scipy import stats

rng = np.random.default_rng(42)
sns.set_theme(style="whitegrid")
```

---

## Langkah-langkah

### Langkah 1: Pearson vs Spearman

```python
# =============================================
# LANGKAH 1: Kapan memakai yang mana
# =============================================

def bandingkan_korelasi(x, y, nama):
    r_p, p_p = stats.pearsonr(x, y)
    r_s, p_s = stats.spearmanr(x, y)
    print(f"{nama}")
    print(f"  Pearson  : r = {r_p:>7.4f}  (p = {p_p:.2e})")
    print(f"  Spearman : ρ = {r_s:>7.4f}  (p = {p_s:.2e})")
    print(f"  r²       : {r_p**2:.4f} → {r_p**2*100:.1f}% keragaman terjelaskan\n")

# (a) Hubungan linear
x1 = np.arange(1, 41)
y1 = 2*x1 + rng.normal(0, 5, 40)
bandingkan_korelasi(x1, y1, "(a) Linear dengan derap")

# (b) Monoton tetapi tidak linear
x2 = np.arange(1, 41)
y2 = x2 ** 3
bandingkan_korelasi(x2, y2, "(b) Monoton tetapi melengkung tajam")

# (c) Ada pencilan ekstrem
x3 = np.concatenate([np.arange(1, 31), [100]])
y3 = np.concatenate([np.arange(1, 31), [5]])
bandingkan_korelasi(x3, y3, "(c) Dengan satu pencilan ekstrem")

# (d) Hubungan nonlinear simetris (parabola)
x4 = np.linspace(-10, 10, 60)
y4 = x4 ** 2 + rng.normal(0, 4, 60)
bandingkan_korelasi(x4, y4, "(d) Parabola (hubungan kuat, tetapi tidak monoton)")
```

```python
# Visualisasi keempat kasus
fig, axes = plt.subplots(1, 4, figsize=(19, 4))
for ax, (x, y, judul) in zip(axes, [
    (x1, y1, "(a) Linear"), (x2, y2, "(b) Monoton melengkung"),
    (x3, y3, "(c) Ada pencilan"), (x4, y4, "(d) Parabola"),
]):
    ax.scatter(x, y, alpha=0.65, s=35, color="steelblue")
    rp = stats.pearsonr(x, y)[0]
    rs = stats.spearmanr(x, y)[0]
    ax.set_title(f"{judul}\nr={rp:.3f}, ρ={rs:.3f}")
plt.tight_layout()
plt.show()
```

> **Tulis interpretasi:** pada kasus (d), korelasi Pearson mendekati nol padahal hubungannya jelas kuat. Apa pelajarannya? Mengapa **scatter plot wajib dilihat sebelum mempercayai angka korelasi**?

### Langkah 2: Korelasi Palsu

```python
# =============================================
# LANGKAH 2: Tiga penyebab korelasi tanpa sebab-akibat
# =============================================

# (a) KEBETULAN — mencari korelasi tinggi dari data acak
print("(a) KEBETULAN\n")
n_var, n_obs = 100, 30
data_acak = rng.normal(0, 1, (n_var, n_obs))

korelasi_tinggi = []
for i in range(n_var):
    for j in range(i+1, n_var):
        r, p = stats.pearsonr(data_acak[i], data_acak[j])
        if p < 0.05:
            korelasi_tinggi.append((i, j, r, p))

total_pasangan = n_var * (n_var - 1) // 2
print(f"Dari {total_pasangan:,} pasangan variabel ACAK:")
print(f"  {len(korelasi_tinggi)} pasangan 'signifikan' (p < 0,05)")
print(f"  Harapan teoretis: {total_pasangan * 0.05:.0f}")
terkuat = max(korelasi_tinggi, key=lambda t: abs(t[2]))
print(f"  Korelasi terkuat: r = {terkuat[2]:.4f} (p = {terkuat[3]:.6f})")
print("\n→ Semuanya PALSU. Tidak ada hubungan nyata sama sekali.")
```

```python
# (b) VARIABEL PERANCU
print("\n(b) VARIABEL PERANCU\n")
n = 300
kompleksitas = rng.uniform(1, 10, n)          # variabel perancu
baris_kode = 200 * kompleksitas + rng.normal(0, 150, n)
jumlah_bug = 3 * kompleksitas + rng.normal(0, 2.5, n)

r_lk, _ = stats.pearsonr(baris_kode, jumlah_bug)
print(f"Korelasi baris_kode vs jumlah_bug : r = {r_lk:.4f}")
print("Kesimpulan naif: 'menulis lebih sedikit kode mengurangi bug'\n")

# Korelasi parsial: kendalikan kompleksitas
def korelasi_parsial(x, y, z):
    """Korelasi x dan y setelah pengaruh z dikendalikan."""
    rxy = stats.pearsonr(x, y)[0]
    rxz = stats.pearsonr(x, z)[0]
    ryz = stats.pearsonr(y, z)[0]
    return (rxy - rxz*ryz) / np.sqrt((1 - rxz**2) * (1 - ryz**2))

r_parsial = korelasi_parsial(baris_kode, jumlah_bug, kompleksitas)
print(f"Setelah kompleksitas dikendalikan: r = {r_parsial:.4f}")
print("→ Korelasinya nyaris hilang. Penyebab sebenarnya adalah")
print("  KOMPLEKSITAS, yang memengaruhi keduanya.")
```

```python
# (c) ARAH TERBALIK — ilustrasi konseptual
print("\n(c) ARAH TERBALIK\n")
print("Contoh: 'tim yang sering rapat lebih produktif'")
print("  Hipotesis A: rapat → produktivitas")
print("  Hipotesis B: proyek bermasalah → banyak rapat → tampak sibuk")
print("  Hipotesis C: tim besar → banyak rapat DAN banyak output")
print("\n→ Data korelasional TIDAK BISA membedakan ketiganya.")
print("→ Yang membedakan: eksperimen terkendali atau data deret waktu")
print("  yang memungkinkan penelusuran urutan kejadian.")
```

### Langkah 3: Regresi Linear Sederhana

```python
# =============================================
# LANGKAH 3: Membangun model regresi
# =============================================

rumah = pd.read_csv("harga_rumah_jabodetabek.csv")
print(rumah.head())
print(f"\nUkuran: {rumah.shape}")

X = sm.add_constant(rumah[["luas_bangunan"]])
y = rumah["harga_juta"]
model = sm.OLS(y, X).fit()

print(model.summary())
```

```python
b0, b1 = model.params
print(f"\n--- PERSAMAAN ---")
print(f"harga = {b0:.4f} + {b1:.4f} × luas_bangunan")

print(f"\n--- TAFSIR ---")
print(f"Intersep ({b0:.2f}): perkiraan harga saat luas = 0 m².")
print("  → Tidak bermakna secara fisik; hanya titik potong matematis.")
print(f"Kemiringan ({b1:.4f}): setiap tambahan 1 m² luas bangunan")
print(f"  DIKAITKAN DENGAN kenaikan harga sekitar Rp {b1:.2f} juta.")
print("  → Perhatikan kata 'dikaitkan dengan', BUKAN 'menyebabkan'.")

print(f"\nR² = {model.rsquared:.4f}")
print(f"  → {model.rsquared*100:.1f}% keragaman harga terjelaskan oleh luas.")
print(f"  → {(1-model.rsquared)*100:.1f}% oleh faktor lain: lokasi, umur,")
print("     akses transportasi, kondisi bangunan, dan sebagainya.")

print(f"\nIK 95% kemiringan: [{model.conf_int().iloc[1,0]:.4f} , "
      f"{model.conf_int().iloc[1,1]:.4f}]")
```

### Langkah 4: Diagnostik Residual (LINE)

```python
# =============================================
# LANGKAH 4: Memeriksa asumsi LINE
# =============================================

def diagnostik_lengkap(model):
    """Empat plot diagnostik + uji formal."""
    pred = model.fittedvalues
    res = model.resid
    res_std = res / res.std()

    fig, axes = plt.subplots(2, 2, figsize=(13, 9))

    axes[0,0].scatter(pred, res, alpha=0.5, s=25, color="steelblue")
    axes[0,0].axhline(0, color="#c0392b", linestyle="--")
    axes[0,0].set_xlabel("Nilai prediksi"); axes[0,0].set_ylabel("Residual")
    axes[0,0].set_title("Residual vs Prediksi\n(L: cari pola · E: cari corong)")

    stats.probplot(res, dist="norm", plot=axes[0,1])
    axes[0,1].set_title("Q-Q Plot Residual\n(N: titik harus di garis)")

    axes[1,0].hist(res, bins=30, color="steelblue", edgecolor="white")
    axes[1,0].set_xlabel("Residual")
    axes[1,0].set_title("Sebaran Residual")

    axes[1,1].scatter(pred, np.sqrt(np.abs(res_std)), alpha=0.5, s=25,
                      color="steelblue")
    axes[1,1].set_xlabel("Nilai prediksi")
    axes[1,1].set_ylabel("√|residual terstandardisasi|")
    axes[1,1].set_title("Scale-Location\n(E: garis tren harus mendatar)")

    plt.tight_layout(); plt.show()

    print("--- UJI FORMAL ASUMSI ---")
    _, p_sw = stats.shapiro(res[:5000])
    print(f"N — Kenormalan residual (Shapiro) : p = {p_sw:.6f} "
          f"{'✓' if p_sw > 0.05 else '✗'}")

    from statsmodels.stats.diagnostic import het_breuschpagan
    _, p_bp, _, _ = het_breuschpagan(res, model.model.exog)
    print(f"E — Homoskedastisitas (Breusch-P) : p = {p_bp:.6f} "
          f"{'✓' if p_bp > 0.05 else '✗ HETEROSKEDASTIS'}")

    from statsmodels.stats.stattools import durbin_watson
    dw = durbin_watson(res)
    print(f"I — Autokorelasi (Durbin-Watson)  : {dw:.4f} "
          f"{'✓' if 1.5 < dw < 2.5 else '✗'}")
    print(f"L — Linearitas                    : telaah plot kiri-atas")

diagnostik_lengkap(model)
```

### Langkah 5: Visualisasi Model dan Bahaya Ekstrapolasi

```python
# =============================================
# LANGKAH 5: Garis regresi dan batas keberlakuannya
# =============================================

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Dalam rentang data
x_plot = np.linspace(rumah["luas_bangunan"].min(),
                     rumah["luas_bangunan"].max(), 100)
X_plot = sm.add_constant(x_plot)
pred = model.get_prediction(X_plot)
ringkas = pred.summary_frame(alpha=0.05)

axes[0].scatter(rumah["luas_bangunan"], rumah["harga_juta"],
                alpha=0.4, s=25, color="steelblue", label="Data")
axes[0].plot(x_plot, ringkas["mean"], color="#c0392b", linewidth=2,
             label="Garis regresi")
axes[0].fill_between(x_plot, ringkas["mean_ci_lower"],
                     ringkas["mean_ci_upper"], alpha=0.25, color="#c0392b",
                     label="IK 95% rata-rata")
axes[0].fill_between(x_plot, ringkas["obs_ci_lower"],
                     ringkas["obs_ci_upper"], alpha=0.12, color="gray",
                     label="Interval prediksi 95%")
axes[0].set_xlabel("Luas bangunan (m²)")
axes[0].set_ylabel("Harga (juta rupiah)")
axes[0].set_title("Dalam rentang data — sahih")
axes[0].legend(fontsize=8)

# Ekstrapolasi jauh di luar rentang
x_ekstrem = np.linspace(rumah["luas_bangunan"].min(), 3000, 200)
pred_ekstrem = model.get_prediction(sm.add_constant(x_ekstrem)).summary_frame()
axes[1].scatter(rumah["luas_bangunan"], rumah["harga_juta"],
                alpha=0.4, s=25, color="steelblue")
axes[1].plot(x_ekstrem, pred_ekstrem["mean"], color="#c0392b", linewidth=2)
axes[1].axvspan(rumah["luas_bangunan"].max(), 3000, alpha=0.2,
                color="#e74c3c", label="EKSTRAPOLASI")
axes[1].set_xlabel("Luas bangunan (m²)")
axes[1].set_title("Ekstrapolasi — TIDAK dapat dipertanggungjawabkan")
axes[1].legend()

plt.tight_layout(); plt.show()

print(f"Rentang data luas bangunan: "
      f"{rumah['luas_bangunan'].min():.0f} – {rumah['luas_bangunan'].max():.0f} m²")
prediksi_3000 = model.predict([1, 3000])[0]
print(f"Prediksi model untuk 3.000 m²: Rp {prediksi_3000:,.0f} juta")
print("→ Angka ini TIDAK dapat dipercaya. Model tidak pernah melihat")
print("  data seukuran itu; hubungannya bisa saja tidak lagi linear.")
```

---

## Tantangan Tambahan

### Tantangan 1: Regresi Berganda

```python
# TUGAS ANDA
# Bangun model dengan beberapa prediktor:
#   harga ~ luas_bangunan + luas_tanah + kamar
#
# 1. Bandingkan R² dan R² terkoreksi dengan model sederhana
# 2. Periksa multikolinearitas dengan VIF
#    (statsmodels.stats.outliers_influence.variance_inflation_factor)
# 3. Tafsirkan koefisien: apa arti "menahan variabel lain tetap"?
# 4. Jalankan diagnostik residual
#
# Pertanyaan: mengapa R² selalu naik ketika prediktor ditambah,
# sehingga R² TERKOREKSI lebih layak untuk membandingkan model?
```

### Tantangan 2: Transformasi untuk Heteroskedastisitas

```python
# TUGAS ANDA
# Bila diagnostik menunjukkan heteroskedastisitas (pola corong):
# 1. Coba model log(harga) ~ luas_bangunan
# 2. Coba model log(harga) ~ log(luas_bangunan)
# 3. Bandingkan diagnostik residual ketiganya
# 4. Tafsirkan koefisien pada model log-log (elastisitas)
#
# Pertanyaan: pada model log-log, apa arti koefisien 0,8?
# (Petunjuk: kenaikan 1% pada x dikaitkan dengan kenaikan 0,8% pada y.)
```

### Tantangan 3: Analisis Regresi untuk Data Anda

```python
# TUGAS ANDA
# Gunakan data proyek kelompok Anda, atau nilai_mahasiswa_if.csv
# dengan model: nilai_uas ~ jam_belajar
#
# Laporkan lengkap:
# 1. Scatter plot dengan garis regresi
# 2. Persamaan dan tafsir koefisien (gunakan "dikaitkan dengan")
# 3. R² dan maknanya
# 4. Diagnostik residual keempat asumsi LINE
# 5. Interval kepercayaan koefisien
# 6. Apa yang TIDAK boleh disimpulkan dari model ini
#
# Pertanyaan penutup: bolehkah dikatakan "belajar lebih lama
# MENYEBABKAN nilai lebih tinggi"? Sebutkan sekurang-kurangnya
# dua penjelasan alternatif.
```

---

## Refleksi

1. Mengapa scatter plot wajib dilihat sebelum mempercayai angka korelasi?
2. Apa perbedaan "dikaitkan dengan" dan "menyebabkan" dalam pelaporan regresi?
3. Mengapa ekstrapolasi berbahaya, dan bagaimana cara menyatakan batas keberlakuan model?

---

## AI Usage Log

| No | Tanggal | Alat AI | Untuk apa | Prompt (ringkas) | Apa yang saya ubah/verifikasi |
|----|---------|---------|-----------|------------------|-------------------------------|
| 1 | | | | | |

> Nama: ______________  NIM: ______________

---

## Checklist Penyelesaian

- [ ] Notebook dinamai `Lab14_NIM_NamaLengkap.ipynb`
- [ ] Langkah 1–5 selesai
- [ ] Keempat asumsi LINE diperiksa dan dilaporkan
- [ ] Tafsir koefisien memakai "dikaitkan dengan", bukan "menyebabkan"
- [ ] Ketiga tantangan dikerjakan
- [ ] Refleksi terisi
- [ ] AI Usage Log terisi
- [ ] Diunggah ke LMS

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
