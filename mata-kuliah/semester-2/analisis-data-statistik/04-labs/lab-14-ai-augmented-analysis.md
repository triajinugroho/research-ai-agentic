# Lab 14: AI-Augmented Data Analysis Workshop

**Mata Kuliah:** Statistika — Universitas Al Azhar Indonesia
**Minggu:** 14
**Platform:** Google Colab (Python) + AI Tool (ChatGPT / Claude / Gemini)

---

## Tujuan Praktikum

Setelah menyelesaikan workshop ini, mahasiswa mampu:

1. Melakukan analisis data end-to-end dengan AI sebagai co-analyst
2. Merumuskan pertanyaan penelitian yang baik
3. Mengevaluasi secara kritis rencana analisis dan interpretasi yang dihasilkan AI
4. Memverifikasi dan memvalidasi kode yang dihasilkan AI
5. Menulis kesimpulan akhir secara mandiri (bukan copy-paste dari AI)
6. Mendokumentasikan penggunaan AI secara transparan

---

## Persiapan

### Yang Dibutuhkan

1. **Google Colab** — untuk menjalankan kode Python
2. **Akses ke AI Tool** — salah satu dari:
   - ChatGPT (chat.openai.com)
   - Claude (claude.ai)
   - Google Gemini (gemini.google.com)
3. **Dataset** — pilih salah satu (lihat Langkah 1)
4. **Dokumen AI Usage Log** — template disediakan di bawah

### Library Dasar

```python
# Jalankan cell ini terlebih dahulu
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Tambahkan library lain sesuai kebutuhan analisis Anda
# (AI mungkin menyarankan library tambahan)

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

print("Library dasar berhasil dimuat!")
print("Tambahkan library lain sesuai kebutuhan analisis Anda.")
```

### Format Workshop

> **Penting:** Workshop ini berbeda dari lab biasa. Anda akan bekerja bersama AI
> sebagai "co-analyst" — namun Anda tetap bertanggung jawab penuh atas kualitas
> analisis dan kesimpulan. AI adalah alat bantu, bukan pengganti pemikiran kritis Anda.

---

## Langkah-langkah Workshop

### Step 1: Pilih Dataset (15 menit)

Pilih salah satu dataset berikut, atau gunakan dataset Anda sendiri:

```python
# Opsi A: Dataset bawaan sklearn
from sklearn.datasets import load_iris, load_wine, fetch_california_housing

# Opsi B: Dataset dari seaborn
print("Dataset tersedia di seaborn:")
print(sns.get_dataset_names())

# Opsi C: Dataset dari URL
# Contoh: Gapminder, WHO, BPS, dll.

# Opsi D: Upload dataset sendiri
# from google.colab import files
# uploaded = files.upload()
```

```python
# Contoh: Load dataset
# Ganti dengan dataset pilihan Anda

# Opsi menggunakan seaborn tips dataset
data = sns.load_dataset('tips')

print(f"Dataset: tips")
print(f"Jumlah baris: {len(data)}")
print(f"Jumlah kolom: {len(data.columns)}")
print(f"Kolom: {data.columns.tolist()}")
print()
data.head()
```

```python
# Eksplorasi awal — LAKUKAN SENDIRI sebelum bertanya ke AI
print("=== Info Dataset ===")
print(data.info())
print()
print("=== Statistik Deskriptif ===")
print(data.describe())
print()
print("=== Nilai Unik (variabel kategorikal) ===")
for col in data.select_dtypes(include='object').columns:
    print(f"  {col}: {data[col].unique().tolist()}")
```

---

### Step 2: Rumuskan Pertanyaan Penelitian (10 menit) — MANUSIA

> **Ini harus dilakukan SENDIRI, tanpa bantuan AI.**

Berdasarkan eksplorasi data di Step 1, rumuskan 2-3 pertanyaan penelitian.

