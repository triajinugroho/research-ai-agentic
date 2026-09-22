# Lab 05: Teorema Bayes dan Penyaring Spam

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Probabilitas dan Statistik (IF52510033) |
| **Minggu** | 5 |
| **Durasi** | 180 menit (mandiri) |
| **Prasyarat** | Lab 04 selesai; materi Minggu 5 |
| **Sub-CPMK** | `PS-Sub-CPMK102-1` |
| **Bobot** | 1,92% |
| **Berkas data** | `email_spam_indonesia.csv` |

---

## Tujuan Praktikum

1. Menerapkan hukum probabilitas total dan Teorema Bayes secara komputasional.
2. Menunjukkan *base rate fallacy* dan pengaruh prevalensi terhadap nilai prediktif positif.
3. Membangun penyaring spam Naive Bayes sederhana dari nol.
4. Mengevaluasi penyaring dengan matriks konfusi.
5. Menjelaskan kaitan langsung Teorema Bayes dengan sistem AI.

---

## Persiapan

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from collections import Counter

rng = np.random.default_rng(42)
```

---

## Langkah-langkah

### Langkah 1: Hukum Probabilitas Total

```python
# =============================================
# LANGKAH 1: Hukum probabilitas total
# =============================================

jalur = {
    "CI otomatis":      {"proporsi": 0.50, "p_gagal": 0.02},
    "Manual terjadwal": {"proporsi": 0.30, "p_gagal": 0.08},
    "Hotfix darurat":   {"proporsi": 0.20, "p_gagal": 0.25},
}

# Pemeriksaan: proporsi harus berjumlah 1
total_proporsi = sum(d["proporsi"] for d in jalur.values())
print(f"Jumlah proporsi = {total_proporsi:.4f}  "
      f"{'✓ valid' if abs(total_proporsi - 1) < 1e-9 else '✗ TIDAK VALID'}")

p_gagal = sum(d["proporsi"] * d["p_gagal"] for d in jalur.values())
print(f"\nP(deployment gagal) = {p_gagal:.4f}  ({p_gagal*100:.2f}%)\n")

print(f"{'Jalur':<20} {'Proporsi':>9} {'P(gagal)':>9} {'Kontribusi':>11} {'% kegagalan':>12}")
print("-" * 66)
for nama, d in jalur.items():
    kontrib = d["proporsi"] * d["p_gagal"]
    print(f"{nama:<20} {d['proporsi']:>9.2f} {d['p_gagal']:>9.2f} "
          f"{kontrib:>11.4f} {kontrib/p_gagal*100:>11.1f}%")
```

> **Tulis interpretasi:** hotfix darurat hanya 20% dari deployment, tetapi menyumbang berapa persen dari seluruh kegagalan? Apa rekomendasi Anda kepada tim?

### Langkah 2: Teorema Bayes — Membalik Arah

```python
# =============================================
# LANGKAH 2: Bayes membalik arah persyaratan
# =============================================

# Bila sebuah deployment diketahui GAGAL, dari jalur mana paling mungkin?
print("P(jalur | deployment gagal):\n")
for nama, d in jalur.items():
    posterior = d["proporsi"] * d["p_gagal"] / p_gagal
    print(f"  {nama:<20}: prior {d['proporsi']:.2f} → posterior {posterior:.4f}")

print("\n→ Perhatikan perubahan prior ke posterior.")
print("  Hotfix naik dari 20% menjadi 59,5% — bukti (kegagalan)")
print("  mengubah keyakinan kita secara drastis.")
```

### Langkah 3: *Base Rate Fallacy*

```python
# =============================================
# LANGKAH 3: Mengapa tes akurat menghasilkan alarm palsu
# =============================================

