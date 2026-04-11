# BAB 8: SOFTWARE TESTING FUNDAMENTALS

**Oleh: Tri Aji Nugroho, S.T., M.T.**
**Mata Kuliah:** IF2205 Rekayasa Perangkat Lunak
**Program Studi Informatika — Universitas Al Azhar Indonesia**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi | Level Bloom | Estimasi Waktu |
|-----------|-----------|-------------|----------------|
| 5.1 | Merancang test case menggunakan teknik equivalence partitioning dan boundary value analysis | C4 (Menganalisis) | 75 menit |
| 5.2 | Mengimplementasikan unit test dan integration test menggunakan pytest (Python) dan Jest (JavaScript) | C3 (Menerapkan) | 75 menit |

---

## Peta Konsep Bab 8

```
                    ┌─────────────────────────────┐
                    │   SOFTWARE TESTING           │
                    │   FUNDAMENTALS               │
                    └──────────┬──────────────────┘
                               │
          ┌────────────────────┼────────────────────┐
          │                    │                     │
    ┌─────▼──────┐    ┌───────▼───────┐    ┌───────▼───────┐
    │ Mengapa     │    │ Testing       │    │ Test Case     │
    │ Testing?    │    │ Levels &      │    │ Design        │
    │             │    │ V-Model       │    │ Techniques    │
    └─────┬──────┘    └───────┬───────┘    └───────┬───────┘
          │                   │                     │
    ┌─────▼──────┐    ┌───────▼───────┐    ┌───────▼───────┐
    │ Terminologi │    │ pytest        │    │ Jest          │
    │ Testing     │    │ Tutorial      │    │ Tutorial      │
    │ (SUT, Mock) │    │ Lengkap       │    │ JavaScript    │
    └─────┬──────┘    └───────┬───────┘    └───────┬───────┘
          │                   │                     │
          └────────────────────┼────────────────────┘
                               │
                    ┌──────────▼──────────┐
                    │ Test Organization   │
                    │ Patterns (AAA)      │
                    └─────────────────────┘
```

---

## 8.1 Mengapa Software Testing Penting?

> *"Testing can only show the presence of bugs, not their absence."* — Edsger W. Dijkstra

Meskipun Dijkstra benar bahwa testing tidak bisa membuktikan ketiadaan bug, testing tetap merupakan **garis pertahanan utama** terhadap cacat perangkat lunak. Tanpa testing yang memadai, software menjadi bom waktu yang bisa meledak kapan saja.

### 8.1.1 Cost of Bugs — Semakin Lambat, Semakin Mahal

Penelitian IBM Systems Sciences Institute dan NIST menunjukkan bahwa biaya perbaikan bug meningkat secara eksponensial seiring berjalannya fase SDLC:

```
Biaya Relatif Perbaikan Bug per Fase SDLC
                                                         ║
                                                    100x ║          ████
                                                         ║          ████
                                                         ║          ████
                                                         ║          ████
                                                    50x  ║     ████ ████
                                                         ║     ████ ████
                                                    15x  ║████ ████ ████
                                                    6.5x ║████ ████ ████
                                                    1x   ║████ ████ ████
                                                         ╚════╧════╧════
                                                          Dev  Test  Prod

  1x = biaya perbaikan saat development
  15x = biaya perbaikan saat testing
  100x = biaya perbaikan setelah production
```

### 8.1.2 Kasus Nyata Kegagalan Testing

| Kasus | Tahun | Dampak | Penyebab |
|-------|-------|--------|----------|
| Ariane 5 Rocket | 1996 | Roket meledak 37 detik setelah peluncuran, kerugian $370 juta | Integer overflow tidak di-test |
| Therac-25 | 1985-87 | 6 pasien overdosis radiasi, 3 meninggal | Race condition tidak terdeteksi |
| Knight Capital | 2012 | Kerugian $440 juta dalam 45 menit | Deployment tanpa regression testing |
| British Post Office (Horizon) | 1999-2015 | 700+ orang dihukum salah akibat bug accounting | Kurang integration testing |

**Konteks Indonesia:** Pada tahun 2023, beberapa perbankan di Indonesia mengalami gangguan layanan digital banking yang menyebabkan nasabah tidak bisa melakukan transaksi selama berjam-jam. Hal ini menunjukkan pentingnya testing menyeluruh pada sistem kritis (*mission-critical systems*).

### 8.1.3 Testing Sebagai Investasi

Testing bukan sekadar biaya tambahan — ini adalah **investasi** yang memberikan:

| Manfaat | Penjelasan |
|---------|------------|
| **Confidence** | Memberikan kepercayaan bahwa perubahan tidak merusak fitur yang sudah ada |
| **Documentation** | Test cases mendokumentasikan expected behavior lebih akurat dari komentar kode |
| **Design feedback** | Kode yang sulit di-test biasanya memiliki desain yang buruk |
| **Regression safety** | Memungkinkan refactoring dengan aman |
| **Communication** | Test menjelaskan business rules ke developer baru |

### 8.1.4 Testing Pyramid

Testing pyramid adalah model yang menggambarkan proporsi ideal dari berbagai jenis test:

```
                 /\
                /  \           E2E Tests
               / 5% \         (sedikit, mahal, lambat)
              /──────\         ~menit per test
             /        \
            / 15-20%   \      Integration Tests
           /────────────\     (sedang)
          /              \    ~detik per test
         /   70-80%       \
        /──────────────────\  Unit Tests
       /                    \ (banyak, murah, cepat)
      /______________________\~milidetik per test

  Semakin ke bawah: LEBIH cepat, LEBIH murah, LEBIH banyak
  Semakin ke atas:  LEBIH lambat, LEBIH mahal, LEBIH sedikit
```

> **Tips:** Google menggunakan rasio 70/20/10 (unit/integration/E2E). Ini bukan aturan baku, tetapi guideline yang baik untuk memulai.

---

## 8.2 Testing Levels dan V-Model

### 8.2.1 Empat Level Testing

| Level | Apa yang Ditest | Siapa yang Melakukan | Tools | Kecepatan |
|-------|----------------|---------------------|-------|-----------|
| **Unit Testing** | Fungsi/method individual secara terisolasi | Developer | pytest, Jest, JUnit | Sangat cepat (ms) |
| **Integration Testing** | Interaksi antar komponen/modul | Developer/QA | pytest, Supertest, TestContainers | Cepat (detik) |
| **System Testing** | Seluruh sistem end-to-end | QA Team | Selenium, Playwright, Cypress | Lambat (menit) |
| **Acceptance Testing** | Kesesuaian dengan requirements bisnis | Stakeholder/PO | Manual, Cucumber, Robot Framework | Bervariasi |

### 8.2.2 V-Model — Hubungan Development dan Testing

V-Model menunjukkan bahwa setiap fase development memiliki fase testing yang berkorespondensi:

```
  Requirements ─────────────────────────────── Acceptance Testing
  Analysis        \                       /       (UAT)
                   \                     /
  System Design ────\─────────────────/──── System Testing
                     \               /
  Architecture ───────\─────────────/────── Integration Testing
  Design               \           /
                        \         /
  Module Design ─────────\───────/──────── Unit Testing
                          \     /
                           \   /
                        Implementation
                          (Coding)

  KIRI: Fase Development (Verification)
  KANAN: Fase Testing (Validation)
  BAWAH: Implementasi (titik balik)
```

**Prinsip V-Model:**
1. Setiap fase development di **sisi kiri** menghasilkan test plan untuk fase testing di **sisi kanan**
2. Requirements menghasilkan Acceptance Test Plan
3. System Design menghasilkan System Test Plan
4. Architecture Design menghasilkan Integration Test Plan
5. Module Design menghasilkan Unit Test Plan

### 8.2.3 Penjelasan Detail Setiap Level

