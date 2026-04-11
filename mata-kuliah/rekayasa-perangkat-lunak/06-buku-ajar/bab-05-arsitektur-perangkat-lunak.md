# BAB 5: ARSITEKTUR PERANGKAT LUNAK

**Oleh: Tri Aji Nugroho, S.T., M.T.**
**Mata Kuliah:** IF2205 Rekayasa Perangkat Lunak
**Program Studi Informatika — Universitas Al Azhar Indonesia**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi | Level Bloom | Estimasi Waktu |
|-----------|-----------|-------------|----------------|
| 3.1 | Menganalisis dan memilih arsitektur perangkat lunak (MVC, layered, microservices, event-driven) berdasarkan quality attributes | C4 (Menganalisis) | 75 menit |
| 3.2 | Menerapkan prinsip SOLID dan design patterns (Singleton, Factory, Observer, Strategy) dalam desain software | C3 (Menerapkan) | 75 menit |

---

## Peta Konsep Bab

```
                        ┌──────────────────────────────┐
                        │  ARSITEKTUR PERANGKAT LUNAK   │
                        └──────────────┬───────────────┘
               ┌───────────────┬───────┴───────┬───────────────┐
               ▼               ▼               ▼               ▼
     ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
     │ Architectural│ │   Quality   │ │    SOLID    │ │   Design    │
     │   Styles    │ │  Attributes │ │  Principles │ │  Patterns   │
     └──────┬──────┘ └──────┬──────┘ └──────┬──────┘ └──────┬──────┘
       ┌────┼────┐     ┌────┼────┐     ┌────┼────┐     ┌────┼────┐
       ▼    ▼    ▼     ▼    ▼    ▼     ▼    ▼    ▼     ▼    ▼    ▼
      MVC Layer Micro Perf Scal Sec   SRP  OCP  DIP  Sing Fact Obs
           │    serv                        │         leton ory  erver
           ▼                                ▼               │
       Event-                          Strategy             ▼
       Driven                          Pattern          ADR & C4
```

---

## 5.1 Apa Itu Arsitektur Perangkat Lunak?

> **Software architecture** adalah struktur fundamental dari sistem software — komponen-komponen, relasi antar komponen, dan prinsip-prinsip yang mengatur desain dan evolusinya (Bass et al., 2021).

Arsitektur adalah keputusan desain paling fundamental — yang **sulit diubah** setelah implementasi dimulai. Berbeda dengan desain detail (class, method), arsitektur menentukan "bentuk besar" dari sistem.

### 5.1.1 Mengapa Arsitektur Penting?

```
┌─────────────────────────────────────────────────────────────────┐
│                 DAMPAK KEPUTUSAN ARSITEKTUR                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Fase Awal (Mudah diubah)          Fase Lanjut (Sulit diubah)  │
│  ●────────────────────────────────────────────────────────●     │
│  │ Arsitektur dipilih                Biaya perubahan       │    │
│  │ Biaya: Rp 1 juta               Biaya: Rp 1 miliar+     │    │
│  │                                                         │    │
│  ▼                                                         ▼    │
│  [Requirements] → [Architecture] → [Design] → [Code] → [Deploy]│
│       ↑                                                         │
│  Keputusan arsitektur di sini menentukan segalanya              │
└─────────────────────────────────────────────────────────────────┘
```

Arsitektur software menentukan:

1. **Quality Attributes** — performance, scalability, maintainability, security
2. **Blueprint Komunikasi** — stakeholder (developer, PM, ops) berbicara dalam "bahasa" yang sama
3. **Struktur Tim** — Conway's Law: "Organizations design systems that mirror their communication structure"
4. **Technical Debt** jangka panjang — arsitektur buruk = hutang teknis yang terus menumpuk
5. **Kemampuan Evolusi** — seberapa mudah sistem beradaptasi terhadap perubahan kebutuhan

### 5.1.2 Conway's Law dalam Konteks Indonesia

Conway's Law menyatakan bahwa arsitektur software cenderung mencerminkan struktur organisasi yang membangunnya.

```
┌──────────────────────────────────────────────────────┐
│               CONWAY'S LAW                           │
│                                                      │
│  Struktur Organisasi      →    Arsitektur Software   │
│                                                      │
│  ┌────────┐                    ┌──────────┐          │
│  │Tim Auth│──┐                 │Service   │──┐       │
│  └────────┘  │                 │Auth      │  │       │
│  ┌────────┐  ├─ Komunikasi ─▶  ┌──────────┐  ├─ API │
│  │Tim Cart│──┤    antar tim    │Service   │──┤       │
│  └────────┘  │                 │Cart      │  │       │
│  ┌────────┐  │                 ┌──────────┐  │       │
│  │Tim Pay │──┘                 │Service   │──┘       │
│  └────────┘                    │Payment   │          │
│                                └──────────┘          │
└──────────────────────────────────────────────────────┘
```

**Contoh Indonesia — Gojek:**
Ketika Gojek masih kecil (2015), mereka menggunakan monolith karena timnya kecil. Seiring pertumbuhan menjadi 20+ tim engineering, mereka bermigrasi ke microservices agar setiap tim (GoRide, GoFood, GoPay) bisa develop dan deploy secara independen — sejalan dengan Conway's Law.

### 5.1.3 Architecture Decision Records (ADR)

ADR adalah dokumen singkat yang merekam **keputusan arsitektur beserta alasannya**. Ini penting agar anggota tim baru memahami *mengapa* keputusan dibuat.

**Template ADR:**

```
# ADR-001: Memilih Modular Monolith untuk Proyek Perpustakaan UAI

## Status
Accepted (2026-04-10)

## Context
Tim terdiri dari 4 mahasiswa semester 4 dengan pengalaman Flask.
Proyek harus selesai dalam 10 minggu.
Sistem perpustakaan memiliki 4 modul: auth, buku, peminjaman, laporan.

## Decision
Menggunakan arsitektur Modular Monolith dengan Flask Blueprints.
Setiap modul menjadi satu Blueprint terpisah.

## Consequences
+ Deployment sederhana (satu aplikasi)
+ Familiar bagi tim (Flask standar)
+ Bisa di-refactor ke microservices nanti jika dibutuhkan
- Tidak bisa scale per modul secara independen
- Semua modul share satu database

## Alternatives Considered
1. Microservices: Terlalu kompleks untuk tim 4 orang + 10 minggu
2. Pure Monolith (tanpa modular): Sulit di-maintain saat fitur bertambah
```

> **Tips:** Simpan file ADR di folder `docs/adr/` dalam repository proyek. Nomor secara berurutan (ADR-001, ADR-002, dst).

---

## 5.2 Architectural Styles

### 5.2.1 MVC (Model-View-Controller)

MVC memisahkan aplikasi menjadi tiga komponen utama, memungkinkan pengembangan paralel dan kemudahan testing.

```
┌──────────────────────────────────────────────────────────────┐
│                    MVC ARCHITECTURE                          │
│                                                              │
│  ┌─────────┐  1. Request   ┌──────────────┐  2. Query       │
│  │         │──────────────▶│              │──────────────┐  │
│  │  USER   │               │  CONTROLLER  │              │  │
│  │(Browser)│  6. Response  │ (Flask route) │  3. Data     │  │
│  │         │◀──────────────│              │◀─────────┐  │  │
│  └─────────┘               └──────┬───────┘          │  │  │
│                              │    │                   │  │  │
│                    4. Select │    │                   │  │  │
│                       View   │    │              ┌────┴──┴┐ │
│                              ▼    │              │ MODEL  │ │
│                        ┌──────────┴─┐            │ (Data  │ │
│                        │    VIEW    │            │  Logic) │ │
│                        │  (Jinja2   │            │ SQLAlch │ │
│                        │  Template) │            │  emy    │ │
│                        └────────────┘            └────────┘ │
│                     5. Rendered HTML                         │
└──────────────────────────────────────────────────────────────┘
```

**Komponen:**
- **Model** — data dan business logic (SQLAlchemy models, validasi data)
- **View** — tampilan ke pengguna (HTML templates, JSON response)
- **Controller** — menerima input, memanggil Model, memilih View (Flask routes)

