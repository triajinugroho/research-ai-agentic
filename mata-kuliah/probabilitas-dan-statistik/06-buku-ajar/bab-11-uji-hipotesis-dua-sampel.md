# BAB 11: UJI HIPOTESIS DUA SAMPEL DAN PROPORSI

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `PS-Sub-CPMK102-1` | Memilih uji yang tepat berdasarkan rancangan dan sifat data | C4 |
| `PS-Sub-CPMK102-1` | Menjalankan uji-t dua sampel dan berpasangan dengan pemeriksaan asumsi | C3 |
| `PS-Sub-CPMK102-1` | Merancang dan menganalisis A/B test secara sahih | C4 |

---

## 11.1 Memilih Uji yang Tepat

Langkah pertama selalu **memilih uji**, bukan menghitung. Kesalahan di sini tidak dapat diperbaiki oleh perhitungan yang benar.

```
  Dua kelompok yang ingin dibandingkan
  │
  ├── BERPASANGAN? (subjek yang sama diukur dua kali,
  │   atau pasangan yang dijodohkan)
  │   │
  │   ├── YA  → selisih Normal?  ── ya ──→ UJI-T BERPASANGAN
  │   │                          └─ tidak → WILCOXON SIGNED-RANK
  │   │
  │   └── TIDAK (kelompok berbeda dan bebas)
  │       │
  │       ├── Data Normal (atau n besar)?
  │       │   ├── Ragam homogen? ── ya ──→ UJI-T pooled
  │       │   └──                  tidak → UJI-T WELCH  ← default aman
  │       │
  │       └── Tidak Normal dan n kecil → MANN-WHITNEY U
  │
  └── Data berupa PROPORSI → UJI PROPORSI DUA SAMPEL
```

> **Anjuran praktis:** untuk dua kelompok bebas, gunakan **uji-t Welch** sebagai pilihan awal.
>
> Ia tidak mengandaikan ragam homogen, dan bila ragamnya memang homogen hasilnya hampir sama dengan uji *pooled*. Penelitian Delacre dkk. (2017) menganjurkan Welch sebagai bawaan, karena uji *pooled* kehilangan keandalan ketika ragam berbeda dan ukuran kelompok tidak seimbang.

---

## 11.2 Uji-t Dua Sampel Bebas

### 11.2.1 Rumus

**Welch (ragam tidak diandaikan sama):**

$$t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}}}$$

**Pooled (ragam diandaikan sama):**

$$t = \frac{\bar{x}_1 - \bar{x}_2}{s_p\sqrt{\dfrac{1}{n_1}+\dfrac{1}{n_2}}}, \quad s_p^2 = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}$$

### 11.2.2 Asumsi dan Pemeriksaannya

| Asumsi | Cara memeriksa | Bila dilanggar |
|--------|----------------|----------------|
| Kebebasan antar dan dalam kelompok | Telaah rancangan | **Tidak ada perbaikan statistik** |
| Kenormalan (n kecil) | Shapiro-Wilk, Q-Q plot | Mann-Whitney U |
| Homogenitas ragam | Uji Levene | Gunakan Welch (bukan *pooled*) |

> **Mengapa uji Levene, bukan uji-F?** Uji-F untuk ragam sangat peka terhadap penyimpangan kenormalan — ia sering menolak homogenitas hanya karena datanya tidak Normal. Uji Levene (berbasis simpangan absolut dari median) jauh lebih *robust*.

### 11.2.3 Implementasi

