# BAB 6: DESAIN PERANGKAT LUNAK DAN UML

**Oleh: Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi | Level Bloom |
|-----------|-----------|-------------|
| 3.3 | Membuat UML diagrams (Class, Sequence, Activity) untuk memodelkan desain software | C3 (Menerapkan) |
| 3.4 | Merancang database (ERD, normalisasi) dan REST API | C3 (Menerapkan) |

---

## 6.1 Unified Modeling Language (UML)

### 6.1.1 Apa Itu UML?

UML adalah bahasa standar untuk **visualisasi, spesifikasi, konstruksi, dan dokumentasi** artefak sistem software. UML v2.5 mendefinisikan 14 jenis diagram, dikelompokkan menjadi:

| Kategori | Diagram | Kegunaan |
|----------|---------|----------|
| **Structural** | Class Diagram | Struktur class dan relasi |
| | Component Diagram | Komponen sistem |
| | Deployment Diagram | Infrastruktur deployment |
| **Behavioral** | Use Case Diagram | Interaksi actor-sistem |
| | Sequence Diagram | Urutan interaksi antar objek |
| | Activity Diagram | Alur proses (flowchart) |
| | State Machine Diagram | Transisi state objek |

Dalam kuliah ini, kita fokus pada **3 diagram paling penting**: Class, Sequence, dan Activity Diagram.

### 6.1.2 Class Diagram

Class Diagram menggambarkan **struktur statis** sistem — class, atribut, method, dan relasi.

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
```

**Visibility modifiers:**
- `+` public — bisa diakses dari mana saja
- `-` private — hanya bisa diakses dari class itu sendiri
- `#` protected — bisa diakses dari class dan subclass

**Relasi:**

| Relasi | Simbol | Deskripsi | Contoh |
|--------|--------|-----------|--------|
| Association | ─── | Hubungan "uses" | User meminjam Buku |
| Aggregation | ◇─── | "Has-a" (bisa hidup terpisah) | Perpustakaan memiliki Buku |
| Composition | ◆─── | "Has-a" (tidak bisa terpisah) | Order terdiri dari OrderItem |
| Inheritance | △─── | "Is-a" | Admin extends User |
| Dependency | - - -▶ | "Uses temporarily" | Controller depends on Service |

**Multiplicity:**
- `1` — tepat satu
- `0..1` — nol atau satu
- `*` atau `0..*` — nol atau banyak
- `1..*` — satu atau banyak

### 6.1.3 Sequence Diagram

Sequence Diagram menggambarkan **interaksi antar objek** dalam urutan waktu.

```
  Browser        Controller       Service        Database
    │                │               │               │
    │── GET /buku ──▶│               │               │
    │                │── get_all() ─▶│               │
    │                │               │── SELECT * ──▶│
    │                │               │◀── rows ──────│
    │                │◀── [buku] ────│               │
    │◀── HTML page ──│               │               │
    │                │               │               │
```

**Elemen Sequence Diagram:**
- **Lifeline** — garis vertikal putus-putus di bawah objek
- **Activation bar** — kotak di lifeline menunjukkan objek sedang aktif
- **Message** — panah horizontal (synchronous: ──▶, asynchronous: - - ▶)
- **Return** — panah putus-putus kembali (◀── ── ──)
- **Alt/Opt/Loop** — fragment untuk kondisi dan perulangan

### 6.1.4 Activity Diagram

Activity Diagram menggambarkan **alur proses** (mirip flowchart tapi lebih terstruktur).

```
  (●) Start
   │
   ▼
  [User membuka halaman login]
   │
   ▼
  [Masukkan username & password]
   │
   ▼
   ◇── Credentials valid? 
  / \
 Ya   Tidak
 │      │
 ▼      ▼
[Redirect    [Tampilkan error]
 Dashboard]       │
 │                ▼
 │         [Kembali ke form login]
 │                │
 ▼                │
(●) End ◀─────────┘
```

## 6.2 Database Design

### 6.2.1 Entity-Relationship Diagram (ERD)

ERD menggambarkan entitas, atribut, dan relasi dalam database.

```
┌──────────┐     1:N     ┌──────────────┐     N:1     ┌──────────┐
│   User   │────────────▶│  Peminjaman   │◀───────────│   Buku   │
│          │             │              │             │          │
│ PK: id   │             │ PK: id       │             │ PK: id   │
│ nama     │             │ FK: user_id  │             │ judul    │
│ email    │             │ FK: buku_id  │             │ penulis  │
│ password │             │ tgl_pinjam   │             │ isbn     │
└──────────┘             │ tgl_kembali  │             │ stok     │
                         │ status       │             └──────────┘
                         └──────────────┘
```

### 6.2.2 Normalisasi

| Normal Form | Aturan | Contoh Pelanggaran |
|-------------|--------|--------------------|
| **1NF** | Setiap kolom bernilai atomik | "081xxx, 082xxx" dalam satu kolom telepon |
| **2NF** | 1NF + non-key bergantung pada SELURUH primary key | Partial dependency pada composite key |
| **3NF** | 2NF + tidak ada transitive dependency | nama_dosen bergantung pada kode_dosen, bukan PK |

### 6.2.3 Implementasi SQLAlchemy ORM

