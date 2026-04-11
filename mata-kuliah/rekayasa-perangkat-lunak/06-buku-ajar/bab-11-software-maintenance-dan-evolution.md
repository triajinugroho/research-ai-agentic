# BAB 11: SOFTWARE MAINTENANCE DAN EVOLUTION

**Oleh: Tri Aji Nugroho, S.T., M.T.**
**Mata Kuliah:** IF2205 Rekayasa Perangkat Lunak
**Program Studi Informatika — Universitas Al Azhar Indonesia**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi | Level Bloom | Estimasi Waktu |
|-----------|-----------|-------------|----------------|
| 6.3 | Menganalisis technical debt dan menerapkan strategi refactoring yang aman | C4 (Menganalisis) | 75 menit |
| 6.4 | Menerapkan semantic versioning (SemVer) dan dependency management | C3 (Menerapkan) | 75 menit |

**Prasyarat:** Bab 7 (Software Construction), Bab 10 (DevOps & CI/CD)

---

## Peta Konsep Bab 11

```
                    ┌─────────────────────────────┐
                    │   SOFTWARE MAINTENANCE &     │
                    │        EVOLUTION             │
                    └──────────┬──────────────────┘
                               │
          ┌────────────┬───────┴───────┬────────────┬──────────────┐
          ▼            ▼               ▼            ▼              ▼
   ┌────────────┐ ┌──────────┐ ┌───────────┐ ┌──────────┐ ┌────────────┐
   │ 4 Tipe     │ │ Lehman's │ │ Technical │ │ SemVer & │ │ Legacy     │
   │ Maintenance│ │ Laws     │ │ Debt      │ │ Deps     │ │ Systems    │
   └─────┬──────┘ └────┬─────┘ └─────┬─────┘ └────┬─────┘ └─────┬──────┘
         │              │             │             │             │
    ┌────┴────┐    8 Hukum     ┌─────┴─────┐  ┌───┴────┐   ┌────┴────┐
    │Correc-  │    Evolusi     │Metafora   │  │pip/npm │   │Strangler│
    │tive     │    Software    │Keuangan   │  │SBOM    │   │Fig      │
    │Adaptive │                │Quadrant   │  │Lock    │   │Wrap/API │
    │Perfec-  │                │Refactoring│  │files   │   │Rewrite  │
    │tive     │                │Strategies │  └────────┘   └─────────┘
    │Preven-  │                └───────────┘
    │tive     │
    └─────────┘
```

---

## 11.1 Mengapa Maintenance Penting?

### 11.1.1 Fakta Industri tentang Software Maintenance

Software maintenance adalah fase **terpanjang dan termahal** dalam SDLC. Beberapa fakta kunci:

| Fakta | Data | Sumber |
|-------|------|--------|
| Biaya maintenance vs total biaya | 60-80% dari total biaya software lifecycle | Sommerville, 2016 |
| Waktu engineer membaca vs menulis kode | 10:1 rasio membaca vs menulis | Martin, 2009 |
| Umur rata-rata software enterprise | 10-15+ tahun | Gartner |
| Persentase IT budget untuk maintenance | ~75% di organisasi besar | IEEE |
| Biaya perbaikan bug di production | 100x lebih mahal dari fase development | IBM Systems Sciences |

```
┌─────────────────────────────────────────────────────────────────┐
│              Distribusi Biaya Software Lifecycle                 │
│                                                                 │
│  Development (20-40%)        Maintenance (60-80%)               │
│  ├──────────────┤├──────────────────────────────────────────┤   │
│  │ Req │Des│Code│Test│  Corrective │ Adaptive │ Perfective │   │
│  │ 5%  │10%│15% │10% │    ~15%     │   ~20%   │   ~40%     │   │
│  └─────┴───┴────┴────┴─────────────┴──────────┴────────────┘   │
│                                                                 │
│  ★ Preventive maintenance: ~5% (sering diabaikan!)              │
└─────────────────────────────────────────────────────────────────┘
```

### 11.1.2 Contoh Indonesia: SIPKD dan Maintenance Pemerintah

**SIPKD (Sistem Informasi Pengelolaan Keuangan Daerah)** adalah contoh nyata tantangan maintenance software pemerintah Indonesia:

| Aspek | Tantangan SIPKD |
|-------|----------------|
| **Adaptive** | Setiap tahun ada perubahan regulasi keuangan dari Kemendagri — software harus diupdate |
| **Corrective** | Bug pelaporan keuangan harus diperbaiki sebelum deadline audit BPK |
| **Perfective** | Peningkatan performa saat ribuan pemda submit laporan bersamaan |
| **Preventive** | Update keamanan untuk melindungi data keuangan daerah |

> **Pelajaran:** Software pemerintah Indonesia sering menghadapi "maintenance hell" karena development awal tidak mempertimbangkan evolusi regulasi yang konstan.

### 11.1.3 Tantangan Maintenance di Indonesia

```
┌─────────────────────────────────────────────────────┐
│        Top 5 Tantangan Maintenance di Indonesia      │
├─────────────────────────────────────────────────────┤
│ 1. Rotasi developer tinggi (terutama startup)       │
│    → Institutional knowledge hilang                  │
│                                                      │
│ 2. Dokumentasi minim atau tidak diupdate             │
│    → Kode menjadi "mystery box"                      │
│                                                      │
│ 3. Regulasi sering berubah (pajak, keuangan)        │
│    → Adaptive maintenance terus-menerus              │
│                                                      │
│ 4. Legacy systems dengan teknologi usang             │
│    → Perbankan masih pakai COBOL mainframe           │
│                                                      │
│ 5. Budget maintenance tidak proporsional             │
│    → Fokus di development baru, bukan maintain       │
└─────────────────────────────────────────────────────┘
```

---

## 11.2 Empat Tipe Software Maintenance

### 11.2.1 Klasifikasi ISO/IEC 14764

Standar ISO/IEC 14764 mendefinisikan empat tipe maintenance:

| Tipe | Tujuan | Trigger | Persentase | Contoh |
|------|--------|---------|------------|--------|
| **Corrective** | Memperbaiki bug/defect | Bug report, crash | ~20% | Fix crash saat pencarian kosong |
| **Adaptive** | Adaptasi ke lingkungan baru | OS update, regulasi baru | ~25% | Migrasi dari Python 3.10 ke 3.12 |
| **Perfective** | Meningkatkan performa/fitur | User request, feedback | ~50% | Optimasi query lambat, fitur baru |
| **Preventive** | Mencegah masalah masa depan | Proaktif oleh tim | ~5% | Refactoring, update dependencies |

### 11.2.2 Corrective Maintenance — Perbaiki yang Rusak

Corrective maintenance menangani **defect** yang ditemukan setelah deployment.

**Contoh kasus: Bug di sistem e-commerce Tokopedia**

```python
# BUG: Harga diskon dihitung salah saat voucher + promo aktif bersamaan
# BEFORE (buggy):
def calculate_final_price(price, discount_percent, voucher_amount):
    discounted = price - (price * discount_percent / 100)
    final = discounted - voucher_amount
    return final  # Bug: bisa menghasilkan harga negatif!

# AFTER (fixed):
def calculate_final_price(price, discount_percent, voucher_amount):
    """Hitung harga akhir dengan proteksi harga minimum.
    
    Args:
        price: Harga asli produk (Rupiah)
        discount_percent: Persentase diskon (0-100)
        voucher_amount: Nilai voucher (Rupiah)
    
    Returns:
        Harga akhir, minimal Rp 0
    """
    if price < 0 or discount_percent < 0 or voucher_amount < 0:
        raise ValueError("Semua nilai harus non-negatif")
    
    discount_percent = min(discount_percent, 100)  # Cap di 100%
    discounted = price * (1 - discount_percent / 100)
    final = discounted - voucher_amount
    return max(final, 0)  # Harga tidak boleh negatif
```

