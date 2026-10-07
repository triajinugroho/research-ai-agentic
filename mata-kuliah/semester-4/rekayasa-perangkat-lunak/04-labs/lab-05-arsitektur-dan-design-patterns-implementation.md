# Lab 05: Arsitektur dan Design Patterns Implementation

## Informasi Lab

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak (IF2205) |
| **Lab** | 5 dari 13 |
| **Topik** | MVC Architecture (Flask), Design Patterns (Factory, Observer), ADR Writing |
| **CPMK** | CPMK-3 (Menganalisis dan merancang arsitektur menggunakan architectural patterns, design patterns, UML, dan prinsip SOLID) |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |
| **Prasyarat** | Lab 01-04 selesai, memahami konsep arsitektur dan design patterns dari modul Minggu 5 |

---

## Tujuan

Setelah menyelesaikan lab ini, mahasiswa mampu:

1. **Menganalisis** (C4) pola arsitektur MVC dan menjelaskan tanggung jawab setiap layer
2. **Mengimplementasikan** (C3) 2 design patterns (Factory dan Observer) dalam Python untuk skenario nyata
3. **Mengevaluasi** (C5) kapan dan mengapa suatu design pattern tepat digunakan
4. **Menyusun** (C6) Architecture Decision Record (ADR) untuk mendokumentasikan keputusan desain

---

## Konsep Singkat

### Mengapa Arsitektur Penting?

Arsitektur perangkat lunak adalah **keputusan desain tingkat tinggi** yang menentukan struktur sistem, komponen utama, dan hubungan antar komponen. Keputusan arsitektur sulit diubah nanti -- ibarat fondasi gedung, jika salah sejak awal, biaya perbaikan sangat mahal.

```
Analogi Arsitektur:

  Arsitektur Rumah                    Arsitektur Software
  ┌─────────────────┐                ┌─────────────────┐
  │ Berapa lantai?  │                │ Monolith atau   │
  │ Berapa kamar?   │   ◄────────►  │ Microservices?  │
  │ Dimana dapur?   │                │ MVC atau Clean? │
  │ Fondasi beton?  │                │ SQL atau NoSQL? │
  └─────────────────┘                └─────────────────┘
  
  Sulit diubah setelah dibangun!     Sulit diubah setelah deployed!
```

### Pola MVC (Model-View-Controller)

MVC memisahkan aplikasi menjadi 3 komponen dengan tanggung jawab berbeda:

```
MVC Architecture Flow:

  ┌──────────┐    Request    ┌────────────┐    Query     ┌─────────┐
  │          │ ──────────── │            │ ──────────── │         │
  │   VIEW   │              │ CONTROLLER │              │  MODEL  │
  │          │ ◄──────────  │            │ ◄──────────  │         │
  │ (HTML/   │   Response   │ (Routes/   │    Data      │ (Data/  │
  │  JSON)   │              │  Logic)    │              │  DB)    │
  └──────────┘              └────────────┘              └─────────┘
  
  Tampilan ke       Menerima request,       Mengelola data,
  pengguna          proses logika,          interaksi database
                    kirim response
```

| Komponen | Tanggung Jawab | Contoh di Flask |
|----------|----------------|----------------|
| **Model** | Data dan business logic | Class Python, SQLAlchemy models |
| **View** | Presentasi data ke user | Template HTML, JSON response |
| **Controller** | Menerima request, koordinasi M dan V | Route functions, Blueprints |

### Design Patterns

Design patterns adalah **solusi yang telah terbukti** untuk masalah desain yang sering muncul. Bukan kode yang di-copy-paste, tetapi template konseptual.

| Pattern | Masalah yang Diselesaikan | Analogi Indonesia |
|---------|--------------------------|-------------------|
| **Factory** | Membuat objek tanpa mengekspos logika pembuatan | Warung nasi: pesan "nasi goreng" tanpa tahu resepnya |
| **Observer** | Objek lain perlu diberitahu saat terjadi perubahan | Grup WhatsApp: kirim 1 pesan, semua anggota ternotifikasi |
| **Singleton** | Memastikan hanya ada 1 instance dari suatu class | Presiden RI: hanya ada 1, semua mengacu ke orang yang sama |
| **Strategy** | Memilih algoritma yang berbeda secara runtime | Ojek online: pilih rute terdekat, tercepat, atau termurah |

