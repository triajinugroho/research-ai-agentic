---
id: uai-inf-konversi-nilai
tipe: pedoman
judul: Konversi Nilai Angka ke Nilai Huruf — Skala Baku UAI
prodi: Informatika
universitas: Universitas Al Azhar Indonesia
versi: 1.0
status: berlaku
diperbarui: 2026-10-07
berlaku_untuk: [IF52510031, IF52510033, ST52510002, IF52510021, IF52520004, IF52520005, IF52520025, INF-101, INF-102, TBD-STAT, IF2205, IF2206, IF3XXX]
---

# Konversi Nilai Angka ke Nilai Huruf

> **Kedudukan berkas.** Ini satu-satunya tempat skala konversi nilai ditetapkan di repositori ini (prinsip *satu fakta satu tempat*, Pedoman OBE §C.3). Bagian "Konversi Nilai" pada setiap RPS dan kerangka asesmen **menyalin tabel di bawah apa adanya dan menautkan ke berkas ini**. Bila ada perbedaan, berkas inilah yang berlaku.

## A. Tabel Konversi

| Rentang Nilai Akhir | Huruf | Bobot | Keterangan |
|---------------------|-------|-------|------------|
| 81,00 – 100 | A | 4,00 | Sangat baik |
| 75,00 – 80,99 | B+ | 3,50 | Baik sekali |
| 69,00 – 74,99 | B | 3,00 | Baik |
| 63,00 – 68,99 | C+ | 2,50 | Cukup baik |
| 56,00 – 62,99 | C | 2,00 | Cukup — **batas lulus** |
| 45,00 – 55,99 | D | 1,00 | Kurang |
| 0 – 44,99 | E | 0,00 | Tidak lulus |

**Ketentuan baku:**

1. Skala terdiri atas **tujuh** huruf mutu. Huruf **A−** dan **B−** tidak dipakai.
2. Batas lulus mata kuliah adalah **C (56,00)**.
3. Rentang ditulis dengan dua desimal agar nilai pecahan (mis. 80,50) tidak jatuh di celah antarbaris. Batas bawah setiap huruf bersifat inklusif.

## B. Status Sumber

| Aspek | Status | Keterangan |
|-------|:------:|------------|
| Batas bawah A = 81 | 🟡 | Dikonfirmasi dosen pengampu sebagai standar UAI (Oktober 2026) |
| Rentang dan bobot huruf lainnya | 🟡 | Disalin dari skala yang ditetapkan dosen pengampu pada RPS IF2205 dan IF2206 (commit `ab45a38`, 12 April 2026) |
| Salinan peraturan akademik resmi UAI | 🔲 | Belum diarsipkan. Simpan salinannya di `00-pedoman-obe/sumber/`, cocokkan seluruh baris tabel §A, lalu ubah status dua baris di atas menjadi ✅ dengan nomor dokumennya |
| Aturan pembulatan nilai akhir sebelum konversi | 🔲 | Belum ada ketentuan tertulis di repositori. Konfirmasikan ke BAAK/SIAKAD |

Status mengikuti sistem tiga status pada Pedoman OBE §B.1: ✅ terverifikasi · 🟡 kerangka terverifikasi, teks resmi belum ada · 🔲 menunggu dokumen.

## C. Yang Bukan Bagian Skala Ini

- **Syarat kelulusan tambahan** yang ditetapkan per mata kuliah (mis. capaian minimum per Sub-CPMK, jumlah wawancara pelanggan, keikutsertaan presentasi) adalah kebijakan mata kuliah. Syarat semacam itu **harus disetujui Program Studi** sebelum diberlakukan, karena dapat membuat mahasiswa dengan nilai akhir ≥ 56,00 tetap tidak lulus.
- **Ambang ketuntasan Sub-CPMK/CPL** (mis. ≥ 60 tuntas) adalah ukuran mutu untuk siklus PPEPP, bukan syarat kelulusan. Penetapannya menunggu SK ambang ketercapaian CPL (Pedoman OBE §K).
- **Pita deskriptor rubrik** (mis. skor 1–4 per kriteria) tidak sama dengan huruf mutu dan tidak perlu mengikuti rentang di atas.

## D. Riwayat Skala di Repositori

Sebelum berkas ini dibuat, repositori memuat sedikitnya empat versi skala yang saling bertentangan:

| Versi | Ciri | Dipakai di |
|-------|------|-----------|
| Baku (berkas ini) | A ≥ 81; 7 huruf; lulus ≥ 56 | IF2205, IF2206 |
| Lama 1 | A ≥ 85; 9 huruf dengan A− dan B−; lulus ≥ 55 | IF52510031, IF52510033, ST52510002 (diselaraskan Oktober 2026) |
| Lama 2 | A ≥ 85; 9 huruf; D 40–54,99; E < 40 | IF52510021 |
| Lama 3 | A ≥ 85/86 dengan beragam varian | INF-101, INF-102, Analisis Data Statistik, IF3XXX |

Mata kuliah yang masih memakai versi lama diselaraskan pada saat RPS-nya diperbarui ke Kurikulum 2025 Revisi 2026.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
