# Minggu 7: Software Construction — Coding Standards dan Version Control

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak |
| **Kode** | IF2205 |
| **Minggu** | 7 dari 16 |
| **Topik** | Clean Code, Code Smells, Refactoring, Git Flow, Conventional Commits, Code Review |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **Bahasa Pemrograman** | Python 3.x + JavaScript |
| **CPMK** | CPMK-4 |
| **Sub-CPMK** | 4.1 (Clean code, code smells, refactoring), 4.2 (Git workflow, code review) |
| **Durasi** | 150 menit (3 x 50 menit) |
| **Metode** | Ceramah, live coding, pair programming, code review exercise |

## Tujuan Pembelajaran

Setelah mengikuti perkuliahan minggu ini, mahasiswa mampu:

1. **Menerapkan** minimal 10 prinsip Clean Code dalam penulisan kode Python (C3)
2. **Mengidentifikasi** 10+ code smells dan menerapkan teknik refactoring yang tepat (C4)
3. **Menggunakan** Git branching strategy (Git Flow) dan conventional commits dalam kolaborasi tim (C3)
4. **Melakukan** code review yang konstruktif menggunakan Pull Request workflow (C4)

---

## Materi Pembelajaran

### 7.1 Clean Code — Seni Menulis Kode yang Bersih

#### 7.1.1 Apa Itu Clean Code?

> "Clean code is code that is easy to understand and easy to change." — Robert C. Martin

> "Any fool can write code that a computer can understand. Good programmers write code that humans can understand." — Martin Fowler

```
┌─────────────────────────────────────────────────────────────────┐
│                 MENGAPA CLEAN CODE PENTING?                       │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │  Fakta industri:                                           │ │
│  │  - Developer menghabiskan 10x lebih banyak waktu           │ │
│  │    MEMBACA kode daripada MENULIS kode                      │ │
│  │  - Kode ditulis SEKALI, dibaca BERKALI-KALI                │ │
│  │  - Software 60-80% waktunya di fase maintenance            │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                  │
│  ┌──────────────────┐     vs     ┌──────────────────┐          │
│  │   DIRTY CODE     │            │   CLEAN CODE     │          │
│  │                  │            │                  │          │
│  │  - Sulit dibaca  │            │  - Mudah dibaca  │          │
│  │  - Sulit diubah  │            │  - Mudah diubah  │          │
│  │  - Banyak bug    │            │  - Sedikit bug   │          │
│  │  - Tim frustrasi │            │  - Tim produktif │          │
│  │  - Biaya tinggi  │            │  - Biaya rendah  │          │
│  └──────────────────┘            └──────────────────┘          │
└─────────────────────────────────────────────────────────────────┘
```

#### 7.1.2 Sepuluh Prinsip Clean Code

**Prinsip 1: Nama Bermakna (*Meaningful Names*)**

```python
# BURUK: Apa itu d, p, dan x?
def calc(d, p, x):
    return d * p * (1 - x)

# BAIK: Nama menjelaskan tujuan
def hitung_total_pembayaran(jumlah_hari, harga_per_hari, diskon_persen):
    """Hitung total pembayaran setelah diskon."""
    return jumlah_hari * harga_per_hari * (1 - diskon_persen)

# BURUK: Variabel ambigu
data = get_data()
info = process_info()
temp = calculate_temp()

# BAIK: Nama spesifik
daftar_mahasiswa = get_daftar_mahasiswa()
ringkasan_nilai = proses_nilai_semester()
suhu_ruangan_celsius = baca_sensor_suhu()
```

**Prinsip 2: Fungsi Kecil (*Small Functions*)**

```python
# BURUK: Fungsi monster 100+ baris
def proses_pendaftaran(data):
    # validasi nama (10 baris)
    # validasi email (10 baris)
    # validasi password (10 baris)
    # simpan ke database (15 baris)
    # kirim email verifikasi (15 baris)
    # buat session (10 baris)
    # log aktivitas (10 baris)
    pass  # Total: 80+ baris, 7 tanggung jawab!

# BAIK: Setiap fungsi punya satu tanggung jawab
def proses_pendaftaran(data):
    """Koordinasi proses pendaftaran mahasiswa baru."""
    validasi_data_pendaftaran(data)
    mahasiswa = simpan_mahasiswa_baru(data)
    kirim_email_verifikasi(mahasiswa.email)
    buat_session(mahasiswa)
    log_aktivitas("pendaftaran", mahasiswa.id)
    return mahasiswa

def validasi_data_pendaftaran(data):
    """Validasi semua field pendaftaran."""
    validasi_nama(data['nama'])
    validasi_email(data['email'])
    validasi_password(data['password'])

def validasi_nama(nama):
    """Nama harus 3-100 karakter, hanya huruf dan spasi."""
    if not nama or len(nama) < 3:
        raise ValueError("Nama minimal 3 karakter")
    if len(nama) > 100:
        raise ValueError("Nama maksimal 100 karakter")
```