```python
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    peminjaman = db.relationship('Peminjaman', backref='user', lazy=True)

class Buku(db.Model):
    __tablename__ = 'buku'
    id = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String(200), nullable=False)
    penulis = db.Column(db.String(100))
    isbn = db.Column(db.String(13), unique=True)
    stok = db.Column(db.Integer, default=0)

class Peminjaman(db.Model):
    __tablename__ = 'peminjaman'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    buku_id = db.Column(db.Integer, db.ForeignKey('buku.id'), nullable=False)
    tanggal_pinjam = db.Column(db.DateTime, default=datetime.utcnow)
    tanggal_kembali = db.Column(db.DateTime)
    status = db.Column(db.String(20), default='dipinjam')
    buku = db.relationship('Buku', backref='peminjaman')
```

## 6.3 RESTful API Design

### 6.3.1 Prinsip REST

| Prinsip | Deskripsi |
|---------|-----------|
| **Stateless** | Setiap request independen |
| **Resource-based** | URL = noun (`/api/buku`), bukan verb (`/api/getBuku`) |
| **HTTP Methods** | GET, POST, PUT, PATCH, DELETE |
| **JSON** | Format data standar |
| **Status Codes** | 200 OK, 201 Created, 400 Bad Request, 404 Not Found, 500 Server Error |

### 6.3.2 API Endpoint Design

| Method | Endpoint | Deskripsi | Response |
|--------|----------|-----------|----------|
| GET | `/api/buku` | Daftar semua buku | `[{buku}, ...]` |
| GET | `/api/buku/:id` | Detail satu buku | `{buku}` |
| POST | `/api/buku` | Tambah buku baru | `{buku}` + 201 |
| PUT | `/api/buku/:id` | Update data buku | `{buku}` |
| DELETE | `/api/buku/:id` | Hapus buku | 204 No Content |

### 6.3.3 Implementasi Flask API

```python
from flask import Flask, jsonify, request

@app.route('/api/buku', methods=['GET'])
def get_semua_buku():
    buku_list = Buku.query.all()
    return jsonify([{
        'id': b.id, 'judul': b.judul,
        'penulis': b.penulis, 'stok': b.stok
    } for b in buku_list])

@app.route('/api/buku/<int:id>', methods=['GET'])
def get_buku(id):
    buku = Buku.query.get_or_404(id)
    return jsonify({'id': buku.id, 'judul': buku.judul})

@app.route('/api/buku', methods=['POST'])
def tambah_buku():
    data = request.get_json()
    buku = Buku(judul=data['judul'], penulis=data['penulis'], stok=data['stok'])
    db.session.add(buku)
    db.session.commit()
    return jsonify({'id': buku.id, 'message': 'Buku berhasil ditambahkan'}), 201
```

---

## AI Corner: AI untuk UML dan Database Design (Level: Intermediate)

| Aktivitas | Prompt Contoh | Catatan |
|-----------|---------------|---------|
| Generate Class Diagram | "Buatkan Class Diagram dalam Mermaid untuk Sistem Perpustakaan dengan class User, Buku, Peminjaman" | Review relasi dan multiplicity |
| Design ERD | "Buatkan ERD untuk Sistem Antrian Puskesmas dengan 5 entitas" | Periksa normalisasi |
| API Design | "Desain REST API endpoints untuk CRUD Buku dan Peminjaman" | Pastikan konsisten dengan resource naming |

---

## Latihan Soal

### Level Dasar (C1-C2)
1. Sebutkan 3 jenis UML diagram structural dan 3 behavioral.
2. Jelaskan perbedaan aggregation dan composition.
3. Apa yang dimaksud dengan normalisasi 3NF?
4. Sebutkan 5 HTTP methods dan kegunaannya.

### Level Menengah (C3-C4)
5. Buatlah Class Diagram lengkap untuk Sistem E-Commerce UMKM (minimal 5 class dengan relasi).
6. Buatlah Sequence Diagram untuk proses checkout pesanan.
7. Desain ERD dan normalisasi hingga 3NF untuk Sistem Manajemen Kos-kosan.

### Level Mahir (C5-C6)
8. Rancang lengkap: Class Diagram + ERD + API Endpoints untuk Aplikasi Pengelolaan Zakat.
9. Evaluasi desain API berikut dan identifikasi pelanggaran prinsip REST.

---

## Rangkuman

1. **UML** adalah bahasa standar untuk memodelkan desain software — 14 diagram dalam 2 kategori.
2. **Class Diagram** menggambarkan struktur statis (class, atribut, method, relasi).
3. **Sequence Diagram** menggambarkan interaksi antar objek dalam urutan waktu.
4. **Activity Diagram** menggambarkan alur proses dengan decision points.
5. **ERD** dan **normalisasi** (1NF-3NF) menghasilkan desain database yang efisien dan konsisten.
6. **REST API** menggunakan HTTP methods pada resource URLs dengan JSON sebagai format data.

---

## Referensi

1. Fowler, M. (2003). *UML Distilled* (3rd ed.). Addison-Wesley.
2. Elmasri, R. & Navathe, S. (2016). *Fundamentals of Database Systems* (7th ed.). Pearson.
3. Fielding, R. T. (2000). *Architectural Styles and the Design of Network-based Software Architectures*.
4. OMG. (2017). *Unified Modeling Language Specification v2.5.1*.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
