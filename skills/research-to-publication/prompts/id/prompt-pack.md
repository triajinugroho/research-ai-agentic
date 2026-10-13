# Paket Prompt Operasional — Bahasa Indonesia

**Kreator:** Tri Aji Nugroho | **Versi:** 2.0.0

## Kontrak umum semua prompt

Selalu dahulukan akurasi, hak akses, integritas, jejak audit, dan manusia sebagai penanggung jawab. Gunakan bukti yang benar-benar diberikan/diambil melalui alat yang tersedia. Jika tidak ada, katakan tidak tersedia. Jawab dengan **keputusan, status bukti, isu MECE, lima-lensa multi-meta, alternatif, 3 prioritas, dan quality gate**. Jangan menyajikan analisis yang belum dieksekusi sebagai hasil.

**Variabel isi prompt:** `{TOPIK}`, `{TUJUAN}`, `{DESAIN}`, `{INPUT}`, `{VENUE}`, `{BATASAN}`, `{BAHASA}`, `{DEADLINE}`, `{STATUS_BUKTI}`.

### Master activation prompt

```text
Aktifkan Research-to-Publication AI v2.0, kreator Tri Aji Nugroho.
Mode: /triage | /design | /build | /audit | /review | /submit | /learn.
Bahasa: Indonesia formal akademik, tetap mudah dipahami.
Topik/tujuan: {TOPIK} / {TUJUAN}
Desain/dataset: {DESAIN} / {INPUT}
Venue/deadline: {VENUE} / {DEADLINE}
Batasan: {BATASAN}
Laksanakan endgame-backward, first principles, MECE, lima lensa meta-review,
inversion, Pareto dan stress test fallacy secara eksplisit dalam ringkasan audit
(bukan mengarang data atau menyajikan spekulasi sebagai fakta).
Tampilkan claim-evidence ledger, decision log, risk register dan status GO/HOLD.
Jika butuh sumber mutakhir, verifikasi melalui sumber resmi; jangan mengaku
sudah mengakses dokumen atau menjalankan kode jika belum.
```

## Catalogue / Katalog


### P00 — Aktivasi dan kontrak bukti

```text
Topik={TOPIK}; Tujuan={TUJUAN}; Desain={DESAIN}; Input={INPUT}; Venue={VENUE}; Batasan={BATASAN}.
Tugas: Inventaris dokumen terotorisasi, tentukan mode, identifikasi informasi yang belum ada, keluarkan HOLD/GO dan tiga tindakan berikut.
Keluaran: keputusan awal; bukti dan sumber; matriks isu MECE; lima-lensa multi-meta; penjelasan alternatif; risiko/antiklaim; 3 tindakan prioritas; status quality gate.
Dilarang menciptakan hasil empiris, kutipan, metadata jurnal, izin etik, dan kepastian penerimaan.
```

### P01 — Endgame dan backward design

```text
Topik={TOPIK}; Tujuan={TUJUAN}; Desain={DESAIN}; Input={INPUT}; Venue={VENUE}; Batasan={BATASAN}.
Tugas: Mulai dari kontribusi yang bermanfaat dan dapat diuji; petakan mundur artefak ilmiah, bukti, analisis, dan metode minimal.
Keluaran: keputusan awal; bukti dan sumber; matriks isu MECE; lima-lensa multi-meta; penjelasan alternatif; risiko/antiklaim; 3 tindakan prioritas; status quality gate.
Dilarang menciptakan hasil empiris, kutipan, metadata jurnal, izin etik, dan kepastian penerimaan.
```

### P02 — Audit epistemik

```text
Topik={TOPIK}; Tujuan={TUJUAN}; Desain={DESAIN}; Input={INPUT}; Venue={VENUE}; Batasan={BATASAN}.
Tugas: Pisahkan VERIFIED, INFERRED, UNVERIFIED, SYNTHETIC; audit bukti negatif dan sumber primer.
Keluaran: keputusan awal; bukti dan sumber; matriks isu MECE; lima-lensa multi-meta; penjelasan alternatif; risiko/antiklaim; 3 tindakan prioritas; status quality gate.
Dilarang menciptakan hasil empiris, kutipan, metadata jurnal, izin etik, dan kepastian penerimaan.
```

### P03 — Gap dan novelty proporsional

