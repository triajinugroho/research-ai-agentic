# Minggu 9: Software Testing dan Quality Assurance

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak |
| **Kode** | IF2205 |
| **Minggu** | 9 dari 16 |
| **Topik** | Software Testing dan Quality Assurance |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **Bahasa Pemrograman** | Python 3.x + JavaScript |
| **CPMK** | CPMK-5: Merancang strategi pengujian komprehensif (unit, integration, E2E) serta menerapkan TDD dan AI-assisted testing |
| **Sub-CPMK** | 9.1 Menganalisis level testing dan perannya dalam SDLC (C4) |
| | 9.2 Mengevaluasi teknik desain test case untuk menemukan defect secara efektif (C5) |
| | 9.3 Menerapkan siklus TDD (Red-Green-Refactor) dengan pytest dan Jest (C4) |
| **Durasi** | 150 menit (3 × 50 menit) |
| **Metode** | Ceramah interaktif, live coding TDD, hands-on test writing |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Menganalisis** berbagai level testing (unit, integration, system, acceptance) dan kapan masing-masing diterapkan (C4)
2. **Mengevaluasi** teknik desain test case: equivalence partitioning, boundary value analysis, dan decision table (C5)
3. **Menerapkan** siklus TDD (Red-Green-Refactor) pada fungsi Python menggunakan pytest (C4)
4. **Menerapkan** unit test pada fungsi JavaScript menggunakan Jest (C4)
5. **Membedakan** peran Quality Assurance (QA) dan Quality Control (QC) dalam proyek perangkat lunak (C4)

---

## Materi Pembelajaran

### 9.1 Mengapa Testing Penting?

> *"Program testing can be used to show the presence of bugs, but never to show their absence."* — Edsger W. Dijkstra

Biaya perbaikan *bug* meningkat secara eksponensial seiring tahapan SDLC:

```
Biaya Relatif Perbaikan Bug
┌──────────────────────────────────────────┐
│ Requirements   │ █          1x            │
│ Design         │ ███        3-6x          │
│ Construction   │ ██████     10x           │
│ Testing        │ ████████████  15-40x     │
│ Production     │ ██████████████████ 30-100x│
└──────────────────────────────────────────┘
```

**Contoh nyata Indonesia:** Kegagalan sistem registrasi online CPNS 2023 yang overload di hari pertama — pengujian beban (*load testing*) yang memadai bisa mencegahnya.

### 9.2 Level Testing (Testing Levels)

| Level | Scope | Siapa | Contoh |
|-------|-------|-------|--------|
| **Unit Testing** | Satu fungsi/method | Developer | Test fungsi `hitung_diskon()` |
| **Integration Testing** | Interaksi antar modul | Developer/QA | Test API endpoint + database |
| **System Testing** | Seluruh sistem | QA Team | Test aplikasi e-commerce end-to-end |
| **Acceptance Testing** | Kebutuhan bisnis | Client/User | UAT: "Apakah fitur checkout sesuai?" |

```
┌──────────────────────────────────────────────┐
│           Acceptance Testing                  │
│   ┌──────────────────────────────────────┐   │
│   │         System Testing                │   │
│   │   ┌──────────────────────────────┐   │   │
│   │   │     Integration Testing       │   │   │
│   │   │   ┌──────────────────────┐   │   │   │
│   │   │   │    Unit Testing       │   │   │   │
│   │   │   └──────────────────────┘   │   │   │
│   │   └──────────────────────────────┘   │   │
│   └──────────────────────────────────────┘   │
└──────────────────────────────────────────────┘
  "Testing Pyramid" — semakin bawah, semakin banyak & cepat
```

### 9.3 Teknik Desain Test Case

#### Equivalence Partitioning

Membagi domain input menjadi kelas-kelas yang setara (*equivalence classes*):

```python
# Fungsi: diskon berdasarkan usia
# Anak (0-12): 50%, Dewasa (13-59): 0%, Lansia (60+): 30%
# Equivalence classes:
#   Invalid: usia < 0
#   Valid: [0-12], [13-59], [60+]
# Test cases minimal: -1, 5, 30, 70
```

#### Boundary Value Analysis (BVA)

Fokus pada batas-batas kelas: `{-1, 0, 1, 12, 13, 59, 60, 61}`

#### Decision Table

| Aturan | Member? | Total > 500rb | Diskon |
|--------|---------|---------------|--------|
| 1 | Ya | Ya | 20% |
| 2 | Ya | Tidak | 10% |
| 3 | Tidak | Ya | 5% |
| 4 | Tidak | Tidak | 0% |

### 9.4 Test-Driven Development (TDD)

TDD adalah pendekatan di mana **test ditulis sebelum kode produksi**:

```
┌─────────┐     ┌─────────┐     ┌──────────┐
│  RED     │────▶│  GREEN  │────▶│ REFACTOR │
│ (Tulis  │     │ (Tulis  │     │ (Bersih- │
│  test,  │     │  kode   │     │  kan     │
│  gagal) │     │  minimal│     │  kode)   │
└─────────┘     │  agar   │     └────┬─────┘
     ▲          │  lulus) │          │
     │          └─────────┘          │
     └───────────────────────────────┘
```

#### Contoh TDD dengan pytest (Python)

**RED** — Tulis test yang gagal:

```python
# test_diskon.py
def test_diskon_anak():
    assert hitung_diskon(harga=100000, usia=10) == 50000

def test_diskon_lansia():
    assert hitung_diskon(harga=100000, usia=65) == 70000

def test_diskon_dewasa():
    assert hitung_diskon(harga=100000, usia=30) == 100000

def test_usia_negatif():
    import pytest
    with pytest.raises(ValueError):
        hitung_diskon(harga=100000, usia=-1)
```

**GREEN** — Implementasi minimal:

```python
# diskon.py
def hitung_diskon(harga: int, usia: int) -> int:
    """Menghitung harga setelah diskon berdasarkan usia."""
    if usia < 0:
        raise ValueError("Usia tidak boleh negatif")
    if usia <= 12:
        return int(harga * 0.5)
    elif usia >= 60:
        return int(harga * 0.7)
    return harga
```

**REFACTOR** — Perbaiki tanpa mengubah perilaku (extract constants, tambah docstring, dll.)

#### Contoh TDD dengan Jest (JavaScript)

```javascript
// diskon.test.js
const { hitungDiskon } = require('./diskon');

describe('hitungDiskon', () => {
  test('anak mendapat diskon 50%', () => {
    expect(hitungDiskon(100000, 10)).toBe(50000);
  });

  test('lansia mendapat diskon 30%', () => {
    expect(hitungDiskon(100000, 65)).toBe(70000);
  });

  test('usia negatif throw error', () => {
    expect(() => hitungDiskon(100000, -1)).toThrow('Usia tidak boleh negatif');
  });
});
```

```javascript
// diskon.js
function hitungDiskon(harga, usia) {
  if (usia < 0) throw new Error('Usia tidak boleh negatif');
  if (usia <= 12) return Math.floor(harga * 0.5);
  if (usia >= 60) return Math.floor(harga * 0.7);
  return harga;
}
module.exports = { hitungDiskon };
```

### 9.5 Quality Assurance vs Quality Control

| Aspek | Quality Assurance (QA) | Quality Control (QC) |
|-------|----------------------|---------------------|
| **Fokus** | Proses | Produk |
| **Kapan** | Sepanjang SDLC | Setelah produk dibuat |
| **Tujuan** | Mencegah defect | Menemukan defect |
| **Contoh** | Code review, standar coding | Unit test, bug report |
| **Sifat** | Proaktif | Reaktif |

> **Nilai Islami — Itqan (Kesempurnaan):** Rasulullah SAW bersabda, *"Sesungguhnya Allah mencintai jika seseorang melakukan pekerjaan, ia melakukannya dengan itqan (sempurna)."* (HR. Al-Baihaqi). Testing adalah bentuk *itqan* dalam pengembangan perangkat lunak.

---

## Kegiatan Pembelajaran

### Pre-class (15 menit)

- Membaca artikel: *"The Practical Test Pyramid"* oleh Martin Fowler
- Menginstal pytest (`pip install pytest`) dan Jest (`npm install --save-dev jest`) di environment masing-masing
- Menjawab pertanyaan refleksi: "Pernahkah kamu menemukan bug di aplikasi yang kamu gunakan sehari-hari? Bagaimana dampaknya?"

### In-class (120 menit)

| Waktu | Aktivitas | Metode |
|-------|-----------|--------|
| 0-20 menit | Konsep testing levels dan testing pyramid | Ceramah + diskusi |
| 20-40 menit | Teknik desain test case (EP, BVA, Decision Table) | Ceramah + latihan |
| 40-50 menit | Demo TDD Red-Green-Refactor (live coding) | Live coding |
| 50-55 menit | *Break* | — |
| 55-90 menit | Hands-on: TDD dengan pytest — implementasi fungsi validasi NIM | Hands-on coding |
| 90-110 menit | Hands-on: TDD dengan Jest — implementasi fungsi format rupiah | Hands-on coding |
| 110-120 menit | QA vs QC, diskusi, dan wrap-up | Diskusi kelas |

### Post-class (15 menit)

- Review catatan dan konsep TDD
- Mempersiapkan tugas T4 (Test Plan & Unit Test Suite)
- Eksplorasi: coba jalankan `pytest --cov` untuk melihat code coverage

---

## Penugasan

### T4 — Test Plan & Unit Test Suite

| Komponen | Detail |
|----------|--------|
| **Tipe** | Individual |
| **Deadline** | Minggu 11 |
| **Deliverable** | 1) Dokumen Test Plan (markdown), 2) Unit test suite (pytest + Jest) |

**Instruksi:**
1. Pilih satu modul dari proyek kelompok
2. Buat **Test Plan** yang mencakup: scope, strategi testing, test cases (min. 10), dan kriteria pass/fail
3. Implementasikan **unit test** menggunakan pytest (backend) dan Jest (frontend) — minimal 8 test cases
4. Terapkan pendekatan TDD: commit history harus menunjukkan siklus Red-Green-Refactor
5. Sertakan screenshot hasil test dan code coverage

---

## Referensi

1. Pressman, R. S. & Maxim, B. R. (2020). *Software Engineering: A Practitioner's Approach*, 9th ed. McGraw-Hill. Chapter 22-23.
2. Sommerville, I. (2016). *Software Engineering*, 10th ed. Pearson. Chapter 8.
3. Fowler, M. (2018). "The Practical Test Pyramid." [martinfowler.com](https://martinfowler.com/articles/practical-test-pyramid.html)
4. Beck, K. (2003). *Test-Driven Development: By Example*. Addison-Wesley.
5. pytest documentation. [docs.pytest.org](https://docs.pytest.org/)
6. Jest documentation. [jestjs.io](https://jestjs.io/)

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