```python
import numpy as np
import pandas as pd
from scipy import stats

def uji_dua_sampel(g1, g2, nama1="Kelompok 1", nama2="Kelompok 2", alpha=0.05):
    g1 = np.asarray(g1, dtype=float); g1 = g1[~np.isnan(g1)]
    g2 = np.asarray(g2, dtype=float); g2 = g2[~np.isnan(g2)]
    n1, n2 = len(g1), len(g2)

    print(f"{nama1:>20}: n={n1:>4} mean={g1.mean():>9.4f} s={g1.std(ddof=1):>8.4f}")
    print(f"{nama2:>20}: n={n2:>4} mean={g2.mean():>9.4f} s={g2.std(ddof=1):>8.4f}\n")

    _, p1 = stats.shapiro(g1[:5000]); _, p2 = stats.shapiro(g2[:5000])
    _, p_lev = stats.levene(g1, g2)
    print(f"Kenormalan {nama1:>14}: p = {p1:.6f}")
    print(f"Kenormalan {nama2:>14}: p = {p2:.6f}")
    print(f"Homogenitas ragam (Levene): p = {p_lev:.6f} "
          f"→ {'homogen' if p_lev > alpha else 'TIDAK homogen'}\n")

    tw, pw = stats.ttest_ind(g1, g2, equal_var=False)
    tp, pp = stats.ttest_ind(g1, g2, equal_var=True)
    u,  pu = stats.mannwhitneyu(g1, g2, alternative="two-sided")
    print(f"Uji-t Welch  : t={tw:>9.4f}  p={pw:.8f}  ← dianjurkan")
    print(f"Uji-t pooled : t={tp:>9.4f}  p={pp:.8f}")
    print(f"Mann-Whitney : U={u:>9.1f}  p={pu:.8f}\n")

    sp = np.sqrt(((n1-1)*g1.var(ddof=1) + (n2-1)*g2.var(ddof=1))/(n1+n2-2))
    d = (g1.mean() - g2.mean())/sp
    se = np.sqrt(g1.var(ddof=1)/n1 + g2.var(ddof=1)/n2)
    dfw = se**4 / ((g1.var(ddof=1)/n1)**2/(n1-1) + (g2.var(ddof=1)/n2)**2/(n2-1))
    tc = stats.t.ppf(1-alpha/2, dfw)
    selisih = g1.mean() - g2.mean()

    print(f"Selisih rata-rata : {selisih:.4f}")
    print(f"IK 95% selisih    : [{selisih-tc*se:.4f} , {selisih+tc*se:.4f}]")
    print(f"Cohen's d         : {d:.4f}")
    return {"p": pw, "d": d}

df = pd.read_csv("nilai_mahasiswa_if.csv")
uji_dua_sampel(df[df.kelas=="IF26A"]["nilai_uas"],
               df[df.kelas=="IF26H"]["nilai_uas"], "IF26A", "IF26H")
```

---

## 11.3 Uji-t Berpasangan

### 11.3.1 Kapan Dipakai

$$t = \frac{\bar{d}}{s_d/\sqrt{n}}, \quad df = n - 1$$

dengan d = selisih tiap pasangan.

| Rancangan | Contoh Informatika |
|-----------|--------------------|
| Sebelum–sesudah | Waktu eksekusi sebelum dan sesudah optimasi, pada **mesin yang sama** |
| Dua perlakuan pada subjek sama | Setiap pengguna mencoba kedua antarmuka |
| Pasangan dijodohkan | Dua server dengan spesifikasi identik, dipasangkan |

### 11.3.2 Mengapa Berpasangan Lebih Berkuasa

```python
import numpy as np
from scipy import stats

# 12 mesin yang SAMA, sebelum dan sesudah optimasi
sebelum = np.array([142, 158, 131, 176, 149, 163, 138, 155, 147, 169, 152, 144])
sesudah = np.array([128, 141, 122, 155, 133, 147, 125, 139, 134, 150, 138, 130])
selisih = sebelum - sesudah

print(f"Rata-rata penurunan : {selisih.mean():.4f} detik")
print(f"SD selisih          : {selisih.std(ddof=1):.4f}")
print(f"SD sebelum          : {sebelum.std(ddof=1):.4f}  ← jauh lebih besar!\n")

tp, pp = stats.ttest_rel(sebelum, sesudah)
ti, pi = stats.ttest_ind(sebelum, sesudah, equal_var=False)

print(f"Uji BERPASANGAN (benar)  : t={tp:>8.4f}  p={pp:.10f}")
print(f"Uji dua sampel (keliru)  : t={ti:>8.4f}  p={pi:.10f}")
print(f"\nRasio p: {pi/pp:,.0f}× lebih besar")
```

> **Mengapa selisihnya sebesar itu?**
>
> Perhatikan bahwa SD **selisih** (sekitar 3,4 detik) jauh lebih kecil daripada SD **sebelum** (sekitar 13,4 detik). Sebabnya: mesin-mesin itu memang berbeda kecepatannya, dan variasi antar mesin mendominasi.
>
> Uji berpasangan **menghilangkan variasi antar subjek** dengan hanya melihat selisih pada subjek yang sama. Uji dua sampel bebas tidak bisa melakukannya, sehingga efek yang nyata tenggelam dalam keragaman antar mesin.
>
> **Memakai uji yang salah membuang kuasa uji** — dan Anda bisa gagal menemukan efek yang sebenarnya ada.

---

## 11.4 Uji Proporsi dan A/B Testing

### 11.4.1 Uji Proporsi Dua Sampel

