# BAB 6: DESAIN PERANGKAT LUNAK DAN UML

**Oleh: Tri Aji Nugroho, S.T., M.T.**
**Mata Kuliah:** IF2205 Rekayasa Perangkat Lunak
**Program Studi Informatika — Universitas Al Azhar Indonesia**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi | Level Bloom | Estimasi Waktu |
|-----------|-----------|-------------|----------------|
| 3.3 | Membuat diagram UML (Class, Sequence, Activity, State, Use Case) menggunakan PlantUML/Mermaid | C3 (Menerapkan) | 75 menit |
| 3.4 | Merancang database (ERD, normalization 1NF-3NF) dan REST API design | C3 (Menerapkan) | 75 menit |

---

## Peta Konsep Bab

```
                     ┌─────────────────────────────┐
                     │  DESAIN PERANGKAT LUNAK      │
                     └──────────────┬──────────────┘
              ┌──────────────┬──────┴──────┬──────────────┐
              ▼              ▼             ▼              ▼
     ┌──────────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐
     │     UML      │ │ Database  │ │ REST API  │ │  OpenAPI  │
     │  Diagrams    │ │  Design   │ │  Design   │ │ / Swagger │
     └──────┬───────┘ └─────┬─────┘ └─────┬─────┘ └───────────┘
       ┌────┼────┐     ┌────┼────┐    ┌────┼────┐
       ▼    ▼    ▼     ▼    ▼    ▼    ▼    ▼    ▼
     Class Seq  Act  ERD  Norm  Denorm HTTP  Status
     Diag  Diag Diag      1-3NF       Methods Codes
       │    │
       ▼    ▼
     State  Use Case
     Diag   Diag
```

---

## 6.1 Unified Modeling Language (UML)

### 6.1.1 Apa Itu UML?

UML (Unified Modeling Language) adalah bahasa standar untuk **visualisasi, spesifikasi, konstruksi, dan dokumentasi** artefak sistem software. Dikembangkan oleh Grady Booch, James Rumbaugh, dan Ivar Jacobson, dan sekarang dikelola oleh OMG (Object Management Group).

UML v2.5 mendefinisikan **14 jenis diagram**, dikelompokkan menjadi 2 kategori besar:

```
┌───────────────────────────────────────────────────────────────┐
│                    14 UML DIAGRAM TYPES                       │
│                                                               │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │              STRUCTURAL DIAGRAMS (7)                    │  │
│  │                                                         │  │
│  │  1. Class Diagram ★       5. Object Diagram             │  │
│  │  2. Component Diagram     6. Package Diagram            │  │
│  │  3. Deployment Diagram    7. Composite Structure        │  │
│  │  4. Profile Diagram                                     │  │
│  └─────────────────────────────────────────────────────────┘  │
│                                                               │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │              BEHAVIORAL DIAGRAMS (7)                    │  │
│  │                                                         │  │
│  │  8. Use Case Diagram ★   12. Timing Diagram             │  │
│  │  9. Sequence Diagram ★   13. Communication Diagram      │  │
│  │ 10. Activity Diagram ★   14. Interaction Overview       │  │
│  │ 11. State Machine ★                                     │  │
│  └─────────────────────────────────────────────────────────┘  │
│                                                               │
│  ★ = 5 diagram yang kita pelajari secara mendalam            │
└───────────────────────────────────────────────────────────────┘
```

### 6.1.2 Kapan Menggunakan Diagram Apa?

| Diagram | Pertanyaan yang Dijawab | Kapan Digunakan | Fase SDLC |
|---------|------------------------|-----------------|-----------|
| **Use Case** | "Apa yang bisa dilakukan user?" | Requirement analysis | Requirements |
| **Class** | "Apa struktur data dan relasinya?" | Desain OOP | Design |
| **Sequence** | "Bagaimana objek berinteraksi?" | Desain alur proses | Design |
| **Activity** | "Bagaimana alur kerja prosesnya?" | Desain workflow | Req/Design |
| **State Machine** | "Bagaimana state objek berubah?" | Desain lifecycle objek | Design |

---

## 6.2 Use Case Diagram

Use Case Diagram menggambarkan **interaksi antara aktor (pengguna) dan sistem** — apa yang bisa dilakukan user terhadap sistem.

```
┌────────────────────────────────────────────────────────────────┐
│        USE CASE DIAGRAM: Sistem Perpustakaan Digital           │
│                                                                │
│  ┌────────┐                                    ┌────────────┐  │
│  │        │    ┌──────────────────────────┐     │            │  │
│  │Mahasiswa│───▶│ Cari Buku               │     │            │  │
│  │        │    └──────────────────────────┘     │            │  │
│  │  ◯     │    ┌──────────────────────────┐     │            │  │
│  │ /|\    │───▶│ Pinjam Buku              │     │   Petugas  │  │
│  │ / \    │    └──────────────────────────┘     │            │  │
│  │        │    ┌──────────────────────────┐     │     ◯      │  │
│  │        │───▶│ Kembalikan Buku          │     │    /|\     │  │
│  │        │    └──────────────────────────┘     │    / \     │  │
│  │        │    ┌──────────────────────────┐     │            │  │
│  │        │───▶│ Lihat Riwayat Peminjaman │     │            │  │
│  └────────┘    └──────────────────────────┘     │            │  │
│                ┌──────────────────────────┐     │            │  │
│                │ Kelola Data Buku         │◀────│            │  │
│                └──────────────────────────┘     │            │  │
│                ┌──────────────────────────┐     │            │  │
│                │ Verifikasi Peminjaman    │◀────│            │  │
│                └──────────────────────────┘     │            │  │
│                ┌──────────────────────────┐     │            │  │
│                │ Generate Laporan         │◀────│            │  │
│                └──────────────────────────┘     └────────────┘  │
│                                                                │
│  Relasi: ───▶ = Association (aktor menggunakan use case)      │
└────────────────────────────────────────────────────────────────┘
```

**Relasi dalam Use Case Diagram:**

| Relasi | Simbol | Deskripsi | Contoh |
|--------|--------|-----------|--------|
| **Association** | ─── | Aktor menggunakan use case | Mahasiswa → Cari Buku |
| **Include** | - - -▶ <<include>> | Use case SELALU memanggil use case lain | Pinjam Buku --include--> Cek Ketersediaan |
| **Extend** | - - -▶ <<extend>> | Use case KADANG memperluas use case lain | Cari Buku --extend--> Filter by Kategori |
| **Generalization** | △─── | Aktor mewarisi use case aktor lain | Admin generalizes Petugas |

**PlantUML Syntax:**

```
@startuml
left to right direction

actor Mahasiswa as M
actor Petugas as P

rectangle "Sistem Perpustakaan" {
    usecase "Cari Buku" as UC1
    usecase "Pinjam Buku" as UC2
    usecase "Kembalikan Buku" as UC3
    usecase "Cek Ketersediaan" as UC4
    usecase "Kelola Data Buku" as UC5
    usecase "Generate Laporan" as UC6
}

M --> UC1
M --> UC2
M --> UC3
UC2 ..> UC4 : <<include>>
P --> UC5
P --> UC6
@enduml
```

---

## 6.3 Class Diagram

Class Diagram menggambarkan **struktur statis** sistem — class, atribut, method, dan relasi antar class.

### 6.3.1 Anatomi Class Diagram

```
┌─────────────────────────────────────────┐
│  NOTASI CLASS DIAGRAM                   │
│                                         │
│  ┌──────────────────┐                   │
│  │    ClassName      │  ← Nama class    │
│  ├──────────────────┤                   │
│  │ - id: int        │  ← Atribut       │
│  │ - nama: str      │    (- private)    │
│  │ # email: str     │    (# protected)  │
│  │ + status: str    │    (+ public)     │
│  ├──────────────────┤                   │
│  │ + register()     │  ← Method        │
│  │ + login(): bool  │    return type    │
│  │ - hash_pwd(): str│                   │
│  └──────────────────┘                   │
└─────────────────────────────────────────┘
```

