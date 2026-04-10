# BAB 5: ARSITEKTUR PERANGKAT LUNAK

**Oleh: Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi | Level Bloom |
|-----------|-----------|-------------|
| 3.1 | Menganalisis architectural styles (MVC, layered, microservices) berdasarkan quality attributes | C4 (Menganalisis) |
| 3.2 | Menerapkan prinsip SOLID dan design patterns dalam desain software | C3 (Menerapkan) |

---

## 5.1 Apa Itu Arsitektur Perangkat Lunak?

> **Software architecture** adalah struktur fundamental dari sistem software — komponen-komponen, relasi antar komponen, dan prinsip-prinsip yang mengatur desain dan evolusinya (Bass et al., 2021).

Arsitektur adalah keputusan desain paling fundamental — yang **sulit diubah** setelah implementasi dimulai.

### 5.1.1 Mengapa Arsitektur Penting?

- Menentukan **quality attributes** (performance, scalability, maintainability)
- Menjadi **blueprint** komunikasi antar stakeholder
- Mempengaruhi **struktur tim** (Conway's Law)
- Menentukan **technical debt** jangka panjang

## 5.2 Architectural Styles

### 5.2.1 MVC (Model-View-Controller)

```
┌──────────┐    ┌──────────────┐    ┌──────────┐
│   View   │◀───│  Controller  │───▶│  Model   │
│ (HTML/JS)│    │ (Flask route) │    │  (Data)  │
└──────────┘    └──────────────┘    └──────────┘
     │                                    │
     └────── User sees ←── Data ──────────┘
```

**Komponen:**
- **Model** — data dan business logic (SQLAlchemy models)
- **View** — tampilan ke pengguna (HTML templates, JSON response)
- **Controller** — menghubungkan Model dan View (Flask routes)

**Contoh Flask MVC:**
```python
# Model (models.py)
class Buku(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String(200))

# Controller (routes.py)
@app.route('/buku')
def daftar_buku():
    buku_list = Buku.query.all()
    return render_template('buku.html', buku=buku_list)

# View (templates/buku.html)
# {% for b in buku %}
#   <p>{{ b.judul }}</p>
# {% endfor %}
```

### 5.2.2 Layered Architecture

```
┌─────────────────────────┐
│   Presentation Layer    │  ← HTML, CSS, JavaScript
├─────────────────────────┤
│   Business Logic Layer  │  ← Flask routes, services
├─────────────────────────┤
│   Data Access Layer     │  ← SQLAlchemy, repositories
├─────────────────────────┤
│   Database Layer        │  ← SQLite, PostgreSQL
└─────────────────────────┘
```

**Aturan:** Setiap layer hanya boleh mengakses layer di bawahnya (tidak boleh loncat).

### 5.2.3 Microservices vs Monolith

| Aspek | Monolith | Microservices | Modular Monolith |
|-------|----------|---------------|------------------|
| Deployment | Satu unit | Independen per service | Satu unit, modular internal |
| Complexity | Rendah awal, tinggi di scale | Tinggi (networking, distributed) | Sedang |
| Scalability | Vertikal | Horizontal per service | Vertikal + modular |
| Data | Satu database | Database per service | Satu DB, schema terpisah |
| Tim | Satu tim besar | Tim per service | Tim per modul |
| Cocok untuk | Startup, MVP, proyek kuliah | Perusahaan besar, high-scale | Proyek growing |

**Rekomendasi untuk proyek kuliah:** Mulai dengan **Modular Monolith** menggunakan Flask Blueprints.

```python
# Modular Monolith dengan Flask Blueprints
from flask import Blueprint

# Modul Auth
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['POST'])
def login():
    # ... login logic
    pass

# Modul Buku
buku_bp = Blueprint('buku', __name__, url_prefix='/buku')

@buku_bp.route('/')
def daftar_buku():
    # ... list buku
    pass

# app.py
app.register_blueprint(auth_bp)
app.register_blueprint(buku_bp)
```

## 5.3 Quality Attributes

| Quality Attribute | Deskripsi | Metrik | Trade-off |
|-------------------|-----------|--------|-----------|
| **Performance** | Seberapa cepat respons | Response time, throughput | vs Maintainability |
| **Scalability** | Kemampuan handle beban naik | Users/detik, data growth | vs Simplicity |
| **Security** | Perlindungan dari ancaman | Vulnerabilities, compliance | vs Usability |
| **Maintainability** | Kemudahan diubah | Cyclomatic complexity, coupling | vs Performance |
| **Availability** | Uptime sistem | 99.9% = 8.76 jam downtime/tahun | vs Cost |
| **Testability** | Kemudahan di-test | Code coverage, test time | vs Development speed |

## 5.4 SOLID Principles

| Prinsip | Deskripsi | Pelanggaran | Solusi |
|---------|-----------|-------------|--------|
| **S**ingle Responsibility | Satu class = satu tanggung jawab | `UserService` yang handle auth + email + logging | Pecah: `AuthService`, `EmailService`, `Logger` |
| **O**pen/Closed | Terbuka untuk ekstensi, tertutup untuk modifikasi | Menambah `if-elif` setiap ada tipe baru | Gunakan inheritance/abstract class |
| **L**iskov Substitution | Subclass bisa menggantikan parent tanpa error | `Square` yang melanggar kontrak `Rectangle` | Desain ulang hierarki |
| **I**nterface Segregation | Interface spesifik, jangan terlalu besar | `IWorker` dengan `work()`, `eat()`, `sleep()` | Pecah: `IWorkable`, `IEatable` |
| **D**ependency Inversion | Bergantung pada abstraksi, bukan implementasi | `OrderService` langsung panggil `MySQLDatabase` | Inject `DatabaseInterface` |

### 5.4.1 Contoh Dependency Inversion di Python

```python
# BURUK: bergantung langsung pada implementasi
class OrderService:
    def __init__(self):
        self.db = MySQLDatabase()  # tight coupling
    
    def save_order(self, order):
        self.db.insert("orders", order)

# BAIK: bergantung pada abstraksi
from abc import ABC, abstractmethod

class DatabaseInterface(ABC):
    @abstractmethod
    def insert(self, table, data): pass

class MySQLDatabase(DatabaseInterface):
    def insert(self, table, data):
        # MySQL implementation
        pass

class SQLiteDatabase(DatabaseInterface):
    def insert(self, table, data):
        # SQLite implementation
        pass

class OrderService:
    def __init__(self, db: DatabaseInterface):
        self.db = db  # dependency injection
    
    def save_order(self, order):
        self.db.insert("orders", order)

# Penggunaan
service = OrderService(SQLiteDatabase())  # mudah diganti
```

## 5.5 Design Patterns

### 5.5.1 Singleton Pattern
```python
class DatabaseConnection:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = "Connected to SQLite"
        return cls._instance

# Penggunaan
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)  # True — hanya satu instance
```

### 5.5.2 Factory Pattern
```python
from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message): pass

class EmailNotification(Notification):
    def send(self, message):
        print(f"[EMAIL] {message}")

class WhatsAppNotification(Notification):
    def send(self, message):
        print(f"[WA] {message}")

class NotificationFactory:
    @staticmethod
    def create(channel):
        factories = {
            "email": EmailNotification,
            "whatsapp": WhatsAppNotification,
        }
        return factories[channel]()

# Penggunaan
notif = NotificationFactory.create("whatsapp")
notif.send("Antrian Anda sudah dipanggil")
```

### 5.5.3 Observer Pattern
```python
class EventManager:
    def __init__(self):
        self._subscribers = {}
    
    def subscribe(self, event, callback):
        self._subscribers.setdefault(event, []).append(callback)
    
    def notify(self, event, data):
        for callback in self._subscribers.get(event, []):
            callback(data)

# Penggunaan
manager = EventManager()
manager.subscribe("buku_dipinjam", lambda d: print(f"Log: {d}"))
manager.subscribe("buku_dipinjam", lambda d: print(f"Email: {d}"))
manager.notify("buku_dipinjam", "Buku 'Clean Code' dipinjam oleh Ahmad")
```

### 5.5.4 Strategy Pattern
```python
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data): pass

class QuickSort(SortStrategy):
    def sort(self, data):
        return sorted(data)  # simplified

class BubbleSort(SortStrategy):
    def sort(self, data):
        # bubble sort implementation
        return sorted(data)

class Sorter:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy
    
    def execute(self, data):
        return self.strategy.sort(data)

# Runtime strategy switch
sorter = Sorter(QuickSort())
result = sorter.execute([3, 1, 4, 1, 5])
```

---

## AI Corner: AI untuk Arsitektur (Level: Intermediate)

| Aktivitas | Prompt Contoh | Catatan |
|-----------|---------------|---------|
| Pilih arsitektur | "Untuk tim 4 mahasiswa membangun Sistem Perpustakaan, apakah lebih cocok monolith atau microservices?" | Bandingkan jawaban AI dengan konteks proyek |
| Review SOLID | "Analisis kode Python ini apakah melanggar prinsip SOLID: [paste code]" | AI bagus mendeteksi pelanggaran SOLID |
| Suggest patterns | "Design pattern apa yang cocok untuk fitur notifikasi multi-channel?" | Verifikasi apakah pattern cocok untuk skala proyek |

---

## Latihan Soal

### Level Dasar (C1-C2)
1. Jelaskan perbedaan antara MVC, Layered Architecture, dan Microservices.
2. Sebutkan 5 prinsip SOLID beserta deskripsi singkat masing-masing.
3. Sebutkan 4 design patterns dan jelaskan kapan masing-masing digunakan.

### Level Menengah (C3-C4)
4. Implementasikan Factory Pattern untuk sistem pembayaran (BCA Transfer, GoPay, OVO, QRIS).
5. Analisis arsitektur aplikasi Tokopedia — menurut Anda, mereka menggunakan monolith atau microservices? Jelaskan alasannya.
6. Refactor kode berikut agar memenuhi prinsip Single Responsibility dan Dependency Inversion.

### Level Mahir (C5-C6)
7. Rancang arsitektur lengkap (arsitektur diagram, komponen, API) untuk Sistem Antrian Puskesmas yang harus mendukung 10.000 pengguna bersamaan.
8. Evaluasi: kapan Observer Pattern lebih baik daripada polling untuk notifikasi real-time?

---

## Rangkuman

1. **Arsitektur software** adalah keputusan desain fundamental yang sulit diubah dan menentukan quality attributes.
2. **MVC** memisahkan Model, View, Controller — cocok untuk web apps dengan Flask.
3. **Layered Architecture** mengisolasi concerns per layer — aturan: akses hanya ke layer di bawah.
4. **Monolith → Modular Monolith → Microservices** — pilih sesuai skala dan kompleksitas.
5. **SOLID principles** (SRP, OCP, LSP, ISP, DIP) menghasilkan kode yang maintainable dan extensible.
6. **Design Patterns** (Singleton, Factory, Observer, Strategy) adalah solusi terbukti untuk masalah desain yang umum.

---

## Referensi

1. Gamma, E. et al. (1994). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley.
2. Martin, R. C. (2018). *Clean Architecture*. Prentice Hall.
3. Bass, L. et al. (2021). *Software Architecture in Practice* (4th ed.). Addison-Wesley.
4. Fowler, M. (2002). *Patterns of Enterprise Application Architecture*. Addison-Wesley.
5. Richards, M. & Ford, N. (2020). *Fundamentals of Software Architecture*. O'Reilly.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
