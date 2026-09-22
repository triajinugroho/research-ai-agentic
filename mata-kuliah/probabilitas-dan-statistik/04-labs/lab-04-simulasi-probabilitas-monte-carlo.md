# Lab 04: Simulasi Probabilitas Monte Carlo

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Probabilitas dan Statistik (IF52510033) |
| **Minggu** | 4 |
| **Durasi** | 180 menit (mandiri) |
| **Prasyarat** | Lab 03 selesai; materi Minggu 4 |
| **Sub-CPMK** | `PS-Sub-CPMK102-1` |
| **Bobot** | 1,92% |

---

## Tujuan Praktikum

1. Menghitung probabilitas secara analitis dengan kaidah pencacahan.
2. Memverifikasi hasil analitis dengan simulasi Monte Carlo.
3. Menunjukkan Hukum Bilangan Besar secara empiris.
4. Menghitung probabilitas bersyarat dari data simulasi.
5. Menjelaskan kapan simulasi lebih praktis daripada perhitungan analitis.

---

## Persiapan

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import comb, perm, factorial
from itertools import product, permutations, combinations

rng = np.random.default_rng(42)   # seed agar hasil dapat direproduksi
```

> **Catatan reproduksibilitas.** Selalu tetapkan *seed* pada pekerjaan yang akan diserahkan. Tanpa *seed*, dosen tidak dapat memverifikasi hasil Anda — dan Anda sendiri tidak dapat mengulanginya.

---

## Langkah-langkah

### Langkah 1: Ruang Sampel dan Kejadian

```python
# =============================================
# LANGKAH 1: Membangun ruang sampel
# =============================================

# Pengujian tiga modul: setiap modul Lulus (L) atau Gagal (G)
ruang_sampel = list(product(["L", "G"], repeat=3))

print(f"Ukuran ruang sampel |S| = {len(ruang_sampel)}")
for i, hasil in enumerate(ruang_sampel, 1):
    print(f"  {i}. {''.join(hasil)}")

# Kejadian A: tepat satu modul gagal
A = [h for h in ruang_sampel if h.count("G") == 1]
# Kejadian B: modul pertama gagal
B = [h for h in ruang_sampel if h[0] == "G"]

print(f"\nA = tepat satu gagal      : {[''.join(h) for h in A]}")
print(f"B = modul pertama gagal   : {[''.join(h) for h in B]}")
print(f"A ∩ B                     : {[''.join(h) for h in set(A) & set(B)]}")

n = len(ruang_sampel)
print(f"\nP(A) = {len(A)}/{n} = {len(A)/n:.4f}")
print(f"P(B) = {len(B)}/{n} = {len(B)/n:.4f}")
print(f"P(A ∩ B) = {len(set(A) & set(B))}/{n} = {len(set(A) & set(B))/n:.4f}")
print(f"P(A | B) = {len(set(A) & set(B))/len(B):.4f}")
```

> **Catatan penting:** perhitungan di atas **mengandaikan seluruh hasil berpeluang sama** — yaitu setiap modul gagal dengan probabilitas 0,5. Bila probabilitas gagal sebenarnya 0,2, perhitungannya berbeda. Ini asumsi yang sering dilupakan.

### Langkah 2: Hukum Bilangan Besar

```python
# =============================================
# LANGKAH 2: Hukum Bilangan Besar
# =============================================

p_sebenarnya = 0.3      # probabilitas satu permintaan gagal
ulangan_maks = 50_000

hasil = rng.random(ulangan_maks) < p_sebenarnya
proporsi_berjalan = np.cumsum(hasil) / np.arange(1, ulangan_maks + 1)

plt.figure(figsize=(11, 5))
plt.plot(proporsi_berjalan, linewidth=0.9, color="steelblue")
plt.axhline(p_sebenarnya, color="#c0392b", linestyle="--", linewidth=2,
            label=f"p sebenarnya = {p_sebenarnya}")
plt.xscale("log")
plt.xlabel("Jumlah percobaan (skala log)")
plt.ylabel("Proporsi kumulatif")
plt.title("Hukum Bilangan Besar: proporsi mendekati probabilitas sebenarnya")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

print(f"{'Ulangan':>10}  {'Proporsi':>10}  {'Selisih':>10}")
for n_u in [10, 100, 1_000, 10_000, 50_000]:
    prop = proporsi_berjalan[n_u - 1]
    print(f"{n_u:>10,}  {prop:>10.4f}  {abs(prop - p_sebenarnya):>10.4f}")
```

> **Tulis interpretasi:** pada ulangan ke-10, seberapa jauh proporsi dari nilai sebenarnya? Pada ulangan ke-50.000? Apa implikasinya bagi seseorang yang menarik kesimpulan dari 10 pengamatan saja?

### Langkah 3: Verifikasi Analitis dengan Simulasi

```python
# =============================================
# LANGKAH 3: Analitis vs simulasi
# =============================================

