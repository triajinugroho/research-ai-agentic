# Panduan Dataset

## Mata Kuliah: Analisis Data Statistik
### Prodi Informatika — UAI — Semester Genap 2025/2026

---

## Prinsip Pemilihan Dataset

Mata kuliah ini menggunakan dataset yang memenuhi kriteria berikut:
1. **Relevan dengan Indonesia** — Konteks lokal untuk pemahaman yang lebih dalam
2. **Publik dan gratis** — Mahasiswa bisa mengakses tanpa biaya
3. **Ukuran yang sesuai** — Cukup besar untuk analisis bermakna, tidak terlalu besar untuk komputasi di Colab
4. **Variasi tipe data** — Numerik, kategorikal, temporal untuk berbagai metode statistik

---

## Dataset Utama yang Digunakan

### 1. Data BPS (Badan Pusat Statistik Indonesia)

| Dataset | URL | Variabel Kunci | Digunakan di |
|---------|-----|----------------|-------------|
| IPM per Provinsi | [bps.go.id](https://www.bps.go.id/id/statistics-table/2/MTk3MCMy/indeks-pembangunan-manusia--metode-baru-.html) | IPM, pendidikan, kesehatan, pengeluaran | Minggu 2, 5, 9 |
| Ketenagakerjaan | [bps.go.id](https://www.bps.go.id/id/statistics-table?subject=6) | Pengangguran, partisipasi kerja, upah | Minggu 7, 11 |
| Pengeluaran RT | [bps.go.id](https://www.bps.go.id/id/statistics-table?subject=5) | Pengeluaran per kapita, kategori | Minggu 11, 12 |
| Pendidikan | [bps.go.id](https://www.bps.go.id/id/statistics-table?subject=28) | Angka partisipasi, literasi, lama sekolah | Minggu 4, 10 |
| Kesehatan | [bps.go.id](https://www.bps.go.id/id/statistics-table?subject=30) | Angka harapan hidup, fasilitas kesehatan | Minggu 6, Proyek |

**Cara mengakses:** Kunjungi bps.go.id → Pilih subjek → Download format Excel/CSV

### 2. Open Data Jakarta

| Dataset | URL | Deskripsi |
|---------|-----|-----------|
| Kualitas Udara | [data.jakarta.go.id](https://data.jakarta.go.id/) | ISPU, PM2.5, PM10 per stasiun |
| Transportasi | [data.jakarta.go.id](https://data.jakarta.go.id/) | Penumpang TransJakarta, MRT |

### 3. Kaggle Datasets (Indonesia-relevant)

| Dataset | URL | Deskripsi |
|---------|-----|-----------|
| Indonesia COVID-19 | [kaggle.com](https://www.kaggle.com/datasets) | Kasus, testing, vaksinasi per provinsi |
| Indonesian E-commerce | [kaggle.com](https://www.kaggle.com/datasets) | Transaksi, kategori produk, review |
| Tokopedia Product | [kaggle.com](https://www.kaggle.com/datasets) | Harga, rating, kategori |

**Catatan:** Cari di Kaggle dengan keyword "Indonesia" untuk menemukan dataset terkini.

### 4. Dataset untuk Lab (Sample/Simulated)

Beberapa lab menggunakan data yang di-generate di Python untuk keperluan demonstrasi:

```python
# Contoh: Generate sample data untuk lab
import numpy as np
import pandas as pd

np.random.seed(42)

# Dataset IPM simulasi (34 provinsi)
data_ipm = pd.DataFrame({
    'provinsi': [f'Provinsi_{i+1}' for i in range(34)],
    'ipm': np.random.normal(71, 5, 34).round(2),
    'pengeluaran_perkapita': np.random.normal(12000, 3000, 34).round(0),
    'angka_melek_huruf': np.random.normal(95, 3, 34).clip(80, 100).round(2),
    'angka_harapan_hidup': np.random.normal(70, 3, 34).round(2),
    'wilayah': np.random.choice(['Jawa', 'Sumatera', 'Kalimantan', 'Sulawesi', 'Papua'], 34)
})
```

---

## Panduan Memilih Dataset untuk Proyek Akhir

### Checklist

- [ ] Minimal 100 observasi (baris)
- [ ] Minimal 5 variabel (kolom)
- [ ] Campuran variabel numerik dan kategorikal
- [ ] Sumber jelas dan dapat diverifikasi
- [ ] Data bisa di-download atau diakses via URL
- [ ] Relevan dengan pertanyaan penelitian kelompok

### Sumber Rekomendasi

| Sumber | URL | Kelebihan |
|--------|-----|-----------|
| BPS | bps.go.id | Data resmi Indonesia, terpercaya |
| Open Data Jakarta | data.jakarta.go.id | Spesifik Jakarta, update reguler |
| Kaggle | kaggle.com | Bervariasi, community support |
| World Bank | data.worldbank.org | Data internasional, bisa compare Indonesia |
| Our World in Data | ourworldindata.org | Visualisasi bagus, data global |
| Data.go.id | data.go.id | Portal data terbuka pemerintah Indonesia |
| Satu Data Indonesia | satudata.go.id | Integrasi data pemerintah |

### Tips

1. **Mulai dari pertanyaan, bukan dari data** — Tentukan apa yang ingin dianalisis, lalu cari data yang sesuai
2. **Cek kualitas data** — Download dan buka dulu, pastikan tidak terlalu banyak missing values
3. **Dokumentasikan sumber** — Catat URL, tanggal download, dan versi data
4. **Preprocessing ringan** — Data BPS kadang perlu sedikit cleaning (format angka, header)
5. **Gunakan AI untuk menemukan dataset** — Prompt: "Saya ingin menganalisis [topik]. Dimana saya bisa menemukan dataset publik tentang ini di Indonesia?"

---

## Panduan Etika Penggunaan Data

1. **Jangan menggunakan data pribadi** tanpa consent
2. **Anonimkan data** jika mengandung informasi identitas
3. **Cite sumber data** di setiap notebook dan laporan
4. **Jangan memanipulasi data** untuk mendukung kesimpulan tertentu
5. **Laporkan limitasi data** — bias, missing values, scope terbatas

---

*Dokumen ini merupakan bagian dari materi kuliah Analisis Data Statistik, Prodi Informatika, Universitas Al Azhar Indonesia.*