**Severity levels untuk bug tracking:**

| Level | Nama | Deskripsi | Response Time |
|-------|------|-----------|---------------|
| P0 | Critical | Sistem down, data loss | < 1 jam |
| P1 | High | Fitur utama tidak berfungsi | < 4 jam |
| P2 | Medium | Fitur minor bermasalah | < 1 hari kerja |
| P3 | Low | Kosmetik, typo | Sprint berikutnya |

### 11.2.3 Adaptive Maintenance — Menyesuaikan Lingkungan

Adaptive maintenance diperlukan ketika **lingkungan berubah** tanpa bug di software.

```
┌──────────────────────────────────────────────────────┐
│          Trigger Adaptive Maintenance                 │
├──────────────────────────────────────────────────────┤
│                                                       │
│  ┌─────────────┐  ┌─────────────┐  ┌──────────────┐ │
│  │ OS/Platform  │  │  Regulasi   │  │  Third-party │ │
│  │   Update     │  │   Berubah   │  │  API Change  │ │
│  │             │  │             │  │              │ │
│  │ Windows 11  │  │ UU PDP      │  │ Midtrans API │ │
│  │ Python 3.12 │  │ Regulasi    │  │ Google Maps  │ │
│  │ Node.js 22  │  │ Pajak       │  │ OAuth update │ │
│  └─────────────┘  └─────────────┘  └──────────────┘ │
│                                                       │
└──────────────────────────────────────────────────────┘
```

**Contoh: Adaptasi untuk UU Perlindungan Data Pribadi (UU PDP) Indonesia**

```python
# BEFORE: Data pengguna disimpan tanpa enkripsi
class User(db.Model):
    nama = db.Column(db.String(100))
    nik = db.Column(db.String(16))         # NIK tersimpan plain text!
    email = db.Column(db.String(120))
    phone = db.Column(db.String(15))       # Nomor HP plain text!

# AFTER: Adaptasi untuk UU PDP — enkripsi data pribadi sensitif
from cryptography.fernet import Fernet

class User(db.Model):
    nama = db.Column(db.String(100))
    _nik_encrypted = db.Column(db.LargeBinary)  # NIK terenkripsi
    email = db.Column(db.String(120))
    _phone_encrypted = db.Column(db.LargeBinary)  # Phone terenkripsi
    data_consent = db.Column(db.Boolean, default=False)  # Consent UU PDP
    consent_date = db.Column(db.DateTime)
    
    @property
    def nik(self):
        """Dekripsi NIK saat diakses."""
        cipher = Fernet(current_app.config['ENCRYPTION_KEY'])
        return cipher.decrypt(self._nik_encrypted).decode()
    
    @nik.setter
    def nik(self, value):
        """Enkripsi NIK saat disimpan."""
        cipher = Fernet(current_app.config['ENCRYPTION_KEY'])
        self._nik_encrypted = cipher.encrypt(value.encode())
```

### 11.2.4 Perfective Maintenance — Tingkatkan Kualitas

Perfective maintenance adalah tipe **paling sering dilakukan** (~50%) — mencakup peningkatan performa dan penambahan fitur.

```python
# BEFORE: Query lambat — fetch semua buku lalu filter di Python
def search_books(keyword):
    all_books = Book.query.all()  # Ambil SEMUA buku ke memory!
    results = []
    for book in all_books:
        if keyword.lower() in book.title.lower():
            results.append(book)
    return results  # Lambat untuk 100.000+ buku

# AFTER: Perfective maintenance — query di database level
def search_books(keyword, page=1, per_page=20):
    """Pencarian buku dengan pagination dan database-level filtering.
    
    Performa: O(log n) dengan index vs O(n) sebelumnya.
    """
    return Book.query.filter(
        Book.title.ilike(f'%{keyword}%')
    ).order_by(
        Book.title
    ).paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )
```

### 11.2.5 Preventive Maintenance — Cegah Masalah Masa Depan

Preventive maintenance adalah **investasi** — menghabiskan effort sekarang untuk mencegah masalah yang lebih mahal nanti.

```python
# Contoh preventive maintenance: menambahkan logging dan monitoring

import logging
from functools import wraps
import time

logger = logging.getLogger(__name__)

def monitor_performance(func):
    """Decorator untuk monitoring performa fungsi.
    
    Preventive: mendeteksi degradasi performa sebelum jadi masalah.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        
        if duration > 1.0:  # Threshold: 1 detik
            logger.warning(
                f"SLOW: {func.__name__} took {duration:.2f}s"
            )
        else:
            logger.info(
                f"{func.__name__} completed in {duration:.4f}s"
            )
        return result
    return wrapper

@monitor_performance
def get_dashboard_data(user_id):
    """Ambil data dashboard — dimonitor untuk degradasi performa."""
    # ... business logic ...
    pass
```

> **Tips & Best Practice:** Alokasikan **10-20% waktu sprint** untuk preventive maintenance. Tim yang mengabaikan preventive maintenance akan menghadapi "maintenance avalanche" dalam 6-12 bulan.

---

## 11.3 Lehman's Laws of Software Evolution

### 11.3.1 Delapan Hukum Evolusi Software

Meir Lehman (1974-1996) merumuskan 8 hukum empiris tentang bagaimana software berevolusi:

| # | Hukum | Deskripsi | Implikasi |
|---|-------|-----------|-----------|
| 1 | **Continuing Change** | Software yang digunakan HARUS berubah, atau akan makin tidak berguna | Maintenance bukan opsional |
| 2 | **Increasing Complexity** | Software yang berevolusi makin kompleks kecuali ada upaya mengurangi | Refactoring itu wajib |
| 3 | **Self Regulation** | Proses evolusi software bersifat self-regulating | Metrics bisa memprediksi tren |
| 4 | **Conservation of Organizational Stability** | Rata-rata kecepatan evolusi konstan | Tambah orang != lebih cepat |
| 5 | **Conservation of Familiarity** | Pertumbuhan incremental per release relatif konstan | Jangan release terlalu besar |
| 6 | **Continuing Growth** | Fungsionalitas harus terus bertambah untuk memenuhi kebutuhan user | Perfective maintenance pasti ada |
| 7 | **Declining Quality** | Kualitas menurun kecuali ada upaya maintain | Quality gate harus ada |
| 8 | **Feedback System** | Proses evolusi adalah sistem multi-loop feedback | Retrospective itu penting |

### 11.3.2 Visualisasi Hukum Lehman

```
   Kompleksitas                    Kualitas
       ▲                              ▲
       │        /                     │\
       │       / Tanpa                │ \  Tanpa upaya
       │      /  refactoring          │  \  maintain
       │     /                        │   \
       │    /                         │    \___
       │   /___  Dengan refactoring   │        \___
       │  /    ─────                  │  Dengan QA ────
       │ /                            │
       └──────────────▶ Waktu         └──────────────▶ Waktu
       
       Hukum #2: Increasing           Hukum #7: Declining
       Complexity                      Quality
```

### 11.3.3 Contoh: Lehman's Laws di Gojek

