# BAB 11: SOFTWARE MAINTENANCE DAN EVOLUTION

**Oleh: Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi | Level Bloom |
|-----------|-----------|-------------|
| 6.3 | Menganalisis jenis maintenance dan strategi pengelolaan technical debt | C4 (Menganalisis) |
| 6.4 | Menerapkan software metrics, SemVer, dan change management | C3-C4 |

---

## 11.1 Software Maintenance

### 11.1.1 Fakta tentang Maintenance

- **60-80%** total biaya software dihabiskan untuk maintenance (bukan development)
- Maintenance dimulai segera setelah software di-deploy
- Mayoritas waktu engineer dihabiskan membaca kode, bukan menulis

### 11.1.2 Jenis Maintenance

| Jenis | Tujuan | Contoh | Persentase |
|-------|--------|--------|------------|
| **Corrective** | Perbaiki bug | Fix crash saat pencarian kosong | 20% |
| **Adaptive** | Adaptasi ke lingkungan baru | Update untuk Python 3.12 | 25% |
| **Perfective** | Tingkatkan performa/fitur | Optimasi query lambat | 50% |
| **Preventive** | Cegah masalah masa depan | Refactoring, update dependencies | 5% |

## 11.2 Technical Debt

### 11.2.1 Apa Itu Technical Debt?

> Technical debt adalah "hutang" yang terjadi ketika kita mengambil shortcut dalam development — bekerja sekarang, tapi harus "dibayar" nanti.

```
                  Kecepatan Development
                  ▲
                  │    /--- Tanpa debt (investasi di kualitas)
                  │   /
                  │  /
                  │ / _____ Dengan debt (cepat awal, lambat nanti)
                  │/
                  └──────────────────────▶ Waktu
```

### 11.2.2 Jenis Technical Debt

| Jenis | Sengaja? | Contoh |
|-------|----------|--------|
| **Deliberate** | Ya | "Kita hardcode dulu, refactor nanti" |
| **Inadvertent** | Tidak | Tidak tahu ada design pattern yang lebih baik |
| **Bit rot** | Alamiah | Dependencies outdated seiring waktu |

### 11.2.3 Mengelola Technical Debt

1. **Identifikasi** — code smells, complexity metrics, outdated dependencies
2. **Visualisasi** — backlog technical debt items di board
3. **Prioritisasi** — selesaikan debt yang paling berdampak
4. **Alokasi waktu** — dedikasikan 10-20% sprint untuk debt reduction
5. **Cegah** — code review, standards, automated quality gates

## 11.3 Software Metrics

| Metrik | Deskripsi | Tool | Target |
|--------|-----------|------|--------|
| **Cyclomatic Complexity** | Jumlah path independen dalam fungsi | radon | ≤ 10 per fungsi |
| **Lines of Code (LOC)** | Ukuran kode | cloc | Konteks-dependent |
| **Code Coverage** | % kode yang di-test | pytest-cov | ≥ 80% |
| **Coupling** | Ketergantungan antar modul | pylint | Rendah |
| **Cohesion** | Seberapa fokus satu modul | Manual review | Tinggi |
| **Defect Density** | Bug per KLOC | Issue tracker | < 5 |

```bash
# Mengukur cyclomatic complexity dengan radon
pip install radon
radon cc app/ -a -s
# Hasil: A (1-5 simple), B (6-10 moderate), C (11-15 complex)
```

## 11.4 Semantic Versioning (SemVer)

Format: **MAJOR.MINOR.PATCH**

| Komponen | Kapan Increment | Contoh |
|----------|----------------|--------|
| **MAJOR** | Breaking changes (API berubah) | 1.0.0 → 2.0.0 |
| **MINOR** | Fitur baru, backward compatible | 1.0.0 → 1.1.0 |
| **PATCH** | Bug fix, backward compatible | 1.0.0 → 1.0.1 |

```
v1.0.0  → v1.0.1 (fix typo di UI)
        → v1.1.0 (tambah fitur dark mode)
        → v2.0.0 (redesign API, breaking change)
```

