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
| **CPMK** | CPMK-6: Menerapkan praktik DevOps, CI/CD pipeline (GitHub Actions), containerization (Docker), cloud deployment, serta memahami software maintenance dan evolusi |
| **Sub-CPMK** | Sub-CPMK-6.3: Menganalisis technical debt dan menerapkan strategi refactoring yang aman (C4) |
| | Sub-CPMK-6.4: Menerapkan semantic versioning (SemVer) dan dependency management (C3) |
| **Durasi** | 150 menit (3 x 50 menit) |
| **Metode** | Ceramah interaktif, code analysis exercise, refactoring workshop |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Menganalisis** empat jenis software maintenance dan proporsi biayanya dalam lifecycle perangkat lunak (C4)
2. **Menjelaskan** Lehman's Laws of Software Evolution dan implikasinya pada proyek nyata (C2)
3. **Mengevaluasi** technical debt dalam codebase menggunakan debt quadrant dan memprioritaskan penanganannya (C5)
4. **Menerapkan** teknik refactoring: Extract Method, Rename, Replace Magic Number, Introduce Parameter Object (C3)
5. **Menganalisis** software metrics: cyclomatic complexity, coupling, cohesion, dan kaitannya dengan maintainability (C4)
6. **Menerapkan** Semantic Versioning (SemVer), dependency management, dan konsep SBOM dasar (C3)

---

## Materi Pembelajaran

### 12.1 Software Maintenance -- Fase Terpanjang dalam SDLC

Maintenance menghabiskan **60-80% total biaya** lifecycle perangkat lunak -- jauh lebih besar dari development awal. Ini adalah fakta yang sering diabaikan oleh developer pemula.

```
Distribusi Biaya Software Lifecycle:
+----------------+----------------------------------------------+
|  Development   |                 Maintenance                   |
|     20-40%     |                   60-80%                      |
|                +--------+----------+-----------+--------------+
| Analisis,      |Correct-| Adaptive |Perfective |  Preventive  |
| Design, Code,  |ive     |          |           |              |
| Test, Deploy   | ~20%   |  ~25%    |   ~50%    |    ~5%       |
+----------------+--------+----------+-----------+--------------+
```

#### Empat Jenis Maintenance

| Jenis | Deskripsi | Proporsi | Contoh Indonesia |
|-------|-----------|----------|-----------------|
| **Corrective** | Perbaikan bug/defect yang ditemukan | ~20% | Fix crash aplikasi Dana saat top-up gagal |
| **Adaptive** | Adaptasi ke lingkungan/platform baru | ~25% | Migrasi SIPKD dari Python 2 ke Python 3 |
| **Perfective** | Penambahan/peningkatan fitur baru | ~50% | Tokopedia menambah fitur live streaming |
| **Preventive** | Cegah masalah di masa depan | ~5% | Refactoring kode legacy Gojek, update dependencies |

```python
# Contoh: Kategorisasi maintenance tasks
from enum import Enum
from dataclasses import dataclass
from datetime import datetime

class MaintenanceType(Enum):
    CORRECTIVE = "corrective"    # Perbaikan bug
    ADAPTIVE = "adaptive"        # Adaptasi lingkungan
    PERFECTIVE = "perfective"    # Peningkatan fitur
    PREVENTIVE = "preventive"    # Pencegahan masalah

@dataclass
class MaintenanceTask:
    judul: str
    tipe: MaintenanceType
    prioritas: int  # 1 (tertinggi) - 5 (terendah)
    estimasi_jam: float
    tanggal_dibuat: datetime

# Contoh backlog maintenance untuk "Toko UMKM Online"
backlog = [
    MaintenanceTask(
        "Fix: Harga produk tampil Rp 0 saat stok habis",
        MaintenanceType.CORRECTIVE, 1, 2.0,
        datetime(2026, 4, 1)
    ),
    MaintenanceTask(
        "Migrasi database dari SQLite ke PostgreSQL",
        MaintenanceType.ADAPTIVE, 2, 16.0,
        datetime(2026, 4, 3)
    ),
    MaintenanceTask(
        "Tambah fitur ekspor laporan penjualan ke PDF",
        MaintenanceType.PERFECTIVE, 3, 8.0,
        datetime(2026, 4, 5)
    ),
    MaintenanceTask(
        "Update Flask dari 2.x ke 3.x + refactoring",
        MaintenanceType.PREVENTIVE, 4, 12.0,
        datetime(2026, 4, 7)
    ),
]

# Analisis distribusi maintenance
from collections import Counter
distribusi = Counter(task.tipe.value for task in backlog)
total_jam = sum(task.estimasi_jam for task in backlog)
print(f"Total estimasi maintenance: {total_jam} jam")
for tipe, count in distribusi.items():
    jam = sum(t.estimasi_jam for t in backlog if t.tipe.value == tipe)
    print(f"  {tipe}: {count} task ({jam:.0f} jam, {jam/total_jam*100:.0f}%)")
```

