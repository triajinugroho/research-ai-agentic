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
| **CPMK** | CPMK-5: Merancang dan melaksanakan strategi pengujian perangkat lunak yang komprehensif (unit, integration, E2E) serta menerapkan quality assurance practices termasuk TDD dan AI-assisted testing |
| **Sub-CPMK** | Sub-CPMK-5.1: Merancang test cases menggunakan teknik equivalence partitioning dan boundary value analysis (C4) |
| | Sub-CPMK-5.2: Mengimplementasikan unit test dan integration test menggunakan pytest (Python) dan Jest (JavaScript) (C3) |
| **Durasi** | 150 menit (3 x 50 menit) |
| **Metode** | Ceramah interaktif, live coding TDD, hands-on test writing |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Menganalisis** berbagai level testing (unit, integration, system, acceptance) dan kapan masing-masing diterapkan dalam SDLC (C4)
2. **Merancang** test cases menggunakan teknik equivalence partitioning, boundary value analysis, dan decision table (C4)
3. **Menerapkan** siklus TDD (Red-Green-Refactor) pada fungsi Python menggunakan pytest (C3)
4. **Mengimplementasikan** unit test pada fungsi JavaScript menggunakan Jest dengan pola AAA (C3)
5. **Membedakan** peran Quality Assurance (QA) dan Quality Control (QC) dalam proyek perangkat lunak (C4)
6. **Mengevaluasi** efektivitas test suite berdasarkan kecukupan test case dan code coverage (C5)

---

## Materi Pembelajaran

### 9.1 Mengapa Testing Penting?

> *"Program testing can be used to show the presence of bugs, but never to show their absence."* — Edsger W. Dijkstra

Biaya perbaikan *bug* meningkat secara eksponensial seiring tahapan SDLC. Semakin terlambat bug ditemukan, semakin mahal untuk memperbaikinya:

```
Biaya Relatif Perbaikan Bug per Fase SDLC
┌──────────────────────────────────────────────────────────┐
│ Fase              │ Biaya Relatif    │ Visualisasi        │
├───────────────────┼──────────────────┼────────────────────┤
│ Requirements      │ 1x               │ █                  │
│ Design            │ 3-6x             │ ████               │
│ Construction      │ 10x              │ ██████████         │
│ Testing           │ 15-40x           │ █████████████████  │
│ Production        │ 30-100x          │ ██████████████████████████│
└──────────────────────────────────────────────────────────┘
Sumber: Boehm & Basili, "Software Defect Reduction Top 10 List"
```

**Contoh kasus Indonesia:**

| Kasus | Tahun | Dampak | Penyebab |
|-------|-------|--------|----------|
| Sistem registrasi CPNS overload | 2023 | Jutaan pelamar gagal akses | Kurang *load testing* |
| Gangguan layanan mobile banking BCA | 2023 | Jutaan nasabah tidak bisa transaksi | Update tanpa *regression testing* memadai |
| Bug sistem PPDB DKI Jakarta | 2022 | Ratusan siswa salah alokasi | Kurang *integration testing* antar modul |
| Error sistem tiket KAI online | 2024 | Lonjakan akses tidak tertangani | Kurang *stress testing* |

> **Studi Kasus Singkat:** Bayangkan sebuah UMKM di Bandung membangun aplikasi kasir POS (*Point of Sale*). Saat rilis, fungsi `hitung_total_dengan_diskon()` mengembalikan harga negatif jika diskon > 100%. Bug ini baru ditemukan setelah 200+ transaksi tercatat salah. Biaya perbaikan? Bukan hanya fix kode — tetapi juga koreksi data, pengembalian uang, dan hilangnya kepercayaan pelanggan.

### 9.2 Level Testing (Testing Levels)

Testing dilakukan secara berlapis (*layered*), dari unit terkecil hingga sistem keseluruhan:

| Level | Scope | Dilakukan Oleh | Contoh | Jumlah Test |
|-------|-------|-----------------|--------|-------------|
| **Unit Testing** | Satu fungsi/method | Developer | Test fungsi `hitung_diskon()` | Ratusan-ribuan |
| **Integration Testing** | Interaksi antar modul | Developer/QA | Test API endpoint + database | Puluhan-ratusan |
| **System Testing** | Seluruh sistem | QA Team | Test aplikasi e-commerce end-to-end | Puluhan |
| **Acceptance Testing** | Kebutuhan bisnis | Client/User | UAT: "Apakah fitur checkout sesuai?" | Belasan |