**Unit Testing** — Menguji komponen terkecil secara terisolasi:

```python
# Contoh unit test: menguji fungsi hitung_diskon() secara terisolasi
def hitung_diskon(total_belanja, persen_diskon):
    """Menghitung diskon belanja."""
    if total_belanja < 0:
        raise ValueError("Total belanja tidak boleh negatif")
    if not 0 <= persen_diskon <= 100:
        raise ValueError("Persen diskon harus antara 0-100")
    return total_belanja * persen_diskon / 100

# Unit test
def test_hitung_diskon_normal():
    assert hitung_diskon(100000, 10) == 10000

def test_hitung_diskon_nol():
    assert hitung_diskon(100000, 0) == 0

def test_hitung_diskon_total_negatif():
    import pytest
    with pytest.raises(ValueError):
        hitung_diskon(-50000, 10)
```

**Integration Testing** — Menguji interaksi antar komponen:

```python
# Contoh integration test: menguji Service + Repository bersama
def test_proses_pembelian_mengurangi_stok(client, db_session):
    """Integration test: pembelian harus mengurangi stok di database."""
    # Setup: tambah produk dengan stok 10
    produk = Produk(nama="Buku Python", stok=10, harga=85000)
    db_session.add(produk)
    db_session.commit()

    # Act: lakukan pembelian via API
    response = client.post('/api/pembelian', json={
        'produk_id': produk.id,
        'jumlah': 3
    })

    # Assert: stok berkurang
    assert response.status_code == 201
    produk_updated = Produk.query.get(produk.id)
    assert produk_updated.stok == 7  # 10 - 3
```

**System Testing** — Menguji keseluruhan sistem:

```python
# Contoh system test: alur lengkap dari login sampai checkout
def test_alur_belanja_lengkap(page):
    """System test: user login, pilih barang, checkout."""
    page.goto("http://localhost:5000")
    page.click("text=Login")
    page.fill("#email", "user@example.com")
    page.fill("#password", "password123")
    page.click("#btn-login")

    # Pilih barang
    page.click("text=Buku Python Dasar")
    page.click("#btn-tambah-keranjang")

    # Checkout
    page.click("#btn-checkout")
    assert page.inner_text(".status") == "Pesanan berhasil!"
```

**Acceptance Testing** — Memvalidasi terhadap requirements bisnis:

```
User Story: Sebagai nasabah BCA, saya ingin transfer antar rekening
            agar saya bisa mengirim uang ke keluarga.

Acceptance Criteria (Given-When-Then):
  Given: Nasabah sudah login dan memiliki saldo Rp 1.000.000
  When:  Nasabah transfer Rp 500.000 ke rekening tujuan
  Then:  Saldo berkurang menjadi Rp 500.000
         AND rekening tujuan bertambah Rp 500.000
         AND muncul notifikasi "Transfer berhasil"
         AND tercatat di mutasi rekening
```

---

## 8.3 Test Case Design Techniques

Test case design techniques adalah teknik sistematis untuk memilih input test yang efektif dari semua kemungkinan input (yang seringkali tidak terbatas jumlahnya).

### 8.3.1 Equivalence Partitioning (EP)

**Prinsip:** Bagi domain input menjadi kelas-kelas ekuivalen (partisi) di mana semua nilai dalam satu kelas diharapkan menghasilkan perilaku yang sama. Cukup test **satu nilai** dari setiap kelas.

**Contoh — Validasi Umur untuk Asuransi Kesehatan:**

```
Domain: umur peserta asuransi (integer)

Partisi:
  ┌──────────────┬───────────────────┬────────────────┬──────────────┐
  │ < 0          │ 0 - 17            │ 18 - 65        │ > 65         │
  │ (Invalid)    │ (Anak)            │ (Dewasa)       │ (Lansia)     │
  │              │ premi: Rp 200rb   │ premi: Rp 500rb│ premi: Rp 1jt│
  └──────────────┴───────────────────┴────────────────┴──────────────┘

Test cases (satu per partisi):
  TC1: umur = -5   → Expected: Error "Umur tidak valid"
  TC2: umur = 10   → Expected: Premi Rp 200.000 (kategori Anak)
  TC3: umur = 30   → Expected: Premi Rp 500.000 (kategori Dewasa)
  TC4: umur = 70   → Expected: Premi Rp 1.000.000 (kategori Lansia)
```

```python
# Implementasi EP dalam Python
def hitung_premi_asuransi(umur):
    """Hitung premi asuransi berdasarkan kategori umur."""
    if umur < 0:
        raise ValueError("Umur tidak valid")
    elif umur <= 17:
        return 200_000   # Anak
    elif umur <= 65:
        return 500_000   # Dewasa
    else:
        return 1_000_000  # Lansia

# Test cases berdasarkan Equivalence Partitioning
import pytest

def test_ep_invalid_umur():
    with pytest.raises(ValueError):
        hitung_premi_asuransi(-5)

def test_ep_kategori_anak():
    assert hitung_premi_asuransi(10) == 200_000

def test_ep_kategori_dewasa():
    assert hitung_premi_asuransi(30) == 500_000

def test_ep_kategori_lansia():
    assert hitung_premi_asuransi(70) == 1_000_000
```

### 8.3.2 Boundary Value Analysis (BVA)

**Prinsip:** Bug paling sering terjadi di **batas** (*boundary*) antar partisi. Test nilai tepat di batas, satu di bawah batas, dan satu di atas batas.

**Contoh — Lanjutan dari EP di atas:**

```
Boundaries:          -1  0  17  18  65  66
                      │  │   │   │   │   │
  Invalid ◄──────────►│  │   │   │   │   │
                       │  │   │   │   │   │
  Anak    ◄────────────┤  ├───┤   │   │   │
                       │  │   │   │   │   │
  Dewasa  ◄────────────┤  │   ├───┤   ├───┤
                       │  │   │   │   │   │
  Lansia  ◄────────────┤  │   │   │   ├───►

Test cases BVA:
  TC1: umur = -1  → Error (tepat di batas invalid)
  TC2: umur = 0   → Premi Anak (batas bawah valid)
  TC3: umur = 17  → Premi Anak (batas atas anak)
  TC4: umur = 18  → Premi Dewasa (batas bawah dewasa)
  TC5: umur = 65  → Premi Dewasa (batas atas dewasa)
  TC6: umur = 66  → Premi Lansia (batas bawah lansia)
```

```python
# Test cases berdasarkan Boundary Value Analysis
class TestBVAAsuransi:
    """Test boundary values untuk hitung_premi_asuransi."""

    def test_bva_batas_bawah_invalid(self):
        with pytest.raises(ValueError):
            hitung_premi_asuransi(-1)

    def test_bva_batas_bawah_anak(self):
        assert hitung_premi_asuransi(0) == 200_000

    def test_bva_batas_atas_anak(self):
        assert hitung_premi_asuransi(17) == 200_000

    def test_bva_batas_bawah_dewasa(self):
        assert hitung_premi_asuransi(18) == 500_000

    def test_bva_batas_atas_dewasa(self):
        assert hitung_premi_asuransi(65) == 500_000

    def test_bva_batas_bawah_lansia(self):
        assert hitung_premi_asuransi(66) == 1_000_000
```

### 8.3.3 Decision Table Testing

**Prinsip:** Untuk logika bisnis yang melibatkan **kombinasi kondisi**, gunakan decision table untuk memastikan semua kombinasi di-test.

**Contoh — Kebijakan Diskon Toko Online Indonesia:**