```
Output:
Total estimasi maintenance: 38.0 jam
  corrective: 1 task (2 jam, 5%)
  adaptive: 1 task (16 jam, 42%)
  perfective: 1 task (8 jam, 21%)
  preventive: 1 task (12 jam, 32%)
```

### 12.2 Lehman's Laws of Software Evolution

Menahem Lehman (1974-1996) merumuskan **8 hukum** yang menjelaskan bagaimana software berkembang di dunia nyata:

| # | Hukum | Deskripsi | Implikasi Praktis |
|---|-------|-----------|-------------------|
| 1 | **Continuing Change** | Software harus terus berubah atau menjadi usang | Alokasikan budget untuk maintenance |
| 2 | **Increasing Complexity** | Kompleksitas meningkat kecuali ada upaya menguranginya | Refactoring reguler wajib |
| 3 | **Self Regulation** | Evolusi software mengikuti pola yang dapat diprediksi | Gunakan metrics untuk tracking |
| 4 | **Conservation of Org. Stability** | Rata-rata laju kerja cenderung konstan | Jangan harap tim bisa terus percepat |
| 5 | **Conservation of Familiarity** | Perubahan per rilis harus terkendali | Rilis kecil lebih baik dari rilis besar |
| 6 | **Continuing Growth** | Fungsionalitas harus terus bertambah untuk memuaskan pengguna | Fitur baru = harapan pengguna |
| 7 | **Declining Quality** | Kualitas menurun kecuali ada adaptasi aktif | QA dan testing harus berkelanjutan |
| 8 | **Feedback System** | Evolusi software adalah proses feedback multi-level | Monitor, ukur, dan iterasi |

```
Visualisasi Lehman's Law #2 (Increasing Complexity):
       Kompleksitas
       ^
       |           /---- Tanpa refactoring
       |         /       (complexity grows)
       |       /
       |     / - - - -   Dengan refactoring berkala
       |   /             (complexity terkontrol)
       | /
       |/
       +-------------------------------> Waktu / Rilis
```