### Architecture Decision Record (ADR)

ADR adalah dokumen singkat yang mencatat **mengapa** suatu keputusan arsitektur diambil. Ini penting agar anggota tim (sekarang dan masa depan) memahami konteks keputusan.

```
Format ADR:
  Title:    ADR-001: Menggunakan MVC dengan Flask Blueprints
  Status:   Accepted
  Context:  [Mengapa keputusan ini perlu diambil?]
  Decision: [Apa yang diputuskan?]
  Consequences: [Apa dampak positif dan negatif?]
```

> **Referensi:** Materi lengkap tersedia di modul Minggu 5 (`week-05`) dan Bab 5 Buku Ajar.

---

## Persiapan

| Kebutuhan | Detail |
|-----------|--------|
| Repository | Repository GitHub dari Lab 01-04 |
| Codespace | Aktif dengan Python dan Flask terinstall |
| Flask | Versi 3.x (`pip install flask`) |
| Pengetahuan | OOP dasar Python (class, inheritance, abstract) |

---

## Langkah-langkah

### Langkah 1: Analisis Arsitektur MVC di Flask (15 menit)

**Mengapa:** Sebelum mengimplementasikan, mahasiswa harus memahami MENGAPA MVC digunakan. MVC adalah pattern paling umum untuk web application dan dipilih karena memisahkan concerns sehingga tim bisa bekerja paralel (frontend dan backend).

**Instruksi:**

1. Diskusikan dalam tim: struktur folder MVC untuk proyek perpustakaan.

```
Struktur Folder MVC Flask:

  rpl-proyek/
  ├── app/
  │   ├── __init__.py          # Application factory
  │   ├── models/              # MODEL layer
  │   │   ├── __init__.py
  │   │   ├── user.py          # Data class User
  │   │   └── buku.py          # Data class Buku
  │   ├── routes/              # CONTROLLER layer
  │   │   ├── __init__.py
  │   │   ├── auth.py          # Route: login, register
  │   │   └── buku.py          # Route: CRUD buku
  │   ├── services/            # Business logic layer
  │   │   ├── __init__.py
  │   │   ├── auth_service.py  # Logika autentikasi
  │   │   └── buku_service.py  # Logika bisnis buku
  │   └── templates/           # VIEW layer
  │       ├── base.html
  │       ├── login.html
  │       └── buku_list.html
  ├── app.py                   # Entry point
  ├── requirements.txt
  └── docs/
```

2. Buat struktur folder:

```bash
mkdir -p app/models app/routes app/services app/templates
touch app/__init__.py app/models/__init__.py app/routes/__init__.py app/services/__init__.py
```

3. Implementasi Application Factory (`app/__init__.py`):

```python
# app/__init__.py - Application Factory Pattern
from flask import Flask

def create_app():
    """Membuat dan mengkonfigurasi aplikasi Flask."""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'rpl-secret-key-2026'
    
    # Register Blueprints (Controllers)
    from app.routes.buku import buku_bp
    app.register_blueprint(buku_bp)
    
    return app
```

4. Diskusikan: mengapa Application Factory pattern digunakan? Apa bedanya dengan membuat `app = Flask(__name__)` langsung di file utama?

**Expected Output:** Struktur folder MVC terbuat, application factory terimplementasi.

**Estimasi waktu:** 15 menit

> **Diskusi kelas:** Jika seorang developer frontend ingin mengubah tampilan halaman pencarian, file mana saja yang perlu diubah di struktur MVC ini? Bandingkan jika semua kode ada di satu file besar.

---

### Langkah 2: Implementasi Model Layer (15 menit)