def analisis_diagnostik(prevalensi, sensitivitas, spesifisitas,
                        nama="kondisi", populasi=100_000):
    """Analisis lengkap sebuah tes diagnostik."""
    ada = populasi * prevalensi
    tidak = populasi * (1 - prevalensi)

    benar_positif = ada * sensitivitas
    salah_negatif = ada * (1 - sensitivitas)
    salah_positif = tidak * (1 - spesifisitas)
    benar_negatif = tidak * spesifisitas

    ppv = benar_positif / (benar_positif + salah_positif)
    npv = benar_negatif / (benar_negatif + salah_negatif)

    print(f"=== {nama.upper()} ===")
    print(f"Prevalensi   : {prevalensi:.4f} ({prevalensi*100:.2f}%)")
    print(f"Sensitivitas : {sensitivitas:.4f}")
    print(f"Spesifisitas : {spesifisitas:.4f}\n")

    print(f"Dari {populasi:,} kasus:")
    print(f"{'':>18} {'Tes POSITIF':>13} {'Tes NEGATIF':>13}")
    print(f"{'Kondisi ADA':>18} {benar_positif:>13,.0f} {salah_negatif:>13,.0f}")
    print(f"{'Kondisi TIDAK ADA':>18} {salah_positif:>13,.0f} {benar_negatif:>13,.0f}")

    print(f"\nPPV — P({nama} | positif) = {ppv:.4f}  ({ppv*100:.2f}%)")
    print(f"NPV — P(bukan | negatif)  = {npv:.4f}  ({npv*100:.2f}%)")
    print(f"\n→ Dari {benar_positif + salah_positif:,.0f} alarm, "
          f"{salah_positif:,.0f} ({salah_positif/(benar_positif+salah_positif)*100:.1f}%) "
          f"adalah ALARM PALSU.")
    return ppv, npv

analisis_diagnostik(0.004, 0.98, 0.97, nama="penipuan transaksi")
print()
analisis_diagnostik(0.001, 0.99, 0.99, nama="penyakit langka")
```

### Langkah 4: Pengaruh Prevalensi

```python
# =============================================
# LANGKAH 4: Prevalensi menentukan segalanya
# =============================================

sens, spes = 0.98, 0.97
prevalensi = np.linspace(0.0005, 0.5, 400)

bp = prevalensi * sens
sp = (1 - prevalensi) * (1 - spes)
ppv = bp / (bp + sp)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].plot(prevalensi * 100, ppv * 100, linewidth=2.2, color="steelblue")
axes[0].axhline(50, color="gray", linestyle=":", linewidth=1)
axes[0].axvline(0.4, color="#c0392b", linestyle="--",
                label="Prevalensi penipuan (0,4%)")
axes[0].set_xlabel("Prevalensi (%)")
axes[0].set_ylabel("PPV — P(kondisi | tes positif) (%)")
axes[0].set_title("Tes yang sama, kepercayaan yang sangat berbeda")
axes[0].legend()
axes[0].grid(alpha=0.3)

# Pengaruh menaikkan spesifisitas vs sensitivitas pada prevalensi rendah
prev_tetap = 0.004
spes_range = np.linspace(0.90, 0.9999, 200)
ppv_spes = (prev_tetap * sens) / (prev_tetap * sens +
                                  (1 - prev_tetap) * (1 - spes_range))
sens_range = np.linspace(0.50, 1.0, 200)
ppv_sens = (prev_tetap * sens_range) / (prev_tetap * sens_range +
                                        (1 - prev_tetap) * (1 - spes))

axes[1].plot(spes_range * 100, ppv_spes * 100, linewidth=2.2,
             label="Menaikkan SPESIFISITAS", color="#27ae60")
axes[1].plot(sens_range * 100, ppv_sens * 100, linewidth=2.2,
             label="Menaikkan SENSITIVITAS", color="#e67e22")
axes[1].set_xlabel("Nilai parameter (%)")
axes[1].set_ylabel("PPV (%)")
axes[1].set_title(f"Pada prevalensi {prev_tetap*100:.1f}%,\n"
                  "mana yang lebih berpengaruh?")
axes[1].legend()
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.show()
```

> **Tulis interpretasi:** pada prevalensi rendah, menaikkan sensitivitas atau spesifisitas yang lebih berpengaruh terhadap PPV? Apa implikasinya untuk merancang sistem deteksi penipuan?

### Langkah 5: Membangun Penyaring Spam Naive Bayes

```python
# =============================================
# LANGKAH 5: Naive Bayes dari nol
# =============================================

