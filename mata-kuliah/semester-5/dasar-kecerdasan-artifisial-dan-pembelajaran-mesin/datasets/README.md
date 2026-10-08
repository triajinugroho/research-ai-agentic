# Panduan Dataset

## Dasar Kecerdasan Artifisial dan Pembelajaran Mesin — IF52510031

**Program Studi Informatika · Universitas Al Azhar Indonesia**

---

## 1. Prinsip Pemilihan Data

Prinsip berikut berlaku untuk **proyek akhir** dan untuk setiap data nyata yang Anda pilih sendiri:

| Prinsip | Alasan |
|---------|--------|
| **Proyek: data nyata, bukan sintetis** | Masalah nyata datang berantakan; itulah yang dilatih dan dinilai pada proyek |
| **Berkonteks Indonesia** | Agar masalah yang dikerjakan bermakna bagi lingkungan sendiri |
| **Lisensi jelas** | Amanah dalam memakai karya orang lain |
| **Definisi variabel dipahami** | Angka tanpa definisi tidak bermakna |
| **Ukuran memadai** | Minimal 500 baris untuk proyek |

### 1.1 Data Praktikum dan Data Proyek: Sengaja Berbeda

**Sebagian besar praktikum memakai data sintetis (simulasi) yang meniru pola Indonesia — bukan data resmi BPS atau lembaga mana pun.** Pada Lab 01 dan Lab 03–14 hal itu dinyatakan pada butir **Data** di bagian Persiapan, dan butir itulah acuannya bila ringkasan di bawah berbeda. Lab 01 memakai dataset bawaan `scikit-learn` dan tabel IPM provinsi yang **ilustratif** (Langkah 4): angkanya sebagian menyerupai rilis IPM BPS dari tahun yang berbeda-beda, sehingga **tidak boleh dikutip** sebagai data BPS. Lab 02 tidak memuat butir Data di bagian Persiapan; datanya (simulasi) dinyatakan pada komentar kode Langkah 4.

| Lab | Data | Jenis |
|-----|------|-------|
| 01 | Dataset bawaan `scikit-learn` (`load_diabetes`, `load_breast_cancer`) dan contoh struktur tabel IPM provinsi — ganti dengan unduhan resmi <https://www.bps.go.id> bila dipakai di luar latihan | Bawaan pustaka + contoh |
| 02, 09, 13 | Pengajuan kredit UMKM | Sintetis (simulasi) |
| 03 | Survei UMKM dengan masalah kualitas yang sengaja disisipkan | Sintetis (simulasi) |
| 04 | Transaksi *e-commerce* | Sintetis (simulasi) |
| 05 | Kemacetan ruas jalan Jakarta per jam | Sintetis (simulasi) |
| 06 | Iklan jual rumah Jabodetabek | Sintetis (simulasi) |
| 07 | Transaksi pembayaran digital | Sintetis (simulasi) |
| 10 | Sesi belanja lokapasar | Sintetis (simulasi) |
| 11 | Indikator sosial-ekonomi 34 provinsi berpola BPS; sumber dan tahun tidak terdokumentasi | Ilustratif (semi-sintetis) |
| 12 | Tabel klasifikasi generik (`make_classification`) | Sintetis, tidak meniru data Indonesia |
| 14 | Kredit UMKM dengan ketimpangan representasi wilayah | Sintetis (simulasi) |

**Mengapa berbeda?** Pada praktikum, data sintetis dipilih karena aturan pembangkitnya diketahui: kebocoran, regularisasi, atau *bias* yang ditanam dapat **diukur terhadap "kebenaran"-nya**, sehingga satu konsep dapat dipelajari terpisah dari kerumitan lain. Pada proyek, yang dinilai justru hal yang tidak dapat dilatih dengan data sintetis — menelusuri sumber dan definisi variabel, membersihkan data yang berantakan tanpa kunci jawaban, serta menyatakan keterwakilan dan keterbatasan yang sesungguhnya. Karena itu [panduan proyek](../05-assessments/project-guidelines.md) **melarang** data sintetis sebagai data utama proyek, dan angka hasil lab **tidak boleh** dikutip sebagai fakta tentang Indonesia.

---

## 2. Yang Wajib Dicatat Setiap Kali Mengunduh

| Butir | Mengapa penting |
|-------|-----------------|
| URL lengkap | Agar dapat ditelusuri ulang |
| **Tanggal akses** | Data terbuka sering diperbarui tanpa pemberitahuan |
| Jumlah baris dan kolom saat diunduh | Pembanding setelah pembersihan |
| Lisensi / ketentuan pakai | Kewajiban hukum dan etis |
| **Definisi tiap variabel** | Sering dilewati, paling mahal akibatnya |
| Cakupan wilayah dan periode | Menentukan batas keberlakuan kesimpulan |

> Contoh akibat melewati baris kelima: "jumlah penduduk" pada satu terbitan BPS dapat berarti hasil proyeksi pertengahan tahun, sedangkan pada terbitan lain berarti hasil sensus. Membandingkan keduanya seolah setara menghasilkan kesimpulan yang salah sejak baris pertama.