**Contoh Flask MVC Lengkap:**

```python
# ============================================
# Model (models.py) - Data & Business Logic
# ============================================
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Buku(db.Model):
    """Model untuk data buku perpustakaan."""
    __tablename__ = 'buku'
    id = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String(200), nullable=False)
    penulis = db.Column(db.String(100))
    isbn = db.Column(db.String(13), unique=True)
    stok = db.Column(db.Integer, default=0)

    def to_dict(self):
        """Konversi ke dictionary untuk JSON response."""
        return {
            'id': self.id,
            'judul': self.judul,
            'penulis': self.penulis,
            'stok': self.stok
        }

    def kurangi_stok(self):
        """Business logic: kurangi stok saat dipinjam."""
        if self.stok <= 0:
            raise ValueError("Stok buku habis")
        self.stok -= 1


# ============================================
# Controller (routes.py) - Menerima & Mengarahkan
# ============================================
from flask import Blueprint, render_template, request, jsonify

buku_bp = Blueprint('buku', __name__, url_prefix='/buku')

@buku_bp.route('/')
def daftar_buku():
    """Controller: ambil data dari Model, kirim ke View."""
    buku_list = Buku.query.all()
    return render_template('buku/daftar.html', buku_list=buku_list)

@buku_bp.route('/api', methods=['GET'])
def api_daftar_buku():
    """Controller: endpoint API mengembalikan JSON."""
    buku_list = Buku.query.all()
    return jsonify([b.to_dict() for b in buku_list])


# ============================================
# View (templates/buku/daftar.html) - Tampilan
# ============================================
# {% extends "base.html" %}
# {% block content %}
#   <h1>Daftar Buku Perpustakaan</h1>
#   <table>
#     {% for buku in buku_list %}
#     <tr>
#       <td>{{ buku.judul }}</td>
#       <td>{{ buku.penulis }}</td>
#       <td>{{ buku.stok }}</td>
#     </tr>
#     {% endfor %}
#   </table>
# {% endblock %}
```

### 5.2.2 Layered Architecture

Arsitektur berlapis (layered) mengisolasi concerns ke dalam layer-layer yang memiliki tanggung jawab berbeda. Aturan utama: **setiap layer hanya boleh mengakses layer tepat di bawahnya** (strict layering).

```
┌─────────────────────────────────────────────────────────┐
│                  LAYERED ARCHITECTURE                    │
│                                                         │
│  ┌───────────────────────────────────────────────────┐  │
│  │            PRESENTATION LAYER                     │  │
│  │   HTML, CSS, JavaScript, Jinja2 Templates         │  │
│  │   Tanggung jawab: Tampilan & interaksi user       │  │
│  └───────────────────────┬───────────────────────────┘  │
│                          │ Hanya panggil Business Layer  │
│  ┌───────────────────────▼───────────────────────────┐  │
│  │            BUSINESS LOGIC LAYER                   │  │
│  │   Flask routes, Services, Validators              │  │
│  │   Tanggung jawab: Aturan bisnis & logika          │  │
│  └───────────────────────┬───────────────────────────┘  │
│                          │ Hanya panggil Data Layer     │
│  ┌───────────────────────▼───────────────────────────┐  │
│  │            DATA ACCESS LAYER                      │  │
│  │   SQLAlchemy ORM, Repositories                    │  │
│  │   Tanggung jawab: Akses & manipulasi data         │  │
│  └───────────────────────┬───────────────────────────┘  │
│                          │ Hanya akses Database          │
│  ┌───────────────────────▼───────────────────────────┐  │
│  │            DATABASE LAYER                         │  │
│  │   SQLite, PostgreSQL                              │  │
│  │   Tanggung jawab: Penyimpanan data persisten      │  │
│  └───────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

**Implementasi Layered di Python:**

```python
# ============================================
# Data Access Layer (repositories/buku_repo.py)
# ============================================
class BukuRepository:
    """Repository pattern: abstraksi akses data."""

    def get_all(self):
        return Buku.query.all()

    def get_by_id(self, buku_id):
        return Buku.query.get_or_404(buku_id)

    def search(self, keyword):
        return Buku.query.filter(
            Buku.judul.ilike(f'%{keyword}%')
        ).all()

    def save(self, buku):
        db.session.add(buku)
        db.session.commit()
        return buku


# ============================================
# Business Logic Layer (services/buku_service.py)
# ============================================
class BukuService:
    """Service layer: berisi business logic."""

    def __init__(self, repo: BukuRepository):
        self.repo = repo  # dependency injection

    def get_semua_buku(self):
        return self.repo.get_all()

    def tambah_buku(self, data):
        # Validasi business rules
        if not data.get('judul'):
            raise ValueError("Judul buku wajib diisi")
        if len(data.get('isbn', '')) != 13:
            raise ValueError("ISBN harus 13 digit")

        buku = Buku(
            judul=data['judul'],
            penulis=data.get('penulis', 'Unknown'),
            isbn=data['isbn'],
            stok=data.get('stok', 0)
        )
        return self.repo.save(buku)


# ============================================
# Presentation Layer (routes/buku_routes.py)
# ============================================
buku_service = BukuService(BukuRepository())

