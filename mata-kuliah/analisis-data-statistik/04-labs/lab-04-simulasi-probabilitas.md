# Lab 04: Simulasi Probabilitas

**Mata Kuliah:** Statistika dan Probabilitas
**Program Studi:** Universitas Al Azhar Indonesia
**Minggu:** 4
**Penilaian:** Dinilai (submit notebook)

---

## Tujuan Praktikum

Setelah menyelesaikan lab ini, mahasiswa mampu:

1. Mensimulasikan eksperimen probabilitas sederhana (koin, dadu) menggunakan Python
2. Memverifikasi probabilitas teoritis melalui simulasi
3. Mensimulasikan dan menganalisis Monty Hall Problem
4. Mengaplikasikan Teorema Bayes dalam perhitungan Python
5. Memahami hukum bilangan besar (Law of Large Numbers) melalui simulasi

---

## Persiapan

- Google Colab notebook baru
- Nama file: `Lab04_NamaAnda_NIM.ipynb`
- Library: numpy, matplotlib, pandas

---

## Langkah-langkah

### Langkah 1: Setup

```python
# =============================================
# LANGKAH 1: Setup
# =============================================

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

np.random.seed(42)

print("Setup selesai!")
print("Pada lab ini kita akan belajar probabilitas melalui simulasi.")
```

### Langkah 2: Simulasi Pelemparan Koin

```python
# =============================================
# LANGKAH 2: Simulasi Koin - Verifikasi P(Head) = 0.5
# =============================================

def simulasi_koin(n_lemparan):
    """Simulasi pelemparan koin sebanyak n kali."""
    # 0 = Tail, 1 = Head
    hasil = np.random.choice(['Head', 'Tail'], size=n_lemparan)
    n_head = np.sum(hasil == 'Head')
    proporsi_head = n_head / n_lemparan
    return hasil, n_head, proporsi_head

# Simulasi dengan berbagai jumlah lemparan
jumlah_lemparan = [10, 100, 1_000, 10_000, 100_000, 1_000_000]

print("=" * 55)
print(f"{'N Lemparan':>12} | {'Head':>8} | {'P(Head)':>10} | {'Error':>10}")
print("=" * 55)

for n in jumlah_lemparan:
    _, n_head, p_head = simulasi_koin(n)
    error = abs(p_head - 0.5)
    print(f"{n:>12,} | {n_head:>8,} | {p_head:>10.6f} | {error:>10.6f}")

print("\nTeori: P(Head) = 0.5")
print("Semakin banyak lemparan, semakin dekat P(Head) ke 0.5")
print("-> Ini adalah Hukum Bilangan Besar (Law of Large Numbers)")
```

### Langkah 3: Visualisasi Law of Large Numbers

```python
# =============================================
# LANGKAH 3: Visualisasi Law of Large Numbers
# =============================================

n_max = 5000
lemparan = np.random.choice([0, 1], size=n_max)  # 0=Tail, 1=Head

# Hitung proporsi kumulatif
proporsi_kumulatif = np.cumsum(lemparan) / np.arange(1, n_max + 1)

plt.figure(figsize=(12, 5))
plt.plot(range(1, n_max + 1), proporsi_kumulatif, color='steelblue',
         linewidth=0.8, alpha=0.8)
plt.axhline(y=0.5, color='red', linestyle='--', linewidth=2, label='P(Head) = 0.5 (teoritis)')
plt.xlabel('Jumlah Lemparan', fontsize=12)
plt.ylabel('Proporsi Head', fontsize=12)
plt.title('Law of Large Numbers: Konvergensi P(Head) ke 0.5', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.ylim(0.3, 0.7)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

print(f"Setelah {n_max} lemparan: P(Head) = {proporsi_kumulatif[-1]:.4f}")
```

### Langkah 4: Simulasi Pelemparan Dadu

