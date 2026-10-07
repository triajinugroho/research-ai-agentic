# BAB 10: UJI HIPOTESIS SATU SAMPEL

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `PS-Sub-CPMK081-1` | Merumuskan hipotesis dan menjalankan uji-t satu sampel | C3 |
| `PS-Sub-CPMK081-1` | Membedakan galat Tipe I dan Tipe II serta menghitung kuasa uji | C3–C4 |
| `PS-Sub-CPMK081-1` | Menafsirkan *p-value* dengan benar dan membedakan signifikansi statistik dari praktis | C4 |

---

## 10.1 Kerangka Uji Hipotesis

### 10.1.1 Logika Peradilan

Uji hipotesis bekerja dengan **bukti tidak langsung**, mirip praktik peradilan:

```
  PERADILAN                        UJI HIPOTESIS
  ─────────                        ─────────────
  Terdakwa dianggap                H₀ dianggap benar
  tidak bersalah                   sampai ada bukti kuat

  Jaksa menghadirkan bukti         Data dikumpulkan

  "Bukti cukup kuat untuk          "Data cukup ekstrem sehingga
   menolak praduga?"                H₀ sulit dipercaya?"

  Bila ya   → bersalah             Bila ya   → tolak H₀
  Bila tidak→ TIDAK TERBUKTI       Bila tidak→ GAGAL MENOLAK H₀
              bersalah                        (BUKAN: H₀ terbukti benar)
```

> **Yang paling sering disalahpahami:** "gagal menolak H₀" **tidak berarti H₀ benar**. Sama seperti "tidak terbukti bersalah" tidak berarti "terbukti tidak bersalah". Bisa saja buktinya memang kurang — misalnya karena sampelnya terlalu kecil.

### 10.1.2 Merumuskan Hipotesis

| Komponen | Lambang | Sifat |
|----------|---------|-------|
| **Hipotesis nol** | H₀ | Pernyataan "tidak ada efek/perbedaan"; selalu memuat tanda sama dengan |
| **Hipotesis alternatif** | H₁ | Yang ingin dibuktikan; memuat ≠, >, atau < |

| Jenis Uji | H₀ | H₁ | Kapan dipakai |
|-----------|-----|-----|---------------|
| Dua sisi | μ = μ₀ | μ ≠ μ₀ | Peduli perbedaan ke arah mana pun |
| Satu sisi kanan | μ ≤ μ₀ | μ > μ₀ | Hanya peduli bila lebih besar |
| Satu sisi kiri | μ ≥ μ₀ | μ < μ₀ | Hanya peduli bila lebih kecil |

> **Aturan yang tidak boleh dilanggar:** arah hipotesis harus ditetapkan **sebelum melihat data**.
>
> Memilih arah setelah melihat hasil adalah bentuk kecurangan statistik yang disebut ***HARKing*** (*Hypothesizing After the Results are Known*). Ia melipatgandakan galat Tipe I secara diam-diam, karena Anda pada dasarnya menguji dua hipotesis sambil melaporkan satu.

---

## 10.2 Galat Tipe I dan Tipe II

|  | **H₀ sebenarnya BENAR** | **H₀ sebenarnya SALAH** |
|--|--------------------------|--------------------------|
| **Menolak H₀** | ❌ **Galat Tipe I** (α)<br>*false positive* | ✅ Benar<br>(kuasa = 1 − β) |
| **Gagal menolak H₀** | ✅ Benar | ❌ **Galat Tipe II** (β)<br>*false negative* |

### 10.2.1 Konsekuensi dalam Konteks Nyata

| Konteks | Galat Tipe I | Galat Tipe II | Mana lebih berbahaya? |
|---------|--------------|---------------|------------------------|
| Uji obat | Menyetujui obat tak manjur | Menolak obat manjur | Tipe I |
| Uji keselamatan penerbangan | Menahan pesawat aman | **Meloloskan pesawat tidak aman** | Tipe II |
| Deteksi penipuan | Memblokir transaksi sah | Meloloskan penipuan | Bergantung nilai transaksi |
| A/B test fitur | Merilis fitur tak lebih baik | Membatalkan fitur lebih baik | Bergantung biaya rilis |
| Deteksi kerentanan | Alarm palsu, tim lelah | **Kerentanan nyata terlewat** | Tipe II |

