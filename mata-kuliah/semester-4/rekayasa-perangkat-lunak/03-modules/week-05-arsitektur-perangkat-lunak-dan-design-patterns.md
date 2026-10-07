# Minggu 5: Arsitektur Perangkat Lunak dan Design Patterns

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak |
| **Kode** | IF2205 |
| **Minggu** | 5 dari 16 |
| **Topik** | Architectural Styles, Quality Attributes, SOLID Principles, Design Patterns, C4 Model |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **Bahasa Pemrograman** | Python 3.x + JavaScript |
| **CPMK** | CPMK-3 |
| **Sub-CPMK** | 3.1 (Arsitektur & quality attributes), 3.2 (SOLID & design patterns) |
| **Durasi** | 150 menit (3 x 50 menit) |
| **Metode** | Ceramah, analisis arsitektur real-world apps, live coding |

## Tujuan Pembelajaran

Setelah mengikuti perkuliahan minggu ini, mahasiswa mampu:

1. **Menganalisis** minimal 5 architectural styles dan memilih yang sesuai berdasarkan quality attributes (C4)
2. **Menerapkan** 5 prinsip SOLID dalam desain software menggunakan Python (C3)
3. **Mengimplementasikan** 4 design patterns (Singleton, Factory, Observer, Strategy) di Python (C3)
4. **Menjelaskan** C4 Model untuk dokumentasi arsitektur dan menulis Architecture Decision Record (ADR) (C2)

---

## Materi Pembelajaran

### 5.1 Arsitektur Perangkat Lunak — Fondasi Desain Sistem

#### 5.1.1 Apa Itu Software Architecture?

> **Software Architecture** adalah struktur fundamental dari sebuah sistem software, yang terdiri dari komponen-komponen software, hubungan antar komponen, dan prinsip-prinsip yang mengatur desain dan evolusinya (Bass, Clements & Kazman, 2012).

```
┌─────────────────────────────────────────────────────────────────┐
│          MENGAPA ARSITEKTUR PENTING?                             │
│                                                                  │
│  1. Kualitas Sistem                                             │
│     Arsitektur menentukan apakah sistem bisa scale,             │
│     mudah dimaintain, dan reliable                              │
│                                                                  │
│  2. Komunikasi Tim                                              │
│     Arsitektur menjadi "bahasa bersama" antara developer,       │
│     product owner, dan stakeholder                              │
│                                                                  │
│  3. Keputusan Awal yang Mahal                                   │
│     Mengubah arsitektur setelah coding = sangat mahal           │
│     (seperti mengubah fondasi rumah setelah dibangun)           │
│                                                                  │
│  4. Constraint & Guideline                                      │
│     Memberikan batasan dan panduan bagi developer               │
│     tentang bagaimana kode harus diorganisir                    │
│                                                                  │
│  Analogi: Arsitektur software = denah rumah                     │
│  Anda tidak mulai membangun rumah tanpa denah!                  │
└─────────────────────────────────────────────────────────────────┘
```

#### 5.1.2 Quality Attributes (Non-Functional Requirements)

Quality attributes menentukan pemilihan arsitektur:

| Quality Attribute | Deskripsi | Contoh Metrik | Arsitektur yang Cocok |
|-------------------|-----------|---------------|----------------------|
| **Performance** | Kecepatan respon sistem | Response time < 200ms | Microservices, Event-driven |
| **Scalability** | Kemampuan menangani beban bertambah | 10K -> 100K concurrent users | Microservices |
| **Maintainability** | Kemudahan modifikasi kode | Waktu untuk fix bug < 2 jam | Layered, Modular Monolith |
| **Availability** | Uptime sistem | 99.9% uptime | Microservices + redundancy |
| **Security** | Perlindungan dari ancaman | 0 critical vulnerabilities | Layered (defense in depth) |
| **Testability** | Kemudahan pengujian | Code coverage > 80% | Layered, MVC |

### 5.2 Lima Architectural Styles

#### 5.2.1 Monolithic Architecture

Seluruh aplikasi dalam satu codebase dan satu unit deployment.