```
Testing Pyramid (Mike Cohn)
┌──────────────────────────────────────────────────────┐
│              Acceptance Testing                       │
│   ┌──────────────────────────────────────────────┐   │
│   │            System Testing                     │   │
│   │   ┌──────────────────────────────────────┐   │   │
│   │   │       Integration Testing             │   │   │
│   │   │   ┌──────────────────────────────┐   │   │   │
│   │   │   │       Unit Testing            │   │   │   │
│   │   │   └──────────────────────────────┘   │   │   │
│   │   └──────────────────────────────────────┘   │   │
│   └──────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────┘

Semakin bawah:  LEBIH BANYAK | LEBIH CEPAT | LEBIH MURAH
Semakin atas:   LEBIH SEDIKIT | LEBIH LAMBAT | LEBIH MAHAL
```

#### Analogi Indonesia

Bayangkan membangun rumah:
- **Unit Test** = Cek setiap bata apakah kokoh (material)
- **Integration Test** = Cek apakah bata terpasang baik dengan semen (sambungan)
- **System Test** = Cek apakah seluruh rumah berdiri kokoh (struktur)
- **Acceptance Test** = Pemilik rumah mengecek: "Apakah sesuai desain saya?" (penerimaan)

#### Contoh di Proyek Web App UMKM

```python
# === UNIT TEST: Test fungsi individual ===
def test_hitung_subtotal():
    """Test: hitung subtotal = harga x jumlah"""
    assert hitung_subtotal(harga=25000, jumlah=3) == 75000

# === INTEGRATION TEST: Test interaksi modul ===
def test_tambah_produk_ke_database(db_session):
    """Test: endpoint POST /api/produk menyimpan ke database"""
    response = client.post("/api/produk", json={
        "nama": "Keripik Tempe",
        "harga": 15000,
        "stok": 100
    })
    assert response.status_code == 201
    produk = db_session.query(Produk).filter_by(nama="Keripik Tempe").first()
    assert produk is not None
    assert produk.harga == 15000

# === SYSTEM TEST: Test alur end-to-end ===
# (Biasanya dilakukan dengan tool E2E seperti Playwright)
# Alur: Login -> Tambah produk -> Cek di daftar -> Hapus produk

# === ACCEPTANCE TEST: Test berdasarkan user story ===
# User Story: Sebagai pemilik toko, saya ingin menambah produk baru
# Acceptance Criteria: Produk tersimpan dan muncul di halaman katalog
```

### 9.3 Teknik Desain Test Case

Teknik desain test case membantu kita memilih **set test minimal yang efektif** untuk menemukan bug secara sistematis.

#### 9.3.1 Equivalence Partitioning (EP)

Membagi domain input menjadi kelas-kelas yang setara (*equivalence classes*). Asumsinya: jika satu nilai dalam kelas berhasil/gagal, semua nilai lain dalam kelas yang sama akan berperilaku sama.

```
Contoh: Fungsi diskon tiket TransJakarta berdasarkan usia
  - Anak (0-12):   diskon 50%
  - Dewasa (13-59): tidak ada diskon
  - Lansia (60+):   diskon 30%
  - Usia negatif:   error (invalid)

Equivalence Classes:
┌──────────┬───────────┬───────────┬──────────┐
│ INVALID  │  ANAK     │  DEWASA   │  LANSIA  │
│ usia < 0 │  0 - 12   │  13 - 59  │  60+     │
└──────────┴───────────┴───────────┴──────────┘

Minimal test cases (1 per kelas): -5, 6, 35, 70
```