> **Pilihan α adalah keputusan nilai, bukan keputusan matematis.**
>
> Dalam pengujian keselamatan, galat Tipe II jauh lebih berbahaya, sehingga α dibuat longgar (misalnya 0,10) agar β mengecil. Dalam uji obat, galat Tipe I lebih berbahaya, sehingga α dibuat ketat (0,01).
>
> **Menetapkan α = 0,05 secara otomatis tanpa memikirkan konteksnya adalah kebiasaan, bukan penalaran.**

### 10.2.2 Kuasa Uji

**Kuasa uji** = 1 − β = probabilitas menolak H₀ ketika H₀ memang salah.

```python
import numpy as np
from scipy import stats

def kuasa_uji_t(n, efek, sigma, alpha=0.05, dua_sisi=True):
    """Kuasa uji-t satu sampel."""
    se = sigma / np.sqrt(n)
    df, delta = n - 1, efek / se
    if dua_sisi:
        tc = stats.t.ppf(1 - alpha/2, df)
        return stats.nct.sf(tc, df, delta) + stats.nct.cdf(-tc, df, delta)
    return stats.nct.sf(stats.t.ppf(1 - alpha, df), df, delta)

sigma, efek = 35, 10
print(f"Kuasa uji (α=0,05, efek={efek} ms, σ={sigma} ms):\n")
for n in [10, 20, 30, 50, 100, 200]:
    k = kuasa_uji_t(n, efek, sigma)
    print(f"  n = {n:>4}  →  kuasa = {k:.4f}{'  ✓' if k >= 0.80 else ''}")
print("\n→ Konvensi umum: kuasa minimal 0,80 (β ≤ 0,20).")
```

> **Studi dengan kuasa rendah adalah pemborosan sumber daya.**
>
> Bila kuasa hanya 0,30, maka **meskipun efeknya nyata**, Anda punya 70% kemungkinan tidak menemukannya. Hasil "tidak signifikan" dari studi berkuasa rendah **tidak memberi informasi apa pun** — Anda tidak tahu apakah efeknya memang tidak ada, atau sekadar tidak terdeteksi.
>
> Karena itu **kuasa harus dihitung SEBELUM penelitian dijalankan**, bukan sesudahnya.

---

## 10.3 Uji-t Satu Sampel

### 10.3.1 Prosedur Enam Langkah

$$t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}, \quad df = n - 1$$

1. Rumuskan H₀ dan H₁ (**sebelum melihat data**).
2. Tetapkan α (**dengan alasan kontekstual**).
3. **Periksa asumsi.**
4. Hitung statistik uji.
5. Hitung *p-value*.
6. Ambil keputusan dan **tafsirkan dalam konteks**.

### 10.3.2 Asumsi yang Wajib Diperiksa

| Asumsi | Cara memeriksa | Bila dilanggar |
|--------|----------------|----------------|
| Sampel acak dan bebas | Telaah cara pengumpulan data | **Tidak ada perbaikan statistik** — data harus dikumpulkan ulang |
| Skala interval/rasio | Telaah jenis variabel | Gunakan uji nonparametrik |
| Kenormalan (untuk n kecil) | Q-Q plot, Shapiro-Wilk | Gunakan Wilcoxon signed-rank |
| Tidak ada pencilan ekstrem | Boxplot | Telaah pencilan; pertimbangkan uji *robust* |

> Untuk n ≥ 30, **CLT membuat uji-t cukup tahan** terhadap pelanggaran kenormalan ringan. Untuk n kecil, kenormalan benar-benar penting.
>
> Perhatikan baris pertama: asumsi **kebebasan dan keacakan tidak dapat diperbaiki dengan metode statistik apa pun**. Bila sampel Anda bias, seluruh analisis menjadi tidak bermakna.