$$z = \frac{\hat{p}_1 - \hat{p}_2}{\sqrt{\hat{p}(1-\hat{p})\left(\frac{1}{n_1}+\frac{1}{n_2}\right)}}, \quad \hat{p} = \frac{x_1 + x_2}{n_1 + n_2}$$

```python
import numpy as np
from statsmodels.stats.proportion import proportions_ztest, confint_proportions_2indep

konv = np.array([148, 191])      # konversi grup A dan B
tot  = np.array([1000, 1000])
p1, p2 = konv / tot

z, p_value = proportions_ztest(konv, tot)
bawah, atas = confint_proportions_2indep(konv[1], tot[1], konv[0], tot[0],
                                         method="wald")

print(f"Grup A : {konv[0]}/{tot[0]} = {p1*100:.2f}%")
print(f"Grup B : {konv[1]}/{tot[1]} = {p2*100:.2f}%")
print(f"Selisih absolut  : {(p2-p1)*100:+.2f} poin persen")
print(f"Kenaikan relatif : {(p2-p1)/p1*100:+.2f}%")
print(f"\nz = {z:.4f}, p = {p_value:.8f}")
print(f"IK 95% selisih   : [{bawah*100:+.2f} , {atas*100:+.2f}] poin persen")
print(f"\n→ Kenaikan sebenarnya bisa serendah {bawah*100:.2f} pp.")
print("  Apakah itu masih membenarkan biaya penerapannya?")
```

> **Interval kepercayaan selisih lebih berguna bagi pengambil keputusan daripada *p-value*.**
>
> *p-value* menjawab "apakah ada perbedaan". Interval kepercayaan menjawab "seberapa besar perbedaannya, dan seberapa yakin kita" — dan pertanyaan kedua itulah yang menentukan keputusan bisnis.

### 11.4.2 Merancang A/B Test yang Sahih

| Tahap | Yang Harus Dilakukan | Kesalahan Umum |
|-------|----------------------|----------------|
| 1. Tetapkan metrik | **Satu** metrik utama, ditentukan di muka | Memilih metrik setelah melihat hasil |
| 2. Tetapkan efek minimum | Berdasarkan pertimbangan bisnis | Tidak ditetapkan sama sekali |
| 3. Hitung ukuran sampel | Dari efek minimum dan kuasa 0,80 | Menjalankan tanpa perhitungan |
| 4. Acak penugasan | Per pengguna, benar-benar acak | Membagi berdasarkan waktu atau lokasi |
| 5. Jalankan sampai selesai | Sesuai n yang dihitung | ***Peeking*** — berhenti saat signifikan |
| 6. Analisis satu kali | Uji sesuai rencana | Menggali banyak segmen sampai ada yang signifikan |
| 7. Laporkan lengkap | Efek, IK, keterbatasan | Hanya *p-value* |

```python
import numpy as np
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

def n_ab_test(p_dasar, kenaikan_min, alpha=0.05, kuasa=0.80):
    efek = proportion_effectsize(p_dasar + kenaikan_min, p_dasar)
    return int(np.ceil(NormalIndPower().solve_power(
        effect_size=efek, alpha=alpha, power=kuasa, ratio=1.0)))

p_dasar = 0.15
print(f"Konversi saat ini: {p_dasar*100:.1f}%\n")
print(f"{'Kenaikan minimum':>18}  {'n per grup':>12}  {'Total':>12}")
for kn in [0.05, 0.03, 0.02, 0.01, 0.005]:
    n = n_ab_test(p_dasar, kn)
    print(f"{kn*100:>15.1f} pp  {n:>12,}  {n*2:>12,}")
```

### 11.4.3 Bahaya *Peeking*

> Bila Anda memeriksa hasil A/B test setiap hari dan berhenti begitu p < 0,05, **tingkat galat Tipe I yang sebenarnya melonjak dari 5% ke lebih dari 25%**.

Alasannya sama seperti *p-hacking* pada Bab 10: setiap kali Anda "mengintip" dan mengambil keputusan, Anda pada dasarnya menjalankan satu uji lagi. Dua puluh kali intipan setara dengan dua puluh uji.

**Yang harus dilakukan:**
- Tetapkan n di muka.
- Jalankan sampai selesai.
- Analisis **satu kali**.

Bila pemantauan berkala benar-benar diperlukan (misalnya untuk menghentikan tes yang merugikan), gunakan metode **sequential testing** yang sudah memperhitungkan intipan berulang — bukan uji biasa.

---

## 11.5 Uji Nonparametrik