```python
# Implementasi test cases berdasarkan EP
import pytest

def test_ep_kelas_invalid():
    """Equivalence class: usia negatif -> ValueError"""
    with pytest.raises(ValueError, match="Usia tidak boleh negatif"):
        hitung_diskon_tiket(harga=3500, usia=-5)

def test_ep_kelas_anak():
    """Equivalence class: usia 0-12 -> diskon 50%"""
    assert hitung_diskon_tiket(harga=3500, usia=6) == 1750

def test_ep_kelas_dewasa():
    """Equivalence class: usia 13-59 -> harga penuh"""
    assert hitung_diskon_tiket(harga=3500, usia=35) == 3500

def test_ep_kelas_lansia():
    """Equivalence class: usia 60+ -> diskon 30%"""
    assert hitung_diskon_tiket(harga=3500, usia=70) == 2450
```

#### 9.3.2 Boundary Value Analysis (BVA)

BVA fokus pada **batas-batas** antar kelas — tempat paling rawan bug:

```
Boundary Values untuk fungsi diskon tiket:

     -1  0  1        12  13        59  60  61
      │  │  │         │   │         │   │   │
──────┼──┼──┼─────────┼───┼─────────┼───┼───┼──────
 INVALID│ ANAK        │ DEWASA     │ LANSIA
      │  │            │            │
   Boundary        Boundary     Boundary

Test cases BVA: {-1, 0, 1, 12, 13, 59, 60, 61}
```

```python
# Test cases berdasarkan BVA
class TestBVADiskonTiket:
    """Boundary Value Analysis untuk hitung_diskon_tiket"""

    # Batas bawah usia valid (0)
    def test_batas_bawah_invalid(self):
        with pytest.raises(ValueError):
            hitung_diskon_tiket(3500, -1)

    def test_batas_bawah_anak(self):
        assert hitung_diskon_tiket(3500, 0) == 1750   # diskon anak

    def test_usia_satu(self):
        assert hitung_diskon_tiket(3500, 1) == 1750   # masih anak

    # Batas anak-dewasa (12-13)
    def test_batas_atas_anak(self):
        assert hitung_diskon_tiket(3500, 12) == 1750  # masih anak

    def test_batas_bawah_dewasa(self):
        assert hitung_diskon_tiket(3500, 13) == 3500  # dewasa

    # Batas dewasa-lansia (59-60)
    def test_batas_atas_dewasa(self):
        assert hitung_diskon_tiket(3500, 59) == 3500  # masih dewasa

    def test_batas_bawah_lansia(self):
        assert hitung_diskon_tiket(3500, 60) == 2450  # lansia

    def test_lansia_normal(self):
        assert hitung_diskon_tiket(3500, 61) == 2450  # masih lansia
```

#### 9.3.3 Decision Table

Decision table cocok untuk fungsi dengan **kombinasi kondisi**:

```
Contoh: Sistem diskon toko online Indonesia

Kondisi:
  C1: Apakah member?
  C2: Total pembelian > Rp 500.000?
  C3: Hari libur nasional?

Decision Table:
┌────────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
│        │ R1  │ R2  │ R3  │ R4  │ R5  │ R6  │ R7  │ R8  │
├────────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ Member │  Y  │  Y  │  Y  │  Y  │  N  │  N  │  N  │  N  │
│ >500rb │  Y  │  Y  │  N  │  N  │  Y  │  Y  │  N  │  N  │
│ Libur  │  Y  │  N  │  Y  │  N  │  Y  │  N  │  Y  │  N  │
├────────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ Diskon │ 25% │ 20% │ 15% │ 10% │ 10% │  5% │  5% │  0% │
└────────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘
```

```python
# Test berdasarkan Decision Table
@pytest.mark.parametrize("member,total,libur,expected_diskon", [
    (True,  600000, True,  0.25),  # R1: Member + >500rb + libur
    (True,  600000, False, 0.20),  # R2: Member + >500rb + bukan libur
    (True,  300000, True,  0.15),  # R3: Member + <=500rb + libur
    (True,  300000, False, 0.10),  # R4: Member + <=500rb + bukan libur
    (False, 600000, True,  0.10),  # R5: Non-member + >500rb + libur
    (False, 600000, False, 0.05),  # R6: Non-member + >500rb + bukan libur
    (False, 300000, True,  0.05),  # R7: Non-member + <=500rb + libur
    (False, 300000, False, 0.00),  # R8: Non-member + <=500rb + bukan libur
])
def test_diskon_toko_online(member, total, libur, expected_diskon):
    hasil = hitung_diskon_toko(member=member, total=total, hari_libur=libur)
    assert hasil == expected_diskon
```