```python
# =============================================
# LANGKAH 4: Simulasi Dadu - Verifikasi Uniform
# =============================================

n_lempar = 60_000
dadu = np.random.randint(1, 7, size=n_lempar)

# Hitung frekuensi setiap sisi
nilai_unik, frekuensi = np.unique(dadu, return_counts=True)
proporsi = frekuensi / n_lempar
teoritis = 1/6

print("=== SIMULASI PELEMPARAN DADU ===")
print(f"Jumlah lemparan: {n_lempar:,}")
print(f"\n{'Sisi':>6} | {'Frekuensi':>10} | {'Proporsi':>10} | {'Teoritis':>10} | {'Error':>10}")
print("-" * 60)
for s, f, p in zip(nilai_unik, frekuensi, proporsi):
    print(f"{s:>6} | {f:>10,} | {p:>10.4f} | {teoritis:>10.4f} | {abs(p-teoritis):>10.4f}")

# Visualisasi
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Bar chart frekuensi
colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6', '#1abc9c']
axes[0].bar(nilai_unik, frekuensi, color=colors, edgecolor='white')
axes[0].axhline(y=n_lempar/6, color='red', linestyle='--', label=f'Ekspektasi: {n_lempar/6:.0f}')
axes[0].set_title(f'Frekuensi Hasil Dadu ({n_lempar:,} lemparan)', fontsize=13, fontweight='bold')
axes[0].set_xlabel('Sisi Dadu')
axes[0].set_ylabel('Frekuensi')
axes[0].legend()

# Simulasi jumlah dua dadu
dadu1 = np.random.randint(1, 7, size=n_lempar)
dadu2 = np.random.randint(1, 7, size=n_lempar)
jumlah_dua_dadu = dadu1 + dadu2

axes[1].hist(jumlah_dua_dadu, bins=np.arange(1.5, 13.5, 1), color='steelblue',
             edgecolor='white', density=True, alpha=0.8)
axes[1].set_title('Distribusi Jumlah Dua Dadu', fontsize=13, fontweight='bold')
axes[1].set_xlabel('Jumlah Dua Dadu')
axes[1].set_ylabel('Probabilitas')
axes[1].set_xticks(range(2, 13))

# Overlay probabilitas teoritis
jumlah_teoritis = range(2, 13)
prob_teoritis = [sum(1 for a in range(1,7) for b in range(1,7) if a+b==s)/36
                 for s in jumlah_teoritis]
axes[1].plot(jumlah_teoritis, prob_teoritis, 'ro-', linewidth=2,
             markersize=6, label='Teoritis')
axes[1].legend()

plt.tight_layout()
plt.show()
```

### Langkah 5: Simulasi Monty Hall Problem