```
┌─────────────────────────────────────────────────────────────────┐
│                    MONOLITHIC ARCHITECTURE                        │
│                                                                  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │                    SATU APLIKASI                           │  │
│  │                                                           │  │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐ │  │
│  │  │  Auth    │  │  Product │  │  Order   │  │  Payment │ │  │
│  │  │  Module  │  │  Module  │  │  Module  │  │  Module  │ │  │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────┘ │  │
│  │                                                           │  │
│  │  ┌─────────────────────────────────────────────────────┐ │  │
│  │  │              Shared Database (1 database)            │ │  │
│  │  └─────────────────────────────────────────────────────┘ │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                  │
│  Deploy: 1 unit  |  Scale: Vertikal  |  Cocok: MVP, startup     │
│                                                                  │
│  Contoh Indonesia: Sistem Akademik kampus kecil, UMKM app       │
└─────────────────────────────────────────────────────────────────┘
```

```python
# Contoh struktur monolithic Flask application
# Semua modul dalam satu proses dan satu database

from flask import Flask, jsonify, request

app = Flask(__name__)

# --- Auth Module ---
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    # Validasi login langsung di sini
    return jsonify({"token": "jwt-token-here"})

# --- Product Module ---
@app.route('/api/products', methods=['GET'])
def get_products():
    # Query langsung ke shared database
    return jsonify({"products": []})

# --- Order Module ---
@app.route('/api/orders', methods=['POST'])
def create_order():
    # Akses product DAN payment langsung
    return jsonify({"order_id": 1})

# Semua jadi satu proses, satu database, satu deployment
if __name__ == '__main__':
    app.run(port=5000)
```

#### 5.2.2 Layered Architecture

Memisahkan concern ke dalam layer-layer yang bertanggung jawab untuk satu aspek.

```
┌─────────────────────────────────────────────────────────────────┐
│                   LAYERED ARCHITECTURE                           │
│                                                                  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  PRESENTATION LAYER                                       │  │
│  │  HTML, CSS, JavaScript, Template (Jinja2)                 │  │
│  │  Tanggung jawab: Menampilkan data ke user                 │  │
│  └─────────────────────────┬─────────────────────────────────┘  │
│                            │ request/response                    │
│  ┌─────────────────────────┴─────────────────────────────────┐  │
│  │  BUSINESS LOGIC LAYER (Service Layer)                     │  │
│  │  Flask routes, validation, business rules                 │  │
│  │  Tanggung jawab: Memproses logika bisnis                  │  │
│  └─────────────────────────┬─────────────────────────────────┘  │
│                            │ method calls                        │
│  ┌─────────────────────────┴─────────────────────────────────┐  │
│  │  DATA ACCESS LAYER (Repository Layer)                     │  │
│  │  SQLAlchemy models, queries, ORM                          │  │
│  │  Tanggung jawab: Mengakses dan menyimpan data             │  │
│  └─────────────────────────┬─────────────────────────────────┘  │
│                            │ SQL queries                         │
│  ┌─────────────────────────┴─────────────────────────────────┐  │
│  │  DATABASE LAYER                                           │  │
│  │  SQLite / PostgreSQL                                      │  │
│  │  Tanggung jawab: Menyimpan data secara persisten          │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                  │
│  Aturan: Layer hanya boleh memanggil layer DI BAWAHNYA          │
│  Presentation -> Business Logic -> Data Access -> Database      │
└─────────────────────────────────────────────────────────────────┘
```

```python
# Implementasi Layered Architecture di Flask

# === DATA ACCESS LAYER (repository) ===
class BukuRepository:
    """Hanya bertanggung jawab untuk operasi database."""
    
    def get_all(self):
        return Buku.query.all()
    
    def get_by_id(self, buku_id):
        return Buku.query.get_or_404(buku_id)
    
    def create(self, judul, penulis, stok):
        buku = Buku(judul=judul, penulis=penulis, stok=stok)
        db.session.add(buku)
        db.session.commit()
        return buku

# === BUSINESS LOGIC LAYER (service) ===
class BukuService:
    """Logika bisnis — validasi, aturan, transformasi."""
    
    def __init__(self):
        self.repo = BukuRepository()
    
    def get_available_books(self):
        """Hanya buku dengan stok > 0."""
        semua_buku = self.repo.get_all()
        return [b for b in semua_buku if b.stok > 0]
    
    def tambah_buku(self, judul, penulis, stok):
        """Validasi sebelum menyimpan."""
        if not judul or len(judul) < 3:
            raise ValueError("Judul buku minimal 3 karakter")
        if stok < 0:
            raise ValueError("Stok tidak boleh negatif")
        return self.repo.create(judul, penulis, stok)

# === PRESENTATION LAYER (route/controller) ===
buku_service = BukuService()

@app.route('/api/buku', methods=['GET'])
def get_buku():
    """Hanya mengatur request/response — tanpa logika bisnis."""
    buku_list = buku_service.get_available_books()
    return jsonify([{
        'id': b.id, 'judul': b.judul, 'penulis': b.penulis, 'stok': b.stok
    } for b in buku_list])
```