**Visibility Modifiers:**
- `+` **public** — bisa diakses dari mana saja
- `-` **private** — hanya bisa diakses dari class itu sendiri
- `#` **protected** — bisa diakses dari class dan subclass
- `~` **package** — bisa diakses dari package yang sama

### 6.3.2 Relasi dalam Class Diagram

```
┌──────────────────────────────────────────────────────────────┐
│           RELASI DALAM CLASS DIAGRAM                         │
│                                                              │
│  Association    ────────────    "Menggunakan"                │
│  (User meminjam Buku)                                        │
│                                                              │
│  Aggregation    ◇────────────  "Memiliki" (bisa hidup       │
│  (Perpustakaan has Buku)        terpisah)                    │
│                                                              │
│  Composition    ◆────────────  "Terdiri dari" (tidak bisa    │
│  (Order has OrderItem)          hidup terpisah)              │
│                                                              │
│  Inheritance    △────────────  "Adalah jenis dari"           │
│  (Admin extends User)           (is-a relationship)          │
│                                                              │
│  Dependency     - - - - -▶     "Menggunakan sementara"      │
│  (Controller uses Service)                                   │
│                                                              │
│  Realization    - - - △ - -    "Mengimplementasikan"         │
│  (EmailNotif implements INotif)                              │
└──────────────────────────────────────────────────────────────┘
```

**Multiplicity (Kardinalitas):**

| Notasi | Arti | Contoh |
|--------|------|--------|
| `1` | Tepat satu | User memiliki 1 profil |
| `0..1` | Nol atau satu | User bisa punya 0 atau 1 foto |
| `*` atau `0..*` | Nol atau banyak | User punya 0 atau banyak peminjaman |
| `1..*` | Satu atau banyak | Order punya 1 atau banyak item |
| `2..5` | Rentang tertentu | Tim punya 2-5 anggota |

### 6.3.3 Class Diagram Lengkap: Sistem Perpustakaan

```
┌──────────────────┐       1     *  ┌──────────────────┐
│      User        │──────────────▶│    Peminjaman     │
├──────────────────┤               ├──────────────────┤
│ - id: int        │               │ - id: int        │
│ - nama: str      │               │ - tanggal_pinjam │
│ - email: str     │               │ - tanggal_kembali│
│ - password: str  │               │ - status: str    │
│ - role: str      │               │ - denda: float   │
├──────────────────┤               ├──────────────────┤
│ + register()     │               │ + create()       │
│ + login(): bool  │               │ + return_book()  │
│ + get_history()  │               │ + hitung_denda() │
└────────┬─────────┘               └───────┬──────────┘
         △                                 │
    ┌────┴────┐                    *       │       1
    │         │               ┌────────────┘
┌───┴────┐ ┌──┴──────┐       │
│Mahasiswa│ │ Petugas │       │
├────────┤ ├─────────┤  ┌────┴─────────────┐
│ - nim  │ │ - nip   │  │      Buku        │
├────────┤ ├─────────┤  ├──────────────────┤
│+pinjam()││+verif() │  │ - id: int        │
│+kembali│ │+kelola()│  │ - judul: str     │
└────────┘ └─────────┘  │ - penulis: str   │
                        │ - isbn: str      │
                        │ - stok: int      │
                        │ - kategori: str  │
                        ├──────────────────┤
                        │ + search()       │
                        │ + kurangi_stok() │
                        │ + tambah_stok()  │
                        └──────┬───────────┘
                               │ *
                               │
                          ┌────┴───────────┐
                          │   Kategori     │
                          ├────────────────┤
                          │ - id: int      │
                          │ - nama: str    │
                          ├────────────────┤
                          │ + get_buku()   │
                          └────────────────┘
```

**Mermaid Syntax untuk Class Diagram:**

```
classDiagram
    class User {
        -int id
        -String nama
        -String email
        -String password
        -String role
        +register()
        +login() bool
        +get_history() List
    }

    class Mahasiswa {
        -String nim
        +pinjam(buku_id)
        +kembalikan(peminjaman_id)
    }

    class Petugas {
        -String nip
        +verifikasi(peminjaman_id)
        +kelola_buku()
    }

    class Buku {
        -int id
        -String judul
        -String penulis
        -String isbn
        -int stok
        +search(keyword) List
        +kurangi_stok()
        +tambah_stok()
    }

    class Peminjaman {
        -int id
        -Date tanggal_pinjam
        -Date tanggal_kembali
        -String status
        -float denda
        +create()
        +return_book()
        +hitung_denda() float
    }

    User <|-- Mahasiswa
    User <|-- Petugas
    User "1" --> "*" Peminjaman
    Buku "1" --> "*" Peminjaman
```

### 6.3.4 Implementasi Python dari Class Diagram

```python
from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """Base class untuk semua user."""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='mahasiswa')
    peminjaman = db.relationship('Peminjaman', backref='user', lazy=True)

    def login(self, password):
        """Verifikasi password user."""
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password_hash, password)

    def get_history(self):
        """Ambil riwayat peminjaman user."""
        return Peminjaman.query.filter_by(user_id=self.id).all()


class Buku(db.Model):
    """Model untuk data buku perpustakaan."""
    __tablename__ = 'buku'
    id = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String(200), nullable=False)
    penulis = db.Column(db.String(100))
    isbn = db.Column(db.String(13), unique=True)
    stok = db.Column(db.Integer, default=0)
    kategori_id = db.Column(db.Integer, db.ForeignKey('kategori.id'))

    @staticmethod
    def search(keyword):
        """Cari buku berdasarkan judul atau penulis."""
        return Buku.query.filter(
            db.or_(
                Buku.judul.ilike(f'%{keyword}%'),
                Buku.penulis.ilike(f'%{keyword}%')
            )
        ).all()

    def kurangi_stok(self):
        if self.stok <= 0:
            raise ValueError("Stok buku habis")
        self.stok -= 1

    def tambah_stok(self):
        self.stok += 1


class Peminjaman(db.Model):
    """Model untuk transaksi peminjaman."""
    __tablename__ = 'peminjaman'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    buku_id = db.Column(db.Integer, db.ForeignKey('buku.id'), nullable=False)
    tanggal_pinjam = db.Column(db.DateTime, default=datetime.utcnow)
    tanggal_kembali = db.Column(db.DateTime)
    status = db.Column(db.String(20), default='dipinjam')
    denda = db.Column(db.Float, default=0.0)
    buku = db.relationship('Buku', backref='peminjaman')

    DENDA_PER_HARI = 1000  # Rp 1.000 per hari keterlambatan

    def return_book(self):
        """Proses pengembalian buku."""
        self.tanggal_kembali = datetime.utcnow()
        self.status = 'dikembalikan'
        self.denda = self.hitung_denda()
        self.buku_rel = Buku.query.get(self.buku_id)
        if self.buku_rel:
            self.buku_rel.tambah_stok()

    def hitung_denda(self):
        """Hitung denda keterlambatan (maks 7 hari pinjam)."""
        if self.tanggal_kembali is None:
            return 0.0
        batas = self.tanggal_pinjam + timedelta(days=7)
        if self.tanggal_kembali > batas:
            hari_telat = (self.tanggal_kembali - batas).days
            return hari_telat * self.DENDA_PER_HARI
        return 0.0
```

---

## 6.4 Sequence Diagram

Sequence Diagram menggambarkan **interaksi antar objek dalam urutan waktu** — siapa memanggil siapa, dalam urutan apa.