### 9.4 Test-Driven Development (TDD)

TDD adalah pendekatan pengembangan di mana **test ditulis sebelum kode produksi**. Siklus TDD dikenal sebagai **Red-Green-Refactor**:

```
Siklus TDD: Red-Green-Refactor
┌─────────────┐       ┌─────────────┐       ┌──────────────┐
│    RED       │──────▶│   GREEN     │──────▶│  REFACTOR    │
│              │       │             │       │              │
│ Tulis test   │       │ Tulis kode  │       │ Bersihkan    │
│ yang GAGAL   │       │ MINIMAL     │       │ kode tanpa   │
│ (test first) │       │ agar test   │       │ mengubah     │
│              │       │ LULUS       │       │ perilaku     │
└─────────────┘       └─────────────┘       └──────┬───────┘
       ▲                                           │
       └───────────────────────────────────────────┘
                   Ulangi siklus
```

#### Mengapa TDD?

| Manfaat | Penjelasan |
|---------|------------|
| **Desain lebih baik** | Memaksa berpikir tentang interface sebelum implementasi |
| **Dokumentasi hidup** | Test menjadi spesifikasi yang selalu up-to-date |
| **Confidence** | Refactoring tanpa takut merusak fungsionalitas |
| **Bug lebih sedikit** | Defect ditemukan lebih awal |
| **Kode lebih modular** | Kode yang mudah di-test = kode yang well-designed |

#### TDD Tutorial: Validasi NIM (Python + pytest)

Kita akan membangun fungsi `validasi_nim()` dengan TDD. NIM UAI memiliki format: `XXYYYY` di mana XX = kode prodi, YYYY = angka unik.

**Langkah 1 - RED: Tulis test yang gagal**

```python
# test_nim.py
import pytest
from nim import validasi_nim

class TestValidasiNIM:
    """TDD: Validasi NIM Universitas Al Azhar Indonesia"""

    def test_nim_valid_informatika(self):
        """NIM valid prodi Informatika (kode 12)"""
        assert validasi_nim("120001") == True

    def test_nim_valid_sistem_informasi(self):
        """NIM valid prodi Sistem Informasi (kode 13)"""
        assert validasi_nim("130042") == True

    def test_nim_terlalu_pendek(self):
        """NIM kurang dari 6 digit -> False"""
        assert validasi_nim("1200") == False

    def test_nim_terlalu_panjang(self):
        """NIM lebih dari 6 digit -> False"""
        assert validasi_nim("12000011") == False

    def test_nim_mengandung_huruf(self):
        """NIM mengandung karakter non-angka -> False"""
        assert validasi_nim("12AB01") == False

    def test_nim_kode_prodi_invalid(self):
        """Kode prodi tidak dikenal (bukan 12 atau 13) -> False"""
        assert validasi_nim("990001") == False

    def test_nim_kosong(self):
        """NIM string kosong -> False"""
        assert validasi_nim("") == False

    def test_nim_none(self):
        """NIM None -> ValueError"""
        with pytest.raises(ValueError, match="NIM tidak boleh None"):
            validasi_nim(None)
```

```bash
# Jalankan test -> SEMUA GAGAL (RED)
$ pytest test_nim.py -v
FAILED test_nim.py::TestValidasiNIM::test_nim_valid_informatika
FAILED test_nim.py::TestValidasiNIM::test_nim_valid_sistem_informasi
... (8 tests FAILED)
```

**Langkah 2 - GREEN: Implementasi minimal**

```python
# nim.py
KODE_PRODI_VALID = {"12", "13"}  # Informatika, Sistem Informasi

def validasi_nim(nim: str) -> bool:
    """
    Validasi NIM mahasiswa UAI.
    Format: XXYYYY (XX=kode prodi, YYYY=angka unik)

    Args:
        nim: String NIM yang akan divalidasi

    Returns:
        True jika NIM valid, False jika tidak

    Raises:
        ValueError: Jika nim adalah None
    """
    if nim is None:
        raise ValueError("NIM tidak boleh None")

    # Cek panjang harus tepat 6 digit
    if len(nim) != 6:
        return False

    # Cek semua karakter harus angka
    if not nim.isdigit():
        return False

    # Cek kode prodi (2 digit pertama)
    kode_prodi = nim[:2]
    if kode_prodi not in KODE_PRODI_VALID:
        return False

    return True
```

