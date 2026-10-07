# LAMPIRAN

**Tri Aji Nugroho, S.T., M.T.**
Probabilitas dan Statistik (IF52510033) — Program Studi Informatika, Universitas Al Azhar Indonesia

---

## Daftar Lampiran

| Lampiran | Judul | Kegunaan |
|----------|-------|----------|
| [A](#lampiran-a-tabel-distribusi) | Tabel Distribusi | Dibawa saat UTS dan UAS |
| [B](#lampiran-b-formularium) | Formularium | Dibawa saat UTS dan UAS |
| [C](#lampiran-c-pohon-keputusan-pemilihan-uji) | Pohon Keputusan Pemilihan Uji | Rujukan cepat saat analisis |
| [D](#lampiran-d-pustaka-python-untuk-statistika) | Pustaka Python untuk Statistika | Rujukan praktikum dan proyek |
| [E](#lampiran-e-glosarium) | Glosarium Istilah Statistika | Padanan Indonesia–Inggris |
| [F](#lampiran-f-kesalahan-tafsir-yang-sering-terjadi) | Kesalahan Tafsir yang Sering Terjadi | Pemeriksaan sebelum menulis laporan |
| [G](#lampiran-g-sumber-data-berkonteks-indonesia) | Sumber Data Berkonteks Indonesia | Bahan proyek |
| [H](#lampiran-h-peta-bab-modul-praktikum) | Peta Bab – Modul – Praktikum | Navigasi materi |

> **Ketentuan ujian:** Lampiran A dan B **boleh dibawa** saat UTS dan UAS dalam bentuk cetak. Lampiran lain tidak. Alat bantu AI **tidak diperkenankan** dalam bentuk apa pun selama ujian.

---

## Lampiran A: Tabel Distribusi

### A.1 Tabel Z — Distribusi Normal Standar

Nilai dalam tabel adalah **luas kumulatif** dari $-\infty$ sampai $z$, yaitu $P(Z \le z)$.

**Cara membaca:** untuk $z = 1{,}96$ → cari baris **1,9**, kolom **0,06** → **0,9750**.

**Sifat simetri:** $P(Z \le -z) = 1 - P(Z \le z)$. Untuk $z = -1{,}96$ → $1 - 0{,}9750 = 0{,}0250$.

| z | 0,00 | 0,01 | 0,02 | 0,03 | 0,04 | 0,05 | 0,06 | 0,07 | 0,08 | 0,09 |
|---|------|------|------|------|------|------|------|------|------|------|
| **0,0** | 0,5000 | 0,5040 | 0,5080 | 0,5120 | 0,5160 | 0,5199 | 0,5239 | 0,5279 | 0,5319 | 0,5359 |
| **0,1** | 0,5398 | 0,5438 | 0,5478 | 0,5517 | 0,5557 | 0,5596 | 0,5636 | 0,5675 | 0,5714 | 0,5753 |
| **0,2** | 0,5793 | 0,5832 | 0,5871 | 0,5910 | 0,5948 | 0,5987 | 0,6026 | 0,6064 | 0,6103 | 0,6141 |
| **0,3** | 0,6179 | 0,6217 | 0,6255 | 0,6293 | 0,6331 | 0,6368 | 0,6406 | 0,6443 | 0,6480 | 0,6517 |
| **0,4** | 0,6554 | 0,6591 | 0,6628 | 0,6664 | 0,6700 | 0,6736 | 0,6772 | 0,6808 | 0,6844 | 0,6879 |
| **0,5** | 0,6915 | 0,6950 | 0,6985 | 0,7019 | 0,7054 | 0,7088 | 0,7123 | 0,7157 | 0,7190 | 0,7224 |
| **0,6** | 0,7257 | 0,7291 | 0,7324 | 0,7357 | 0,7389 | 0,7422 | 0,7454 | 0,7486 | 0,7517 | 0,7549 |
| **0,7** | 0,7580 | 0,7611 | 0,7642 | 0,7673 | 0,7704 | 0,7734 | 0,7764 | 0,7794 | 0,7823 | 0,7852 |
| **0,8** | 0,7881 | 0,7910 | 0,7939 | 0,7967 | 0,7995 | 0,8023 | 0,8051 | 0,8078 | 0,8106 | 0,8133 |
| **0,9** | 0,8159 | 0,8186 | 0,8212 | 0,8238 | 0,8264 | 0,8289 | 0,8315 | 0,8340 | 0,8365 | 0,8389 |
| **1,0** | 0,8413 | 0,8438 | 0,8461 | 0,8485 | 0,8508 | 0,8531 | 0,8554 | 0,8577 | 0,8599 | 0,8621 |
| **1,1** | 0,8643 | 0,8665 | 0,8686 | 0,8708 | 0,8729 | 0,8749 | 0,8770 | 0,8790 | 0,8810 | 0,8830 |
| **1,2** | 0,8849 | 0,8869 | 0,8888 | 0,8907 | 0,8925 | 0,8944 | 0,8962 | 0,8980 | 0,8997 | 0,9015 |
| **1,3** | 0,9032 | 0,9049 | 0,9066 | 0,9082 | 0,9099 | 0,9115 | 0,9131 | 0,9147 | 0,9162 | 0,9177 |
| **1,4** | 0,9192 | 0,9207 | 0,9222 | 0,9236 | 0,9251 | 0,9265 | 0,9279 | 0,9292 | 0,9306 | 0,9319 |
| **1,5** | 0,9332 | 0,9345 | 0,9357 | 0,9370 | 0,9382 | 0,9394 | 0,9406 | 0,9418 | 0,9429 | 0,9441 |
| **1,6** | 0,9452 | 0,9463 | 0,9474 | 0,9484 | 0,9495 | 0,9505 | 0,9515 | 0,9525 | 0,9535 | 0,9545 |
| **1,7** | 0,9554 | 0,9564 | 0,9573 | 0,9582 | 0,9591 | 0,9599 | 0,9608 | 0,9616 | 0,9625 | 0,9633 |
| **1,8** | 0,9641 | 0,9649 | 0,9656 | 0,9664 | 0,9671 | 0,9678 | 0,9686 | 0,9693 | 0,9699 | 0,9706 |
| **1,9** | 0,9713 | 0,9719 | 0,9726 | 0,9732 | 0,9738 | 0,9744 | 0,9750 | 0,9756 | 0,9761 | 0,9767 |
| **2,0** | 0,9772 | 0,9778 | 0,9783 | 0,9788 | 0,9793 | 0,9798 | 0,9803 | 0,9808 | 0,9812 | 0,9817 |
| **2,1** | 0,9821 | 0,9826 | 0,9830 | 0,9834 | 0,9838 | 0,9842 | 0,9846 | 0,9850 | 0,9854 | 0,9857 |
| **2,2** | 0,9861 | 0,9864 | 0,9868 | 0,9871 | 0,9875 | 0,9878 | 0,9881 | 0,9884 | 0,9887 | 0,9890 |
| **2,3** | 0,9893 | 0,9896 | 0,9898 | 0,9901 | 0,9904 | 0,9906 | 0,9909 | 0,9911 | 0,9913 | 0,9916 |
| **2,4** | 0,9918 | 0,9920 | 0,9922 | 0,9925 | 0,9927 | 0,9929 | 0,9931 | 0,9932 | 0,9934 | 0,9936 |
| **2,5** | 0,9938 | 0,9940 | 0,9941 | 0,9943 | 0,9945 | 0,9946 | 0,9948 | 0,9949 | 0,9951 | 0,9952 |
| **2,6** | 0,9953 | 0,9955 | 0,9956 | 0,9957 | 0,9959 | 0,9960 | 0,9961 | 0,9962 | 0,9963 | 0,9964 |
| **2,7** | 0,9965 | 0,9966 | 0,9967 | 0,9968 | 0,9969 | 0,9970 | 0,9971 | 0,9972 | 0,9973 | 0,9974 |
| **2,8** | 0,9974 | 0,9975 | 0,9976 | 0,9977 | 0,9977 | 0,9978 | 0,9979 | 0,9979 | 0,9980 | 0,9981 |
| **2,9** | 0,9981 | 0,9982 | 0,9982 | 0,9983 | 0,9984 | 0,9984 | 0,9985 | 0,9985 | 0,9986 | 0,9986 |
| **3,0** | 0,9987 | 0,9987 | 0,9987 | 0,9988 | 0,9988 | 0,9989 | 0,9989 | 0,9989 | 0,9990 | 0,9990 |
| **3,1** | 0,9990 | 0,9991 | 0,9991 | 0,9991 | 0,9992 | 0,9992 | 0,9992 | 0,9992 | 0,9993 | 0,9993 |
| **3,2** | 0,9993 | 0,9993 | 0,9994 | 0,9994 | 0,9994 | 0,9994 | 0,9994 | 0,9995 | 0,9995 | 0,9995 |
| **3,3** | 0,9995 | 0,9995 | 0,9995 | 0,9996 | 0,9996 | 0,9996 | 0,9996 | 0,9996 | 0,9996 | 0,9997 |
| **3,4** | 0,9997 | 0,9997 | 0,9997 | 0,9997 | 0,9997 | 0,9997 | 0,9997 | 0,9997 | 0,9997 | 0,9998 |

#### A.1.1 Nilai Kritis z yang Paling Sering Dipakai

| Keperluan | Taraf | Nilai kritis |
|-----------|-------|--------------|
| IK 90% | α = 0,10 dua arah | z = 1,645 |
| IK 95% | α = 0,05 dua arah | **z = 1,960** |
| IK 99% | α = 0,01 dua arah | z = 2,576 |
| Uji satu arah | α = 0,05 | z = 1,645 |
| Uji satu arah | α = 0,01 | z = 2,326 |

---

### A.2 Tabel t — Distribusi Student

Nilai dalam tabel adalah $t_\alpha$ sedemikian hingga $P(T > t_\alpha) = \alpha$ untuk derajat bebas (db) tertentu.

**Uji dua arah:** pakai kolom $\alpha/2$. Untuk α = 0,05 dua arah dengan db = 20 → kolom **0,025** → **2,086**.

| db | 0,10 | 0,05 | 0,025 | 0,01 | 0,005 |
|----|------|------|-------|------|-------|
| 1 | 3,078 | 6,314 | 12,706 | 31,821 | 63,657 |
| 2 | 1,886 | 2,920 | 4,303 | 6,965 | 9,925 |
| 3 | 1,638 | 2,353 | 3,182 | 4,541 | 5,841 |
| 4 | 1,533 | 2,132 | 2,776 | 3,747 | 4,604 |
| 5 | 1,476 | 2,015 | 2,571 | 3,365 | 4,032 |
| 6 | 1,440 | 1,943 | 2,447 | 3,143 | 3,707 |
| 7 | 1,415 | 1,895 | 2,365 | 2,998 | 3,499 |
| 8 | 1,397 | 1,860 | 2,306 | 2,896 | 3,355 |
| 9 | 1,383 | 1,833 | 2,262 | 2,821 | 3,250 |
| 10 | 1,372 | 1,812 | 2,228 | 2,764 | 3,169 |
| 11 | 1,363 | 1,796 | 2,201 | 2,718 | 3,106 |
| 12 | 1,356 | 1,782 | 2,179 | 2,681 | 3,055 |
| 13 | 1,350 | 1,771 | 2,160 | 2,650 | 3,012 |
| 14 | 1,345 | 1,761 | 2,145 | 2,624 | 2,977 |
| 15 | 1,341 | 1,753 | 2,131 | 2,602 | 2,947 |
| 16 | 1,337 | 1,746 | 2,120 | 2,583 | 2,921 |
| 17 | 1,333 | 1,740 | 2,110 | 2,567 | 2,898 |
| 18 | 1,330 | 1,734 | 2,101 | 2,552 | 2,878 |
| 19 | 1,328 | 1,729 | 2,093 | 2,539 | 2,861 |
| 20 | 1,325 | 1,725 | 2,086 | 2,528 | 2,845 |
| 21 | 1,323 | 1,721 | 2,080 | 2,518 | 2,831 |
| 22 | 1,321 | 1,717 | 2,074 | 2,508 | 2,819 |
| 23 | 1,319 | 1,714 | 2,069 | 2,500 | 2,807 |
| 24 | 1,318 | 1,711 | 2,064 | 2,492 | 2,797 |
| 25 | 1,316 | 1,708 | 2,060 | 2,485 | 2,787 |
| 26 | 1,315 | 1,706 | 2,056 | 2,479 | 2,779 |
| 27 | 1,314 | 1,703 | 2,052 | 2,473 | 2,771 |
| 28 | 1,313 | 1,701 | 2,048 | 2,467 | 2,763 |
| 29 | 1,311 | 1,699 | 2,045 | 2,462 | 2,756 |
| 30 | 1,310 | 1,697 | 2,042 | 2,457 | 2,750 |
| 35 | 1,306 | 1,690 | 2,030 | 2,438 | 2,724 |
| 40 | 1,303 | 1,684 | 2,021 | 2,423 | 2,704 |
| 45 | 1,301 | 1,679 | 2,014 | 2,412 | 2,690 |
| 50 | 1,299 | 1,676 | 2,009 | 2,403 | 2,678 |
| 60 | 1,296 | 1,671 | 2,000 | 2,390 | 2,660 |
| 80 | 1,292 | 1,664 | 1,990 | 2,374 | 2,639 |
| 100 | 1,290 | 1,660 | 1,984 | 2,364 | 2,626 |
| 120 | 1,289 | 1,658 | 1,980 | 2,358 | 2,617 |
| **∞ (z)** | 1,282 | 1,645 | 1,960 | 2,326 | 2,576 |

> Perhatikan baris terakhir: pada db besar, distribusi t mendekati distribusi normal standar. Inilah sebabnya pada n > 30 banyak buku membolehkan pemakaian z sebagai hampiran — meski memakai t selalu lebih tepat.

---

### A.3 Tabel Chi-Square (χ²)

Nilai dalam tabel adalah $\chi^2_\alpha$ sedemikian hingga $P(X^2 > \chi^2_\alpha) = \alpha$.

**Derajat bebas:**

| Penggunaan | db |
|------------|-----|
| Uji kesesuaian (*goodness of fit*) | $k - 1$ |
| Uji kebebasan (tabel kontingensi $r \times c$) | $(r-1)(c-1)$ |
| Uji homogenitas | $(r-1)(c-1)$ |

| db | 0,10 | 0,05 | 0,025 | 0,01 | 0,005 |
|----|------|------|-------|------|-------|
| 1 | 2,706 | 3,841 | 5,024 | 6,635 | 7,879 |
| 2 | 4,605 | 5,991 | 7,378 | 9,210 | 10,597 |
| 3 | 6,251 | 7,815 | 9,348 | 11,345 | 12,838 |
| 4 | 7,779 | 9,488 | 11,143 | 13,277 | 14,860 |
| 5 | 9,236 | 11,070 | 12,833 | 15,086 | 16,750 |
| 6 | 10,645 | 12,592 | 14,449 | 16,812 | 18,548 |
| 7 | 12,017 | 14,067 | 16,013 | 18,475 | 20,278 |
| 8 | 13,362 | 15,507 | 17,535 | 20,090 | 21,955 |
| 9 | 14,684 | 16,919 | 19,023 | 21,666 | 23,589 |
| 10 | 15,987 | 18,307 | 20,483 | 23,209 | 25,188 |
| 11 | 17,275 | 19,675 | 21,920 | 24,725 | 26,757 |
| 12 | 18,549 | 21,026 | 23,337 | 26,217 | 28,300 |
| 13 | 19,812 | 22,362 | 24,736 | 27,688 | 29,819 |
| 14 | 21,064 | 23,685 | 26,119 | 29,141 | 31,319 |
| 15 | 22,307 | 24,996 | 27,488 | 30,578 | 32,801 |
| 16 | 23,542 | 26,296 | 28,845 | 32,000 | 34,267 |
| 17 | 24,769 | 27,587 | 30,191 | 33,409 | 35,718 |
| 18 | 25,989 | 28,869 | 31,526 | 34,805 | 37,156 |
| 19 | 27,204 | 30,144 | 32,852 | 36,191 | 38,582 |
| 20 | 28,412 | 31,410 | 34,170 | 37,566 | 39,997 |
| 21 | 29,615 | 32,671 | 35,479 | 38,932 | 41,401 |
| 22 | 30,813 | 33,924 | 36,781 | 40,289 | 42,796 |
| 23 | 32,007 | 35,172 | 38,076 | 41,638 | 44,181 |
| 24 | 33,196 | 36,415 | 39,364 | 42,980 | 45,559 |
| 25 | 34,382 | 37,652 | 40,646 | 44,314 | 46,928 |
| 26 | 35,563 | 38,885 | 41,923 | 45,642 | 48,290 |
| 27 | 36,741 | 40,113 | 43,195 | 46,963 | 49,645 |
| 28 | 37,916 | 41,337 | 44,461 | 48,278 | 50,993 |
| 29 | 39,087 | 42,557 | 45,722 | 49,588 | 52,336 |
| 30 | 40,256 | 43,773 | 46,979 | 50,892 | 53,672 |
| 40 | 51,805 | 55,758 | 59,342 | 63,691 | 66,766 |
| 50 | 63,167 | 67,505 | 71,420 | 76,154 | 79,490 |
| 60 | 74,397 | 79,082 | 83,298 | 88,379 | 91,952 |

---

### A.4 Tabel F — α = 0,05

Nilai kritis $F_{0{,}05}(db_1, db_2)$; $db_1$ = derajat bebas pembilang (antar kelompok), $db_2$ = derajat bebas penyebut (dalam kelompok).

**Untuk ANOVA satu arah dengan $k$ kelompok dan $N$ pengamatan:** $db_1 = k - 1$, $db_2 = N - k$.

| db₂ \ db₁ | 1 | 2 | 3 | 4 | 5 | 6 | 8 | 10 | 12 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|
| **1** | 161,45 | 199,50 | 215,71 | 224,58 | 230,16 | 233,99 | 238,88 | 241,88 | 243,91 | 248,01 |
| **2** | 18,51 | 19,00 | 19,16 | 19,25 | 19,30 | 19,33 | 19,37 | 19,40 | 19,41 | 19,45 |
| **3** | 10,13 | 9,55 | 9,28 | 9,12 | 9,01 | 8,94 | 8,85 | 8,79 | 8,74 | 8,66 |
| **4** | 7,71 | 6,94 | 6,59 | 6,39 | 6,26 | 6,16 | 6,04 | 5,96 | 5,91 | 5,80 |
| **5** | 6,61 | 5,79 | 5,41 | 5,19 | 5,05 | 4,95 | 4,82 | 4,74 | 4,68 | 4,56 |
| **6** | 5,99 | 5,14 | 4,76 | 4,53 | 4,39 | 4,28 | 4,15 | 4,06 | 4,00 | 3,87 |
| **7** | 5,59 | 4,74 | 4,35 | 4,12 | 3,97 | 3,87 | 3,73 | 3,64 | 3,57 | 3,44 |
| **8** | 5,32 | 4,46 | 4,07 | 3,84 | 3,69 | 3,58 | 3,44 | 3,35 | 3,28 | 3,15 |
| **9** | 5,12 | 4,26 | 3,86 | 3,63 | 3,48 | 3,37 | 3,23 | 3,14 | 3,07 | 2,94 |
| **10** | 4,96 | 4,10 | 3,71 | 3,48 | 3,33 | 3,22 | 3,07 | 2,98 | 2,91 | 2,77 |
| **11** | 4,84 | 3,98 | 3,59 | 3,36 | 3,20 | 3,09 | 2,95 | 2,85 | 2,79 | 2,65 |
| **12** | 4,75 | 3,89 | 3,49 | 3,26 | 3,11 | 3,00 | 2,85 | 2,75 | 2,69 | 2,54 |
| **13** | 4,67 | 3,81 | 3,41 | 3,18 | 3,03 | 2,92 | 2,77 | 2,67 | 2,60 | 2,46 |
| **14** | 4,60 | 3,74 | 3,34 | 3,11 | 2,96 | 2,85 | 2,70 | 2,60 | 2,53 | 2,39 |
| **15** | 4,54 | 3,68 | 3,29 | 3,06 | 2,90 | 2,79 | 2,64 | 2,54 | 2,48 | 2,33 |
| **16** | 4,49 | 3,63 | 3,24 | 3,01 | 2,85 | 2,74 | 2,59 | 2,49 | 2,42 | 2,28 |
| **17** | 4,45 | 3,59 | 3,20 | 2,96 | 2,81 | 2,70 | 2,55 | 2,45 | 2,38 | 2,23 |
| **18** | 4,41 | 3,55 | 3,16 | 2,93 | 2,77 | 2,66 | 2,51 | 2,41 | 2,34 | 2,19 |
| **19** | 4,38 | 3,52 | 3,13 | 2,90 | 2,74 | 2,63 | 2,48 | 2,38 | 2,31 | 2,16 |
| **20** | 4,35 | 3,49 | 3,10 | 2,87 | 2,71 | 2,60 | 2,45 | 2,35 | 2,28 | 2,12 |
| **25** | 4,24 | 3,39 | 2,99 | 2,76 | 2,60 | 2,49 | 2,34 | 2,24 | 2,16 | 2,01 |
| **30** | 4,17 | 3,32 | 2,92 | 2,69 | 2,53 | 2,42 | 2,27 | 2,16 | 2,09 | 1,93 |
| **40** | 4,08 | 3,23 | 2,84 | 2,61 | 2,45 | 2,34 | 2,18 | 2,08 | 2,00 | 1,84 |
| **60** | 4,00 | 3,15 | 2,76 | 2,53 | 2,37 | 2,25 | 2,10 | 1,99 | 1,92 | 1,75 |
| **120** | 3,92 | 3,07 | 2,68 | 2,45 | 2,29 | 2,18 | 2,02 | 1,91 | 1,83 | 1,66 |
| **∞** | 3,84 | 3,00 | 2,60 | 2,37 | 2,21 | 2,10 | 1,94 | 1,83 | 1,75 | 1,57 |

### A.5 Tabel F — α = 0,01

| db₂ \ db₁ | 1 | 2 | 3 | 4 | 5 | 6 | 8 | 10 | 12 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|
| **1** | 4052,18 | 4999,50 | 5403,35 | 5624,58 | 5763,65 | 5858,99 | 5981,07 | 6055,85 | 6106,32 | 6208,73 |
| **2** | 98,50 | 99,00 | 99,17 | 99,25 | 99,30 | 99,33 | 99,37 | 99,40 | 99,42 | 99,45 |
| **3** | 34,12 | 30,82 | 29,46 | 28,71 | 28,24 | 27,91 | 27,49 | 27,23 | 27,05 | 26,69 |
| **4** | 21,20 | 18,00 | 16,69 | 15,98 | 15,52 | 15,21 | 14,80 | 14,55 | 14,37 | 14,02 |
| **5** | 16,26 | 13,27 | 12,06 | 11,39 | 10,97 | 10,67 | 10,29 | 10,05 | 9,89 | 9,55 |
| **6** | 13,75 | 10,92 | 9,78 | 9,15 | 8,75 | 8,47 | 8,10 | 7,87 | 7,72 | 7,40 |
| **7** | 12,25 | 9,55 | 8,45 | 7,85 | 7,46 | 7,19 | 6,84 | 6,62 | 6,47 | 6,16 |
| **8** | 11,26 | 8,65 | 7,59 | 7,01 | 6,63 | 6,37 | 6,03 | 5,81 | 5,67 | 5,36 |
| **9** | 10,56 | 8,02 | 6,99 | 6,42 | 6,06 | 5,80 | 5,47 | 5,26 | 5,11 | 4,81 |
| **10** | 10,04 | 7,56 | 6,55 | 5,99 | 5,64 | 5,39 | 5,06 | 4,85 | 4,71 | 4,41 |
| **11** | 9,65 | 7,21 | 6,22 | 5,67 | 5,32 | 5,07 | 4,74 | 4,54 | 4,40 | 4,10 |
| **12** | 9,33 | 6,93 | 5,95 | 5,41 | 5,06 | 4,82 | 4,50 | 4,30 | 4,16 | 3,86 |
| **13** | 9,07 | 6,70 | 5,74 | 5,21 | 4,86 | 4,62 | 4,30 | 4,10 | 3,96 | 3,66 |
| **14** | 8,86 | 6,51 | 5,56 | 5,04 | 4,69 | 4,46 | 4,14 | 3,94 | 3,80 | 3,51 |
| **15** | 8,68 | 6,36 | 5,42 | 4,89 | 4,56 | 4,32 | 4,00 | 3,80 | 3,67 | 3,37 |
| **16** | 8,53 | 6,23 | 5,29 | 4,77 | 4,44 | 4,20 | 3,89 | 3,69 | 3,55 | 3,26 |
| **17** | 8,40 | 6,11 | 5,18 | 4,67 | 4,34 | 4,10 | 3,79 | 3,59 | 3,46 | 3,16 |
| **18** | 8,29 | 6,01 | 5,09 | 4,58 | 4,25 | 4,01 | 3,71 | 3,51 | 3,37 | 3,08 |
| **19** | 8,18 | 5,93 | 5,01 | 4,50 | 4,17 | 3,94 | 3,63 | 3,43 | 3,30 | 3,00 |
| **20** | 8,10 | 5,85 | 4,94 | 4,43 | 4,10 | 3,87 | 3,56 | 3,37 | 3,23 | 2,94 |
| **25** | 7,77 | 5,57 | 4,68 | 4,18 | 3,85 | 3,63 | 3,32 | 3,13 | 2,99 | 2,70 |
| **30** | 7,56 | 5,39 | 4,51 | 4,02 | 3,70 | 3,47 | 3,17 | 2,98 | 2,84 | 2,55 |
| **40** | 7,31 | 5,18 | 4,31 | 3,83 | 3,51 | 3,29 | 2,99 | 2,80 | 2,66 | 2,37 |
| **60** | 7,08 | 4,98 | 4,13 | 3,65 | 3,34 | 3,12 | 2,82 | 2,63 | 2,50 | 2,20 |
| **120** | 6,85 | 4,79 | 3,95 | 3,48 | 3,17 | 2,96 | 2,66 | 2,47 | 2,34 | 2,03 |

---

### A.6 Nilai Kritis Korelasi Pearson

Nilai $|r|$ minimum agar korelasi dinyatakan berbeda nyata dari nol (uji dua arah), dengan db = $n - 2$.

| n | 0,05 | 0,01 |
|---|------|------|
| 5 | 0,878 | 0,959 |
| 6 | 0,811 | 0,917 |
| 7 | 0,754 | 0,875 |
| 8 | 0,707 | 0,834 |
| 9 | 0,666 | 0,798 |
| 10 | 0,632 | 0,765 |
| 12 | 0,576 | 0,708 |
| 14 | 0,532 | 0,661 |
| 16 | 0,497 | 0,623 |
| 18 | 0,468 | 0,590 |
| 20 | 0,444 | 0,561 |
| 25 | 0,396 | 0,505 |
| 30 | 0,361 | 0,463 |
| 35 | 0,334 | 0,430 |
| 40 | 0,312 | 0,403 |
| 50 | 0,279 | 0,361 |
| 60 | 0,254 | 0,330 |
| 80 | 0,220 | 0,286 |
| 100 | 0,197 | 0,256 |

> Perhatikan: pada n = 100, korelasi sebesar r = 0,20 sudah "signifikan" — padahal r² = 0,04, artinya hanya 4% keragaman yang berkaitan. **Signifikansi statistik bukan kekuatan hubungan.**

---

## Lampiran B: Formularium

### B.1 Statistika Deskriptif

| Besaran | Rumus |
|---------|-------|
| Rata-rata sampel | $\bar{x} = \dfrac{1}{n}\sum_{i=1}^{n} x_i$ |
| Rata-rata populasi | $\mu = \dfrac{1}{N}\sum_{i=1}^{N} x_i$ |
| Varians sampel | $s^2 = \dfrac{\sum (x_i - \bar{x})^2}{n-1}$ |
| Varians populasi | $\sigma^2 = \dfrac{\sum (x_i - \mu)^2}{N}$ |
| Simpangan baku | $s = \sqrt{s^2}$ |
| Koefisien variasi | $CV = \dfrac{s}{\bar{x}} \times 100\%$ |
| Jangkauan antarkuartil | $IQR = Q_3 - Q_1$ |
| Batas pencilan | $[\,Q_1 - 1{,}5\,IQR\;,\; Q_3 + 1{,}5\,IQR\,]$ |
| Skor baku | $z = \dfrac{x - \bar{x}}{s}$ |

### B.2 Probabilitas

| Aturan | Rumus |
|--------|-------|
| Komplemen | $P(A^c) = 1 - P(A)$ |
| Penjumlahan | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ |
| Perkalian | $P(A \cap B) = P(A)\,P(B \mid A)$ |
| Kejadian bebas | $P(A \cap B) = P(A)\,P(B)$ |
| Probabilitas bersyarat | $P(A \mid B) = \dfrac{P(A \cap B)}{P(B)}$ |
| Probabilitas total | $P(B) = \sum_i P(B \mid A_i)\,P(A_i)$ |
| **Teorema Bayes** | $P(A_i \mid B) = \dfrac{P(B \mid A_i)\,P(A_i)}{\sum_j P(B \mid A_j)\,P(A_j)}$ |
| Permutasi | $P(n,r) = \dfrac{n!}{(n-r)!}$ |
| Kombinasi | $C(n,r) = \dbinom{n}{r} = \dfrac{n!}{r!\,(n-r)!}$ |

### B.3 Peubah Acak

| Besaran | Diskret | Kontinu |
|---------|---------|---------|
| Ekspektasi | $E(X) = \sum x\,p(x)$ | $E(X) = \int x\,f(x)\,dx$ |
| Varians | $\text{Var}(X) = E(X^2) - [E(X)]^2$ | sama |
| Sifat linear | $E(aX + b) = a\,E(X) + b$ | sama |
| Varians transformasi | $\text{Var}(aX+b) = a^2\,\text{Var}(X)$ | sama |
| Jumlah peubah bebas | $E(X+Y) = E(X)+E(Y)$; $\text{Var}(X+Y) = \text{Var}(X)+\text{Var}(Y)$ | sama |

### B.4 Distribusi Penting

| Distribusi | PMF/PDF | Rata-rata | Varians |
|------------|---------|-----------|---------|
| Bernoulli($p$) | $p^x(1-p)^{1-x}$ | $p$ | $p(1-p)$ |
| Binomial($n,p$) | $\dbinom{n}{x} p^x (1-p)^{n-x}$ | $np$ | $np(1-p)$ |
| Poisson($\lambda$) | $\dfrac{e^{-\lambda}\lambda^x}{x!}$ | $\lambda$ | $\lambda$ |
| Geometrik($p$) | $(1-p)^{x-1}p$ | $1/p$ | $(1-p)/p^2$ |
| Uniform($a,b$) | $\dfrac{1}{b-a}$ | $\dfrac{a+b}{2}$ | $\dfrac{(b-a)^2}{12}$ |
| Eksponensial($\lambda$) | $\lambda e^{-\lambda x}$ | $1/\lambda$ | $1/\lambda^2$ |
| Normal($\mu,\sigma^2$) | $\dfrac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ | $\mu$ | $\sigma^2$ |

### B.5 Distribusi Sampling dan Estimasi

| Besaran | Rumus |
|---------|-------|
| Galat baku rata-rata | $SE_{\bar{x}} = \dfrac{\sigma}{\sqrt{n}}$ atau $\dfrac{s}{\sqrt{n}}$ |
| Galat baku proporsi | $SE_{\hat{p}} = \sqrt{\dfrac{p(1-p)}{n}}$ |
| IK rata-rata (σ diketahui) | $\bar{x} \pm z_{\alpha/2}\dfrac{\sigma}{\sqrt{n}}$ |
| IK rata-rata (σ tidak diketahui) | $\bar{x} \pm t_{\alpha/2,\,n-1}\dfrac{s}{\sqrt{n}}$ |
| IK proporsi | $\hat{p} \pm z_{\alpha/2}\sqrt{\dfrac{\hat{p}(1-\hat{p})}{n}}$ |
| IK selisih dua rata-rata | $(\bar{x}_1-\bar{x}_2) \pm t_{\alpha/2}\,SE_{\text{selisih}}$ |
| Ukuran sampel (rata-rata) | $n = \left(\dfrac{z_{\alpha/2}\,\sigma}{E}\right)^2$ |
| Ukuran sampel (proporsi) | $n = \dfrac{z_{\alpha/2}^2\,p(1-p)}{E^2}$ |

### B.6 Uji Hipotesis

| Uji | Statistik uji | db |
|-----|---------------|-----|
| z satu sampel | $z = \dfrac{\bar{x}-\mu_0}{\sigma/\sqrt{n}}$ | — |
| t satu sampel | $t = \dfrac{\bar{x}-\mu_0}{s/\sqrt{n}}$ | $n-1$ |
| z satu proporsi | $z = \dfrac{\hat{p}-p_0}{\sqrt{p_0(1-p_0)/n}}$ | — |
| t dua sampel (varians sama) | $t = \dfrac{\bar{x}_1-\bar{x}_2}{s_p\sqrt{1/n_1+1/n_2}}$ | $n_1+n_2-2$ |
| Varians gabungan | $s_p^2 = \dfrac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}$ | — |
| t Welch (varians beda) | $t = \dfrac{\bar{x}_1-\bar{x}_2}{\sqrt{s_1^2/n_1+s_2^2/n_2}}$ | hampiran Welch |
| t berpasangan | $t = \dfrac{\bar{d}}{s_d/\sqrt{n}}$ | $n-1$ |
| z dua proporsi | $z = \dfrac{\hat{p}_1-\hat{p}_2}{\sqrt{\hat{p}(1-\hat{p})(1/n_1+1/n_2)}}$ | — |
| Chi-square | $\chi^2 = \sum \dfrac{(O-E)^2}{E}$ | lihat A.3 |
| ANOVA | $F = \dfrac{MS_{\text{antar}}}{MS_{\text{dalam}}}$ | $k-1$, $N-k$ |

### B.7 Ukuran Efek

| Ukuran | Rumus | Kecil | Sedang | Besar |
|--------|-------|-------|--------|-------|
| Cohen's d | $d = \dfrac{\bar{x}_1-\bar{x}_2}{s_p}$ | 0,2 | 0,5 | 0,8 |
| $\eta^2$ (ANOVA) | $\eta^2 = \dfrac{SS_{\text{antar}}}{SS_{\text{total}}}$ | 0,01 | 0,06 | 0,14 |
| Cramér's V | $V = \sqrt{\dfrac{\chi^2}{n\,(\min(r,c)-1)}}$ | 0,10 | 0,30 | 0,50 |
| $r^2$ (regresi) | proporsi keragaman terjelaskan | 0,01 | 0,09 | 0,25 |

> **Wajib dilaporkan bersama *p-value*.** *p* menjawab "apakah ada"; ukuran efek menjawab "seberapa besar". Hanya keduanya bersama yang berguna.

### B.8 Korelasi dan Regresi

| Besaran | Rumus |
|---------|-------|
| Kovarians | $\text{Cov}(X,Y) = \dfrac{\sum (x_i-\bar{x})(y_i-\bar{y})}{n-1}$ |
| Korelasi Pearson | $r = \dfrac{\text{Cov}(X,Y)}{s_X\,s_Y}$ |
| Uji signifikansi r | $t = \dfrac{r\sqrt{n-2}}{\sqrt{1-r^2}}$, db = $n-2$ |
| Kemiringan regresi | $b_1 = r\,\dfrac{s_Y}{s_X} = \dfrac{\sum(x_i-\bar{x})(y_i-\bar{y})}{\sum(x_i-\bar{x})^2}$ |
| Intersep | $b_0 = \bar{y} - b_1\bar{x}$ |
| Koefisien determinasi | $R^2 = 1 - \dfrac{SS_{\text{residual}}}{SS_{\text{total}}}$ |
| Galat baku estimasi | $s_e = \sqrt{\dfrac{\sum (y_i-\hat{y}_i)^2}{n-2}}$ |

---

## Lampiran C: Pohon Keputusan Pemilihan Uji

```
LANGKAH 1 — Apa jenis datanya?
│
├── NUMERIK (rasio/interval)
│   │
│   └── LANGKAH 2 — Apa yang dibandingkan?
│       │
│       ├── Satu kelompok vs nilai acuan
│       │   ├── σ diketahui, n besar ──────► Uji-z satu sampel
│       │   └── σ tidak diketahui ─────────► Uji-t satu sampel
│       │
│       ├── Dua kelompok
│       │   ├── BEBAS (subjek berbeda)
│       │   │   ├── Varians homogen ───────► Uji-t dua sampel gabungan
│       │   │   └── Varians tidak homogen ─► Uji-t Welch
│       │   └── BERPASANGAN (subjek sama)
│       │       └─────────────────────────► Uji-t berpasangan
│       │
│       ├── Tiga kelompok atau lebih ──────► ANOVA satu arah
│       │                                     └─ bila signifikan: uji lanjut
│       │
│       └── Hubungan dua variabel
│           ├── Linear, data normal ───────► Korelasi Pearson
│           ├── Monoton, ada pencilan ─────► Korelasi Spearman
│           └── Memprediksi y dari x ──────► Regresi linear sederhana
│
└── KATEGORIK
    │
    └── LANGKAH 2 — Apa yang diuji?
        │
        ├── Satu proporsi vs acuan ────────► Uji-z satu proporsi
        ├── Dua proporsi ──────────────────► Uji-z dua proporsi
        ├── Sebaran vs harapan ────────────► Chi-square kesesuaian
        └── Hubungan dua variabel ─────────► Chi-square kebebasan
```

### C.1 Asumsi yang Harus Diperiksa

| Uji | Asumsi | Cara memeriksa |
|-----|--------|----------------|
| Uji-t satu sampel | Kenormalan (atau n ≥ 30) | Shapiro-Wilk, Q-Q plot |
| Uji-t dua sampel | Kenormalan tiap kelompok; kesamaan varians | Shapiro-Wilk; uji Levene |
| Uji-t berpasangan | Kenormalan **selisih** | Shapiro-Wilk pada selisih |
| ANOVA | Kenormalan residual; kesamaan varians; kebebasan | Shapiro-Wilk; Levene; rancangan |
| Chi-square | Frekuensi harapan ≥ 5 pada ≥ 80% sel | Periksa matriks frekuensi harapan |
| Regresi linear | **L**inear, **I**ndependen, **N**ormal residual, **E**qual variance | Plot residual, Q-Q plot, Durbin-Watson |
| Korelasi Pearson | Hubungan linear; tanpa pencilan ekstrem | **Scatter plot** |

> **Kaidah tetap:** tidak ada uji yang dijalankan sebelum datanya dilihat bentuknya.

---

## Lampiran D: Pustaka Python untuk Statistika

### D.1 Persiapan Google Colab

```python
# Seluruh pustaka berikut sudah tersedia di Google Colab —
# tidak perlu dipasang.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.api as sm

# Pengaturan tampilan yang disarankan
pd.set_option("display.max_columns", 50)
pd.set_option("display.float_format", "{:.4f}".format)
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (8, 5)
plt.rcParams["figure.dpi"] = 110

# Tetapkan seed agar hasil dapat direproduksi
np.random.seed(42)
```

### D.2 Statistika Deskriptif

| Keperluan | Perintah |
|-----------|----------|
| Ringkasan menyeluruh | `df.describe()` |
| Rata-rata | `df["kol"].mean()` |
| Median | `df["kol"].median()` |
| Modus | `df["kol"].mode()` |
| Simpangan baku sampel | `df["kol"].std()` — **pembagi n−1** |
| Simpangan baku populasi | `df["kol"].std(ddof=0)` |
| Kuartil | `df["kol"].quantile([0.25, 0.5, 0.75])` |
| Kemencengan | `df["kol"].skew()` |
| Keruncingan | `df["kol"].kurt()` |
| Ringkasan per kelompok | `df.groupby("grup")["kol"].describe()` |
| Tabel kontingensi | `pd.crosstab(df["a"], df["b"])` |

> **Catatan penting:** `numpy.std()` memakai pembagi $n$ (`ddof=0`), sedangkan `pandas.std()` memakai $n-1$ (`ddof=1`). Untuk simpangan baku **sampel**, pakai `ddof=1`.

### D.3 Distribusi Probabilitas (`scipy.stats`)

| Keperluan | Perintah |
|-----------|----------|
| PMF binomial | `stats.binom.pmf(k, n, p)` |
| CDF binomial | `stats.binom.cdf(k, n, p)` |
| PMF Poisson | `stats.poisson.pmf(k, mu)` |
| PDF normal | `stats.norm.pdf(x, loc, scale)` |
| CDF normal | `stats.norm.cdf(x, loc, scale)` |
| Kuantil normal (invers) | `stats.norm.ppf(q, loc, scale)` |
| Nilai kritis t | `stats.t.ppf(1 - alpha/2, df)` |
| Nilai kritis chi-square | `stats.chi2.ppf(1 - alpha, df)` |
| Nilai kritis F | `stats.f.ppf(1 - alpha, df1, df2)` |
| Membangkitkan sampel | `stats.norm.rvs(loc, scale, size=n, random_state=42)` |

### D.4 Uji Hipotesis

| Uji | Perintah |
|-----|----------|
| t satu sampel | `stats.ttest_1samp(data, popmean=mu0)` |
| t dua sampel (varians sama) | `stats.ttest_ind(a, b)` |
| t Welch | `stats.ttest_ind(a, b, equal_var=False)` |
| t berpasangan | `stats.ttest_rel(sebelum, sesudah)` |
| ANOVA satu arah | `stats.f_oneway(g1, g2, g3)` |
| Chi-square kebebasan | `stats.chi2_contingency(tabel)` |
| Chi-square kesesuaian | `stats.chisquare(f_obs, f_exp)` |
| Korelasi Pearson | `stats.pearsonr(x, y)` |
| Korelasi Spearman | `stats.spearmanr(x, y)` |
| Uji kenormalan | `stats.shapiro(data)` |
| Uji kesamaan varians | `stats.levene(g1, g2, g3)` |
| Mann-Whitney (nonparametrik) | `stats.mannwhitneyu(a, b)` |
| Kruskal-Wallis (nonparametrik) | `stats.kruskal(g1, g2, g3)` |

> **Uji satu arah:** `scipy` menyediakan `alternative="greater"` atau `"less"`. Bila versi yang dipakai tidak mendukungnya, bagi dua *p-value* dua arah **dan pastikan arah statistik uji sesuai hipotesis**.

### D.5 Regresi (`statsmodels`)

```python
import statsmodels.api as sm

X = sm.add_constant(df["luas"])      # wajib: menambahkan intersep
model = sm.OLS(df["harga"], X).fit()
print(model.summary())

# Diagnostik residual
residual = model.resid
fitted = model.fittedvalues

fig, ax = plt.subplots(1, 2, figsize=(12, 4))
ax[0].scatter(fitted, residual, alpha=0.6)
ax[0].axhline(0, color="red", linestyle="--")
ax[0].set_xlabel("Nilai prediksi"); ax[0].set_ylabel("Residual")
ax[0].set_title("Residual vs Prediksi")

sm.qqplot(residual, line="45", fit=True, ax=ax[1])
ax[1].set_title("Q-Q Plot Residual")
plt.tight_layout()
```

### D.6 Visualisasi

| Jenis grafik | Perintah | Dipakai untuk |
|--------------|----------|---------------|
| Histogram | `sns.histplot(data=df, x="kol", bins=20)` | Sebaran satu variabel numerik |
| Box plot | `sns.boxplot(data=df, x="grup", y="nilai")` | Perbandingan antar kelompok |
| Violin plot | `sns.violinplot(data=df, x="grup", y="nilai")` | Bentuk sebaran antar kelompok |
| Scatter plot | `sns.scatterplot(data=df, x="x", y="y")` | Hubungan dua variabel numerik |
| Scatter + garis regresi | `sns.regplot(data=df, x="x", y="y")` | Hubungan linear |
| Bar chart | `sns.barplot(data=df, x="kat", y="nilai")` | Perbandingan kategori |
| Count plot | `sns.countplot(data=df, x="kat")` | Frekuensi kategori |
| Heatmap korelasi | `sns.heatmap(df.corr(numeric_only=True), annot=True)` | Matriks korelasi |
| Q-Q plot | `stats.probplot(data, dist="norm", plot=plt)` | Pemeriksaan kenormalan |

### D.7 Daftar Periksa Grafik

- [ ] Judul menyatakan **temuan**, bukan sekadar nama variabel
- [ ] Label sumbu lengkap **dengan satuan**
- [ ] Ukuran sampel (n) dicantumkan
- [ ] Sumber data dicantumkan
- [ ] Sumbu-y bar chart **dimulai dari nol**
- [ ] Skala warna sesuai (berurutan untuk numerik, kategorik untuk nominal)
- [ ] Terbaca bila dicetak hitam-putih

---

## Lampiran E: Glosarium

| Indonesia | Inggris | Makna ringkas |
|-----------|---------|---------------|
| Alfa (taraf nyata) | Significance level | Batas peluang menolak H₀ yang benar; lazim 0,05 |
| ANOVA | Analysis of Variance | Uji beda rata-rata tiga kelompok atau lebih |
| Beta | Type II error rate | Peluang gagal menolak H₀ yang salah |
| Bias | Bias | Penyimpangan sistematis penduga dari nilai sebenarnya |
| Daya uji | Statistical power | $1-\beta$; peluang menemukan efek yang memang ada |
| Derajat bebas | Degrees of freedom | Banyaknya nilai yang bebas bervariasi |
| Distribusi sampling | Sampling distribution | Sebaran statistik dari seluruh kemungkinan sampel |
| Galat baku | Standard error | Simpangan baku distribusi sampling |
| Galat Tipe I | Type I error | Menolak H₀ yang benar (*positif palsu*) |
| Galat Tipe II | Type II error | Gagal menolak H₀ yang salah (*negatif palsu*) |
| Hipotesis nol | Null hypothesis | Pernyataan "tidak ada efek/perbedaan" |
| Hipotesis alternatif | Alternative hypothesis | Pernyataan yang hendak dibuktikan |
| Interval kepercayaan | Confidence interval | Rentang nilai plausibel bagi parameter |
| Kemencengan | Skewness | Ukuran ketidaksimetrisan sebaran |
| Keruncingan | Kurtosis | Ukuran ketebalan ekor sebaran |
| Kovarians | Covariance | Ukuran arah hubungan dua peubah |
| Korelasi | Correlation | Kovarians ternormalisasi, rentang [−1, 1] |
| Nilai-p | p-value | Peluang data seekstrem ini **bila H₀ benar** |
| Parameter | Parameter | Besaran populasi (μ, σ, p) |
| Pencilan | Outlier | Pengamatan yang jauh dari pola umum |
| Peubah acak | Random variable | Fungsi dari ruang sampel ke bilangan riil |
| Populasi | Population | Keseluruhan objek yang hendak disimpulkan |
| Proporsi | Proportion | Bagian dari keseluruhan, rentang [0, 1] |
| Regresi | Regression | Pemodelan hubungan variabel respons dan penjelas |
| Residual | Residual | Selisih nilai teramati dan nilai prediksi |
| Sampel | Sample | Bagian populasi yang diamati |
| Statistik | Statistic | Besaran sampel ($\bar{x}$, $s$, $\hat{p}$) |
| Taksiran titik | Point estimate | Satu nilai sebagai dugaan parameter |
| Teorema Limit Pusat | Central Limit Theorem | Distribusi rata-rata sampel mendekati normal pada n besar |
| Ukuran efek | Effect size | Besarnya perbedaan/hubungan, bebas ukuran sampel |
| Variabel perancu | Confounding variable | Variabel ketiga yang memengaruhi keduanya |
| Varians | Variance | Rata-rata kuadrat simpangan dari rata-rata |

---

## Lampiran F: Kesalahan Tafsir yang Sering Terjadi

Periksa daftar ini sebelum menyerahkan laporan apa pun.

| # | Kalimat yang keliru | Mengapa keliru | Versi yang benar |
|---|---------------------|----------------|------------------|
| 1 | "p = 0,03 berarti peluang H₀ benar adalah 3%" | *p* dihitung **dengan mengandaikan H₀ benar** | "Bila H₀ benar, peluang memperoleh data seekstrem ini adalah 3%" |
| 2 | "p > 0,05, jadi tidak ada perbedaan" | Tidak menolak ≠ membuktikan tidak ada | "Tidak ditemukan cukup bukti adanya perbedaan" |
| 3 | "IK 95% berarti 95% data berada dalam rentang ini" | IK tentang **parameter**, bukan data | "Prosedur ini menghasilkan rentang yang memuat parameter pada 95% pengulangan" |
| 4 | "Hasilnya sangat signifikan (p < 0,001)" | Signifikansi bukan besaran bertingkat | "p < 0,001, dengan Cohen's d = 0,23 (efek kecil)" |
| 5 | "X berkorelasi dengan Y, jadi X menyebabkan Y" | Korelasi tidak menyiratkan sebab | "X berkaitan dengan Y; rancangan ini tidak dapat menyimpulkan sebab" |
| 6 | "r = 0,7 berarti 70% hubungan" | r bukan persentase; r² yang proporsi | "r = 0,7; r² = 0,49, artinya 49% keragaman berkaitan" |
| 7 | "Sampel besar, jadi pasti mewakili" | Ukuran tidak mengatasi bias pemilihan | "n besar mengurangi galat acak, tetapi tidak mengatasi bias pemilihan" |
| 8 | "Data tidak normal, jadi tidak bisa dianalisis" | Banyak alternatif tersedia | "Karena data tidak normal, dipakai uji Mann-Whitney" |
| 9 | "Pencilan dibuang agar hasilnya lebih baik" | Manipulasi hasil | "Pencilan diperiksa; terbukti data sah, maka dipertahankan" |
| 10 | "Model memprediksi nilai pada x = 500" (data hanya sampai 200) | Ekstrapolasi | "Model berlaku pada rentang x = 30–200" |
| 11 | "Penelitian ini tidak memiliki keterbatasan" | Selalu ada keterbatasan | Tulis minimal empat butir keterbatasan |
| 12 | "AI yang menghitung, jadi pasti benar" | Tanggung jawab tetap pada analis | "Setiap keluaran telah diverifikasi; rinciannya pada AI Usage Log" |

---

## Lampiran G: Sumber Data Berkonteks Indonesia

| Sumber | Cakupan | Tautan |
|--------|---------|--------|
| Badan Pusat Statistik | Statistik resmi nasional dan daerah | <https://www.bps.go.id> |
| Satu Data Indonesia | Portal data lintas kementerian/lembaga | <https://data.go.id> |
| Jakarta Open Data | Data Pemprov DKI Jakarta | <https://data.jakarta.go.id> |
| SIRUSA BPS | **Definisi baku setiap variabel statistik** | <https://sirusa.bps.go.id> |
| Kementerian Kesehatan | Data kesehatan dan fasilitas | <https://data.kemkes.go.id> |
| Kemendikbudristek | Data pendidikan (Dapodik, PDDikti) | <https://pddikti.kemdikbud.go.id> |
| BMKG | Data cuaca dan iklim | <https://dataonline.bmkg.go.id> |
| Kaggle (Indonesia) | Kumpulan data bertema Indonesia | <https://www.kaggle.com/datasets?search=indonesia> |

> **Wajib dicatat setiap kali mengunduh:** tautan lengkap, tanggal akses, jumlah baris dan kolom, lisensi, dan **definisi tiap variabel** dari sumbernya. Panduan lengkap ada pada [datasets/README.md](../datasets/README.md).

---

## Lampiran H: Peta Bab – Modul – Praktikum

| Minggu | Bab | Modul Kuliah | Praktikum |
|--------|-----|--------------|-----------|
| 1 | [Bab 1](bab-01-pengantar-statistika-ketidakpastian.md) | [Minggu 1](../03-modules/week-01-pengantar-statistika-data-ketidakpastian.md) | [Lab 1](../04-labs/lab-01-setup-colab-eksplorasi-data.md) |
| 2 | [Bab 2](bab-02-statistika-deskriptif.md) | [Minggu 2](../03-modules/week-02-statistika-deskriptif.md) | [Lab 2](../04-labs/lab-02-statistika-deskriptif-pandas.md) |
| 3 | [Bab 3](bab-03-visualisasi-data-statistik.md) | [Minggu 3](../03-modules/week-03-visualisasi-data-statistik.md) | [Lab 3](../04-labs/lab-03-studio-visualisasi-statistik.md) |
| 4 | [Bab 4](bab-04-dasar-probabilitas.md) | [Minggu 4](../03-modules/week-04-dasar-probabilitas.md) | [Lab 4](../04-labs/lab-04-simulasi-probabilitas-monte-carlo.md) |
| 5 | [Bab 5](bab-05-probabilitas-bersyarat-bayes.md) | [Minggu 5](../03-modules/week-05-teorema-bayes-kebebasan.md) | [Lab 5](../04-labs/lab-05-bayes-penyaring-spam.md) |
| 6 | [Bab 6](bab-06-peubah-acak-distribusi-diskret.md) | [Minggu 6](../03-modules/week-06-peubah-acak-diskret.md) | [Lab 6](../04-labs/lab-06-distribusi-diskret-scipy.md) |
| 7 | [Bab 7](bab-07-distribusi-kontinu-normal.md) | [Minggu 7](../03-modules/week-07-peubah-acak-kontinu-normal.md) | [Lab 7](../04-labs/lab-07-distribusi-kontinu-uji-kenormalan.md) |
| 8 | — | [Minggu 8 — UTS](../03-modules/week-08-uts-review-dan-ujian.md) | — |
| 9 | [Bab 8](bab-08-ekspektasi-varians-sampling.md) | [Minggu 9](../03-modules/week-09-ekspektasi-varians-distribusi-sampling.md) | [Lab 9](../04-labs/lab-09-simulasi-teorema-limit-pusat.md) |
| 10 | [Bab 9](bab-09-estimasi-interval-kepercayaan.md) | [Minggu 10](../03-modules/week-10-estimasi-interval-kepercayaan.md) | [Lab 10](../04-labs/lab-10-interval-kepercayaan-cakupan.md) |
| 11 | [Bab 10](bab-10-uji-hipotesis-satu-sampel.md) | [Minggu 11](../03-modules/week-11-uji-hipotesis-satu-sampel.md) | [Lab 11](../04-labs/lab-11-uji-hipotesis-satu-sampel.md) |
| 12 | [Bab 11](bab-11-uji-hipotesis-dua-sampel.md) | [Minggu 12](../03-modules/week-12-uji-hipotesis-dua-sampel.md) | [Lab 12](../04-labs/lab-12-ab-testing-dua-sampel.md) |
| 13 | [Bab 12](bab-12-anova-chi-square.md) | [Minggu 13](../03-modules/week-13-anova-chi-square.md) | [Lab 13](../04-labs/lab-13-anova-chi-square.md) |
| 14 | [Bab 13](bab-13-korelasi-regresi-linear.md) · [Bab 14](bab-14-proyek-akhir.md) | [Minggu 14](../03-modules/week-14-korelasi-regresi-linear.md) | [Lab 14](../04-labs/lab-14-korelasi-regresi-linear.md) |
| 15 | [Bab 14](bab-14-proyek-akhir.md) | [Minggu 15](../03-modules/week-15-presentasi-proyek.md) | — |
| 16 | — | [Minggu 16 — UAS](../03-modules/week-16-uas-review-dan-ujian.md) | — |

---

## Catatan Penyusunan Tabel

Seluruh tabel pada Lampiran A dihitung dengan `scipy.stats` (Python 3), bukan disalin dari sumber lain, sehingga dapat diperiksa ulang:

```python
from scipy import stats

stats.norm.cdf(1.96)          # → 0,9750   (Tabel Z)
stats.t.ppf(0.975, 20)        # → 2,086    (Tabel t, db = 20)
stats.chi2.ppf(0.95, 3)       # → 7,815    (Tabel χ², db = 3)
stats.f.ppf(0.95, 3, 20)      # → 3,10     (Tabel F, α = 0,05)
```

Pembulatan: Tabel Z empat angka di belakang koma; Tabel t dan χ² tiga angka; Tabel F dua angka. Pemisah desimal memakai **koma**, sesuai kaidah bahasa Indonesia.
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