class NaiveBayesSederhana:
    """Penyaring Naive Bayes multinomial dengan penghalusan Laplace."""

    def __init__(self, alpha=1.0):
        self.alpha = alpha          # parameter penghalusan
        self.prior = {}
        self.hitung_kata = {}
        self.total_kata = {}
        self.kosakata = set()

    def _tokenisasi(self, teks):
        """Memecah teks menjadi kata, diubah ke huruf kecil."""
        return str(teks).lower().split()

    def latih(self, dokumen, label):
        kelas = set(label)
        n_dok = len(dokumen)
        for k in kelas:
            teks_k = [d for d, l in zip(dokumen, label) if l == k]
            self.prior[k] = len(teks_k) / n_dok
            kata = [w for d in teks_k for w in self._tokenisasi(d)]
            self.hitung_kata[k] = Counter(kata)
            self.total_kata[k] = len(kata)
            self.kosakata.update(kata)
        return self

    def log_probabilitas(self, teks):
        """Mengembalikan log probabilitas tiap kelas."""
        V = len(self.kosakata)
        skor = {}
        for k in self.prior:
            log_p = math.log(self.prior[k])
            for w in self._tokenisasi(teks):
                # Penghalusan Laplace agar kata baru tidak membuat P = 0
                p_w = ((self.hitung_kata[k][w] + self.alpha) /
                       (self.total_kata[k] + self.alpha * V))
                log_p += math.log(p_w)
            skor[k] = log_p
        return skor

    def prediksi(self, teks):
        skor = self.log_probabilitas(teks)
        return max(skor, key=skor.get)

# Data latih
dokumen = [
    "selamat anda memenangkan hadiah gratis klik sekarang juga",
    "promo diskon besar gratis klik tautan ini sebelum habis",
    "menangkan undian hadiah gratis segera daftar sekarang",
    "transfer sekarang untuk klaim hadiah undian anda",
    "klik tautan ini untuk dapat bonus gratis tanpa syarat",
    "rapat proyek besok pukul sembilan di ruang lab komputer",
    "tolong kirim laporan praktikum sebelum hari jumat",
    "jadwal kuliah statistika pindah ke ruang tiga nol satu",
    "mohon konfirmasi kehadiran seminar tugas akhir",
    "berkas revisi sudah saya unggah ke folder bersama",
]
label = ["spam"]*5 + ["ham"]*5

model = NaiveBayesSederhana().latih(dokumen, label)

print(f"Prior    : {model.prior}")
print(f"Kosakata : {len(model.kosakata)} kata unik\n")

uji = [
    "gratis hadiah klik sekarang",
    "laporan praktikum statistika besok",
    "selamat anda mendapat bonus",
    "mohon kirim berkas revisi",
]

for pesan in uji:
    skor = model.log_probabilitas(pesan)
    hasil = max(skor, key=skor.get)
    print(f"\"{pesan}\"")
    print(f"  → {hasil.upper()}  (log P spam={skor['spam']:.3f}, "
          f"ham={skor['ham']:.3f})\n")
```

### Langkah 6: Evaluasi dengan Matriks Konfusi

```python
# =============================================
# LANGKAH 6: Evaluasi penyaring
# =============================================

def matriks_konfusi(y_benar, y_prediksi, kelas_positif="spam"):
    """Matriks konfusi dan metrik turunannya."""
    tp = sum(1 for b, p in zip(y_benar, y_prediksi)
             if b == kelas_positif and p == kelas_positif)
    fp = sum(1 for b, p in zip(y_benar, y_prediksi)
             if b != kelas_positif and p == kelas_positif)
    fn = sum(1 for b, p in zip(y_benar, y_prediksi)
             if b == kelas_positif and p != kelas_positif)
    tn = sum(1 for b, p in zip(y_benar, y_prediksi)
             if b != kelas_positif and p != kelas_positif)

    akurasi = (tp + tn) / len(y_benar)
    presisi = tp / (tp + fp) if (tp + fp) else 0
    recall = tp / (tp + fn) if (tp + fn) else 0
    f1 = 2*presisi*recall/(presisi+recall) if (presisi+recall) else 0

    print("=== MATRIKS KONFUSI ===")
    print(f"{'':>16} {'Prediksi spam':>14} {'Prediksi ham':>14}")
    print(f"{'Benar spam':>16} {tp:>14} {fn:>14}")
    print(f"{'Benar ham':>16} {fp:>14} {tn:>14}")
    print(f"\nAkurasi : {akurasi:.4f}")
    print(f"Presisi : {presisi:.4f}  — dari yang ditandai spam, berapa benar")
    print(f"Recall  : {recall:.4f}  — dari spam yang ada, berapa tertangkap")
    print(f"F1      : {f1:.4f}")
    print(f"\nCATATAN: presisi adalah P(benar spam | ditandai spam)")
    print(f"         recall  adalah P(ditandai spam | benar spam)")
    print(f"         Keduanya BERBEDA — persis seperti PPV vs sensitivitas.")
    return {"akurasi": akurasi, "presisi": presisi, "recall": recall, "f1": f1}