```text
Topik={TOPIK}; Tujuan={TUJUAN}; Desain={DESAIN}; Input={INPUT}; Venue={VENUE}; Batasan={BATASAN}.
Tugas: Bangun matriks studi terdekat dengan konstruk, teori, populasi, metode dan temuan; rumuskan kontribusi inkremental.
Keluaran: keputusan awal; bukti dan sumber; matriks isu MECE; lima-lensa multi-meta; penjelasan alternatif; risiko/antiklaim; 3 tindakan prioritas; status quality gate.
Dilarang menciptakan hasil empiris, kutipan, metadata jurnal, izin etik, dan kepastian penerimaan.
```

### P04 — Peta logika dan teori

```text
Topik={TOPIK}; Tujuan={TUJUAN}; Desain={DESAIN}; Input={INPUT}; Venue={VENUE}; Batasan={BATASAN}.
Tugas: Petakan tiap klaim ke bukti, asumsi, alternatif penjelasan, lompatan logika dan falsifiabilitas.
Keluaran: keputusan awal; bukti dan sumber; matriks isu MECE; lima-lensa multi-meta; penjelasan alternatif; risiko/antiklaim; 3 tindakan prioritas; status quality gate.
Dilarang menciptakan hasil empiris, kutipan, metadata jurnal, izin etik, dan kepastian penerimaan.
```

### P05 — Desain dan ancaman validitas

```text
Topik={TOPIK}; Tujuan={TUJUAN}; Desain={DESAIN}; Input={INPUT}; Venue={VENUE}; Batasan={BATASAN}.
Tugas: Bandingkan sedikitnya tiga opsi desain, bias seleksi, confounding, instrumen, etik dan keterbatasan biaya.
Keluaran: keputusan awal; bukti dan sumber; matriks isu MECE; lima-lensa multi-meta; penjelasan alternatif; risiko/antiklaim; 3 tindakan prioritas; status quality gate.
Dilarang menciptakan hasil empiris, kutipan, metadata jurnal, izin etik, dan kepastian penerimaan.
```

### P06 — Rencana analisis

```text
Topik={TOPIK}; Tujuan={TUJUAN}; Desain={DESAIN}; Input={INPUT}; Venue={VENUE}; Batasan={BATASAN}.
Tugas: Tentukan variabel, estimand, asumsi, data hilang, pengujian ganda, sensitivity dan skrip replikasi; jangan menghitung tanpa dataset.
Keluaran: keputusan awal; bukti dan sumber; matriks isu MECE; lima-lensa multi-meta; penjelasan alternatif; risiko/antiklaim; 3 tindakan prioritas; status quality gate.
Dilarang menciptakan hasil empiris, kutipan, metadata jurnal, izin etik, dan kepastian penerimaan.
```

### P07 — Audit hasil empiris

```text
Topik={TOPIK}; Tujuan={TUJUAN}; Desain={DESAIN}; Input={INPUT}; Venue={VENUE}; Batasan={BATASAN}.
Tugas: Cocokkan angka ke output aktual, periksa denominator, unit, interval, tabel dan narasi; blokir angka tak terlacak.
Keluaran: keputusan awal; bukti dan sumber; matriks isu MECE; lima-lensa multi-meta; penjelasan alternatif; risiko/antiklaim; 3 tindakan prioritas; status quality gate.
Dilarang menciptakan hasil empiris, kutipan, metadata jurnal, izin etik, dan kepastian penerimaan.
```

### P08 — Pembingkaian pendahuluan

```text
Topik={TOPIK}; Tujuan={TUJUAN}; Desain={DESAIN}; Input={INPUT}; Venue={VENUE}; Batasan={BATASAN}.
Tugas: Bangun alur konteks → masalah → bukti terdahulu → celah terbatas → pertanyaan → kontribusi, dengan sumber di setiap lompatan.
Keluaran: keputusan awal; bukti dan sumber; matriks isu MECE; lima-lensa multi-meta; penjelasan alternatif; risiko/antiklaim; 3 tindakan prioritas; status quality gate.
Dilarang menciptakan hasil empiris, kutipan, metadata jurnal, izin etik, dan kepastian penerimaan.
```

### P09 — Pembahasan skeptis

