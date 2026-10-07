# Panduan Dataset

## Mata Kuliah: Kecerdasan Buatan dan Machine Learning
### Prodi Informatika — UAI — Semester Ganjil 2026/2027

---

## Prinsip Pemilihan Dataset

Mata kuliah ini menggunakan dataset yang memenuhi kriteria berikut:
1. **Relevan dengan Indonesia** — Konteks lokal untuk pemahaman yang lebih dalam
2. **Publik dan gratis** — Mahasiswa bisa mengakses tanpa biaya
3. **Ukuran yang sesuai** — Cukup besar untuk training ML, tidak terlalu besar untuk komputasi di Colab
4. **Variasi tipe data** — Numerik, kategorikal, teks, gambar untuk berbagai metode ML
5. **Cocok untuk ML** — Memiliki target variable yang jelas untuk supervised learning atau struktur yang cocok untuk unsupervised learning

---

## Dataset Utama yang Digunakan

### 1. Data BPS (Badan Pusat Statistik Indonesia)

| Dataset | URL | Variabel Kunci | Digunakan di |
|---------|-----|----------------|-------------|
| IPM per Provinsi | [bps.go.id](https://www.bps.go.id/id/statistics-table/2/MTk3MCMy/indeks-pembangunan-manusia--metode-baru-.html) | IPM, pendidikan, kesehatan, pengeluaran | Minggu 4, 5 |
| Ketenagakerjaan | [bps.go.id](https://www.bps.go.id/id/statistics-table?subject=6) | Pengangguran, partisipasi kerja, upah | Minggu 5, 9 |
| Pendidikan | [bps.go.id](https://www.bps.go.id/id/statistics-table?subject=28) | Angka partisipasi, literasi, lama sekolah | Minggu 6, Proyek |
| Kesehatan | [bps.go.id](https://www.bps.go.id/id/statistics-table?subject=30) | Angka harapan hidup, fasilitas kesehatan | Minggu 7, Proyek |

**Cara mengakses:** Kunjungi bps.go.id → Pilih subjek → Download format Excel/CSV

### 2. Open Data Jakarta

| Dataset | URL | Deskripsi |
|---------|-----|-----------|
| Kualitas Udara | [data.jakarta.go.id](https://data.jakarta.go.id/) | ISPU, PM2.5, PM10 per stasiun — cocok untuk regresi/time series |
| Transportasi | [data.jakarta.go.id](https://data.jakarta.go.id/) | Penumpang TransJakarta, MRT — cocok untuk clustering |

### 3. Kaggle Datasets (Indonesia-relevant)

| Dataset | URL | Deskripsi | Cocok untuk |
|---------|-----|-----------|-------------|
| Indonesian E-commerce | [kaggle.com](https://www.kaggle.com/datasets) | Transaksi, kategori produk, review | Klasifikasi, NLP |
| Tokopedia Product | [kaggle.com](https://www.kaggle.com/datasets) | Harga, rating, kategori | Regresi, Clustering |
| Indonesian Hotel Reviews | [kaggle.com](https://www.kaggle.com/datasets) | Review teks + rating | Sentiment Analysis (NLP) |
| Indonesian Food Images | [kaggle.com](https://www.kaggle.com/datasets) | Gambar makanan Indonesia | Image Classification (CV) |

**Catatan:** Cari di Kaggle dengan keyword "Indonesia" untuk menemukan dataset terkini.

### 4. Dataset Klasik ML (untuk benchmarking)

| Dataset | Sumber | Deskripsi | Digunakan di |
|---------|--------|-----------|-------------|
| Iris | sklearn.datasets | 150 sampel bunga, 4 fitur | Minggu 6, 7 (klasifikasi) |
| Boston Housing | sklearn.datasets | Harga rumah, 13 fitur | Minggu 5 (regresi) |
| MNIST Digits | tensorflow.keras | 70K gambar digit tulisan tangan | Minggu 11, 13 (deep learning, CV) |
| 20 Newsgroups | sklearn.datasets | 20K dokumen teks, 20 kategori | Minggu 12 (NLP) |

### 5. Dataset untuk Lab (Sample/Simulated)

Beberapa lab menggunakan data yang di-generate di Python untuk keperluan demonstrasi:

```python
# Contoh: Generate sample data untuk klasifikasi
import numpy as np
import pandas as pd
from sklearn.datasets import make_classification, make_blobs

np.random.seed(42)

# Dataset klasifikasi dengan konteks Indonesia
X, y = make_classification(n_samples=500, n_features=5, n_informative=3,
                           n_redundant=1, random_state=42)
data_kredit = pd.DataFrame(X, columns=['pendapatan', 'usia', 'lama_kerja',
                                        'jumlah_tanggungan', 'skor_riwayat'])
data_kredit['status_kredit'] = y  # 0: ditolak, 1: disetujui
```

```python
# Dataset clustering: profil pelanggan e-commerce
X_cluster, _ = make_blobs(n_centers=4, n_samples=300, n_features=3,
                           random_state=42)
data_pelanggan = pd.DataFrame(X_cluster,
                               columns=['total_belanja', 'frekuensi_kunjungan',
                                        'rata_rata_rating'])
```

---

## Panduan Memilih Dataset untuk Proyek Akhir

### Checklist

- [ ] Minimal 500 observasi (baris) — lebih banyak lebih baik untuk ML
- [ ] Minimal 5 variabel (kolom) termasuk target variable
- [ ] Campuran variabel numerik dan kategorikal
- [ ] Sumber jelas dan dapat diverifikasi
- [ ] Relevan dengan konteks Indonesia (diutamakan)
- [ ] Memiliki problem statement yang jelas (klasifikasi, regresi, atau clustering)

### Rekomendasi Sumber untuk Proyek

| Sumber | URL | Kelebihan |
|--------|-----|-----------|
| Kaggle | [kaggle.com/datasets](https://www.kaggle.com/datasets) | Terbesar, banyak dataset Indonesia |
| BPS | [bps.go.id](https://www.bps.go.id/) | Data resmi pemerintah Indonesia |
| Satu Data Indonesia | [data.go.id](https://data.go.id/) | Portal data terbuka pemerintah |
| Open Data Jakarta | [data.jakarta.go.id](https://data.jakarta.go.id/) | Data DKI Jakarta |
| UCI ML Repository | [archive.ics.uci.edu](https://archive.ics.uci.edu/) | Dataset klasik ML |
| Hugging Face Datasets | [huggingface.co/datasets](https://huggingface.co/datasets) | Dataset NLP & CV |

### Tips

1. **Untuk regresi**: Pilih dataset dengan variabel target kontinu (harga, skor, jumlah)
2. **Untuk klasifikasi**: Pastikan class balance relatif seimbang (atau jelaskan strategi handling imbalance)
3. **Untuk clustering**: Pilih dataset tanpa label yang jelas, lalu validasi clustering dengan domain knowledge
4. **Untuk NLP**: Pilih dataset teks Indonesia — review produk, berita, atau tweet
5. **Untuk CV**: Pilih dataset gambar dengan kategori yang jelas dan jumlah cukup per kategori

---

## Catatan Etika Data

- Selalu **sitasi sumber data** dalam laporan dan notebook
- Jangan menggunakan data **pribadi tanpa izin** (personal data, data medis individu)
- Perhatikan **bias** dalam data — diskusikan potensi bias dan implikasinya
- Gunakan data dengan **lisensi terbuka** (Creative Commons, Open Data)
- Dalam konteks Islam: **amanah** dalam pengelolaan data — jujur, transparan, dan bertanggung jawab

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
