# Minggu 6: Desain Perangkat Lunak — UML dan Database Design

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak |
| **Kode** | IF2205 |
| **Minggu** | 6 dari 16 |
| **Topik** | UML Diagrams, Database Design, API Design (REST) |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **CPMK** | CPMK-3 |
| **Sub-CPMK** | 3.3 (UML structural & behavioral), 3.4 (Database design & normalisasi) |
| **Durasi** | 150 menit (3 × 50 menit) |
| **Metode** | Ceramah, live modeling, praktik desain |

## Tujuan Pembelajaran

1. **Membuat** Class Diagram, Sequence Diagram, dan Activity Diagram menggunakan UML (C3)
2. **Merancang** skema database relasional dengan normalisasi hingga 3NF (C3)
3. **Mendesain** RESTful API endpoint untuk web application (C3)

## Materi Pembelajaran

### 6.1 UML (Unified Modeling Language)

UML adalah bahasa standar untuk memodelkan sistem software. Ada 2 kategori utama:

#### Structural Diagrams (Statis)

**Class Diagram** — menggambarkan struktur class dan relasinya:
```
┌──────────────────┐       1     *  ┌──────────────────┐
│      User        │──────────────▶│    Peminjaman     │
├──────────────────┤               ├──────────────────┤
│ - id: int        │               │ - id: int        │
│ - nama: str      │               │ - tanggal: date  │
│ - email: str     │               │ - status: str    │
├──────────────────┤               ├──────────────────┤
│ + register()     │               │ + create()       │
│ + login()        │               │ + return_book()  │
└──────────────────┘               └──────────────────┘
         │                                  │
         │                                  │ *
         │                            ┌─────┴──────────┐
         │                            │      Buku       │
         │                            ├────────────────┤
         │                            │ - id: int      │
         │                            │ - judul: str   │
         │                            │ - penulis: str │
         │                            │ - stok: int    │
         │                            ├────────────────┤
         │                            │ + search()     │
         │                            │ + update_stok()│
         │                            └────────────────┘
```

**Relasi dalam Class Diagram:**

| Relasi | Simbol | Contoh |
|--------|--------|--------|
| Association | ─── | User meminjam Buku |
| Aggregation | ◇─── | Perpustakaan memiliki Buku |
| Composition | ◆─── | Order terdiri dari OrderItem |
| Inheritance | △─── | Admin extends User |
| Dependency | - - -▶ | Controller depends on Service |

#### Behavioral Diagrams (Dinamis)

**Sequence Diagram** — menggambarkan interaksi antar objek dari waktu ke waktu:
```
  User         Controller      Service       Database
   │               │              │              │
   │──── login ───▶│              │              │
   │               │── validate ─▶│              │
   │               │              │── query ────▶│
   │               │              │◀── result ───│
   │               │◀─ user obj ──│              │
   │◀── response ──│              │              │
   │               │              │              │
```

**Activity Diagram** — menggambarkan alur proses (mirip flowchart):
```
  (●) Start
   │
   ▼
  [Masukkan Username & Password]
   │
   ◇ Valid?
  / \
 Ya   Tidak
 │      │
 ▼      ▼
[Dashboard]  [Error Message]
 │            │
 │            ▼
 │     [Kembali ke Login]
 │            │
 ▼            │
(●) End ◀─────┘
```

### 6.2 Database Design

#### Entity-Relationship Diagram (ERD)

Contoh ERD untuk Sistem Perpustakaan:
```
┌──────────┐     1:N     ┌──────────────┐     N:1     ┌──────────┐
│   User   │────────────▶│  Peminjaman   │◀───────────│   Buku   │
│          │             │              │             │          │
│ PK: id   │             │ PK: id       │             │ PK: id   │
│ nama     │             │ FK: user_id  │             │ judul    │
│ email    │             │ FK: buku_id  │             │ penulis  │
│ password │             │ tanggal_pinjam│            │ isbn     │
└──────────┘             │ tanggal_kembali│           │ stok     │
                         │ status       │             └──────────┘
                         └──────────────┘
```

#### Normalisasi Database