#### 5.2.3 MVC (Model-View-Controller)

```
┌─────────────────────────────────────────────────────────────────┐
│                MVC ARCHITECTURE                                  │
│                                                                  │
│       ┌──────────────┐                                          │
│       │   Browser    │                                          │
│       │   (User)     │                                          │
│       └──────┬───────┘                                          │
│              │ HTTP Request                                      │
│              ▼                                                   │
│       ┌──────────────┐       ┌──────────────┐                  │
│       │  Controller  │──────▶│    Model     │                  │
│       │ (Flask route)│       │ (SQLAlchemy) │                  │
│       │              │◀──────│              │                  │
│       └──────┬───────┘ data  └──────────────┘                  │
│              │                       │                           │
│              │ render                │ query/update              │
│              ▼                       ▼                           │
│       ┌──────────────┐       ┌──────────────┐                  │
│       │    View      │       │   Database   │                  │
│       │  (Jinja2     │       │   (SQLite)   │                  │
│       │   template)  │       └──────────────┘                  │
│       └──────┬───────┘                                          │
│              │ HTML Response                                     │
│              ▼                                                   │
│       ┌──────────────┐                                          │
│       │   Browser    │                                          │
│       └──────────────┘                                          │
│                                                                  │
│  Flask secara natural mengikuti pola MVC:                       │
│  - Model: SQLAlchemy models                                     │
│  - View: Jinja2 templates atau JSON responses                   │
│  - Controller: Flask route functions                             │
└─────────────────────────────────────────────────────────────────┘
```

#### 5.2.4 Microservices Architecture

Aplikasi dipecah menjadi layanan-layanan kecil yang independen.

```
┌─────────────────────────────────────────────────────────────────┐
│              MICROSERVICES ARCHITECTURE                           │
│                                                                  │
│  ┌──────────┐                                                   │
│  │  Client  │                                                   │
│  └────┬─────┘                                                   │
│       │                                                          │
│  ┌────┴─────────────────────────────────┐                       │
│  │         API GATEWAY                   │                       │
│  │    (routing, auth, rate limiting)     │                       │
│  └──┬──────────┬──────────┬─────────────┘                       │
│     │          │          │                                      │
│     ▼          ▼          ▼                                      │
│  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐                       │
│  │ User │  │Product│  │Order │  │Payment│                       │
│  │Service│  │Service│  │Service│  │Service│                      │
│  │:5001 │  │:5002 │  │:5003 │  │:5004 │                       │
│  └──┬───┘  └──┬───┘  └──┬───┘  └──┬───┘                       │
│     │         │         │         │                              │
│  ┌──┴──┐  ┌──┴──┐  ┌──┴──┐  ┌──┴──┐                          │
│  │ DB1 │  │ DB2 │  │ DB3 │  │ DB4 │                          │
│  └─────┘  └─────┘  └─────┘  └─────┘                          │
│                                                                  │
│  Setiap service: own database, own deployment, own team         │
│                                                                  │
│  Contoh Indonesia: Gojek (GoRide, GoFood, GoPay = services)    │
│  Tokopedia: Product Service, Order Service, Payment Service     │
└─────────────────────────────────────────────────────────────────┘
```

#### 5.2.5 Event-Driven Architecture

Komponen berkomunikasi melalui *events* (pesan asinkron).

```
┌─────────────────────────────────────────────────────────────────┐
│            EVENT-DRIVEN ARCHITECTURE                             │
│                                                                  │
│  ┌──────────┐   publish    ┌─────────────────┐                 │
│  │  Order   │─────────────▶│  MESSAGE BROKER  │                 │
│  │  Service │  "order.created" │(RabbitMQ/Kafka)│                │
│  └──────────┘              └────┬────┬────┬──┘                 │
│                                 │    │    │                      │
│                     subscribe   │    │    │  subscribe           │
│                                 ▼    │    ▼                      │
│                          ┌──────┐   │   ┌──────────┐           │
│                          │Payment│   │   │Notification│          │
│                          │Service│   │   │ Service   │          │
│                          └──────┘   │   └──────────┘           │
│                                     │                            │
│                                     ▼                            │
│                              ┌──────────┐                       │
│                              │Inventory │                       │
│                              │ Service  │                       │
│                              └──────────┘                       │
│                                                                  │
│  Keuntungan: Loose coupling — services tidak saling kenal       │
│  Contoh: TransJakarta real-time tracking (bus publish lokasi,   │
│  dashboard dan app subscribe untuk update posisi)               │
└─────────────────────────────────────────────────────────────────┘
```