```bash
# Jalankan test -> SEMUA LULUS (GREEN)
$ pytest test_nim.py -v
PASSED test_nim.py::TestValidasiNIM::test_nim_valid_informatika
PASSED test_nim.py::TestValidasiNIM::test_nim_valid_sistem_informasi
... (8 tests PASSED)
```

**Langkah 3 - REFACTOR: Perbaiki tanpa mengubah perilaku**

```python
# nim.py (setelah refactor)
from dataclasses import dataclass
from typing import Final

# Konstanta prodi
KODE_PRODI: Final[dict[str, str]] = {
    "12": "Informatika",
    "13": "Sistem Informasi",
}
PANJANG_NIM: Final[int] = 6

def validasi_nim(nim: str) -> bool:
    """Validasi NIM mahasiswa UAI. Format: XXYYYY."""
    if nim is None:
        raise ValueError("NIM tidak boleh None")

    if not _format_valid(nim):
        return False

    return _kode_prodi_valid(nim)

def _format_valid(nim: str) -> bool:
    """Cek apakah format NIM memenuhi syarat panjang dan digit."""
    return len(nim) == PANJANG_NIM and nim.isdigit()

def _kode_prodi_valid(nim: str) -> bool:
    """Cek apakah kode prodi (2 digit pertama) terdaftar."""
    return nim[:2] in KODE_PRODI
```

```bash
# Jalankan test lagi -> TETAP LULUS (REFACTOR berhasil)
$ pytest test_nim.py -v
... (8 tests PASSED)
```

#### TDD Tutorial: Format Rupiah (JavaScript + Jest)

**Langkah 1 - RED:**

```javascript
// formatRupiah.test.js
const { formatRupiah } = require('./formatRupiah');

describe('formatRupiah', () => {
  // === Pola AAA: Arrange, Act, Assert ===

  test('format angka positif dengan separator ribuan', () => {
    // Arrange
    const angka = 1500000;
    // Act
    const hasil = formatRupiah(angka);
    // Assert
    expect(hasil).toBe('Rp 1.500.000');
  });

  test('format angka nol', () => {
    expect(formatRupiah(0)).toBe('Rp 0');
  });

  test('format angka kecil tanpa separator', () => {
    expect(formatRupiah(500)).toBe('Rp 500');
  });

  test('format angka dengan desimal dibulatkan', () => {
    expect(formatRupiah(15999.7)).toBe('Rp 16.000');
  });

  test('angka negatif menampilkan tanda minus', () => {
    expect(formatRupiah(-50000)).toBe('-Rp 50.000');
  });

  test('input bukan angka throw error', () => {
    expect(() => formatRupiah('bukan angka')).toThrow('Input harus berupa angka');
  });

  test('input null throw error', () => {
    expect(() => formatRupiah(null)).toThrow('Input harus berupa angka');
  });
});
```

**Langkah 2 - GREEN:**

```javascript
// formatRupiah.js
function formatRupiah(angka) {
  if (typeof angka !== 'number' || isNaN(angka)) {
    throw new Error('Input harus berupa angka');
  }

  const bulat = Math.round(angka);
  const isNegatif = bulat < 0;
  const absolut = Math.abs(bulat);

  // Format dengan separator titik (Indonesia)
  const formatted = absolut.toString().replace(/\B(?=(\d{3})+(?!\d))/g, '.');

  return `${isNegatif ? '-' : ''}Rp ${formatted}`;
}

module.exports = { formatRupiah };
```

```bash
# Jalankan test
$ npx jest formatRupiah.test.js --verbose
 PASS  ./formatRupiah.test.js
  formatRupiah
    ✓ format angka positif dengan separator ribuan (2 ms)
    ✓ format angka nol (1 ms)
    ✓ format angka kecil tanpa separator (1 ms)
    ✓ format angka dengan desimal dibulatkan (1 ms)
    ✓ angka negatif menampilkan tanda minus (1 ms)
    ✓ input bukan angka throw error (2 ms)
    ✓ input null throw error (1 ms)

Tests: 7 passed, 7 total
```

