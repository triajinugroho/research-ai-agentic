# Minggu 12: Software Maintenance dan Evolution

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak |
| **Kode** | IF2205 |
| **Minggu** | 12 dari 16 |
| **Topik** | Software Maintenance dan Evolution |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **Bahasa Pemrograman** | Python 3.x + JavaScript |
| **CPMK** | CPMK-6: Menerapkan DevOps, CI/CD, containerization (Docker), cloud deployment, dan software maintenance |
| **Sub-CPMK** | 12.1 Menganalisis jenis-jenis software maintenance dan dampaknya pada lifecycle (C4) |
| | 12.2 Mengevaluasi technical debt dan strategi pengelolaannya (C5) |
| | 12.3 Menerapkan refactoring dan software metrics untuk meningkatkan kualitas kode (C4) |
| **Durasi** | 150 menit (3 × 50 menit) |
| **Metode** | Ceramah interaktif, code analysis exercise, refactoring workshop |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Menganalisis** empat jenis software maintenance dan proporsi biayanya dalam lifecycle (C4)
2. **Mengevaluasi** technical debt dalam codebase dan memprioritaskan penanganannya (C5)
3. **Menerapkan** teknik refactoring: Extract Method, Rename, Replace Magic Number, dll. (C4)
4. **Menganalisis** software metrics: cyclomatic complexity, coupling, cohesion (C4)
5. **Menerapkan** Semantic Versioning (SemVer) dan dependency management (C4)

---

## Materi Pembelajaran

### 12.1 Jenis-Jenis Software Maintenance

Maintenance menghabiskan **60-80% total biaya** lifecycle perangkat lunak — jauh lebih besar dari development awal.

| Jenis | Deskripsi | Proporsi | Contoh |
|-------|-----------|----------|--------|
| **Corrective** | Perbaikan bug/defect | ~20% | Fix crash saat login |
| **Adaptive** | Adaptasi ke lingkungan baru | ~25% | Migrasi dari Python 3.9 ke 3.12 |
| **Perfective** | Penambahan/peningkatan fitur | ~50% | Tambah fitur ekspor PDF |
| **Preventive** | Cegah masalah di masa depan | ~5% | Refactoring, update dependencies |

```
Distribusi Biaya Software Lifecycle
┌────────────────┬──────────────────────────────────────────────┐
│  Development   │                 Maintenance                   │
│     20-40%     │                   60-80%                      │
│                │ Corrective│ Adaptive │ Perfective │Preventive │
└────────────────┴──────────────────────────────────────────────┘
```

> **Lehman's Laws of Software Evolution:** Perangkat lunak yang digunakan di dunia nyata *harus* terus berevolusi, atau akan menjadi semakin tidak memuaskan (*law of continuing change*).

### 12.2 Technical Debt (Utang Teknis)

Technical debt adalah "jalan pintas" dalam kode yang mempercepat delivery jangka pendek tetapi menambah biaya jangka panjang.

```
Technical Debt Quadrant (Martin Fowler):
┌─────────────────────┬──────────────────────┐
│   Reckless &        │   Prudent &          │
│   Deliberate        │   Deliberate         │
│ "Kita tidak punya   │ "Kita harus deliver  │
│  waktu untuk        │  sekarang, refactor  │
│  design"            │  nanti"              │
├─────────────────────┼──────────────────────┤
│   Reckless &        │   Prudent &          │
│   Inadvertent       │   Inadvertent        │
│ "Apa itu design     │ "Sekarang kita tahu  │
│  patterns?"         │  seharusnya begini"  │
└─────────────────────┴──────────────────────┘
```

#### Gejala Technical Debt

- **Code smells**: Long method, large class, duplicate code, magic numbers
- **Outdated dependencies**: Library dengan known vulnerabilities
- **Missing tests**: Bagian kode tanpa test coverage
- **Poor documentation**: Kode tanpa komentar atau dokumentasi usang
- **Tight coupling**: Perubahan satu modul memaksa perubahan banyak modul lain

#### Strategi Mengelola Technical Debt

1. **Boy Scout Rule**: "Tinggalkan kode lebih bersih dari saat kamu temukan"
2. **Refactoring sprints**: Alokasikan 20% sprint capacity untuk mengurangi debt
3. **Debt backlog**: Dokumentasikan dan prioritaskan technical debt seperti backlog fitur
4. **Automated tools**: SonarQube, ESLint, Pylint untuk deteksi otomatis

### 12.3 Refactoring — Mengubah Struktur Tanpa Mengubah Perilaku

Refactoring adalah proses memperbaiki desain internal kode **tanpa mengubah perilaku eksternalnya**.

#### Teknik Refactoring Umum

**1. Extract Method** — Pecah fungsi besar menjadi fungsi-fungsi kecil:

```python
# SEBELUM: Fungsi terlalu panjang
def proses_pesanan(pesanan):
    # Validasi (10 baris)
    if not pesanan.items:
        raise ValueError("Pesanan kosong")
    for item in pesanan.items:
        if item.stok <= 0:
            raise ValueError(f"{item.nama} habis")

    # Hitung total (8 baris)
    subtotal = sum(i.harga * i.qty for i in pesanan.items)
    pajak = subtotal * 0.11  # PPN 11%
    total = subtotal + pajak

    # Kirim notifikasi (5 baris)
    kirim_email(pesanan.email, f"Total: Rp {total:,.0f}")
    return total

# SESUDAH: Extract Method
def proses_pesanan(pesanan):
    validasi_pesanan(pesanan)
    total = hitung_total(pesanan)
    kirim_notifikasi(pesanan, total)
    return total

def validasi_pesanan(pesanan):
    if not pesanan.items:
        raise ValueError("Pesanan kosong")
    for item in pesanan.items:
        if item.stok <= 0:
            raise ValueError(f"{item.nama} habis")

def hitung_total(pesanan):
    subtotal = sum(i.harga * i.qty for i in pesanan.items)
    pajak = subtotal * 0.11
    return subtotal + pajak

def kirim_notifikasi(pesanan, total):
    kirim_email(pesanan.email, f"Total: Rp {total:,.0f}")
```

