# Lab 02: Statistika Deskriptif dengan pandas

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Probabilitas dan Statistik (IF52510033) |
| **Minggu** | 2 |
| **Durasi** | 180 menit (mandiri) |
| **Prasyarat** | Lab 01 selesai |
| **Sub-CPMK** | `PS-Sub-CPMK102-1` |
| **Bobot** | 1,92% |
| **Berkas data** | `nilai_mahasiswa_if.csv`, `waktu_respons_server.csv` |

---

## Tujuan Praktikum

1. Menghitung ukuran pemusatan, penyebaran, dan posisi dengan pandas dan NumPy.
2. Memverifikasi hasil komputasi dengan perhitungan manual.
3. Menjelaskan perbedaan `ddof=0` dan `ddof=1` serta kapan masing-masing dipakai.
4. Mendeteksi pencilan dengan aturan 1,5×IQR dan menelaahnya secara kritis.
5. Menentukan ukuran pemusatan yang tepat berdasarkan bentuk sebaran.

---

## Persiapan

1. Buat notebook `Lab02_NIM_NamaLengkap`.
2. Unggah kedua berkas data.
3. Siapkan kalkulator untuk verifikasi manual.

---

## Langkah-langkah

### Langkah 1: Setup

```python
# =============================================
# LANGKAH 1: Setup
# =============================================

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

pd.set_option("display.float_format", "{:.4f}".format)

df = pd.read_csv("nilai_mahasiswa_if.csv")
srv = pd.read_csv("waktu_respons_server.csv")

print(f"Data nilai  : {df.shape}")
print(f"Data server : {srv.shape}")
```

### Langkah 2: Verifikasi Manual vs Komputasi

Kerjakan **dengan kalkulator terlebih dahulu**, baru jalankan kodenya.

```python
# =============================================
# LANGKAH 2: Verifikasi manual
# =============================================

data_kecil = np.array([42, 38, 45, 41, 39, 44, 40, 185])

print("Data:", data_kecil)
print("\n--- HITUNG MANUAL DULU, baru jalankan sel ini ---\n")

n = len(data_kecil)
mean = data_kecil.mean()
median = np.median(data_kecil)
rentang = data_kecil.max() - data_kecil.min()

# Varians sampel: penyebut n−1
simpangan = data_kecil - mean
var_sampel = (simpangan ** 2).sum() / (n - 1)
sd_sampel = np.sqrt(var_sampel)

# Varians populasi: penyebut n
var_populasi = (simpangan ** 2).sum() / n
sd_populasi = np.sqrt(var_populasi)

print(f"n                     : {n}")
print(f"Mean                  : {mean:.4f}")
print(f"Median                : {median:.4f}")
print(f"Range                 : {rentang}")
print(f"Varians SAMPEL  (n−1) : {var_sampel:.4f}")
print(f"SD SAMPEL             : {sd_sampel:.4f}")
print(f"Varians POPULASI (n)  : {var_populasi:.4f}")
print(f"SD POPULASI           : {sd_populasi:.4f}")

# Membuktikan default NumPy vs pandas berbeda
print(f"\nnumpy .var()  default (ddof=0) : {data_kecil.var():.4f}")
print(f"numpy .var(ddof=1)             : {data_kecil.var(ddof=1):.4f}")
print(f"pandas .var() default (ddof=1) : {pd.Series(data_kecil).var():.4f}")
```

> **Tulis interpretasi:** mengapa NumPy dan pandas punya nilai bawaan yang berbeda? Mana yang benar? Apa risikonya bila Anda tidak menyadari perbedaan ini?

### Langkah 3: Fungsi Ringkasan Deskriptif Lengkap