#### 5.2.6 Perbandingan Architectural Styles

| Aspek | Monolithic | Layered | MVC | Microservices | Event-Driven |
|-------|-----------|---------|-----|---------------|-------------|
| **Complexity** | Rendah | Sedang | Sedang | Tinggi | Tinggi |
| **Scalability** | Vertikal | Vertikal | Vertikal | Horizontal | Horizontal |
| **Deployment** | 1 unit | 1 unit | 1 unit | Independen | Independen |
| **Team size** | 1-5 | 3-10 | 3-10 | 10+ (per service) | 10+ |
| **Cocok untuk** | MVP, startup | Proyek menengah | Web app | Enterprise | Real-time |
| **Contoh** | UMKM app | Sistem Akademik | Flask app | Gojek | TransJakarta tracking |

### 5.3 SOLID Principles — Lima Prinsip Desain OOP

#### 5.3.1 Single Responsibility Principle (SRP)

> Setiap class harus memiliki **satu dan hanya satu** alasan untuk berubah.

```python
# BURUK: Satu class melakukan terlalu banyak hal
class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    
    def simpan_ke_database(self):
        # SQL insert... — tanggung jawab persistence
        pass
    
    def kirim_email(self, pesan):
        # SMTP send... — tanggung jawab notifikasi
        pass
    
    def generate_pdf_rapor(self):
        # PDF generation... — tanggung jawab reporting
        pass


# BAIK: Setiap class punya satu tanggung jawab
class Mahasiswa:
    """Hanya menyimpan data mahasiswa."""
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

class MahasiswaRepository:
    """Hanya bertanggung jawab untuk persistence."""
    def simpan(self, mahasiswa: Mahasiswa):
        db.session.add(mahasiswa)
        db.session.commit()

class EmailService:
    """Hanya bertanggung jawab untuk pengiriman email."""
    def kirim(self, penerima, pesan):
        # SMTP logic di sini
        pass

class RaporGenerator:
    """Hanya bertanggung jawab untuk pembuatan rapor."""
    def generate_pdf(self, mahasiswa: Mahasiswa):
        # PDF generation di sini
        pass
```

#### 5.3.2 Open/Closed Principle (OCP)

> Software entities harus **terbuka untuk ekstensi**, tapi **tertutup untuk modifikasi**.

```python
# BURUK: Harus memodifikasi kode setiap kali ada tipe baru
class PerhitunganDiskon:
    def hitung(self, tipe_pelanggan, total):
        if tipe_pelanggan == "reguler":
            return total * 0.05
        elif tipe_pelanggan == "premium":
            return total * 0.10
        elif tipe_pelanggan == "vip":
            return total * 0.15
        # Setiap tipe baru = modifikasi method ini!


# BAIK: Tambah tipe baru tanpa mengubah kode yang sudah ada
from abc import ABC, abstractmethod

class StrategiDiskon(ABC):
    @abstractmethod
    def hitung_diskon(self, total: float) -> float:
        pass

class DiskonReguler(StrategiDiskon):
    def hitung_diskon(self, total: float) -> float:
        return total * 0.05

class DiskonPremium(StrategiDiskon):
    def hitung_diskon(self, total: float) -> float:
        return total * 0.10

class DiskonVIP(StrategiDiskon):
    def hitung_diskon(self, total: float) -> float:
        return total * 0.15

# Tambah diskon baru tanpa mengubah kode yang sudah ada
class DiskonMahasiswa(StrategiDiskon):
    def hitung_diskon(self, total: float) -> float:
        return total * 0.20  # Diskon khusus mahasiswa

class KasirService:
    def proses_pembayaran(self, total: float, strategi: StrategiDiskon) -> float:
        diskon = strategi.hitung_diskon(total)
        return total - diskon

# Penggunaan
kasir = KasirService()
print(kasir.proses_pembayaran(100_000, DiskonMahasiswa()))  # 80000.0
```

#### 5.3.3 Liskov Substitution Principle (LSP)

> Objek subclass harus bisa **menggantikan** objek parent class tanpa merusak program.

