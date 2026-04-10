# Minggu 5: Arsitektur Perangkat Lunak dan Design Patterns

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak |
| **Kode** | IF2205 |
| **Minggu** | 5 dari 16 |
| **Topik** | Architectural Styles, Quality Attributes, SOLID, Design Patterns |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **CPMK** | CPMK-3 |
| **Sub-CPMK** | 3.1 (Arsitektur & quality attributes), 3.2 (SOLID & design patterns) |
| **Durasi** | 150 menit (3 × 50 menit) |
| **Metode** | Ceramah, analisis arsitektur real-world apps, live coding |

## Tujuan Pembelajaran

1. **Menganalisis** arsitektur perangkat lunak (MVC, layered, microservices) berdasarkan quality attributes (C4)
2. **Menerapkan** prinsip SOLID dalam desain software (C3)
3. **Mengimplementasikan** design patterns (Singleton, Factory, Observer, Strategy) di Python (C3)

## Materi Pembelajaran

### 5.1 Architectural Styles

#### MVC (Model-View-Controller)
```
┌──────────┐    ┌──────────────┐    ┌──────────┐
│   View   │◀───│  Controller  │───▶│  Model   │
│ (HTML/JS)│    │  (Flask route)│    │  (Data)  │
└──────────┘    └──────────────┘    └──────────┘
```
Flask secara natural mengikuti pola ini.

#### Layered Architecture
```
┌─────────────────────────┐
│   Presentation Layer    │  ← HTML, CSS, JavaScript
├─────────────────────────┤
│   Business Logic Layer  │  ← Flask routes, services
├─────────────────────────┤
│   Data Access Layer     │  ← SQLAlchemy, queries
├─────────────────────────┤
│   Database Layer        │  ← SQLite, PostgreSQL
└─────────────────────────┘
```

#### Microservices vs Monolith

| Aspek | Monolith | Microservices | Modular Monolith |
|-------|----------|---------------|------------------|
| Deployment | Satu unit | Independen per service | Satu unit, modular |
| Complexity | Rendah awal | Tinggi (networking) | Sedang |
| Scalability | Vertikal | Horizontal per service | Vertikal + modular |
| Cocok untuk | Startup, MVP | Perusahaan besar | Proyek growing |

### 5.2 SOLID Principles

| Prinsip | Deskripsi | Contoh |
|---------|-----------|--------|
| **S**ingle Responsibility | Satu class = satu tanggung jawab | `UserService` hanya mengelola user |
| **O**pen/Closed | Terbuka untuk ekstensi, tertutup untuk modifikasi | Gunakan inheritance/interface |
| **L**iskov Substitution | Subclass bisa menggantikan parent | `Square` harus bisa menggantikan `Rectangle` |
| **I**nterface Segregation | Interface spesifik, jangan terlalu besar | Pecah `WorkerInterface` jadi `Workable` + `Eatable` |
| **D**ependency Inversion | Bergantung pada abstraksi, bukan implementasi | Inject `DatabaseInterface`, bukan `MySQLDatabase` |

### 5.3 Design Patterns

#### Singleton Pattern (Python)
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

#### Factory Pattern (Python)
```python
class NotificationFactory:
    @staticmethod
    def create(channel):
        if channel == "email":
            return EmailNotification()
        elif channel == "sms":
            return SMSNotification()
        elif channel == "whatsapp":
            return WhatsAppNotification()

# Penggunaan
notif = NotificationFactory.create("whatsapp")
notif.send("Antrian Anda sudah dipanggil")
```

## Kegiatan Pembelajaran

### Pre-class (15 menit)
- Membaca tentang MVC architecture di Flask documentation

### In-class (120 menit)

| Waktu | Aktivitas | Metode |
|-------|-----------|--------|
| 0-30 menit | Architectural Styles: MVC, Layered, Microservices | Ceramah |
| 30-50 menit | SOLID Principles dengan contoh Python | Ceramah + live coding |
| 50-80 menit | Design Patterns: Singleton, Factory, Observer, Strategy | Live coding |
| 80-110 menit | Analisis arsitektur: "Bagaimana Tokopedia diarsitekturkan?" | Diskusi + studi kasus |
| 110-120 menit | Q&A dan preview minggu depan | Diskusi |

### Post-class (15 menit)
- Refleksi: Arsitektur apa yang cocok untuk proyek akhir Anda?

## Referensi

1. Gamma, E. et al. (1994). *Design Patterns*. Addison-Wesley.
2. Martin, R. C. (2018). *Clean Architecture*. Prentice Hall.
3. Fowler, M. (2002). *Patterns of Enterprise Application Architecture*. Addison-Wesley.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