@app.route('/api/buku', methods=['POST'])
def tambah_buku():
    try:
        data = request.get_json()
        buku = buku_service.tambah_buku(data)
        return jsonify(buku.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
```

### 5.2.3 Microservices Architecture

Microservices memecah aplikasi menjadi **service-service kecil yang independen**, masing-masing memiliki database sendiri dan berkomunikasi via API.

```
┌────────────────────────────────────────────────────────────────┐
│                  MICROSERVICES ARCHITECTURE                     │
│                                                                │
│  ┌───────────┐                                                 │
│  │  API      │                                                 │
│  │  Gateway  │◀──── Client (Web/Mobile)                        │
│  └─────┬─────┘                                                 │
│        │                                                       │
│   ┌────┼──────────┬──────────────┬──────────────┐              │
│   │    ▼          ▼              ▼              ▼              │
│ ┌─┴──────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐         │
│ │ Auth   │  │  Buku    │  │Peminjaman│  │ Notif    │         │
│ │Service │  │ Service  │  │ Service  │  │ Service  │         │
│ ├────────┤  ├──────────┤  ├──────────┤  ├──────────┤         │
│ │Port    │  │Port      │  │Port      │  │Port      │         │
│ │:5001   │  │:5002     │  │:5003     │  │:5004     │         │
│ └───┬────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘         │
│     │            │             │              │               │
│     ▼            ▼             ▼              ▼               │
│  ┌──────┐   ┌──────┐    ┌──────┐        ┌──────┐            │
│  │Users │   │Books │    │Loans │        │Redis │            │
│  │ DB   │   │ DB   │    │ DB   │        │Queue │            │
│  └──────┘   └──────┘    └──────┘        └──────┘            │
└────────────────────────────────────────────────────────────────┘
```

### 5.2.4 Event-Driven Architecture

Pada arsitektur event-driven, komponen berkomunikasi melalui **events** (peristiwa) alih-alih pemanggilan langsung. Ini memungkinkan loose coupling yang tinggi.

```
┌────────────────────────────────────────────────────────────────┐
│                EVENT-DRIVEN ARCHITECTURE                       │
│                                                                │
│  Producer                Event Bus              Consumer       │
│  ┌──────────┐        ┌──────────────┐       ┌──────────┐     │
│  │ Order    │──emit──▶│              │──────▶│ Inventory│     │
│  │ Service  │ "order  │   Message    │       │ Service  │     │
│  └──────────┘ created"│   Broker     │       └──────────┘     │
│                       │  (RabbitMQ/  │       ┌──────────┐     │
│  ┌──────────┐         │   Redis/     │──────▶│ Email    │     │
│  │ Payment  │──emit──▶│   Kafka)     │       │ Service  │     │
│  │ Service  │"payment │              │       └──────────┘     │
│  └──────────┘ done"   │              │       ┌──────────┐     │
│                       │              │──────▶│ Analytics│     │
│                       └──────────────┘       │ Service  │     │
│                                              └──────────┘     │
└────────────────────────────────────────────────────────────────┘
```

**Contoh Event-Driven di Python:**

```python
import redis
import json

# ============================================
# Event Bus sederhana menggunakan Redis Pub/Sub
# ============================================
class EventBus:
    """Event bus menggunakan Redis untuk publish/subscribe."""

    def __init__(self):
        self.redis = redis.Redis(host='localhost', port=6379)
        self.pubsub = self.redis.pubsub()

    def publish(self, event_type, data):
        """Publish event ke channel."""
        event = {
            'type': event_type,
            'data': data,
            'timestamp': '2026-04-11T10:00:00'
        }
        self.redis.publish(event_type, json.dumps(event))
        print(f"[EVENT] Published: {event_type}")

    def subscribe(self, event_type, handler):
        """Subscribe ke event tertentu."""
        self.pubsub.subscribe(**{event_type: handler})


# ============================================
# Producer: Order Service
# ============================================
class OrderService:
    def __init__(self, event_bus: EventBus):
        self.event_bus = event_bus

    def create_order(self, order_data):
        # Simpan order ke database
        order_id = self._save_to_db(order_data)
        # Publish event — tidak perlu tahu siapa yang listen
        self.event_bus.publish('order_created', {
            'order_id': order_id,
            'items': order_data['items'],
            'user_email': order_data['email']
        })
        return order_id


# ============================================
# Consumer: Email Service (otomatis bereaksi)
# ============================================
def handle_order_created(message):
    data = json.loads(message['data'])
    print(f"[EMAIL] Kirim konfirmasi ke {data['data']['user_email']}")

event_bus = EventBus()
event_bus.subscribe('order_created', handle_order_created)
```

**Contoh Indonesia — TransJakarta Real-time Tracking:**
Sistem TransJakarta menggunakan event-driven architecture: setiap bus mengirimkan event posisi GPS setiap 10 detik. Event ini dikonsumsi oleh: (1) Layanan peta real-time di aplikasi penumpang, (2) Sistem prediksi waktu kedatangan, (3) Dashboard monitoring Dishub DKI.

### 5.2.5 Pipe-and-Filter Architecture

Arsitektur pipe-and-filter memproses data melalui serangkaian transformasi berurutan. Setiap filter menerima input, memproses, dan menghasilkan output.

```
┌───────────────────────────────────────────────────────────────┐
│              PIPE-AND-FILTER ARCHITECTURE                     │
│                                                               │
│  ┌──────┐    ┌──────────┐    ┌──────────┐    ┌───────────┐   │
│  │Input │───▶│ Filter 1 │───▶│ Filter 2 │───▶│ Filter 3  │   │
│  │ Data │pipe│ (Parse)  │pipe│(Transform│pipe│ (Output)  │   │
│  └──────┘    └──────────┘    └──────────┘    └───────────┘   │
│                                                               │
│  Contoh: ETL Pipeline                                         │
│  CSV file → Parse → Validasi → Transform → Load ke DB         │
└───────────────────────────────────────────────────────────────┘
```

**Contoh Python Pipe-and-Filter:**

```python
# Pipeline sederhana untuk memproses data mahasiswa
def parse_csv(raw_data):
    """Filter 1: Parse CSV menjadi list of dict."""
    lines = raw_data.strip().split('\n')
    headers = lines[0].split(',')
    return [dict(zip(headers, line.split(','))) for line in lines[1:]]

def validate(records):
    """Filter 2: Validasi data — buang yang tidak lengkap."""
    return [r for r in records if r.get('nama') and r.get('nim')]

def transform(records):
    """Filter 3: Transformasi — standardisasi format."""
    for r in records:
        r['nama'] = r['nama'].strip().title()
        r['nim'] = r['nim'].strip()
    return records

def load_to_db(records):
    """Filter 4: Simpan ke database."""
    for r in records:
        print(f"Simpan: {r['nim']} - {r['nama']}")
    return len(records)

# Pipeline execution
raw = "nama,nim\nAhmad Fauzi,2025001\nbudi santoso,2025002"
result = load_to_db(transform(validate(parse_csv(raw))))
print(f"Total disimpan: {result}")
# Output:
# Simpan: 2025001 - Ahmad Fauzi
# Simpan: 2025002 - Budi Santoso
# Total disimpan: 2
```

### 5.2.6 Perbandingan Architectural Styles

| Aspek | MVC | Layered | Microservices | Event-Driven | Pipe-Filter |
|-------|-----|---------|---------------|-------------|-------------|
| **Kompleksitas** | Rendah | Rendah-Sedang | Tinggi | Sedang-Tinggi | Rendah |
| **Scalability** | Vertikal | Vertikal | Horizontal per service | Horizontal | Per filter |
| **Coupling** | Sedang | Rendah (antar layer) | Sangat rendah | Sangat rendah | Rendah |
| **Deployment** | Satu unit | Satu unit | Independen | Independen | Satu/multi |
| **Data** | Satu DB | Satu DB | DB per service | Event store | Stream |
| **Tim** | 1-5 orang | 3-10 orang | Tim per service | Tim per service | 1-5 orang |
| **Cocok untuk** | Web apps | Enterprise apps | Platform besar | Real-time systems | Data pipeline |
| **Contoh Indonesia** | SIAKAD UAI | Sistem BPJS | Gojek, Tokopedia | TransJakarta tracking | ETL BPS data |

### 5.2.7 Monolith vs Modular Monolith vs Microservices

```
┌──────────────────────────────────────────────────────────────────┐
│              EVOLUSI ARSITEKTUR                                   │
│                                                                  │
│  Monolith          Modular Monolith       Microservices          │
│  ┌──────────┐      ┌──────────────┐       ┌────┐ ┌────┐ ┌────┐ │
│  │ ████████ │      │ ┌──┐┌──┐┌──┐│       │Auth│ │Buku│ │Loan│ │
│  │ ████████ │  →   │ │A ││B ││C ││   →   │    │ │    │ │    │ │
│  │ ████████ │      │ └──┘└──┘└──┘│       └──┬─┘ └──┬─┘ └──┬─┘ │
│  │ ████████ │      │  Satu deploy │       ┌──┴┐ ┌──┴┐ ┌──┴┐   │
│  └──────────┘      └──────────────┘       │DB1│ │DB2│ │DB3│   │
│  Semua jadi satu   Modular internal       └───┘ └───┘ └───┘   │
│                    Deploy satu unit        Deploy independen     │
│                                                                  │
│  ← Proyek kuliah                   Enterprise →                  │
│    (4 orang, 10 minggu)           (100+ engineer)                │
└──────────────────────────────────────────────────────────────────┘
```

**Rekomendasi untuk proyek kuliah:** Mulai dengan **Modular Monolith** menggunakan Flask Blueprints.

```python
# Modular Monolith dengan Flask Blueprints
from flask import Flask

# Modul Auth
from auth.routes import auth_bp      # auth/__init__.py, auth/routes.py, auth/models.py
# Modul Buku
from buku.routes import buku_bp      # buku/__init__.py, buku/routes.py, buku/models.py
# Modul Peminjaman
from peminjaman.routes import pinjam_bp

app = Flask(__name__)
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(buku_bp, url_prefix='/buku')
app.register_blueprint(pinjam_bp, url_prefix='/peminjaman')
```

**Struktur folder Modular Monolith:**

```
perpustakaan/
├── app.py                  # Entry point
├── config.py               # Konfigurasi
├── auth/                   # Modul Auth
│   ├── __init__.py
│   ├── models.py           # User model
│   ├── routes.py           # Login, register
│   └── services.py         # Auth logic
├── buku/                   # Modul Buku
│   ├── __init__.py
│   ├── models.py           # Buku model
│   ├── routes.py           # CRUD buku
│   └── services.py         # Business logic buku
├── peminjaman/             # Modul Peminjaman
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── services.py
└── templates/              # Shared templates
    ├── base.html
    └── ...
```

---

## 5.3 Quality Attributes (Atribut Kualitas)

Quality attributes adalah **karakteristik non-fungsional** yang menentukan seberapa baik sistem bekerja — bukan *apa* yang dilakukan, tapi *seberapa baik* melakukannya.

### 5.3.1 Enam Quality Attributes Utama

| Quality Attribute | Deskripsi | Metrik | Trade-off |
|-------------------|-----------|--------|-----------|
| **Performance** | Seberapa cepat sistem merespons | Response time < 200ms, throughput 1000 req/s | vs Maintainability |
| **Scalability** | Kemampuan handle beban yang meningkat | Users/detik, data growth handling | vs Simplicity |
| **Security** | Perlindungan dari ancaman | Vulnerabilities count, compliance level | vs Usability |
| **Maintainability** | Kemudahan diubah dan diperbaiki | Cyclomatic complexity < 10, coupling rendah | vs Performance |
| **Availability** | Uptime sistem (seberapa sering bisa diakses) | 99.9% = 8.76 jam downtime/tahun | vs Cost |
| **Testability** | Kemudahan untuk di-test | Code coverage > 80%, test execution time | vs Dev speed |

### 5.3.2 Quality Attribute Scenarios

Cara formal mendokumentasikan quality attributes menggunakan **scenario**:

```
┌────────────────────────────────────────────────────────────────┐
│         QUALITY ATTRIBUTE SCENARIO                             │
│                                                                │
│  Stimulus:     1000 mahasiswa login bersamaan                  │
│  Source:       Mahasiswa saat KRS online                       │
│  Environment:  Jam sibuk (08:00 WIB hari pertama KRS)          │
│  Artifact:     Sistem Akademik UAI                             │
│  Response:     Sistem tetap responsif                          │
│  Measure:      Response time < 3 detik, 0% error rate          │
└────────────────────────────────────────────────────────────────┘
```

**Contoh Indonesia — Sistem Akademik saat KRS Online:**

Setiap awal semester, ribuan mahasiswa UAI mengakses SIAKAD secara bersamaan untuk KRS. Quality attributes yang kritis:
- **Performance**: halaman harus load < 3 detik
- **Availability**: 99.9% uptime selama periode KRS (3 hari)
- **Scalability**: mampu handle 5x traffic normal

### 5.3.3 Trade-off Analysis

Tidak ada arsitektur yang sempurna di semua quality attributes. Selalu ada **trade-off**.

```
┌─────────────────────────────────────────────────────┐
│            QUALITY ATTRIBUTE TRADE-OFFS              │
│                                                     │
│  Performance ◀──────────────────▶ Maintainability   │
│     (Cache, denormalize)    (Clean code, modularity) │
│                                                     │
│  Security    ◀──────────────────▶ Usability         │
│     (2FA, encryption)       (Simple login, fast)     │
│                                                     │
│  Availability◀──────────────────▶ Cost              │
│     (Redundancy, backup)    (Budget terbatas)        │
│                                                     │
│  Scalability ◀──────────────────▶ Simplicity        │
│     (Distributed, async)    (Monolith, synchronous)  │
└─────────────────────────────────────────────────────┘
```

> **Contoh Trade-off di Tokopedia:** Untuk fitur search produk, Tokopedia memilih menggunakan Elasticsearch (performance tinggi) meskipun menambah operational complexity. Trade-off: performance > simplicity karena search adalah fitur kritis bagi e-commerce.

---

## 5.4 C4 Model — Visualisasi Arsitektur

C4 Model (oleh Simon Brown) memberikan pendekatan **hierarkis** untuk menggambarkan arsitektur software, dari level tertinggi (konteks) hingga level terendah (kode).

```
┌──────────────────────────────────────────────────┐
│                  C4 MODEL                        │
│                                                  │
│  Level 1: System Context   ← Siapa pakai sistem?│
│     ┌─────────────┐                              │
│     │  [Person]   │──▶ [System]──▶ [External]   │
│     └─────────────┘                              │
│              │                                   │
│              ▼                                   │
│  Level 2: Container        ← Dari apa sistem?   │
│     ┌──────┐ ┌──────┐ ┌──────┐                  │
│     │Web   │ │API   │ │ DB   │                  │
│     │App   │ │Server│ │      │                  │
│     └──────┘ └──────┘ └──────┘                  │
│              │                                   │
│              ▼                                   │
│  Level 3: Component        ← Apa isi container? │
│     ┌──────┐ ┌──────┐ ┌──────┐                  │
│     │Auth  │ │Buku  │ │Loan  │                  │
│     │Ctrl  │ │Ctrl  │ │Ctrl  │                  │
│     └──────┘ └──────┘ └──────┘                  │
│              │                                   │
│              ▼                                   │
│  Level 4: Code             ← Class diagram (UML)│
│     (Biasanya auto-generated)                    │
└──────────────────────────────────────────────────┘
```

**Level 1 — System Context Diagram (Perpustakaan UAI):**

```
┌─────────────────────────────────────────────────────────────┐
│                SYSTEM CONTEXT DIAGRAM                        │
│                                                             │
│  ┌──────────┐                           ┌────────────────┐  │
│  │Mahasiswa │──── Cari & pinjam buku ──▶│                │  │
│  │          │◀── Notifikasi deadline ───│                │  │
│  └──────────┘                           │   Sistem       │  │
│                                         │ Perpustakaan   │  │
│  ┌──────────┐                           │   Digital      │  │
│  │ Petugas  │──── Kelola buku ─────────▶│                │  │
│  │Perpustak.│◀── Laporan sirkulasi ────│                │  │
│  └──────────┘                           └───────┬────────┘  │
│                                                 │           │
│                                    ┌────────────▼────────┐  │
│                                    │   Email Service     │  │
│                                    │   (SendGrid/SMTP)   │  │
│                                    └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

**Level 2 — Container Diagram:**

```
┌─────────────────────────────────────────────────────────────┐
│                   CONTAINER DIAGRAM                          │
│                                                             │
│  ┌──────────┐     HTTPS      ┌──────────────────────────┐  │
│  │ Browser  │───────────────▶│   Web Application        │  │
│  │ (User)   │◀───────────────│   (Flask + Jinja2)       │  │
│  └──────────┘                │   Port 5000              │  │
│                              └────────────┬─────────────┘  │
│                                           │                 │
│  ┌──────────┐     HTTPS      ┌────────────▼─────────────┐  │
│  │ Mobile   │───────────────▶│   REST API               │  │
│  │ App      │◀───────────────│   (Flask-RESTful)        │  │
│  └──────────┘                │   /api/v1/*              │  │
│                              └────────────┬─────────────┘  │
│                                           │ SQLAlchemy     │
│                              ┌────────────▼─────────────┐  │
│                              │   Database               │  │
│                              │   (SQLite / PostgreSQL)  │  │
│                              └──────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## 5.5 SOLID Principles

SOLID adalah lima prinsip desain object-oriented yang menghasilkan kode yang **maintainable, extensible, dan testable**.

### 5.5.1 Single Responsibility Principle (SRP)

> "Sebuah class harus memiliki satu, dan hanya satu, alasan untuk berubah." — Robert C. Martin

```python
# ============================================
# BURUK: UserService punya banyak tanggung jawab
# ============================================
class UserService:
    def register(self, nama, email, password):
        # Validasi input
        if '@' not in email:
            raise ValueError("Email tidak valid")
        # Simpan ke database
        user = User(nama=nama, email=email)
        db.session.add(user)
        db.session.commit()
        # Kirim email selamat datang
        self._send_email(email, "Selamat datang!")
        # Log aktivitas
        print(f"[LOG] User {nama} registered at {datetime.now()}")

    def _send_email(self, to, subject):
        # Logic kirim email...
        pass


# ============================================
# BAIK: Setiap class punya satu tanggung jawab
# ============================================
class UserValidator:
    """Tanggung jawab: validasi data user."""
    def validate(self, email, password):
        if '@' not in email:
            raise ValueError("Email tidak valid")
        if len(password) < 8:
            raise ValueError("Password minimal 8 karakter")

class UserRepository:
    """Tanggung jawab: akses data user ke database."""
    def save(self, user):
        db.session.add(user)
        db.session.commit()
        return user

class EmailService:
    """Tanggung jawab: kirim email."""
    def send_welcome(self, email, nama):
        print(f"[EMAIL] Kirim welcome email ke {email}")

class ActivityLogger:
    """Tanggung jawab: logging aktivitas."""
    def log(self, message):
        print(f"[LOG] {datetime.now()}: {message}")

class UserService:
    """Tanggung jawab: koordinasi registrasi user."""
    def __init__(self, validator, repo, email_svc, logger):
        self.validator = validator
        self.repo = repo
        self.email_svc = email_svc
        self.logger = logger

    def register(self, nama, email, password):
        self.validator.validate(email, password)
        user = self.repo.save(User(nama=nama, email=email))
        self.email_svc.send_welcome(email, nama)
        self.logger.log(f"User {nama} registered")
        return user
```

### 5.5.2 Open/Closed Principle (OCP)

> "Software entities harus terbuka untuk ekstensi, tertutup untuk modifikasi."

```python
# ============================================
# BURUK: Harus modifikasi class setiap ada tipe baru
# ============================================
class DiskonCalculator:
    def hitung(self, tipe, harga):
        if tipe == "mahasiswa":
            return harga * 0.8   # Diskon 20%
        elif tipe == "dosen":
            return harga * 0.7   # Diskon 30%
        elif tipe == "alumni":      # ← Harus edit class!
            return harga * 0.85
        # Setiap tipe baru = tambah elif = melanggar OCP


# ============================================
# BAIK: Ekstensi via class baru, tanpa modifikasi
# ============================================
from abc import ABC, abstractmethod

class DiskonStrategy(ABC):
    @abstractmethod
    def hitung(self, harga: float) -> float:
        pass

class DiskonMahasiswa(DiskonStrategy):
    def hitung(self, harga):
        return harga * 0.8  # Diskon 20%

class DiskonDosen(DiskonStrategy):
    def hitung(self, harga):
        return harga * 0.7  # Diskon 30%

class DiskonAlumni(DiskonStrategy):
    """Tambah tipe baru = tambah class baru, BUKAN edit yang ada."""
    def hitung(self, harga):
        return harga * 0.85  # Diskon 15%

class KasirService:
    def proses_pembayaran(self, harga, diskon: DiskonStrategy):
        total = diskon.hitung(harga)
        print(f"Total bayar: Rp {total:,.0f}")
        return total

# Penggunaan
kasir = KasirService()
kasir.proses_pembayaran(100_000, DiskonMahasiswa())  # Rp 80,000
kasir.proses_pembayaran(100_000, DiskonAlumni())     # Rp 85,000
```

### 5.5.3 Liskov Substitution Principle (LSP)

> "Subclass harus bisa menggantikan parent class tanpa merusak perilaku program."

```python
# ============================================
# BURUK: Melanggar LSP
# ============================================
class Burung:
    def terbang(self):
        return "Terbang di udara"

class Elang(Burung):
    def terbang(self):
        return "Terbang tinggi di angkasa"

class Penguin(Burung):
    def terbang(self):
        raise Exception("Penguin tidak bisa terbang!")  # ← Melanggar LSP!


# ============================================
# BAIK: Desain ulang hierarki
# ============================================
class Burung(ABC):
    @abstractmethod
    def bergerak(self):
        pass

class BurungTerbang(Burung):
    def bergerak(self):
        return "Terbang di udara"

class BurungBerenang(Burung):
    def bergerak(self):
        return "Berenang di air"

class Elang(BurungTerbang):
    def bergerak(self):
        return "Terbang tinggi di angkasa"

class Penguin(BurungBerenang):
    def bergerak(self):
        return "Berenang cepat di air dingin"

# Semua bisa digunakan secara polimorfik tanpa error
burung_list = [Elang(), Penguin()]
for b in burung_list:
    print(b.bergerak())  # Tidak ada exception
```

### 5.5.4 Interface Segregation Principle (ISP)

> "Client tidak boleh dipaksa bergantung pada interface yang tidak mereka gunakan."

```python
# ============================================
# BURUK: Interface terlalu besar (fat interface)
# ============================================
class IWorker(ABC):
    @abstractmethod
    def bekerja(self): pass
    @abstractmethod
    def makan(self): pass
    @abstractmethod
    def tidur(self): pass

class Robot(IWorker):
    def bekerja(self):
        return "Robot bekerja"
    def makan(self):
        raise NotImplementedError("Robot tidak makan!")  # Dipaksa implementasi
    def tidur(self):
        raise NotImplementedError("Robot tidak tidur!")


# ============================================
# BAIK: Interface kecil dan spesifik
# ============================================
class IWorkable(ABC):
    @abstractmethod
    def bekerja(self): pass

class IFeedable(ABC):
    @abstractmethod
    def makan(self): pass

class ISleepable(ABC):
    @abstractmethod
    def tidur(self): pass

class Manusia(IWorkable, IFeedable, ISleepable):
    def bekerja(self): return "Manusia bekerja"
    def makan(self): return "Manusia makan"
    def tidur(self): return "Manusia tidur"

class Robot(IWorkable):  # Hanya implementasi yang relevan
    def bekerja(self): return "Robot bekerja 24/7"
```

### 5.5.5 Dependency Inversion Principle (DIP)

> "Module tingkat tinggi tidak boleh bergantung pada module tingkat rendah. Keduanya harus bergantung pada abstraksi."

```python
# ============================================
# BURUK: Bergantung langsung pada implementasi
# ============================================
class OrderService:
    def __init__(self):
        self.db = MySQLDatabase()  # Tight coupling ke MySQL!
        self.notif = WhatsAppNotifier()  # Tight coupling ke WhatsApp!

    def create_order(self, data):
        self.db.insert("orders", data)
        self.notif.send(f"Order {data['id']} dibuat")


# ============================================
# BAIK: Bergantung pada abstraksi (interface)
# ============================================
class DatabaseInterface(ABC):
    @abstractmethod
    def insert(self, table, data): pass

class NotifierInterface(ABC):
    @abstractmethod
    def send(self, message): pass

class MySQLDatabase(DatabaseInterface):
    def insert(self, table, data):
        print(f"[MySQL] INSERT INTO {table}")

class SQLiteDatabase(DatabaseInterface):
    def insert(self, table, data):
        print(f"[SQLite] INSERT INTO {table}")

class WhatsAppNotifier(NotifierInterface):
    def send(self, message):
        print(f"[WA] {message}")

class EmailNotifier(NotifierInterface):
    def send(self, message):
        print(f"[Email] {message}")

class OrderService:
    def __init__(self, db: DatabaseInterface, notif: NotifierInterface):
        self.db = db      # Dependency injection
        self.notif = notif

    def create_order(self, data):
        self.db.insert("orders", data)
        self.notif.send(f"Order {data['id']} dibuat")

# Mudah diganti implementasi tanpa mengubah OrderService
service = OrderService(SQLiteDatabase(), EmailNotifier())
service.create_order({'id': 1, 'item': 'Buku Clean Code'})
# Output:
# [SQLite] INSERT INTO orders
# [Email] Order 1 dibuat
```

### 5.5.6 Ringkasan SOLID

| Prinsip | Singkatan | Inti | Pertanyaan Pengecekan |
|---------|-----------|------|----------------------|
| **S**ingle Responsibility | SRP | Satu class = satu alasan berubah | "Apakah class ini punya lebih dari satu alasan untuk diubah?" |
| **O**pen/Closed | OCP | Ekstensi yes, modifikasi no | "Apakah saya harus edit class yang ada untuk menambah fitur baru?" |
| **L**iskov Substitution | LSP | Subclass = substitusi parent | "Apakah subclass ini bisa menggantikan parent tanpa error?" |
| **I**nterface Segregation | ISP | Interface kecil & spesifik | "Apakah ada method yang tidak dipakai oleh implementor?" |
| **D**ependency Inversion | DIP | Bergantung pada abstraksi | "Apakah class ini langsung membuat instance dependensinya?" |

---

## 5.6 Design Patterns (GoF)

Design patterns adalah **solusi terbukti untuk masalah desain yang berulang**. Ditemukan oleh Gang of Four (GoF) — Gamma, Helm, Johnson, Vlissides.

### 5.6.1 Singleton Pattern

**Masalah:** Hanya boleh ada satu instance dari sebuah class (misal: koneksi database, konfigurasi aplikasi).

```
┌────────────────────────────────────────────┐
│             SINGLETON PATTERN              │
│                                            │
│  ┌──────────────────┐                      │
│  │ DatabaseConnection│                     │
│  ├──────────────────┤                      │
│  │ - _instance: cls │   Hanya satu instance│
│  ├──────────────────┤   yang dibuat        │
│  │ + __new__()      │                      │
│  │ + get_connection()│                     │
│  └──────────────────┘                      │
│         ▲                                  │
│         │ Semua akses via instance tunggal  │
│    ┌────┼────┐                             │
│    ▼    ▼    ▼                             │
│  obj1  obj2  obj3  ← Semua menunjuk        │
│                      ke objek yang sama    │
└────────────────────────────────────────────┘
```

```python
class DatabaseConnection:
    """Singleton: hanya satu koneksi database untuk seluruh aplikasi."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = "Connected to SQLite"
            cls._instance.queries_count = 0
        return cls._instance

    def execute(self, query):
        self.queries_count += 1
        print(f"[DB] Executing query #{self.queries_count}: {query}")

# Penggunaan — semua variabel menunjuk ke objek yang sama
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)  # True — hanya satu instance!

db1.execute("SELECT * FROM buku")       # Query #1
db2.execute("INSERT INTO buku VALUES")   # Query #2 (counter tetap lanjut)
print(db1.queries_count)  # 2
```

> **Kapan digunakan:** Koneksi database, konfigurasi global, logging, cache manager.
> **Perhatian:** Singleton bisa menyulitkan testing. Gunakan dengan bijak.

### 5.6.2 Factory Pattern

**Masalah:** Membuat objek tanpa meng-expose logic pembuatan ke client. Client hanya perlu tahu "apa yang diinginkan", bukan "bagaimana membuatnya".

```
┌────────────────────────────────────────────────────────┐
│                FACTORY PATTERN                         │
│                                                        │
│  Client → "Saya mau WhatsApp" → Factory → WhatsApp()  │
│  Client → "Saya mau Email"    → Factory → Email()     │
│                                                        │
│               ┌──────────────────┐                     │
│               │NotificationFactory│                    │
│               ├──────────────────┤                     │
│               │+ create(channel) │                     │
│               └────────┬─────────┘                     │
│                        │ creates                       │
│           ┌────────────┼────────────┐                  │
│           ▼            ▼            ▼                  │
│  ┌──────────────┐ ┌──────────┐ ┌──────────┐           │
│  │ EmailNotif   │ │ WANotif  │ │ SMSNotif │           │
│  └──────────────┘ └──────────┘ └──────────┘           │
│     Semua implement Notification (ABC)                 │
└────────────────────────────────────────────────────────┘
```

```python
from abc import ABC, abstractmethod

class Notification(ABC):
    """Abstraksi notifikasi."""
    @abstractmethod
    def send(self, message: str) -> None: pass

class EmailNotification(Notification):
    def send(self, message):
        print(f"[EMAIL] Mengirim: {message}")

class WhatsAppNotification(Notification):
    def send(self, message):
        print(f"[WA] Mengirim: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"[SMS] Mengirim: {message}")

class PushNotification(Notification):
    def send(self, message):
        print(f"[PUSH] Mengirim: {message}")


class NotificationFactory:
    """Factory: membuat objek notifikasi berdasarkan channel."""

    _channels = {
        "email": EmailNotification,
        "whatsapp": WhatsAppNotification,
        "sms": SMSNotification,
        "push": PushNotification,
    }

    @classmethod
    def create(cls, channel: str) -> Notification:
        klass = cls._channels.get(channel)
        if klass is None:
            raise ValueError(f"Channel '{channel}' tidak didukung")
        return klass()

    @classmethod
    def register(cls, channel: str, klass):
        """Ekstensi: tambah channel baru tanpa modifikasi Factory."""
        cls._channels[channel] = klass


# Penggunaan
notif = NotificationFactory.create("whatsapp")
notif.send("Antrian Anda di Puskesmas Kecamatan Cilandak sudah dipanggil")
# Output: [WA] Mengirim: Antrian Anda di Puskesmas...

# Tambah channel baru tanpa modifikasi class yang ada (OCP compliant)
class TelegramNotification(Notification):
    def send(self, message):
        print(f"[TELEGRAM] Mengirim: {message}")

NotificationFactory.register("telegram", TelegramNotification)
notif2 = NotificationFactory.create("telegram")
notif2.send("Pesanan Anda sedang diproses")
```

> **Kapan digunakan:** Pembayaran multi-channel (BCA, GoPay, OVO), notifikasi, export format (PDF, Excel, CSV).

### 5.6.3 Observer Pattern

**Masalah:** Ketika satu objek berubah state, banyak objek lain harus diberitahu secara otomatis — tanpa coupling langsung.

```
┌────────────────────────────────────────────────────────────┐
│                 OBSERVER PATTERN                           │
│                                                            │
│  Subject (Publisher)          Observers (Subscribers)      │
│  ┌─────────────────┐         ┌──────────────────┐         │
│  │  EventManager   │──notify─▶│ LoggingObserver  │         │
│  │                 │         └──────────────────┘         │
│  │  subscribers:   │         ┌──────────────────┐         │
│  │   - logging     │──notify─▶│ EmailObserver    │         │
│  │   - email       │         └──────────────────┘         │
│  │   - analytics   │         ┌──────────────────┐         │
│  │                 │──notify─▶│ AnalyticsObserver│         │
│  └─────────────────┘         └──────────────────┘         │
│                                                            │
│  Event: "buku_dipinjam" → semua subscriber diberitahu     │
└────────────────────────────────────────────────────────────┘
```

```python
from typing import Callable, Dict, List

class EventManager:
    """Observer pattern: publish/subscribe untuk events."""

    def __init__(self):
        self._subscribers: Dict[str, List[Callable]] = {}

    def subscribe(self, event: str, callback: Callable):
        """Daftarkan observer untuk event tertentu."""
        self._subscribers.setdefault(event, []).append(callback)
        print(f"  [+] Subscribed to '{event}'")

    def unsubscribe(self, event: str, callback: Callable):
        """Hapus observer dari event."""
        if event in self._subscribers:
            self._subscribers[event].remove(callback)

    def notify(self, event: str, data: dict):
        """Kirim notifikasi ke semua subscriber event."""
        callbacks = self._subscribers.get(event, [])
        print(f"\n[EVENT] '{event}' fired — {len(callbacks)} subscribers")
        for callback in callbacks:
            callback(data)


# Observers (subscribers)
def logging_handler(data):
    print(f"  [LOG] {data['action']}: {data['detail']}")

def email_handler(data):
    print(f"  [EMAIL] Kirim ke {data.get('email', 'admin')}: {data['detail']}")

def stok_handler(data):
    print(f"  [STOK] Update stok buku: {data.get('buku_id')}")


# Setup & penggunaan
events = EventManager()
events.subscribe("buku_dipinjam", logging_handler)
events.subscribe("buku_dipinjam", email_handler)
events.subscribe("buku_dipinjam", stok_handler)
events.subscribe("buku_dikembalikan", logging_handler)
events.subscribe("buku_dikembalikan", stok_handler)

# Trigger event
events.notify("buku_dipinjam", {
    'action': 'PINJAM',
    'detail': "'Clean Code' dipinjam oleh Ahmad",
    'email': 'ahmad@uai.ac.id',
    'buku_id': 42
})
# Output:
# [EVENT] 'buku_dipinjam' fired — 3 subscribers
#   [LOG] PINJAM: 'Clean Code' dipinjam oleh Ahmad
#   [EMAIL] Kirim ke ahmad@uai.ac.id: 'Clean Code' dipinjam oleh Ahmad
#   [STOK] Update stok buku: 42
```

> **Kapan digunakan:** Real-time notifications, event logging, UI updates, stock/inventory tracking.

### 5.6.4 Strategy Pattern

**Masalah:** Algoritma/behavior bisa diganti secara runtime tanpa mengubah kode client.

```
┌────────────────────────────────────────────────────────┐
│                STRATEGY PATTERN                        │
│                                                        │
│  Context                    Strategy (interface)       │
│  ┌──────────────┐          ┌──────────────────┐       │
│  │ PaymentProc  │──uses───▶│ PaymentStrategy  │       │
│  │              │          │ + process(amount) │       │
│  │  strategy ───┘          └────────┬─────────┘       │
│  └──────────────┘           ┌───────┼───────┐         │
│                             ▼       ▼       ▼         │
│                       ┌──────┐ ┌──────┐ ┌──────┐      │
│                       │ BCA  │ │GoPay │ │ QRIS │      │
│                       │Trans.│ │      │ │      │      │
│                       └──────┘ └──────┘ └──────┘      │
└────────────────────────────────────────────────────────┘
```

```python
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    """Strategy interface untuk pembayaran."""
    @abstractmethod
    def process(self, amount: float) -> dict: pass

    @abstractmethod
    def get_fee(self, amount: float) -> float: pass


class BCATransfer(PaymentStrategy):
    def process(self, amount):
        fee = self.get_fee(amount)
        total = amount + fee
        return {'method': 'BCA Transfer', 'amount': amount,
                'fee': fee, 'total': total, 'status': 'success'}

    def get_fee(self, amount):
        return 6_500  # Biaya transfer tetap


class GoPay(PaymentStrategy):
    def process(self, amount):
        fee = self.get_fee(amount)
        total = amount + fee
        return {'method': 'GoPay', 'amount': amount,
                'fee': fee, 'total': total, 'status': 'success'}

    def get_fee(self, amount):
        return 0  # Gratis


class QRIS(PaymentStrategy):
    def process(self, amount):
        fee = self.get_fee(amount)
        total = amount + fee
        return {'method': 'QRIS', 'amount': amount,
                'fee': fee, 'total': total, 'status': 'success'}

    def get_fee(self, amount):
        return amount * 0.007  # 0.7% dari transaksi


class PaymentProcessor:
    """Context: memproses pembayaran dengan strategy yang bisa diganti."""

    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        """Ganti strategy saat runtime."""
        self._strategy = strategy

    def checkout(self, amount: float):
        result = self._strategy.process(amount)
        print(f"Pembayaran via {result['method']}:")
        print(f"  Harga:  Rp {result['amount']:>12,.0f}")
        print(f"  Biaya:  Rp {result['fee']:>12,.0f}")
        print(f"  Total:  Rp {result['total']:>12,.0f}")
        print(f"  Status: {result['status']}")
        return result


# Penggunaan — strategi bisa dipilih user saat checkout
processor = PaymentProcessor(GoPay())
processor.checkout(150_000)
# Output:
# Pembayaran via GoPay:
#   Harga:  Rp      150,000
#   Biaya:  Rp            0
#   Total:  Rp      150,000
#   Status: success

# User ganti metode pembayaran
processor.set_strategy(QRIS())
processor.checkout(150_000)
# Output:
# Pembayaran via QRIS:
#   Harga:  Rp      150,000
#   Biaya:  Rp        1,050
#   Total:  Rp      151,050
#   Status: success
```

> **Kapan digunakan:** Multi-payment gateway, sorting algorithms, pricing strategies, format export.

### 5.6.5 Ringkasan Design Patterns

| Pattern | Kategori | Masalah | Contoh Penggunaan Indonesia |
|---------|----------|---------|---------------------------|
| **Singleton** | Creational | Hanya satu instance | Koneksi DB, konfigurasi app |
| **Factory** | Creational | Pembuatan objek tanpa coupling | Multi-channel notifikasi (WA, email, SMS) |
| **Observer** | Behavioral | Notifikasi perubahan state | Event tracking TransJakarta, stok update |
| **Strategy** | Behavioral | Algoritma interchangeable | Multi-payment (BCA, GoPay, OVO, QRIS) |

---

## 5.7 Studi Kasus: Arsitektur Sistem Perpustakaan Digital UAI

### Skenario

Tim proyek 4 mahasiswa diminta merancang Sistem Perpustakaan Digital UAI yang harus:
- Mendukung 500 mahasiswa aktif
- Fitur: pencarian buku, peminjaman, pengembalian, notifikasi, laporan
- Deadline: 10 minggu
- Tech stack: Flask + SQLite + GitHub Codespaces

### Keputusan Arsitektur (ADR)

**ADR-001: Modular Monolith**
- Alasan: Tim kecil (4 orang), deadline ketat, familiar dengan Flask
- Alternatif ditolak: Microservices (terlalu kompleks untuk tim/timeline)

**ADR-002: MVC dengan Repository Pattern**
- Alasan: Separation of concerns yang jelas, mudah di-test

**ADR-003: SQLite untuk development, PostgreSQL untuk production**
- Alasan: SQLite ringan untuk dev, PostgreSQL untuk performa production

### Arsitektur Hasil

```
┌────────────────────────────────────────────────────────────────┐
│            PERPUSTAKAAN DIGITAL UAI — ARSITEKTUR               │
│                                                                │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                   PRESENTATION LAYER                     │  │
│  │  templates/   (Jinja2)     static/   (CSS, JS)          │  │
│  │  API routes   (Flask-RESTful)                            │  │
│  └────────────────────────────┬─────────────────────────────┘  │
│                               │                                │
│  ┌────────────────────────────▼─────────────────────────────┐  │
│  │                   BUSINESS LOGIC LAYER                   │  │
│  │                                                          │  │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐│  │
│  │  │   Auth   │  │   Buku   │  │Peminjaman│  │ Laporan  ││  │
│  │  │ Service  │  │ Service  │  │ Service  │  │ Service  ││  │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────┘│  │
│  │                                                          │  │
│  │  ┌──────────────────────────────────────────────────────┐│  │
│  │  │  Shared: EventManager, NotificationFactory           ││  │
│  │  │         (Observer + Factory patterns)                 ││  │
│  │  └──────────────────────────────────────────────────────┘│  │
│  └────────────────────────────┬─────────────────────────────┘  │
│                               │                                │
│  ┌────────────────────────────▼─────────────────────────────┐  │
│  │                   DATA ACCESS LAYER                      │  │
│  │  UserRepo  │  BukuRepo  │  PeminjamanRepo  │  LaporanRepo│  │
│  └────────────────────────────┬─────────────────────────────┘  │
│                               │                                │
│  ┌────────────────────────────▼─────────────────────────────┐  │
│  │             DATABASE: SQLite / PostgreSQL                 │  │
│  └──────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────┘
```

### Design Patterns yang Digunakan

| Pattern | Penerapan | Alasan |
|---------|-----------|--------|
| Singleton | DatabaseConnection | Satu koneksi shared |
| Factory | NotificationFactory | Multi-channel (email, WA push) |
| Observer | EventManager untuk event peminjaman/pengembalian | Loose coupling antara modul |
| Strategy | Tidak digunakan (belum butuh) | Bisa ditambahkan nanti untuk diskon |
| Repository | Repository per entitas | Abstraksi data access |

---

## AI Corner: AI untuk Arsitektur (Level: Intermediate)

### 5.AI.1 Memilih Arsitektur dengan AI

**Prompt:**
```
Saya mahasiswa semester 4 di Indonesia. Tim saya (4 orang) akan
membangun Sistem Perpustakaan Digital dalam 10 minggu menggunakan
Flask dan SQLite. Fitur: pencarian buku, peminjaman, pengembalian,
notifikasi email. Arsitektur apa yang paling cocok? Jelaskan
alasannya dan berikan struktur folder.
```

**Evaluasi output AI:**
- Cek apakah AI mempertimbangkan ukuran tim dan deadline
- Cek apakah rekomendasi realistis (bukan over-engineering)
- Bandingkan dengan ADR template yang sudah kita pelajari

### 5.AI.2 Review SOLID Violations dengan AI

**Prompt:**
```
Analisis kode Python berikut terhadap prinsip SOLID. Identifikasi
pelanggaran dan berikan refactoring suggestion:

class OrderManager:
    def create_order(self, data):
        # validasi
        if not data['item']:
            raise ValueError("Item kosong")
        # simpan ke MySQL langsung
        import mysql.connector
        conn = mysql.connector.connect(host='localhost', database='shop')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO orders VALUES (%s)", (data,))
        # kirim email
        import smtplib
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.sendmail('shop@gmail.com', data['email'], 'Order created')
        # generate PDF receipt
        from fpdf import FPDF
        pdf = FPDF()
        pdf.output('receipt.pdf')
```

**Evaluasi:** AI seharusnya mengidentifikasi pelanggaran SRP (terlalu banyak tanggung jawab) dan DIP (bergantung langsung pada MySQL, SMTP, FPDF).

### 5.AI.3 Generate Design Pattern Implementation

**Prompt:**
```
Implementasikan Factory Pattern di Python untuk sistem pembayaran
Indonesia: BCA Transfer, GoPay, OVO, QRIS, Dana.
Setiap payment method harus memiliki method process() dan get_fee().
Gunakan ABC sebagai interface. Tambahkan contoh penggunaan.
```

**Evaluasi:** Review apakah AI menerapkan OCP (bisa menambah payment baru tanpa edit Factory).

### 5.AI.4 Membandingkan Architectural Styles

**Prompt:**
```
Bandingkan MVC, Layered Architecture, dan Microservices untuk
konteks startup Indonesia yang baru berdiri (tim 5 orang)
membangun aplikasi delivery makanan. Buat tabel perbandingan
dengan kriteria: complexity, scalability, deployment, cost,
dan rekomendasi.
```

### 5.AI.5 Membuat Architecture Decision Record

**Prompt:**
```
Buatkan ADR (Architecture Decision Record) untuk keputusan berikut:
Tim kami memilih menggunakan Flask Blueprints (Modular Monolith)
untuk Sistem Antrian Puskesmas. Alternatif yang dipertimbangkan:
(1) Pure monolith, (2) Microservices dengan Docker.
Tim: 3 orang, deadline: 8 minggu. Gunakan template ADR standar.
```

### 5.AI.6 Ethical Considerations

- **Jangan blindly copy** arsitektur yang disarankan AI — selalu sesuaikan dengan konteks proyek
- **AI tidak tahu** constraint spesifik tim Anda (skill, waktu, budget)
- **Dokumentasikan** saat AI membantu keputusan arsitektur (AI Usage Log)
- **Validasi** setiap design pattern suggestion — apakah benar-benar dibutuhkan atau over-engineering?

---

## Latihan Soal

### Level Dasar (C1-C2) — 5 Soal

1. **Jelaskan** perbedaan antara MVC, Layered Architecture, dan Microservices. Sebutkan minimal 3 perbedaan utama.

2. **Sebutkan** 5 prinsip SOLID beserta deskripsi singkat masing-masing (satu kalimat per prinsip).

3. **Sebutkan** 4 design patterns GoF yang dipelajari di bab ini (Singleton, Factory, Observer, Strategy) dan jelaskan **kapan** masing-masing digunakan.

4. **Jelaskan** apa itu Conway's Law dan berikan satu contoh penerapannya di perusahaan teknologi Indonesia.

5. **Apa** yang dimaksud dengan Architecture Decision Record (ADR)? Sebutkan 4 komponen utama dalam template ADR.

### Level Menengah (C3-C4) — 7 Soal

6. **Implementasikan** Factory Pattern untuk sistem pembayaran dengan 4 metode: BCA Transfer (fee Rp 6.500), GoPay (fee 0%), OVO (fee 1.5%), dan QRIS (fee 0.7%). Setiap method harus memiliki `process()` dan `get_fee()`.

7. **Analisis** arsitektur aplikasi Tokopedia — menurut Anda, mereka menggunakan monolith atau microservices? Jelaskan 3 alasan berdasarkan quality attributes.

8. **Refactor** kode berikut agar memenuhi prinsip Single Responsibility dan Dependency Inversion:
   ```python
   class ReportGenerator:
       def generate(self, data):
           # validasi data
           # query ke MySQL
           # hitung statistik
           # buat PDF
           # kirim email ke admin
           pass
   ```

9. **Buatlah** ADR untuk proyek tim Anda yang memilih arsitektur tertentu untuk Sistem Antrian Puskesmas. Gunakan template ADR lengkap.

10. **Gambarkan** C4 Model Level 1 (System Context) dan Level 2 (Container) untuk aplikasi e-commerce UMKM.

11. **Bandingkan** event-driven architecture dengan request-response architecture untuk kasus notifikasi real-time. Kapan masing-masing lebih cocok?

12. **Implementasikan** Observer Pattern untuk sistem perpustakaan di mana event "buku_dipinjam" harus memicu: (a) update stok, (b) kirim email ke peminjam, (c) log ke sistem.

### Level Mahir (C5-C6) — 6 Soal

13. **Rancang** arsitektur lengkap (C4 diagram, komponen, API endpoints, design patterns) untuk Sistem Antrian Puskesmas yang harus mendukung 10.000 pengguna bersamaan. Jelaskan quality attributes yang diprioritaskan.

14. **Evaluasi**: kapan Observer Pattern lebih baik daripada polling untuk notifikasi real-time? Berikan analisis trade-off performance, complexity, dan resource usage.

15. **Rancang** evolusi arsitektur untuk startup Indonesia dari fase MVP (3 developer) ke fase scale-up (50 developer). Jelaskan kapan dan mengapa migrasi dari monolith ke microservices dilakukan.

16. **Kritisi** penerapan microservices pada proyek mahasiswa 4 orang dengan deadline 10 minggu. Apakah ini over-engineering? Jelaskan dengan mempertimbangkan Conway's Law.

17. **Desain** sistem notifikasi multi-channel (Email, WA, SMS, Push, Telegram) menggunakan kombinasi Factory Pattern dan Observer Pattern. Gambarkan class diagram dan berikan implementasi Python.

18. **Evaluasi** apakah SOLID principles selalu harus diterapkan 100%? Berikan contoh situasi di mana penerapan SOLID yang terlalu ketat justru counter-productive (YAGNI — You Ain't Gonna Need It).

---

## Rangkuman

1. **Arsitektur software** adalah keputusan desain fundamental yang sulit diubah dan menentukan quality attributes sistem.

2. **Lima architectural styles** utama: MVC (web apps), Layered (enterprise), Microservices (platform besar), Event-Driven (real-time), Pipe-and-Filter (data pipeline).

3. **Quality attributes** (performance, scalability, security, maintainability, availability, testability) selalu melibatkan trade-off — tidak ada arsitektur sempurna.

4. **Conway's Law**: arsitektur software mencerminkan struktur organisasi — contoh: Gojek bermigrasi ke microservices seiring pertumbuhan tim.

5. **ADR (Architecture Decision Record)** mendokumentasikan keputusan arsitektur beserta alasannya — penting untuk knowledge management tim.

6. **C4 Model** memberikan pendekatan hierarkis (Context → Container → Component → Code) untuk visualisasi arsitektur.

7. **SOLID principles** (SRP, OCP, LSP, ISP, DIP) menghasilkan kode yang maintainable, extensible, dan testable.

8. **Design Patterns** (Singleton, Factory, Observer, Strategy) adalah solusi terbukti untuk masalah desain yang berulang — jangan over-engineer, gunakan hanya saat dibutuhkan.

9. **Modular Monolith** (Flask Blueprints) adalah pilihan arsitektur terbaik untuk proyek kuliah — sederhana namun terstruktur.

10. **Keputusan arsitektur** harus mempertimbangkan konteks: ukuran tim, deadline, skill, dan kebutuhan bisnis.

---

## Referensi

1. Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley.
2. Martin, R. C. (2018). *Clean Architecture: A Craftsman's Guide to Software Structure and Design*. Prentice Hall.
3. Bass, L., Clements, P., & Kazman, R. (2021). *Software Architecture in Practice* (4th ed.). Addison-Wesley.
4. Fowler, M. (2002). *Patterns of Enterprise Application Architecture*. Addison-Wesley.
5. Richards, M. & Ford, N. (2020). *Fundamentals of Software Architecture*. O'Reilly.
6. Brown, S. (2018). *The C4 Model for Visualising Software Architecture*. https://c4model.com/
7. Newman, S. (2021). *Building Microservices* (2nd ed.). O'Reilly.
8. Nygard, M. T. (2017). *Architecture Decision Records*. https://adr.github.io/

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