```python
# =============================================
# LANGKAH 3: Ringkasan deskriptif lengkap
# =============================================

def ringkasan_lengkap(seri, nama):
    """Ringkasan deskriptif beserta rekomendasi ukuran pemusatan."""
    seri = seri.dropna()
    q1, q2, q3 = seri.quantile([0.25, 0.50, 0.75])
    iqr = q3 - q1
    kemencengan = stats.skew(seri)
    kurtosis = stats.kurtosis(seri)

    print("=" * 56)
    print(f"  {nama}")
    print("=" * 56)
    print(f"  n                    : {seri.count()}")
    print(f"  --- PEMUSATAN ---")
    print(f"  Mean                 : {seri.mean():.4f}")
    print(f"  Median               : {seri.median():.4f}")
    print(f"  Modus                : {seri.mode().tolist()[:3]}")
    print(f"  --- PENYEBARAN ---")
    print(f"  Range                : {seri.max() - seri.min():.4f}")
    print(f"  Varians (ddof=1)     : {seri.var():.4f}")
    print(f"  Simpangan baku       : {seri.std():.4f}")
    print(f"  Koefisien variasi    : {seri.std()/seri.mean()*100:.2f}%")
    print(f"  --- POSISI ---")
    print(f"  Min / Q1 / Q2 / Q3 / Max")
    print(f"  {seri.min():.2f} / {q1:.2f} / {q2:.2f} / {q3:.2f} / {seri.max():.2f}")
    print(f"  IQR                  : {iqr:.4f}")
    print(f"  p90 / p95 / p99      : {seri.quantile(0.90):.2f} / "
          f"{seri.quantile(0.95):.2f} / {seri.quantile(0.99):.2f}")
    print(f"  --- BENTUK ---")
    print(f"  Kemencengan          : {kemencengan:.4f}")
    print(f"  Kurtosis berlebih    : {kurtosis:.4f}")

    # Rekomendasi otomatis
    print(f"  --- REKOMENDASI ---")
    if abs(kemencengan) < 0.5:
        print("  Sebaran cukup simetris → MEAN layak dipakai.")
    else:
        arah = "kanan" if kemencengan > 0 else "kiri"
        print(f"  Menceng {arah} → gunakan MEDIAN dan IQR.")

    # Pencilan
    bb, ba = q1 - 1.5*iqr, q3 + 1.5*iqr
    pencilan = seri[(seri < bb) | (seri > ba)]
    print(f"  Batas wajar 1,5×IQR  : [{bb:.2f} , {ba:.2f}]")
    print(f"  Kandidat pencilan    : {len(pencilan)} nilai "
          f"({len(pencilan)/len(seri)*100:.1f}%)")
    if len(pencilan) > 0:
        print(f"    → {sorted(pencilan.tolist())[:8]}")
        print("    JANGAN dibuang tanpa alasan substantif.")

for kolom in ["nilai_uts", "nilai_uas", "jam_belajar"]:
    ringkasan_lengkap(df[kolom], kolom)
```

### Langkah 4: Kasus Nyata — Waktu Respons Server

```python
# =============================================
# LANGKAH 4: Mengapa industri tidak memakai rata-rata
# =============================================

waktu = srv["waktu_ms"]

ringkasan_lengkap(waktu, "Waktu Respons Server (ms)")

print("\n" + "=" * 56)
print("  PERBANDINGAN CARA MELAPORKAN KINERJA")
print("=" * 56)
print(f"  Laporan A (menyesatkan) : 'rata-rata {waktu.mean():.0f} ms'")
print(f"  Laporan B (jujur)       : 'p50={waktu.quantile(0.50):.0f} ms, "
      f"p95={waktu.quantile(0.95):.0f} ms, p99={waktu.quantile(0.99):.0f} ms'")

# Berapa persen pengguna mengalami pengalaman buruk?
ambang = 1000
buruk = (waktu > ambang).mean() * 100
print(f"\n  Pengguna yang menunggu > {ambang} ms: {buruk:.2f}%")
print(f"  Jumlah permintaan terdampak dari {len(waktu)}: {(waktu > ambang).sum()}")
```

> **Tulis interpretasi:** jelaskan dalam kalimat sendiri mengapa Laporan A menyesatkan meskipun angkanya benar. Bila Anda manajer produk, laporan mana yang Anda butuhkan?