### 6.4.1 Elemen Sequence Diagram

```
┌────────────────────────────────────────────────────────────────┐
│         ELEMEN SEQUENCE DIAGRAM                                │
│                                                                │
│  ┌──────┐   ┌──────┐          Lifeline: garis vertikal       │
│  │Object│   │Object│          putus-putus di bawah objek      │
│  │  A   │   │  B   │                                          │
│  └──┬───┘   └──┬───┘          Activation bar: kotak di       │
│     │          │              lifeline = objek aktif           │
│     │──msg()──▶│                                              │
│     │          │ ▒▒▒          Synchronous message: ──▶        │
│     │          │ ▒▒▒          Asynchronous message: - -▶      │
│     │◀─return──│ ▒▒▒          Return: ◀── ── ──               │
│     │          │                                              │
│     │  ┌─alt─────────┐        Fragment: alt (if/else),       │
│     │  │ [condition]  │        opt (optional), loop           │
│     │  │  ──msg()──▶  │                                      │
│     │  └──────────────┘                                      │
└────────────────────────────────────────────────────────────────┘
```

### 6.4.2 Sequence Diagram: Proses Peminjaman Buku

```
  Mahasiswa     BukuController   BukuService    BukuRepo      Database
     │               │               │             │              │
     │── POST        │               │             │              │
     │  /pinjam ────▶│               │             │              │
     │               │── pinjam()───▶│             │              │
     │               │               │── cek_stok()│              │
     │               │               │────────────▶│              │
     │               │               │             │── SELECT ───▶│
     │               │               │             │◀── row ──────│
     │               │               │◀── stok=3 ──│              │
     │               │               │             │              │
     │               │     ┌─alt─────┤             │              │
     │               │     │[stok>0] │             │              │
     │               │     │         │── save()───▶│              │
     │               │     │         │             │── INSERT ───▶│
     │               │     │         │             │◀── OK ───────│
     │               │     │         │◀── OK ──────│              │
     │               │◀── 201 ──────│             │              │
     │◀── JSON ──────│     │         │             │              │
     │  "Berhasil"   │     ├─────────┤             │              │
     │               │     │[stok=0] │             │              │
     │               │◀── 400 ──────│             │              │
     │◀── JSON ──────│     │"Habis"  │             │              │
     │  "Stok habis" │     └─────────┘             │              │
     │               │               │             │              │
```

**PlantUML Syntax:**

```
@startuml
actor Mahasiswa
participant BukuController
participant BukuService
participant BukuRepo
database Database

Mahasiswa -> BukuController : POST /pinjam
BukuController -> BukuService : pinjam(user_id, buku_id)
BukuService -> BukuRepo : cek_stok(buku_id)
BukuRepo -> Database : SELECT stok FROM buku
Database --> BukuRepo : row
BukuRepo --> BukuService : stok=3

alt stok > 0
    BukuService -> BukuRepo : save(peminjaman)
    BukuRepo -> Database : INSERT INTO peminjaman
    Database --> BukuRepo : OK
    BukuRepo --> BukuService : OK
    BukuService --> BukuController : 201 Created
    BukuController --> Mahasiswa : {"message": "Berhasil"}
else stok = 0
    BukuService --> BukuController : 400 Bad Request
    BukuController --> Mahasiswa : {"error": "Stok habis"}
end
@enduml
```

### 6.4.3 Sequence Diagram: Proses Login

```
  User          LoginController    AuthService     UserRepo     Database
   │                │                  │              │             │
   │── POST         │                  │              │             │
   │  /login ──────▶│                  │              │             │
   │ {email,pwd}    │── authenticate()─▶│              │             │
   │                │                  │── find_by()──▶│             │
   │                │                  │              │── SELECT ──▶│
   │                │                  │              │◀── user ────│
   │                │                  │◀── user ─────│             │
   │                │                  │              │             │
   │                │     ┌─alt────────┤              │             │
   │                │     │[user &&    │              │             │
   │                │     │ pwd valid] │              │             │
   │                │     │            │── gen_token()│             │
   │                │     │            │──────────┐   │             │
   │                │     │            │◀─ JWT ───┘   │             │
   │                │◀──── 200 + JWT ──│              │             │
   │◀── Set-Cookie ─│     │            │              │             │
   │   + redirect   │     ├────────────┤              │             │
   │                │     │[invalid]   │              │             │
   │                │◀──── 401 ────────│              │             │
   │◀── Error msg ──│     └────────────┘              │             │
   │                │                  │              │             │
```

---

## 6.5 Activity Diagram

Activity Diagram menggambarkan **alur proses** (workflow) dengan decision points, parallel activities, dan branching — mirip flowchart tapi lebih terstruktur.

### 6.5.1 Notasi Activity Diagram

```
┌────────────────────────────────────────────────────────┐
│          NOTASI ACTIVITY DIAGRAM                       │
│                                                        │
│  (●)  = Initial node (start)                          │
│                                                        │
│  (◉)  = Final node (end)                              │
│                                                        │
│  [Action] = Activity (aksi yang dilakukan)             │
│                                                        │
│  ◇   = Decision node (percabangan)                    │
│                                                        │
│  ═══ = Fork/Join (parallel activities)                 │
│                                                        │
│  ─── = Transition (aliran kontrol)                     │
│                                                        │
│  |swimlane| = Partisi tanggung jawab per aktor         │
└────────────────────────────────────────────────────────┘
```

### 6.5.2 Activity Diagram: Proses Peminjaman Buku

```
┌─────────────────────────────────────────────────────────────┐
│         ACTIVITY DIAGRAM: Peminjaman Buku                   │
│                                                             │
│  │    Mahasiswa    │     Sistem     │     Petugas    │      │
│  │                 │                │                │      │
│  │     (●)         │                │                │      │
│  │      │          │                │                │      │
│  │      ▼          │                │                │      │
│  │ [Cari buku di   │                │                │      │
│  │  katalog]       │                │                │      │
│  │      │          │                │                │      │
│  │      ├─────────▶│                │                │      │
│  │      │          ▼                │                │      │
│  │      │   [Tampilkan hasil       │                │      │
│  │      │    pencarian]            │                │      │
│  │      │          │                │                │      │
│  │      │◀─────────┤                │                │      │
│  │      ▼          │                │                │      │
│  │ [Pilih buku &   │                │                │      │
│  │  klik "Pinjam"] │                │                │      │
│  │      │          │                │                │      │
│  │      ├─────────▶│                │                │      │
│  │      │          ▼                │                │      │
│  │      │     ◇── Stok > 0?        │                │      │
│  │      │    / \                    │                │      │
│  │      │  Ya   Tidak              │                │      │
│  │      │  │      │                │                │      │
│  │      │  ▼      ▼                │                │      │
│  │      │ [Buat    [Tampilkan       │                │      │
│  │      │ record   "Stok habis"]   │                │      │
│  │      │ pinjam]       │          │                │      │
│  │      │  │            ▼          │                │      │
│  │      │  │           (◉)         │                │      │
│  │      │  │                       │                │      │
│  │      │  ├──════════════════════▶│                │      │
│  │      │  │      Fork             │                │      │
│  │      │  │                       ▼                │      │
│  │      │  │                [Verifikasi             │      │
│  │      │  │                 peminjaman]            │      │
│  │      │  ▼                       │                │      │
│  │      │ [Kurangi stok]           │                │      │
│  │      │  │                       │                │      │
│  │      │  ├──════════════════════◀┤                │      │
│  │      │  │      Join             │                │      │
│  │      │  ▼                       │                │      │
│  │      │ [Kirim notifikasi        │                │      │
│  │      │  ke mahasiswa]           │                │      │
│  │      │  │                       │                │      │
│  │      │  ▼                       │                │      │
│  │      │ (◉)                      │                │      │
└─────────────────────────────────────────────────────────────┘
```