### 10.3.3 Implementasi

```python
import numpy as np
import pandas as pd
from scipy import stats

def uji_t_satu_sampel(data, mu0, alpha=0.05, arah="dua sisi", nama="data"):
    data = np.asarray(data, dtype=float); data = data[~np.isnan(data)]
    n = len(data); x_bar, s = data.mean(), data.std(ddof=1)
    se = s/np.sqrt(n); t_stat = (x_bar - mu0)/se; df = n - 1

    if arah == "dua sisi":  p = 2*stats.t.sf(abs(t_stat), df); sym = "≠"
    elif arah == "kanan":   p = stats.t.sf(t_stat, df);        sym = ">"
    else:                   p = stats.t.cdf(t_stat, df);       sym = "<"

    d = (x_bar - mu0)/s
    besar = ("sangat kecil" if abs(d)<0.2 else "kecil" if abs(d)<0.5
             else "sedang" if abs(d)<0.8 else "besar")
    tc = stats.t.ppf(1-alpha/2, df)

    print(f"H₀: μ = {mu0}   H₁: μ {sym} {mu0}   α = {alpha}\n")
    if 3 <= n <= 5000:
        _, pn = stats.shapiro(data)
        print(f"Kenormalan (Shapiro): p = {pn:.6f} "
              f"{'✓' if pn > alpha else '✗ menyimpang'}")
    if n >= 30:
        print(f"n = {n} ≥ 30 → CLT memberi ketahanan.\n")

    print(f"x̄ = {x_bar:.4f}, s = {s:.4f}, SE = {se:.4f}")
    print(f"t = {t_stat:.4f} (df={df}),  p = {p:.8f}")
    print(f"Cohen's d = {d:.4f} (efek {besar})")
    print(f"IK {(1-alpha)*100:.0f}% = [{x_bar-tc*se:.4f} , {x_bar+tc*se:.4f}]\n")

    if p < alpha:
        print(f"p < α  →  TOLAK H₀.")
        if abs(d) < 0.2:
            print("PERINGATAN: efek sangat kecil — periksa kebermaknaan praktis.")
    else:
        print(f"p ≥ α  →  GAGAL MENOLAK H₀.")
        print("CATATAN: ini BUKAN berarti H₀ terbukti benar.")
    return {"t": t_stat, "p": p, "d": d}

df = pd.read_csv("nilai_mahasiswa_if.csv")
uji_t_satu_sampel(df["jam_belajar"], mu0=12, nama="Jam belajar")
```

---

## 10.4 Memahami *p-value*

### 10.4.1 Definisi yang Tepat

> ***p-value*** adalah probabilitas memperoleh data **seekstrem ini atau lebih ekstrem**, **bila H₀ benar**.

$$p = P(\text{data seekstrem ini} \mid H_0 \text{ benar})$$

### 10.4.2 Lima Salah Tafsir yang Paling Umum

| No | Pernyataan | Status | Mengapa |
|----|-----------|--------|---------|
| 1 | "p = 0,03 berarti 3% probabilitas H₀ benar" | ❌ | *p* = P(data \| H₀), bukan P(H₀ \| data) — **kekeliruan membalik arah persyaratan**, sama seperti Bab 5 |
| 2 | "p = 0,03 berarti 97% probabilitas H₁ benar" | ❌ | Alasan yang sama |
| 3 | "p < 0,05 berarti efeknya besar dan penting" | ❌ | *p* dipengaruhi ukuran sampel; efek sangat kecil menjadi signifikan bila n besar |
| 4 | "p = 0,06 berarti tidak ada efek" | ❌ | Ambang 0,05 adalah konvensi; p = 0,06 dan 0,04 hampir tidak berbeda maknanya |
| 5 | "Hasil signifikan pasti dapat direplikasi" | ❌ | *p* tidak mengukur replikabilitas |