```
Kondisi:
  C1: Member VIP?         (Ya/Tidak)
  C2: Total > Rp 500rb?   (Ya/Tidak)
  C3: Hari libur nasional? (Ya/Tidak)

Decision Table:
  ┌──────────────────────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┐
  │ Kondisi              │ R1   │ R2   │ R3   │ R4   │ R5   │ R6   │ R7   │ R8   │
  ├──────────────────────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
  │ C1: Member VIP       │ Ya   │ Ya   │ Ya   │ Ya   │ Tdk  │ Tdk  │ Tdk  │ Tdk  │
  │ C2: Total > 500rb    │ Ya   │ Ya   │ Tdk  │ Tdk  │ Ya   │ Ya   │ Tdk  │ Tdk  │
  │ C3: Hari libur       │ Ya   │ Tdk  │ Ya   │ Tdk  │ Ya   │ Tdk  │ Ya   │ Tdk  │
  ├──────────────────────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
  │ Diskon (%)           │ 25%  │ 20%  │ 15%  │ 10%  │ 15%  │ 10%  │ 5%   │ 0%   │
  │ Free ongkir          │ Ya   │ Ya   │ Ya   │ Ya   │ Ya   │ Ya   │ Tdk  │ Tdk  │
  └──────────────────────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┘
```

```python
def hitung_diskon_toko(is_vip, total_belanja, is_hari_libur):
    """Hitung diskon berdasarkan decision table."""
    diskon = 0
    free_ongkir = False

    if is_vip:
        diskon += 10  # Base VIP discount
        free_ongkir = True
    if total_belanja > 500_000:
        diskon += 10
        free_ongkir = True
    if is_hari_libur:
        diskon += 5

    return {"diskon_persen": diskon, "free_ongkir": free_ongkir}

# Test berdasarkan decision table
@pytest.mark.parametrize("is_vip, total, libur, exp_diskon, exp_ongkir", [
    (True,  600_000, True,  25, True),   # R1
    (True,  600_000, False, 20, True),   # R2
    (True,  300_000, True,  15, True),   # R3
    (True,  300_000, False, 10, True),   # R4
    (False, 600_000, True,  15, True),   # R5
    (False, 600_000, False, 10, True),   # R6
    (False, 300_000, True,   5, False),  # R7
    (False, 300_000, False,  0, False),  # R8
])
def test_decision_table_diskon(is_vip, total, libur, exp_diskon, exp_ongkir):
    result = hitung_diskon_toko(is_vip, total, libur)
    assert result["diskon_persen"] == exp_diskon
    assert result["free_ongkir"] == exp_ongkir
```

### 8.3.4 State Transition Testing

**Prinsip:** Untuk sistem yang memiliki **state** (keadaan), test transisi antar state, termasuk transisi yang tidak valid.

**Contoh — State Diagram Pesanan E-Commerce:**

```
  ┌──────────┐   bayar()    ┌───────────┐  kirim()   ┌────────────┐
  │ MENUNGGU  │────────────►│ DIBAYAR    │──────────►│ DIKIRIM     │
  │ BAYAR     │             │            │           │             │
  └─────┬────┘             └─────┬──────┘           └──────┬──────┘
        │                        │                          │
        │ batal()                │ batal()                  │ terima()
        │                        │                          │
        ▼                        ▼                          ▼
  ┌──────────┐             ┌───────────┐            ┌────────────┐
  │ DIBATALKAN│             │ REFUND     │            │ SELESAI     │
  │           │             │            │            │             │
  └──────────┘             └───────────┘            └──────┬──────┘
                                                           │
                                                           │ komplain()
                                                           ▼
                                                    ┌────────────┐
                                                    │ KOMPLAIN    │
                                                    └────────────┘

  Transisi VALID:
    MENUNGGU_BAYAR → DIBAYAR (bayar)
    MENUNGGU_BAYAR → DIBATALKAN (batal)
    DIBAYAR → DIKIRIM (kirim)
    DIBAYAR → REFUND (batal)
    DIKIRIM → SELESAI (terima)
    SELESAI → KOMPLAIN (komplain)

  Transisi INVALID (harus ditolak):
    MENUNGGU_BAYAR → DIKIRIM (tidak bisa kirim sebelum bayar)
    DIKIRIM → DIBATALKAN (tidak bisa batal setelah kirim)
    SELESAI → MENUNGGU_BAYAR (tidak bisa kembali ke awal)
```

```python
from enum import Enum

class StatusPesanan(Enum):
    MENUNGGU_BAYAR = "menunggu_bayar"
    DIBAYAR = "dibayar"
    DIKIRIM = "dikirim"
    SELESAI = "selesai"
    DIBATALKAN = "dibatalkan"
    REFUND = "refund"
    KOMPLAIN = "komplain"

class Pesanan:
    TRANSISI_VALID = {
        StatusPesanan.MENUNGGU_BAYAR: [StatusPesanan.DIBAYAR, StatusPesanan.DIBATALKAN],
        StatusPesanan.DIBAYAR: [StatusPesanan.DIKIRIM, StatusPesanan.REFUND],
        StatusPesanan.DIKIRIM: [StatusPesanan.SELESAI],
        StatusPesanan.SELESAI: [StatusPesanan.KOMPLAIN],
    }

    def __init__(self):
        self.status = StatusPesanan.MENUNGGU_BAYAR

    def ubah_status(self, status_baru):
        valid = self.TRANSISI_VALID.get(self.status, [])
        if status_baru not in valid:
            raise ValueError(
                f"Transisi dari {self.status.value} ke {status_baru.value} tidak valid"
            )
        self.status = status_baru

# State transition tests
class TestStatePesanan:
    def test_transisi_valid_bayar(self):
        p = Pesanan()
        p.ubah_status(StatusPesanan.DIBAYAR)
        assert p.status == StatusPesanan.DIBAYAR

    def test_transisi_valid_kirim(self):
        p = Pesanan()
        p.ubah_status(StatusPesanan.DIBAYAR)
        p.ubah_status(StatusPesanan.DIKIRIM)
        assert p.status == StatusPesanan.DIKIRIM

    def test_transisi_invalid_kirim_tanpa_bayar(self):
        p = Pesanan()
        with pytest.raises(ValueError, match="tidak valid"):
            p.ubah_status(StatusPesanan.DIKIRIM)

    def test_transisi_invalid_batal_setelah_kirim(self):
        p = Pesanan()
        p.ubah_status(StatusPesanan.DIBAYAR)
        p.ubah_status(StatusPesanan.DIKIRIM)
        with pytest.raises(ValueError, match="tidak valid"):
            p.ubah_status(StatusPesanan.DIBATALKAN)
```

### 8.3.5 Perbandingan Teknik Test Case Design

| Teknik | Kapan Digunakan | Kekuatan | Kelemahan |
|--------|----------------|----------|-----------|
| **Equivalence Partitioning** | Input bisa dibagi ke kelas-kelas | Mengurangi jumlah test case | Bisa miss boundary bugs |
| **Boundary Value Analysis** | Ada batasan numerik/range | Efektif menemukan off-by-one bugs | Hanya untuk tipe data ordered |
| **Decision Table** | Banyak kombinasi kondisi bisnis | Komprehensif untuk logika kompleks | Jumlah test case bisa meledak (2^n) |
| **State Transition** | Sistem memiliki state/lifecycle | Menangkap transisi ilegal | Sulit untuk state yang sangat banyak |

> **Best Practice:** Kombinasikan teknik-teknik ini. Gunakan EP + BVA untuk input numerik, Decision Table untuk logika bisnis, dan State Transition untuk objek dengan lifecycle.

---

## 8.4 Terminologi Testing yang Wajib Dipahami

Sebelum masuk ke implementasi, pahami istilah-istilah kunci berikut:

| Istilah | Definisi | Analogi |
|---------|----------|---------|
| **SUT** (System Under Test) | Komponen yang sedang di-test | "Pasien" yang sedang diperiksa |
| **Test Case** | Skenario spesifik dengan input dan expected output | Satu "pertanyaan ujian" |
| **Test Suite** | Kumpulan test cases yang terkait | Satu "kertas ujian" |
| **Fixture** | Setup/teardown data yang dibutuhkan test | Menyiapkan ruang kelas sebelum ujian |
| **Mock** | Objek tiruan yang meniru perilaku dependency | "Stuntman" pengganti aktor asli |
| **Stub** | Implementasi sederhana yang mengembalikan nilai tetap | Mesin ATM demo yang selalu berhasil |
| **Spy** | Seperti mock, tapi juga merekam bagaimana dipanggil | CCTV yang merekam interaksi |
| **Assertion** | Pernyataan yang memverifikasi expected vs actual | Jawaban kunci ujian |
| **Code Coverage** | Persentase kode yang dieksekusi oleh test | Berapa persen materi yang diujikan |
| **Regression** | Memastikan fitur lama tidak rusak oleh perubahan | Cek ulang semua lantai setelah renovasi |

### Mock vs Stub vs Spy — Kapan Menggunakan Apa?

```
  ┌─────────────────────────────────────────────────────────────────┐
  │                                                                 │
  │  STUB: "Kalau ditanya, jawab X"                                │
  │  ┌─────────────────────────────────────────────┐               │
  │  │ fake_bank.get_saldo = lambda: 1_000_000     │               │
  │  │ → Selalu return Rp 1 juta, tidak peduli     │               │
  │  │   bagaimana dipanggil                        │               │
  │  └─────────────────────────────────────────────┘               │
  │                                                                 │
  │  MOCK: "Harus dipanggil dengan cara tertentu"                  │
  │  ┌─────────────────────────────────────────────┐               │
  │  │ mock_email.send.assert_called_once_with(     │               │
  │  │     to="user@mail.com", subject="Notif"     │               │
  │  │ )                                            │               │
  │  │ → Verifikasi CARA pemanggilan                │               │
  │  └─────────────────────────────────────────────┘               │
  │                                                                 │
  │  SPY: "Catat semua, tapi tetap jalankan aslinya"               │
  │  ┌─────────────────────────────────────────────┐               │
  │  │ spy_logger = mocker.spy(logger, 'info')     │               │
  │  │ → Fungsi asli tetap jalan, tapi tercatat    │               │
  │  │   berapa kali dan dengan parameter apa      │               │
  │  └─────────────────────────────────────────────┘               │
  │                                                                 │
  └─────────────────────────────────────────────────────────────────┘
```

---

## 8.5 Tutorial Lengkap pytest (Python)

pytest adalah framework testing Python yang paling populer karena syntax-nya yang sederhana dan fitur yang powerful.

### 8.5.1 Instalasi dan Struktur Proyek

```bash
# Instalasi di GitHub Codespaces
pip install pytest pytest-cov pytest-mock

# Struktur proyek yang direkomendasikan
perpustakaan-app/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── buku_service.py
│   │   └── peminjaman_service.py
│   └── utils/
│       ├── __init__.py
│       └── validators.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Shared fixtures
│   ├── unit/
│   │   ├── __init__.py
│   │   ├── test_validators.py
│   │   └── test_buku_service.py
│   └── integration/
│       ├── __init__.py
│       └── test_api_buku.py
├── pytest.ini
└── requirements.txt
```

```ini
# pytest.ini — Konfigurasi pytest
[pytest]
testpaths = tests
python_files = test_*.py
python_functions = test_*
python_classes = Test*
markers =
    slow: marks tests as slow
    integration: marks integration tests
addopts = -v --tb=short
```

### 8.5.2 Dasar-Dasar pytest

```python
# tests/unit/test_validators.py
"""Unit tests untuk modul validators."""
import pytest
from app.utils.validators import (
    validate_email,
    validate_isbn,
    validate_nomor_telepon,
)


# --- Test sederhana dengan assert ---
def test_email_valid():
    assert validate_email("mahasiswa@uai.ac.id") is True

def test_email_tanpa_at():
    assert validate_email("mahasiswauai.ac.id") is False

def test_email_kosong():
    assert validate_email("") is False


# --- Test exception handling ---
def test_isbn_none_raises_error():
    with pytest.raises(TypeError, match="ISBN tidak boleh None"):
        validate_isbn(None)


# --- Test dengan pesan kustom ---
def test_nomor_telepon_indonesia():
    assert validate_nomor_telepon("08123456789") is True, \
        "Nomor HP Indonesia format 08xx harus valid"

def test_nomor_telepon_kode_negara():
    assert validate_nomor_telepon("+628123456789") is True, \
        "Nomor HP format +62 harus valid"
```

### 8.5.3 Fixtures — Setup dan Teardown

Fixtures menyediakan data dan objek yang dibutuhkan oleh test. Ini menghindari duplikasi kode setup.

```python
# tests/conftest.py — Shared fixtures untuk semua tests
import pytest
from dataclasses import dataclass
from typing import List


@dataclass
class Buku:
    judul: str
    penulis: str
    isbn: str = ""
    stok: int = 0
    harga: int = 0


class BukuService:
    def __init__(self):
        self._buku: List[Buku] = []

    def tambah(self, buku: Buku):
        self._buku.append(buku)

    def search(self, keyword: str) -> List[Buku]:
        return [b for b in self._buku if keyword.lower() in b.judul.lower()]

    def get_by_isbn(self, isbn: str) -> Buku:
        for b in self._buku:
            if b.isbn == isbn:
                return b
        return None

    def total_koleksi(self) -> int:
        return len(self._buku)


# --- Fixture sederhana ---
@pytest.fixture
def sample_buku():
    """Fixture: satu buku untuk testing."""
    return Buku(
        judul="Algoritma dan Pemrograman",
        penulis="Ahmad Fauzi",
        isbn="978-602-1234-56-7",
        stok=10,
        harga=85_000
    )


# --- Fixture dengan setup data ---
@pytest.fixture
def buku_service_dengan_data():
    """Fixture: BukuService dengan 3 buku sampel."""
    service = BukuService()
    service.tambah(Buku(judul="Clean Code", penulis="Robert Martin",
                        isbn="978-0-13-235088-4", stok=5, harga=350_000))
    service.tambah(Buku(judul="Design Patterns", penulis="GoF",
                        isbn="978-0-201-63361-0", stok=3, harga=420_000))
    service.tambah(Buku(judul="Refactoring", penulis="Martin Fowler",
                        isbn="978-0-134-75759-9", stok=7, harga=380_000))
    return service


# --- Fixture dengan teardown (yield) ---
@pytest.fixture
def temp_database(tmp_path):
    """Fixture: database sementara yang dihapus setelah test."""
    db_path = tmp_path / "test.db"
    # Setup
    import sqlite3
    conn = sqlite3.connect(str(db_path))
    conn.execute("CREATE TABLE buku (id INTEGER PRIMARY KEY, judul TEXT)")
    conn.commit()

    yield conn  # Test berjalan di sini

    # Teardown — otomatis dipanggil setelah test selesai
    conn.close()
```

```python
# tests/unit/test_buku_service.py
"""Unit tests untuk BukuService menggunakan fixtures."""

def test_search_buku_ditemukan(buku_service_dengan_data):
    hasil = buku_service_dengan_data.search("Clean")
    assert len(hasil) == 1
    assert hasil[0].judul == "Clean Code"

def test_search_buku_tidak_ditemukan(buku_service_dengan_data):
    hasil = buku_service_dengan_data.search("xyz")
    assert len(hasil) == 0

def test_search_case_insensitive(buku_service_dengan_data):
    hasil = buku_service_dengan_data.search("clean code")
    assert len(hasil) == 1

def test_total_koleksi(buku_service_dengan_data):
    assert buku_service_dengan_data.total_koleksi() == 3

def test_get_by_isbn(buku_service_dengan_data):
    buku = buku_service_dengan_data.get_by_isbn("978-0-13-235088-4")
    assert buku is not None
    assert buku.judul == "Clean Code"

def test_stok_buku(sample_buku):
    assert sample_buku.stok == 10
    assert sample_buku.harga == 85_000
```