```python
# Tuliskan pertanyaan penelitian Anda di sini (sebagai komentar atau markdown)
# Jangan tanyakan ke AI — ini adalah latihan berpikir kritis Anda

pertanyaan_penelitian = """
Contoh (ganti dengan pertanyaan Anda sendiri):
1. Apakah terdapat perbedaan rata-rata total bill antara waktu makan
   siang (Lunch) dan makan malam (Dinner)?
2. Faktor-faktor apa saja yang mempengaruhi besarnya tip?
3. Apakah ada hubungan antara ukuran kelompok (size) dan persentase tip?
"""

print("=== Pertanyaan Penelitian ===")
print(pertanyaan_penelitian)
```

**Kriteria pertanyaan yang baik:**
- Spesifik dan dapat dijawab dengan data yang tersedia
- Menggunakan variabel yang ada di dataset
- Menjelaskan variabel dependen dan independen
- Menyatakan arah hubungan yang diduga (jika ada)

---

### Step 3: Minta AI Menyusun Rencana Analisis (10 menit) — AI

Salin teks berikut ke AI tool pilihan Anda. **Sesuaikan** bagian dalam kurung siku.

```
=== PROMPT UNTUK AI ===

Saya adalah mahasiswa statistika. Saya memiliki dataset [nama dataset]
dengan variabel berikut: [daftar variabel dan tipe datanya].

Pertanyaan penelitian saya:
1. [pertanyaan 1]
2. [pertanyaan 2]
3. [pertanyaan 3]

Tolong buatkan rencana analisis statistik yang terstruktur untuk menjawab
setiap pertanyaan. Untuk setiap pertanyaan, jelaskan:
- Metode statistik yang tepat dan alasannya
- Asumsi yang perlu diperiksa
- Visualisasi yang sesuai
- Urutan langkah analisis

Gunakan Python dengan library: pandas, scipy, sklearn, matplotlib, seaborn.
```

```python
# Tempelkan rencana analisis dari AI di sini (sebagai komentar)
# PENTING: Jangan langsung menjalankan — review dulu di Step 4

rencana_ai = """
[Tempelkan respons AI di sini]
"""

print("=== Rencana Analisis dari AI ===")
print(rencana_ai)
```

---

### Step 4: Review Rencana AI (15 menit) — MANUSIA

> **Evaluasi kritis rencana yang diberikan AI.** Gunakan checklist berikut:

```python
# Checklist Review Rencana AI
review_checklist = {
    "Apakah metode statistik yang disarankan tepat untuk tipe data?": "",
    "Apakah asumsi yang disebutkan lengkap?": "",
    "Apakah ada metode alternatif yang tidak disebutkan AI?": "",
    "Apakah urutan langkah sudah logis?": "",
    "Apakah visualisasi yang disarankan informatif?": "",
    "Apakah ada potensi bias atau kesalahan dalam rencana AI?": "",
}

print("=== Checklist Review Rencana AI ===")
for pertanyaan, jawaban in review_checklist.items():
    print(f"\n□ {pertanyaan}")
    print(f"  Catatan: {jawaban if jawaban else '[ISI CATATAN ANDA]'}")
```

```python
# Dokumentasikan modifikasi Anda terhadap rencana AI
modifikasi = """
Contoh modifikasi (ganti dengan modifikasi Anda):
1. AI menyarankan t-test, tapi saya akan cek normalitas dulu dengan Shapiro-Wilk.
   Jika tidak normal, saya akan gunakan Mann-Whitney U.
2. AI tidak menyebutkan pengecekan multikolinearitas. Saya akan tambahkan VIF.
3. Saya akan menambahkan effect size yang tidak disebutkan AI.
"""

print("=== Modifikasi terhadap Rencana AI ===")
print(modifikasi)
```

---

### Step 5: Minta AI Menghasilkan Kode (20 menit) — AI

Untuk setiap langkah dalam rencana analisis, minta AI menghasilkan kode Python.

```
=== PROMPT UNTUK AI ===

Berdasarkan rencana analisis di atas, buatkan kode Python untuk langkah [X].
Dataset sudah di-load dalam variabel 'data' (pandas DataFrame).
Berikan kode yang lengkap dengan komentar penjelasan.
Sertakan juga interpretasi dari output yang diharapkan.
```