def simulasi_pilih_tim(n_backend=8, n_frontend=5, n_pilih=4,
                       target_backend=2, ulangan=200_000):
    """Memverifikasi C(8,2)·C(5,2)/C(13,4) dengan simulasi."""
    tim = np.array([1]*n_backend + [0]*n_frontend)   # 1=backend, 0=frontend
    berhasil = 0
    for _ in range(ulangan):
        terpilih = rng.choice(tim, size=n_pilih, replace=False)
        if terpilih.sum() == target_backend:
            berhasil += 1
    return berhasil / ulangan

analitis = comb(8, 2) * comb(5, 2) / comb(13, 4)
simulasi = simulasi_pilih_tim()

print("Masalah: dari 8 backend dan 5 frontend, dipilih 4 orang.")
print("Berapa P(tepat 2 backend dan 2 frontend)?\n")
print(f"  Analitis : C(8,2)·C(5,2)/C(13,4) = {comb(8,2)}·{comb(5,2)}/{comb(13,4)}"
      f" = {analitis:.6f}")
print(f"  Simulasi : {simulasi:.6f}")
print(f"  Selisih  : {abs(analitis - simulasi):.6f}")
```

### Langkah 4: Masalah Ulang Tahun (Birthday Problem)

Contoh klasik ketika intuisi manusia keliru — dan relevan untuk *hash collision*.

```python
# =============================================
# LANGKAH 4: Masalah ulang tahun dan hash collision
# =============================================

def p_ada_kesamaan_analitis(n, ruang=365):
    """P(sedikitnya dua orang berulang tahun sama)."""
    if n > ruang:
        return 1.0
    p_semua_beda = 1.0
    for i in range(n):
        p_semua_beda *= (ruang - i) / ruang
    return 1 - p_semua_beda

def p_ada_kesamaan_simulasi(n, ruang=365, ulangan=20_000):
    """Verifikasi dengan simulasi."""
    cocok = 0
    for _ in range(ulangan):
        hari = rng.integers(0, ruang, n)
        if len(np.unique(hari)) < n:
            cocok += 1
    return cocok / ulangan

print(f"{'n orang':>9}  {'Analitis':>10}  {'Simulasi':>10}")
for n_orang in [5, 10, 23, 30, 50, 70]:
    a = p_ada_kesamaan_analitis(n_orang)
    s = p_ada_kesamaan_simulasi(n_orang)
    print(f"{n_orang:>9}  {a:>10.4f}  {s:>10.4f}")

print("\n→ Dengan hanya 23 orang, peluangnya sudah melebihi 50%.")
print("  Intuisi kebanyakan orang menebak jauh lebih rendah.")
```

```python
# Kaitannya dengan hash collision
print("\nPenerapan: hash collision")
print("Bila fungsi hash menghasilkan k bit, ruang keluarannya 2^k.")
print("Jumlah masukan sebelum peluang tabrakan mencapai 50%:\n")
for k in [16, 32, 64, 128]:
    ruang = 2 ** k
    # Hampiran: n ≈ 1,177 × sqrt(ruang)
    n_50 = 1.1774 * np.sqrt(ruang)
    print(f"  hash {k:>3} bit (ruang 2^{k}) → sekitar {n_50:.3e} masukan")
print("\n→ Inilah yang disebut 'birthday attack' dalam kriptografi.")
```

### Langkah 5: Probabilitas Bersyarat dari Simulasi

```python
# =============================================
# LANGKAH 5: Probabilitas bersyarat dari data
# =============================================

# Simulasi 500 permintaan API dengan sifat yang saling berkaitan
n_permintaan = 500

# Permintaan yang melewati modul lama lebih mungkin lambat DAN galat
lewat_modul_lama = rng.random(n_permintaan) < 0.30
p_lambat = np.where(lewat_modul_lama, 0.45, 0.08)
p_galat = np.where(lewat_modul_lama, 0.25, 0.04)

lambat = rng.random(n_permintaan) < p_lambat
galat = rng.random(n_permintaan) < p_galat

log = pd.DataFrame({
    "modul_lama": lewat_modul_lama,
    "lambat": lambat,
    "galat": galat,
})

print("=== TABEL KONTINGENSI ===")
print(pd.crosstab(log["lambat"], log["galat"],
                  rownames=["Lambat"], colnames=["Galat"]))

# Menghitung berbagai probabilitas dari data
p_l = log["lambat"].mean()
p_g = log["galat"].mean()
p_lg = (log["lambat"] & log["galat"]).mean()

