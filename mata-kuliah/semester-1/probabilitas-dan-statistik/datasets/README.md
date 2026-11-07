# Panduan Dataset — Probabilitas dan Statistik (IF52510033)

**Semester Ganjil 2026/2027 · Tri Aji Nugroho, S.T., M.T.**

Berkas ini memuat sumber data yang dipakai pada lab, latihan, dan proyek akhir. Seluruhnya berkonteks Indonesia dan dapat diakses tanpa biaya.

---

## 1. Prinsip Pemilihan Data

1. **Nyata, bukan sintetis.** Data sintetis hanya dipakai untuk mendemonstrasikan sifat distribusi (misalnya simulasi Teorema Limit Pusat), bukan untuk menarik kesimpulan substantif.
2. **Berkonteks Indonesia.** Mahasiswa harus bisa menilai apakah angka yang keluar masuk akal — itu hanya mungkin bila konteksnya dikenal.
3. **Sumber terbuka dan dapat dirujuk.** Setiap dataset harus punya tautan dan keterangan lisensi.
4. **Ukuran wajar.** Data proyek cukup 200–50.000 baris; lebih besar tidak menambah nilai pembelajaran statistika dasar.
5. **Tidak memuat data pribadi yang dapat mengidentifikasi orang.** Bila memakai data primer, identitas responden harus dianonimkan.

---

## 2. Sumber Data Nasional

### 2.1 Badan Pusat Statistik (BPS)

**Tautan:** <https://www.bps.go.id>

Sumber paling otoritatif untuk data sosial-ekonomi Indonesia.

| Topik | Kegunaan dalam MK Ini |
|-------|------------------------|
| Indeks Harga Konsumen (IHK) bulanan | Deret waktu, ukuran pemusatan, visualisasi tren (Minggu 2–3) |
| Tingkat Pengangguran Terbuka per provinsi | Perbandingan kelompok, ANOVA (Minggu 13) |
| Jumlah penduduk dan kepadatan per provinsi | Distribusi miring, transformasi (Minggu 2) |
| Statistik Telekomunikasi Indonesia | Proporsi, uji proporsi (Minggu 12) |
| Indeks Pembangunan Manusia (IPM) | Korelasi dan regresi (Minggu 14) |
| Produksi tanaman pangan per provinsi | Uji dua sampel, ANOVA (Minggu 12–13) |

**Cara mengunduh:** menu *Tabel Statistik* → pilih subjek → unduh format `.xlsx` atau `.csv`. Perhatikan baris judul ganda — perlu dibersihkan sebelum dianalisis.

### 2.2 Portal Satu Data Indonesia

**Tautan:** <https://data.go.id>

Katalog data terbuka lintas kementerian dan pemerintah daerah.

| Dataset | Kegunaan |
|---------|----------|
| Data kualitas udara DKI Jakarta (ISPU harian) | Distribusi kontinu, uji kenormalan, deret waktu (Minggu 7) |
| Data kecelakaan lalu lintas | Distribusi Poisson (Minggu 6) |
| Data fasilitas kesehatan per kabupaten/kota | Statistika deskriptif, pencilan (Minggu 2) |
| Data penerima bantuan sosial | Proporsi dan uji chi-square (Minggu 13) |

### 2.3 Jakarta Open Data

**Tautan:** <https://data.jakarta.go.id>

| Dataset | Kegunaan |
|---------|----------|
| Jumlah penumpang TransJakarta per koridor | Perbandingan kelompok, ANOVA (Minggu 13) |
| Data banjir dan genangan | Probabilitas kejadian (Minggu 4) |
| Data kependudukan kelurahan | Statistika deskriptif (Minggu 2) |

### 2.4 Sumber Internasional dengan Data Indonesia

| Sumber | Tautan | Kegunaan |
|--------|--------|----------|
| World Bank Open Data | <https://data.worldbank.org> | Indikator makro Indonesia lintas tahun |
| Our World in Data | <https://ourworldindata.org> | Perbandingan Indonesia dengan negara lain |
| Kaggle (filter Indonesia) | <https://www.kaggle.com/datasets> | Dataset e-commerce, properti, ulasan berbahasa Indonesia |

---

## 3. Dataset Latihan di Folder Ini

Delapan berkas berikut **ada di folder ini** dan dapat langsung dipakai. Seluruhnya **sintetis**: dibangkitkan oleh [`bangkitkan_dataset.py`](bangkitkan_dataset.py) dari *seed* tetap (2026), meniru pola yang wajar untuk konteks Indonesia, dan **bukan statistik resmi**. Menjalankan ulang skrip itu selalu menghasilkan berkas yang identik.