#### Pola AAA (Arrange-Act-Assert)

Setiap test sebaiknya mengikuti pola **AAA** untuk keterbacaan:

```python
def test_hitung_total_pesanan():
    # Arrange - siapkan data dan kondisi awal
    pesanan = Pesanan(items=[
        Item(nama="Nasi Goreng", harga=25000, qty=2),
        Item(nama="Es Teh", harga=5000, qty=2),
    ])

    # Act - jalankan aksi yang diuji
    total = pesanan.hitung_total()

    # Assert - verifikasi hasilnya
    assert total == 60000  # (25000*2) + (5000*2)
```

```javascript
// Pola AAA di Jest
test('menghitung total pesanan dengan benar', () => {
  // Arrange
  const items = [
    { nama: 'Nasi Goreng', harga: 25000, qty: 2 },
    { nama: 'Es Teh', harga: 5000, qty: 2 },
  ];

  // Act
  const total = hitungTotal(items);

  // Assert
  expect(total).toBe(60000);
});
```

### 9.5 Menjalankan Test dan Melihat Hasil

#### pytest (Python)

```bash
# Jalankan semua test
$ pytest

# Jalankan dengan output verbose
$ pytest -v

# Jalankan test di file tertentu
$ pytest test_nim.py

# Jalankan test class atau fungsi tertentu
$ pytest test_nim.py::TestValidasiNIM::test_nim_valid_informatika

# Jalankan dengan code coverage
$ pytest --cov=src --cov-report=term-missing

# Contoh output coverage:
# Name             Stmts   Miss  Cover   Missing
# ------------------------------------------------
# src/nim.py          15      0   100%
# src/diskon.py       12      2    83%   18-19
# ------------------------------------------------
# TOTAL               27      2    93%
```

#### Jest (JavaScript)

```bash
# Jalankan semua test
$ npx jest

# Jalankan dengan verbose
$ npx jest --verbose

# Jalankan test tertentu
$ npx jest formatRupiah.test.js

# Jalankan dengan coverage
$ npx jest --coverage

# Watch mode (re-run saat file berubah)
$ npx jest --watch
```

### 9.6 Quality Assurance vs Quality Control

```
QA vs QC — Dua Pendekatan Komplementer
┌────────────────────────────────────────────────────────────┐
│                    Quality Management                       │
│                                                            │
│  ┌──────────────────────┐   ┌──────────────────────────┐  │
│  │  Quality Assurance   │   │  Quality Control          │  │
│  │  (QA)                │   │  (QC)                     │  │
│  │                      │   │                           │  │
│  │  Fokus: PROSES       │   │  Fokus: PRODUK            │  │
│  │  Kapan: Sepanjang    │   │  Kapan: Setelah produk    │  │
│  │         SDLC         │   │         dibuat            │  │
│  │  Tujuan: MENCEGAH    │   │  Tujuan: MENEMUKAN        │  │
│  │          defect      │   │          defect            │  │
│  │  Sifat: PROAKTIF     │   │  Sifat: REAKTIF           │  │
│  │                      │   │                           │  │
│  │  Contoh:             │   │  Contoh:                  │  │
│  │  - Code review       │   │  - Unit testing           │  │
│  │  - Coding standards  │   │  - Bug report             │  │
│  │  - Pair programming  │   │  - UAT (User Acceptance)  │  │
│  │  - CI/CD setup       │   │  - Performance testing    │  │
│  └──────────────────────┘   └──────────────────────────┘  │
└────────────────────────────────────────────────────────────┘
```

| Aspek | Quality Assurance (QA) | Quality Control (QC) |
|-------|----------------------|---------------------|
| **Analogi** | Memastikan resep masakan benar | Mencicipi makanan jadi |
| **Pendekatan** | Process-oriented | Product-oriented |
| **Timing** | Sebelum & selama produksi | Setelah produksi |
| **Tanggung jawab** | Seluruh tim | Tim testing / QC |
| **Tool** | ESLint, Prettier, SonarQube | pytest, Jest, Playwright |
| **Contoh Indonesia** | SNI sebagai standar proses | Uji lab BPOM untuk produk jadi |