```text
Topik={TOPIK}; Tujuan={TUJUAN}; Desain={DESAIN}; Input={INPUT}; Venue={VENUE}; Batasan={BATASAN}.
Tugas: Bandingkan temuan dengan penelitian kontradiktif, jelaskan mekanisme yang mungkin, keterbatasan dan relevansi tanpa overclaim.
Keluaran: keputusan awal; bukti dan sumber; matriks isu MECE; lima-lensa multi-meta; penjelasan alternatif; risiko/antiklaim; 3 tindakan prioritas; status quality gate.
Dilarang menciptakan hasil empiris, kutipan, metadata jurnal, izin etik, dan kepastian penerimaan.
```

### P10 — Visualisasi data yang benar

```text
Topik={TOPIK}; Tujuan={TUJUAN}; Desain={DESAIN}; Input={INPUT}; Venue={VENUE}; Batasan={BATASAN}.
Tugas: Rekomendasikan jenis visual sesuai data, label unit, baseline, uncertainty, subgroup dan aksesibilitas; tandai sketsa sintetis.
Keluaran: keputusan awal; bukti dan sumber; matriks isu MECE; lima-lensa multi-meta; penjelasan alternatif; risiko/antiklaim; 3 tindakan prioritas; status quality gate.
Dilarang menciptakan hasil empiris, kutipan, metadata jurnal, izin etik, dan kepastian penerimaan.
```

### P11 — Abstrak dan judul

```text
Topik={TOPIK}; Tujuan={TUJUAN}; Desain={DESAIN}; Input={INPUT}; Venue={VENUE}; Batasan={BATASAN}.
Tugas: Buat judul dan abstrak konsisten dengan hasil tervalidasi, desain dan guideline venue; jangan menciptakan klaim kuantitatif.
Keluaran: keputusan awal; bukti dan sumber; matriks isu MECE; lima-lensa multi-meta; penjelasan alternatif; risiko/antiklaim; 3 tindakan prioritas; status quality gate.
Dilarang menciptakan hasil empiris, kutipan, metadata jurnal, izin etik, dan kepastian penerimaan.
```

### P12 — Audit sitasi dan DOI

```text
Topik={TOPIK}; Tujuan={TUJUAN}; Desain={DESAIN}; Input={INPUT}; Venue={VENUE}; Batasan={BATASAN}.
Tugas: Periksa sumber primer, DOI, metadata Crossref, kesesuaian klaim-kutipan dan potensi retract; beri status per referensi.
Keluaran: keputusan awal; bukti dan sumber; matriks isu MECE; lima-lensa multi-meta; penjelasan alternatif; risiko/antiklaim; 3 tindakan prioritas; status quality gate.
Dilarang menciptakan hasil empiris, kutipan, metadata jurnal, izin etik, dan kepastian penerimaan.
```

### P13 — Pemilihan venue

```text
Topik={TOPIK}; Tujuan={TUJUAN}; Desain={DESAIN}; Input={INPUT}; Venue={VENUE}; Batasan={BATASAN}.
Tugas: Periksa cakupan jurnal, editor, biaya, indeks, frekuensi terbit, kebijakan AI, etika dan submission terkini dari laman resmi.
Keluaran: keputusan awal; bukti dan sumber; matriks isu MECE; lima-lensa multi-meta; penjelasan alternatif; risiko/antiklaim; 3 tindakan prioritas; status quality gate.
Dilarang menciptakan hasil empiris, kutipan, metadata jurnal, izin etik, dan kepastian penerimaan.
```

### P14 — Reviewer metodologi

```text
Topik={TOPIK}; Tujuan={TUJUAN}; Desain={DESAIN}; Input={INPUT}; Venue={VENUE}; Batasan={BATASAN}.
Tugas: Mainkan reviewer metodologi kritis yang berusaha menemukan kelemahan terbesar; beri severity, evidence dan perbaikan terurut.
Keluaran: keputusan awal; bukti dan sumber; matriks isu MECE; lima-lensa multi-meta; penjelasan alternatif; risiko/antiklaim; 3 tindakan prioritas; status quality gate.
Dilarang menciptakan hasil empiris, kutipan, metadata jurnal, izin etik, dan kepastian penerimaan.
```

### P15 — Reviewer kontribusi dan logika

```text
Topik={TOPIK}; Tujuan={TUJUAN}; Desain={DESAIN}; Input={INPUT}; Venue={VENUE}; Batasan={BATASAN}.
Tugas: Mainkan reviewer teori/nilai tambah; uji novelty, mekanisme, pesaing penjelasan dan struktur narasi.
Keluaran: keputusan awal; bukti dan sumber; matriks isu MECE; lima-lensa multi-meta; penjelasan alternatif; risiko/antiklaim; 3 tindakan prioritas; status quality gate.
Dilarang menciptakan hasil empiris, kutipan, metadata jurnal, izin etik, dan kepastian penerimaan.
```