**Mermaid Syntax:**

```
flowchart TD
    A((Start)) --> B[Cari buku di katalog]
    B --> C[Tampilkan hasil pencarian]
    C --> D[Pilih buku & klik Pinjam]
    D --> E{Stok > 0?}
    E -- Ya --> F[Buat record peminjaman]
    E -- Tidak --> G[Tampilkan 'Stok habis']
    G --> H((End))
    F --> I[Kurangi stok buku]
    F --> J[Verifikasi oleh petugas]
    I --> K[Kirim notifikasi]
    J --> K
    K --> H
```

---

## 6.6 State Machine Diagram

State Machine Diagram menggambarkan **lifecycle (siklus hidup)** sebuah objek — bagaimana state-nya berubah sebagai respons terhadap events.

### 6.6.1 State Machine: Status Peminjaman

```
┌────────────────────────────────────────────────────────────────┐
│       STATE MACHINE: Lifecycle Peminjaman Buku                 │
│                                                                │
│                          pinjam()                              │
│  (●) ─────────────▶ ┌──────────────┐                          │
│                      │              │                          │
│                      │  DIPINJAM    │                          │
│                      │              │                          │
│                      └──────┬───────┘                          │
│                         │         │                            │
│              kembali()  │         │  lewat_deadline()          │
│                         │         │                            │
│                    ┌────▼──┐  ┌───▼──────────┐                 │
│                    │       │  │              │                 │
│                    │DIKEMBA│  │  TERLAMBAT   │                 │
│                    │LIKAN  │  │              │                 │
│                    │       │  └──────┬───────┘                 │
│                    └───┬───┘        │                          │
│                        │     kembali() + bayar_denda()         │
│                        │            │                          │
│                        │     ┌──────▼───────┐                  │
│                        │     │   DIKEMBA-   │                  │
│                        │     │   LIKAN +    │                  │
│                        │     │   DENDA      │                  │
│                        │     └──────┬───────┘                  │
│                        │            │                          │
│                        ▼            ▼                          │
│                    ┌────────────────────┐                      │
│                    │     SELESAI        │                      │
│                    └─────────┬──────────┘                      │
│                              │                                 │
│                              ▼                                 │
│                             (◉)                                │
└────────────────────────────────────────────────────────────────┘
```

### 6.6.2 State Machine: Status Buku

```
┌────────────────────────────────────────────────────────────┐
│       STATE MACHINE: Lifecycle Buku                        │
│                                                            │
│  (●) ──create()──▶ ┌───────────┐                          │
│                     │ TERSEDIA  │◀──── kembali()           │
│                     └─────┬─────┘          │               │
│                           │                │               │
│                    pinjam()│         ┌──────┴─────┐        │
│                           │         │ DIPINJAM   │        │
│                           └────────▶│            │        │
│                                     └──────┬─────┘        │
│                                            │               │
│                                  rusak()   │               │
│                                            ▼               │
│                              ┌──────────────────┐          │
│            hapus()           │  RUSAK/HILANG    │          │
│   ┌────────────────┐        └────────┬─────────┘          │
│   │   DIHAPUS      │◀── hapus() ─────┘                    │
│   └────────┬───────┘                                      │
│            ▼                                               │
│           (◉)                                              │
└────────────────────────────────────────────────────────────┘
```

**PlantUML Syntax:**

```
@startuml
[*] --> Tersedia : create()

Tersedia --> Dipinjam : pinjam()
Dipinjam --> Tersedia : kembali()
Dipinjam --> RusakHilang : rusak() / hilang()
Tersedia --> Dihapus : hapus()
RusakHilang --> Dihapus : hapus()
Dihapus --> [*]

Tersedia : stok > 0
Dipinjam : stok berkurang
RusakHilang : perlu penggantian
@enduml
```

### 6.6.3 Implementasi State Machine di Python

```python
class PeminjamanStatus:
    """Enum untuk status peminjaman."""
    DIPINJAM = 'dipinjam'
    TERLAMBAT = 'terlambat'
    DIKEMBALIKAN = 'dikembalikan'
    DENDA = 'dikembalikan_denda'
    SELESAI = 'selesai'

    # Transisi yang valid: {current_state: [allowed_next_states]}
    TRANSITIONS = {
        DIPINJAM: [DIKEMBALIKAN, TERLAMBAT],
        TERLAMBAT: [DENDA],
        DIKEMBALIKAN: [SELESAI],
        DENDA: [SELESAI],
    }

    @classmethod
    def can_transition(cls, current, target):
        """Cek apakah transisi state valid."""
        allowed = cls.TRANSITIONS.get(current, [])
        return target in allowed


class Peminjaman:
    def __init__(self, user_id, buku_id):
        self.user_id = user_id
        self.buku_id = buku_id
        self.status = PeminjamanStatus.DIPINJAM
        print(f"[STATE] Peminjaman dibuat: {self.status}")

    def transition_to(self, new_status):
        """Transisi state dengan validasi."""
        if PeminjamanStatus.can_transition(self.status, new_status):
            old = self.status
            self.status = new_status
            print(f"[STATE] {old} → {new_status}")
        else:
            raise ValueError(
                f"Transisi tidak valid: {self.status} → {new_status}"
            )


# Penggunaan
p = Peminjaman(user_id=1, buku_id=42)
# [STATE] Peminjaman dibuat: dipinjam

p.transition_to(PeminjamanStatus.DIKEMBALIKAN)
# [STATE] dipinjam → dikembalikan

p.transition_to(PeminjamanStatus.SELESAI)
# [STATE] dikembalikan → selesai

# Coba transisi invalid
try:
    p2 = Peminjaman(user_id=2, buku_id=10)
    p2.transition_to(PeminjamanStatus.SELESAI)  # Langsung selesai?
except ValueError as e:
    print(f"[ERROR] {e}")
    # [ERROR] Transisi tidak valid: dipinjam → selesai
```

---

## 6.7 Database Design

### 6.7.1 Entity-Relationship Diagram (ERD)

ERD menggambarkan **entitas, atribut, dan relasi** dalam database.

```
┌────────────────────────────────────────────────────────────────┐
│              ERD: Sistem Perpustakaan Digital                   │
│                                                                │
│ ┌──────────┐     1:N      ┌──────────────┐     N:1  ┌───────┐ │
│ │   User   │─────────────▶│  Peminjaman   │◀────────│ Buku  │ │
│ │          │              │              │          │       │ │
│ │ PK: id   │              │ PK: id       │          │ PK: id│ │
│ │ nama     │              │ FK: user_id  │          │ judul │ │
│ │ email    │              │ FK: buku_id  │          │penulis│ │
│ │ password │              │ tgl_pinjam   │          │ isbn  │ │
│ │ role     │              │ tgl_kembali  │          │ stok  │ │
│ └──────────┘              │ status       │          │FK:kat │ │
│                           │ denda        │          └───┬───┘ │
│                           └──────────────┘              │     │
│                                                    N:1  │     │
│                                               ┌─────────┴──┐  │
│ ┌──────────┐     1:N      ┌──────────────┐    │  Kategori  │  │
│ │   Buku   │─────────────▶│    Review     │    │            │  │
│ │          │              │              │    │ PK: id     │  │
│ └──────────┘              │ PK: id       │    │ nama       │  │
│                           │ FK: buku_id  │    └────────────┘  │
│ ┌──────────┐              │ FK: user_id  │                    │
│ │   User   │─────────────▶│ rating       │                    │
│ │          │     1:N      │ komentar     │                    │
│ └──────────┘              └──────────────┘                    │
└────────────────────────────────────────────────────────────────┘
```