| Uji Parametrik | Padanan Nonparametrik | Yang Dibandingkan |
|----------------|-----------------------|-------------------|
| Uji-t satu sampel | Wilcoxon signed-rank | Median |
| Uji-t dua sampel bebas | Mann-Whitney U | Sebaran/median |
| Uji-t berpasangan | Wilcoxon signed-rank | Median selisih |
| ANOVA satu arah | Kruskal-Wallis | Sebaran/median |

| Aspek | Parametrik | Nonparametrik |
|-------|------------|---------------|
| Asumsi | Lebih ketat | Lebih longgar |
| Kuasa bila asumsi terpenuhi | Lebih tinggi | Sedikit lebih rendah (±95%) |
| Tahan pencilan | Tidak | Ya |
| Yang dibandingkan | Rata-rata | Median/sebaran |

> **Bila kesimpulan uji parametrik dan nonparametrik berbeda**, laporkan keduanya dan jelaskan mengapa Anda memilih salah satunya. Menyembunyikan yang tidak mendukung adalah pelaporan selektif.

---

## AI Corner — Tingkat Lanjut

### Kesalahan Paling Mahal: Uji yang Salah

AI tidak dapat mengetahui rancangan pengumpulan data Anda kecuali Anda ceritakan — dan pemula biasanya tidak menceritakannya karena tidak sadar bahwa itu menentukan.

**Percobaan:**

> *"Ini waktu eksekusi sebelum dan sesudah optimasi: [12 nilai] dan [12 nilai]. Apakah ada perbedaan signifikan?"*

Sebagian besar AI akan menjalankan uji **dua sampel bebas**. Padahal bila pengukurannya pada mesin yang sama, yang benar adalah uji **berpasangan** — dan bedanya bisa ribuan kali lipat pada *p-value*.

Sekarang tambahkan satu kalimat:

> *"Kedua pengukuran dilakukan pada 12 mesin yang sama."*

Sekarang AI akan memilih uji berpasangan.

> **Pelajarannya:** satu kalimat konteks mengubah seluruh analisis. Dan yang mengetahui kalimat itu perlu disampaikan, hanya Anda.

### Daftar Periksa Sebelum Menerima Hasil dari AI

- [ ] Apakah AI tahu rancangan pengumpulan data saya (berpasangan atau bebas)?
- [ ] Apakah ia memeriksa asumsi, atau langsung menghitung?
- [ ] Apakah ia memakai Welch atau *pooled*? Apakah pilihannya beralasan?
- [ ] Apakah ia melaporkan ukuran efek dan interval kepercayaan, bukan hanya *p*?
- [ ] Apakah kesimpulannya melampaui yang didukung data?

### Pemakaian yang Dianjurkan

```
PROMPT YANG BAIK:
"Rancangan: A/B test, 2 grup pengguna berbeda, dialokasikan acak,
 n=1000 per grup, metrik konversi (biner). Saya memilih uji proporsi
 dua sampel. Efek minimum bermakna yang saya tetapkan di muka: 2 poin
 persen. Apakah pilihan uji dan rancangan saya sahih? Apa yang perlu
 saya periksa sebelum menganalisis?"
```

---

## Latihan Soal

### Tingkat Dasar

1. Jelaskan perbedaan rancangan "dua sampel bebas" dan "berpasangan". Beri satu contoh masing-masing dari Informatika.

2. Mengapa uji-t Welch dianjurkan sebagai pilihan awal untuk dua kelompok bebas?

3. Dari dua kelompok: n₁=25, x̄₁=118, s₁=15; n₂=30, x̄₂=127, s₂=18. Hitung statistik t Welch.

4. Sebuah A/B test: grup A 120/800 konversi, grup B 156/800. Hitung kedua proporsi dan selisihnya dalam poin persen.

5. Sebutkan tiga asumsi uji-t dua sampel bebas dan cara memeriksa masing-masing.

### Tingkat Menengah

6. Sebuah tim mengukur waktu muat halaman pada 15 perangkat yang sama, sebelum dan sesudah optimasi gambar.
   (a) Rancangan ini berpasangan atau bebas? Jelaskan.
   (b) Uji apa yang tepat?
   (c) Bila mereka keliru memakai uji dua sampel bebas, apa akibatnya?
   (d) Asumsi apa yang perlu diperiksa untuk uji yang benar? (Petunjuk: pada **selisihnya**.)

7. Sebuah A/B test dijalankan dengan konversi dasar 12%. Tim ingin mendeteksi kenaikan minimal 1,5 poin persen.
   (a) Hitung n per grup untuk kuasa 0,80 dan α = 0,05.
   (b) Bila trafik 5.000 pengunjung per hari terbagi rata, berapa hari tes harus berjalan?
   (c) Pada hari ke-3 hasilnya sudah p = 0,04. Bolehkah tes dihentikan? Jelaskan.
   (d) Apa risiko menghentikannya lebih awal?