**Prinsip 3: Satu Level Abstraksi (*One Level of Abstraction*)**

```python
# BURUK: Campur level abstraksi
def generate_laporan_peminjaman(bulan, tahun):
    # Level tinggi: bisnis
    peminjaman = get_peminjaman(bulan, tahun)
    
    # Level rendah: SQL langsung!
    cursor.execute("SELECT COUNT(*) FROM peminjaman WHERE status='terlambat'")
    
    # Level rendah: string manipulation
    html = "<html><body><h1>Laporan</h1>"
    for p in peminjaman:
        html += f"<tr><td>{p.nama}</td></tr>"
    html += "</body></html>"

# BAIK: Setiap fungsi di satu level abstraksi
def generate_laporan_peminjaman(bulan, tahun):
    """Level tinggi: koordinasi pembuatan laporan."""
    data = kumpulkan_data_peminjaman(bulan, tahun)
    statistik = hitung_statistik(data)
    return render_laporan_html(data, statistik)
```

**Prinsip 4: DRY (Don't Repeat Yourself)**

```python
# BURUK: Copy-paste kode validasi
def create_mahasiswa(data):
    if not data.get('email') or '@' not in data['email']:
        raise ValueError("Email tidak valid")
    # ... proses create

def update_mahasiswa(mhs_id, data):
    if not data.get('email') or '@' not in data['email']:
        raise ValueError("Email tidak valid")  # Duplikasi!
    # ... proses update


# BAIK: Extract ke fungsi reusable
def validasi_email(email):
    """Validasi format email."""
    if not email or '@' not in email:
        raise ValueError("Email tidak valid")

def create_mahasiswa(data):
    validasi_email(data.get('email'))
    # ... proses create

def update_mahasiswa(mhs_id, data):
    validasi_email(data.get('email'))
    # ... proses update
```

**Prinsip 5: Komentar yang Bermakna**

```python
# BURUK: Komentar menjelaskan "apa" (redundan)
i = i + 1  # Tambah i dengan 1

# BAIK: Komentar menjelaskan "mengapa"
# Tambah 1 karena indeks database dimulai dari 1, bukan 0
i = i + 1

# BURUK: Komentar sebagai permintaan maaf
# TODO: Fix this later (sudah 2 tahun)
# HACK: Ini workaround yang jelek tapi works

# BAIK: Self-documenting code — kode yang menjelaskan dirinya sendiri
def is_eligible_for_scholarship(mahasiswa):
    """Cek apakah mahasiswa memenuhi syarat beasiswa."""
    has_high_gpa = mahasiswa.ipk >= 3.5
    is_active = mahasiswa.status == "aktif"
    no_academic_violation = mahasiswa.pelanggaran_count == 0
    return has_high_gpa and is_active and no_academic_violation
```

**Prinsip 6-10 (Ringkasan):**

| # | Prinsip | Buruk | Baik |
|---|---------|-------|------|
| 6 | **KISS** (Keep It Simple) | Nested if 5 level | Early return, guard clause |
| 7 | **Error Handling** terpisah | Exception di tengah-tengah logika bisnis | Try-except di boundary |
| 8 | **Konsisten** formatting | Campur tab dan space, inkonsisten naming | PEP 8, auto-formatter (Black) |
| 9 | **Avoid Magic Numbers** | `if status == 3` | `if status == STATUS_APPROVED` |
| 10 | **Command-Query Separation** | Fungsi yang mengubah data DAN mengembalikan data | Pisahkan: set_status() dan get_status() |

#### 7.1.3 PEP 8 — Python Coding Standards

```python
# PEP 8 Rules yang Paling Penting

# 1. Indentasi: 4 spasi (BUKAN tab)
def fungsi():
    if True:
        return "4 spasi"

# 2. Panjang baris maksimal: 79 karakter (kode), 72 (docstring)
# Jika terlalu panjang, pecah:
daftar_mahasiswa = get_mahasiswa_by_criteria(
    angkatan=2022,
    jurusan="Informatika",
    status="aktif"
)

# 3. Naming Convention
nama_variabel = "snake_case"        # variabel dan fungsi
KONSTANTA = "SCREAMING_SNAKE_CASE"  # konstanta
class NamaKelas:                     # PascalCase untuk class
    pass

# 4. Import berurutan
import os                           # Standard library
import sys

import flask                        # Third-party
import sqlalchemy

from app.models import User         # Local
from app.services import AuthService

# 5. Whitespace
x = 1                # Baik: spasi di sekitar operator
y=2                  # Buruk: tanpa spasi

fungsi(arg1, arg2)   # Baik: spasi setelah koma
fungsi(arg1,arg2)    # Buruk: tanpa spasi

# 6. Docstring (Google style)
def hitung_ipk(daftar_nilai):
    """Hitung IPK mahasiswa berdasarkan daftar nilai.
    
    Args:
        daftar_nilai: List of dict, setiap dict berisi
            'sks' (int) dan 'bobot' (float).
    
    Returns:
        Float: IPK dengan 2 desimal.
    
    Raises:
        ValueError: Jika daftar_nilai kosong.
    """
    if not daftar_nilai:
        raise ValueError("Daftar nilai tidak boleh kosong")
    
    total_sks = sum(n['sks'] for n in daftar_nilai)
    total_bobot = sum(n['sks'] * n['bobot'] for n in daftar_nilai)
    return round(total_bobot / total_sks, 2)
```

### 7.2 Code Smells — Tanda-tanda Kode Bermasalah

#### 7.2.1 Apa Itu Code Smell?

> Code smell adalah indikasi di dalam kode yang menunjukkan masalah desain yang lebih dalam. Bukan bug — kode masih berjalan — tapi code smell membuat kode sulit di-maintain.

```
┌─────────────────────────────────────────────────────────────────┐
│                    CODE SMELL CATEGORIES                         │
│                                                                  │
│  ┌─────────────────┐  ┌─────────────────┐  ┌────────────────┐ │
│  │   BLOATERS       │  │   OO ABUSERS     │  │  DISPENSABLES  │ │
│  │                 │  │                 │  │                │ │
│  │  Long Method    │  │  Feature Envy   │  │  Dead Code     │ │
│  │  Large Class    │  │  Refused Bequest│  │  Comments      │ │
│  │  Long Param List│  │  Switch         │  │  Duplicate Code│ │
│  │  Primitive      │  │  Statements     │  │  Speculative   │ │
│  │  Obsession      │  │                 │  │  Generality    │ │
│  └─────────────────┘  └─────────────────┘  └────────────────┘ │
│                                                                  │
│  ┌─────────────────┐  ┌─────────────────┐                     │
│  │   COUPLERS       │  │   CHANGE         │                     │
│  │                 │  │   PREVENTERS     │                     │
│  │  Message Chains │  │  Divergent Change│                     │
│  │  Middle Man     │  │  Shotgun Surgery │                     │
│  │  Inappropriate  │  │  Parallel         │                     │
│  │  Intimacy       │  │  Inheritance     │                     │
│  └─────────────────┘  └─────────────────┘                     │
└─────────────────────────────────────────────────────────────────┘
```

#### 7.2.2 Dua Belas Code Smells dengan Before/After

**1. Long Method** — Fungsi terlalu panjang

```python
# BEFORE (smell): Fungsi 50+ baris
def process_order(order):
    # validasi (15 baris)
    # hitung total (10 baris)
    # apply diskon (10 baris)
    # simpan ke DB (10 baris)
    # kirim notifikasi (10 baris)
    pass

# AFTER (refactored): Extract Method
def process_order(order):
    validate_order(order)
    total = calculate_total(order)
    total = apply_discount(total, order.customer)
    save_order(order, total)
    send_order_notification(order)
```

**2. Duplicate Code** — Kode yang sama muncul berulang

```python
# BEFORE: Duplikasi format tanggal
def get_peminjaman_aktif(user_id):
    items = Peminjaman.query.filter_by(user_id=user_id, status='aktif').all()
    return [{
        'id': p.id,
        'buku': p.buku.judul,
        'tanggal': p.tanggal_pinjam.strftime('%d/%m/%Y')  # Duplikasi!
    } for p in items]

def get_peminjaman_selesai(user_id):
    items = Peminjaman.query.filter_by(user_id=user_id, status='selesai').all()
    return [{
        'id': p.id,
        'buku': p.buku.judul,
        'tanggal': p.tanggal_pinjam.strftime('%d/%m/%Y')  # Duplikasi!
    } for p in items]

# AFTER: Extract common logic
def format_tanggal(dt):
    return dt.strftime('%d/%m/%Y')

def serialize_peminjaman(peminjaman_list):
    return [{'id': p.id, 'buku': p.buku.judul, 'tanggal': format_tanggal(p.tanggal_pinjam)}
            for p in peminjaman_list]

def get_peminjaman_by_status(user_id, status):
    items = Peminjaman.query.filter_by(user_id=user_id, status=status).all()
    return serialize_peminjaman(items)
```

**3. God Class** — Class yang terlalu besar

```python
# BEFORE: GodClass — satu class melakukan segalanya
class SistemPerpustakaan:
    def cari_buku(self): pass
    def pinjam_buku(self): pass
    def kembalikan_buku(self): pass
    def daftar_anggota(self): pass
    def kirim_email(self): pass
    def generate_laporan(self): pass
    def backup_database(self): pass
    # 500+ baris...

# AFTER: Split menjadi class-class kecil (SRP!)
class BukuService:
    def cari(self): pass
    
class PeminjamanService:
    def pinjam(self): pass
    def kembalikan(self): pass

class AnggotaService:
    def daftar(self): pass

class NotifikasiService:
    def kirim_email(self): pass

class LaporanService:
    def generate(self): pass
```

**4. Magic Number** — Angka tanpa konteks

```python
# BEFORE: Magic numbers
if user.peminjaman_count >= 5:        # Apa arti 5?
    if denda > 50000:                  # Apa arti 50000?
        user.status = 3                # Apa arti 3?

# AFTER: Named constants
MAX_PEMINJAMAN = 5
BATAS_DENDA_SUSPEND = 50_000
STATUS_SUSPENDED = "suspended"

if user.peminjaman_count >= MAX_PEMINJAMAN:
    if denda > BATAS_DENDA_SUSPEND:
        user.status = STATUS_SUSPENDED
```

**5. Feature Envy** — Method yang lebih banyak mengakses data class lain

```python
# BEFORE: Method di Order terlalu banyak akses Customer
class Order:
    def calculate_discount(self):
        if self.customer.loyalty_level == "gold":
            if self.customer.total_purchases > 1_000_000:
                return self.total * 0.15
        return self.total * 0.05

# AFTER: Pindahkan ke class yang punya datanya
class Customer:
    def get_discount_rate(self):
        if self.loyalty_level == "gold" and self.total_purchases > 1_000_000:
            return 0.15
        return 0.05

class Order:
    def calculate_discount(self):
        return self.total * self.customer.get_discount_rate()
```

**6-12: Ringkasan Code Smells:**

| # | Code Smell | Tanda | Refactoring |
|---|-----------|-------|-------------|
| 6 | **Dead Code** | Kode yang tidak pernah dieksekusi | Delete (berani hapus!) |
| 7 | **Long Parameter List** | Fungsi dengan > 3 parameter | Introduce Parameter Object |
| 8 | **Primitive Obsession** | Pakai string untuk status, level | Replace with Enum/Class |
| 9 | **Switch Statements** | Banyak if-elif-else berulang | Replace with Polymorphism |
| 10 | **Message Chains** | `a.b().c().d().e()` | Hide Delegate |
| 11 | **Shotgun Surgery** | Satu perubahan = edit banyak file | Move Method, Inline Class |
| 12 | **Comments** (berlebih) | Komentar menjelaskan yang sudah jelas | Rename variable/method |

### 7.3 Refactoring — Memperbaiki Tanpa Mengubah Perilaku

#### 7.3.1 Apa Itu Refactoring?

> Refactoring adalah proses mengubah **struktur internal** kode tanpa mengubah **perilaku eksternal**-nya.

```
┌─────────────────────────────────────────────────────────────────┐
│               REFACTORING SAFETY NET                             │
│                                                                  │
│  SEBELUM refactoring, pastikan ada:                             │
│                                                                  │
│  1. Unit Tests ─────────┐                                       │
│  2. Version Control ────┤── SAFETY NET                          │
│  3. Code Review ────────┘                                       │
│                                                                  │
│  Proses:                                                        │
│  ┌────────┐   ┌──────────┐   ┌────────┐   ┌──────────┐       │
│  │ Test   │──▶│ Refactor │──▶│ Test   │──▶│ Commit   │       │
│  │ (Green)│   │ (Small   │   │ (Still │   │ (Save    │       │
│  │        │   │  step)   │   │  Green)│   │  point)  │       │
│  └────────┘   └──────────┘   └────────┘   └──────────┘       │
│                     │                                            │
│                     └── Ulangi sampai bersih                    │
│                                                                  │
│  JANGAN: Refactor + tambah fitur baru sekaligus!                │
│  LAKUKAN: Satu perubahan kecil, test, commit. Ulangi.           │
└─────────────────────────────────────────────────────────────────┘
```

#### 7.3.2 Teknik Refactoring Utama

```python
# 1. EXTRACT METHOD — Pecah fungsi panjang

# Before
def display_receipt(order):
    print("=" * 40)
    print(f"Toko Buku UAI")
    print(f"Tanggal: {order.date}")
    print("=" * 40)
    total = 0
    for item in order.items:
        subtotal = item.price * item.qty
        total += subtotal
        print(f"{item.name}: Rp {subtotal:,}")
    print("=" * 40)
    print(f"Total: Rp {total:,}")

# After
def display_receipt(order):
    print_header(order.date)
    total = print_items(order.items)
    print_footer(total)

def print_header(date):
    print("=" * 40)
    print(f"Toko Buku UAI")
    print(f"Tanggal: {date}")
    print("=" * 40)

def print_items(items):
    total = 0
    for item in items:
        subtotal = item.price * item.qty
        total += subtotal
        print(f"{item.name}: Rp {subtotal:,}")
    return total

def print_footer(total):
    print("=" * 40)
    print(f"Total: Rp {total:,}")
```

```python
# 2. REPLACE MAGIC NUMBER WITH CONSTANT

# Before
if response.status_code == 200:
    pass
elif response.status_code == 404:
    pass

# After
from http import HTTPStatus

if response.status_code == HTTPStatus.OK:
    pass
elif response.status_code == HTTPStatus.NOT_FOUND:
    pass
```

```python
# 3. INTRODUCE PARAMETER OBJECT

# Before: Terlalu banyak parameter
def cari_buku(judul, penulis, kategori, tahun_min, tahun_max, available_only):
    pass

# After: Kelompokkan dalam dataclass
from dataclasses import dataclass

@dataclass
class SearchCriteria:
    judul: str = ""
    penulis: str = ""
    kategori: str = ""
    tahun_min: int = 0
    tahun_max: int = 9999
    available_only: bool = False

def cari_buku(criteria: SearchCriteria):
    pass

# Penggunaan
criteria = SearchCriteria(judul="algoritma", available_only=True)
hasil = cari_buku(criteria)
```

```python
# 4. REPLACE CONDITIONAL WITH POLYMORPHISM

# Before: Switch statement
def hitung_biaya_pengiriman(tipe, berat):
    if tipe == "reguler":
        return berat * 10_000
    elif tipe == "express":
        return berat * 20_000
    elif tipe == "same_day":
        return berat * 35_000

# After: Polymorphism
from abc import ABC, abstractmethod

class ShippingStrategy(ABC):
    @abstractmethod
    def hitung_biaya(self, berat: float) -> int:
        pass

class RegulerShipping(ShippingStrategy):
    def hitung_biaya(self, berat: float) -> int:
        return int(berat * 10_000)

class ExpressShipping(ShippingStrategy):
    def hitung_biaya(self, berat: float) -> int:
        return int(berat * 20_000)

class SameDayShipping(ShippingStrategy):
    def hitung_biaya(self, berat: float) -> int:
        return int(berat * 35_000)
```

### 7.4 Git Branching Strategy

#### 7.4.1 Git Flow — Strategi Branching untuk Tim

```
┌─────────────────────────────────────────────────────────────────┐
│                      GIT FLOW                                    │
│                                                                  │
│ main      ──●──────────────────────────●──────────── (production)│
│             │                          ▲                         │
│             │                          │ merge                   │
│ develop   ──●──●──●──●──●──●──●──●──●── (integration)          │
│                 │     ▲  │     ▲                                 │
│                 │     │  │     │                                  │
│ feature/    ────●──●──┘  │     │                                 │
│ login                    │     │                                  │
│                          │     │                                  │
│ feature/    ─────────●──●──┘   │                                 │
│ search                         │                                  │
│                                │                                  │
│ bugfix/     ───────────────●──┘                                  │
│ typo                                                             │
│                                                                  │
│ hotfix/     ──────────────────────────●──▶ main + develop       │
│ critical                                                         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Branch Types:**

| Branch | Tujuan | Naming Convention | Merge ke |
|--------|--------|-------------------|----------|
| `main` | Production-ready code | `main` | — |
| `develop` | Integration branch | `develop` | `main` (via release) |
| `feature/*` | Fitur baru | `feature/nama-fitur` | `develop` |
| `bugfix/*` | Perbaikan bug | `bugfix/deskripsi` | `develop` |
| `release/*` | Persiapan release | `release/v1.0.0` | `main` + `develop` |
| `hotfix/*` | Perbaikan urgent | `hotfix/critical-fix` | `main` + `develop` |

#### 7.4.2 GitHub Flow — Alternatif yang Lebih Sederhana

```
┌─────────────────────────────────────────────────────────────────┐
│                    GITHUB FLOW (Simplified)                      │
│                                                                  │
│  main    ──●──────●──────●──────●──────●── (selalu deployable)  │
│            │      ▲      │      ▲      │                        │
│            │      │      │      │      │                        │
│  feature ──●──●──┘      │      │      │                        │
│  /login                  │      │      │                        │
│                          │      │      │                        │
│  feature ────────●──●──┘      │                                │
│  /search                       │                                │
│                                │                                │
│  bugfix  ──────────────●──●──┘                                 │
│  /fix-login                                                     │
│                                                                  │
│  Proses: branch -> commit -> PR -> review -> merge -> deploy   │
│                                                                  │
│  Lebih sederhana dari Git Flow — cocok untuk proyek kuliah!     │
└─────────────────────────────────────────────────────────────────┘
```

#### 7.4.3 Git Workflow Sehari-hari

```bash
# === 1. MULAI FITUR BARU ===
# Pastikan develop terbaru
git checkout develop
git pull origin develop

# Buat branch fitur baru
git checkout -b feature/pencarian-buku

# === 2. KERJAKAN FITUR ===
# Edit kode...
git add src/search.py src/templates/search.html
git commit -m "feat(search): tambah fitur pencarian buku berdasarkan judul"

# Tambahan perubahan...
git add src/search.py
git commit -m "feat(search): tambah filter berdasarkan kategori"

# === 3. PUSH DAN BUAT PULL REQUEST ===
git push -u origin feature/pencarian-buku
# Buka GitHub -> Create Pull Request -> feature/pencarian-buku → develop

# === 4. SETELAH REVIEW DAN APPROVE ===
# Merge dilakukan via GitHub (bukan manual)
# Hapus branch setelah merge
git checkout develop
git pull origin develop
git branch -d feature/pencarian-buku
```

#### 7.4.4 Conventional Commits — Pesan Commit yang Terstandar

```
┌─────────────────────────────────────────────────────────────────┐
│              CONVENTIONAL COMMITS FORMAT                         │
│                                                                  │
│  <type>(<scope>): <description>                                 │
│                                                                  │
│  Types:                                                         │
│  feat:     fitur baru                                           │
│  fix:      perbaikan bug                                        │
│  docs:     perubahan dokumentasi                                │
│  style:    formatting (tidak mengubah logic)                    │
│  refactor: refactoring kode (tidak mengubah fitur)              │
│  test:     menambah/memperbaiki test                            │
│  chore:    maintenance (dependencies, config)                   │
│  perf:     perbaikan performa                                   │
│  ci:       perubahan CI/CD config                               │
└─────────────────────────────────────────────────────────────────┘
```

**Contoh Commit Messages:**

```bash
# Fitur baru
git commit -m "feat(auth): tambah login dengan Google OAuth"
git commit -m "feat(search): tambah pencarian buku berdasarkan ISBN"
git commit -m "feat(loan): tambah fitur perpanjangan peminjaman"

# Bug fix
git commit -m "fix(search): perbaiki pencarian case-insensitive"
git commit -m "fix(loan): perbaiki kalkulasi denda yang salah"

# Dokumentasi
git commit -m "docs(readme): update instruksi instalasi"
git commit -m "docs(api): tambah dokumentasi endpoint buku"

# Refactoring
git commit -m "refactor(auth): extract validasi ke middleware"
git commit -m "refactor(models): rename field sesuai konvensi"

# Test
git commit -m "test(search): tambah unit test pencarian buku"
git commit -m "test(loan): tambah test edge case denda"
```

### 7.5 Pull Request dan Code Review

#### 7.5.1 Anatomi Pull Request yang Baik

```
┌─────────────────────────────────────────────────────────────────┐
│  PULL REQUEST TEMPLATE                                           │
│                                                                  │
│  Title: feat(search): tambah fitur pencarian buku               │
│                                                                  │
│  ## Deskripsi                                                   │
│  Menambahkan fitur pencarian buku berdasarkan judul, penulis,   │
│  dan ISBN dengan pagination.                                    │
│                                                                  │
│  ## Perubahan                                                   │
│  - Tambah endpoint GET /api/v1/buku?q=keyword                  │
│  - Tambah service layer: BukuSearchService                      │
│  - Tambah unit test (5 test cases)                              │
│                                                                  │
│  ## Screenshots (jika ada UI)                                   │
│  [gambar halaman pencarian]                                     │
│                                                                  │
│  ## Testing                                                     │
│  - [x] Unit tests pass                                          │
│  - [x] Manual testing: pencarian dengan keyword                 │
│  - [x] Edge case: keyword kosong, tidak ditemukan               │
│                                                                  │
│  ## Checklist                                                   │
│  - [x] Kode mengikuti PEP 8                                    │
│  - [x] Tidak ada code smells baru                               │
│  - [x] Conventional commit messages                             │
│  - [x] AI Usage Log updated                                    │
└─────────────────────────────────────────────────────────────────┘
```

#### 7.5.2 Code Review Checklist

| Kategori | Yang Diperiksa | Contoh |
|----------|----------------|--------|
| **Correctness** | Apakah kode berjalan sesuai requirement? | Logic benar, edge cases handled |
| **Design** | Apakah desain sesuai arsitektur? | SRP, proper layering |
| **Readability** | Apakah kode mudah dipahami? | Naming, structure, comments |
| **Testing** | Apakah ada test yang memadai? | Unit tests, edge cases |
| **Security** | Apakah ada kerentanan? | SQL injection, XSS, auth bypass |
| **Performance** | Apakah ada bottleneck? | N+1 query, unnecessary loops |
| **DRY** | Apakah ada duplikasi kode? | Copy-paste, similar functions |
| **Style** | Apakah sesuai coding standards? | PEP 8, naming conventions |

#### 7.5.3 Etika Code Review

```
┌─────────────────────────────────────────────────────────────────┐
│              ETIKA CODE REVIEW                                   │
│                                                                  │
│  JANGAN:                                                        │
│  "Kode ini jelek, siapa yang nulis?"                            │
│  "Ini salah semua, buat ulang."                                 │
│  "Harusnya kamu sudah tahu ini."                                │
│  Membiarkan PR berhari-hari tanpa review                        │
│                                                                  │
│  LAKUKAN:                                                       │
│  "Bagaimana kalau kita extract method ini supaya lebih mudah    │
│   di-test? Misalnya seperti ini: [contoh kode]"                │
│  "Saya punya saran alternatif. Mau diskusi?"                   │
│  "Kode ini sudah baik! Satu saran kecil di line 42..."         │
│  Review dalam 24 jam, beri feedback yang actionable             │
│                                                                  │
│  PRINSIP:                                                       │
│  1. Review kode, bukan orangnya                                 │
│  2. Berikan solusi, bukan hanya masalah                         │
│  3. Apresiasi hal yang sudah baik                               │
│  4. Gunakan "kita" bukan "kamu"                                 │
│  5. Tanya dulu sebelum judge: "Apakah ada alasan X?"           │
│                                                                  │
│  Dalam Islam: "Dan tolong-menolonglah kamu dalam kebaikan       │
│  dan ketakwaan" (QS. Al-Maidah: 2) — code review sebagai       │
│  bentuk tolong-menolong dalam meningkatkan kualitas             │
└─────────────────────────────────────────────────────────────────┘
```

#### 7.5.4 Contoh Code Review Comments

```python
# Reviewer comment pada PR:

# Line 15:
# Suggestion: Gunakan f-string daripada string concatenation
# Before: "Hello " + user.name + "!"
# After:  f"Hello {user.name}!"

# Line 28:
# Question: Apakah ada alasan khusus menggunakan raw SQL di sini?
# Biasanya kita pakai SQLAlchemy ORM untuk konsistensi.

# Line 42:
# Praise: Nice! Penggunaan dataclass di sini membuat kode
# jauh lebih rapi. Bagus!

# Line 55:
# Issue: Potential SQL injection vulnerability.
# request.args.get('q') dimasukkan langsung ke query.
# Fix: Gunakan parameterized query atau SQLAlchemy filter.
```

---

## Kegiatan Pembelajaran

### Pre-class (20 menit)

- Membaca Chapter 1-3 dari buku "Clean Code" (Robert C. Martin)
- Setup Git repository untuk proyek kelompok di GitHub
- Install linter Python: `pip install flake8 black`

### In-class (110 menit)

| Waktu | Aktivitas | Metode |
|-------|-----------|--------|
| 0-25 menit | Clean Code: 10 prinsip, naming, functions, PEP 8 | Ceramah + contoh |
| 25-45 menit | Code Smells: 12 jenis dengan before/after | Live coding |
| 45-60 menit | Refactoring: 4 teknik utama (Extract Method, Replace Magic Number, Parameter Object, Polymorphism) | Live coding |
| 60-80 menit | Git Flow: branching strategy, conventional commits | Demo + praktik |
| 80-100 menit | **Workshop**: Code review exercise — review PR partner | Pair review |
| 100-110 menit | **K2: Kuis Design & Construction** | Kuis |

### Post-class (20 menit)

- Mulai coding proyek akhir dengan Git Flow dan conventional commits
- Setup branch protection rules di GitHub repository
- Persiapan UTS: review seluruh materi Minggu 1-7

---

## Latihan & Diskusi

### Soal 1 (C3 — Menerapkan)

Identifikasi **minimal 5 code smells** dalam kode berikut dan jelaskan refactoring yang tepat untuk masing-masing:

```python
def p(d, u, s):
    r = []
    for i in d:
        if i['type'] == 'buku' and i['stok'] > 0:
            if u.status == 1 and u.pinjam < 5:
                i['available'] = True
                r.append(i)
                import smtplib
                server = smtplib.SMTP('smtp.gmail.com')
                server.send_message(f"Buku {i['judul']} tersedia")
    conn = sqlite3.connect('db.sqlite')
    c = conn.cursor()
    c.execute(f"INSERT INTO log VALUES ('{u.id}', '{len(r)}')")
    conn.commit()
    return r
```

### Soal 2 (C4 — Menganalisis)

Bandingkan Git Flow dan GitHub Flow. Untuk proyek akhir kuliah RPL (tim 4 orang, 4 sprint, Flask web app), mana yang lebih cocok? Jelaskan alasannya dan gambarkan alur branch-nya.

### Soal 3 (C3 — Menerapkan)

Tulis ulang fungsi berikut mengikuti prinsip Clean Code (PEP 8, meaningful names, small functions, DRY):

```python
def f(x,y):
 if x>0:
  if y>0:
   r=x*y*0.1
   if r>100000:
    r=100000
   return r
  else:
   return 0
 else:
  return 0
```

### Soal 4 (C3 — Menerapkan)

Buatlah 5 contoh commit message menggunakan Conventional Commits format untuk skenario pengembangan fitur "peminjaman buku" di proyek perpustakaan digital. Pastikan mencakup minimal 3 tipe commit yang berbeda.

### Soal 5 (C4 — Menganalisis)

Anda melakukan code review pada PR teman. Tuliskan 3 review comments yang **konstruktif** (bukan hanya "ini salah") untuk kode berikut:

```python
def get_data(id):
    data = db.execute(f"SELECT * FROM users WHERE id = {id}")
    if data:
        return {"name": data[0], "email": data[1], "password": data[2]}
    return None
```

---

## Penugasan

### K2: Kuis Design & Construction (3% nilai akhir)

| Komponen | Detail |
|----------|--------|
| **Cakupan** | Minggu 5-7 (Arsitektur, SOLID, Design Patterns, UML, ERD, Clean Code, Git) |
| **Durasi** | 20 menit |
| **Format** | 10 Pilihan Ganda + 2 Analisis Kode Singkat |
| **Sifat** | Closed-book, tanpa AI/internet |

---

## Referensi

1. Martin, R. C. (2009). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall.
2. Fowler, M. (2019). *Refactoring: Improving the Design of Existing Code* (2nd ed.). Addison-Wesley.
3. Chacon, S. & Straub, B. (2014). *Pro Git* (2nd ed.). Apress. https://git-scm.com/book
4. Driessen, V. (2010). "A successful Git branching model." https://nvie.com/posts/a-successful-git-branching-model/
5. PEP 8 — Style Guide for Python Code. https://peps.python.org/pep-0008/
6. Conventional Commits. https://www.conventionalcommits.org/

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