**2. Replace Magic Number with Named Constant:**

```python
# SEBELUM
pajak = subtotal * 0.11

# SESUDAH
TARIF_PPN = 0.11  # PPN Indonesia per 2025
pajak = subtotal * TARIF_PPN
```

**3. Rename for Clarity:**

```python
# SEBELUM
def proc(d, t):
    return d * (1 - t)

# SESUDAH
def hitung_harga_setelah_diskon(harga: float, persen_diskon: float) -> float:
    return harga * (1 - persen_diskon)
```

### 12.4 Software Metrics

| Metrik | Deskripsi | Target | Tool |
|--------|-----------|--------|------|
| **Cyclomatic Complexity** | Jumlah jalur independen dalam fungsi | ≤ 10 per fungsi | radon (Python) |
| **Coupling** | Ketergantungan antar modul | Rendah (loose) | SonarQube |
| **Cohesion** | Keterkaitan internal dalam modul | Tinggi | SonarQube |
| **Lines of Code (LOC)** | Ukuran kode | — | cloc |
| **Code Churn** | Frekuensi perubahan kode | — | git log analysis |

```python
# Cyclomatic Complexity = Jumlah keputusan + 1
def kategorisasi_nilai(skor):   # CC = 5
    if skor >= 85:              # +1
        return 'A'
    elif skor >= 70:            # +1
        return 'B'
    elif skor >= 55:            # +1
        return 'C'
    elif skor >= 40:            # +1
        return 'D'
    else:
        return 'E'
```

```bash
# Mengukur cyclomatic complexity dengan radon
pip install radon
radon cc src/ -a -s  # -a: average, -s: show score
```

### 12.5 Semantic Versioning (SemVer)

SemVer menggunakan format **MAJOR.MINOR.PATCH** untuk mengkomunikasikan jenis perubahan:

```
Versi: 2.4.1
        │ │ │
        │ │ └── PATCH: Bug fix, backward-compatible
        │ └──── MINOR: Fitur baru, backward-compatible
        └────── MAJOR: Breaking change, TIDAK backward-compatible

Contoh riwayat versi:
1.0.0 → 1.0.1 (fix typo) → 1.1.0 (tambah fitur ekspor)
      → 1.2.0 (tambah fitur filter) → 2.0.0 (ubah API format)
```

#### Dependency Management

```json
// package.json — Pinning dependencies
{
  "dependencies": {
    "express": "^4.18.2",    // ^: minor updates OK (4.x.x)
    "lodash": "~4.17.21",   // ~: patch updates only (4.17.x)
    "react": "18.2.0"       // Exact: hanya versi ini
  }
}
```

> **Nilai Islami — Istiqamah (Konsistensi):** Software maintenance membutuhkan istiqamah — komitmen untuk terus memperbaiki dan menjaga kualitas, bukan hanya saat awal pengembangan. Sebagaimana ibadah yang terbaik adalah yang dilakukan secara konsisten, perawatan kode yang terbaik juga dilakukan secara rutin.

---

## Kegiatan Pembelajaran

### Pre-class (15 menit)

- Membaca: Martin Fowler, "Refactoring: Improving the Design of Existing Code" — Chapter 1 (free online summary)
- Install radon: `pip install radon`
- Jalankan `radon cc` pada salah satu file proyek kelompok

### In-class (120 menit)

| Waktu | Aktivitas | Metode |
|-------|-----------|--------|
| 0-20 menit | Jenis maintenance, Lehman's Laws, lifecycle cost | Ceramah + diskusi |
| 20-40 menit | Technical debt: quadrant, gejala, strategi | Ceramah + contoh |
| 40-60 menit | Code analysis exercise: identifikasi code smells di contoh kode | Exercise kelompok |
| 60-65 menit | *Break* | — |
| 65-95 menit | Refactoring workshop: perbaiki kode bermasalah step-by-step | Hands-on coding |
| 95-110 menit | Software metrics, SemVer, dependency management | Ceramah + demo |
| 110-120 menit | **Kuis K3** (materi Minggu 9-12, 15 menit) + wrap-up | Kuis + diskusi |

### Post-class (15 menit)

- Analisis cyclomatic complexity proyek kelompok, identifikasi fungsi yang perlu di-refactor
- Review dependencies proyek: adakah yang outdated atau vulnerable?
- Lanjutkan pengerjaan proyek akhir

---

## Referensi

1. Pressman, R. S. & Maxim, B. R. (2020). *Software Engineering*, 9th ed. Chapter 28-29.
2. Sommerville, I. (2016). *Software Engineering*, 10th ed. Chapter 9.
3. Fowler, M. (2019). *Refactoring: Improving the Design of Existing Code*, 2nd ed. Addison-Wesley.
4. Cunningham, W. (1992). "The WyCash Portfolio Management System" — origin of technical debt metaphor.
5. Semantic Versioning 2.0.0. [semver.org](https://semver.org/)
6. radon documentation. [radon.readthedocs.io](https://radon.readthedocs.io/)

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