```python
# =============================================
# LANGKAH 5: Monty Hall Problem
# =============================================

# Deskripsi masalah:
# - Ada 3 pintu: di balik 1 pintu ada mobil, 2 pintu lainnya ada kambing
# - Anda memilih satu pintu
# - Host (yang tahu isi pintu) membuka salah satu pintu lain yang berisi kambing
# - Anda diberi pilihan: tetap (stay) atau pindah (switch)?
# - Pertanyaan: Strategi mana yang lebih baik?

def monty_hall_simulasi(n_simulasi, strategi='switch'):
    """
    Simulasi Monty Hall Problem.

    Parameters:
    - n_simulasi: jumlah simulasi
    - strategi: 'switch' (pindah pintu) atau 'stay' (tetap)

    Returns:
    - proporsi kemenangan
    """
    menang = 0

    for _ in range(n_simulasi):
        # Setup: mobil di salah satu dari 3 pintu (0, 1, 2)
        pintu_mobil = np.random.randint(0, 3)

        # Pemain memilih pintu secara acak
        pilihan_pemain = np.random.randint(0, 3)

        # Host membuka pintu yang bukan pilihan pemain DAN bukan pintu mobil
        pintu_tersedia = [p for p in range(3) if p != pilihan_pemain and p != pintu_mobil]
        pintu_dibuka_host = np.random.choice(pintu_tersedia)

        if strategi == 'switch':
            # Pindah ke pintu yang tersisa
            pilihan_akhir = [p for p in range(3) if p != pilihan_pemain and p != pintu_dibuka_host][0]
        else:
            # Tetap di pilihan awal
            pilihan_akhir = pilihan_pemain

        if pilihan_akhir == pintu_mobil:
            menang += 1

    return menang / n_simulasi

# Jalankan simulasi
n_sim = 10_000

p_stay = monty_hall_simulasi(n_sim, strategi='stay')
p_switch = monty_hall_simulasi(n_sim, strategi='switch')

print("=" * 50)
print("MONTY HALL PROBLEM - SIMULASI")
print("=" * 50)
print(f"Jumlah simulasi: {n_sim:,}")
print(f"\nStrategi TETAP (stay)  : P(menang) = {p_stay:.4f}")
print(f"Strategi PINDAH (switch): P(menang) = {p_switch:.4f}")
print(f"\nTeori: P(stay) = 1/3 = {1/3:.4f}")
print(f"Teori: P(switch) = 2/3 = {2/3:.4f}")
print(f"\nKesimpulan: {'PINDAH lebih baik!' if p_switch > p_stay else 'Hasil tidak sesuai teori'}")
```

### Langkah 6: Visualisasi Konvergensi Monty Hall

```python
# =============================================
# LANGKAH 6: Konvergensi Monty Hall
# =============================================

n_max = 5000
menang_stay = np.zeros(n_max)
menang_switch = np.zeros(n_max)

for i in range(n_max):
    pintu_mobil = np.random.randint(0, 3)
    pilihan = np.random.randint(0, 3)

    # Stay: menang jika pilihan = mobil
    menang_stay[i] = 1 if pilihan == pintu_mobil else 0

    # Switch: menang jika pilihan != mobil (karena pasti pindah ke mobil)
    menang_switch[i] = 1 if pilihan != pintu_mobil else 0

# Proporsi kumulatif
kum_stay = np.cumsum(menang_stay) / np.arange(1, n_max + 1)
kum_switch = np.cumsum(menang_switch) / np.arange(1, n_max + 1)

plt.figure(figsize=(12, 6))
plt.plot(range(1, n_max + 1), kum_stay, label='Stay (Tetap)', color='#e74c3c', alpha=0.8)
plt.plot(range(1, n_max + 1), kum_switch, label='Switch (Pindah)', color='#2ecc71', alpha=0.8)
plt.axhline(y=1/3, color='#e74c3c', linestyle='--', alpha=0.5, label='Teori Stay = 1/3')
plt.axhline(y=2/3, color='#2ecc71', linestyle='--', alpha=0.5, label='Teori Switch = 2/3')
plt.xlabel('Jumlah Simulasi', fontsize=12)
plt.ylabel('Proporsi Kemenangan', fontsize=12)
plt.title('Monty Hall Problem: Konvergensi ke Probabilitas Teoritis',
          fontsize=14, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(alpha=0.3)
plt.ylim(0, 1)
plt.tight_layout()
plt.show()
```

### Langkah 7: Teorema Bayes - Perhitungan