```python
# Cell untuk kode dari AI — Langkah 1
# [Tempelkan kode AI di sini]
# PENTING: Baca dan pahami kode sebelum menjalankan

# === KODE DARI AI (Langkah 1: ...) ===

pass  # Ganti dengan kode dari AI
```

```python
# Cell untuk kode dari AI — Langkah 2
# [Tempelkan kode AI di sini]

# === KODE DARI AI (Langkah 2: ...) ===

pass  # Ganti dengan kode dari AI
```

```python
# Cell untuk kode dari AI — Langkah 3
# [Tempelkan kode AI di sini]

# === KODE DARI AI (Langkah 3: ...) ===

pass  # Ganti dengan kode dari AI
```

---

### Step 6: Jalankan dan Verifikasi Kode (20 menit) — MANUSIA

> **Jalankan kode satu per satu.** Untuk setiap cell:
> 1. Baca kode dan pastikan Anda memahami setiap baris
> 2. Jalankan cell
> 3. Periksa apakah output masuk akal
> 4. Dokumentasikan error atau masalah yang ditemukan

```python
# Template verifikasi untuk setiap langkah
def verifikasi_langkah(nomor_langkah, deskripsi):
    """Template untuk mendokumentasikan verifikasi."""
    print(f"=== Verifikasi Langkah {nomor_langkah}: {deskripsi} ===")
    print()

    verifikasi = {
        "Kode berjalan tanpa error": "[Ya/Tidak]",
        "Output sesuai ekspektasi": "[Ya/Tidak]",
        "Apakah saya paham setiap baris kode": "[Ya/Tidak]",
        "Apakah saya perlu modifikasi": "[Ya/Tidak — jelaskan]",
        "Catatan": "[Tulis catatan Anda]"
    }

    for item, status in verifikasi.items():
        print(f"  {item}: {status}")

# Contoh penggunaan:
verifikasi_langkah(1, "Eksplorasi data dan visualisasi awal")
```

```python
# Jika ada error, dokumentasikan di sini
log_error = """
Error yang ditemukan:
1. [Langkah X]: [Deskripsi error]
   - Penyebab: [...]
   - Solusi: [...]

2. [Langkah Y]: [Deskripsi error]
   - Penyebab: [...]
   - Solusi: [...]
"""
```

---

### Step 7: Minta AI Menginterpretasikan Hasil (10 menit) — AI

```
=== PROMPT UNTUK AI ===

Berikut adalah hasil analisis statistik saya:

[Tempelkan output/hasil analisis Anda]

Tolong interpretasikan hasil ini dalam konteks:
- Dataset: [nama dataset]
- Pertanyaan penelitian: [pertanyaan]
- Metode yang digunakan: [metode]

Berikan interpretasi yang:
1. Menjelaskan dalam bahasa non-teknis
2. Menyebutkan signifikansi statistik dan effect size
3. Menyebutkan keterbatasan (limitations)
4. Memberikan rekomendasi praktis (jika relevan)
```

```python
# Tempelkan interpretasi AI di sini
interpretasi_ai = """
[Tempelkan interpretasi dari AI di sini]
"""

print("=== Interpretasi dari AI ===")
print(interpretasi_ai)
```

---

### Step 8: Evaluasi Kritis Interpretasi AI (15 menit) — MANUSIA

> **Ini adalah langkah paling penting.** Jangan langsung menerima interpretasi AI.

```python
# Framework evaluasi kritis
evaluasi_kritis = {
    "1. Apakah interpretasi AI sesuai dengan output statistik?": {
        "penilaian": "[Ya/Tidak/Sebagian]",
        "alasan": "[Jelaskan]"
    },
    "2. Apakah AI over-interpret atau under-interpret hasil?": {
        "penilaian": "[Ya/Tidak]",
        "alasan": "[Jelaskan]"
    },
    "3. Apakah AI menyebutkan keterbatasan yang tepat?": {
        "penilaian": "[Ya/Tidak/Sebagian]",
        "yang terlewat": "[Jelaskan jika ada]"
    },
    "4. Apakah AI membuat klaim kausal dari data korelasional?": {
        "penilaian": "[Ya/Tidak]",
        "catatan": "[Jelaskan]"
    },
    "5. Apakah interpretasi AI kontekstual dan relevan?": {
        "penilaian": "[Ya/Tidak/Sebagian]",
        "catatan": "[Jelaskan]"
    }
}

print("=== Evaluasi Kritis Interpretasi AI ===")
for pertanyaan, detail in evaluasi_kritis.items():
    print(f"\n{pertanyaan}")
    for key, value in detail.items():
        print(f"  {key}: {value}")
```

