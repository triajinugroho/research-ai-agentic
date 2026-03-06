---
id: "nugget-alp-01-02"
title: "Algoritma dalam Kehidupan Sehari-hari"
course: "alp"
week: 1
sequence: 2
type: "example"
topic_slug: "algoritma-kehidupan-sehari-hari"

cpmk: ["CPMK-1"]
sub_cpmk: ["CPMK-1.1"]
bloom_level: "C2"
difficulty: 1
estimated_minutes: 7

prerequisites: ["nugget-alp-01-01"]
related: ["nugget-alp-01-03", "nugget-alp-01-05"]
cross_course: []

modality: ["text", "diagram", "table"]
has_interactive_code: false
has_quiz: true
quiz_count: 2

review_priority: "medium"
key_concepts:
  - "Algoritma dalam konteks sehari-hari"
  - "Perbedaan algoritma baik dan buruk"
  - "Urutan langkah yang logis"

tags: ["algoritma", "contoh", "kehidupan-sehari-hari", "indonesia"]
---

# Algoritma dalam Kehidupan Sehari-hari

> **Pertanyaan Pemicu:** Apa yang terjadi jika langkah-langkah dalam resep membuat nasi goreng diacak urutannya?

---

## Contoh 1: Menarik Uang di ATM BCA

Perhatikan algoritma berikut:

```
MULAI
  1. Masukkan kartu ATM ke mesin
  2. Pilih bahasa (Indonesia / English)
  3. Masukkan PIN 6 digit
  4. JIKA PIN benar:
       5. Pilih menu "Penarikan Tunai"
       6. Pilih nominal (Rp100.000 / Rp500.000 / jumlah lain)
       7. JIKA saldo cukup:
            8. Ambil uang yang keluar
            9. Pilih "Ya" atau "Tidak" untuk transaksi lain
           10. Ambil kartu ATM
           11. Ambil struk (opsional)
          JIKA saldo tidak cukup:
            8. Tampilkan pesan "Saldo tidak mencukupi"
            9. Kembali ke menu utama
     JIKA PIN salah:
       5. Tampilkan pesan "PIN salah"
       6. Ulangi (maksimal 3 kali)
SELESAI
```

**Mari kita cek 5 karakteristik:**

| Karakteristik | Terpenuhi? | Penjelasan |
|---------------|-----------|------------|
| Finiteness | Ya | Ada langkah SELESAI, maksimal 3 kali percobaan PIN |
| Definiteness | Ya | Setiap langkah jelas ("masukkan PIN 6 digit", bukan "masukkan PIN") |
| Input | Ya | Kartu ATM, PIN, pilihan nominal |
| Output | Ya | Uang tunai, struk |
| Effectiveness | Ya | Semua langkah bisa dilakukan oleh pengguna |

---

## Contoh 2: Menentukan Tarif TransJakarta

Algoritma untuk menentukan apakah penumpang membayar tarif normal atau gratis:

```
MULAI
  1. Penumpang tap kartu di gate
  2. BACA jenis_kartu
  3. JIKA jenis_kartu == "Lansia" ATAU jenis_kartu == "Disabilitas":
       tarif = 0  (gratis)
     JIKA jenis_kartu == "Pelajar":
       tarif = 1500
     SELAINNYA:
       tarif = 3500
  4. JIKA saldo_kartu >= tarif:
       potong saldo
       buka gate
     SELAINNYA:
       tampilkan "Saldo tidak cukup"
       gate tetap tertutup
SELESAI
```

> **Perhatikan:** Algoritma ini memiliki **percabangan** (decision) — langkah yang berbeda tergantung kondisi. Ini sangat umum dalam algoritma komputer!

---

## Contoh 3: Algoritma yang BURUK

Bandingkan dua algoritma membuat kopi:

**Algoritma A (Baik):**
```
1. Siapkan gelas bersih
2. Masukkan 1 sendok teh kopi ke gelas
3. Masukkan 2 sendok teh gula ke gelas
4. Tuangkan air panas 200ml ke gelas
5. Aduk selama 10 detik
6. Kopi siap disajikan
```

**Algoritma B (Buruk):**
```
1. Siapkan gelas
2. Masukkan kopi secukupnya        ← tidak definite!
3. Masukkan gula sesuai selera     ← tidak definite!
4. Aduk terus sampai enak          ← kapan berhenti? tidak finite!
5. Tambahkan air                   ← berapa ml? panas atau dingin?
```

Algoritma B melanggar prinsip **definiteness** (langkah ambigu) dan **finiteness** ("sampai enak" bisa tak terbatas).

---

## Cek Pemahaman

**Soal 1** (C2 — Understand):
Dalam algoritma ATM di atas, apa yang terjadi jika pengguna salah memasukkan PIN sebanyak 3 kali?

- A) Mesin mengeluarkan kartu dan proses selesai ✓
- B) Mesin meminta PIN untuk ke-4 kalinya
- C) Mesin langsung mengeluarkan uang
- D) Tidak ada yang terjadi

> **Penjelasan:** Algoritma memiliki batas "maksimal 3 kali" — ini memenuhi karakteristik **finiteness**. Setelah 3 kali salah, kartu biasanya diblokir dan dikembalikan.

**Soal 2** (C2 — Understand):
Mengapa "aduk terus sampai enak" adalah langkah algoritma yang **buruk**?

- A) Karena tidak menggunakan bahasa Python
- B) Karena melanggar prinsip finiteness dan definiteness ✓
- C) Karena terlalu panjang
- D) Karena tidak ada input

> **Penjelasan:** "Sampai enak" tidak memiliki kriteria berhenti yang jelas (melanggar **finiteness**) dan "enak" itu subjektif, tidak bisa diukur (melanggar **definiteness**).

---

## Poin Penting

- Algoritma bukan hanya di komputer — ada di mana-mana dalam kehidupan
- Algoritma yang baik: langkah **jelas**, ada **batas akhir**, menghasilkan **output**
- Konteks Indonesia: ATM BCA, TransJakarta, GoFood — semua dijalankan oleh algoritma
- Latihan menyusun algoritma dalam bahasa sehari-hari adalah fondasi penting sebelum belajar coding

**Selanjutnya:** Kita akan belajar *Computational Thinking* — cara berpikir seperti programmer →

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