> ✅ **Tafsir yang benar:** "Bila benar tidak ada perbedaan, data seekstrem ini hanya akan muncul pada 3% pengulangan penelitian. Karena itu kami menganggap H₀ kurang layak dipercaya."

### 10.4.3 Pernyataan ASA 2016

American Statistical Association menerbitkan enam prinsip tentang *p-value* — pernyataan resmi pertama organisasi itu tentang praktik statistik dalam 177 tahun sejarahnya:

1. *p-value* dapat menunjukkan seberapa tidak cocok data dengan model statistik tertentu.
2. *p-value* **bukan** ukuran probabilitas bahwa hipotesis yang diteliti benar.
3. Kesimpulan ilmiah **tidak boleh** hanya didasarkan pada apakah *p-value* melewati ambang tertentu.
4. Inferensi yang baik menuntut **pelaporan yang lengkap dan transparan**.
5. *p-value* **tidak mengukur besarnya efek** maupun pentingnya suatu hasil.
6. *p-value* saja **tidak memberikan ukuran bukti** yang baik tentang sebuah model atau hipotesis.

### 10.4.4 Pengaruh Ukuran Sampel

```python
import numpy as np
from scipy import stats

rng = np.random.default_rng(42)
MU_SEBENARNYA, MU0, SIGMA = 200.5, 200, 35   # efek hanya 0,5 ms

print("Efek sebenarnya: 0,5 ms — tidak berarti apa pun dalam praktik.\n")
print(f"{'n':>10}  {'p-value':>12}  {'Cohen d':>9}  Kesimpulan")
for n in [30, 100, 1_000, 10_000, 100_000, 1_000_000]:
    s = rng.normal(MU_SEBENARNYA, SIGMA, n)
    _, p = stats.ttest_1samp(s, MU0)
    d = (s.mean() - MU0) / s.std(ddof=1)
    print(f"{n:>10,}  {p:>12.6f}  {d:>9.4f}  "
          f"{'SIGNIFIKAN' if p < 0.05 else 'tidak signifikan'}")

print("\n→ Cohen's d tetap ~0,014 (sangat kecil) di semua n.")
print("→ Tetapi p-value terus mengecil seiring n bertambah.")
print("→ SELALU laporkan ukuran efek, bukan hanya p-value.")
```

---

## 10.5 Signifikansi Statistik vs Praktis

| Aspek | Signifikansi Statistik | Signifikansi Praktis |
|-------|------------------------|----------------------|
| Pertanyaan | "Apakah efeknya nyata, bukan kebetulan?" | "Apakah efeknya cukup besar untuk diperhatikan?" |
| Diukur dengan | *p-value* | Ukuran efek, interval kepercayaan |
| Dipengaruhi n | **Ya, sangat** | Tidak |
| Cukup untuk mengambil keputusan? | **Tidak** | Bersama konteks, ya |

**Ukuran efek Cohen's d:**

| \|d\| | Tafsir |
|-------|--------|
| < 0,2 | Sangat kecil |
| 0,2 – 0,5 | Kecil |
| 0,5 – 0,8 | Sedang |
| > 0,8 | Besar |

> **Praktik pelaporan yang baik** menyertakan **empat hal sekaligus**: statistik uji, *p-value*, **ukuran efek**, dan **interval kepercayaan**.
>
> Melaporkan *p-value* saja adalah praktik yang sudah ditinggalkan di banyak bidang ilmu, dan sejumlah jurnal kini menolaknya.

---

## AI Corner — Tingkat Lanjut

### AI Dapat Menjalankan Uji, Tetapi Tidak Dapat Memilihkannya

Memilih uji statistik memerlukan pengetahuan tentang: rancangan pengumpulan data, skala variabel, kebebasan pengamatan, dan tujuan penelitian. **Semuanya konteks yang tidak dimiliki AI** kecuali Anda ceritakan — dan biasanya Anda tidak menceritakan semuanya karena tidak sadar bahwa itu relevan.

### Percobaan: Uji Pemeriksaan Asumsi