8. Bandingkan uji-t Welch, *pooled*, dan Mann-Whitney pada data dengan pencilan ekstrem.
   (a) Bangkitkan dua kelompok: satu normal, satu dengan 2 pencilan ekstrem.
   (b) Jalankan ketiga uji.
   (c) Mengapa kesimpulannya bisa berbeda?
   (d) Mana yang Anda laporkan, dan bagaimana Anda menjelaskan pilihan itu?

9. Sebuah laporan A/B test menyatakan: *"Fitur baru meningkatkan konversi 18% (p = 0,03). Kami merekomendasikan peluncuran penuh."*
   (a) Informasi apa yang hilang dari laporan itu?
   (b) Mengapa "kenaikan 18%" bisa menyesatkan? (Petunjuk: relatif vs absolut.)
   (c) Tuliskan ulang laporan itu secara lengkap dan jujur.

### Tingkat Mahir

10. Simulasikan dampak *peeking* pada A/B test.
    (a) Buat simulasi dengan H₀ **benar** (kedua grup identik).
    (b) Periksa hasil pada 1, 5, 10, dan 20 titik waktu; hentikan bila p < 0,05.
    (c) Hitung galat Tipe I empiris untuk tiap skenario.
    (d) Bandingkan dengan target 5%.
    (e) Jelaskan mengapa masalahnya identik dengan *p-hacking* pada Bab 10.
    (f) Cari dan jelaskan secara ringkas satu metode *sequential testing* yang mengatasi masalah ini.

11. Analisis A/B test dengan **metrik penjaga** (*guardrail metric*).
    (a) Jelaskan apa itu metrik penjaga dan mengapa diperlukan.
    (b) Rancang A/B test untuk fitur "rekomendasi konten" dengan metrik utama waktu-di-aplikasi dan dua metrik penjaga.
    (c) Bagaimana Anda menangani masalah perbandingan ganda dari beberapa metrik?
    (d) Apa yang Anda lakukan bila metrik utama membaik tetapi metrik penjaga memburuk?

12. Tulislah pedoman internal (satu halaman) berjudul *"Standar A/B Testing"* untuk tim produk. Sertakan: tahapan wajib, apa yang harus ditetapkan sebelum tes dimulai, aturan tentang *peeking*, format pelaporan minimum, dan daftar praktik yang dilarang.

---

## Rangkuman

1. **Langkah pertama adalah memilih uji**, bukan menghitung. Kesalahan di sini tidak dapat diperbaiki perhitungan yang benar.
2. Untuk dua kelompok bebas, **uji-t Welch adalah pilihan awal yang aman**.
3. **Uji berpasangan jauh lebih berkuasa** ketika rancangannya berpasangan, karena variasi antar subjek dihilangkan.
4. **Asumsi wajib diperiksa**: kenormalan (Shapiro-Wilk), homogenitas ragam (**Levene**, bukan uji-F), dan kebebasan (telaah rancangan).
5. Uji proporsi dua sampel adalah tulang punggung **A/B testing**.
6. **Interval kepercayaan selisih lebih berguna bagi pengambil keputusan** daripada *p-value*.
7. **Ukuran sampel A/B test dihitung di muka** dari efek minimum yang bermakna.
8. ***Peeking*** melonjakkan galat Tipe I dari 5% ke lebih dari 25%.
9. Uji **nonparametrik** lebih tahan pencilan tetapi sedikit kurang berkuasa.
10. Bila kesimpulan parametrik dan nonparametrik berbeda, **laporkan keduanya**.

---

## Referensi

1. Walpole, R. E., et al. (2016). *Probability and Statistics for Engineers and Scientists* (9th ed.), Bab 10. Pearson.
2. Kohavi, R., Tang, D., & Xu, Y. (2020). *Trustworthy Online Controlled Experiments*. Cambridge University Press.
3. Delacre, M., Lakens, D., & Leys, C. (2017). Why Psychologists Should by Default Use Welch's t-test. *International Review of Social Psychology*, 30(1), 92–101.
4. Johari, R., Koomen, P., Pekelis, L., & Walsh, D. (2017). Peeking at A/B Tests. *Proceedings of KDD '17*, 1517–1525.
5. Brown, M. B., & Forsythe, A. B. (1974). Robust Tests for the Equality of Variances. *JASA*, 69(346), 364–367.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