### 6.7.2 Normalisasi Database (1NF - 3NF)

Normalisasi adalah proses **menghilangkan redundansi data** dan **mencegah anomali** (insert, update, delete anomaly).

**Contoh Kasus: Data Mahasiswa dan Mata Kuliah**

**Tabel awal (belum normal):**

```
┌────────────────────────────────────────────────────────────────┐
│  mahasiswa_matakuliah (UNNORMALIZED)                           │
├──────┬──────────┬──────────────────┬───────────────────────────┤
│ NIM  │ Nama     │ Mata_Kuliah      │ Dosen                     │
├──────┼──────────┼──────────────────┼───────────────────────────┤
│ 001  │ Ahmad    │ RPL, Algoritma   │ Tri Aji, Budi S.          │
│ 002  │ Fatimah  │ RPL              │ Tri Aji                   │
│ 003  │ Budi     │ Algoritma, DB    │ Budi S., Andi W.          │
└──────┴──────────┴──────────────────┴───────────────────────────┘
  Masalah: Kolom Mata_Kuliah dan Dosen berisi multiple values!
```

**1NF — Setiap kolom bernilai atomik (satu nilai per sel):**

```
┌──────────────────────────────────────────────────────────────┐
│  mahasiswa_matakuliah (1NF)                                  │
├──────┬──────────┬──────────────────┬─────────────────────────┤
│ NIM  │ Nama     │ Mata_Kuliah      │ Dosen                   │
├──────┼──────────┼──────────────────┼─────────────────────────┤
│ 001  │ Ahmad    │ RPL              │ Tri Aji                 │
│ 001  │ Ahmad    │ Algoritma        │ Budi S.                 │
│ 002  │ Fatimah  │ RPL              │ Tri Aji                 │
│ 003  │ Budi     │ Algoritma        │ Budi S.                 │
│ 003  │ Budi     │ DB               │ Andi W.                 │
└──────┴──────────┴──────────────────┴─────────────────────────┘
  PK: (NIM, Mata_Kuliah) — composite key
  Masalah: Nama bergantung hanya pada NIM (partial dependency)
```

**2NF — Tidak ada partial dependency (semua non-key bergantung pada SELURUH PK):**

```
┌─────────────────────────┐    ┌──────────────────────────────┐
│  mahasiswa (2NF)        │    │  mahasiswa_mk (2NF)          │
├──────┬──────────────────┤    ├──────┬──────────┬────────────┤
│ NIM  │ Nama             │    │ NIM  │ Kode_MK  │ Dosen      │
├──────┼──────────────────┤    ├──────┼──────────┼────────────┤
│ 001  │ Ahmad            │    │ 001  │ IF2205   │ Tri Aji    │
│ 002  │ Fatimah          │    │ 001  │ INF101   │ Budi S.    │
│ 003  │ Budi             │    │ 002  │ IF2205   │ Tri Aji    │
└──────┴──────────────────┘    │ 003  │ INF101   │ Budi S.    │
  PK: NIM                      │ 003  │ IF3301   │ Andi W.    │
                                └──────┴──────────┴────────────┘
                                 PK: (NIM, Kode_MK)
  Masalah: Dosen bergantung pada Kode_MK, bukan pada (NIM, Kode_MK)
           → transitive dependency
```

**3NF — Tidak ada transitive dependency:**

```
┌──────────────────┐  ┌──────────────────────┐  ┌──────────────────────┐
│  mahasiswa       │  │  enrollment          │  │  mata_kuliah         │
├──────┬───────────┤  ├──────┬───────────────┤  ├────────┬─────────────┤
│ NIM  │ Nama      │  │ NIM  │ Kode_MK       │  │Kode_MK │ Nama_MK    │
├──────┼───────────┤  ├──────┼───────────────┤  ├────────┼─────────────┤
│ 001  │ Ahmad     │  │ 001  │ IF2205        │  │ IF2205 │ RPL        │
│ 002  │ Fatimah   │  │ 001  │ INF101        │  │ INF101 │ Algoritma  │
│ 003  │ Budi      │  │ 002  │ IF2205        │  │ IF3301 │ Database   │
└──────┴───────────┘  │ 003  │ INF101        │  └────────┼─────────────┤
                      │ 003  │ IF3301        │           │ Dosen       │
                      └──────┴───────────────┘           ├─────────────┤
                                                         │ Tri Aji     │
                                                         │ Budi S.     │
                                                         │ Andi W.     │
                                                         └─────────────┘
  Sekarang: Dosen bergantung langsung pada Kode_MK (bukan transitif)
```

### 6.7.3 Ringkasan Normalisasi

| Normal Form | Aturan | Cek |
|-------------|--------|-----|
| **1NF** | Setiap kolom bernilai atomik (satu nilai) | Ada kolom yang berisi list/array? |
| **2NF** | 1NF + non-key bergantung pada SELURUH PK | Ada atribut yang bergantung hanya pada sebagian composite key? |
| **3NF** | 2NF + tidak ada transitive dependency | Ada non-key yang bergantung pada non-key lain? |

### 6.7.4 Denormalisasi

Kadang kita sengaja **melanggar normalisasi** untuk meningkatkan performance (mengurangi JOIN).

```
┌────────────────────────────────────────────────────────────┐
│              NORMALISASI vs DENORMALISASI                   │
│                                                            │
│  Normalisasi (3NF)              Denormalisasi              │
│  ┌─────┐  ┌─────┐             ┌──────────────────┐        │
│  │Order│──│Item │             │ Order + Item      │        │
│  └─────┘  └─────┘             │ (digabung)       │        │
│                                └──────────────────┘        │
│  + Tidak ada redundansi       + Query lebih cepat          │
│  + Update konsisten           + Lebih sedikit JOIN         │
│  - Banyak JOIN saat query     - Redundansi data            │
│  - Bisa lebih lambat          - Update lebih kompleks      │
│                                                            │
│  Kapan denormalisasi?                                      │
│  - Read-heavy system (banyak baca, jarang tulis)          │
│  - Reporting/dashboard                                     │
│  - Caching layer                                          │
└────────────────────────────────────────────────────────────┘
```

**Contoh Indonesia — Sistem Akademik UAI:**
Tabel `enrollment` yang sudah 3NF perlu JOIN ke `mahasiswa`, `mata_kuliah`, dan `dosen` setiap kali menampilkan KRS. Untuk dashboard KRS, kita bisa membuat tabel denormalisasi `krs_view` yang sudah include nama mahasiswa, nama MK, dan nama dosen — mengurangi 3 JOIN menjadi 1 query.

### 6.7.5 Implementasi SQLAlchemy ORM Lengkap

```python
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """Tabel users — 3NF compliant."""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(20), default='mahasiswa')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relasi: User has many Peminjaman
    peminjaman = db.relationship('Peminjaman', backref='user', lazy=True)
    # Relasi: User has many Review
    reviews = db.relationship('Review', backref='user', lazy=True)

    def to_dict(self):
        return {
            'id': self.id, 'nama': self.nama,
            'email': self.email, 'role': self.role
        }


class Kategori(db.Model):
    """Tabel kategori buku."""
    __tablename__ = 'kategori'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(50), unique=True, nullable=False)
    buku_list = db.relationship('Buku', backref='kategori', lazy=True)


class Buku(db.Model):
    """Tabel buku — FK ke kategori."""
    __tablename__ = 'buku'
    id = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String(200), nullable=False)
    penulis = db.Column(db.String(100))
    isbn = db.Column(db.String(13), unique=True)
    stok = db.Column(db.Integer, default=0)
    kategori_id = db.Column(db.Integer, db.ForeignKey('kategori.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id, 'judul': self.judul,
            'penulis': self.penulis, 'isbn': self.isbn,
            'stok': self.stok,
            'kategori': self.kategori.nama if self.kategori else None
        }


class Peminjaman(db.Model):
    """Tabel peminjaman — FK ke users dan buku."""
    __tablename__ = 'peminjaman'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    buku_id = db.Column(db.Integer, db.ForeignKey('buku.id'), nullable=False)
    tanggal_pinjam = db.Column(db.DateTime, default=datetime.utcnow)
    tanggal_kembali = db.Column(db.DateTime)
    status = db.Column(db.String(20), default='dipinjam')
    denda = db.Column(db.Float, default=0.0)
    buku = db.relationship('Buku', backref='peminjaman_list')


class Review(db.Model):
    """Tabel review buku oleh user."""
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    buku_id = db.Column(db.Integer, db.ForeignKey('buku.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # 1-5
    komentar = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    buku = db.relationship('Buku', backref='reviews')
```