> **Nilai Islami -- Itqan (Kesempurnaan):** Rasulullah SAW bersabda, *"Sesungguhnya Allah mencintai jika seseorang melakukan pekerjaan, ia melakukannya dengan itqan (sempurna)."* (HR. Al-Baihaqi). Testing adalah bentuk *itqan* dalam pengembangan perangkat lunak -- memastikan produk digital yang kita buat benar-benar berkualitas dan dapat dipercaya oleh pengguna.

### 9.7 Ringkasan Strategi Testing per Konteks

```
Proyek kecil (1-2 developer, 1 bulan):
├── Unit test: Fokus pada fungsi inti (coverage 60%+)
├── Integration test: Test API endpoint utama
└── Manual testing: Cek UI/UX

Proyek medium (3-5 developer, 3 bulan):
├── Unit test: Komprehensif (coverage 70%+)
├── Integration test: Semua API endpoints
├── E2E test: Happy path utama
└── CI/CD: Automated test di setiap push

Proyek besar (10+ developer, 6+ bulan):
├── Unit test: Wajib semua modul (coverage 80%+)
├── Integration test: Kontrak antar service
├── E2E test: Semua user flow kritis
├── Performance test: Load & stress testing
├── Security test: OWASP Top 10
└── CI/CD + staging environment
```

---

## Kegiatan Pembelajaran

### Pre-class (20 menit)

- Membaca artikel: *"The Practical Test Pyramid"* oleh Martin Fowler ([martinfowler.com](https://martinfowler.com/articles/practical-test-pyramid.html))
- Menginstal pytest (`pip install pytest pytest-cov`) dan Jest (`npm install --save-dev jest`) di GitHub Codespaces
- Menjawab pertanyaan refleksi: "Pernahkah kamu menemukan bug di aplikasi yang kamu gunakan sehari-hari (Gojek, Tokopedia, dll.)? Apa dampaknya?"

### In-class (110 menit)

| Waktu | Aktivitas | Metode |
|-------|-----------|--------|
| 0-15 menit | Konsep testing levels, testing pyramid, biaya bug | Ceramah + diskusi |
| 15-35 menit | Teknik desain test case (EP, BVA, Decision Table) dengan contoh Indonesia | Ceramah + latihan |
| 35-50 menit | Demo TDD Red-Green-Refactor: validasi NIM (live coding) | Live coding |
| 50-55 menit | *Break* | -- |
| 55-75 menit | Hands-on: TDD dengan pytest -- implementasi fungsi hitung_pajak() | Hands-on coding |
| 75-95 menit | Hands-on: TDD dengan Jest -- implementasi fungsi formatRupiah() | Hands-on coding |
| 95-110 menit | QA vs QC, pola AAA, diskusi strategi testing untuk proyek kelompok | Diskusi kelas |

### Post-class (20 menit)

- Review catatan dan konsep TDD, jalankan kembali contoh kode di Codespaces
- Jalankan `pytest --cov` pada modul proyek kelompok dan analisis hasilnya
- Mempersiapkan tugas T4 (Test Plan & Unit Test Suite)
- Eksplorasi: baca dokumentasi pytest fixtures untuk integration testing

---

## Latihan & Diskusi

### Soal 1 (C2 -- Memahami)
Jelaskan perbedaan antara *unit testing* dan *integration testing*. Berikan masing-masing satu contoh konkret dari proyek web app toko online UMKM.

### Soal 2 (C3 -- Menerapkan)
Diberikan fungsi berikut:

```python
def kategorisasi_bmi(berat_kg: float, tinggi_m: float) -> str:
    """Kategorisasi BMI: Underweight (<18.5), Normal (18.5-24.9),
    Overweight (25-29.9), Obese (>=30)"""
    bmi = berat_kg / (tinggi_m ** 2)
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"
```

a) Identifikasi equivalence classes untuk parameter input.
b) Tentukan boundary values yang perlu diuji.
c) Tulis minimal 6 test cases menggunakan pytest.