```python
# =============================================
# LANGKAH 7: Teorema Bayes
# =============================================

# Skenario: Tes penyakit
# - Prevalensi penyakit: P(D) = 0.01 (1%)
# - Sensitivitas (true positive rate): P(+|D) = 0.95
# - Spesifisitas (true negative rate): P(-|~D) = 0.90
# - False positive rate: P(+|~D) = 1 - 0.90 = 0.10

# Pertanyaan: Jika seseorang positif, berapa P(D|+)?

P_D = 0.01        # P(sakit)
P_notD = 1 - P_D  # P(sehat)
P_pos_D = 0.95    # P(positif | sakit) - sensitivitas
P_pos_notD = 0.10 # P(positif | sehat) - false positive rate

# Teorema Bayes: P(D|+) = P(+|D) * P(D) / P(+)
# P(+) = P(+|D)*P(D) + P(+|~D)*P(~D)
P_pos = P_pos_D * P_D + P_pos_notD * P_notD

P_D_pos = (P_pos_D * P_D) / P_pos

print("=" * 55)
print("TEOREMA BAYES: Tes Penyakit")
print("=" * 55)
print(f"P(Sakit)                  = {P_D:.4f} ({P_D*100:.1f}%)")
print(f"P(Sehat)                  = {P_notD:.4f}")
print(f"P(Positif | Sakit)        = {P_pos_D:.4f} (Sensitivitas)")
print(f"P(Positif | Sehat)        = {P_pos_notD:.4f} (False Positive)")
print(f"P(Positif)                = {P_pos:.4f}")
print(f"\nP(Sakit | Positif) = {P_D_pos:.4f} ({P_D_pos*100:.1f}%)")
print(f"\nInterpretasi: Meskipun tes positif, probabilitas benar-benar sakit")
print(f"hanya {P_D_pos*100:.1f}%! Ini karena prevalensi penyakit sangat rendah.")
print(f"Ini dikenal sebagai 'Base Rate Fallacy'.")
```

### Langkah 8: Simulasi Teorema Bayes

```python
# =============================================
# LANGKAH 8: Simulasi Teorema Bayes
# =============================================

n_populasi = 1_000_000

# Simulasi populasi
sakit = np.random.choice([True, False], size=n_populasi, p=[P_D, P_notD])

# Simulasi hasil tes
hasil_tes = np.zeros(n_populasi, dtype=bool)
for i in range(n_populasi):
    if sakit[i]:
        hasil_tes[i] = np.random.random() < P_pos_D   # true positive
    else:
        hasil_tes[i] = np.random.random() < P_pos_notD  # false positive

# Hitung
n_sakit = np.sum(sakit)
n_positif = np.sum(hasil_tes)
n_sakit_dan_positif = np.sum(sakit & hasil_tes)  # True Positive
n_sehat_dan_positif = np.sum(~sakit & hasil_tes)  # False Positive

P_D_pos_sim = n_sakit_dan_positif / n_positif

print("=" * 55)
print("SIMULASI TEOREMA BAYES (n=1,000,000)")
print("=" * 55)
print(f"Jumlah sakit        : {n_sakit:>10,} ({n_sakit/n_populasi*100:.2f}%)")
print(f"Jumlah tes positif  : {n_positif:>10,} ({n_positif/n_populasi*100:.2f}%)")
print(f"True Positive       : {n_sakit_dan_positif:>10,}")
print(f"False Positive      : {n_sehat_dan_positif:>10,}")
print(f"\nP(Sakit | Positif) simulasi = {P_D_pos_sim:.4f} ({P_D_pos_sim*100:.1f}%)")
print(f"P(Sakit | Positif) teoritis = {P_D_pos:.4f} ({P_D_pos*100:.1f}%)")

# Confusion matrix visual
print(f"\n{'':>20} {'Sakit':>12} {'Sehat':>12} {'Total':>12}")
print("-" * 60)
tp = n_sakit_dan_positif
fp = n_sehat_dan_positif
fn = np.sum(sakit & ~hasil_tes)
tn = np.sum(~sakit & ~hasil_tes)
print(f"{'Tes Positif':>20} {tp:>12,} {fp:>12,} {tp+fp:>12,}")
print(f"{'Tes Negatif':>20} {fn:>12,} {tn:>12,} {fn+tn:>12,}")
print(f"{'Total':>20} {tp+fn:>12,} {fp+tn:>12,} {n_populasi:>12,}")
```

### Langkah 9: Bayes dengan Berbagai Prevalensi