### 8.5.4 Parametrize — Satu Test, Banyak Data

`@pytest.mark.parametrize` memungkinkan menjalankan test yang sama dengan berbagai input/output tanpa duplikasi kode.

```python
# Test parametrize untuk validasi nomor telepon Indonesia
@pytest.mark.parametrize("nomor, expected", [
    ("08123456789",    True),   # Format 08xx
    ("+628123456789",  True),   # Format +62
    ("628123456789",   True),   # Format 62 tanpa +
    ("0812345",        False),  # Terlalu pendek
    ("08123456789012", False),  # Terlalu panjang
    ("12345678901",    False),  # Tidak dimulai 0/+62
    ("",               False),  # Kosong
    ("08xx-invalid",   False),  # Mengandung huruf
])
def test_validate_nomor_telepon(nomor, expected):
    assert validate_nomor_telepon(nomor) == expected


# Test parametrize untuk hitung diskon (contoh Tokopedia-style)
@pytest.mark.parametrize("total, kode_voucher, expected_diskon", [
    (100_000,   None,         0),        # Di bawah minimum, tanpa voucher
    (200_000,   "DISKON10",   20_000),   # 10% diskon
    (500_000,   "DISKON10",   50_000),   # 10% diskon
    (1_000_000, "DISKON10",   100_000),  # 10% tapi max 100rb
    (200_000,   "EXPIRED",    0),        # Voucher expired
    (200_000,   "INVALID",    0),        # Voucher tidak valid
])
def test_hitung_diskon_voucher(total, kode_voucher, expected_diskon):
    result = hitung_diskon_voucher(total, kode_voucher)
    assert result == expected_diskon
```

### 8.5.5 Markers — Menandai dan Memfilter Test

```python
import pytest

# Marker untuk test yang lambat
@pytest.mark.slow
def test_proses_batch_1000_buku():
    """Test ini butuh waktu lama karena memproses 1000 data."""
    service = BukuService()
    for i in range(1000):
        service.tambah(Buku(judul=f"Buku {i}", penulis="Author"))
    assert service.total_koleksi() == 1000

# Marker untuk integration test
@pytest.mark.integration
def test_koneksi_database_real():
    """Butuh database PostgreSQL yang sedang berjalan."""
    pass

# Marker skip
@pytest.mark.skip(reason="Fitur belum diimplementasi")
def test_fitur_rekomendasi_buku():
    pass

# Marker skip bersyarat
@pytest.mark.skipif(
    not shutil.which("docker"),
    reason="Docker tidak terinstall"
)
def test_dengan_docker():
    pass
```

```bash
# Menjalankan test dengan filter marker
pytest -m "not slow"             # Skip test lambat
pytest -m "integration"          # Hanya integration tests
pytest -m "not integration"      # Hanya unit tests
pytest -k "test_search"          # Filter berdasarkan nama
```

### 8.5.6 Mocking — Mengisolasi Dependencies

```python
from unittest.mock import patch, MagicMock

# Contoh: PeminjamanService yang bergantung pada EmailService
class PeminjamanService:
    def __init__(self, email_service, buku_repo):
        self.email_service = email_service
        self.buku_repo = buku_repo

    def pinjam(self, user_email, buku_id):
        buku = self.buku_repo.get(buku_id)
        if buku is None:
            raise ValueError("Buku tidak ditemukan")
        if buku.stok <= 0:
            raise ValueError("Stok habis")

        buku.stok -= 1
        self.buku_repo.save(buku)
        self.email_service.send(
            to=user_email,
            subject="Peminjaman Berhasil",
            body=f"Anda meminjam: {buku.judul}"
        )
        return True


# Test dengan mock — mengisolasi dari email dan database
class TestPeminjamanService:
    def test_pinjam_berhasil(self, sample_buku):
        # Arrange — siapkan mock
        mock_email = MagicMock()
        mock_repo = MagicMock()
        mock_repo.get.return_value = sample_buku  # Stub: return buku

        service = PeminjamanService(mock_email, mock_repo)

        # Act
        result = service.pinjam("mhs@uai.ac.id", "isbn-123")

        # Assert
        assert result is True
        assert sample_buku.stok == 9  # Stok berkurang
        mock_repo.save.assert_called_once()  # Verify save dipanggil
        mock_email.send.assert_called_once_with(
            to="mhs@uai.ac.id",
            subject="Peminjaman Berhasil",
            body="Anda meminjam: Algoritma dan Pemrograman"
        )

    def test_pinjam_buku_tidak_ada(self):
        mock_email = MagicMock()
        mock_repo = MagicMock()
        mock_repo.get.return_value = None  # Stub: buku tidak ada

        service = PeminjamanService(mock_email, mock_repo)

        with pytest.raises(ValueError, match="tidak ditemukan"):
            service.pinjam("mhs@uai.ac.id", "isbn-999")

        # Verify email TIDAK terkirim
        mock_email.send.assert_not_called()

    def test_pinjam_stok_habis(self):
        mock_email = MagicMock()
        mock_repo = MagicMock()
        buku_habis = Buku(judul="Buku Habis", penulis="X", stok=0)
        mock_repo.get.return_value = buku_habis

        service = PeminjamanService(mock_email, mock_repo)

        with pytest.raises(ValueError, match="Stok habis"):
            service.pinjam("mhs@uai.ac.id", "isbn-123")
```

### 8.5.7 Menjalankan dan Membaca Hasil Test

```bash
# Jalankan semua test
pytest

# Jalankan dengan output verbose
pytest -v

# Jalankan test tertentu
pytest tests/unit/test_buku_service.py
pytest tests/unit/test_buku_service.py::test_search_buku_ditemukan

# Jalankan dengan coverage report
pytest --cov=app --cov-report=term-missing tests/

# Output contoh coverage:
# Name                          Stmts   Miss  Cover   Missing
# -----------------------------------------------------------
# app/__init__.py                   0      0   100%
# app/models.py                    15      0   100%
# app/services/buku_service.py     22      2    91%   35-36
# app/utils/validators.py          18      3    83%   22, 28-29
# -----------------------------------------------------------
# TOTAL                            55      5    91%

# Generate HTML coverage report
pytest --cov=app --cov-report=html tests/
# Buka htmlcov/index.html di browser
```

---

## 8.6 Tutorial Jest (JavaScript)

Jest adalah framework testing JavaScript yang populer, terutama untuk proyek Node.js dan React.

### 8.6.1 Instalasi dan Setup

```bash
# Instalasi di GitHub Codespaces
npm init -y
npm install --save-dev jest

# Tambahkan script di package.json
# "scripts": { "test": "jest --verbose" }
```

```
# Struktur proyek JavaScript
perpustakaan-app/
├── src/
│   ├── buku-service.js
│   ├── validators.js
│   └── peminjaman-service.js
├── tests/
│   ├── buku-service.test.js
│   ├── validators.test.js
│   └── peminjaman-service.test.js
├── package.json
└── jest.config.js
```

### 8.6.2 Dasar-Dasar Jest

```javascript
// src/validators.js
function validateEmail(email) {
  if (!email || typeof email !== 'string') return false;
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}

function hitungDiskon(totalBelanja, persenDiskon) {
  if (totalBelanja < 0) throw new Error('Total belanja tidak boleh negatif');
  if (persenDiskon < 0 || persenDiskon > 100) {
    throw new Error('Persen diskon harus antara 0-100');
  }
  return totalBelanja * persenDiskon / 100;
}

module.exports = { validateEmail, hitungDiskon };
```