```python
# BURUK: Melanggar LSP — Square mengubah perilaku Rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    # Jika ada setter, mengubah width juga mengubah height
    # Ini melanggar ekspektasi Rectangle


# BAIK: Gunakan abstraksi yang benar
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self) -> float:
        return self.side ** 2

# Keduanya bisa digunakan di mana saja Shape diharapkan
def print_area(shape: Shape):
    print(f"Luas: {shape.area()}")

print_area(Rectangle(5, 10))  # Luas: 50
print_area(Square(5))          # Luas: 25
```

#### 5.3.4 Interface Segregation Principle (ISP)

> Client tidak boleh dipaksa bergantung pada interface yang tidak digunakannya.

```python
# BURUK: Interface terlalu besar
from abc import ABC, abstractmethod

class MesinMultifungsi(ABC):
    @abstractmethod
    def print_doc(self, doc): pass
    @abstractmethod
    def scan_doc(self, doc): pass
    @abstractmethod
    def fax_doc(self, doc): pass

class PrinterSederhana(MesinMultifungsi):
    def print_doc(self, doc):
        print(f"Mencetak: {doc}")
    def scan_doc(self, doc):
        raise NotImplementedError("Printer ini tidak bisa scan!")
    def fax_doc(self, doc):
        raise NotImplementedError("Printer ini tidak bisa fax!")


# BAIK: Interface dipecah sesuai kebutuhan
class Printable(ABC):
    @abstractmethod
    def print_doc(self, doc): pass

class Scannable(ABC):
    @abstractmethod
    def scan_doc(self, doc): pass

class Faxable(ABC):
    @abstractmethod
    def fax_doc(self, doc): pass

class PrinterSederhana(Printable):
    def print_doc(self, doc):
        print(f"Mencetak: {doc}")

class MesinKantor(Printable, Scannable, Faxable):
    def print_doc(self, doc): print(f"Mencetak: {doc}")
    def scan_doc(self, doc): print(f"Scanning: {doc}")
    def fax_doc(self, doc): print(f"Faxing: {doc}")
```

#### 5.3.5 Dependency Inversion Principle (DIP)

> Modul high-level tidak boleh bergantung pada modul low-level. Keduanya harus bergantung pada **abstraksi**.

```python
# BURUK: Service langsung bergantung pada implementasi MySQL
class MySQLDatabase:
    def query(self, sql):
        return f"MySQL result for: {sql}"

class LaporanService:
    def __init__(self):
        self.db = MySQLDatabase()  # Tightly coupled ke MySQL!
    
    def get_laporan(self):
        return self.db.query("SELECT * FROM laporan")


# BAIK: Bergantung pada abstraksi (interface)
from abc import ABC, abstractmethod

class DatabaseInterface(ABC):
    @abstractmethod
    def query(self, sql: str) -> str:
        pass

class MySQLDatabase(DatabaseInterface):
    def query(self, sql: str) -> str:
        return f"MySQL result for: {sql}"

class SQLiteDatabase(DatabaseInterface):
    def query(self, sql: str) -> str:
        return f"SQLite result for: {sql}"

class LaporanService:
    def __init__(self, db: DatabaseInterface):  # Dependency Injection
        self.db = db
    
    def get_laporan(self):
        return self.db.query("SELECT * FROM laporan")

# Bisa ganti database tanpa mengubah LaporanService
service_mysql = LaporanService(MySQLDatabase())
service_sqlite = LaporanService(SQLiteDatabase())
print(service_mysql.get_laporan())   # MySQL result for: SELECT * FROM laporan
print(service_sqlite.get_laporan())  # SQLite result for: SELECT * FROM laporan
```

#### 5.3.6 Ringkasan SOLID

```
┌─────────────────────────────────────────────────────────────────┐
│                    SOLID PRINCIPLES                               │
│                                                                  │
│  S — Single Responsibility    Satu class = satu tanggung jawab  │
│  O — Open/Closed              Ekstensi: ya. Modifikasi: tidak   │
│  L — Liskov Substitution      Subclass bisa gantikan parent     │
│  I — Interface Segregation    Interface kecil dan spesifik      │
│  D — Dependency Inversion     Bergantung pada abstraksi         │
│                                                                  │
│  Manfaat menerapkan SOLID:                                      │
│  - Kode mudah di-test (unit test)                               │
│  - Kode mudah di-maintain (perubahan terisolasi)                │
│  - Kode mudah di-extend (fitur baru tanpa merusak yang ada)     │
│  - Kode mudah dipahami (separation of concerns)                 │
└─────────────────────────────────────────────────────────────────┘
```