**Pre-release:** `v1.0.0-alpha.1`, `v1.0.0-beta.1`, `v1.0.0-rc.1`

## 11.5 Change Management

### 11.5.1 Change Request Process

```
Request → Impact Analysis → Approval → Implementation → Verification → Release
```

### 11.5.2 Release Management

```
develop ── feature complete ── code freeze ── RC testing ── release ── tag
```

**Release checklist:**
- [ ] Semua tests pass (unit, integration, E2E)
- [ ] Code review completed
- [ ] Security scan clean
- [ ] Documentation updated
- [ ] Changelog written
- [ ] Version bumped (SemVer)
- [ ] Deployment tested di staging
- [ ] Stakeholder sign-off

## 11.6 Legacy System Modernization

Strategi untuk menangani sistem lama:

| Strategi | Deskripsi | Risiko | Cocok Untuk |
|----------|-----------|--------|-------------|
| **Rewrite** | Tulis ulang dari nol | Tinggi (second system effect) | Sistem kecil |
| **Refactor** | Perbaiki bertahap | Rendah | Sistem medium |
| **Strangler Fig** | Ganti modul per modul | Sedang | Sistem besar |
| **Wrap** | Bungkus dengan API baru | Rendah | Integrasi |

---

## AI Corner: AI untuk Maintenance (Level: Advanced)

| Aktivitas | Prompt Contoh | Catatan |
|-----------|---------------|---------|
| Technical debt | "Analisis kode ini dan identifikasi technical debt: [paste]" | AI bisa mendeteksi code smells dan outdated patterns |
| Legacy analysis | "Jelaskan kode legacy ini dan sarankan strategi modernisasi" | Berguna untuk memahami kode lama |
| Changelog | "Buatkan changelog dari git log commits berikut: [paste]" | Review untuk akurasi |

---

## Latihan Soal

### Level Dasar (C1-C2)
1. Sebutkan 4 jenis software maintenance dan persentase masing-masing.
2. Apa itu technical debt? Berikan 3 contoh.
3. Jelaskan format Semantic Versioning.

### Level Menengah (C3-C4)
4. Analisis sebuah Flask project dan ukur cyclomatic complexity menggunakan radon.
5. Buatlah release checklist untuk Sistem Perpustakaan versi 1.0.0.
6. Identifikasi 5 sumber technical debt dalam proyek tim Anda dan buat rencana pelunasan.

### Level Mahir (C5-C6)
7. Evaluasi: strangler fig pattern vs rewrite — kapan masing-masing strategi cocok?
8. Rancang maintenance plan untuk Sistem Antrian Puskesmas — cover semua 4 jenis maintenance untuk 1 tahun ke depan.

---

## Rangkuman

1. **Software maintenance** menghabiskan 60-80% total biaya — corrective, adaptive, perfective, preventive.
2. **Technical debt** adalah shortcut yang harus "dibayar" nanti — kelola dengan identifikasi, prioritisasi, dan alokasi waktu.
3. **Software metrics** (cyclomatic complexity, coverage, coupling) membantu mengukur kualitas secara objektif.
4. **Semantic Versioning** (MAJOR.MINOR.PATCH) memberikan komunikasi jelas tentang nature perubahan.
5. **Change management** memastikan perubahan terkelola dengan impact analysis dan release checklist.
6. **Legacy modernization** bisa dilakukan gradual (strangler fig, refactor) atau radikal (rewrite).

---

## Referensi

1. Lehman, M. M. (1980). "Programs, Life Cycles, and Laws of Software Evolution." *IEEE Proceedings*.
2. Cunningham, W. (1992). "The WyCash Portfolio Management System." *OOPSLA Experience Report*.
3. Newman, S. (2019). *Monolith to Microservices*. O'Reilly.
4. Sommerville, I. (2016). *Software Engineering* (10th ed.). Chapter 9. Pearson.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
