---
id: uai-inf-checklist-verifikasi
tipe: pedoman
judul: Checklist Verifikasi Manual — Paket Mata Kuliah OBE
prodi: Informatika
universitas: Universitas Al Azhar Indonesia
versi: 1.0
status: berlaku
diperbarui: 2026-09-05
berlaku_untuk: [INF-101, INF-102, TBD-STAT, IF2205, IF2206, IF3XXX]
---

# Checklist Verifikasi Manual

> **Pembagian tugas.** `tools/validasi-obe.py` memeriksa yang dapat dimekanisasi (V1–V12). Checklist ini memeriksa yang **tidak dapat diskripkan**: mutu rumusan, ketepatan pedagogis, dan kebenaran substansi. Keduanya wajib dijalankan.
>
> **Tanda tangan penelaah sejawat pada bagian akhir bukan formalitas** — telaah sejawat adalah bukti langsung kriteria 1 (Budaya Mutu) Instrumen LAM-INFOKOM 2.0.

## A. Menjalankan Validator Otomatis

```bash
python3 tools/validasi-obe.py                 # seluruh repositori
python3 tools/validasi-obe.py --mk INF-101    # satu mata kuliah
```

Keluar dengan kode 0 bila bersih. **Syarat lulus: 0 pelanggaran** untuk mata kuliah yang sedang diverifikasi.

### Pemeriksaan cepat tanpa skrip

```bash
# Sisa kode Sub-CPMK bentuk lama (harus kosong)
grep -rEn '(^|[^-])CPMK-[0-9]+\.[0-9]+|Sub-CPMK [0-9]' mata-kuliah/<mk>/ --include=*.md

# Sitasi regulasi yang sudah dicabut (harus kosong)
grep -rn "Nomor 3 Tahun 2020" mata-kuliah/ --include=*.md

# Penyebutan SKS di luar RPS (harus kosong)
grep -rn "SKS" mata-kuliah/<mk>/03-modules/ mata-kuliah/<mk>/0*-buku-ajar/ --include=*.md

# Panjang RPS (pagu 550 baris)
wc -l mata-kuliah/<mk>/01-rps/*.md
```

## B. Checklist Telaah Manusia

### B.1 Mutu rumusan capaian

- [ ] Setiap Sub-CPMK diawali **kata kerja operasional** dari `taksonomi-cap.md` — bukan kata kerja kabur seperti "memahami" atau "mengetahui".
- [ ] Setiap Sub-CPMK **terukur**: dapat dibayangkan bentuk soal atau unjuk kerja yang membuktikannya.
- [ ] Level taksonomi **sesuai kata kerjanya** (mis. "Menganalisis" tidak ditandai C2).
- [ ] Ranah **A** dan **P** dipakai hanya bila alami — tidak dipaksakan pada capaian yang murni kognitif.
- [ ] Mata kuliah praktikum menonjolkan ranah **P**; Sub-CPMK praktikum yang seluruhnya beranah C adalah tanda rumusan belum tepat.

### B.2 Keselarasan konstruktif

- [ ] Bentuk asesmen **sepadan** dengan level taksonomi (C5–C6 tidak diuji dengan pilihan ganda).
- [ ] Materi pada modul/bab **benar-benar mengajarkan** Sub-CPMK yang ditandai, bukan sekadar menyebut kodenya.
- [ ] Bobot asesmen **proporsional** terhadap keluasan Sub-CPMK yang diukurnya.
- [ ] Tidak ada Sub-CPMK yang diajarkan tetapi tidak pernah diuji, maupun sebaliknya.

### B.3 Kebenaran substansi

- [ ] Sitasi regulasi berstatus ✅ atau 🟡 sesuai `pedoman-obe-konvensi.md` §B — **tidak ada nomor pasal yang ditulis untuk acuan berstatus 🟡**.
- [ ] Referensi buku dan standar merujuk edisi yang benar-benar ada (judul, edisi, penerbit, tahun cocok).
- [ ] Kode Python dapat dijalankan di Google Colab dengan versi Python yang dinyatakan.
- [ ] Nilai keislaman dan konteks Indonesia terintegrasi **secara alami**, bukan ditempelkan.

### B.4 Keramping-an dokumen

- [ ] RPS terbaca tuntas dalam satu duduk.
- [ ] Tidak ada detail di RPS yang seharusnya berada di `mutu/` atau `04-assessments/`.
- [ ] Tidak ada fakta yang ditulis di dua tempat (rumusan CPL, bobot, SKS, jadwal).

### B.5 Kesiapan akreditasi

- [ ] `mutu/01` §2 memetakan Profil Lulusan hingga CPMK tanpa mata rantai terputus.
- [ ] `mutu/02` §2 memungkinkan ketercapaian CPMK **benar-benar dihitung** — setiap butir soal bertanda Sub-CPMK.
- [ ] `mutu/03` §2 terisi jujur; tahap yang belum berjalan ditandai ⏳, bukan dikarang.
- [ ] Butir yang menunggu dokumen resmi ditandai 🔲, bukan disamarkan.

## C. Lembar Telaah Sejawat

| Peran | Nama | Tanggal | Tanda tangan |
|---|---|---|---|
| Penyusun | | | |
| Penelaah sejawat | | | |
| Ketua Program Studi | | | |

**Catatan penelaah:**

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