| Normal Form | Aturan | Contoh Pelanggaran |
|-------------|--------|--------------------|
| **1NF** | Setiap kolom bernilai atomik (tunggal) | Kolom "telepon" berisi "081xxx, 082xxx" |
| **2NF** | Memenuhi 1NF + setiap non-key bergantung pada seluruh primary key | Nama_mahasiswa tergantung hanya pada NIM, bukan NIM+Kode_MK |
| **3NF** | Memenuhi 2NF + tidak ada transitive dependency | Nama_dosen tergantung pada Kode_dosen, bukan pada primary key |

#### Implementasi dengan SQLAlchemy (Python)
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    peminjaman = db.relationship('Peminjaman', backref='user')

class Buku(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String(200), nullable=False)
    penulis = db.Column(db.String(100))
    stok = db.Column(db.Integer, default=0)

class Peminjaman(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    buku_id = db.Column(db.Integer, db.ForeignKey('buku.id'))
    tanggal_pinjam = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), default='dipinjam')
```

### 6.3 RESTful API Design

#### Prinsip REST

| Prinsip | Deskripsi |
|---------|-----------|
| Stateless | Setiap request independen, tidak bergantung state sebelumnya |
| Resource-based | URL merepresentasikan resource (noun, bukan verb) |
| HTTP Methods | GET (baca), POST (buat), PUT (update penuh), PATCH (update parsial), DELETE (hapus) |
| JSON | Format data standar untuk request dan response |

#### Contoh API Endpoint Perpustakaan

| Method | Endpoint | Deskripsi |
|--------|----------|-----------|
| GET | `/api/buku` | Daftar semua buku |
| GET | `/api/buku/{id}` | Detail satu buku |
| POST | `/api/buku` | Tambah buku baru |
| PUT | `/api/buku/{id}` | Update data buku |
| DELETE | `/api/buku/{id}` | Hapus buku |
| POST | `/api/peminjaman` | Buat peminjaman baru |
| PATCH | `/api/peminjaman/{id}/return` | Kembalikan buku |

#### Implementasi Flask API
```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/buku', methods=['GET'])
def get_buku():
    buku_list = Buku.query.all()
    return jsonify([{
        'id': b.id,
        'judul': b.judul,
        'penulis': b.penulis,
        'stok': b.stok
    } for b in buku_list])

@app.route('/api/buku', methods=['POST'])
def create_buku():
    data = request.get_json()
    buku = Buku(judul=data['judul'], penulis=data['penulis'], stok=data['stok'])
    db.session.add(buku)
    db.session.commit()
    return jsonify({'id': buku.id, 'message': 'Buku berhasil ditambahkan'}), 201
```

## Kegiatan Pembelajaran

### Pre-class (15 menit)
- Review materi Class Diagram dari Bab 6 buku ajar
- Install ekstensi PlantUML/Mermaid di editor

### In-class (120 menit)

| Waktu | Aktivitas | Metode |
|-------|-----------|--------|
| 0-30 menit | UML: Class Diagram, Sequence Diagram, Activity Diagram | Ceramah + demo |
| 30-55 menit | Database Design: ERD, Normalisasi (1NF-3NF) | Ceramah + contoh |
| 55-80 menit | **Praktik**: Desain ERD dan Class Diagram untuk proyek kelompok | Workshop |
| 80-110 menit | RESTful API Design + implementasi Flask | Live coding |
| 110-120 menit | Q&A dan preview minggu depan | Diskusi |

### Post-class (15 menit)
- Lengkapi desain UML dan ERD untuk proyek kelompok
- Persiapan: Baca tentang Clean Code dan Code Review

## Penugasan

**T3: UML & Database Design** (2.5% nilai akhir)
- **Deliverable:** Class Diagram + Sequence Diagram + ERD + API endpoint list untuk proyek akhir
- **AI Policy:** AI diizinkan + AI Usage Log

## Referensi

1. Fowler, M. (2003). *UML Distilled* (3rd ed.). Addison-Wesley.
2. Elmasri, R. & Navathe, S. (2016). *Fundamentals of Database Systems* (7th ed.).
3. Fielding, R. T. (2000). *Architectural Styles and the Design of Network-based Software Architectures*. Doctoral Dissertation.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