---

## 6.8 RESTful API Design

### 6.8.1 Prinsip REST

REST (Representational State Transfer) adalah gaya arsitektur untuk merancang API web. Prinsip-prinsipnya:

| Prinsip | Deskripsi | Contoh |
|---------|-----------|--------|
| **Stateless** | Setiap request independen, server tidak menyimpan state | Token JWT dikirim di setiap request |
| **Resource-based** | URL = noun (kata benda), bukan verb (kata kerja) | `/api/buku` (benar) vs `/api/getBuku` (salah) |
| **HTTP Methods** | Gunakan method HTTP untuk operasi CRUD | GET, POST, PUT, PATCH, DELETE |
| **Uniform Interface** | Konsisten dalam format response | Semua endpoint return JSON |
| **HATEOAS** | Response berisi link ke resource terkait | `"links": {"self": "/api/buku/1"}` |
| **Layered System** | Client tidak tahu apakah langsung ke server | Load balancer, API gateway transparan |

### 6.8.2 HTTP Methods & Status Codes

**HTTP Methods:**

| Method | Operasi | Idempotent | Safe | Contoh |
|--------|---------|------------|------|--------|
| **GET** | Read (baca data) | Ya | Ya | `GET /api/buku` |
| **POST** | Create (buat baru) | Tidak | Tidak | `POST /api/buku` |
| **PUT** | Update (ganti seluruh) | Ya | Tidak | `PUT /api/buku/1` |
| **PATCH** | Partial update | Ya | Tidak | `PATCH /api/buku/1` |
| **DELETE** | Delete (hapus) | Ya | Tidak | `DELETE /api/buku/1` |

**HTTP Status Codes yang Sering Dipakai:**

| Code | Nama | Kapan Digunakan |
|------|------|-----------------|
| **200** | OK | GET/PUT/PATCH berhasil |
| **201** | Created | POST berhasil membuat resource baru |
| **204** | No Content | DELETE berhasil, tidak ada body response |
| **400** | Bad Request | Input tidak valid (validasi gagal) |
| **401** | Unauthorized | Belum login (token tidak ada/expired) |
| **403** | Forbidden | Login tapi tidak punya akses |
| **404** | Not Found | Resource tidak ditemukan |
| **409** | Conflict | Duplikasi data (email sudah terdaftar) |
| **422** | Unprocessable Entity | Data valid secara format tapi invalid secara bisnis |
| **500** | Internal Server Error | Bug di server |

### 6.8.3 API Endpoint Design Best Practices

```
┌──────────────────────────────────────────────────────────────┐
│          REST API DESIGN BEST PRACTICES                      │
│                                                              │
│  ✓ BENAR                          ✗ SALAH                   │
│  ────────                         ────────                   │
│  GET  /api/buku                   GET  /api/getBuku          │
│  GET  /api/buku/1                 GET  /api/getBukuById/1    │
│  POST /api/buku                   POST /api/createBuku       │
│  PUT  /api/buku/1                 POST /api/updateBuku       │
│  DELETE /api/buku/1               POST /api/deleteBuku/1     │
│                                                              │
│  URL menggunakan noun (kata benda), bukan verb (kata kerja)  │
│  HTTP method yang menentukan operasi, bukan URL              │
│                                                              │
│  Plural naming:                                              │
│  /api/buku      ← daftar buku (collection)                  │
│  /api/buku/1    ← satu buku (resource)                      │
│                                                              │
│  Nested resources:                                           │
│  /api/buku/1/reviews     ← reviews untuk buku 1             │
│  /api/users/5/peminjaman ← peminjaman oleh user 5           │
│                                                              │
│  Query parameters untuk filter, sort, pagination:            │
│  /api/buku?kategori=fiksi&sort=judul&page=2&limit=10       │
└──────────────────────────────────────────────────────────────┘
```

### 6.8.4 API Versioning

API versioning penting saat API sudah digunakan client dan perlu diubah tanpa merusak client lama.

| Strategi | Contoh | Pro | Kontra |
|----------|--------|-----|--------|
| **URL Path** | `/api/v1/buku` | Paling jelas, mudah di-route | URL berubah |
| **Header** | `Accept: application/vnd.lib.v1+json` | URL tetap bersih | Lebih kompleks |
| **Query Param** | `/api/buku?version=1` | Mudah dipakai | Terlihat kotor |

**Rekomendasi:** Gunakan **URL Path versioning** (`/api/v1/`) — paling jelas dan mudah di-maintain.

**Contoh Indonesia — MyPertamina API Versioning:**
Aplikasi MyPertamina menggunakan API versioning karena versi mobile app yang beredar di Play Store sangat beragam (v1, v2, v3). API v1 tetap dipertahankan untuk app lama, sementara API v2 melayani fitur baru seperti loyalty points.

### 6.8.5 Implementasi Flask REST API Lengkap