---

## 3. Sumber Data Resmi Indonesia

| Sumber | Cakupan | Tautan |
|--------|---------|--------|
| **Badan Pusat Statistik** | Statistik resmi nasional, provinsi, kabupaten | <https://www.bps.go.id> |
| **SIRUSA BPS** | **Definisi baku setiap variabel statistik** | <https://sirusa.bps.go.id> |
| **Satu Data Indonesia** | Portal data lintas kementerian dan lembaga | <https://data.go.id> |
| Jakarta Open Data | Data Pemprov DKI Jakarta | <https://data.jakarta.go.id> |
| Open Data Jabar | Data Pemprov Jawa Barat | <https://opendata.jabarprov.go.id> |
| Kementerian Kesehatan | Fasilitas dan indikator kesehatan | <https://data.kemkes.go.id> |
| PDDikti | Data perguruan tinggi | <https://pddikti.kemdikbud.go.id> |
| BMKG | Cuaca, iklim, kualitas udara | <https://dataonline.bmkg.go.id> |
| Bank Indonesia | Statistik ekonomi dan keuangan | <https://www.bi.go.id/id/statistik> |
| OJK | Statistik perbankan dan keuangan | <https://www.ojk.go.id> |

> **SIRUSA sering terlewat dan paling berguna.** Ia memuat metadata baku: definisi, satuan, metode pengumpulan, dan cakupan setiap variabel statistik resmi.

---

## 4. Sumber Data Bertema Indonesia di Kaggle

| Jenis data | Kata kunci pencarian |
|------------|----------------------|
| Properti | `indonesia house price`, `jakarta property` |
| E-commerce | `indonesia e-commerce`, `tokopedia`, `shopee indonesia` |
| Transportasi | `transjakarta`, `indonesia traffic` |
| Kesehatan | `indonesia health`, `puskesmas` |
| Pendidikan | `indonesia education`, `pddikti` |
| Keuangan | `indonesia banking`, `p2p lending indonesia` |
| Teks bahasa Indonesia | `indonesian text`, `indonesian sentiment` |

Alamat pencarian: <https://www.kaggle.com/datasets?search=indonesia>

> **Peringatan:** dataset Kaggle sering tidak menyertakan definisi variabel yang jelas, dan sebagiannya merupakan data sintetis yang tidak dinyatakan demikian. Periksa deskripsinya dengan saksama; bila sumber aslinya tidak dapat ditelusuri, sebutkan hal itu sebagai keterbatasan.

---

## 5. Dataset Bawaan `scikit-learn` — untuk Latihan

Dipakai pada sebagian praktikum (Lab 1; `make_classification` pada Lab 12; `make_moons`/`make_circles` pada Tantangan Lab 13), **tidak diperkenankan** sebagai data utama proyek.

| Dataset | Jenis *task* | Ukuran |
|---------|--------------|--------|
| `load_diabetes` | Regresi | 442 × 10 |
| `load_breast_cancer` | Klasifikasi biner | 569 × 30 |
| `load_wine` | Klasifikasi multikelas | 178 × 13 |
| `load_digits` | Klasifikasi multikelas | 1.797 × 64 |
| `fetch_california_housing` | Regresi | 20.640 × 8 |
| `make_classification` | Klasifikasi (sintetis) | Dapat ditentukan |
| `make_moons`, `make_circles` | Klasifikasi non-linear (sintetis) | Dapat ditentukan |

---

## 6. Data Primer

Bila kelompok mengumpulkan data sendiri (survei, pencatatan, pengamatan):

| Ketentuan | Penjelasan |
|-----------|------------|
| Minimal responden/pengamatan | 500 |
| Persetujuan | Responden diberi tahu tujuan pengumpulan dan menyetujuinya |
| Kerahasiaan | **Data pribadi yang dapat mengidentifikasi orang tidak boleh disertakan** dalam pengumpulan tugas |
| Instrumen | Kuesioner atau lembar pencatatan dilampirkan |
| Metode pengambilan | Dinyatakan, termasuk keterbatasannya (misalnya *convenience sampling*) |
| Periode pengumpulan | Dicatat |

> **Anonimisasi wajib.** Nama, NIK, nomor telepon, alamat lengkap, dan pengenal serupa dibuang atau diganti dengan kode sebelum data dipakai. Ini bukan formalitas — ia adalah wujud amanah terhadap orang yang mempercayakan datanya.

---

## 7. Memeriksa Kelayakan Dataset

Jalankan sebelum memutuskan memakai sebuah dataset:

```python
import pandas as pd

df = pd.read_csv("data.csv")

print("1. Dimensi:", df.shape)                       # >= 500 baris?
df.info()                                            # 2. Tipe data benar?
display(df.describe().T)                             # 3. Ada nilai mustahil?
print((df.isna().mean()*100).round(2))               # 4. Berapa % hilang?
print("Duplikat:", df.duplicated().sum())            # 5. Ada duplikat?
for k in df.select_dtypes(include="object"):         # 6. Kardinalitas wajar?
    print(f"{k:25s} {df[k].nunique():5d} unik")
print(df[TARGET].value_counts(normalize=True))       # 7. Kelas seimbang?
```