# Evaluasi pada data latih (untuk demonstrasi; idealnya pakai data uji terpisah)
prediksi = [model.prediksi(d) for d in dokumen]
matriks_konfusi(label, prediksi)
```

> **Tulis interpretasi:** dalam konteks penyaring surel, mana yang lebih merugikan pengguna — surel penting masuk folder spam (*false positive*), atau spam lolos ke kotak masuk (*false negative*)? Metrik mana yang harus dioptimalkan?

---

## Tantangan Tambahan

### Tantangan 1: Menguji pada Dataset Lebih Besar

Muat `email_spam_indonesia.csv` (800 baris), bagi menjadi data latih (80%) dan uji (20%), latih model, dan evaluasi pada data uji.

```python
# TUGAS ANDA
df_spam = pd.read_csv("email_spam_indonesia.csv")

# 1. Acak dan bagi data 80:20 (gunakan seed!)
# 2. Latih model pada data latih
# 3. Prediksi pada data uji
# 4. Hitung matriks konfusi dan metriknya
# 5. Bandingkan dengan hasil pada data latih — apakah lebih buruk? Mengapa?
```

**Pertanyaan:** mengapa mengevaluasi pada data latih memberi gambaran yang terlalu optimistis? (Konsep ini akan Anda pelajari lebih dalam di Semester 5 sebagai *overfitting*.)

### Tantangan 2: Pengaruh Penghalusan Laplace

Jalankan model dengan `alpha` = 0 (tanpa penghalusan), 0,1, 1,0, dan 10. Bandingkan hasilnya.

```python
# TUGAS ANDA
for a in [0.0001, 0.1, 1.0, 10.0]:
    m = NaiveBayesSederhana(alpha=a).latih(dokumen, label)
    # evaluasi dan laporkan
```

**Pertanyaan:** apa yang terjadi bila `alpha` mendekati nol dan ada kata yang tidak pernah muncul di satu kelas? Mengapa penghalusan diperlukan?

### Tantangan 3: Kalkulator Bayes Interaktif

Buat fungsi yang menerima prior, sensitivitas, spesifisitas, lalu menampilkan diagram pohon dan PPV/NPV. Terapkan pada tiga skenario nyata:

1. Tes COVID cepat (sensitivitas ±0,85, spesifisitas ±0,98) pada prevalensi 2% dan 20%.
2. Sistem pengenalan wajah (sensitivitas 0,95, spesifisitas 0,999) untuk mencari 1 buronan di antara 1 juta orang.
3. Pemindai kerentanan kode (sensitivitas 0,90, spesifisitas 0,85) pada basis kode dengan 1% berkas rentan.

Untuk setiap skenario, tuliskan: **apakah sistem ini layak dipakai untuk pengambilan keputusan otomatis, atau hanya sebagai penyaring awal yang diverifikasi manusia?**

---

## Refleksi

1. Apa yang paling mengejutkan Anda dari *base rate fallacy*?
2. Bagaimana konsep ini berkaitan dengan berita tentang kesalahan sistem pengenalan wajah?
3. Mengapa asumsi "naive" (kata saling bebas) jelas salah, tetapi modelnya tetap berguna?

---

## AI Usage Log

| No | Tanggal | Alat AI | Untuk apa | Prompt (ringkas) | Apa yang saya ubah/verifikasi |
|----|---------|---------|-----------|------------------|-------------------------------|
| 1 | | | | | |

> Nama: ______________  NIM: ______________

---

## Checklist Penyelesaian

- [ ] Notebook dinamai `Lab05_NIM_NamaLengkap.ipynb`
- [ ] Langkah 1–6 selesai
- [ ] Setiap keluaran disertai interpretasi
- [ ] Ketiga tantangan dikerjakan
- [ ] Tantangan 3 menjawab pertanyaan kelayakan untuk ketiga skenario
- [ ] Refleksi terisi
- [ ] AI Usage Log terisi
- [ ] Diunggah ke LMS

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