```python
# =============================================
# LANGKAH 9: Dampak Prevalensi terhadap Bayes
# =============================================

prevalensi_list = np.arange(0.001, 0.20, 0.001)
ppv_list = []  # Positive Predictive Value = P(D|+)

for prev in prevalensi_list:
    p_pos = P_pos_D * prev + P_pos_notD * (1 - prev)
    ppv = (P_pos_D * prev) / p_pos
    ppv_list.append(ppv)

plt.figure(figsize=(10, 6))
plt.plot(prevalensi_list * 100, np.array(ppv_list) * 100, color='steelblue', linewidth=2)
plt.xlabel('Prevalensi Penyakit (%)', fontsize=12)
plt.ylabel('P(Sakit | Tes Positif) (%)', fontsize=12)
plt.title('Dampak Prevalensi terhadap Positive Predictive Value\n'
          f'(Sensitivitas={P_pos_D*100:.0f}%, Spesifisitas={100-P_pos_notD*100:.0f}%)',
          fontsize=13, fontweight='bold')
plt.grid(alpha=0.3)

# Anotasi titik prevalensi 1%
plt.axvline(x=1, color='red', linestyle='--', alpha=0.5)
plt.annotate(f'Prevalensi 1%\nPPV = {P_D_pos*100:.1f}%',
             xy=(1, P_D_pos*100), xytext=(5, 60),
             arrowprops=dict(arrowstyle='->', color='red'),
             fontsize=11, color='red')

plt.tight_layout()
plt.show()

print("Insight: Semakin rendah prevalensi, semakin rendah PPV.")
print("Inilah mengapa screening massal untuk penyakit langka bisa menyesatkan.")
```

### Langkah 10: Simulasi Tambahan - Birthday Problem

```python
# =============================================
# LANGKAH 10: Birthday Problem (Bonus Simulasi)
# =============================================

# Pertanyaan: Berapa probabilitas setidaknya 2 orang dalam ruangan
# memiliki ulang tahun yang sama?

def simulasi_birthday(n_orang, n_simulasi=10_000):
    """Simulasi birthday problem."""
    cocok = 0
    for _ in range(n_simulasi):
        ulang_tahun = np.random.randint(1, 366, size=n_orang)
        if len(ulang_tahun) != len(set(ulang_tahun)):
            cocok += 1
    return cocok / n_simulasi

# Hitung probabilitas teoritis
def birthday_teoritis(n):
    """Hitung P(match) secara teoritis."""
    p_no_match = 1.0
    for i in range(n):
        p_no_match *= (365 - i) / 365
    return 1 - p_no_match

# Simulasi untuk berbagai ukuran ruangan
ukuran = list(range(2, 61))
prob_sim = [simulasi_birthday(n, 10_000) for n in ukuran]
prob_teori = [birthday_teoritis(n) for n in ukuran]

plt.figure(figsize=(10, 6))
plt.plot(ukuran, prob_sim, 'o', markersize=3, alpha=0.6, label='Simulasi (10,000x)')
plt.plot(ukuran, prob_teori, '-', color='red', linewidth=2, label='Teoritis')
plt.axhline(y=0.5, color='gray', linestyle='--', alpha=0.5)
plt.axvline(x=23, color='green', linestyle='--', alpha=0.5)
plt.annotate('23 orang -> P > 50%', xy=(23, 0.5), xytext=(30, 0.35),
             arrowprops=dict(arrowstyle='->', color='green'),
             fontsize=11, color='green', fontweight='bold')

plt.xlabel('Jumlah Orang dalam Ruangan', fontsize=12)
plt.ylabel('P(setidaknya 2 orang ulang tahun sama)', fontsize=12)
plt.title('Birthday Problem: Simulasi vs Teoritis', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

print("Fakta mengejutkan: Hanya butuh 23 orang agar probabilitas")
print("setidaknya 2 orang memiliki ulang tahun yang sama > 50%!")
```