### 5.4 Design Patterns — Solusi Teruji untuk Masalah Umum

#### 5.4.1 Apa Itu Design Pattern?

Design patterns (GoF — Gang of Four, 1994) adalah **solusi yang telah teruji** untuk masalah desain yang sering muncul. Bukan kode jadi, tapi *template* yang bisa diadaptasi.

```
┌─────────────────────────────────────────────────────────────────┐
│                KATEGORI DESIGN PATTERNS (GoF)                    │
│                                                                  │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐   │
│  │   CREATIONAL   │  │   STRUCTURAL   │  │   BEHAVIORAL   │   │
│  │                │  │                │  │                │   │
│  │  Singleton *   │  │  Adapter       │  │  Observer *    │   │
│  │  Factory *     │  │  Decorator     │  │  Strategy *    │   │
│  │  Builder       │  │  Facade        │  │  Command       │   │
│  │  Prototype     │  │  Composite     │  │  State         │   │
│  └────────────────┘  └────────────────┘  └────────────────┘   │
│                                                                  │
│  * = yang dipelajari di minggu ini                              │
└─────────────────────────────────────────────────────────────────┘
```

#### 5.4.2 Singleton Pattern

```python
# Singleton: Memastikan hanya ada SATU instance dari sebuah class
# Use case: Database connection, configuration, logger

class DatabaseConnection:
    """Singleton — hanya satu koneksi database untuk seluruh aplikasi."""
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = "Connected to SQLite: perpustakaan.db"
            cls._instance.query_count = 0
            print("[Singleton] Koneksi database dibuat")
        return cls._instance
    
    def execute(self, query):
        self.query_count += 1
        return f"Hasil query #{self.query_count}: {query}"

# Penggunaan — keduanya adalah objek yang SAMA
db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1 is db2)                          # True
print(db1.execute("SELECT * FROM buku"))    # Hasil query #1: ...
print(db2.execute("SELECT * FROM user"))    # Hasil query #2: ...
print(f"Total queries: {db1.query_count}")  # Total queries: 2
```

#### 5.4.3 Factory Pattern

```python
# Factory: Menyerahkan pembuatan objek ke factory method
# Use case: Notifikasi multi-channel (email, SMS, WhatsApp)

from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> str:
        pass

class EmailNotification(Notification):
    def send(self, recipient: str, message: str) -> str:
        return f"[EMAIL] Ke {recipient}: {message}"

class SMSNotification(Notification):
    def send(self, recipient: str, message: str) -> str:
        return f"[SMS] Ke {recipient}: {message}"

class WhatsAppNotification(Notification):
    def send(self, recipient: str, message: str) -> str:
        return f"[WHATSAPP] Ke {recipient}: {message}"


class NotificationFactory:
    """Factory — memilih jenis notifikasi yang tepat."""
    
    _registry = {
        "email": EmailNotification,
        "sms": SMSNotification,
        "whatsapp": WhatsAppNotification,
    }
    
    @classmethod
    def create(cls, channel: str) -> Notification:
        notif_class = cls._registry.get(channel.lower())
        if notif_class is None:
            raise ValueError(f"Channel '{channel}' tidak didukung")
        return notif_class()
    
    @classmethod
    def register(cls, channel: str, notif_class):
        """Daftarkan channel baru tanpa modifikasi kode (OCP!)."""
        cls._registry[channel] = notif_class

# Penggunaan
notif = NotificationFactory.create("whatsapp")
print(notif.send("+628123456", "Antrian Anda sudah dipanggil"))
# [WHATSAPP] Ke +628123456: Antrian Anda sudah dipanggil
```

#### 5.4.4 Observer Pattern