### Langkah 5: Analisis per Kelompok

```python
# =============================================
# LANGKAH 5: Perbandingan antar kelompok
# =============================================

print("=== NILAI UAS MENURUT KELAS ===")
print(df.groupby("kelas")["nilai_uas"].agg(
    ["count", "mean", "median", "std", "min", "max"]
).round(2))

print("\n=== JAM BELAJAR MENURUT ASAL SEKOLAH ===")
print(df.groupby("asal_sekolah")["jam_belajar"].agg(
    ["count", "mean", "median", "std"]
).round(2))

print("\n=== TABEL SILANG: rata-rata nilai UAS ===")
print(pd.crosstab(df["kelas"], df["asal_sekolah"],
                  values=df["nilai_uas"], aggfunc="mean").round(2))
```

> **Tulis interpretasi:** apakah selisih rata-rata yang Anda lihat cukup besar untuk disebut "berbeda"? Jawaban jujurnya: **belum bisa dipastikan dari statistika deskriptif saja.** Sebutkan minggu ke berapa yang akan menjawabnya.

### Langkah 6: Menelaah Pencilan Secara Kritis

```python
# =============================================
# LANGKAH 6: Telaah pencilan — bukan sekadar mendeteksi
# =============================================

def telaah_pencilan(seri, df_asal, nama):
    """Mendeteksi pencilan DAN menampilkan konteksnya."""
    q1, q3 = seri.quantile([0.25, 0.75])
    iqr = q3 - q1
    bb, ba = q1 - 1.5*iqr, q3 + 1.5*iqr
    mask = (seri < bb) | (seri > ba)

    print(f"=== PENCILAN PADA {nama} ===")
    print(f"Batas wajar: [{bb:.2f} , {ba:.2f}]")
    print(f"Ditemukan {mask.sum()} kandidat pencilan.\n")

    if mask.sum() > 0:
        print("Konteks lengkap baris-baris tersebut:")
        print(df_asal[mask])
        print("\nPERTANYAAN YANG HARUS DIJAWAB:")
        print("  1. Apakah ini kesalahan pencatatan yang terbukti?")
        print("  2. Apakah ada penjelasan substantif untuk nilai ekstrem ini?")
        print("  3. Apa dampaknya pada kesimpulan bila dipertahankan?")
        print("  4. Apa dampaknya bila dibuang?")

telaah_pencilan(df["jam_belajar"], df, "JAM BELAJAR")
```

```python
# Membandingkan statistik dengan dan tanpa pencilan
q1, q3 = df["jam_belajar"].quantile([0.25, 0.75])
iqr = q3 - q1
mask_bersih = df["jam_belajar"].between(q1 - 1.5*iqr, q3 + 1.5*iqr)

print(f"{'Statistik':<20} {'Dengan pencilan':>17} {'Tanpa pencilan':>16}")
print("-" * 55)
for nama, fungsi in [("Mean", "mean"), ("Median", "median"),
                     ("Simpangan baku", "std")]:
    dengan = getattr(df["jam_belajar"], fungsi)()
    tanpa = getattr(df.loc[mask_bersih, "jam_belajar"], fungsi)()
    print(f"{nama:<20} {dengan:>17.4f} {tanpa:>16.4f}")

print("\n→ Perhatikan: MEDIAN hampir tidak berubah, MEAN dan SD berubah.")
print("→ Ini bukan alasan untuk membuang pencilan; ini alasan untuk")
print("  MELAPORKAN median ketika pencilan ada.")
```

---

## Tantangan Tambahan

### Tantangan 1: Fungsi Deteksi Pencilan Alternatif

Selain aturan 1,5×IQR, ada metode skor-z dan skor-z termodifikasi (berbasis MAD). Implementasikan ketiganya dan bandingkan hasilnya.