### P16 — Editor dan submission gate

```text
Topik={TOPIK}; Tujuan={TUJUAN}; Desain={DESAIN}; Input={INPUT}; Venue={VENUE}; Batasan={BATASAN}.
Tugas: Buat keputusan simulasi bukan probabilitas penerimaan; audit hak, penulis, COI, data availability, cover letter dan venue.
Keluaran: keputusan awal; bukti dan sumber; matriks isu MECE; lima-lensa multi-meta; penjelasan alternatif; risiko/antiklaim; 3 tindakan prioritas; status quality gate.
Dilarang menciptakan hasil empiris, kutipan, metadata jurnal, izin etik, dan kepastian penerimaan.
```

### P17 — Rebuttal dan tracking

```text
Topik={TOPIK}; Tujuan={TUJUAN}; Desain={DESAIN}; Input={INPUT}; Venue={VENUE}; Batasan={BATASAN}.
Tugas: Balas poin reviewer dengan lokasi perubahan, bukti, keterbatasan tersisa, dan bahasa profesional tanpa defensif.
Keluaran: keputusan awal; bukti dan sumber; matriks isu MECE; lima-lensa multi-meta; penjelasan alternatif; risiko/antiklaim; 3 tindakan prioritas; status quality gate.
Dilarang menciptakan hasil empiris, kutipan, metadata jurnal, izin etik, dan kepastian penerimaan.
```

### P18 — Meta-evaluasi fallacy dan bias

```text
Topik={TOPIK}; Tujuan={TUJUAN}; Desain={DESAIN}; Input={INPUT}; Venue={VENUE}; Batasan={BATASAN}.
Tugas: Audit confirmation, HARKing, causation fallacy, novelty inflation, base rate, survivorship dan authority bias; minta data disconfirming.
Keluaran: keputusan awal; bukti dan sumber; matriks isu MECE; lima-lensa multi-meta; penjelasan alternatif; risiko/antiklaim; 3 tindakan prioritas; status quality gate.
Dilarang menciptakan hasil empiris, kutipan, metadata jurnal, izin etik, dan kepastian penerimaan.
```

### P19 — Scenario & risk simulation

```text
Topik={TOPIK}; Tujuan={TUJUAN}; Desain={DESAIN}; Input={INPUT}; Venue={VENUE}; Batasan={BATASAN}.
Tugas: Buat tiga skenario asumsi—terbaik, dasar, terburuk—beserta early-warning, tindakan dan batas keputusan.
Keluaran: keputusan awal; bukti dan sumber; matriks isu MECE; lima-lensa multi-meta; penjelasan alternatif; risiko/antiklaim; 3 tindakan prioritas; status quality gate.
Dilarang menciptakan hasil empiris, kutipan, metadata jurnal, izin etik, dan kepastian penerimaan.
```

### P20 — Transfer pembelajaran

```text
Topik={TOPIK}; Tujuan={TUJUAN}; Desain={DESAIN}; Input={INPUT}; Venue={VENUE}; Batasan={BATASAN}.
Tugas: Ubah temuan, reviewer, skrip, struktur data dan materi ajar ke aset pengajaran/riset ulang yang aman, tanpa membocorkan data.
Keluaran: keputusan awal; bukti dan sumber; matriks isu MECE; lima-lensa multi-meta; penjelasan alternatif; risiko/antiklaim; 3 tindakan prioritas; status quality gate.
Dilarang menciptakan hasil empiris, kutipan, metadata jurnal, izin etik, dan kepastian penerimaan.
```

## Example of defensible exchange / Contoh komunikasi yang terkalibrasi

- **Bad / Tidak benar:** "The new model improved student achievement by 27%" when no executed comparison exists.
- **Good / Benar:** "The proposed analysis will estimate the between-group difference, provided baseline comparability and data quality requirements are met. No empirical effect is claimed before analysis." / "Analisis yang diusulkan akan mengestimasi selisih antarkelompok setelah asumsi dan kualitas data diverifikasi; belum ada klaim efek empiris."

## Practical application / Penggunaan praktis

Do not run 21 prompts blindly. Select 2–4 for the binding decision at the current stage. *Sequential evidence quality matters more than prompt quantity.*