```python
# Observer: Satu objek (subject) memberitahu banyak objek (observers)
# Use case: Sistem antrian puskesmas — update ke monitor, WA, dashboard

from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, event: str, data: dict):
        pass

class Subject:
    def __init__(self):
        self._observers = []
    
    def subscribe(self, observer: Observer):
        self._observers.append(observer)
    
    def notify(self, event: str, data: dict):
        for observer in self._observers:
            observer.update(event, data)


class SistemAntrian(Subject):
    def __init__(self):
        super().__init__()
        self.current_number = 0
    
    def panggil_selanjutnya(self, poli: str):
        self.current_number += 1
        data = {"nomor": self.current_number, "poli": poli}
        print(f"\n>>> Memanggil antrian #{self.current_number} - Poli {poli}")
        self.notify("antrian_dipanggil", data)


class DisplayMonitor(Observer):
    def update(self, event: str, data: dict):
        print(f"  [MONITOR] Menampilkan: Nomor {data['nomor']} - {data['poli']}")

class WhatsAppNotifier(Observer):
    def update(self, event: str, data: dict):
        print(f"  [WHATSAPP] Mengirim notifikasi ke pasien #{data['nomor']}")

class DashboardAdmin(Observer):
    def update(self, event: str, data: dict):
        print(f"  [DASHBOARD] Update statistik antrian {data['poli']}")


# Penggunaan
antrian = SistemAntrian()
antrian.subscribe(DisplayMonitor())
antrian.subscribe(WhatsAppNotifier())
antrian.subscribe(DashboardAdmin())

antrian.panggil_selanjutnya("Umum")
# >>> Memanggil antrian #1 - Poli Umum
#   [MONITOR] Menampilkan: Nomor 1 - Umum
#   [WHATSAPP] Mengirim notifikasi ke pasien #1
#   [DASHBOARD] Update statistik antrian Umum
```

#### 5.4.5 Strategy Pattern

```python
# Strategy: Algoritma yang bisa ditukar saat runtime
# Use case: Sistem pembayaran e-commerce (QRIS, transfer, COD)

from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass
    
    @abstractmethod
    def get_fee(self, amount: float) -> float:
        pass

class QRISPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        fee = self.get_fee(amount)
        total = amount + fee
        return f"Pembayaran QRIS: Rp {total:,.0f} (fee Rp {fee:,.0f})"
    
    def get_fee(self, amount: float) -> float:
        return amount * 0.007  # 0.7% MDR

class BankTransferPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        fee = self.get_fee(amount)
        total = amount + fee
        return f"Transfer Bank: Rp {total:,.0f} (fee Rp {fee:,.0f})"
    
    def get_fee(self, amount: float) -> float:
        return 2_500  # Flat fee

class CODPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        fee = self.get_fee(amount)
        total = amount + fee
        return f"COD: Rp {total:,.0f} (fee Rp {fee:,.0f})"
    
    def get_fee(self, amount: float) -> float:
        return 5_000


class Checkout:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy
    
    def process_payment(self, amount: float) -> str:
        return self._strategy.pay(amount)


# Penggunaan — user memilih metode pembayaran
checkout = Checkout(QRISPayment())
print(checkout.process_payment(150_000))
# Pembayaran QRIS: Rp 151,050 (fee Rp 1,050)

checkout.set_strategy(BankTransferPayment())
print(checkout.process_payment(150_000))
# Transfer Bank: Rp 152,500 (fee Rp 2,500)

checkout.set_strategy(CODPayment())
print(checkout.process_payment(150_000))
# COD: Rp 155,000 (fee Rp 5,000)
```

### 5.5 C4 Model — Dokumentasi Arsitektur Bertingkat

```
┌─────────────────────────────────────────────────────────────────┐
│              C4 MODEL (Simon Brown)                              │
│                                                                  │
│  Level 1: CONTEXT                                               │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Siapa yang menggunakan sistem? Sistem eksternal apa?    │   │
│  │  [Mahasiswa] -> [Perpustakaan Digital] -> [Sistem Email] │   │
│  └─────────────────────────────────────────────────────────┘   │
│                         │ zoom in                                │
│  Level 2: CONTAINER                                             │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Aplikasi/database/service apa saja?                     │   │
│  │  [Web App (Flask)] -> [API Server] -> [Database SQLite]  │   │
│  └─────────────────────────────────────────────────────────┘   │
│                         │ zoom in                                │
│  Level 3: COMPONENT                                             │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Komponen utama di dalam setiap container?               │   │
│  │  [Auth Module] [Book Module] [Loan Module] [Report]     │   │
│  └─────────────────────────────────────────────────────────┘   │
│                         │ zoom in                                │
│  Level 4: CODE                                                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Class diagram, sequence diagram (UML)                   │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                  │
│  Tips: Untuk proyek kuliah, Level 1-3 sudah cukup              │
└─────────────────────────────────────────────────────────────────┘
```

### 5.6 Architecture Decision Record (ADR)

ADR mendokumentasikan keputusan arsitektur beserta alasannya.