```python
def deteksi_pencilan_3metode(data):
    """Membandingkan tiga metode deteksi pencilan."""
    data = np.asarray(data)

    # Metode 1: IQR
    q1, q3 = np.percentile(data, [25, 75])
    iqr = q3 - q1
    iqr_mask = (data < q1 - 1.5*iqr) | (data > q3 + 1.5*iqr)

    # Metode 2: skor-z (|z| > 3)
    z = (data - data.mean()) / data.std(ddof=1)
    z_mask = np.abs(z) > 3

    # Metode 3: skor-z termodifikasi (berbasis MAD)
    # TUGAS ANDA: lengkapi
    # Petunjuk: MAD = median(|xi − median|)
    #           z_mod = 0.6745 × (xi − median) / MAD
    #           pencilan bila |z_mod| > 3.5
    mad_mask = None   # ganti dengan implementasi Anda

    return {"IQR": iqr_mask, "z-score": z_mask, "z-mod": mad_mask}

# Bandingkan pada data waktu respons server
hasil = deteksi_pencilan_3metode(srv["waktu_ms"])
for nama, mask in hasil.items():
    if mask is not None:
        print(f"{nama:10s}: {mask.sum()} pencilan terdeteksi")
```

**Pertanyaan:** metode mana yang paling banyak menandai pencilan pada data menceng? Mengapa?

### Tantangan 2: Statistika Deskriptif untuk Data BPS

Unduh data IPM per provinsi dari BPS. Hitung ringkasan deskriptif lengkap dan jawab:

1. Provinsi mana yang menjadi pencilan?
2. Apakah sebarannya simetris atau menceng?
3. Ukuran pemusatan mana yang paling tepat untuk melaporkan "IPM tipikal Indonesia"?
4. Bolehkah provinsi pencilan dibuang dari laporan? Jelaskan.

### Tantangan 3: Membandingkan Konsistensi dengan Koefisien Variasi

Tiga layanan memiliki waktu respons dengan satuan berbeda. Gunakan koefisien variasi untuk membandingkan konsistensinya secara adil.

```python
layanan = {
    "API Autentikasi (ms)":  np.array([45, 48, 43, 47, 44, 46, 49, 45]),
    "Query Database (ms)":   np.array([210, 350, 180, 420, 195, 380, 205, 390]),
    "Render Laporan (detik)": np.array([3.1, 3.4, 2.9, 3.2, 3.0, 3.3, 3.1, 3.5]),
}

# TUGAS ANDA: hitung mean, SD, dan CV untuk tiap layanan.
# Tentukan layanan mana yang PALING KONSISTEN dan jelaskan
# mengapa simpangan baku saja tidak cukup untuk menjawabnya.
```

---

## Refleksi

1. Apa hal paling penting yang Anda pelajari tentang mean vs median?
2. Mengapa pencilan tidak boleh langsung dibuang?
3. Dalam pekerjaan sebagai pengembang perangkat lunak kelak, kapan Anda akan memakai p95 alih-alih rata-rata?

---

## AI Usage Log

| No | Tanggal | Alat AI | Untuk apa | Prompt (ringkas) | Apa yang saya ubah/verifikasi |
|----|---------|---------|-----------|------------------|-------------------------------|
| 1 | | | | | |

> *Saya menyatakan bahwa seluruh perhitungan statistik, pemilihan metode, dan interpretasi hasil dalam pekerjaan ini adalah hasil pemahaman saya sendiri.*
> Nama: ______________  NIM: ______________

---

## Checklist Penyelesaian

- [ ] Notebook dinamai `Lab02_NIM_NamaLengkap.ipynb`
- [ ] Langkah 2 dikerjakan **manual lebih dahulu**, hasilnya dibandingkan dengan kode
- [ ] Langkah 1–6 selesai
- [ ] Setiap keluaran disertai interpretasi
- [ ] Ketiga tantangan dikerjakan (Tantangan 1 dan 3 dilengkapi kodenya)
- [ ] Refleksi terisi
- [ ] AI Usage Log terisi
- [ ] Diunggah ke LMS

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
