# Panduan Dataset — Probabilitas dan Statistik (IF52510033)

**Semester Ganjil 2026/2027 · Tri Aji Nugroho, S.T., M.T.**

Berkas ini memuat sumber data yang dipakai pada lab, latihan, dan proyek akhir: sumber data publik berkonteks Indonesia yang dapat diakses tanpa biaya (§2), delapan berkas latihan lab yang disiapkan dosen (§3), dan cara memuatnya di Google Colab (§4).

---

## 1. Prinsip Pemilihan Data

1. **Kesimpulan substantif hanya dari data nyata; data sintetis dinyatakan terbuka.** Proyek akhir wajib memakai data nyata ([panduan proyek §2](../05-assessments/project-guidelines.md#2-ketentuan-dasar)). Berkas latihan lab boleh sintetis atau hasil simulasi — misalnya `nilai_mahasiswa_if.csv` — asalkan sifatnya dinyatakan di berkas ini dan di lab yang memakainya, dan hasilnya tidak dipakai untuk menarik kesimpulan tentang dunia nyata.
   > **Status per 7 Oktober 2026 — belum terpenuhi penuh.** Sifat sintetis `nilai_mahasiswa_if.csv` baru dinyatakan di berkas ini (§3) dan pada pemakaian pertamanya, [Lab 01](../04-labs/lab-01-setup-colab-eksplorasi-data.md). Delapan lab lain yang memakai berkas yang sama — Lab 02, 03, 07, 10, 11, 12, 13, dan 14 — belum memuat pernyataan itu; pernyataan perlu ditambahkan pada revisi lab berikutnya. Sampai saat itu, anggap pernyataan di Lab 01 dan di sini berlaku untuk semua lab.
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

## 3. Dataset yang Disediakan untuk Lab

Delapan berkas berikut disiapkan dosen untuk lab, modul, dan buku ajar. Kolom **Dipakai pada** sama dengan baris *Berkas data* di header tiap lab; kolom **Juga dipakai di** mencatat modul mingguan dan bab buku ajar yang memuat berkas yang sama. Jumlah baris dan kolom adalah **spesifikasi** — periksa ulang setelah berkas diunggah (§3.2).

| Berkas | Baris | Kolom utama | Dipakai pada (header lab) | Juga dipakai di | Sifat dan sumber |
|--------|-------|-------------|---------------------------|-----------------|------------------|
| `nilai_mahasiswa_if.csv` | 240 | nim, kelas, nilai_uts, nilai_uas, jam_belajar, asal_sekolah | Lab 01, 02, 03, 07, 10, 11, 12, 13, 14 | Modul Minggu 1, 2, 3, 5, 7, 10, 11, 12, 13, 14 · Bab 1, 2, 3, 9, 10, 11, 12 | **Sintetis** — dibuat menyerupai sebaran nilai nyata; tidak menggambarkan mahasiswa sesungguhnya (dinyatakan di Lab 01) |
| `waktu_respons_server.csv` | 1.000 | timestamp, endpoint, waktu_ms, status_code | Lab 02, 03, 07, 09, 11 | Modul Minggu 2 | Belum didokumentasikan |
| `bug_report_harian.csv` | 365 | tanggal, jumlah_bug, modul, prioritas | Lab 06 | Modul Minggu 6 · Bab 6 | Belum didokumentasikan |
| `email_spam_indonesia.csv` | 800 | teks, label (spam/ham) | Lab 05 | Bab 5 | Belum didokumentasikan |
| `transjakarta_koridor.csv` | 1.200 | koridor, hari, jumlah_penumpang, cuaca | Lab 13 | Modul Minggu 13 | Belum didokumentasikan |
| `harga_rumah_jabodetabek.csv` | 600 | luas_tanah, luas_bangunan, kamar, lokasi, harga_juta | Lab 14 | Modul Minggu 14 · Bab 13 | Belum didokumentasikan |
| `ab_test_fitur_checkout.csv` | 2.000 | user_id, grup, konversi, durasi_detik | Lab 12 | — | Belum didokumentasikan |
| `ispu_jakarta_2025.csv` | 365 | tanggal, stasiun, pm25, pm10, kategori | Lab 07, 10 | — | Belum didokumentasikan |

Lab 04 tidak memakai berkas data (simulasi Monte Carlo); Lab 03 juga memakai dataset bawaan `seaborn` (`anscombe`).

> **Kejujuran asal-usul data.** Hanya `nilai_mahasiswa_if.csv` yang sifatnya sudah dinyatakan, yaitu **sintetis**. Untuk tujuh berkas lainnya, sumber dan sifatnya (data publik yang diolah, atau sintetis/simulasi) **belum didokumentasikan** di repositori ini, sehingga belum boleh disebut "data nyata". Kolom *Sifat dan sumber* diisi dosen saat mengunggah berkas (§3.2); sampai saat itu, perlakukan hasil analisis atas berkas-berkas ini sebagai latihan prosedur, bukan temuan tentang dunia nyata.

### 3.1 Berkas Contoh yang Disiapkan Mahasiswa Sendiri

| Berkas | Dipakai di | Keterangan |
|--------|------------|------------|
| `data_ipm_provinsi_2025.csv` | Bab 14 (contoh alur proyek) | **Tidak disediakan dosen.** Contoh berkas proyek yang diunduh kelompok sendiri dari tabel Indeks Pembangunan Manusia menurut provinsi di BPS (§2.1); kolom yang dipakai contoh: `provinsi`, `ipm` |
| `ipm_provinsi.xlsx` | §4.4 berkas ini | Contoh berkas Excel BPS mentah, diunduh sendiri |

### 3.2 Lokasi Berkas dan Daftar Berkas yang Diharapkan

1. **Lokasi baku:** kedelapan berkas CSV pada §3 disimpan di **folder ini** (`datasets/`, sejajar dengan README ini) dan **diunggah oleh dosen**. Salinan yang sama dibagikan di LMS UAI, sesuai petunjuk "tersedia di LMS" pada lab.
2. **Status per 7 Oktober 2026:** folder ini **belum berisi** berkas CSV — hanya README ini. Daftar berkas yang diharapkan (nama harus persis sama, huruf kecil):
   - [ ] `nilai_mahasiswa_if.csv`
   - [ ] `waktu_respons_server.csv`
   - [ ] `bug_report_harian.csv`
   - [ ] `email_spam_indonesia.csv`
   - [ ] `transjakarta_koridor.csv`
   - [ ] `harga_rumah_jabodetabek.csv`
   - [ ] `ab_test_fitur_checkout.csv`
   - [ ] `ispu_jakarta_2025.csv`
3. **Format:** UTF-8, baris pertama berisi nama kolom seperti pada tabel §3, pemisah kolom koma, pemisah desimal **titik** — agar `pd.read_csv("nama_berkas.csv")` tanpa argumen tambahan berjalan seperti di lab.
4. **Saat mengunggah,** isi kolom *Sifat dan sumber* pada §3 untuk setiap berkas: sumber (tautan, tanggal akses, lisensi) bila berasal dari data publik, atau keterangan "sintetis/simulasi" beserta cara pembuatannya; lalu sesuaikan jumlah baris dengan berkas yang sebenarnya.
5. **Repositori ini publik.** Berkas tidak boleh memuat data pribadi atau nilai mahasiswa sungguhan. Kolom `nim` pada `nilai_mahasiswa_if.csv` harus berisi nomor fiktif, bukan NIM mahasiswa nyata.

Setelah berkas diunggah, sel berikut memeriksa kelengkapan nama berkas dan kolom. Jalankan di Colab setelah berkas diunggah ke sesi (§4.2) atau di dalam folder ini:

```python
import os
import pandas as pd

# Nama berkas dan kolom utama yang diharapkan oleh lab (tabel §3)
BERKAS_DIHARAPKAN = {
    "nilai_mahasiswa_if.csv":      ["nim", "kelas", "nilai_uts", "nilai_uas", "jam_belajar", "asal_sekolah"],
    "waktu_respons_server.csv":    ["timestamp", "endpoint", "waktu_ms", "status_code"],
    "bug_report_harian.csv":       ["tanggal", "jumlah_bug", "modul", "prioritas"],
    "email_spam_indonesia.csv":    ["teks", "label"],
    "transjakarta_koridor.csv":    ["koridor", "hari", "jumlah_penumpang", "cuaca"],
    "harga_rumah_jabodetabek.csv": ["luas_tanah", "luas_bangunan", "kamar", "lokasi", "harga_juta"],
    "ab_test_fitur_checkout.csv":  ["user_id", "grup", "konversi", "durasi_detik"],
    "ispu_jakarta_2025.csv":       ["tanggal", "stasiun", "pm25", "pm10", "kategori"],
}

for nama, kolom in BERKAS_DIHARAPKAN.items():
    if not os.path.exists(nama):
        print(f"[BELUM ADA] {nama}")
        continue
    df = pd.read_csv(nama)
    kurang = [k for k in kolom if k not in df.columns]
    status = "OK" if not kurang else f"KOLOM KURANG {kurang}"
    print(f"[{status}] {nama}: {df.shape[0]} baris × {df.shape[1]} kolom")
```

---

## 4. Memuat Data di Google Colab

### 4.1 Dari URL langsung

Cara ini berlaku **setelah** berkas diunggah ke folder ini pada cabang `main` (§3.2).

```python
import pandas as pd

# Membaca CSV langsung dari folder datasets/ di repositori
BASE = ("https://raw.githubusercontent.com/triajinugroho/research-ai-agentic/main/"
        "mata-kuliah/semester-1/probabilitas-dan-statistik/datasets/")
df = pd.read_csv(BASE + "nilai_mahasiswa_if.csv")
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