Berikan data dan minta uji-t tanpa menyebutkan cara pengumpulannya:

> *"Ini 20 waktu respons sebelum optimasi dan 20 sesudah. Apakah ada perbedaan signifikan?"*

Sebagian besar AI akan menjalankan uji-t **dua sampel bebas**. Tetapi bila kedua pengukuran dilakukan pada **mesin yang sama**, yang benar adalah uji **berpasangan** — dan memakai uji yang salah membuang sebagian besar kuasa uji (Bab 11).

AI tidak dapat mengetahui itu, karena Anda tidak menceritakannya.

### Kebijakan Mata Kuliah Ini

| Kegiatan | AI |
|----------|-----|
| Menjelaskan konsep *p-value* | Boleh |
| Menulis kode `scipy.stats.ttest_1samp` | Boleh, dicatat di log |
| **Memilih uji untuk data proyek Anda** | **Tidak boleh sebagai penentu** |
| **Menafsirkan hasil uji proyek** | **Tidak boleh sebagai penentu** |

> **Alasan kebijakan ini.** Pada mata kuliah fondasi, yang sedang dinilai adalah **kemampuan memilih dan menafsirkan** — bukan kemampuan mengeksekusi. Menyerahkan bagian itu kepada AI berarti menyerahkan capaian pembelajarannya.

### Pemakaian yang Dianjurkan

```
PROMPT YANG BAIK:
"Rancangan saya: 20 endpoint yang SAMA diukur sebelum dan sesudah caching.
 Saya memilih uji-t BERPASANGAN karena pengukurannya pada objek yang sama.
 Asumsi yang saya periksa: kenormalan SELISIH (Shapiro p=0,31).
 Apakah penalaran saya benar? Adakah asumsi lain yang saya lewatkan?"

Mengapa baik: Anda sudah memilih, sudah punya alasan, sudah memeriksa
asumsi, dan meminta AI memeriksa PENALARAN.
```

---

## Latihan Soal

### Tingkat Dasar

1. Tuliskan definisi *p-value* tanpa menyebut frasa "probabilitas hipotesis benar".

2. Lengkapi tabel galat Tipe I dan Tipe II beserta konsekuensinya.

3. Rumuskan H₀ dan H₁ untuk klaim: *"Optimasi baru membuat rata-rata waktu respons turun di bawah 200 ms."* Tentukan arah ujinya.

4. Dari sampel n = 25 diperoleh x̄ = 195 dan s = 18. Uji H₀: μ = 200 vs H₁: μ < 200 pada α = 0,05.

5. Jelaskan mengapa "gagal menolak H₀" berbeda dari "H₀ terbukti benar".

### Tingkat Menengah

6. Sebuah studi dengan n = 15 melaporkan "tidak ada perbedaan signifikan" (p = 0,21) untuk efek 10 ms dengan σ = 35 ms.
   (a) Hitung kuasa uji studi itu.
   (b) Apakah kesimpulan "tidak ada perbedaan" dapat dipercaya?
   (c) Berapa n yang diperlukan untuk kuasa 0,80?
   (d) Tuliskan kesimpulan yang lebih jujur untuk laporan.