| Berkas | Baris | Kolom | Dipakai pada | Pola yang sengaja dibangun |
|--------|------:|-------|--------------|----------------------------|
| `nilai_mahasiswa_if.csv` | 240 | nim, kelas (IF26A/IF26H), nilai_uts, nilai_uas, jam_belajar, asal_sekolah | Lab 01, 02, 03, 07, 10, 11, 12, 13; Minggu 1–3, 5, 7, 10–14 | Jam belajar miring kanan; korelasi jam belajar–UAS ±0,5; selisih kecil antarkelas |
| `waktu_respons_server.csv` | 1.000 | timestamp, endpoint, waktu_ms, status_code | Lab 02, 03, 07, 09, 11 | Lognormal (miring kanan); rata-rata ±220 ms, median ±195 ms |
| `bug_report_harian.csv` | 365 | tanggal, jumlah_bug, modul, prioritas | Lab 06; Minggu 6 | Laju tidak konstan (hari kerja, minggu rilis) → *overdispersion* (var/mean ±1,6) |
| `email_spam_indonesia.csv` | 800 | teks, label (spam/ham) | Lab 05 (Tantangan 1) | 35% spam; kata kunci khas tiap kelas dengan tumpang tindih |
| `transjakarta_koridor.csv` | 1.200 | koridor, hari, jumlah_penumpang, cuaca | Lab 13 | Rata-rata berbeda antarkoridor; akhir pekan dan hujan menurunkan penumpang |
| `harga_rumah_jabodetabek.csv` | 600 | luas_tanah, luas_bangunan, kamar, lokasi, harga_juta | Lab 14; Minggu 14 | Harga naik terhadap luas; lokasi sangat berpengaruh (R² luas saja sedang) |
| `ab_test_fitur_checkout.csv` | 2.000 | user_id, grup (A/B), konversi, durasi_detik | Lab 12 | Konversi A ±8%, B ±11% |
| `ispu_jakarta_2025.csv` | 365 | tanggal, stasiun, pm25, pm10, kategori | Latihan mandiri Minggu 7 dan 10 | PM2.5 lebih tinggi pada Juni–Oktober |

> **Mengapa sintetis?** Agar setiap mahasiswa memperoleh angka yang sama, lab berjalan tanpa akses LMS, dan tidak ada data pribadi. Konsekuensinya, dataset ini **hanya untuk melatih teknik** — jangan menarik kesimpulan tentang mahasiswa, TransJakarta, atau pasar properti sungguhan darinya. Untuk proyek akhir dan klaim substantif, gunakan data resmi dari §2 (BPS, Satu Data Indonesia, Jakarta Open Data) dan catat tabel serta tahunnya.

> **Catatan `nim`.** Bila dibaca biasa, `pd.read_csv` mengubah `nim` menjadi angka dan **membuang nol di depan** (`0102526001` → `102526001`). Ini contoh nyata "kolom yang tipenya tampak keliru" pada Lab 1. Perbaikannya: `pd.read_csv("nilai_mahasiswa_if.csv", dtype={"nim": str})`.

## 4. Memuat Data di Google Colab

### 4.1 Dari URL langsung

```python
import pandas as pd

# Membaca CSV langsung dari tautan
# Berlaku bila repositori dapat diakses publik; bila tidak, pakai cara 4.2
url = ("https://raw.githubusercontent.com/triajinugroho/research-ai-agentic/main/"
       "mata-kuliah/semester-1/probabilitas-dan-statistik/datasets/nilai_mahasiswa_if.csv")
df = pd.read_csv(url)
print(df.shape)
df.head()
```

### 4.2 Mengunggah berkas dari komputer

```python
from google.colab import files

# Akan memunculkan tombol pilih berkas
uploaded = files.upload()

import pandas as pd
df = pd.read_csv("nilai_mahasiswa_if.csv")
df.head()
```

### 4.3 Dari Google Drive

```python
from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/statistika/nilai_mahasiswa_if.csv')
df.head()
```

### 4.4 Membaca berkas Excel BPS

Berkas BPS sering memiliki baris judul ganda dan catatan kaki.

```python
import pandas as pd

# skiprows melewati baris judul; skipfooter melewati catatan kaki
df = pd.read_excel(
    "ipm_provinsi.xlsx",
    skiprows=3,        # sesuaikan dengan struktur berkas
    skipfooter=2,
    engine="openpyxl"
)

# Membersihkan nama kolom
df.columns = [str(c).strip().lower().replace(" ", "_") for c in df.columns]
df = df.dropna(how="all")          # buang baris kosong
print(df.shape)
df.head()
```