```python
from flask import Flask, jsonify, request, abort
from functools import wraps

app = Flask(__name__)

# ============================================
# Middleware: Error handling global
# ============================================
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad Request', 'message': str(error)}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found', 'message': 'Resource tidak ditemukan'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500


# ============================================
# API v1: CRUD Buku
# ============================================
@app.route('/api/v1/buku', methods=['GET'])
def get_semua_buku():
    """GET /api/v1/buku — Daftar semua buku dengan pagination."""
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    kategori = request.args.get('kategori', None)
    search = request.args.get('q', None)

    query = Buku.query
    if kategori:
        query = query.filter_by(kategori_id=kategori)
    if search:
        query = query.filter(Buku.judul.ilike(f'%{search}%'))

    pagination = query.paginate(page=page, per_page=limit)

    return jsonify({
        'data': [b.to_dict() for b in pagination.items],
        'meta': {
            'page': page,
            'limit': limit,
            'total': pagination.total,
            'pages': pagination.pages
        }
    })


@app.route('/api/v1/buku/<int:id>', methods=['GET'])
def get_buku(id):
    """GET /api/v1/buku/:id — Detail satu buku."""
    buku = Buku.query.get_or_404(id)
    return jsonify({'data': buku.to_dict()})


@app.route('/api/v1/buku', methods=['POST'])
def tambah_buku():
    """POST /api/v1/buku — Tambah buku baru."""
    data = request.get_json()

    # Validasi input
    required = ['judul', 'isbn']
    for field in required:
        if field not in data:
            return jsonify({'error': f"Field '{field}' wajib diisi"}), 400

    # Cek duplikasi ISBN
    if Buku.query.filter_by(isbn=data['isbn']).first():
        return jsonify({'error': 'ISBN sudah terdaftar'}), 409

    buku = Buku(
        judul=data['judul'],
        penulis=data.get('penulis', 'Unknown'),
        isbn=data['isbn'],
        stok=data.get('stok', 0)
    )
    db.session.add(buku)
    db.session.commit()

    return jsonify({
        'data': buku.to_dict(),
        'message': 'Buku berhasil ditambahkan'
    }), 201


@app.route('/api/v1/buku/<int:id>', methods=['PUT'])
def update_buku(id):
    """PUT /api/v1/buku/:id — Update seluruh data buku."""
    buku = Buku.query.get_or_404(id)
    data = request.get_json()

    buku.judul = data.get('judul', buku.judul)
    buku.penulis = data.get('penulis', buku.penulis)
    buku.isbn = data.get('isbn', buku.isbn)
    buku.stok = data.get('stok', buku.stok)
    db.session.commit()

    return jsonify({
        'data': buku.to_dict(),
        'message': 'Buku berhasil diupdate'
    })


@app.route('/api/v1/buku/<int:id>', methods=['DELETE'])
def hapus_buku(id):
    """DELETE /api/v1/buku/:id — Hapus buku."""
    buku = Buku.query.get_or_404(id)
    db.session.delete(buku)
    db.session.commit()
    return '', 204


# ============================================
# Nested Resource: Reviews untuk Buku
# ============================================
@app.route('/api/v1/buku/<int:buku_id>/reviews', methods=['GET'])
def get_reviews(buku_id):
    """GET /api/v1/buku/:id/reviews — Reviews untuk buku tertentu."""
    buku = Buku.query.get_or_404(buku_id)
    reviews = Review.query.filter_by(buku_id=buku_id).all()
    return jsonify({
        'data': [{
            'id': r.id, 'rating': r.rating,
            'komentar': r.komentar, 'user': r.user.nama
        } for r in reviews]
    })


@app.route('/api/v1/buku/<int:buku_id>/reviews', methods=['POST'])
def tambah_review(buku_id):
    """POST /api/v1/buku/:id/reviews — Tambah review baru."""
    buku = Buku.query.get_or_404(buku_id)
    data = request.get_json()

    if not 1 <= data.get('rating', 0) <= 5:
        return jsonify({'error': 'Rating harus 1-5'}), 400

    review = Review(
        buku_id=buku_id,
        user_id=data['user_id'],
        rating=data['rating'],
        komentar=data.get('komentar', '')
    )
    db.session.add(review)
    db.session.commit()

    return jsonify({'message': 'Review berhasil ditambahkan'}), 201
```

### 6.8.6 OpenAPI/Swagger Documentation

OpenAPI (sebelumnya Swagger) adalah standar untuk mendokumentasikan REST API.

```yaml
# openapi.yaml — Contoh dokumentasi API Perpustakaan
openapi: 3.0.0
info:
  title: API Perpustakaan Digital UAI
  version: 1.0.0
  description: REST API untuk Sistem Perpustakaan Digital

paths:
  /api/v1/buku:
    get:
      summary: Daftar semua buku
      parameters:
        - name: page
          in: query
          schema:
            type: integer
            default: 1
        - name: limit
          in: query
          schema:
            type: integer
            default: 10
        - name: q
          in: query
          description: Kata kunci pencarian
          schema:
            type: string
      responses:
        '200':
          description: Daftar buku berhasil diambil
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/Buku'
                  meta:
                    type: object

    post:
      summary: Tambah buku baru
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/BukuInput'
      responses:
        '201':
          description: Buku berhasil ditambahkan
        '400':
          description: Input tidak valid
        '409':
          description: ISBN sudah terdaftar

components:
  schemas:
    Buku:
      type: object
      properties:
        id:
          type: integer
        judul:
          type: string
        penulis:
          type: string
        isbn:
          type: string
        stok:
          type: integer
    BukuInput:
      type: object
      required:
        - judul
        - isbn
      properties:
        judul:
          type: string
        penulis:
          type: string
        isbn:
          type: string
        stok:
          type: integer
```

> **Tips:** Gunakan library `flask-smorest` atau `flask-restx` untuk auto-generate Swagger UI dari kode Flask.

---

## 6.9 Studi Kasus: Desain Sistem Traveloka API

### Skenario

Traveloka adalah platform travel terbesar di Indonesia. Bayangkan Anda diminta mendesain modul **Pemesanan Hotel** sederhana.

### Class Diagram

```
┌──────────────┐   1    *   ┌──────────────┐   *    1   ┌──────────┐
│   Customer   │───────────▶│   Booking    │◀───────────│   Hotel   │
├──────────────┤            ├──────────────┤            ├──────────┤
│ - id         │            │ - id         │            │ - id     │
│ - nama       │            │ - check_in   │            │ - nama   │
│ - email      │            │ - check_out  │            │ - kota   │
│ - phone      │            │ - total      │            │ - rating │
├──────────────┤            │ - status     │            ├──────────┤
│ + search()   │            ├──────────────┤            │+get_rooms│
│ + book()     │            │ + create()   │            │+search() │
│ + cancel()   │            │ + cancel()   │            └────┬─────┘
└──────────────┘            │ + pay()      │                 │ 1
                            └──────────────┘            ┌────┴─────┐
                                    │ 1                 │   Room   │
                               ┌────┴─────┐   *        ├──────────┤
                               │ Payment  │◀────────────│ - type   │
                               ├──────────┤            │ - harga  │
                               │ - method │            │ - status │
                               │ - amount │            └──────────┘
                               │ - status │
                               └──────────┘
```

### API Endpoints

| Method | Endpoint | Deskripsi |
|--------|----------|-----------|
| GET | `/api/v1/hotels?kota=bali&check_in=2026-05-01` | Cari hotel |
| GET | `/api/v1/hotels/:id/rooms` | Lihat kamar tersedia |
| POST | `/api/v1/bookings` | Buat booking |
| GET | `/api/v1/bookings/:id` | Detail booking |
| DELETE | `/api/v1/bookings/:id` | Cancel booking |
| POST | `/api/v1/bookings/:id/payments` | Bayar booking |

### Sequence Diagram: Proses Booking

```
Customer     HotelAPI      BookingService    PaymentService    Database
   │            │               │                │               │
   │── POST     │               │                │               │
   │ /bookings─▶│               │                │               │
   │            │── create() ──▶│                │               │
   │            │               │── check_room()─────────────────▶│
   │            │               │◀── available ──────────────────│
   │            │               │── save() ──────────────────────▶│
   │            │               │◀── booking_id ─────────────────│
   │            │◀── 201 ──────│                │               │
   │◀── booking │               │                │               │
   │  details   │               │                │               │
   │            │               │                │               │
   │── POST     │               │                │               │
   │ /payments─▶│               │                │               │
   │            │────────────────────── pay() ──▶│               │
   │            │               │                │── charge() ──▶│
   │            │               │                │◀── OK ────────│
   │            │◀──────────────────── 200 ─────│               │
   │◀── payment │               │                │               │
   │  confirmed │               │                │               │
```

---

## AI Corner: AI untuk UML dan Database Design (Level: Intermediate)

### 6.AI.1 Generate Class Diagram dengan AI

**Prompt:**
```
Buatkan Class Diagram dalam Mermaid syntax untuk Sistem
Perpustakaan Digital dengan class: User, Mahasiswa (extends
User), Petugas (extends User), Buku, Kategori, Peminjaman,
Review. Sertakan atribut, method, relasi, dan multiplicity.
```

