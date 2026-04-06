# Lab 05: Arsitektur dan Design Patterns Implementation

## Informasi Lab

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak (IF2205) |
| **Lab** | 5 dari 13 |
| **Topik** | MVC Flask, Singleton, Factory, Observer, Strategy |
| **CPMK** | CPMK-3 |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |

## Tujuan

1. **Mengimplementasikan** pola MVC menggunakan Flask Blueprints
2. **Mengimplementasikan** 4 design patterns: Singleton, Factory, Observer, Strategy
3. **Menerapkan** prinsip SOLID dalam kode Python

## Langkah-langkah

### Langkah 1: MVC dengan Flask Blueprints (25 menit)
```python
# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    from app.routes.buku import buku_bp
    app.register_blueprint(buku_bp)
    return app

# app/routes/buku.py (Controller)
from flask import Blueprint, jsonify
buku_bp = Blueprint('buku', __name__, url_prefix='/api/buku')

@buku_bp.route('/')
def get_all():
    return jsonify(BukuService().get_all())

# app/models/buku.py (Model)
class Buku:
    def __init__(self, judul, penulis, stok=0):
        self.judul = judul
        self.penulis = penulis
        self.stok = stok
```

### Langkah 2: Singleton Pattern (15 menit)
```python
class DatabaseConnection:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = "Connected"
        return cls._instance

# Test
db1 = DatabaseConnection()
db2 = DatabaseConnection()
assert db1 is db2  # True
```

### Langkah 3: Factory Pattern (15 menit)
```python
from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, msg): pass

class EmailNotif(Notification):
    def send(self, msg): print(f"[EMAIL] {msg}")

class WANotif(Notification):
    def send(self, msg): print(f"[WA] {msg}")

class NotifFactory:
    @staticmethod
    def create(channel):
        return {"email": EmailNotif, "wa": WANotif}[channel]()

notif = NotifFactory.create("wa")
notif.send("Buku sudah tersedia")
```

### Langkah 4: Observer Pattern (15 menit)
```python
class EventManager:
    def __init__(self):
        self._subs = {}
    def subscribe(self, event, fn):
        self._subs.setdefault(event, []).append(fn)
    def notify(self, event, data):
        for fn in self._subs.get(event, []):
            fn(data)

mgr = EventManager()
mgr.subscribe("pinjam", lambda d: print(f"Log: {d}"))
mgr.subscribe("pinjam", lambda d: print(f"Email: {d}"))
mgr.notify("pinjam", "Buku 'Clean Code' dipinjam")
```

### Langkah 5: Strategy Pattern (15 menit)
```python
class SearchStrategy(ABC):
    @abstractmethod
    def search(self, data, query): pass

class TitleSearch(SearchStrategy):
    def search(self, data, query):
        return [b for b in data if query.lower() in b['judul'].lower()]

class AuthorSearch(SearchStrategy):
    def search(self, data, query):
        return [b for b in data if query.lower() in b['penulis'].lower()]

class SearchEngine:
    def __init__(self, strategy: SearchStrategy):
        self.strategy = strategy
    def execute(self, data, query):
        return self.strategy.search(data, query)
```

## Tantangan Tambahan

1. Implementasikan Strategy pattern untuk sorting (by judul, by penulis, by stok)
2. Refactor kode yang melanggar SRP menjadi multiple classes

## Checklist Penyelesaian

- [ ] Flask app menggunakan Blueprints (MVC)
- [ ] Singleton pattern berjalan (test: db1 is db2)
- [ ] Factory pattern untuk 3 tipe notifikasi
- [ ] Observer pattern dengan 2+ subscribers
- [ ] Strategy pattern untuk pencarian
- [ ] Semua kode di-commit

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