---

## 5. Daftar Periksa Kualitas Data

Jalankan daftar periksa ini **sebelum** menganalisis dataset apa pun. Pada proyek akhir, hasil pemeriksaan ini wajib dilaporkan.

```python
def periksa_kualitas(df):
    """Pemeriksaan kualitas data dasar sebelum analisis statistik."""
    print("=== UKURAN ===")
    print(f"Baris : {df.shape[0]}")
    print(f"Kolom : {df.shape[1]}")

    print("\n=== TIPE DATA ===")
    print(df.dtypes)

    print("\n=== NILAI HILANG ===")
    hilang = df.isnull().sum()
    persen = (hilang / len(df) * 100).round(2)
    print(pd.DataFrame({"jumlah": hilang, "persen": persen}))

    print("\n=== DUPLIKAT ===")
    print(f"Baris duplikat: {df.duplicated().sum()}")

    print("\n=== RINGKASAN NUMERIK ===")
    print(df.describe().T)

    print("\n=== KARDINALITAS KOLOM KATEGORIKAL ===")
    for kolom in df.select_dtypes(include="object").columns:
        print(f"{kolom}: {df[kolom].nunique()} nilai unik")

periksa_kualitas(df)
```

**Pertanyaan yang harus dijawab sebelum lanjut:**

1. Apakah jumlah baris masuk akal untuk konteksnya?
2. Apakah ada kolom yang tipenya salah (angka terbaca sebagai teks)?
3. Berapa persen nilai hilang, dan apakah hilangnya acak atau sistematis?
4. Apakah ada nilai yang mustahil (umur negatif, persentase di atas 100)?
5. Apakah duplikat memang duplikat, atau kebetulan sama?

---

## 6. Etika Penggunaan Data

Mengacu pada nilai **amanah** yang menjadi landasan Prodi Informatika UAI:

| Prinsip | Penerapan Konkret |
|---------|-------------------|
| **Sebutkan sumber** | Setiap dataset dalam laporan wajib disertai tautan dan tanggal akses |
| **Hormati lisensi** | Periksa ketentuan pakai; data BPS boleh dipakai untuk pendidikan dengan atribusi |
| **Lindungi privasi** | Jangan memakai data yang memuat nama, NIK, nomor telepon, atau alamat |
| **Jangan memanipulasi** | Membuang data yang "mengganggu" agar hasil signifikan adalah pelanggaran berat |
| **Laporkan pembersihan** | Setiap baris yang dibuang harus dijelaskan alasannya |
| **Akui keterbatasan** | Sampel yang tidak representatif harus dinyatakan, bukan disembunyikan |

> **Yang paling sering terjadi dan paling berbahaya:** mahasiswa membuang pencilan tanpa alasan substantif, hanya karena hasilnya jadi lebih rapi. Pencilan boleh dibuang **hanya** bila ada alasan yang dapat dipertanggungjawabkan — misalnya kesalahan pencatatan yang terbukti. Bila tidak, pencilan adalah data, bukan gangguan.

---

## 7. Data Primer: Bila Kelompok Mengumpulkan Sendiri

Sebagian kelompok memilih mengumpulkan data sendiri (survei mahasiswa, pengukuran waktu eksekusi, pengamatan antrean). Ketentuannya:

1. **Rancang instrumen dulu**, jangan mengumpulkan data lalu memikirkan pertanyaannya.
2. **Tentukan populasi dan kerangka sampel** secara eksplisit; sampel kenyamanan (*convenience sample*) boleh, tetapi keterbatasannya wajib dinyatakan.
3. **Minimal 30 pengamatan per kelompok** yang akan dibandingkan.
4. **Anonimkan** sejak pencatatan — jangan pernah menyimpan nama.
5. **Minta persetujuan** responden secara jelas, termasuk untuk apa data dipakai.
6. **Lampirkan instrumen** (kuesioner atau prosedur pengukuran) pada laporan.

---

## 8. Referensi

1. Badan Pusat Statistik. *Statistik Indonesia*. <https://www.bps.go.id>
2. Kementerian PPN/Bappenas. *Portal Satu Data Indonesia*. <https://data.go.id>
3. Pemerintah Provinsi DKI Jakarta. *Jakarta Open Data*. <https://data.jakarta.go.id>
4. Wickham, H. (2014). Tidy Data. *Journal of Statistical Software*, 59(10).
5. Dokumentasi pandas — <https://pandas.pydata.org/docs/>

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