---

### Step 9: Tulis Kesimpulan Akhir (15 menit) — MANUSIA

> **Tuliskan kesimpulan Anda SENDIRI.** Ini bukan copy-paste dari AI.
> Kesimpulan harus mencerminkan pemahaman Anda, bukan AI.

```python
# Template kesimpulan
kesimpulan_akhir = """
=== KESIMPULAN AKHIR ===
(Ditulis oleh: [Nama Anda])

1. RINGKASAN TEMUAN:
   [Tuliskan temuan utama dari analisis Anda dalam 2-3 kalimat]

2. JAWABAN PERTANYAAN PENELITIAN:
   - Pertanyaan 1: [Jawaban berdasarkan hasil analisis]
   - Pertanyaan 2: [Jawaban berdasarkan hasil analisis]
   - Pertanyaan 3: [Jawaban berdasarkan hasil analisis]

3. KETERBATASAN:
   [Sebutkan minimal 2 keterbatasan analisis Anda]

4. REKOMENDASI:
   [Jika relevan, berikan rekomendasi berdasarkan temuan]

5. REFLEKSI PENGGUNAAN AI:
   [Bagaimana AI membantu? Apa yang AI salah atau kurang tepat?
    Apa yang Anda pelajari dari proses ini?]
"""

print(kesimpulan_akhir)
```

---

### Step 10: Dokumentasikan Penggunaan AI (10 menit)

Lengkapi AI Usage Log berikut. **Transparansi dalam penggunaan AI adalah wajib.**

```python
# ============================================================
# AI USAGE LOG — TEMPLATE
# ============================================================

ai_usage_log = pd.DataFrame(columns=[
    'Step', 'Waktu', 'AI_Tool', 'Prompt_Ringkas',
    'Output_Digunakan', 'Modifikasi_Manusia', 'Catatan'
])

# Contoh pengisian (ganti dengan log Anda yang sebenarnya)
log_entries = [
    {
        'Step': 'Step 3',
        'Waktu': '09:30',
        'AI_Tool': 'ChatGPT',
        'Prompt_Ringkas': 'Minta rencana analisis untuk 3 pertanyaan penelitian',
        'Output_Digunakan': 'Ya — rencana analisis 3 langkah',
        'Modifikasi_Manusia': 'Menambahkan uji normalitas yang tidak disarankan AI',
        'Catatan': 'AI tidak menyebutkan perlu cek asumsi normalitas'
    },
    {
        'Step': 'Step 5',
        'Waktu': '09:50',
        'AI_Tool': 'ChatGPT',
        'Prompt_Ringkas': 'Minta kode Python untuk t-test dan visualisasi',
        'Output_Digunakan': 'Ya — kode t-test dan box plot',
        'Modifikasi_Manusia': 'Memperbaiki nama variabel dan menambahkan effect size',
        'Catatan': 'Kode AI berjalan setelah perbaikan minor'
    },
    {
        'Step': 'Step 7',
        'Waktu': '10:20',
        'AI_Tool': 'ChatGPT',
        'Prompt_Ringkas': 'Minta interpretasi hasil t-test',
        'Output_Digunakan': 'Sebagian — interpretasi statistik',
        'Modifikasi_Manusia': 'AI membuat klaim kausal, saya koreksi jadi korelasional',
        'Catatan': 'Hati-hati: AI sering over-interpret hasil'
    },
]

for entry in log_entries:
    ai_usage_log = pd.concat(
        [ai_usage_log, pd.DataFrame([entry])],
        ignore_index=True
    )

print("=== AI Usage Log ===")
print(ai_usage_log.to_string(index=False))
```

---

## Pertanyaan Refleksi