```
┌───────────────────────────────────────────────────────┐
│         Lehman's Laws di Evolusi Gojek App            │
├───────────────────────────────────────────────────────┤
│                                                        │
│ Law 1 (Continuing Change):                             │
│   2010: GoJek = ojek online saja                       │
│   2015: + GoFood, GoPay, GoSend                        │
│   2020: + GoInvestasi, GoPlay, GoBills                 │
│   2025: Super app dengan 20+ layanan                   │
│   → Software HARUS berevolusi atau mati                │
│                                                        │
│ Law 2 (Increasing Complexity):                         │
│   Monolith → Microservices (600+ services)             │
│   → Kompleksitas naik, butuh platform team             │
│                                                        │
│ Law 5 (Conservation of Familiarity):                   │
│   UI redesign bertahap, bukan sekaligus               │
│   → User tetap familiar dengan app                     │
│                                                        │
│ Law 6 (Continuing Growth):                             │
│   Fitur baru tiap bulan untuk kompetisi                │
│   → Grab menambah fitur serupa → Gojek harus respond   │
│                                                        │
└───────────────────────────────────────────────────────┘
```

---

## 11.4 Technical Debt

### 11.4.1 Metafora Keuangan

Ward Cunningham (1992) memperkenalkan metafora **technical debt** — analogi dengan hutang finansial:

```
┌─────────────────────────────────────────────────────────────┐
│               Analogi Technical Debt = Hutang Finansial      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Hutang Finansial          Technical Debt                    │
│  ─────────────────         ──────────────────────           │
│  Pinjam uang             → Ambil shortcut dalam kode        │
│  Pokok hutang            → Effort untuk refactor kode       │
│  Bunga                   → Extra cost maintenance tiap hari │
│  Cicilan                 → Alokasi waktu refactoring        │
│  Gagal bayar (default)   → Kode tidak bisa diubah lagi      │
│  Kebangkrutan            → Rewrite total (sangat mahal)      │
│                                                              │
│  ★ Seperti hutang: sedikit boleh, terlalu banyak = bahaya!  │
└─────────────────────────────────────────────────────────────┘
```

### 11.4.2 Technical Debt Quadrant (Martin Fowler)

```
                    Deliberate (Sengaja)
                         │
              ┌──────────┼──────────┐
              │          │          │
   Prudent    │  "Kita tahu ini    │  Reckless
   (Bijak)    │  shortcut, akan    │  (Ceroboh)
              │  refactor sprint   │
              │  depan"            │  "Kirim aja dulu,
              │                    │   perbaiki nanti
              │                    │   (never)"
   ───────────┼────────────────────┼──────────
              │                    │
              │  "Baru sadar ada   │  "Kita tidak tahu
              │  pattern yang      │   apa itu design
              │  lebih baik"       │   patterns"
              │                    │
              └──────────┼──────────┘
                         │
                 Inadvertent (Tidak Sengaja)
```

| Kuadran | Tipe | Contoh | Strategi |
|---------|------|--------|----------|
| Prudent + Deliberate | **Tactical debt** | "Hardcode config dulu, refactor di Sprint 3" | Jadwalkan pelunasan |
| Reckless + Deliberate | **Dangerous debt** | "Copy-paste aja, nanti pikirir" | Hindari! Atau bayar segera |
| Prudent + Inadvertent | **Learning debt** | "Oh ternyata ada Repository Pattern" | Refactor saat tahu |
| Reckless + Inadvertent | **Ignorance debt** | "Apa itu SOLID?" | Edukasi tim + refactor |

### 11.4.3 Jenis Technical Debt

| Jenis | Deskripsi | Contoh | Deteksi |
|-------|-----------|--------|---------|
| **Code debt** | Kode tidak clean | Fungsi 300 baris, duplikasi | Linter, code review |
| **Architecture debt** | Arsitektur tidak tepat | Monolith yang harusnya microservice | Architecture review |
| **Test debt** | Test tidak memadai | Coverage < 30% | Coverage tool |
| **Documentation debt** | Docs tidak diupdate | README tidak sesuai realita | Manual audit |
| **Infrastructure debt** | Infra ketinggalan | Server OS tidak diupdate | Security scan |
| **Dependency debt** | Dependencies outdated | Library 3 major version tertinggal | `pip list --outdated` |

### 11.4.4 Mengukur Technical Debt

```python
# Tool: radon — mengukur cyclomatic complexity Python
# Install: pip install radon

# Contoh output radon cc (cyclomatic complexity):
"""
$ radon cc app/services/booking_service.py -s

app/services/booking_service.py
    F 15:0 process_booking - C (14)    ← Terlalu kompleks!
    F 45:0 validate_input - A (3)      ← Baik
    F 60:0 calculate_price - B (8)     ← Perlu perhatian
    F 90:0 send_notification - A (2)   ← Baik

Average complexity: B (6.75)
"""
```

```python
# Tool: pylint — deteksi code smells
"""
$ pylint app/

app/models/user.py:45: R0902: Too many instance attributes (12/7)
app/services/order.py:120: C0301: Line too long (156/120)
app/routes/api.py:30: W0612: Unused variable 'temp_data'
app/utils/helpers.py:1: C0114: Missing module docstring

Your code has been rated at 6.23/10
"""
```

```bash
# Tool: pip-audit — cek vulnerability di dependencies
pip install pip-audit
pip-audit

# Contoh output:
# Name        Version  ID                   Fix Versions
# ----------  -------  -------------------  ------------
# flask       2.0.1    PYSEC-2023-62        2.3.2
# werkzeug    2.0.2    GHSA-hrfv-mqp8-q5rw  2.3.3
# Found 2 known vulnerabilities
```

### 11.4.5 Strategi Mengelola Technical Debt