**Mengapa:** Model layer bertanggung jawab atas data dan business logic. Memisahkan model dari controller memastikan logika bisnis bisa di-test secara independen tanpa perlu menjalankan web server.

**Instruksi:**

Buat model untuk data buku (`app/models/buku.py`):

```python
# app/models/buku.py - Model layer: representasi data Buku

class Buku:
    """Representasi data buku di perpustakaan.
    
    Attributes:
        id: Identifier unik buku
        judul: Judul buku
        penulis: Nama penulis
        isbn: International Standard Book Number
        stok: Jumlah eksemplar tersedia
        kategori: Kategori/genre buku
    """
    
    def __init__(self, id, judul, penulis, isbn="", stok=0, kategori="Umum"):
        self.id = id
        self.judul = judul
        self.penulis = penulis
        self.isbn = isbn
        self.stok = stok
        self.kategori = kategori
    
    def is_available(self):
        """Cek apakah buku tersedia untuk dipinjam."""
        return self.stok > 0
    
    def pinjam(self):
        """Kurangi stok saat buku dipinjam.
        
        Returns:
            bool: True jika berhasil, False jika stok habis
        """
        if self.stok > 0:
            self.stok -= 1
            return True
        return False
    
    def kembalikan(self):
        """Tambah stok saat buku dikembalikan."""
        self.stok += 1
    
    def to_dict(self):
        """Konversi ke dictionary untuk JSON response."""
        return {
            "id": self.id,
            "judul": self.judul,
            "penulis": self.penulis,
            "isbn": self.isbn,
            "stok": self.stok,
            "kategori": self.kategori,
            "tersedia": self.is_available()
        }


# Data dummy untuk simulasi (menggantikan database)
BUKU_DATA = [
    Buku(1, "Algoritma dan Pemrograman", "Rinaldi Munir", "978-602-1234-01", 5, "Informatika"),
    Buku(2, "Rekayasa Perangkat Lunak", "Ian Sommerville", "978-013-235-088", 3, "Informatika"),
    Buku(3, "Clean Code", "Robert C. Martin", "978-013-235-088", 2, "Software Engineering"),
    Buku(4, "Design Patterns", "Gang of Four", "978-020-163-361", 1, "Software Engineering"),
    Buku(5, "Statistika Dasar", "Sudjana", "978-602-1234-05", 4, "Matematika"),
]
```

Buat service layer (`app/services/buku_service.py`):

```python
# app/services/buku_service.py - Business logic untuk buku

from app.models.buku import BUKU_DATA

class BukuService:
    """Service layer untuk operasi bisnis terkait buku."""
    
    def get_all(self):
        """Ambil semua buku."""
        return [b.to_dict() for b in BUKU_DATA]
    
    def get_by_id(self, buku_id):
        """Ambil buku berdasarkan ID."""
        for buku in BUKU_DATA:
            if buku.id == buku_id:
                return buku.to_dict()
        return None
    
    def search(self, keyword):
        """Cari buku berdasarkan judul atau penulis."""
        keyword = keyword.lower()
        results = [
            b.to_dict() for b in BUKU_DATA
            if keyword in b.judul.lower() or keyword in b.penulis.lower()
        ]
        return results
    
    def pinjam(self, buku_id):
        """Proses peminjaman buku."""
        for buku in BUKU_DATA:
            if buku.id == buku_id:
                if buku.pinjam():
                    return {"status": "berhasil", "buku": buku.to_dict()}
                return {"status": "gagal", "pesan": "Stok habis"}
        return {"status": "gagal", "pesan": "Buku tidak ditemukan"}
```

**Expected Output:** Model `Buku` dan `BukuService` siap digunakan oleh controller.

---

### Langkah 3: Implementasi Controller Layer dan Test (15 menit)

**Mengapa:** Controller menerima HTTP request dari user, memanggil service/model yang sesuai, dan mengembalikan response. Dengan Blueprint, setiap grup fitur bisa dikembangkan secara independen oleh developer berbeda.

**Instruksi:**

Buat controller (`app/routes/buku.py`):