```markdown
# ADR-001: Memilih Layered Architecture untuk Proyek Perpustakaan

## Status
Accepted

## Context
Tim 4 mahasiswa, pengalaman Flask dasar, deadline 10 minggu (4 sprint).
Proyek: web app perpustakaan kampus dengan ~20 fitur.

## Decision
Menggunakan Layered Architecture (Presentation -> Service -> Repository -> Database).

## Rationale
- Tim kecil — microservices terlalu kompleks
- Familiar dengan Flask — layered mudah dipahami
- Testing lebih mudah — bisa mock per layer

## Alternatives Considered
1. Monolithic tanpa layer — ditolak: sulit di-test
2. Microservices — ditolak: overkill untuk tim 4 orang

## Consequences
- Positif: Kode terorganisir, mudah di-test
- Negatif: Sedikit lebih banyak boilerplate
```

---

## Kegiatan Pembelajaran

### Pre-class (20 menit)

- Membaca tentang MVC architecture di Flask documentation
- Baca artikel: "Microservices vs Monolith — Which to Choose?"
- Review: bagaimana Gojek/Tokopedia membangun arsitektur mereka?

### In-class (110 menit)

| Waktu | Aktivitas | Metode |
|-------|-----------|--------|
| 0-25 menit | Architectural Styles: Monolithic, Layered, MVC, Microservices, Event-Driven | Ceramah + ASCII diagram |
| 25-45 menit | Quality Attributes dan cara memilih arsitektur | Ceramah + diskusi |
| 45-65 menit | SOLID Principles dengan contoh Python (live coding) | Live coding |
| 65-90 menit | Design Patterns: Singleton, Factory, Observer, Strategy | Live coding |
| 90-105 menit | Studi Kasus: "Bagaimana arsitektur Gojek?" + C4 Model + ADR | Diskusi kelompok |
| 105-110 menit | Wrap-up: Arsitektur apa yang cocok untuk proyek akhir? | Q&A |

### Post-class (20 menit)

- Refleksi: Pilih arsitektur untuk proyek akhir kelompok, tulis ADR singkat
- Implementasikan 1 design pattern (Singleton atau Factory) di proyek kelompok
- Preview: UML Diagram dan Database Design minggu depan

---

## Latihan & Diskusi

### Soal 1 (C2 — Memahami)

Jelaskan perbedaan fundamental antara Monolithic Architecture dan Microservices Architecture. Dalam kondisi apa masing-masing arsitektur lebih cocok? Berikan contoh aplikasi Indonesia untuk masing-masing.

### Soal 2 (C3 — Menerapkan)

Identifikasi prinsip SOLID mana yang dilanggar oleh kode berikut, lalu refactor agar sesuai SOLID:

```python
class OrderService:
    def create_order(self, items, user):
        total = sum(item['price'] * item['qty'] for item in items)
        db.execute(f"INSERT INTO orders VALUES ({user.id}, {total})")
        smtp = smtplib.SMTP('smtp.gmail.com')
        smtp.send_message(f"Order Rp {total} berhasil")
        pdf = FPDF()
        pdf.output(f"invoice_{user.id}.pdf")
```

### Soal 3 (C3 — Menerapkan)

Implementasikan Factory Pattern untuk sistem pembayaran parkir di mall Jakarta yang mendukung 3 metode: e-Money (Flazz/Mandiri), QRIS, dan tunai. Setiap metode memiliki tarif berbeda.

### Soal 4 (C4 — Menganalisis)

TransJakarta ingin membangun sistem tracking bus real-time yang menampilkan posisi bus di peta untuk penumpang. Analisis:
a) Architectural style apa yang paling cocok? Jelaskan alasannya.
b) Gambarkan arsitektur high-level menggunakan ASCII diagram.
c) Tulis ADR singkat untuk keputusan arsitektur tersebut.

---

## Referensi

1. Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley.
2. Martin, R. C. (2018). *Clean Architecture: A Craftsman's Guide to Software Structure and Design*. Prentice Hall.
3. Fowler, M. (2002). *Patterns of Enterprise Application Architecture*. Addison-Wesley.
4. Bass, L., Clements, P., & Kazman, R. (2012). *Software Architecture in Practice* (3rd ed.). Addison-Wesley.
5. Brown, S. (2018). *The C4 Model for Visualising Software Architecture*. https://c4model.com/
6. Richards, M. (2022). *Fundamentals of Software Architecture*. O'Reilly Media.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