### Soal 3 (C4 -- Menganalisis)
Sebuah sistem e-commerce memiliki aturan ongkos kirim berikut:
- Berat <= 1 kg dan dalam Pulau Jawa: Rp 10.000
- Berat <= 1 kg dan luar Jawa: Rp 20.000
- Berat > 1 kg dan dalam Pulau Jawa: Rp 10.000 + Rp 5.000 per kg tambahan
- Berat > 1 kg dan luar Jawa: Rp 20.000 + Rp 10.000 per kg tambahan

Buat decision table dan tulis test cases lengkap menggunakan `pytest.mark.parametrize`.

### Soal 4 (C5 -- Mengevaluasi)
Tim pengembang mendapatkan code coverage 95% pada proyek mereka, namun masih sering menemukan bug di production. Analisis kemungkinan penyebabnya dan jelaskan mengapa code coverage tinggi belum tentu berarti kualitas test yang tinggi. Sarankan metrik tambahan yang bisa digunakan.

### Soal 5 (C4 -- Menganalisis)
Perhatikan dua pendekatan berikut untuk menambahkan fitur baru:
- **Pendekatan A:** Tulis kode terlebih dahulu, lalu tulis test setelahnya
- **Pendekatan B:** Terapkan TDD (Red-Green-Refactor)

Bandingkan kedua pendekatan tersebut dari segi: (a) kualitas desain kode, (b) waktu pengembangan, (c) confidence saat refactoring. Kapan masing-masing pendekatan lebih tepat digunakan?

---

## Penugasan

### T4 -- Test Plan & Unit Test Suite

| Komponen | Detail |
|----------|--------|
| **Tipe** | Individual |
| **Bobot** | 2.5% dari nilai akhir |
| **Deadline** | Minggu 11 |
| **Deliverable** | 1) Dokumen Test Plan (markdown), 2) Unit test suite (pytest + Jest) |
| **CPMK** | CPMK-5 |

**Instruksi:**
1. Pilih satu modul dari proyek kelompok (misalnya: modul produk, modul user, modul transaksi)
2. Buat **Test Plan** yang mencakup:
   - Scope: modul mana yang diuji dan mana yang di-luar scope
   - Strategi testing: teknik apa yang digunakan (EP, BVA, dll.)
   - Test cases: minimal 10 test cases dengan ID, deskripsi, input, expected output
   - Kriteria pass/fail: kapan modul dianggap siap
3. Implementasikan **unit test** menggunakan pytest (backend) dan/atau Jest (frontend) -- minimal 8 test cases
4. Terapkan pendekatan TDD: commit history harus menunjukkan siklus Red-Green-Refactor
5. Sertakan screenshot hasil `pytest --cov` dan/atau `npx jest --coverage`

**Kriteria Penilaian:**

| Kriteria | Bobot |
|----------|-------|
| Kelengkapan Test Plan | 25% |
| Kualitas test cases (bermakna, bukan trivial) | 30% |
| Implementasi test (runnable, mengikuti pola AAA) | 25% |
| Commit history menunjukkan TDD | 10% |
| Code coverage >= 70% | 10% |

---

## Referensi

1. Pressman, R. S. & Maxim, B. R. (2020). *Software Engineering: A Practitioner's Approach*, 9th ed. McGraw-Hill. Chapter 22-23.
2. Sommerville, I. (2016). *Software Engineering*, 10th ed. Pearson. Chapter 8.
3. Fowler, M. (2018). "The Practical Test Pyramid." [martinfowler.com](https://martinfowler.com/articles/practical-test-pyramid.html)
4. Beck, K. (2003). *Test-Driven Development: By Example*. Addison-Wesley.
5. pytest documentation. [docs.pytest.org](https://docs.pytest.org/)
6. Jest documentation. [jestjs.io](https://jestjs.io/)
7. IEEE Computer Society. (2024). *SWEBOK v4* -- Chapter 10: Software Testing.
8. Myers, G. J. et al. (2011). *The Art of Software Testing*, 3rd ed. Wiley.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* -- Program Studi Informatika, Universitas Al Azhar Indonesia