```javascript
// tests/validators.test.js
const { validateEmail, hitungDiskon } = require('../src/validators');

// --- describe: mengelompokkan test terkait ---
describe('validateEmail', () => {
  // --- test/it: satu test case ---
  test('mengembalikan true untuk email valid', () => {
    expect(validateEmail('mahasiswa@uai.ac.id')).toBe(true);
  });

  test('mengembalikan false untuk email tanpa @', () => {
    expect(validateEmail('mahasiswauai.ac.id')).toBe(false);
  });

  test('mengembalikan false untuk string kosong', () => {
    expect(validateEmail('')).toBe(false);
  });

  test('mengembalikan false untuk null', () => {
    expect(validateEmail(null)).toBe(false);
  });
});

describe('hitungDiskon', () => {
  test('menghitung diskon dengan benar', () => {
    expect(hitungDiskon(100000, 10)).toBe(10000);
  });

  test('diskon 0% menghasilkan 0', () => {
    expect(hitungDiskon(100000, 0)).toBe(0);
  });

  test('melempar error untuk total negatif', () => {
    expect(() => hitungDiskon(-50000, 10)).toThrow('tidak boleh negatif');
  });

  test('melempar error untuk diskon > 100%', () => {
    expect(() => hitungDiskon(100000, 150)).toThrow('antara 0-100');
  });
});
```

### 8.6.3 Jest Matchers

```javascript
// Perbandingan matcher Jest yang sering digunakan
describe('Jest Matchers Cheat Sheet', () => {
  // Equality
  test('toBe — strict equality (===)', () => {
    expect(2 + 2).toBe(4);
  });

  test('toEqual — deep equality untuk objek', () => {
    const buku = { judul: 'Clean Code', penulis: 'Martin' };
    expect(buku).toEqual({ judul: 'Clean Code', penulis: 'Martin' });
  });

  // Truthiness
  test('toBeTruthy / toBeFalsy', () => {
    expect('ada isi').toBeTruthy();
    expect('').toBeFalsy();
    expect(null).toBeFalsy();
  });

  // Numbers
  test('toBeGreaterThan / toBeLessThan', () => {
    expect(100000).toBeGreaterThan(50000);
    expect(3.14).toBeCloseTo(22 / 7, 1);  // Approx
  });

  // Strings
  test('toMatch — regex matching', () => {
    expect('Universitas Al Azhar Indonesia').toMatch(/Al Azhar/);
  });

  // Arrays
  test('toContain — array contains', () => {
    const jurusan = ['Informatika', 'Sistem Informasi', 'Teknik Elektro'];
    expect(jurusan).toContain('Informatika');
    expect(jurusan).toHaveLength(3);
  });

  // Exceptions
  test('toThrow — exception handling', () => {
    expect(() => { throw new Error('gagal'); }).toThrow('gagal');
  });
});
```

### 8.6.4 Jest Mocking

```javascript
// src/peminjaman-service.js
class PeminjamanService {
  constructor(bukuRepo, emailService) {
    this.bukuRepo = bukuRepo;
    this.emailService = emailService;
  }

  async pinjam(userId, bukuId) {
    const buku = await this.bukuRepo.findById(bukuId);
    if (!buku) throw new Error('Buku tidak ditemukan');
    if (buku.stok <= 0) throw new Error('Stok habis');

    buku.stok -= 1;
    await this.bukuRepo.save(buku);
    await this.emailService.send(userId, `Peminjaman ${buku.judul} berhasil`);

    return { success: true, buku: buku.judul };
  }
}

module.exports = PeminjamanService;
```

```javascript
// tests/peminjaman-service.test.js
const PeminjamanService = require('../src/peminjaman-service');

describe('PeminjamanService', () => {
  let mockBukuRepo;
  let mockEmailService;
  let service;

  // beforeEach: dijalankan sebelum SETIAP test
  beforeEach(() => {
    mockBukuRepo = {
      findById: jest.fn(),
      save: jest.fn(),
    };
    mockEmailService = {
      send: jest.fn(),
    };
    service = new PeminjamanService(mockBukuRepo, mockEmailService);
  });

  test('peminjaman berhasil mengurangi stok', async () => {
    // Arrange
    const buku = { judul: 'Clean Code', stok: 5 };
    mockBukuRepo.findById.mockResolvedValue(buku);
    mockBukuRepo.save.mockResolvedValue(true);
    mockEmailService.send.mockResolvedValue(true);

    // Act
    const result = await service.pinjam('user-1', 'buku-1');

    // Assert
    expect(result.success).toBe(true);
    expect(buku.stok).toBe(4);
    expect(mockBukuRepo.save).toHaveBeenCalledWith(buku);
    expect(mockEmailService.send).toHaveBeenCalledTimes(1);
  });

  test('melempar error jika buku tidak ditemukan', async () => {
    mockBukuRepo.findById.mockResolvedValue(null);

    await expect(service.pinjam('user-1', 'buku-999'))
      .rejects.toThrow('Buku tidak ditemukan');

    expect(mockEmailService.send).not.toHaveBeenCalled();
  });

  test('melempar error jika stok habis', async () => {
    mockBukuRepo.findById.mockResolvedValue({ judul: 'Buku', stok: 0 });

    await expect(service.pinjam('user-1', 'buku-1'))
      .rejects.toThrow('Stok habis');
  });
});
```

### 8.6.5 Perbandingan pytest vs Jest

| Aspek | pytest (Python) | Jest (JavaScript) |
|-------|----------------|-------------------|
| **Assertion** | `assert x == y` | `expect(x).toBe(y)` |
| **Exception** | `with pytest.raises(Error):` | `expect(() => ...).toThrow()` |
| **Setup/Teardown** | `@pytest.fixture` | `beforeEach()` / `afterEach()` |
| **Mocking** | `unittest.mock.MagicMock` | `jest.fn()` |
| **Parametrize** | `@pytest.mark.parametrize` | `test.each([...])` |
| **Async** | `@pytest.mark.asyncio` | `async/await` langsung |
| **Coverage** | `pytest-cov` | `jest --coverage` (built-in) |
| **Grouping** | File / class | `describe()` blocks |

---

## 8.7 Test Organization Patterns — AAA (Arrange-Act-Assert)

Pattern AAA adalah standar de facto untuk menulis test yang bersih dan mudah dibaca.

### 8.7.1 Struktur AAA

```
  ┌─────────────────────────────────────────────────┐
  │  ARRANGE (Persiapan)                            │
  │  - Siapkan objek yang dibutuhkan                │
  │  - Setup mock/stub                              │
  │  - Siapkan data input                           │
  ├─────────────────────────────────────────────────┤
  │  ACT (Aksi)                                     │
  │  - Panggil method/fungsi yang ditest            │
  │  - HANYA SATU aksi utama per test               │
  ├─────────────────────────────────────────────────┤
  │  ASSERT (Verifikasi)                            │
  │  - Verifikasi hasil sesuai ekspektasi           │
  │  - Cek side effects (mock calls, state change)  │
  └─────────────────────────────────────────────────┘
```

### 8.7.2 Contoh AAA dalam Python

```python
def test_transfer_antar_rekening():
    """Test transfer BCA antar rekening (contoh banking Indonesia)."""
    # ARRANGE — Siapkan rekening pengirim dan penerima
    pengirim = Rekening(nomor="1234567890", saldo=1_000_000)
    penerima = Rekening(nomor="0987654321", saldo=500_000)
    bank_service = BankService()

    # ACT — Lakukan transfer
    result = bank_service.transfer(
        dari=pengirim,
        ke=penerima,
        jumlah=300_000
    )

    # ASSERT — Verifikasi hasil
    assert result.sukses is True
    assert pengirim.saldo == 700_000       # Saldo pengirim berkurang
    assert penerima.saldo == 800_000       # Saldo penerima bertambah
    assert result.referensi is not None    # Ada nomor referensi
```