### Tanda Dataset Sebaiknya Tidak Dipakai

| Tanda | Alasan |
|-------|--------|
| Kurang dari 500 baris | Tidak memadai untuk proyek |
| Target tidak jelas atau tidak ada | Tidak dapat dijadikan *task* terbimbing |
| Nilai hilang > 50% pada kolom penting | Terlalu banyak yang harus diandaikan |
| Definisi variabel tidak dapat ditemukan | Interpretasi tidak dapat dipertanggungjawabkan |
| Kelas minoritas < 20 kasus | Terlalu sedikit untuk dipelajari dan dievaluasi |
| Sumber asli tidak dapat ditelusuri | Keandalan tidak dapat dinilai |
| **Ada kolom yang jelas merupakan turunan target** | Kebocoran yang sulit dipisahkan |

---

## 8. Memuat Data di Google Colab

```python
# (a) Dari URL langsung
import pandas as pd
df = pd.read_csv("https://contoh.go.id/data.csv")

# (b) Unggah dari komputer
from google.colab import files
diunggah = files.upload()
df = pd.read_csv(next(iter(diunggah)))

# (c) Dari Google Drive
from google.colab import drive
drive.mount("/content/drive")
df = pd.read_csv("/content/drive/MyDrive/proyek/data.csv")

# (d) Berkas Excel BPS (sering berjudul di beberapa baris pertama)
df = pd.read_excel("data_bps.xlsx", skiprows=3, sheet_name="Sheet1")

# (e) Menyimpan salinan mentah — agar hasil dapat direproduksi
df.to_csv("/content/drive/MyDrive/proyek/data_mentah_2026-10-01.csv", index=False)
```

> **Simpan salinan data mentah dengan tanggal pada namanya.** Data terbuka dapat berubah; tanpa salinan, notebook Anda tidak dapat dijalankan ulang dengan hasil yang sama — dan reproduksibilitas adalah kriteria penilaian.

---

## 9. Masalah Khas Data Indonesia

| Masalah | Contoh | Penanganan |
|---------|--------|------------|
| Nama wilayah tidak baku | "DI Yogyakarta", "D.I. Yogyakarta", "Yogyakarta" | Bakukan sebelum pengelompokan |
| Pemekaran wilayah | Provinsi baru muncul pada data tahun tertentu | Nyatakan cakupan periode; pertimbangkan penggabungan |
| Angka dengan pemisah ribuan | "1.234.567" terbaca sebagai teks | Bersihkan lalu konversi |
| Kode nilai hilang | `-`, `...`, `-99`, `999` | Ubah menjadi `NaN` sebelum apa pun |
| Judul berlapis pada Excel BPS | Header di baris 3–5 | `skiprows` dan `header` disesuaikan |
| Satuan berbeda antar-terbitan | Ribu vs juta rupiah | Periksa SIRUSA; samakan satuan |
| Data terpusat di Jawa | Sebagian besar baris berasal dari provinsi di Jawa | **Nyatakan sebagai keterbatasan**; audit kinerja per wilayah |

> Baris terakhir bukan sekadar catatan teknis. Ketimpangan representasi dalam data terbuka Indonesia dapat membuat model yang dilatih darinya bekerja lebih buruk untuk wilayah yang datanya sedikit — bahasan Minggu 14. Lab 14 memperagakan gejala ini dengan data **sintetis** yang sengaja dibuat timpang; pada proyek, periksa dan laporkan ketimpangan yang **sesungguhnya** pada data nyata Anda.

---

## 10. Etika Pemakaian Data

| Prinsip | Wujud praktis |
|---------|---------------|
| **Amanah** | Mencantumkan sumber lengkap; mematuhi lisensi; tidak mengubah data untuk memperbagus hasil |
| **Menjaga kerahasiaan** | Anonimisasi data pribadi; tidak menyertakan pengenal dalam pengumpulan |
| **Tidak menimbulkan kerugian** | Mempertimbangkan siapa yang dapat dirugikan bila model diterapkan |
| **Adil** | Memeriksa apakah kelompok tertentu kurang terwakili, dan menyatakannya |
| **Jujur** | Menyatakan keterbatasan data apa adanya, termasuk yang melemahkan kesimpulan sendiri |

---

## 11. Dokumen Terkait

1. [Panduan proyek](../05-assessments/project-guidelines.md) — ketentuan data untuk proyek
2. [Modul Minggu 3](../03-modules/week-03-data-dan-prapemrosesan.md) — pemeriksaan kualitas data
3. [Modul Minggu 4](../03-modules/week-04-pembagian-data-dan-kebocoran.md) — kebocoran data
4. [Lab 14](../04-labs/lab-14-audit-bias-dan-model-card.md) — audit ketimpangan representasi (data sintetis)
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