---

## Tugas yang Harus Dikumpulkan

Kumpulkan notebook (.ipynb) yang berisi:

1. **Semua kode** dari Langkah 1-10 yang sudah dijalankan (tanpa error)
2. **Tabel perbandingan** simulasi vs teoritis untuk:
   - Koin (minimal 5 ukuran sampel berbeda)
   - Dadu (frekuensi setiap sisi)
   - Monty Hall (stay vs switch)
3. **Interpretasi tertulis** (text cell) untuk setiap eksperimen:
   - Apa yang Anda pelajari dari simulasi ini?
   - Bagaimana simulasi membantu memahami konsep probabilitas?

---

## Rubrik Singkat

| Kriteria | Bobot | Keterangan |
|----------|-------|------------|
| Kelengkapan kode | 30% | Semua langkah 1-10 dijalankan tanpa error |
| Tabel perbandingan | 25% | Tabel simulasi vs teoritis lengkap dan akurat |
| Interpretasi | 25% | Penjelasan jelas dan menunjukkan pemahaman konsep |
| Kerapian notebook | 10% | Terstruktur rapi dengan text cell |
| Visualisasi | 10% | Grafik bersih, informatif, dengan label |

---

## Challenge / Bonus

```python
# =============================================
# CHALLENGE: Gambler's Ruin Problem
# =============================================

# Seorang penjudi mulai dengan modal Rp 50.
# Setiap taruhan: menang +Rp 10 (p=0.5) atau kalah -Rp 10 (p=0.5)
# Berhenti jika: modal = 0 (bangkrut) atau modal = 100 (target tercapai)

def gamblers_ruin(modal_awal=50, target=100, p_menang=0.5):
    """Simulasi satu sesi gambler's ruin."""
    modal = modal_awal
    history = [modal]

    while 0 < modal < target:
        if np.random.random() < p_menang:
            modal += 10
        else:
            modal -= 10
        history.append(modal)

    return history, modal == target

# Simulasi 10 sesi
fig, ax = plt.subplots(figsize=(12, 6))

n_sesi = 10
menang = 0
for i in range(n_sesi):
    history, is_win = gamblers_ruin()
    color = 'green' if is_win else 'red'
    ax.plot(history, color=color, alpha=0.5, linewidth=1)
    if is_win:
        menang += 1

ax.axhline(y=0, color='red', linestyle='--', alpha=0.3, label='Bangkrut (0)')
ax.axhline(y=100, color='green', linestyle='--', alpha=0.3, label='Target (100)')
ax.axhline(y=50, color='gray', linestyle='--', alpha=0.3, label='Modal Awal (50)')
ax.set_xlabel('Langkah', fontsize=12)
ax.set_ylabel('Modal (Rp)', fontsize=12)
ax.set_title(f"Gambler's Ruin: {n_sesi} Sesi (Hijau=menang, Merah=bangkrut)\n"
             f"Menang: {menang}/{n_sesi}", fontsize=13, fontweight='bold')
ax.legend()
plt.tight_layout()
plt.show()

# Simulasi banyak kali untuk estimasi probabilitas
n_sim = 10_000
hasil = [gamblers_ruin()[1] for _ in range(n_sim)]
p_menang_sim = sum(hasil) / n_sim
print(f"\nSimulasi {n_sim:,} sesi:")
print(f"P(menang/capai target) = {p_menang_sim:.4f}")
print(f"P(bangkrut) = {1-p_menang_sim:.4f}")
print(f"Teori (p=0.5): P(menang) = modal_awal/target = 50/100 = 0.5000")
```

---

> **Catatan:** Semua simulasi menggunakan `np.random.seed()` untuk reproducibility. Namun, setiap kali Anda menjalankan ulang sel tanpa seed, hasilnya akan sedikit berbeda -- dan itu normal! Yang penting adalah rata-rata simulasi mendekati nilai teoritis.