```python
# app/routes/buku.py - Controller layer menggunakan Flask Blueprint

from flask import Blueprint, jsonify, request
from app.services.buku_service import BukuService

buku_bp = Blueprint('buku', __name__, url_prefix='/api/buku')
service = BukuService()

@buku_bp.route('/')
def get_all():
    """GET /api/buku - Daftar semua buku."""
    return jsonify({"data": service.get_all()})

@buku_bp.route('/<int:buku_id>')
def get_by_id(buku_id):
    """GET /api/buku/:id - Detail buku berdasarkan ID."""
    buku = service.get_by_id(buku_id)
    if buku:
        return jsonify({"data": buku})
    return jsonify({"error": "Buku tidak ditemukan"}), 404

@buku_bp.route('/search')
def search():
    """GET /api/buku/search?q=keyword - Pencarian buku."""
    keyword = request.args.get('q', '')
    if not keyword:
        return jsonify({"error": "Parameter 'q' diperlukan"}), 400
    results = service.search(keyword)
    return jsonify({"data": results, "total": len(results)})

@buku_bp.route('/<int:buku_id>/pinjam', methods=['POST'])
def pinjam(buku_id):
    """POST /api/buku/:id/pinjam - Pinjam buku."""
    result = service.pinjam(buku_id)
    if result["status"] == "berhasil":
        return jsonify(result), 200
    return jsonify(result), 400
```

Update entry point (`app.py`):

```python
# app.py - Entry point aplikasi
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

Jalankan dan test:

```bash
flask run --host=0.0.0.0 --port=5000

# Test di terminal baru:
# curl http://localhost:5000/api/buku/
# curl http://localhost:5000/api/buku/1
# curl http://localhost:5000/api/buku/search?q=algoritma
# curl -X POST http://localhost:5000/api/buku/1/pinjam
```

**Expected Output:**

```json
// GET /api/buku/search?q=algoritma
{
  "data": [
    {
      "id": 1,
      "judul": "Algoritma dan Pemrograman",
      "penulis": "Rinaldi Munir",
      "stok": 5,
      "tersedia": true
    }
  ],
  "total": 1
}
```

Commit:

```bash
git add app/
git commit -m "feat: implementasi arsitektur MVC dengan Flask Blueprints"
git push origin main
```

**Estimasi waktu:** 15 menit

> **Troubleshooting:** Jika error `ModuleNotFoundError: No module named 'app'`, pastikan `__init__.py` ada di folder `app/` dan sub-foldernya. Jalankan dari root project directory.

---

### Langkah 4: Implementasi Factory Pattern (15 menit)

**Mengapa:** Factory Pattern digunakan ketika kita perlu membuat objek dari beberapa tipe berbeda tanpa mengekspos logika pembuatan ke client code. Ini sangat berguna saat tipe objek ditentukan secara dinamis (misalnya dari konfigurasi atau input user).

**Instruksi:**

Skenario: Sistem perpustakaan mengirim notifikasi melalui berbagai channel (email, WhatsApp, SMS). Kita tidak ingin client code tahu detail pembuatan setiap tipe notifikasi.

Buat file `app/services/notification.py`:

```python
# app/services/notification.py - Factory Pattern untuk notifikasi

from abc import ABC, abstractmethod
from datetime import datetime

# === Abstract Product ===
class Notification(ABC):
    """Interface untuk semua tipe notifikasi."""
    
    @abstractmethod
    def send(self, recipient, message):
        """Kirim notifikasi ke penerima."""
        pass
    
    @abstractmethod
    def get_channel_name(self):
        """Nama channel notifikasi."""
        pass