**Studi kasus Indonesia -- SIPKD (Sistem Informasi Pengelolaan Keuangan Daerah):**
- Dibangun awal 2010-an dengan teknologi .NET Framework
- Seiring waktu, fitur ditambah tanpa refactoring (Lehman #2: Increasing Complexity)
- Tahun 2020: kode sudah sangat kompleks, developer baru butuh 3+ bulan untuk onboarding
- Solusi: rewrite bertahap ke arsitektur microservices dengan teknologi modern

**Studi kasus -- MyPertamina:**
- Awalnya hanya untuk tracking subsidi BBM (Lehman #6: Continuing Growth)
- Pengguna menuntut fitur baru: pembayaran digital, loyalty points, lokasi SPBU
- Jika tidak berkembang, pengguna beralih ke aplikasi lain (Lehman #1: Continuing Change)

### 12.3 Technical Debt (Utang Teknis)

Technical debt adalah "jalan pintas" dalam kode yang mempercepat delivery jangka pendek tetapi menambah biaya jangka panjang -- seperti utang finansial yang menghasilkan bunga.

```
Analogi Technical Debt:
+--------------------------------------------------------+
|                                                        |
|  Utang Finansial:                                      |
|  Pinjam Rp 10 juta --> Bayar cicilan + bunga -->       |
|  Kalau tidak bayar --> Bunga makin besar! (compound)   |
|                                                        |
|  Technical Debt:                                       |
|  Ambil shortcut --> Kode makin sulit di-maintain -->    |
|  Kalau tidak refactor --> Development makin lambat!     |
|                                                        |
|  Kecepatan Dev                                         |
|  ^                                                     |
|  | \                                                   |
|  |   \---- Dengan tech debt (makin lambat)             |
|  |     \                                               |
|  |       \                                             |
|  |  ------- Dengan refactoring berkala (stabil)        |
|  +-------------------------------> Waktu               |
+--------------------------------------------------------+
```

#### Technical Debt Quadrant (Martin Fowler)

```
                  Deliberate (Sengaja)
                       |
            +----------+---------------+
            |          |               |
            | RECKLESS |   PRUDENT     |
            | & DELIB. |  & DELIB.     |
            |          |               |
            | "Kita    | "Kita harus   |
            |  tidak   |  deliver      |
            |  punya   |  sekarang,    |
            |  waktu   |  refactor     |
            |  untuk   |  sprint       |
            |  design" |  depan"       |
 Reckless --+----------+---------------+-- Prudent
            |          |               |
            | RECKLESS |   PRUDENT     |
            | & INADV. |  & INADV.     |
            |          |               |
            | "Apa itu | "Sekarang     |
            |  design  |  kita tahu    |
            |  pattern |  seharusnya   |
            |  ?"      |  begini"      |
            |          |               |
            +----------+---------------+
                       |
              Inadvertent (Tidak sengaja)
```

| Kuadran | Deskripsi | Penanganan |
|---------|-----------|------------|
| **Reckless & Deliberate** | Sengaja ambil shortcut, tahu risikonya | Hindari! Ini debt paling berbahaya |
| **Prudent & Deliberate** | Sadar trade-off, punya rencana bayar | Dokumentasikan, jadwalkan refactoring |
| **Reckless & Inadvertent** | Kurang pengetahuan, tidak sadar | Training tim, code review ketat |
| **Prudent & Inadvertent** | Baru sadar setelah implementasi | Normal dalam software evolution, perbaiki segera |

#### Gejala Technical Debt dalam Kode

```python
# ========================================
# CONTOH 1: Magic Numbers (angka tanpa nama)
# ========================================

# BURUK -- apa arti 0.11? Mengapa 50000?
def hitung_total(harga, qty):
    subtotal = harga * qty
    if subtotal > 50000:
        subtotal *= 0.95  # Apa ini?
    pajak = subtotal * 0.11  # Apa ini?
    ongkir = 15000 if subtotal < 100000 else 0  # Apa ini?
    return subtotal + pajak + ongkir

# BAIK -- gunakan named constants
TARIF_PPN = 0.11                    # PPN Indonesia per 2025
DISKON_BESAR = 0.05                 # Diskon 5% untuk pembelian besar
BATAS_DISKON = 50_000               # Min Rp 50.000 untuk diskon
BATAS_GRATIS_ONGKIR = 100_000       # Min Rp 100.000 gratis ongkir
BIAYA_ONGKIR_DEFAULT = 15_000       # Ongkir default Rp 15.000

def hitung_total(harga: float, qty: int) -> float:
    """Hitung total belanja termasuk PPN dan ongkir."""
    subtotal = harga * qty
    if subtotal > BATAS_DISKON:
        subtotal *= (1 - DISKON_BESAR)
    pajak = subtotal * TARIF_PPN
    ongkir = BIAYA_ONGKIR_DEFAULT if subtotal < BATAS_GRATIS_ONGKIR else 0
    return subtotal + pajak + ongkir
```

```python
# ========================================
# CONTOH 2: Long Method -- Extract Method
# ========================================

# BURUK -- satu fungsi melakukan terlalu banyak hal
def proses_pesanan(pesanan):
    # Validasi (10 baris)
    if not pesanan.items:
        raise ValueError("Pesanan kosong")
    for item in pesanan.items:
        if item.stok <= 0:
            raise ValueError(f"{item.nama} habis")
    
    # Hitung total (8 baris)
    subtotal = sum(i.harga * i.qty for i in pesanan.items)
    pajak = subtotal * 0.11
    total = subtotal + pajak
    
    # Update stok (5 baris)
    for item in pesanan.items:
        item.stok -= item.qty
    
    # Kirim notifikasi (5 baris)
    kirim_email(pesanan.email, f"Total: Rp {total:,.0f}")
    return total

# BAIK -- Extract Method refactoring
def proses_pesanan(pesanan):
    """Proses pesanan: validasi -> hitung -> update stok -> notifikasi."""
    validasi_pesanan(pesanan)
    total = hitung_total_pesanan(pesanan)
    update_stok(pesanan)
    kirim_notifikasi_pesanan(pesanan, total)
    return total

def validasi_pesanan(pesanan):
    """Validasi: pesanan tidak kosong, semua item tersedia."""
    if not pesanan.items:
        raise ValueError("Pesanan kosong")
    for item in pesanan.items:
        if item.stok <= 0:
            raise ValueError(f"{item.nama} habis")

def hitung_total_pesanan(pesanan) -> float:
    """Hitung subtotal + PPN 11%."""
    subtotal = sum(i.harga * i.qty for i in pesanan.items)
    pajak = subtotal * TARIF_PPN
    return subtotal + pajak

def update_stok(pesanan):
    """Kurangi stok untuk setiap item yang dipesan."""
    for item in pesanan.items:
        item.stok -= item.qty

def kirim_notifikasi_pesanan(pesanan, total: float):
    """Kirim email konfirmasi pesanan ke pembeli."""
    kirim_email(pesanan.email, f"Total: Rp {total:,.0f}")
```

```python
# ========================================
# CONTOH 3: Rename for Clarity
# ========================================

# BURUK -- nama tidak deskriptif
def proc(d, t):
    return d * (1 - t)

# BAIK -- nama jelas, type hints, docstring
def hitung_harga_setelah_diskon(
    harga: float, 
    persen_diskon: float
) -> float:
    """
    Hitung harga setelah diskon.
    
    Args:
        harga: Harga asli dalam Rupiah
        persen_diskon: Persentase diskon (0.0 - 1.0)
    
    Returns:
        Harga setelah diskon
    """
    if not 0 <= persen_diskon <= 1:
        raise ValueError("Diskon harus antara 0.0 dan 1.0")
    return harga * (1 - persen_diskon)
```

#### Strategi Mengelola Technical Debt

| Strategi | Deskripsi | Kapan Digunakan |
|----------|-----------|-----------------|
| **Boy Scout Rule** | "Tinggalkan kode lebih bersih dari saat kamu temukan" | Setiap kali edit kode |
| **Refactoring Sprint** | Alokasikan 20% sprint capacity untuk debt | Per sprint |
| **Debt Backlog** | Dokumentasikan dan prioritaskan tech debt items | Secara berkala |
| **Automated Tools** | SonarQube, ESLint, Pylint untuk deteksi otomatis | Di CI/CD pipeline |
| **Code Review** | Reviewer cek apakah PR menambah debt baru | Setiap PR |

```python
# Contoh: Tech debt tracker sederhana
from datetime import datetime

class TechDebtTracker:
    """Tracker untuk mencatat dan memprioritaskan technical debt."""
    
    def __init__(self):
        self.items = []
    
    def tambah_debt(self, judul, kuadran, dampak, effort):
        """
        Tambah item tech debt.
        
        Args:
            judul: Deskripsi singkat debt
            kuadran: "prudent-deliberate", "reckless-deliberate", dll.
            dampak: 1-5 (seberapa besar dampak negatif)
            effort: 1-5 (seberapa besar usaha untuk memperbaiki)
        """
        prioritas = dampak / effort  # Semakin tinggi = fix duluan
        self.items.append({
            "judul": judul,
            "kuadran": kuadran,
            "dampak": dampak,
            "effort": effort,
            "prioritas": round(prioritas, 2),
            "tanggal": datetime.now().isoformat()
        })
    
    def get_prioritized(self):
        """Dapatkan daftar debt diurutkan berdasarkan prioritas."""
        return sorted(self.items, key=lambda x: x["prioritas"], reverse=True)

# Contoh penggunaan
tracker = TechDebtTracker()
tracker.tambah_debt(
    "Replace magic numbers di modul billing",
    "prudent-inadvertent", dampak=4, effort=1
)
tracker.tambah_debt(
    "Refactor monolithic views.py (2000+ baris)",
    "prudent-deliberate", dampak=5, effort=4
)
tracker.tambah_debt(
    "Migrasi dari unittest ke pytest",
    "prudent-deliberate", dampak=3, effort=3
)

for item in tracker.get_prioritized():
    print(f"[{item['prioritas']:.1f}] {item['judul']}")
```

```
Output:
[4.0] Replace magic numbers di modul billing
[1.2] Refactor monolithic views.py (2000+ baris)
[1.0] Migrasi dari unittest ke pytest
```

### 12.4 Refactoring -- Mengubah Struktur Tanpa Mengubah Perilaku

Refactoring adalah proses memperbaiki desain internal kode **tanpa mengubah perilaku eksternalnya**. Prasyarat utama: **harus ada test** yang memverifikasi perilaku tidak berubah.

```
Refactoring Safety Net:
+--------------------------------------------------+
|                                                  |
|  1. Pastikan ada test yang passing                |
|     --> pytest --cov -> semua green               |
|                                                  |
|  2. Lakukan refactoring (ubah struktur)           |
|     --> Extract method, rename, dll.              |
|                                                  |
|  3. Jalankan test lagi                            |
|     --> pytest --cov -> masih semua green?        |
|         +-- YA -> refactoring aman!               |
|         +-- TIDAK -> revert, coba lagi            |
|                                                  |
|  "Refactoring tanpa test = berjalan di kegelapan" |
+--------------------------------------------------+
```

#### Katalog Teknik Refactoring

| Teknik | Kapan Digunakan | Sebelum | Sesudah |
|--------|-----------------|---------|---------|
| **Extract Method** | Fungsi terlalu panjang (>20 baris) | 1 fungsi besar | Beberapa fungsi kecil |
| **Rename** | Nama tidak deskriptif | `proc(d, t)` | `hitung_diskon(harga, persen)` |
| **Replace Magic Number** | Angka tanpa makna jelas | `0.11` | `TARIF_PPN = 0.11` |
| **Introduce Parameter Object** | Terlalu banyak parameter | `f(a, b, c, d, e)` | `f(config_obj)` |
| **Replace Conditional with Polymorphism** | If-else panjang | 10 if-else | Subclass per kasus |
| **Move Method** | Method di kelas yang salah | Class A punya method untuk B | Pindah ke Class B |

```python
# ========================================
# CONTOH 4: Introduce Parameter Object
# ========================================

# BURUK -- terlalu banyak parameter (parameter smell)
def buat_invoice(
    nama_pelanggan, alamat, kota, kode_pos, telepon,
    items, metode_bayar, tanggal
):
    pass  # ... logika kompleks

# BAIK -- gunakan dataclass sebagai parameter object
from dataclasses import dataclass
from typing import List

@dataclass
class Pelanggan:
    nama: str
    alamat: str
    kota: str
    kode_pos: str
    telepon: str

@dataclass  
class ItemPesanan:
    nama: str
    harga: float
    qty: int

@dataclass
class Invoice:
    pelanggan: Pelanggan
    items: List[ItemPesanan]
    metode_bayar: str
    tanggal: str

def buat_invoice(invoice: Invoice) -> dict:
    """Buat invoice dari data terstruktur."""
    subtotal = sum(i.harga * i.qty for i in invoice.items)
    return {
        "pelanggan": invoice.pelanggan.nama,
        "kota": invoice.pelanggan.kota,
        "subtotal": subtotal,
        "ppn": subtotal * TARIF_PPN,
        "total": subtotal * (1 + TARIF_PPN),
        "metode": invoice.metode_bayar
    }
```

```python
# ========================================
# CONTOH 5: Replace Conditional with Strategy Pattern
# ========================================

# BURUK -- if-else panjang untuk kalkulasi ongkir
def hitung_ongkir(berat_kg, tujuan, metode):
    if metode == "reguler":
        if tujuan == "jawa":
            return berat_kg * 8000
        elif tujuan == "sumatera":
            return berat_kg * 12000
        elif tujuan == "kalimantan":
            return berat_kg * 15000
    elif metode == "express":
        if tujuan == "jawa":
            return berat_kg * 15000
        # ... dan seterusnya

# BAIK -- Strategy Pattern dengan dictionary
TARIF_ONGKIR = {
    "reguler": {"jawa": 8000, "sumatera": 12000, "kalimantan": 15000},
    "express": {"jawa": 15000, "sumatera": 22000, "kalimantan": 28000},
    "same_day": {"jawa": 25000}  # Hanya tersedia di Jawa
}

def hitung_ongkir(berat_kg: float, tujuan: str, metode: str) -> float:
    """
    Hitung ongkos kirim berdasarkan berat, tujuan, dan metode.
    
    Raises:
        ValueError: jika metode atau tujuan tidak valid
    """
    if metode not in TARIF_ONGKIR:
        raise ValueError(f"Metode '{metode}' tidak tersedia")
    if tujuan not in TARIF_ONGKIR[metode]:
        raise ValueError(f"Tujuan '{tujuan}' tidak tersedia untuk {metode}")
    
    return berat_kg * TARIF_ONGKIR[metode][tujuan]

# Test
print(hitung_ongkir(2.5, "jawa", "reguler"))     # 20000
print(hitung_ongkir(1.0, "sumatera", "express"))  # 22000
```

### 12.5 Software Metrics

Metrics membantu kita mengukur kualitas kode secara **objektif**, bukan berdasarkan intuisi.

| Metrik | Deskripsi | Target | Tool |
|--------|-----------|--------|------|
| **Cyclomatic Complexity** | Jumlah jalur independen dalam fungsi | <= 10 per fungsi | radon (Python) |
| **Coupling** | Ketergantungan antar modul | Rendah (loose coupling) | SonarQube |
| **Cohesion** | Keterkaitan internal dalam modul | Tinggi (strong cohesion) | SonarQube |
| **Lines of Code (LOC)** | Ukuran kode | -- | cloc |
| **Code Churn** | Frekuensi perubahan kode | -- | git log analysis |
| **Maintainability Index** | Skor 0-100 kemudahan maintenance | >= 65 | radon |

```
Hubungan Coupling dan Cohesion:
+----------------------------------------------+
|                                              |
|  BAIK:                    BURUK:             |
|  Low Coupling,            High Coupling,     |
|  High Cohesion            Low Cohesion       |
|                                              |
|  +------+  +------+     +------+  +------+  |
|  | A    |  | B    |     | A    |--| B    |  |
|  | ---  |  | ---  |     | abc  |--| def  |  |
|  | aaa  |  | bbb  |     | ghi  |--| jkl  |  |
|  +--+---+  +--+---+     +--+---+  +--+---+  |
|     |         |             |\ /|     |      |
|     +----+----+             | X |     |      |
|    (sedikit link)           |/ \|     |      |
|                          (banyak link)       |
+----------------------------------------------+
```

```python
# Cyclomatic Complexity = Jumlah keputusan (if/elif/for/while/and/or) + 1

# CC = 5 (4 keputusan + 1)
def kategorisasi_nilai(skor: int) -> str:
    """Kategorisasi nilai mahasiswa UAI."""
    if skor >= 85:              # +1
        return 'A'
    elif skor >= 75:            # +1
        return 'B+'
    elif skor >= 65:            # +1
        return 'C+'
    elif skor >= 55:            # +1
        return 'C'
    else:
        return 'D'

# CC = 2 (refactored -- minim branch)
def kategorisasi_nilai_v2(skor: int) -> str:
    """Versi refactored menggunakan lookup table."""
    BATAS = [(85, 'A'), (75, 'B+'), (65, 'C+'), (55, 'C')]
    for batas, grade in BATAS:
        if skor >= batas:
            return grade
    return 'D'
```

```bash
# Mengukur cyclomatic complexity dengan radon
pip install radon

# Analisis complexity per fungsi
radon cc src/ -a -s
# Output contoh:
# src/services/order.py
#     F 12:0 proses_pesanan - B (6)
#     F 25:0 validasi_pesanan - A (3)
# Average complexity: B (4.5)

# Skala radon:
# A (1-5)   = Rendah -- bagus
# B (6-10)  = Sedang -- perhatikan
# C (11-15) = Tinggi -- perlu refactor
# D (16-20) = Sangat tinggi -- wajib refactor
# F (21+)   = Kritis -- refactor SEGERA

# Maintainability Index
radon mi src/ -s
# Output: src/app.py - A (75.23)

# Raw metrics (LOC, SLOC, comments, dll.)
radon raw src/ -s
```

### 12.6 Semantic Versioning (SemVer)

SemVer menggunakan format **MAJOR.MINOR.PATCH** untuk mengkomunikasikan jenis perubahan secara standar:

```
Versi: 2.4.1
        | | |
        | | +-- PATCH: Bug fix, backward-compatible
        | +---- MINOR: Fitur baru, backward-compatible
        +------ MAJOR: Breaking change, TIDAK backward-compatible

Contoh riwayat versi aplikasi "Toko UMKM":
1.0.0  Rilis pertama (MVP)
1.0.1  Fix: harga tampil Rp 0 saat stok habis
1.1.0  Tambah fitur filter produk by kategori
1.2.0  Tambah fitur ekspor laporan CSV
1.2.1  Fix: laporan CSV encoding error di Excel
2.0.0  Ubah format API response (breaking change!)
2.1.0  Tambah endpoint baru /api/v2/analytics

Aturan increment:
+-- Bug fix saja --------------------- PATCH (1.0.0 -> 1.0.1)
+-- Fitur baru (backward-compat) ----- MINOR (1.0.0 -> 1.1.0)
+-- Breaking change ------------------- MAJOR (1.0.0 -> 2.0.0)
+-- PATCH di-reset saat MINOR naik: 1.2.3 -> 1.3.0
```

```python
# Contoh: SemVer parser dan comparator
class SemVer:
    """Semantic Version parser."""
    
    def __init__(self, version_str: str):
        parts = version_str.split(".")
        if len(parts) != 3:
            raise ValueError(f"Format tidak valid: {version_str}")
        self.major = int(parts[0])
        self.minor = int(parts[1])
        self.patch = int(parts[2])
    
    def bump_patch(self) -> 'SemVer':
        """Increment PATCH version (bug fix)."""
        return SemVer(f"{self.major}.{self.minor}.{self.patch + 1}")
    
    def bump_minor(self) -> 'SemVer':
        """Increment MINOR version (fitur baru)."""
        return SemVer(f"{self.major}.{self.minor + 1}.0")
    
    def bump_major(self) -> 'SemVer':
        """Increment MAJOR version (breaking change)."""
        return SemVer(f"{self.major + 1}.0.0")
    
    def is_compatible(self, other: 'SemVer') -> bool:
        """Cek apakah dua versi backward-compatible (same major)."""
        return self.major == other.major
    
    def __str__(self):
        return f"{self.major}.{self.minor}.{self.patch}"

# Penggunaan
v = SemVer("1.2.3")
print(f"Current: {v}")                     # 1.2.3
print(f"Bug fix: {v.bump_patch()}")        # 1.2.4
print(f"New feature: {v.bump_minor()}")    # 1.3.0
print(f"Breaking: {v.bump_major()}")       # 2.0.0

v2 = SemVer("1.5.0")
print(f"Compatible? {v.is_compatible(v2)}")  # True (same major)

v3 = SemVer("2.0.0")
print(f"Compatible? {v.is_compatible(v3)}")  # False (different major)
```

#### Dependency Management

```
Dependency Range Syntax:
+--------------+------------------------+----------------------+
| Syntax       | Arti                   | Contoh               |
+--------------+------------------------+----------------------+
| ==2.0.0      | Exact: hanya versi ini | pip: flask==2.0.0    |
| ^4.18.2      | Compatible: minor OK   | npm: "^4.18.2"       |
|              | (4.18.2 - 4.x.x)      | -> 4.18.2 s/d 4.99.x|
| ~4.17.21     | Close to: patch only   | npm: "~4.17.21"      |
|              | (4.17.21 - 4.17.x)    | -> 4.17.21 s/d 4.17.x|
| >=2.0,<3.0   | Range: dalam rentang   | pip: flask>=2.0,<3.0 |
+--------------+------------------------+----------------------+
```

```bash
# Python: pip + requirements.txt
pip freeze > requirements.txt     # Export semua versi exact
pip install -r requirements.txt   # Install dari file
pip-audit                         # Cek vulnerabilities

# Node.js: npm + package.json
npm audit                  # Cek vulnerabilities
npm audit fix              # Auto-fix yang aman
npm outdated               # Lihat package yang outdated
```

```json
// package.json -- dependency management
{
  "dependencies": {
    "express": "^4.18.2",
    "lodash": "~4.17.21",
    "react": "18.2.0"
  }
}
```

#### SBOM -- Software Bill of Materials (Pengantar)

SBOM adalah **daftar lengkap** semua komponen dalam software -- seperti daftar bahan pada kemasan makanan BPOM.

```
SBOM Contoh untuk Toko UMKM:
+--------------+--------+---------+-------------+
| Komponen     | Versi  | Lisensi | Kerentanan  |
+--------------+--------+---------+-------------+
| flask        | 3.0.0  | BSD     | Tidak ada   |
| sqlalchemy   | 2.0.25 | MIT     | Tidak ada   |
| requests     | 2.31.0 | Apache  | CVE-2024-XX |
| pillow       | 10.1.0 | MIT     | CVE-2024-YY |
| jinja2       | 3.1.3  | BSD     | Tidak ada   |
| gunicorn     | 21.2.0 | MIT     | Tidak ada   |
+--------------+--------+---------+-------------+

Mengapa SBOM penting?
+-- Transparansi: tahu apa yang ada di software kita
+-- Keamanan: deteksi dini komponen yang vulnerable
+-- Compliance: regulasi mulai mewajibkan SBOM (US EO 14028)
+-- Maintenance: tahu kapan harus update dependency
```

> **Nilai Islami -- Istiqamah (Konsistensi):** Software maintenance membutuhkan istiqamah -- komitmen untuk terus memperbaiki dan menjaga kualitas, bukan hanya saat awal pengembangan. Sebagaimana ibadah yang terbaik adalah yang dilakukan secara konsisten walau sedikit (*khairul 'amal adwamuha wa in qalla*), perawatan kode yang terbaik juga dilakukan secara rutin: boy scout rule di setiap commit, refactoring di setiap sprint.

---

## Kegiatan Pembelajaran

### Pre-class (20 menit)

- Baca: Martin Fowler, "Refactoring: Improving the Design of Existing Code" -- Chapter 1 (free online summary di [refactoring.com](https://refactoring.com/))
- Install radon: `pip install radon`
- Jalankan `radon cc` pada salah satu file proyek kelompok dan catat hasilnya
- Identifikasi 3 contoh technical debt di proyek kelompok sendiri

### In-class (110 menit)

| Waktu | Aktivitas | Metode |
|-------|-----------|--------|
| 0-20 menit | 4 jenis maintenance, Lehman's Laws, lifecycle cost, studi kasus Indonesia | Ceramah + diskusi |
| 20-40 menit | Technical debt: quadrant, gejala, strategi, debt tracker | Ceramah + contoh kode |
| 40-60 menit | Code analysis exercise: identifikasi code smells di contoh kode (kelompok 3-4 orang) | Exercise kelompok |
| 60-65 menit | *Break* | -- |
| 65-90 menit | Refactoring workshop: perbaiki kode bermasalah step-by-step (Extract Method, Rename, dll.) | Hands-on coding |
| 90-100 menit | Software metrics (radon demo), SemVer, dependency management, SBOM | Ceramah + demo |
| 100-110 menit | **Kuis K3** (materi Minggu 9-12, 15 menit) + wrap-up | Kuis + diskusi |

### Post-class (20 menit)

- Analisis cyclomatic complexity proyek kelompok dengan `radon cc src/ -a -s`
- Identifikasi 3 fungsi yang perlu di-refactor dan lakukan refactoring dengan safety net (test dulu!)
- Review dependencies proyek: `pip-audit` atau `npm audit` -- adakah yang vulnerable?
- Buat tag SemVer pertama di repo: `git tag v1.0.0`
- Lanjutkan pengerjaan proyek akhir (Sprint 3)

---

## Latihan & Diskusi

### Soal 1 (C2 -- Memahami)
Jelaskan empat jenis software maintenance (corrective, adaptive, perfective, preventive) dengan contoh konkret dari proyek kelompok Anda. Mengapa perfective maintenance biasanya memiliki proporsi terbesar (~50%)?

### Soal 2 (C4 -- Menganalisis)
Analisis kode berikut dan identifikasi minimal 5 code smells. Untuk setiap code smell, sebutkan teknik refactoring yang tepat dan tulis kode setelah refactoring:

```python
def p(data, t, d, n, e, a):
    r = 0
    for i in data:
        if i["type"] == "A":
            r += i["v"] * 1.1
        elif i["type"] == "B":
            r += i["v"] * 1.05
        elif i["type"] == "C":
            r += i["v"] * 1.0
    if r > 1000000:
        r = r * 0.95
    if d == True:
        r = r * 0.9
    print("Total: " + str(r))
    return r
```

### Soal 3 (C4 -- Menganalisis)
Jelaskan Lehman's Law #2 (Increasing Complexity) dengan studi kasus sebuah aplikasi e-commerce Indonesia yang sudah berusia 5 tahun. Bagaimana law ini terlihat dalam codebase? Apa strategi untuk mengatasi peningkatan kompleksitas?

### Soal 4 (C3 -- Menerapkan)
Proyek kelompok Anda saat ini di versi 1.3.2. Tentukan versi berikutnya untuk setiap skenario berikut dan jelaskan alasannya berdasarkan SemVer:
a) Fix bug di halaman checkout (tombol tidak responsif)
b) Tambah fitur baru: notifikasi email saat pesanan dikirim
c) Ubah format response API dari `{"data": [...]}` menjadi `{"items": [...]}`
d) Tambah fitur pencarian produk + fix 2 bug minor

### Soal 5 (C5 -- Mengevaluasi)
Tim Anda menemukan bahwa file `views.py` memiliki 2000 baris kode dan cyclomatic complexity rata-rata 25 per fungsi. Evaluasi pendekatan mana yang lebih baik: (a) rewrite dari nol, atau (b) refactoring bertahap. Pertimbangkan: risiko, waktu, dampak ke fitur yang sudah berjalan, dan Lehman's Laws.

---

## Penugasan

### K3 -- Kuis Testing & DevOps

| Komponen | Detail |
|----------|--------|
| **Tipe** | Individual |
| **Bobot** | 3% dari nilai akhir |
| **Waktu** | 15 menit, in-class (akhir sesi Minggu 12) |
| **Cakupan** | Materi Minggu 9-12 (Testing, Advanced Testing, DevOps, Maintenance) |
| **Sifat** | Closed-book, tanpa AI/internet |
| **Format** | 10 soal pilihan ganda + 2 soal jawaban singkat |

---

## Referensi

1. Pressman, R. S. & Maxim, B. R. (2020). *Software Engineering*, 9th ed. Chapter 28-29.
2. Sommerville, I. (2016). *Software Engineering*, 10th ed. Chapter 9.
3. Fowler, M. (2019). *Refactoring: Improving the Design of Existing Code*, 2nd ed. Addison-Wesley.
4. Cunningham, W. (1992). "The WyCash Portfolio Management System" -- origin of technical debt metaphor.
5. Semantic Versioning 2.0.0. [semver.org](https://semver.org/)
6. radon documentation. [radon.readthedocs.io](https://radon.readthedocs.io/)
7. Lehman, M. M. (1996). "Laws of Software Evolution Revisited." *EWSPT 1996*.
8. Fowler, M. (2009). "Technical Debt Quadrant." [martinfowler.com](https://martinfowler.com/bliki/TechnicalDebtQuadrant.html)

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* -- Program Studi Informatika, Universitas Al Azhar Indonesia