**Evaluasi output AI:**
- Cek apakah relasi (association, aggregation, composition, inheritance) tepat
- Cek apakah multiplicity logis (1, *, 0..1, 1..*)
- Cek apakah visibility modifiers benar (+, -, #)

### 6.AI.2 Generate ERD dari Requirements

**Prompt:**
```
Berdasarkan requirements berikut, buatkan ERD dan tabel SQL:
1. Mahasiswa bisa meminjam banyak buku
2. Setiap buku punya satu kategori
3. Mahasiswa bisa memberi review (rating 1-5) pada buku
4. Ada riwayat peminjaman dengan status dan denda
Normalisasi hingga 3NF.
```

### 6.AI.3 Design REST API dengan AI

**Prompt:**
```
Desain REST API endpoints untuk Sistem Antrian Puskesmas.
Fitur: registrasi pasien, ambil nomor antrian, panggil antrian,
lihat status antrian, riwayat kunjungan.
Gunakan JSON format, sertakan contoh request/response.
```

**Evaluasi:** Pastikan AI menggunakan noun-based URLs, HTTP methods yang tepat, dan status codes yang benar.

### 6.AI.4 Generate Sequence Diagram

**Prompt:**
```
Buatkan Sequence Diagram dalam PlantUML syntax untuk proses
checkout e-commerce: user klik checkout → validasi stok →
hitung total → pilih pembayaran → proses payment → kirim
konfirmasi email. Sertakan alt fragment untuk stok habis.
```

### 6.AI.5 Normalisasi Database dengan AI

**Prompt:**
```
Tabel berikut belum normal. Normalisasi hingga 3NF:

| OrderID | CustomerName | CustomerPhone | Products | Prices |
|---------|-------------|---------------|----------|--------|
| 1 | Ahmad | 0812xxx | Buku A, Buku B | 50000, 75000 |
| 2 | Budi | 0813xxx | Buku A | 50000 |

Tunjukkan proses step-by-step: UNF → 1NF → 2NF → 3NF.
```

### 6.AI.6 Ethical Considerations

- **Review semua diagram** yang dihasilkan AI — AI sering salah dalam multiplicity dan relasi
- **Jangan langsung copy** SQL schema dari AI — cek normalisasi dan constraint
- **Validasi** API design terhadap prinsip REST — AI kadang mencampur verb dan noun di URL
- **Dokumentasikan** penggunaan AI dalam AI Usage Log

---

## Latihan Soal

### Level Dasar (C1-C2) — 6 Soal

1. **Sebutkan** 14 jenis UML diagram dan kelompokkan menjadi structural dan behavioral.

2. **Jelaskan** perbedaan antara aggregation dan composition dalam Class Diagram. Berikan masing-masing satu contoh.

3. **Apa** yang dimaksud dengan normalisasi database? Jelaskan aturan 1NF, 2NF, dan 3NF masing-masing dalam satu kalimat.

4. **Sebutkan** 5 HTTP methods beserta operasi CRUD yang sesuai.

5. **Jelaskan** 5 HTTP status codes yang paling sering digunakan dalam REST API.

6. **Apa** perbedaan antara PUT dan PATCH dalam REST API? Kapan masing-masing digunakan?

### Level Menengah (C3-C4) — 7 Soal

7. **Buatlah** Class Diagram lengkap untuk Sistem E-Commerce UMKM dengan minimal 6 class: Customer, Product, Category, Order, OrderItem, Payment. Sertakan atribut, method, relasi, dan multiplicity.

8. **Buatlah** Sequence Diagram untuk proses checkout pesanan di e-commerce: user → Cart → OrderService → PaymentGateway → NotificationService.

9. **Desain** ERD dan normalisasi hingga 3NF untuk Sistem Manajemen Kos-kosan dengan entitas: Pemilik, Kos, Kamar, Penyewa, Pembayaran.

10. **Buatlah** Activity Diagram untuk proses registrasi mahasiswa baru di UAI: isi formulir → upload dokumen → verifikasi → bayar → terima NPM.

11. **Desain** REST API endpoints lengkap (URL, method, request body, response) untuk CRUD Buku dan Peminjaman di Sistem Perpustakaan.

12. **Buatlah** State Machine Diagram untuk lifecycle sebuah Pesanan di e-commerce: Draft → Pending Payment → Paid → Processing → Shipped → Delivered → Completed (dengan kondisi cancel dan return).

13. **Normalisasi** tabel berikut dari UNF hingga 3NF:
    ```
    | InvoiceID | Customer | Phone | Items | Prices | Qty |
    | 1 | Toko Makmur | 021-xxx | Beras,Gula | 15000,12000 | 10,5 |
    ```

### Level Mahir (C5-C6) — 6 Soal

14. **Rancang lengkap**: Class Diagram + ERD + API Endpoints + Sequence Diagram untuk Aplikasi Pengelolaan Zakat. Fitur: registrasi muzakki, hitung zakat, pembayaran, distribusi ke mustahik, laporan.

15. **Evaluasi** desain API berikut dan identifikasi pelanggaran prinsip REST:
    ```
    POST /api/getAllBooks
    POST /api/createBook
    GET /api/deleteBook?id=1
    POST /api/book/update/1
    ```

16. **Bandingkan** normalisasi (3NF) vs denormalisasi untuk Sistem Akademik UAI dalam skenario: (a) menampilkan KRS mahasiswa (read-heavy), (b) mengupdate jadwal kuliah (write-heavy). Kapan masing-masing lebih tepat?

17. **Rancang** strategi API versioning untuk aplikasi MyPertamina yang harus mendukung: mobile app v1 (legacy), mobile app v2 (current), web app v3 (upcoming). Bagaimana mengelola 3 versi API secara bersamaan?

18. **Kritisi** apakah desain database berikut sudah memenuhi 3NF? Jika tidak, tunjukkan langkah normalisasi:
    ```
    orders(order_id, customer_name, customer_email,
           product_name, product_price, quantity,
           total, order_date)
    ```

19. **Rancang** arsitektur API gateway untuk sistem microservices universitas yang terdiri dari: Auth Service, Akademik Service, Keuangan Service, Perpustakaan Service. Gambarkan Container Diagram (C4 Level 2) dan desain routing API gateway.

---

## Rangkuman

1. **UML** adalah bahasa standar untuk memodelkan desain software — 14 diagram dalam 2 kategori (structural & behavioral).

2. **Use Case Diagram** menggambarkan interaksi aktor-sistem — siapa melakukan apa.

3. **Class Diagram** menggambarkan struktur statis (class, atribut, method, relasi) — dasar dari desain OOP.

4. **Sequence Diagram** menggambarkan interaksi antar objek dalam urutan waktu — siapa memanggil siapa.

5. **Activity Diagram** menggambarkan alur proses (workflow) dengan decision points dan parallel activities.

6. **State Machine Diagram** menggambarkan lifecycle objek — bagaimana state berubah akibat events.

7. **ERD** dan **normalisasi** (1NF-3NF) menghasilkan desain database yang efisien, konsisten, dan bebas anomali.

8. **Denormalisasi** kadang diperlukan untuk performance pada read-heavy systems.

9. **REST API** menggunakan HTTP methods pada resource URLs dengan JSON — ikuti best practices: noun URLs, proper status codes, versioning.

10. **OpenAPI/Swagger** adalah standar dokumentasi API yang memungkinkan auto-generation client dan testing.

---

## Referensi

1. Fowler, M. (2003). *UML Distilled: A Brief Guide to the Standard Object Modeling Language* (3rd ed.). Addison-Wesley.
2. OMG. (2017). *Unified Modeling Language Specification v2.5.1*. Object Management Group.
3. Elmasri, R. & Navathe, S. (2016). *Fundamentals of Database Systems* (7th ed.). Pearson.
4. Fielding, R. T. (2000). *Architectural Styles and the Design of Network-based Software Architectures*. Doctoral Dissertation, UC Irvine.
5. Richardson, L. & Ruby, S. (2013). *RESTful Web APIs*. O'Reilly.
6. OpenAPI Initiative. (2024). *OpenAPI Specification v3.1.0*. https://spec.openapis.org/
7. Booch, G., Rumbaugh, J., & Jacobson, I. (2005). *The Unified Modeling Language User Guide* (2nd ed.). Addison-Wesley.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