# === Concrete Products ===
class EmailNotification(Notification):
    """Notifikasi via email."""
    
    def send(self, recipient, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        print(f"[EMAIL] [{timestamp}] Ke: {recipient}")
        print(f"  Pesan: {message}")
        return {"channel": "email", "status": "sent", "recipient": recipient}
    
    def get_channel_name(self):
        return "Email"


class WhatsAppNotification(Notification):
    """Notifikasi via WhatsApp."""
    
    def send(self, recipient, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        print(f"[WHATSAPP] [{timestamp}] Ke: {recipient}")
        print(f"  Pesan: {message}")
        return {"channel": "whatsapp", "status": "sent", "recipient": recipient}
    
    def get_channel_name(self):
        return "WhatsApp"


class SMSNotification(Notification):
    """Notifikasi via SMS."""
    
    def send(self, recipient, message):
        # SMS memiliki batas 160 karakter
        truncated = message[:160] if len(message) > 160 else message
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        print(f"[SMS] [{timestamp}] Ke: {recipient}")
        print(f"  Pesan: {truncated}")
        return {"channel": "sms", "status": "sent", "recipient": recipient}
    
    def get_channel_name(self):
        return "SMS"


# === Factory ===
class NotificationFactory:
    """Factory untuk membuat objek Notification berdasarkan channel.
    
    Penggunaan Factory Pattern di sini memungkinkan:
    1. Menambah channel baru tanpa mengubah client code
    2. Client tidak perlu tahu class mana yang di-instantiate
    3. Logika pembuatan terpusat di satu tempat
    """
    
    _channels = {
        "email": EmailNotification,
        "whatsapp": WhatsAppNotification,
        "wa": WhatsAppNotification,       # alias
        "sms": SMSNotification,
    }
    
    @classmethod
    def create(cls, channel):
        """Buat notifikasi berdasarkan nama channel.
        
        Args:
            channel: Nama channel ("email", "whatsapp", "wa", "sms")
        
        Returns:
            Instance Notification sesuai channel
        
        Raises:
            ValueError: Jika channel tidak dikenali
        """
        channel = channel.lower()
        if channel not in cls._channels:
            available = ", ".join(cls._channels.keys())
            raise ValueError(
                f"Channel '{channel}' tidak tersedia. "
                f"Pilihan: {available}"
            )
        return cls._channels[channel]()
    
    @classmethod
    def register(cls, name, notification_class):
        """Daftarkan channel notifikasi baru (Open-Closed Principle)."""
        cls._channels[name.lower()] = notification_class


# === Demo penggunaan ===
if __name__ == "__main__":
    print("=== Demo Factory Pattern ===\n")
    
    # Client code tidak perlu tahu class mana yang dibuat
    channels = ["email", "whatsapp", "sms"]
    
    for ch in channels:
        notif = NotificationFactory.create(ch)
        result = notif.send(
            "andi@uai.ac.id",
            "Buku 'Clean Code' harus dikembalikan besok!"
        )
        print(f"  Result: {result}\n")
    
    # Demonstrasi error handling
    print("--- Test channel tidak valid ---")
    try:
        NotificationFactory.create("telegram")
    except ValueError as e:
        print(f"  Error: {e}")
```

Jalankan demo:

```bash
python -m app.services.notification
```

**Expected Output:**

```
=== Demo Factory Pattern ===

[EMAIL] [2026-04-11 10:00] Ke: andi@uai.ac.id
  Pesan: Buku 'Clean Code' harus dikembalikan besok!
  Result: {'channel': 'email', 'status': 'sent', 'recipient': 'andi@uai.ac.id'}

[WHATSAPP] [2026-04-11 10:00] Ke: andi@uai.ac.id
  Pesan: Buku 'Clean Code' harus dikembalikan besok!
  Result: {'channel': 'whatsapp', 'status': 'sent', 'recipient': 'andi@uai.ac.id'}

[SMS] [2026-04-11 10:00] Ke: andi@uai.ac.id
  Pesan: Buku 'Clean Code' harus dikembalikan besok!
  Result: {'channel': 'sms', 'status': 'sent', 'recipient': 'andi@uai.ac.id'}

--- Test channel tidak valid ---
  Error: Channel 'telegram' tidak tersedia. Pilihan: email, whatsapp, wa, sms
```

**Estimasi waktu:** 15 menit

> **Diskusi kelas:** Mengapa kita tidak langsung `if channel == "email": ... elif channel == "whatsapp": ...`? Apa keuntungan Factory Pattern dibanding if-else chain? Hint: Open-Closed Principle.

---

### Langkah 5: Implementasi Observer Pattern (15 menit)

**Mengapa:** Observer Pattern digunakan ketika satu event perlu memicu beberapa aksi yang tidak saling terkait. Contoh: saat buku dipinjam, sistem perlu (1) update stok, (2) kirim email, (3) catat log. Tanpa Observer, semua logika ini tercampur di satu fungsi.

**Instruksi:**

Buat file `app/services/event_manager.py`:

```python
# app/services/event_manager.py - Observer Pattern untuk event handling

from datetime import datetime


class EventManager:
    """Observer Pattern: mengelola event dan subscriber.
    
    Analogi: Seperti grup WhatsApp
    - subscribe() = join grup
    - unsubscribe() = leave grup
    - notify() = kirim pesan ke semua anggota
    """
    
    def __init__(self):
        self._subscribers = {}  # {"event_name": [callback1, callback2, ...]}
    
    def subscribe(self, event_name, callback):
        """Daftarkan callback untuk event tertentu.
        
        Args:
            event_name: Nama event (contoh: "buku.dipinjam")
            callback: Fungsi yang dipanggil saat event terjadi
        """
        if event_name not in self._subscribers:
            self._subscribers[event_name] = []
        self._subscribers[event_name].append(callback)
        print(f"  [EventManager] Subscriber terdaftar untuk '{event_name}'")
    
    def unsubscribe(self, event_name, callback):
        """Hapus callback dari event tertentu."""
        if event_name in self._subscribers:
            self._subscribers[event_name].remove(callback)
    
    def notify(self, event_name, data):
        """Kirim notifikasi ke semua subscriber event.
        
        Args:
            event_name: Nama event yang terjadi
            data: Data yang dikirim ke subscriber
        """
        if event_name not in self._subscribers:
            return
        
        print(f"\n  [EventManager] Event '{event_name}' triggered!")
        print(f"  [EventManager] Notifying {len(self._subscribers[event_name])} subscribers...\n")
        
        for callback in self._subscribers[event_name]:
            callback(data)


# === Subscriber Functions (Observers) ===

def log_peminjaman(data):
    """Observer 1: Mencatat log peminjaman."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"  [LOG] [{timestamp}] Peminjaman: {data['mahasiswa']} meminjam '{data['buku']}'")


def kirim_email_konfirmasi(data):
    """Observer 2: Mengirim email konfirmasi ke mahasiswa."""
    print(f"  [EMAIL] Konfirmasi dikirim ke {data['mahasiswa']}: "
          f"Anda meminjam '{data['buku']}', deadline: {data['deadline']}")


def update_dashboard(data):
    """Observer 3: Update dashboard statistik real-time."""
    print(f"  [DASHBOARD] Statistik diperbarui: +1 peminjaman hari ini")


def cek_batas_peminjaman(data):
    """Observer 4: Cek apakah mahasiswa melebihi batas pinjam."""
    jumlah_pinjaman = data.get('total_pinjaman', 0)
    if jumlah_pinjaman >= 3:
        print(f"  [WARNING] {data['mahasiswa']} sudah meminjam {jumlah_pinjaman} buku (batas: 3)")
    else:
        print(f"  [INFO] {data['mahasiswa']} masih bisa meminjam {3 - jumlah_pinjaman} buku lagi")


# === Demo penggunaan ===
if __name__ == "__main__":
    print("=== Demo Observer Pattern ===\n")
    
    # Setup event manager
    events = EventManager()
    
    # Register observers (subscribers)
    print("--- Registrasi Subscribers ---")
    events.subscribe("buku.dipinjam", log_peminjaman)
    events.subscribe("buku.dipinjam", kirim_email_konfirmasi)
    events.subscribe("buku.dipinjam", update_dashboard)
    events.subscribe("buku.dipinjam", cek_batas_peminjaman)
    
    # Trigger event: buku dipinjam
    print("\n--- Simulasi: Mahasiswa meminjam buku ---")
    events.notify("buku.dipinjam", {
        "mahasiswa": "Andi (20230001)",
        "buku": "Clean Code",
        "deadline": "2026-04-25",
        "total_pinjaman": 2
    })
    
    # Trigger event kedua
    print("\n--- Simulasi: Mahasiswa lain meminjam buku ---")
    events.notify("buku.dipinjam", {
        "mahasiswa": "Budi (20230002)",
        "buku": "Design Patterns",
        "deadline": "2026-04-25",
        "total_pinjaman": 3
    })
    
    # Event tanpa subscriber (tidak error)
    print("\n--- Simulasi: Event tanpa subscriber ---")
    events.notify("buku.dikembalikan", {"buku": "Clean Code"})
    print("  (Tidak ada output karena belum ada subscriber)")
```

Jalankan demo:

```bash
python -m app.services.event_manager
```

**Expected Output:**

```
=== Demo Observer Pattern ===

--- Registrasi Subscribers ---
  [EventManager] Subscriber terdaftar untuk 'buku.dipinjam'
  [EventManager] Subscriber terdaftar untuk 'buku.dipinjam'
  [EventManager] Subscriber terdaftar untuk 'buku.dipinjam'
  [EventManager] Subscriber terdaftar untuk 'buku.dipinjam'

--- Simulasi: Mahasiswa meminjam buku ---

  [EventManager] Event 'buku.dipinjam' triggered!
  [EventManager] Notifying 4 subscribers...

  [LOG] [2026-04-11 10:05:00] Peminjaman: Andi (20230001) meminjam 'Clean Code'
  [EMAIL] Konfirmasi dikirim ke Andi (20230001): ...
  [DASHBOARD] Statistik diperbarui: +1 peminjaman hari ini
  [INFO] Andi (20230001) masih bisa meminjam 1 buku lagi
```

Commit:

```bash
git add app/services/notification.py app/services/event_manager.py
git commit -m "feat: implementasi Factory dan Observer design patterns"
git push origin main
```

**Estimasi waktu:** 15 menit

> **Diskusi kelas:** Apa yang terjadi jika kita TIDAK menggunakan Observer Pattern? Bayangkan fungsi `pinjam_buku()` harus memanggil `log()`, `kirim_email()`, `update_dashboard()`, dan `cek_batas()` langsung. Bagaimana jika kita ingin menambah observer baru? Prinsip SOLID mana yang dilanggar?

---

### Langkah 6: Tulis Architecture Decision Record (ADR) (10 menit)

**Mengapa:** Keputusan arsitektur yang tidak didokumentasikan akan hilang seiring waktu. Tim baru yang bergabung tidak tahu MENGAPA suatu pattern dipilih. ADR menyelamatkan konteks keputusan ini.

**Instruksi:**

Buat file `docs/adr/ADR-001-mvc-flask-blueprints.md`:

```markdown
# ADR-001: Menggunakan Arsitektur MVC dengan Flask Blueprints

## Status
Accepted

## Tanggal
[Tanggal hari ini]

## Konteks
Tim perlu memilih arsitektur untuk Sistem Perpustakaan Digital UAI.
Proyek ini adalah web application dengan 3 tipe pengguna (mahasiswa,
pustakawan, admin) dan 10+ fitur utama. Tim terdiri dari 3-4 orang
yang akan bekerja secara paralel selama 1 semester.

Opsi yang dipertimbangkan:
1. **Monolithic (semua di 1 file)** - Sederhana tapi sulit kolaborasi
2. **MVC dengan Blueprints** - Terstruktur, modular, bisa paralel
3. **Microservices** - Terlalu kompleks untuk proyek akademik

## Keputusan
Kami memilih **MVC Architecture menggunakan Flask Blueprints** karena:
- Memisahkan concerns (Model, View, Controller) sehingga 3 developer
  bisa bekerja paralel
- Flask Blueprints memungkinkan modularisasi per fitur
- Sesuai dengan skala proyek (tidak over-engineering)
- Tim familiar dengan Python dan Flask

## Konsekuensi

### Positif
- Developer bisa bekerja di routes/ dan models/ secara independen
- Mudah menambah fitur baru (buat Blueprint baru)
- Testing lebih mudah (test model terpisah dari controller)

### Negatif
- Sedikit lebih banyak file dibanding monolithic
- Perlu disiplin menjaga batasan layer (jangan akses DB dari controller)
- Tidak cocok jika nanti perlu scaling per-fitur (butuh microservices)
```

Buat juga `docs/adr/ADR-002-factory-pattern-notifikasi.md` untuk keputusan menggunakan Factory Pattern.

Commit:

```bash
mkdir -p docs/adr
git add docs/adr/
git commit -m "docs: tambah Architecture Decision Records (ADR-001, ADR-002)"
git push origin main
```

**Expected Output:** 2 file ADR tersimpan di repository.

**Estimasi waktu:** 10 menit

---

## Tantangan Tambahan

### Tantangan 1: Dasar
Implementasikan **Strategy Pattern** untuk fitur pencarian buku. Buat 3 strategi: `TitleSearch`, `AuthorSearch`, dan `CategorySearch`. Client code harus bisa memilih strategi secara runtime tanpa mengubah logika pencarian.

### Tantangan 2: Menengah
Integrasikan Factory Pattern dan Observer Pattern ke dalam arsitektur MVC. Saat buku dipinjam (melalui controller), gunakan EventManager untuk trigger notifikasi, dan gunakan NotificationFactory untuk menentukan channel notifikasi berdasarkan preferensi user.

### Tantangan 3: Lanjutan
Analisis arsitektur aplikasi Gojek atau Tokopedia. Identifikasi: (a) Architectural pattern utama yang mereka gunakan (monolith vs microservices), (b) 3 design patterns yang kemungkinan digunakan dan alasannya, (c) Buat ADR untuk keputusan migrasi dari monolith ke microservices dari perspektif CTO Gojek. Tulis analisis di `docs/adr/analisis-arsitektur-gojek.md`.

---

## Refleksi & AI Usage Log

Sebelum meninggalkan lab, isi refleksi berikut di file `docs/refleksi-lab-05.md`:

1. **Apa manfaat utama MVC dibanding menaruh semua kode di satu file?**
2. **Design pattern mana yang paling mudah dipahami? Mana yang paling sulit?**
3. **Kapan Factory Pattern TIDAK tepat digunakan?**
4. **Mengapa menulis ADR penting untuk tim?**

Jika menggunakan AI selama lab, catat di **AI Usage Log**:

| Prompt yang Diberikan | Output AI | Modifikasi yang Dilakukan | Refleksi |
|----------------------|-----------|--------------------------|----------|
| (contoh prompt) | (ringkasan output) | (apa yang diubah) | (apa yang dipelajari) |

---

## Checklist Penyelesaian

- [ ] Struktur folder MVC terbuat (`app/models/`, `app/routes/`, `app/services/`, `app/templates/`)
- [ ] Application Factory (`create_app()`) terimplementasi di `app/__init__.py`
- [ ] Model `Buku` dengan method `pinjam()`, `kembalikan()`, `to_dict()`
- [ ] Controller `buku_bp` dengan 4 endpoint (list, detail, search, pinjam)
- [ ] API berjalan dan bisa di-test via browser/curl
- [ ] Factory Pattern: `NotificationFactory` dengan 3 channel (Email, WhatsApp, SMS)
- [ ] Observer Pattern: `EventManager` dengan 4 subscribers untuk event "buku.dipinjam"
- [ ] ADR-001 (MVC) dan ADR-002 (Factory) tersimpan di `docs/adr/`
- [ ] Semua kode di-commit dengan conventional commits
- [ ] File refleksi `docs/refleksi-lab-05.md` terisi

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