```
┌─────────────────────────────────────────────────────────┐
│          Strategi Pengelolaan Technical Debt             │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  1. IDENTIFIKASI                                         │
│     ├── Code analysis tools (radon, pylint, SonarQube)  │
│     ├── Code review → tandai debt items                  │
│     └── Sprint retrospective → tim report debt           │
│                                                          │
│  2. VISUALISASI                                          │
│     ├── Tech Debt Board (kolom di Kanban)                │
│     ├── Label di GitHub Issues: "tech-debt"              │
│     └── Dashboard metrics (complexity trend)             │
│                                                          │
│  3. PRIORITISASI                                         │
│     ├── Impact × Effort matrix                           │
│     ├── Debt yang block fitur baru → prioritas tinggi    │
│     └── Debt di kode yang jarang diubah → prioritas rendah│
│                                                          │
│  4. ALOKASI WAKTU                                        │
│     ├── "Boy Scout Rule": tinggalkan kode lebih bersih   │
│     ├── 10-20% sprint capacity untuk debt reduction      │
│     └── "Tech Debt Sprint" periodik (setiap 4-6 sprint) │
│                                                          │
│  5. PENCEGAHAN                                           │
│     ├── Code review wajib                                │
│     ├── Automated quality gates (CI/CD)                  │
│     ├── Definition of Done include "no new debt"         │
│     └── Coding standards + linter enforcement            │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## 11.5 Refactoring — Membayar Technical Debt

### 11.5.1 Definisi Refactoring

> **Refactoring** adalah proses mengubah struktur internal kode **tanpa mengubah perilaku eksternalnya** (Martin Fowler, 2018).

**Prasyarat utama refactoring: HARUS PUNYA TESTS!**

```
┌──────────────────────────────────────────────────┐
│        Safe Refactoring Workflow                  │
│                                                   │
│  1. Pastikan tests pass (green) ────────── ✓     │
│  2. Identifikasi code smell ────────────── 👃    │
│  3. Pilih teknik refactoring ───────────── 📋    │
│  4. Lakukan refactoring kecil ──────────── ✏️    │
│  5. Jalankan tests lagi ────────────────── ✓     │
│  6. Commit ─────────────────────────────── 💾    │
│  7. Ulangi dari langkah 2 ─────────────── 🔄    │
│                                                   │
│  ★ Setiap langkah kecil, selalu test!            │
└──────────────────────────────────────────────────┘
```

### 11.5.2 Teknik Refactoring Umum

**1. Extract Function — Pecah fungsi besar**

```python
# BEFORE: Fungsi terlalu panjang (God Function)
def process_order(order_data):
    # Validasi (20 baris)
    if not order_data.get('items'):
        raise ValueError("Order harus punya items")
    if not order_data.get('customer_id'):
        raise ValueError("Customer ID wajib")
    for item in order_data['items']:
        if item['quantity'] <= 0:
            raise ValueError(f"Quantity harus positif: {item}")
    
    # Hitung total (15 baris)
    subtotal = sum(i['price'] * i['quantity'] for i in order_data['items'])
    tax = subtotal * 0.11  # PPN 11%
    shipping = 15000 if subtotal < 100000 else 0
    total = subtotal + tax + shipping
    
    # Simpan ke database (10 baris)
    order = Order(customer_id=order_data['customer_id'], total=total)
    db.session.add(order)
    db.session.commit()
    
    # Kirim notifikasi (10 baris)
    send_email(order_data['customer_id'], f"Order #{order.id} confirmed")
    
    return order

# AFTER: Extract Function — setiap fungsi punya 1 tanggung jawab
def process_order(order_data):
    """Proses order: validasi → hitung → simpan → notifikasi."""
    validate_order(order_data)
    total = calculate_total(order_data['items'])
    order = save_order(order_data['customer_id'], total)
    notify_customer(order)
    return order

def validate_order(order_data):
    """Validasi data order sebelum diproses."""
    if not order_data.get('items'):
        raise ValueError("Order harus punya items")
    if not order_data.get('customer_id'):
        raise ValueError("Customer ID wajib")
    for item in order_data['items']:
        if item['quantity'] <= 0:
            raise ValueError(f"Quantity harus positif: {item}")

def calculate_total(items):
    """Hitung total dengan PPN 11% dan ongkir."""
    subtotal = sum(i['price'] * i['quantity'] for i in items)
    tax = subtotal * 0.11
    shipping = 15000 if subtotal < 100000 else 0
    return subtotal + tax + shipping

def save_order(customer_id, total):
    """Simpan order ke database."""
    order = Order(customer_id=customer_id, total=total)
    db.session.add(order)
    db.session.commit()
    return order

def notify_customer(order):
    """Kirim notifikasi ke customer."""
    send_email(order.customer_id, f"Order #{order.id} confirmed")
```

**2. Replace Magic Numbers with Constants**

```python
# BEFORE: Magic numbers
if total > 100000:
    shipping = 0
tax = subtotal * 0.11

# AFTER: Named constants
FREE_SHIPPING_THRESHOLD = 100_000  # Rupiah
PPN_RATE = 0.11  # 11% PPN Indonesia
BASE_SHIPPING_COST = 15_000  # Rupiah

if total > FREE_SHIPPING_THRESHOLD:
    shipping = 0
tax = subtotal * PPN_RATE
```

**3. Replace Conditional with Polymorphism**

```python
# BEFORE: Complex conditional
def calculate_discount(customer_type, amount):
    if customer_type == 'regular':
        return amount * 0.05
    elif customer_type == 'silver':
        return amount * 0.10
    elif customer_type == 'gold':
        return amount * 0.15
    elif customer_type == 'platinum':
        return amount * 0.20
    else:
        return 0

# AFTER: Strategy pattern (polymorphism)
class DiscountStrategy:
    def calculate(self, amount):
        raise NotImplementedError

class RegularDiscount(DiscountStrategy):
    def calculate(self, amount):
        return amount * 0.05

class SilverDiscount(DiscountStrategy):
    def calculate(self, amount):
        return amount * 0.10

class GoldDiscount(DiscountStrategy):
    def calculate(self, amount):
        return amount * 0.15

class PlatinumDiscount(DiscountStrategy):
    def calculate(self, amount):
        return amount * 0.20

# Usage:
DISCOUNT_STRATEGIES = {
    'regular': RegularDiscount(),
    'silver': SilverDiscount(),
    'gold': GoldDiscount(),
    'platinum': PlatinumDiscount(),
}

def calculate_discount(customer_type, amount):
    strategy = DISCOUNT_STRATEGIES.get(customer_type)
    return strategy.calculate(amount) if strategy else 0
```

### 11.5.3 Katalog Code Smells

| Code Smell | Deskripsi | Refactoring |
|------------|-----------|-------------|
| **Long Method** | Fungsi > 30 baris | Extract Function |
| **Large Class** | Class terlalu banyak tanggung jawab | Extract Class |
| **Duplicate Code** | Kode yang sama di 2+ tempat | Extract Function/Method |
| **Magic Numbers** | Angka tanpa penjelasan | Replace with Named Constants |
| **Feature Envy** | Method lebih banyak akses data class lain | Move Method |
| **Data Clumps** | Parameter yang selalu muncul bersamaan | Extract Class/Dataclass |
| **Long Parameter List** | Fungsi dengan 5+ parameter | Parameter Object |
| **Dead Code** | Kode yang tidak pernah dieksekusi | Remove Dead Code |
| **Comments as Deodorant** | Komentar panjang menjelaskan kode buruk | Refactor kode agar self-explanatory |
| **Shotgun Surgery** | Satu perubahan mempengaruhi banyak file | Move Method, Inline Class |

---

## 11.6 Semantic Versioning (SemVer)

### 11.6.1 Format SemVer 2.0.0

```
     MAJOR . MINOR . PATCH
       │       │       │
       │       │       └── Bug fixes, backward compatible
       │       └────────── Fitur baru, backward compatible
       └────────────────── Breaking changes, NOT backward compatible
```

| Komponen | Kapan Increment | Contoh | Aturan |
|----------|----------------|--------|--------|
| **MAJOR** | Breaking changes (API berubah) | 1.0.0 → 2.0.0 | Reset MINOR & PATCH ke 0 |
| **MINOR** | Fitur baru, backward compatible | 1.0.0 → 1.1.0 | Reset PATCH ke 0 |
| **PATCH** | Bug fix, backward compatible | 1.0.0 → 1.0.1 | Increment saja |

### 11.6.2 Contoh Evolusi Versi

```
Sistem Perpustakaan UAI — Version History
═══════════════════════════════════════════

v0.1.0  (Alpha)    → Fitur peminjaman dasar
v0.2.0  (Alpha)    → Tambah pencarian buku
v0.3.0  (Alpha)    → Tambah manajemen anggota
v1.0.0-rc.1        → Release candidate pertama
v1.0.0  (Release!) → Versi production pertama

v1.0.1             → Fix: crash saat buku tidak ditemukan
v1.0.2             → Fix: pagination salah di halaman katalog
v1.1.0             → Fitur: notifikasi batas peminjaman (email)
v1.2.0             → Fitur: barcode scanner untuk pengembalian
v1.2.1             → Fix: barcode tidak terbaca untuk ISBN lama