### 8.7.3 Contoh AAA dalam JavaScript

```javascript
test('transfer antar rekening berhasil', () => {
  // ARRANGE
  const pengirim = { nomor: '1234567890', saldo: 1000000 };
  const penerima = { nomor: '0987654321', saldo: 500000 };
  const bankService = new BankService();

  // ACT
  const result = bankService.transfer(pengirim, penerima, 300000);

  // ASSERT
  expect(result.sukses).toBe(true);
  expect(pengirim.saldo).toBe(700000);
  expect(penerima.saldo).toBe(800000);
  expect(result.referensi).toBeDefined();
});
```

### 8.7.4 Anti-Patterns dalam Testing

| Anti-Pattern | Masalah | Solusi |
|-------------|---------|--------|
| **Test yang terlalu besar** | Sulit di-debug saat gagal | Satu test = satu assertion logis |
| **Test saling bergantung** | Urutan eksekusi mempengaruhi hasil | Setiap test harus independent |
| **Magic numbers** | Tidak jelas kenapa nilainya segitu | Gunakan konstanta yang bermakna |
| **Testing implementation** | Test patah saat refactor | Test behavior, bukan implementasi |
| **No assertion** | Test selalu "pass" tanpa verifikasi | Setiap test HARUS punya assert |
| **Flaky tests** | Kadang pass, kadang fail | Hindari dependency ke waktu, random, network |

```python
# BURUK — testing implementation (terikat ke cara implementasi)
def test_search_buruk(buku_service):
    buku_service.search("Clean")
    assert buku_service._buku is not None  # Akses private attribute

# BAIK — testing behavior (hanya cek perilaku yang diharapkan)
def test_search_baik(buku_service):
    hasil = buku_service.search("Clean")
    assert len(hasil) == 1
    assert hasil[0].judul == "Clean Code"
```

---

## 8.8 Studi Kasus Komprehensif: Testing Sistem Transfer Bank

Bayangkan Anda diminta menguji modul transfer uang untuk aplikasi mobile banking Bank Mandiri. Berikut pendekatan testing komprehensif menggunakan semua teknik yang dipelajari.

### Spesifikasi Bisnis:

```
Transfer antar rekening Mandiri:
- Minimum transfer: Rp 10.000
- Maksimum transfer per transaksi: Rp 250.000.000
- Saldo minimum tersisa: Rp 50.000
- Biaya admin: Rp 0 (sesama Mandiri)
- Jam operasional: 24/7
- Validasi: PIN 6 digit, nomor rekening 13 digit
```

### 8.8.1 Equivalence Partitioning

```python
# Test cases EP untuk jumlah transfer
@pytest.mark.parametrize("jumlah, expected", [
    (-100_000,       "error"),    # EP1: Negatif (invalid)
    (5_000,          "error"),    # EP2: Di bawah minimum (invalid)
    (100_000,        "success"),  # EP3: Dalam range valid
    (300_000_000,    "error"),    # EP4: Di atas maksimum (invalid)
])
def test_ep_transfer(jumlah, expected):
    result = transfer_service.transfer(
        pengirim="1234567890123",
        penerima="9876543210987",
        jumlah=jumlah,
        pin="123456"
    )
    assert result.status == expected
```

### 8.8.2 Boundary Value Analysis

```python
# Test cases BVA untuk jumlah transfer
@pytest.mark.parametrize("jumlah, expected", [
    (9_999,           "error"),    # Tepat di bawah minimum
    (10_000,          "success"),  # Batas bawah minimum (valid)
    (10_001,          "success"),  # Tepat di atas minimum
    (249_999_999,     "success"),  # Tepat di bawah maksimum
    (250_000_000,     "success"),  # Batas atas maksimum (valid)
    (250_000_001,     "error"),    # Tepat di atas maksimum
])
def test_bva_transfer(jumlah, expected):
    result = transfer_service.transfer(
        pengirim="1234567890123",
        penerima="9876543210987",
        jumlah=jumlah,
        pin="123456"
    )
    assert result.status == expected
```

### 8.8.3 Decision Table

```python
# Decision table: kombinasi kondisi transfer
@pytest.mark.parametrize("saldo_cukup, pin_valid, rek_valid, expected", [
    (True,  True,  True,  "success"),     # Semua valid
    (True,  True,  False, "error_rek"),    # Rekening tidak valid
    (True,  False, True,  "error_pin"),    # PIN salah
    (False, True,  True,  "error_saldo"), # Saldo tidak cukup
    (False, False, False, "error_pin"),    # Multiple errors (PIN prioritas)
])
def test_decision_table_transfer(saldo_cukup, pin_valid, rek_valid, expected):
    # Setup sesuai kondisi ...
    pass
```

### 8.8.4 State Transition

```python
# State transition: status transaksi transfer
def test_transfer_state_flow():
    """Test alur state: INITIATED → VALIDATED → PROCESSED → COMPLETED"""
    trx = Transfer(pengirim="123", penerima="456", jumlah=100_000)
    assert trx.status == "INITIATED"

    trx.validate(pin="123456")
    assert trx.status == "VALIDATED"

    trx.process()
    assert trx.status == "PROCESSED"

    trx.complete()
    assert trx.status == "COMPLETED"

def test_transfer_state_gagal_validasi():
    """Test: INITIATED → FAILED (pin salah)"""
    trx = Transfer(pengirim="123", penerima="456", jumlah=100_000)
    trx.validate(pin="wrong")
    assert trx.status == "FAILED"
    assert trx.error == "PIN tidak valid"
```

> **Catatan:** Studi kasus ini menunjukkan bagaimana keempat teknik test design saling melengkapi untuk menghasilkan test suite yang komprehensif.

---

## 8.9 AI Corner: AI untuk Software Testing (Level: Advanced)

### 8.9.1 AI untuk Generate Test Cases

```
PROMPT:
"Buatkan pytest test cases untuk fungsi berikut, termasuk happy path,
edge cases, error handling, dan boundary values:

def validate_transfer(jumlah, saldo, pin):
    if not isinstance(pin, str) or len(pin) != 6:
        raise ValueError('PIN harus 6 digit')
    if jumlah < 10000:
        raise ValueError('Minimum transfer Rp 10.000')
    if jumlah > saldo - 50000:
        raise ValueError('Saldo tidak mencukupi')
    return True"
```

**Evaluasi output AI:** Periksa apakah AI mencakup:
- Happy path (transfer normal berhasil)
- Boundary: jumlah = 10000, jumlah = saldo - 50000
- Error: PIN kurang dari 6 digit, PIN bukan string
- Edge case: saldo tepat = jumlah + 50000

### 8.9.2 AI untuk Identifikasi Test Coverage Gaps

```
PROMPT:
"Analisis kode berikut dan identifikasi test cases yang belum
di-cover oleh test suite saya. Berikut kodenya:
[paste production code]

Berikut test suite yang ada:
[paste test code]

Apa saja gaps-nya?"
```

### 8.9.3 AI untuk Test Data Generation

```
PROMPT:
"Generate test data untuk Equivalence Partitioning dan Boundary
Value Analysis pada fungsi validasi nomor KTP Indonesia (NIK 16 digit).
Sertakan kode provinsi valid, tanggal lahir, dan nomor urut.
Format: tabel dengan kolom Input, Partisi, Expected Result."
```

### 8.9.4 AI untuk Refactor Test Code

```
PROMPT:
"Refactor test suite berikut agar menggunakan pytest fixtures
dan @pytest.mark.parametrize untuk mengurangi duplikasi:
[paste test code with duplication]"
```

### 8.9.5 Evaluasi Kritis terhadap AI-Generated Tests