Jawab pertanyaan-pertanyaan berikut di bagian akhir notebook Anda.

```python
refleksi = """
=== PERTANYAAN REFLEKSI ===

1. PERAN AI DALAM ANALISIS DATA:
   Menurut Anda, apa peran ideal AI dalam analisis data statistik?
   Apakah sebagai "asisten", "co-analyst", atau "pengganti"?
   Jelaskan alasan Anda.

   Jawaban: [...]

2. KEKUATAN DAN KELEMAHAN AI:
   Dari pengalaman workshop ini, apa kekuatan utama AI dalam membantu
   analisis data? Apa kelemahannya?

   Jawaban: [...]

3. CRITICAL THINKING:
   Apakah Anda menemukan kesalahan atau ketidaktepatan dalam output AI?
   Jika ya, jelaskan. Jika tidak, mengapa menurut Anda penting untuk
   tetap memeriksa?

   Jawaban: [...]

4. ETIKA PENGGUNAAN AI:
   Jika Anda menggunakan AI untuk tugas kuliah atau skripsi,
   bagaimana seharusnya penggunaan AI dilaporkan?
   Apa batas antara "dibantu AI" dan "plagiarisme"?

   Jawaban: [...]

5. KETERAMPILAN YANG TETAP DIBUTUHKAN:
   Keterampilan apa saja yang tetap perlu dikuasai manusia meskipun
   AI semakin canggih dalam analisis data?

   Jawaban: [...]

6. PENGALAMAN PRIBADI:
   Apa satu hal baru yang Anda pelajari dari workshop ini yang tidak
   Anda ketahui sebelumnya?

   Jawaban: [...]
"""

print(refleksi)
```

---

## Tugas yang Harus Dikumpulkan

Notebook Google Colab yang berisi **semua 10 step** dengan dokumentasi lengkap:

1. **Dataset dan Eksplorasi** (10 poin)
   - Dataset yang dipilih dan eksplorasi awal

2. **Pertanyaan Penelitian** (10 poin)
   - Minimal 2 pertanyaan yang dirumuskan sendiri (tanpa AI)

3. **Rencana Analisis + Review** (15 poin)
   - Rencana dari AI dan evaluasi kritis Anda

4. **Kode Analisis + Verifikasi** (20 poin)
   - Kode yang berjalan dengan benar
   - Dokumentasi modifikasi yang Anda lakukan

5. **Interpretasi + Evaluasi Kritis** (15 poin)
   - Interpretasi AI dan evaluasi kritis Anda

6. **Kesimpulan Akhir** (10 poin)
   - Ditulis sendiri, bukan copy-paste dari AI

7. **AI Usage Log** (10 poin)
   - Log lengkap setiap interaksi dengan AI

8. **Refleksi** (10 poin)
   - Jawaban refleksi yang thoughtful dan jujur

**Format:** File `.ipynb` diunggah ke Google Classroom
**Deadline:** Satu minggu setelah pertemuan praktikum

> **Peringatan Integritas Akademik:**
> Penggunaan AI untuk analisis data diizinkan dan didorong dalam workshop ini,
> NAMUN Anda harus mendokumentasikan seluruh penggunaan AI secara transparan.
> Kesimpulan dan refleksi harus ditulis sendiri. Mengklaim hasil AI sebagai
> karya sendiri tanpa dokumentasi adalah pelanggaran integritas akademik.

---

## Challenge / Bonus

1. **Bandingkan 2 AI tools**: Gunakan dua AI tools berbeda (misalnya ChatGPT dan Claude) untuk langkah yang sama. Bandingkan kualitas rencana analisis, kode, dan interpretasi. Mana yang lebih baik dan mengapa?

2. **Adversarial testing**: Sengaja berikan AI informasi yang salah atau ambigu. Apakah AI mengoreksi Anda atau mengikuti instruksi yang salah? Dokumentasikan temuannya.

3. **Reproducibility challenge**: Minta teman Anda menggunakan prompt yang sama dengan AI tool yang sama. Apakah hasilnya identik? Apa implikasi ini untuk reproducibility dalam penelitian?