v2.0.0             → BREAKING: Redesign API (REST → GraphQL)
                      → endpoint /api/v1/* dihapus
                      → migrasi ke /graphql
```

### 11.6.3 Pre-release dan Build Metadata

```
Format lengkap: MAJOR.MINOR.PATCH-prerelease+build

Contoh:
  1.0.0-alpha.1          → Alpha pertama
  1.0.0-beta.1           → Beta pertama
  1.0.0-beta.2           → Beta kedua (perbaikan)
  1.0.0-rc.1             → Release Candidate pertama
  1.0.0-rc.2             → RC dengan fix terakhir
  1.0.0                  → Release!
  1.0.0+20260415         → Build dengan tanggal
  1.0.0+sha.a1b2c3d      → Build dengan Git SHA

Urutan precedence:
  1.0.0-alpha < 1.0.0-beta < 1.0.0-rc.1 < 1.0.0
```

### 11.6.4 SemVer dalam package.json dan requirements.txt

```json
// package.json (npm) — version range operators
{
  "dependencies": {
    "express": "^4.18.0",     // ^: compatible (>=4.18.0 <5.0.0)
    "lodash": "~4.17.21",     // ~: patch-level (>=4.17.21 <4.18.0)
    "react": "18.2.0",        // exact: hanya versi ini
    "axios": ">=1.0.0 <2.0.0" // range: eksplisit
  }
}
```

```
# requirements.txt (pip) — version specifiers
Flask==3.0.0             # Exact: hanya 3.0.0
Flask>=3.0.0,<4.0.0      # Range: compatible dengan major 3
Flask~=3.0.0              # Compatible release: >=3.0.0, <3.1.0
Flask>=3.0.0              # Minimum: apapun >= 3.0.0 (tidak disarankan!)
```

> **Best Practice:** Gunakan **pinned versions** (`==`) di production, **compatible ranges** (`^` atau `~=`) di library.

---

## 11.7 Dependency Management

### 11.7.1 Ekosistem Package Manager

| Bahasa | Package Manager | Registry | Lock File | Config File |
|--------|----------------|----------|-----------|-------------|
| Python | pip | PyPI | `requirements.txt` | `pyproject.toml` |
| JavaScript | npm | npmjs.com | `package-lock.json` | `package.json` |
| JavaScript | yarn | npmjs.com | `yarn.lock` | `package.json` |
| Rust | cargo | crates.io | `Cargo.lock` | `Cargo.toml` |
| Go | go mod | proxy.golang.org | `go.sum` | `go.mod` |

### 11.7.2 Dependency Tree dan Transitive Dependencies

```
Proyek Anda
├── Flask==3.0.0
│   ├── Werkzeug>=3.0.0         ← Transitive dependency
│   ├── Jinja2>=3.1.2           ← Transitive dependency
│   │   └── MarkupSafe>=2.0    ← Transitive dari transitive!
│   ├── itsdangerous>=2.1.2
│   ├── click>=8.1.3
│   └── blinker>=1.6.2
├── SQLAlchemy==2.0.25
│   ├── typing-extensions>=4.6.0
│   └── greenlet!=0.4.17       ← Dependency dengan exclusion
└── pytest==8.0.0 (dev only)
    ├── iniconfig
    ├── packaging
    └── pluggy>=1.3.0
```

```bash
# Melihat dependency tree di Python
pip install pipdeptree
pipdeptree

# Melihat dependency tree di npm
npm ls --all

# Cek dependencies yang outdated
pip list --outdated
npm outdated
```

### 11.7.3 Lock Files — Kenapa Penting?

```
┌─────────────────────────────────────────────────────────┐
│          MASALAH TANPA LOCK FILE                         │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Developer A (Senin):     Developer B (Rabu):            │
│  pip install Flask>=3.0   pip install Flask>=3.0         │
│  → Install Flask 3.0.0   → Install Flask 3.0.2 (baru!) │
│  → Tests pass ✓          → Tests FAIL ✗                 │
│                                                          │
│  "Tapi di mesin saya berjalan!" (Works on my machine)   │
│                                                          │
├─────────────────────────────────────────────────────────┤
│          SOLUSI: LOCK FILE                               │
│                                                          │
│  requirements.txt:        pip-compile output:            │
│  Flask>=3.0    →          Flask==3.0.0                   │
│  (range)                  Werkzeug==3.0.1                │
│                           Jinja2==3.1.3                  │
│                           (semua versi exact)            │
│                                                          │
│  Semua developer & CI install versi yang PERSIS sama.   │
└─────────────────────────────────────────────────────────┘
```

```bash
# Python: menggunakan pip-tools untuk lock file
pip install pip-tools

# 1. Tulis requirements.in (versi range)
echo "Flask>=3.0.0" > requirements.in
echo "SQLAlchemy>=2.0.0" >> requirements.in

# 2. Compile ke requirements.txt (versi exact + semua transitive)
pip-compile requirements.in --output-file=requirements.txt

# 3. Install dari lock file
pip install -r requirements.txt

# 4. Update dependencies
pip-compile --upgrade requirements.in
```

```bash
# npm: lock file otomatis
npm install              # Buat/update package-lock.json
npm ci                   # Install PERSIS dari lock file (untuk CI)
npm audit                # Cek vulnerability
npm audit fix            # Auto-fix vulnerability
```

### 11.7.4 SBOM (Software Bill of Materials)

**SBOM** adalah daftar lengkap semua komponen (dependencies) dalam software — seperti "daftar bahan" pada produk makanan.

```
┌─────────────────────────────────────────────────┐
│        SBOM — Software Bill of Materials         │
├─────────────────────────────────────────────────┤
│                                                  │
│  Analogi: Label komposisi di kemasan makanan     │
│                                                  │
│  Makanan:              Software:                 │
│  ─────────             ─────────                 │
│  Tepung terigu 40%     Flask 3.0.0 (BSD)        │
│  Gula 20%              SQLAlchemy 2.0.25 (MIT)  │
│  Telur 15%             Jinja2 3.1.3 (BSD)       │
│  Mentega 15%           Werkzeug 3.0.1 (BSD)     │
│  Pengawet E211 *       lodash 4.17.21 (MIT) *   │
│                                                  │
│  * = Perlu perhatian khusus (vulnerability)      │
│                                                  │
│  Format standar: SPDX, CycloneDX                 │
│                                                  │
│  Kenapa penting?                                 │
│  - Supply chain security (Log4Shell incident)    │
│  - Compliance (lisensi open source)              │
│  - Vulnerability tracking                        │
│  - Regulasi (US Executive Order 14028)           │
└─────────────────────────────────────────────────┘
```

```bash
# Generate SBOM dengan syft
# Install: https://github.com/anchore/syft
syft . -o cyclonedx-json > sbom.json

# Scan SBOM untuk vulnerabilities dengan grype
grype sbom:sbom.json
```

---

## 11.8 Software Metrics

### 11.8.1 Kategori Metrics

| Kategori | Metrik | Deskripsi | Tool | Target |
|----------|--------|-----------|------|--------|
| **Size** | LOC (Lines of Code) | Jumlah baris kode | cloc | Konteks-dependent |
| **Size** | Function Points | Ukuran fungsionalitas | Manual | Konteks-dependent |
| **Complexity** | Cyclomatic Complexity | Jumlah path independen | radon | <= 10 per fungsi |
| **Complexity** | Cognitive Complexity | Seberapa sulit dipahami manusia | SonarQube | <= 15 |
| **Quality** | Code Coverage | % kode yang di-test | pytest-cov | >= 80% |
| **Quality** | Defect Density | Bug per KLOC | Issue tracker | < 5 |
| **Coupling** | Afferent Coupling (Ca) | Modul lain yang bergantung pada modul ini | pydeps | Rendah |
| **Coupling** | Efferent Coupling (Ce) | Modul yang digunakan oleh modul ini | pydeps | Rendah |
| **Cohesion** | LCOM | Lack of Cohesion of Methods | Manual | Rendah (= cohesion tinggi) |
| **Churn** | Code Churn | Frekuensi perubahan file | git log | Perhatikan "hot spots" |

### 11.8.2 Mengukur Metrics dengan Python Tools

```bash
# 1. Lines of Code — menggunakan cloc
pip install cloc  # atau install dari package manager OS
cloc app/ --exclude-dir=__pycache__,migrations

# Contoh output:
# ──────────────────────────────────────
# Language      files   blank  comment   code
# ──────────────────────────────────────
# Python           15     120      85     650
# HTML              8      30      10     420
# JavaScript        5      25      15     280
# CSS               3      10       5     150
# ──────────────────────────────────────
# SUM              31     185     115    1500

# 2. Cyclomatic Complexity — menggunakan radon
pip install radon
radon cc app/ -a -s -n C  # Tampilkan hanya yang >= C (complex)

# 3. Maintainability Index
radon mi app/ -s
# A (20+): sangat maintainable
# B (10-19): moderate
# C (0-9): perlu perbaikan

# 4. Code coverage
pip install pytest pytest-cov
pytest --cov=app --cov-report=html
# Buka htmlcov/index.html di browser
```

### 11.8.3 Code Churn Analysis

**Code churn** = seberapa sering file diubah. File dengan churn tinggi + complexity tinggi = **hot spot** yang perlu prioritas refactoring.

```bash
# Git: file yang paling sering diubah (top 10)
git log --format=format: --name-only --since="6 months ago" \
  | sort | uniq -c | sort -rn | head -10

# Contoh output:
#  45 app/services/order_service.py      ← HOT SPOT!
#  38 app/routes/api.py                  ← HOT SPOT!
#  25 app/models/user.py
#  20 tests/test_order.py
#  18 app/templates/dashboard.html
```

```
┌─────────────────────────────────────────────────┐
│        Hot Spot Analysis Matrix                  │
│                                                  │
│  Complexity                                      │
│      High  │ Refactor soon │ CRITICAL -         │
│            │               │ Refactor NOW!       │
│      ──────┼───────────────┼─────────────────   │
│      Low   │ Leave alone   │ Simplify or         │
│            │               │ split file          │
│            └───────────────┴─────────────────   │
│                Low              High             │
│                        Churn                     │
└─────────────────────────────────────────────────┘
```

---

## 11.9 Legacy System Strategies

### 11.9.1 Apa Itu Legacy System?

Legacy system adalah software yang **masih digunakan** tapi menggunakan **teknologi lama**, sulit di-maintain, dan berisiko tinggi jika diubah.

**Contoh di Indonesia:**

| Sektor | Sistem Legacy | Teknologi | Tantangan |
|--------|--------------|-----------|-----------|
| **Perbankan** | Core banking BCA, Mandiri | COBOL, mainframe | Risiko tinggi jika gagal migrasi |
| **Pemerintah** | SIPKD, SIMPEG | PHP 5, MySQL lama | Tidak ada yang paham kode lama |
| **Telekomunikasi** | Billing system Telkomsel | C/C++, Oracle | Jutaan transaksi/hari |
| **Pendidikan** | Sistem akademik kampus | Visual Basic, Access | Developer sudah tidak ada |

### 11.9.2 Empat Strategi Modernisasi

```
┌─────────────────────────────────────────────────────────────┐
│              Strategi Modernisasi Legacy System               │
├──────────────┬──────────────┬──────────────┬────────────────┤
│   REWRITE    │  REFACTOR    │ STRANGLER    │    WRAP        │
│              │              │    FIG       │                │
│  ┌────────┐  │  ┌────────┐  │ ┌──┬──┬──┐  │  ┌──────────┐ │
│  │ NEW    │  │  │ BETTER │  │ │N │N │O │  │  │ API      │ │
│  │ SYSTEM │  │  │ SAME   │  │ │E │E │L │  │  │ WRAPPER  │ │
│  │        │  │  │ SYSTEM │  │ │W │W │D │  │  │ ┌──────┐ │ │
│  └────────┘  │  └────────┘  │ └──┴──┴──┘  │  │ │LEGACY│ │ │
│              │              │              │  │ └──────┘ │ │
│ Tulis ulang  │ Perbaiki     │ Ganti modul  │  │          │ │
│ dari nol     │ bertahap     │ per modul    │  └──────────┘ │
│              │              │              │  Bungkus dgn  │
│ Risiko:      │ Risiko:      │ Risiko:      │  API baru     │
│ TINGGI       │ RENDAH       │ SEDANG       │  Risiko:      │
│              │              │              │  RENDAH        │
└──────────────┴──────────────┴──────────────┴────────────────┘
```

| Strategi | Kapan Digunakan | Keuntungan | Kerugian |
|----------|----------------|------------|----------|
| **Rewrite** | Sistem kecil, teknologi benar-benar mati | Clean slate | Second system effect, mahal, berisiko |
| **Refactor** | Struktur masih layak, cuma perlu perbaikan | Low risk, incremental | Lambat, tetap bawa legacy baggage |
| **Strangler Fig** | Sistem besar, bisa dipisah per modul | Gradual migration, rollback mudah | Perlu maintain 2 sistem sementara |
| **Wrap/API** | Perlu integrasi cepat tanpa ubah legacy | Cepat, low risk | Legacy tetap ada (hutang ditunda) |

### 11.9.3 Strangler Fig Pattern — Detail

```
Phase 1: Identifikasi modul yang bisa dipisah
┌─────────────────────────────────────────┐
│            LEGACY MONOLITH              │
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐  │
│  │Auth  │ │Order │ │Report│ │Notif │  │
│  └──────┘ └──────┘ └──────┘ └──────┘  │
└─────────────────────────────────────────┘

Phase 2: Bangun modul baru, route traffic
┌───────────────────────────┐
│     API GATEWAY / PROXY   │
│  ┌────────────────────┐   │
│  │ /auth → NEW Auth   │───┼──► ┌──────────┐
│  │ /order → LEGACY    │   │    │ NEW Auth  │
│  │ /report → LEGACY   │   │    │ Service   │
│  │ /notif → LEGACY    │   │    └──────────┘
│  └────────────────────┘   │
└───────────┬───────────────┘
            │
            ▼
┌─────────────────────────────────────────┐
│            LEGACY MONOLITH              │
│           ┌──────┐ ┌──────┐ ┌──────┐   │
│           │Order │ │Report│ │Notif │   │
│           └──────┘ └──────┘ └──────┘   │
└─────────────────────────────────────────┘

Phase 3: Migrasi semua modul
┌───────────────────────────┐
│     API GATEWAY           │
│  ┌────────────────────┐   │    ┌──────────┐
│  │ /auth → NEW Auth   │───┼──► │ NEW Auth │
│  │ /order → NEW Order │───┼──► │ NEW Order│
│  │ /report → NEW Rpt  │───┼──► │ NEW Rpt  │
│  │ /notif → NEW Notif │───┼──► │ NEW Notif│
│  └────────────────────┘   │    └──────────┘
└───────────────────────────┘

Legacy monolith: DIMATIKAN ✓
```

### 11.9.4 Contoh: Modernisasi Sistem Akademik Kampus

```python
# WRAP strategy: Bungkus sistem akademik lama dengan REST API

from flask import Flask, jsonify
import pyodbc  # Koneksi ke database Access/SQL Server lama

app = Flask(__name__)

# Koneksi ke database legacy (Microsoft Access)
LEGACY_CONN_STR = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\legacy\akademik.mdb;'
)

@app.route('/api/v1/mahasiswa/<nim>')
def get_mahasiswa(nim):
    """API wrapper untuk data mahasiswa dari sistem legacy.
    
    Sistem lama: Microsoft Access + Visual Basic
    API baru: REST JSON — bisa diakses oleh frontend modern
    """
    conn = pyodbc.connect(LEGACY_CONN_STR)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT NIM, Nama, Prodi, Angkatan FROM tblMahasiswa WHERE NIM = ?",
        nim
    )
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return jsonify({
            'nim': row.NIM,
            'nama': row.Nama,
            'prodi': row.Prodi,
            'angkatan': row.Angkatan
        })
    return jsonify({'error': 'Mahasiswa tidak ditemukan'}), 404
```

---

## 11.10 Studi Kasus Komprehensif: Modernisasi Sistem Perpustakaan UAI

### Skenario

Sistem Perpustakaan UAI saat ini menggunakan PHP 5.6 + MySQL, dikembangkan tahun 2015. Tim ingin memodernisasi ke Flask + SQLAlchemy + Docker.

### Langkah 1: Audit Technical Debt

```
┌────────────────────────────────────────────────────┐
│          Technical Debt Audit Results               │
├────────────────────────────────────────────────────┤
│                                                     │
│  Code Debt:                                         │
│  - 45 fungsi dengan complexity > 15                 │
│  - 120 kasus duplikasi kode                        │
│  - 0% test coverage                                │
│                                                     │
│  Architecture Debt:                                 │
│  - Monolith tanpa separation of concerns            │
│  - SQL queries di dalam view layer                  │
│  - Hardcoded config (password di source code)       │
│                                                     │
│  Infrastructure Debt:                               │
│  - PHP 5.6 (EOL sejak 2018!)                       │
│  - MySQL 5.5 (EOL sejak 2018!)                     │
│  - Tidak ada CI/CD                                  │
│  - Deployment manual via FTP                        │
│                                                     │
│  Dependency Debt:                                   │
│  - 15 library dengan known vulnerabilities          │
│  - Tidak ada lock file                              │
│                                                     │
│  Keputusan: STRANGLER FIG PATTERN                   │
│  (sistem terlalu besar untuk rewrite, tapi          │
│   teknologi terlalu lama untuk sekadar refactor)    │
└────────────────────────────────────────────────────┘
```

### Langkah 2: Rencana Migrasi (6 bulan)

| Bulan | Modul | Strategi | Deliverable |
|-------|-------|----------|-------------|
| 1-2 | Auth + User Management | Strangler Fig | New Flask auth service + API gateway |
| 2-3 | Katalog Buku | Strangler Fig | New Flask catalog service |
| 3-4 | Peminjaman | Strangler Fig | New Flask lending service |
| 4-5 | Reporting | Wrap + New UI | API wrapper + dashboard baru |
| 5-6 | Integration + Testing | Testing | Full test suite, CI/CD, Docker |

### Langkah 3: Versioning Plan

```
v1.x.x  = Sistem lama (PHP)
v2.0.0-alpha.1 = Auth module migrasi selesai
v2.0.0-beta.1  = Katalog + Peminjaman migrasi selesai
v2.0.0-rc.1    = Semua modul migrasi, testing
v2.0.0         = Full release — sistem lama dimatikan
```

---

## AI Corner: AI untuk Software Maintenance (Level: Advanced)

### AC.1 AI untuk Deteksi Technical Debt

```
Prompt:
"Analisis kode Python berikut dan identifikasi semua technical debt.
Kategorikan setiap temuan sebagai: Code Debt, Architecture Debt, 
Test Debt, atau Documentation Debt. Berikan severity (High/Medium/Low)
dan rekomendasi refactoring untuk setiap temuan.

[paste kode]"
```

**Contoh output AI (harus diverifikasi manusia!):**

```
Temuan Technical Debt:
1. [HIGH] Code Debt: Fungsi process_order() 85 baris
   → Refactoring: Extract Function (split jadi 4 fungsi)

2. [MEDIUM] Architecture Debt: SQL queries di route handler
   → Refactoring: Implement Repository Pattern

3. [HIGH] Test Debt: Tidak ada unit test sama sekali
   → Rekomendasi: Mulai dengan test untuk business logic kritis

4. [LOW] Documentation Debt: Tidak ada docstring di 12 fungsi
   → Rekomendasi: Tambahkan docstring sesuai PEP 257
```

### AC.2 AI untuk Refactoring Assistance

```
Prompt:
"Refactor fungsi Python ini menggunakan teknik Extract Function.
Pastikan:
1. Setiap fungsi baru memiliki satu tanggung jawab (SRP)
2. Nama fungsi deskriptif (bahasa Inggris)
3. Tambahkan type hints dan docstring
4. Hasilnya harus memiliki behavior yang PERSIS sama

[paste fungsi]"
```

### AC.3 AI untuk Legacy Code Understanding

```
Prompt:
"Kode PHP legacy berikut mengelola peminjaman buku perpustakaan.
Jelaskan:
1. Apa yang dilakukan setiap fungsi?
2. Di mana potential bugs?
3. Bagaimana kode ini bisa dimodernisasi ke Python/Flask?
4. Buatkan mapping: PHP function → Python equivalent

[paste kode PHP legacy]"
```

### AC.4 AI untuk Changelog Generation

```
Prompt:
"Berdasarkan git log berikut, buatkan changelog dalam format 
Keep a Changelog (https://keepachangelog.com/). 
Kategorikan: Added, Changed, Deprecated, Removed, Fixed, Security.

[paste git log --oneline dari tag terakhir]"
```

### AC.5 AI untuk Dependency Audit

```
Prompt:
"Berikut adalah daftar dependencies proyek Python kami beserta 
versinya. Analisis:
1. Mana yang sudah outdated? (bandingkan dengan versi terbaru)
2. Apakah ada known vulnerability?
3. Mana yang bisa di-upgrade tanpa breaking changes?
4. Buatkan rencana upgrade bertahap.

[paste pip list output]"
```

### AC.6 Batasan AI untuk Maintenance

| AI Bisa | AI Tidak Bisa |
|---------|--------------|
| Mendeteksi code smells | Memahami konteks bisnis spesifik |
| Suggest refactoring | Memutuskan strategi modernisasi |
| Generate changelog | Memastikan backward compatibility |
| Jelaskan kode legacy | Menilai risiko bisnis migrasi |
| Identifikasi outdated deps | Memahami politik organisasi |

> **Prinsip Amanah:** Selalu verifikasi saran AI sebelum menerapkan refactoring. AI bisa suggest refactoring yang secara teknis benar tapi merusak business logic yang subtle.

---

## Latihan Soal

### Level Dasar (C1-C2) — 5 Soal

1. **Sebutkan** 4 tipe software maintenance menurut ISO/IEC 14764 beserta persentase masing-masing dan berikan satu contoh untuk setiap tipe.

2. **Jelaskan** apa itu technical debt menggunakan metafora keuangan. Apa yang dimaksud dengan "pokok hutang", "bunga", dan "cicilan" dalam konteks software?

3. **Sebutkan** format Semantic Versioning dan jelaskan kapan masing-masing komponen (MAJOR, MINOR, PATCH) di-increment. Berikan contoh untuk setiap kasus.

4. **Jelaskan** 3 dari 8 Lehman's Laws of Software Evolution dan berikan contoh nyata untuk masing-masing.

5. **Apa** perbedaan antara lock file (`requirements.txt` yang di-pin) dan file requirement range (`requirements.in`)? Mengapa lock file penting?

### Level Menengah (C3-C4) — 7 Soal

6. **Analisis** proyek Flask berikut menggunakan radon. Identifikasi fungsi-fungsi dengan cyclomatic complexity tinggi dan buatlah rencana refactoring.

7. **Klasifikasikan** skenario maintenance berikut ke dalam 4 tipe yang tepat:
   - a) Menambahkan fitur dark mode karena permintaan user
   - b) Memperbaiki error 500 saat login dengan password kosong
   - c) Migrasi database dari MySQL 5.7 ke 8.0
   - d) Menambahkan structured logging ke semua API endpoints
   - e) Update kode untuk comply dengan UU PDP

8. **Buatlah** release checklist lengkap untuk Sistem Perpustakaan v2.0.0 yang meliputi: testing, security, documentation, versioning, deployment, dan rollback plan.

9. **Identifikasi** 5 code smells dalam kode berikut dan terapkan refactoring yang tepat:
   ```python
   def process(d, t, u, f):
       if t == 1:
           x = d * 0.11
           if u == "gold":
               x = x * 0.85
           elif u == "silver":
               x = x * 0.9
           if f == True:
               x = x - 15000
       return d + x
   ```

10. **Bandingkan** Strangler Fig Pattern dan Rewrite untuk skenario modernisasi sistem akademik kampus yang menggunakan Visual Basic + Microsoft Access. Pertimbangkan: risiko, biaya, timeline, dan dampak ke pengguna.

11. **Buatlah** SBOM sederhana untuk proyek Flask yang menggunakan: Flask, SQLAlchemy, pytest, flask-login, dan gunicorn. Sertakan versi, lisensi, dan apakah direct/transitive dependency.

12. **Analisis** output berikut dan tentukan prioritas refactoring (gunakan Hot Spot Analysis):
    ```
    File                          Changes  Complexity
    app/services/order.py         45       C (14)
    app/models/user.py            12       A (3)
    app/routes/api.py             38       B (8)
    app/utils/helpers.py          5        D (22)
    app/config.py                 3        A (1)
    ```

### Level Mahir (C5-C6) — 7 Soal

13. **Evaluasi** strategi modernisasi untuk sistem core banking yang masih menggunakan COBOL mainframe. Pertimbangkan: risiko operasional (bank harus tetap beroperasi 24/7), regulasi OJK, migrasi data jutaan nasabah, dan biaya. Rekomendasikan strategi dan buat roadmap 2 tahun.

14. **Rancang** maintenance plan 1 tahun untuk Sistem Antrian Puskesmas yang mencakup semua 4 tipe maintenance. Sertakan: jadwal, resource allocation, risk mitigation, dan metrics untuk mengukur keberhasilan.

15. **Kritisi** pernyataan: "Jika kita tidak punya waktu untuk refactoring, berarti kita tidak punya waktu untuk TIDAK refactoring." Apakah selalu benar? Berikan skenario di mana menambah technical debt adalah keputusan yang rasional.

16. **Rancang** automated quality gate CI/CD pipeline yang mendeteksi dan mencegah technical debt baru. Pipeline harus mencakup: linting, complexity check, coverage threshold, dependency audit, dan SBOM generation.

17. **Evaluasi** penggunaan AI untuk software maintenance. Dalam skenario apa AI sangat membantu? Kapan AI bisa berbahaya? Buatlah policy penggunaan AI untuk maintenance di perusahaan software Indonesia.

18. **Analisis** fenomena "Lehman's Law #4 (Conservation of Organizational Stability)" dalam konteks startup Indonesia. Mengapa menambah developer tidak selalu mempercepat development? Kaitkan dengan Brooks's Law.

19. **Rancang** dependency management strategy untuk organisasi yang mengelola 10+ microservices Python. Sertakan: versioning policy, update cadence, vulnerability response process, dan SBOM compliance.

20. **Sintesis** seluruh konsep bab ini dalam sebuah "Software Health Dashboard" — tentukan 10 metrik kunci yang harus dimonitor, threshold untuk setiap metrik, dan action plan ketika metrik melewati threshold.

---

## Rangkuman

1. **Software maintenance** menghabiskan **60-80%** total biaya software — terdiri dari corrective (20%), adaptive (25%), perfective (50%), dan preventive (5%).

2. **Lehman's Laws** menjelaskan bahwa software HARUS berevolusi (Law 1), akan semakin kompleks tanpa upaya (Law 2), dan kualitasnya menurun tanpa maintenance aktif (Law 7).

3. **Technical debt** adalah metafora untuk shortcut yang diambil selama development — harus dikelola dengan identifikasi, prioritisasi, dan alokasi waktu refactoring (10-20% per sprint).

4. **Refactoring** mengubah struktur internal tanpa mengubah behavior — HARUS didukung oleh test suite. Teknik umum: Extract Function, Replace Magic Numbers, Replace Conditional with Polymorphism.

5. **Semantic Versioning** (MAJOR.MINOR.PATCH) memberikan komunikasi jelas tentang nature perubahan dan backward compatibility.

6. **Dependency management** menggunakan lock files untuk memastikan konsistensi, dan SBOM untuk transparency komponen software.

7. **Software metrics** (LOC, complexity, coverage, churn) membantu mengukur kualitas secara objektif — kombinasikan churn + complexity untuk Hot Spot Analysis.

8. **Legacy system modernization** dapat dilakukan dengan 4 strategi: Rewrite, Refactor, Strangler Fig, atau Wrap — pilih berdasarkan ukuran sistem, risiko, dan sumber daya.

9. **AI tools** dapat membantu mendeteksi technical debt, suggest refactoring, dan menjelaskan kode legacy — tetapi keputusan strategis tetap tanggung jawab engineer.

---

## Referensi

1. Lehman, M. M. (1980). "Programs, Life Cycles, and Laws of Software Evolution." *IEEE Proceedings*, 68(9), 1060-1076.
2. Cunningham, W. (1992). "The WyCash Portfolio Management System." *OOPSLA Experience Report*.
3. Fowler, M. (2018). *Refactoring: Improving the Design of Existing Code* (2nd ed.). Addison-Wesley.
4. Newman, S. (2019). *Monolith to Microservices: Evolutionary Patterns to Transform Your Monolith*. O'Reilly.
5. Sommerville, I. (2016). *Software Engineering* (10th ed.). Chapter 9: Software Evolution. Pearson.
6. semver.org. (2024). *Semantic Versioning 2.0.0*. https://semver.org/
7. NTIA. (2021). *Software Bill of Materials (SBOM)*. https://www.ntia.gov/SBOM
8. Martin, R. C. (2009). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