| Aspek | AI Kuat | AI Lemah |
|-------|---------|----------|
| Happy path coverage | Sangat baik | — |
| Boundary values | Baik jika diminta eksplisit | Sering miss jika tidak diminta |
| Business logic context | — | Tidak paham aturan bisnis OJK |
| Integration scenarios | — | Sulit tanpa arsitektur lengkap |
| Security edge cases | Basic (SQL injection, XSS) | Advanced penetration testing |
| Indonesian context | — | Perlu guidance spesifik (format NIK, NPWP) |

### 8.9.6 Hands-On: Coba dan Evaluasi

**Aktivitas:**
1. Tulis fungsi `hitung_pajak_pph21(penghasilan_bruto)` berdasarkan bracket pajak Indonesia
2. Minta AI generate test cases untuk fungsi tersebut
3. Evaluasi: apakah AI memahami bracket pajak progresif Indonesia?
4. Tambahkan test cases yang di-miss oleh AI
5. Refleksi: di mana AI membantu vs di mana human expertise diperlukan?

> **Etika AI:** Gunakan AI sebagai *pair testing partner*, bukan pengganti pemikiran kritis. Selalu review dan validasi AI-generated tests terhadap business requirements yang sebenarnya. Dalam konteks perbankan Indonesia (BCA, Mandiri, BRI), regulasi OJK mengharuskan testing yang sangat ketat — AI harus diawasi oleh human tester yang memahami regulasi.

---

## Latihan Soal

### Level Dasar (C1-C2) — 6 Soal

1. Jelaskan empat level testing (unit, integration, system, acceptance) beserta contoh masing-masing. Siapa yang bertanggung jawab di setiap level?

2. Gambarkan dan jelaskan V-Model testing. Bagaimana setiap fase development berkorespondensi dengan fase testing?

3. Jelaskan perbedaan antara mock, stub, dan spy. Berikan contoh skenario kapan masing-masing digunakan.

4. Apa itu testing pyramid? Mengapa unit test harus paling banyak jumlahnya?

5. Jelaskan pola AAA (Arrange-Act-Assert) dalam penulisan test. Mengapa pola ini penting?

6. Sebutkan dan jelaskan empat teknik test case design yang dipelajari di bab ini.

### Level Menengah (C3-C4) — 7 Soal

7. Diberikan fungsi `validasi_nik(nik)` yang memvalidasi NIK Indonesia (16 digit, kode provinsi valid, tanggal lahir valid). Buatlah test cases menggunakan teknik Equivalence Partitioning. Identifikasi minimal 5 partisi.

8. Untuk fungsi `hitung_tarif_tol(golongan, jarak_km)` pada jalan tol di Indonesia, buatlah test cases menggunakan Boundary Value Analysis. Asumsikan:
   - Golongan I: Rp 500/km (min Rp 5.000)
   - Golongan II: Rp 750/km (min Rp 7.500)
   - Jarak minimum 1 km, maksimum 200 km

9. Buatlah decision table dan test cases untuk kebijakan pemberian kredit di bank Indonesia:
   - Kondisi: skor kredit (baik/buruk), penghasilan (>5jt/<5jt), agunan (ada/tidak)
   - Aksi: kredit disetujui/ditolak, bunga normal/tinggi

10. Implementasikan 5 unit tests menggunakan pytest untuk fungsi `validate_email(email)` yang memvalidasi format email. Gunakan `@pytest.mark.parametrize`.

11. Tulis integration test untuk endpoint Flask `POST /api/peminjaman` yang meminjamkan buku. Test harus mencakup: peminjaman berhasil, buku tidak ditemukan, stok habis.

12. Implementasikan test mocking untuk `NotifikasiService` yang bergantung pada `SMSGateway` dan `EmailGateway`. Pastikan test mengisolasi dependencies.

13. Tuliskan state transition test untuk lifecycle pesanan Tokopedia: CREATED -> PAID -> SHIPPED -> DELIVERED -> REVIEWED, termasuk test untuk transisi yang tidak valid.

### Level Mahir (C5-C6) — 7 Soal

14. Rancang strategi testing komprehensif untuk Sistem Antrian Puskesmas digital. Tentukan: (a) test cases per level (unit, integration, system, acceptance), (b) teknik test design yang digunakan, (c) prioritas testing.

15. Evaluasi pernyataan: "100% code coverage menjamin software bebas bug." Berikan minimal 3 argumen yang mendukung dan 3 yang menentang, dengan contoh kode.

16. Bandingkan pendekatan testing untuk dua skenario: (a) aplikasi e-commerce yang sering berubah fitur (Tokopedia), dan (b) sistem perbankan yang regulasinya ketat (BCA). Teknik mana yang lebih diprioritaskan di masing-masing?

17. Anda menerima legacy codebase Flask tanpa test sama sekali (0% coverage). Rancang strategi bertahap untuk menambahkan test — dari mana Anda memulai? Apa prioritas? Target coverage per bulan?

18. Analisis trade-off antara kecepatan development dan thoroughness of testing. Kapan Anda mengorbankan coverage demi kecepatan? Kapan sebaliknya? Berikan contoh industri di Indonesia.

19. Desain test suite untuk fitur "Transfer QRIS" (Quick Response Code Indonesian Standard) yang mencakup: EP, BVA, decision table, dan state transition. Pertimbangkan skenario offline dan timeout.

20. Evaluasi kekuatan dan kelemahan AI-assisted testing. Buatkan prompt engineering guide untuk 5 skenario testing berbeda, dan diskusikan kapan AI TIDAK boleh menggantikan human tester.

---

## Rangkuman

1. **Testing pyramid** mengajarkan proporsi ideal: banyak unit test (cepat, murah), sedikit E2E test (lambat, mahal). Google menggunakan rasio 70/20/10.

2. **V-Model** menunjukkan hubungan langsung antara setiap fase development dengan fase testing yang berkorespondensi.

3. **Empat level testing**: Unit (fungsi individual), Integration (antar komponen), System (seluruh sistem), Acceptance (kesesuaian requirements).

4. **Equivalence Partitioning** membagi domain input ke kelas-kelas ekuivalen untuk mengurangi jumlah test case tanpa mengorbankan efektivitas.

5. **Boundary Value Analysis** fokus pada batas antar partisi, di mana bug paling sering bersembunyi.

6. **Decision Table** efektif untuk kombinasi kondisi bisnis yang kompleks, sedangkan **State Transition** untuk objek dengan lifecycle.

7. **pytest** adalah framework testing Python yang powerful dengan fitur fixtures, parametrize, markers, dan mocking.

8. **Jest** adalah framework testing JavaScript dengan describe/test blocks, matchers, dan mocking via `jest.fn()`.

9. **AAA Pattern** (Arrange-Act-Assert) adalah standar penulisan test yang bersih: siapkan, lakukan, verifikasi.

10. **AI-assisted testing** membantu generate test cases, tetapi tetap memerlukan evaluasi manusia untuk business logic dan edge cases yang spesifik konteks.

---

## Referensi

1. Myers, G. J., Sandler, C., & Badgett, T. (2011). *The Art of Software Testing* (3rd ed.). Wiley.
2. Beck, K. (2003). *Test Driven Development: By Example*. Addison-Wesley.
3. pytest documentation. (2025). *pytest: helps you write better programs*. https://docs.pytest.org/
4. Jest documentation. (2025). *Jest: Delightful JavaScript Testing*. https://jestjs.io/
5. Sommerville, I. (2016). *Software Engineering* (10th ed.). Chapter 8: Software Testing. Pearson.
6. Copeland, L. (2004). *A Practitioner's Guide to Software Test Design*. Artech House.
7. ISTQB. (2023). *Certified Tester Foundation Level Syllabus v4.0*. International Software Testing Qualifications Board.
8. IEEE Computer Society. (2024). *SWEBOK v4* — Chapter 4: Software Testing. IEEE.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