7. Sebuah A/B test dengan n = 500.000 per grup menemukan selisih konversi 0,04 poin persen dengan p = 0,003.
   (a) Apakah hasilnya signifikan secara statistik?
   (b) Hitung ukuran efeknya (perkirakan Cohen's h untuk proporsi).
   (c) Apakah hasilnya bermakna secara praktis?
   (d) Bila penerapan fitur ini memerlukan biaya rekayasa 3 bulan, apa rekomendasi Anda?

8. Jelaskan mengapa menetapkan α = 0,05 untuk **semua** penelitian adalah kebiasaan, bukan penalaran.
   (a) Beri dua contoh di mana α = 0,01 lebih tepat.
   (b) Beri dua contoh di mana α = 0,10 lebih tepat.
   (c) Bagaimana cara menetapkan α secara berdasar?

9. Untuk setiap pernyataan, tentukan benar atau salah dan jelaskan:
   (a) "p = 0,04 berarti ada 4% kemungkinan hasil ini kebetulan."
   (b) "p = 0,04 berarti ada 96% kemungkinan H₁ benar."
   (c) "p = 0,04 lebih meyakinkan daripada p = 0,06."
   (d) "Hasil dengan p = 0,001 pasti penting secara praktis."
   (e) "Gagal menolak H₀ membuktikan tidak ada efek."

### Tingkat Mahir

10. Simulasikan *p-hacking* dan hitung dampaknya.
    (a) Uji 20 variabel yang semuanya tidak berefek (H₀ benar). Berapa yang "signifikan"?
    (b) Ulangi 2.000 kali. Berapa persen percobaan menghasilkan sedikitnya satu temuan palsu?
    (c) Bandingkan dengan perhitungan teoretis 1 − 0,95^k.
    (d) Terapkan koreksi Bonferroni dan hitung ulang.
    (e) Jelaskan mengapa "melaporkan hanya yang signifikan" adalah pelanggaran integritas ilmiah.

11. Analisis kuasa sebuah rancangan penelitian.
    (a) Buat fungsi yang mencari n minimum untuk kuasa 0,80 pada berbagai ukuran efek.
    (b) Buat kurva kuasa untuk n = 20, 50, 100, 200.
    (c) Sebuah tim hanya sanggup mengumpulkan 30 pengamatan. Efek terkecil apa yang dapat mereka deteksi dengan kuasa 0,80?
    (d) Bila efek yang diharapkan lebih kecil dari itu, apa saran Anda kepada tim?

12. Tulislah esai (500 kata): *"Mengapa pernyataan ASA 2016 tentang p-value diperlukan, dan apa implikasinya bagi seorang analis data di industri teknologi?"* Sertakan sekurang-kurangnya tiga dari enam prinsip ASA dan hubungkan dengan praktik A/B testing.

---

## Rangkuman

1. Uji hipotesis bekerja seperti peradilan: H₀ dianggap benar sampai bukti cukup kuat menolaknya.
2. **"Gagal menolak H₀" bukan "H₀ terbukti benar."**
3. Arah hipotesis ditetapkan **sebelum melihat data**. Menyesuaikannya setelah melihat hasil adalah *HARKing*.
4. **Galat Tipe I (α)** = menolak H₀ yang benar; **Tipe II (β)** = gagal menolak H₀ yang salah.
5. **Pilihan α adalah keputusan nilai**, bergantung mana galat yang lebih berbahaya dalam konteks.
6. **Kuasa uji** = 1 − β, dihitung **sebelum** penelitian. Studi berkuasa rendah yang menghasilkan "tidak signifikan" tidak memberi informasi.
7. Asumsi uji-t **wajib diperiksa**. Asumsi keacakan sampel **tidak dapat diperbaiki** secara statistik.
8. ***p-value* adalah P(data | H₀), bukan P(H₀ | data).**
9. Dengan n cukup besar, **efek sekecil apa pun menjadi "signifikan"**.
10. Laporkan **empat hal**: statistik uji, *p-value*, **ukuran efek**, dan **interval kepercayaan**.

---

## Referensi

1. Walpole, R. E., et al. (2016). *Probability and Statistics for Engineers and Scientists* (9th ed.), Bab 10. Pearson.
2. Wasserstein, R. L., & Lazar, N. A. (2016). The ASA Statement on p-Values. *The American Statistician*, 70(2), 129–133.
3. Greenland, S., et al. (2016). Statistical tests, P values, confidence intervals, and power. *European Journal of Epidemiology*, 31(4), 337–350.
4. Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2nd ed.). Lawrence Erlbaum.
5. Kerr, N. L. (1998). HARKing: Hypothesizing After the Results are Known. *Personality and Social Psychology Review*, 2(3), 196–217.
6. Ioannidis, J. P. A. (2005). Why Most Published Research Findings Are False. *PLoS Medicine*, 2(8), e124.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