print(f"\nP(lambat)              = {p_l:.4f}")
print(f"P(galat)               = {p_g:.4f}")
print(f"P(lambat ∩ galat)      = {p_lg:.4f}")
print(f"P(lambat ∪ galat)      = {p_l + p_g - p_lg:.4f}")
print(f"P(galat | lambat)      = {p_lg/p_l:.4f}")
print(f"P(lambat | galat)      = {p_lg/p_g:.4f}")

# Uji kebebasan secara kasar
print(f"\nP(lambat)×P(galat)     = {p_l*p_g:.4f}")
print(f"P(lambat ∩ galat)      = {p_lg:.4f}")
print(f"Selisih                = {abs(p_lg - p_l*p_g):.4f}")
print("→ Selisih besar menandakan lambat dan galat TIDAK bebas.")
print("  (Uji formalnya adalah chi-square kebebasan — Minggu 13.)")
```

---

## Tantangan Tambahan

### Tantangan 1: Masalah Monty Hall

Simulasikan masalah Monty Hall untuk membuktikan bahwa berganti pintu memberi peluang 2/3.

```python
def monty_hall(berganti, ulangan=100_000):
    """
    Tiga pintu, satu berisi hadiah.
    Peserta memilih satu, pembawa acara membuka pintu kosong lain,
    lalu peserta boleh bertahan atau berganti.
    """
    menang = 0
    for _ in range(ulangan):
        hadiah = rng.integers(0, 3)
        pilihan = rng.integers(0, 3)

        # TUGAS ANDA: lengkapi
        # 1. Pembawa acara membuka pintu yang BUKAN pilihan peserta
        #    dan BUKAN pintu berhadiah
        # 2. Bila berganti, peserta pindah ke pintu ketiga
        # 3. Hitung apakah menang

        pass

    return menang / ulangan

# print(f"Bertahan : {monty_hall(False):.4f}  (harapan ≈ 0,3333)")
# print(f"Berganti : {monty_hall(True):.4f}   (harapan ≈ 0,6667)")
```

**Pertanyaan:** jelaskan **mengapa** berganti lebih baik, menggunakan konsep probabilitas bersyarat dari Minggu 4.

### Tantangan 2: Keandalan Sistem

Simulasikan keandalan sistem dengan susunan seri dan paralel.

```python
def simulasi_keandalan(r_komponen, n, susunan, ulangan=100_000):
    """
    Simulasi keandalan sistem.
    susunan: 'seri' (semua harus hidup) atau 'paralel' (cukup satu)
    """
    # TUGAS ANDA: lengkapi, lalu bandingkan dengan rumus analitis
    # seri    : r^n
    # paralel : 1 − (1−r)^n
    pass

# Bandingkan hasil simulasi dengan analitis untuk:
#   r = 0.99, n = 1, 2, 3, 5, 10, susunan seri dan paralel
```

**Pertanyaan:** sebuah layanan terdiri dari 8 mikroservis yang harus semuanya hidup. Bila masing-masing andal 99,5%, berapa keandalan sistemnya? Apa saran Anda kepada tim arsitektur?

### Tantangan 3: Kapan Simulasi Lebih Praktis

Cari satu persoalan probabilitas yang **sangat sulit atau tidak praktis** dihitung analitis, lalu selesaikan dengan simulasi.

Saran persoalan:
- Probabilitas sebuah *quicksort* dengan pivot acak memerlukan lebih dari 2n log n perbandingan.
- Probabilitas antrean pada sebuah loket melebihi 10 orang, bila kedatangan Poisson dan layanan Eksponensial.
- Probabilitas sedikitnya satu dari 20 mikroservis mengalami gangguan bersamaan, bila gangguan **berkorelasi**.

Laporkan: rumusan masalah, mengapa sulit dihitung analitis, kode simulasi, hasil, dan estimasi ketidakpastiannya.

---

## Refleksi

1. Dalam kasus apa Anda lebih memilih simulasi daripada perhitungan analitis?
2. Apa risiko terbesar dari mengandalkan simulasi saja?
3. Mengapa menetapkan *seed* penting dalam pekerjaan ilmiah?

---

## AI Usage Log

| No | Tanggal | Alat AI | Untuk apa | Prompt (ringkas) | Apa yang saya ubah/verifikasi |
|----|---------|---------|-----------|------------------|-------------------------------|
| 1 | | | | | |

> Nama: ______________  NIM: ______________

---

## Checklist Penyelesaian

- [ ] Notebook dinamai `Lab04_NIM_NamaLengkap.ipynb`
- [ ] *Seed* ditetapkan di awal notebook
- [ ] Langkah 1–5 selesai
- [ ] Setiap hasil simulasi dibandingkan dengan hasil analitis (bila ada)
- [ ] Ketiga tantangan dikerjakan, termasuk melengkapi kode yang kosong
- [ ] Refleksi terisi
- [ ] AI Usage Log terisi
- [ ] Diunggah ke LMS

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
