# BAB 7: SOFTWARE CONSTRUCTION DAN VERSION CONTROL

**Oleh: Tri Aji Nugroho, S.T., M.T.**
**Mata Kuliah:** IF2205 Rekayasa Perangkat Lunak
**Program Studi Informatika — Universitas Al Azhar Indonesia**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi | Level Bloom | Estimasi Waktu |
|-----------|-----------|-------------|----------------|
| 4.1 | Menerapkan coding standards (PEP 8, ESLint), mengidentifikasi code smells (10+), dan melakukan refactoring | C3 (Menerapkan) | 75 menit |
| 4.2 | Menerapkan Git workflow (branching strategies, PR, code review) untuk kolaborasi tim yang efektif | C3-C4 (Menerapkan-Menganalisis) | 75 menit |

---

## Peta Konsep Bab

```
                    ┌──────────────────────────────────┐
                    │   SOFTWARE CONSTRUCTION           │
                    │   & VERSION CONTROL               │
                    └──────────────┬───────────────────┘
                                   │
           ┌───────────────────────┼───────────────────────┐
           ▼                       ▼                       ▼
  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
  │   CLEAN CODE     │    │  CODE SMELLS &   │    │  VERSION CONTROL │
  │                  │    │  REFACTORING     │    │  (Git)           │
  ├──────────────────┤    ├──────────────────┤    ├──────────────────┤
  │ • 10+ Prinsip    │    │ • 10+ Smells     │    │ • Git Internals  │
  │ • Naming         │    │ • Extract Method │    │ • Branching      │
  │ • Functions      │    │ • Rename Var     │    │   Strategies     │
  │ • Comments       │    │ • Move Method    │    │ • Conventional   │
  │ • PEP 8 / ESLint│    │ • Before/After   │    │   Commits        │
  └────────┬────────┘    └────────┬────────┘    │ • PR Workflow    │
           │                      │              │ • Code Review    │
           └──────────────────────┼──────────────┘
                                  ▼
                    ┌──────────────────────────────┐
                    │  KOLABORASI TIM               │
                    │  PR → Code Review → Merge     │
                    └──────────────────────────────┘
```

---

## 7.1 Clean Code: Prinsip Penulisan Kode Bersih

### 7.1.1 Mengapa Clean Code Penting?

> "Any fool can write code that a computer can understand. Good programmers write code that humans can understand." — Martin Fowler

Dalam rekayasa perangkat lunak, kode dibaca **10x lebih sering** daripada ditulis. Menurut Robert C. Martin (*Clean Code*, 2009), clean code adalah kode yang:
- **Mudah dibaca** — developer lain (atau diri sendiri 6 bulan kemudian) bisa memahami tanpa penjelasan tambahan
- **Mudah diubah** — perubahan tidak menyebabkan bug di tempat lain
- **Mudah ditest** — bisa diuji secara otomatis
- **Minimalis** — tidak ada kode yang tidak perlu

> **Konteks Indonesia:** Di perusahaan tech Indonesia seperti Gojek dan Tokopedia, code review adalah bagian wajib dari workflow. Kode yang tidak "bersih" akan ditolak dalam Pull Request, memperlambat delivery. Di tim startup kecil, technical debt dari kode yang tidak bersih bisa menghambat pertumbuhan ketika tim bertambah dari 3 menjadi 30 orang.

### 7.1.2 Sepuluh Prinsip Clean Code

| No | Prinsip | Deskripsi | Contoh |
|----|---------|-----------|--------|
| 1 | **Meaningful Names** | Nama variabel/fungsi harus menjelaskan tujuan | `d` → `days_until_deadline` |
| 2 | **Functions Do One Thing** | Setiap fungsi hanya punya satu tanggung jawab | Pisahkan `process_order()` menjadi `validate()`, `calculate()`, `save()` |
| 3 | **Small Functions** | Idealnya < 20 baris per fungsi | Jika > 20, pertimbangkan Extract Method |
| 4 | **DRY (Don't Repeat Yourself)** | Jangan duplikasi kode — gunakan abstraksi | Extract common logic ke fungsi/class |
| 5 | **KISS (Keep It Simple, Stupid)** | Solusi sederhana lebih baik daripada yang "pintar" | Hindari over-engineering |
| 6 | **YAGNI (You Ain't Gonna Need It)** | Jangan menulis fitur yang belum dibutuhkan | Jangan buat abstraksi "untuk masa depan" |
| 7 | **Boy Scout Rule** | Tinggalkan kode lebih bersih dari yang Anda temukan | Refactor sedikit setiap kali menyentuh file |
| 8 | **Minimize Comments** | Kode yang baik menjelaskan dirinya sendiri — comment hanya untuk "mengapa" | Ganti comment "// menghitung total" dengan fungsi `calculate_total()` |
| 9 | **Error Handling** | Handle error secara eksplisit, jangan abaikan exception | Gunakan specific exceptions, bukan bare `except` |
| 10 | **Consistent Formatting** | Ikuti coding standard tim secara konsisten | PEP 8, ESLint, Prettier |

### 7.1.3 Prinsip Penamaan (Naming Conventions)

```python
# ============================================
# BURUK vs BAIK: Penamaan variabel
# ============================================

# BURUK — nama tidak bermakna
d = 7
temp = []
data = {}
flag = True
x = calculate(a, b)

# BAIK — nama menjelaskan tujuan
days_until_deadline = 7
active_students = []
student_grades = {}
is_authenticated = True
total_price = calculate_subtotal(items, discount_percentage)

# ============================================
# BURUK vs BAIK: Penamaan fungsi
# ============================================

# BURUK — tidak jelas apa yang dilakukan
def process(data):
    pass

def do_stuff(x, y):
    pass

def handle(item):
    pass

# BAIK — verb + noun yang jelas
def validate_student_registration(registration_data: dict) -> bool:
    pass

def calculate_semester_gpa(courses: list) -> float:
    pass

def send_payment_reminder(student_id: str) -> None:
    pass
```

```python
# ============================================
# Konvensi penamaan Python (PEP 8)
# ============================================

# Variabel dan fungsi: snake_case
total_harga = 150000
jumlah_mahasiswa = 35

def hitung_ipk_semester(daftar_mata_kuliah: list) -> float:
    """Hitung IPK semester berdasarkan daftar mata kuliah."""
    pass

# Class: PascalCase
class MahasiswaInformatika:
    """Representasi mahasiswa program studi Informatika."""

    # Konstanta: UPPER_SNAKE_CASE
    MAX_SKS_PER_SEMESTER = 24
    MIN_IPK_LULUS = 2.0

    def __init__(self, nim: str, nama: str):
        self.nim = nim
        self.nama = nama
        self._ipk = 0.0  # Protected (konvensi underscore prefix)

    @property
    def ipk(self) -> float:
        return self._ipk

# Module: lowercase, short
# student_service.py, grade_calculator.py

# Boolean: prefix is_, has_, can_, should_
is_active = True
has_submitted_assignment = False
can_register_courses = True
```

### 7.1.4 Prinsip Fungsi

```python
# ============================================
# BURUK: Fungsi terlalu panjang, banyak tanggung jawab
# ============================================
def process_order(order_data):
    # Validasi order (20 baris)
    if not order_data.get("items"):
        raise ValueError("Order harus punya items")
    if not order_data.get("customer_id"):
        raise ValueError("Customer ID wajib")
    for item in order_data["items"]:
        if item["qty"] <= 0:
            raise ValueError(f"Qty {item['name']} harus > 0")
        if item["price"] < 0:
            raise ValueError(f"Harga {item['name']} tidak valid")

    # Hitung total (15 baris)
    subtotal = 0
    for item in order_data["items"]:
        subtotal += item["price"] * item["qty"]
    tax = subtotal * 0.11  # PPN 11%
    total = subtotal + tax

    # Proses pembayaran (10 baris)
    payment_result = {"status": "success", "amount": total}

    # Kirim email konfirmasi (10 baris)
    email_body = f"Pesanan Anda total Rp {total:,.0f}"
    print(f"Email terkirim: {email_body}")

    # Update inventory (10 baris)
    for item in order_data["items"]:
        print(f"Stok {item['name']} dikurangi {item['qty']}")

    return payment_result


# ============================================
# BAIK: Setiap fungsi satu tanggung jawab
# ============================================
PPN_RATE = 0.11  # PPN 11% Indonesia

def process_order(order_data: dict) -> dict:
    """Proses order: validasi → hitung → bayar → notify → update stok."""
    validate_order(order_data)
    total = calculate_total_with_tax(order_data["items"])
    payment = process_payment(order_data["customer_id"], total)
    send_confirmation(order_data["customer_id"], total)
    update_inventory(order_data["items"])
    return payment

def validate_order(order_data: dict) -> None:
    """Validasi kelengkapan dan kebenaran data order."""
    if not order_data.get("items"):
        raise ValueError("Order harus punya items")
    if not order_data.get("customer_id"):
        raise ValueError("Customer ID wajib")
    for item in order_data["items"]:
        _validate_item(item)

def _validate_item(item: dict) -> None:
    """Validasi satu item order."""
    if item.get("qty", 0) <= 0:
        raise ValueError(f"Qty {item['name']} harus > 0")
    if item.get("price", 0) < 0:
        raise ValueError(f"Harga {item['name']} tidak valid")

def calculate_total_with_tax(items: list) -> float:
    """Hitung total termasuk PPN 11%."""
    subtotal = sum(item["price"] * item["qty"] for item in items)
    return subtotal * (1 + PPN_RATE)

def process_payment(customer_id: str, amount: float) -> dict:
    """Proses pembayaran melalui payment gateway."""
    return {"status": "success", "customer": customer_id, "amount": amount}

def send_confirmation(customer_id: str, total: float) -> None:
    """Kirim email konfirmasi ke customer."""
    print(f"Email ke {customer_id}: Pesanan Rp {total:,.0f}")

def update_inventory(items: list) -> None:
    """Update stok setelah order berhasil."""
    for item in items:
        print(f"Stok {item['name']} dikurangi {item['qty']}")
```

### 7.1.5 Coding Standards: PEP 8 dan ESLint

**Python — PEP 8 (Style Guide for Python Code):**

| Aturan | Deskripsi | Contoh |
|--------|-----------|--------|
| Indentasi | 4 spasi (BUKAN tab) | `def foo():\n    return 42` |
| Max line length | 79 karakter (atau 120 untuk proyek modern) | Gunakan line continuation `\` atau `()` |
| Blank lines | 2 blank lines sebelum top-level function/class, 1 blank line antar method | — |
| Imports | Satu import per baris, urut: stdlib → third-party → local | `import os` (bukan `import os, sys`) |
| Naming | `snake_case` untuk var/func, `PascalCase` untuk class, `UPPER_CASE` untuk constants | — |
| String quotes | Konsisten — pilih single atau double, tidak campur | `'hello'` ATAU `"hello"` |
| Trailing whitespace | Tidak boleh ada spasi di akhir baris | Gunakan editor yang auto-trim |
| Docstrings | Gunakan triple double-quotes untuk semua public functions/classes | `"""Deskripsi fungsi."""` |

```python
# Contoh file Python yang sesuai PEP 8
"""
Modul untuk mengelola data mahasiswa.

Modul ini menyediakan fungsi-fungsi CRUD untuk data mahasiswa
Program Studi Informatika UAI.
"""

from dataclasses import dataclass
from typing import Optional


MAX_SKS = 24
MIN_IPK_LULUS = 2.0


@dataclass
class Mahasiswa:
    """Representasi data mahasiswa."""

    nim: str
    nama: str
    semester: int
    ipk: float = 0.0

    def is_eligible_for_graduation(self) -> bool:
        """Cek apakah mahasiswa memenuhi syarat lulus."""
        return self.ipk >= MIN_IPK_LULUS and self.semester >= 8

    def get_max_sks(self) -> int:
        """Hitung maksimal SKS yang bisa diambil berdasarkan IPK."""
        if self.ipk >= 3.0:
            return MAX_SKS
        elif self.ipk >= 2.5:
            return 21
        else:
            return 18


def find_student_by_nim(
    students: list[Mahasiswa],
    nim: str,
) -> Optional[Mahasiswa]:
    """Cari mahasiswa berdasarkan NIM.

    Args:
        students: Daftar mahasiswa yang dicari.
        nim: Nomor Induk Mahasiswa yang dicari.

    Returns:
        Objek Mahasiswa jika ditemukan, None jika tidak.
    """
    for student in students:
        if student.nim == nim:
            return student
    return None
```

**JavaScript — ESLint + Prettier:**

```javascript
// .eslintrc.json — Konfigurasi ESLint untuk proyek JS
{
  "env": {
    "browser": true,
    "es2021": true,
    "node": true
  },
  "extends": ["eslint:recommended", "prettier"],
  "rules": {
    "no-unused-vars": "warn",
    "no-console": "warn",
    "prefer-const": "error",
    "no-var": "error",
    "eqeqeq": ["error", "always"],
    "curly": ["error", "all"],
    "camelCase": "warn"
  }
}
```

```javascript
// Contoh kode JavaScript yang mengikuti ESLint rules
/**
 * Menghitung total harga pesanan termasuk PPN.
 * @param {Array<{name: string, price: number, qty: number}>} items
 * @param {number} discountPercent - Persentase diskon (0-100)
 * @returns {number} Total harga setelah diskon dan PPN
 */
const calculateOrderTotal = (items, discountPercent = 0) => {
  const PPN_RATE = 0.11; // PPN 11% Indonesia

  const subtotal = items.reduce(
    (sum, item) => sum + item.price * item.qty,
    0
  );

  const discountAmount = subtotal * (discountPercent / 100);
  const afterDiscount = subtotal - discountAmount;
  const total = afterDiscount * (1 + PPN_RATE);

  return Math.round(total);
};

// Penggunaan
const items = [
  { name: "Nasi Goreng", price: 25000, qty: 2 },
  { name: "Es Teh Manis", price: 5000, qty: 3 },
];

const total = calculateOrderTotal(items, 10);
console.log(`Total: Rp ${total.toLocaleString("id-ID")}`);
// Output: Total: Rp 72,150
```

---

## 7.2 Code Smells: Katalog Bau Kode

### 7.2.1 Apa Itu Code Smell?

**Code smell** (istilah dari Martin Fowler, *Refactoring*, 1999) adalah indikasi di permukaan kode bahwa ada masalah yang lebih dalam di desain. Code smell bukan bug — kode tetap berjalan — tetapi menandakan bahwa kode akan sulit di-maintain di masa depan.

### 7.2.2 Katalog 12 Code Smells dengan Before/After

**Smell 1: Long Method**

```python
# SEBELUM (BURUK) — Fungsi 40+ baris
def generate_student_report(student_id):
    # Ambil data mahasiswa
    student = db.query(f"SELECT * FROM students WHERE id = {student_id}")
    if not student:
        return None

    # Ambil nilai
    grades = db.query(f"SELECT * FROM grades WHERE student_id = {student_id}")

    # Hitung IPK
    total_quality_points = 0
    total_credits = 0
    for grade in grades:
        if grade.letter == "A":
            quality = 4.0
        elif grade.letter == "B+":
            quality = 3.5
        elif grade.letter == "B":
            quality = 3.0
        elif grade.letter == "C+":
            quality = 2.5
        elif grade.letter == "C":
            quality = 2.0
        elif grade.letter == "D":
            quality = 1.0
        else:
            quality = 0.0
        total_quality_points += quality * grade.credits
        total_credits += grade.credits

    ipk = total_quality_points / total_credits if total_credits else 0

    # Generate report
    report = f"=== TRANSKRIP NILAI ===\n"
    report += f"NIM: {student.nim}\n"
    report += f"Nama: {student.nama}\n"
    report += f"IPK: {ipk:.2f}\n"
    # ... (20 baris lagi)

    return report


# SESUDAH (BAIK) — Dipecah menjadi fungsi-fungsi kecil
GRADE_POINTS = {
    "A": 4.0, "B+": 3.5, "B": 3.0, "C+": 2.5,
    "C": 2.0, "D": 1.0, "E": 0.0,
}

def generate_student_report(student_id: str) -> str | None:
    """Generate transkrip nilai mahasiswa."""
    student = fetch_student(student_id)
    if not student:
        return None
    grades = fetch_grades(student_id)
    ipk = calculate_ipk(grades)
    return format_transcript(student, grades, ipk)

def calculate_ipk(grades: list) -> float:
    """Hitung IPK dari daftar nilai."""
    if not grades:
        return 0.0
    total_qp = sum(GRADE_POINTS.get(g.letter, 0) * g.credits for g in grades)
    total_credits = sum(g.credits for g in grades)
    return total_qp / total_credits if total_credits else 0.0
```

**Smell 2: Duplicate Code**

```python
# SEBELUM (BURUK) — Kode duplikat di banyak tempat
def get_active_students():
    students = db.query("SELECT * FROM students")
    result = []
    for s in students:
        if s.status == "active" and s.semester <= 14:
            result.append(s)
    return result

def get_active_students_by_prodi(prodi):
    students = db.query("SELECT * FROM students WHERE prodi = ?", prodi)
    result = []
    for s in students:
        if s.status == "active" and s.semester <= 14:  # Duplikat!
            result.append(s)
    return result


# SESUDAH (BAIK) — Extract common logic
def is_active_student(student) -> bool:
    """Cek apakah mahasiswa aktif (belum DO)."""
    return student.status == "active" and student.semester <= 14

def get_active_students():
    return [s for s in db.query("SELECT * FROM students") if is_active_student(s)]

def get_active_students_by_prodi(prodi):
    students = db.query("SELECT * FROM students WHERE prodi = ?", prodi)
    return [s for s in students if is_active_student(s)]
```

**Smell 3: God Class**

```python
# SEBELUM (BURUK) — Class yang tahu segalanya
class ApplicationManager:
    """Class ini melakukan SEGALANYA."""

    def validate_user(self, user_data): ...
    def authenticate(self, username, password): ...
    def send_email(self, to, subject, body): ...
    def generate_pdf_report(self, data): ...
    def calculate_gpa(self, grades): ...
    def process_payment(self, amount): ...
    def backup_database(self): ...
    def resize_image(self, image, width, height): ...
    # ... 50 method lainnya


# SESUDAH (BAIK) — Split into focused classes
class AuthService:
    def validate_user(self, user_data): ...
    def authenticate(self, username, password): ...

class EmailService:
    def send_email(self, to, subject, body): ...

class ReportService:
    def generate_pdf_report(self, data): ...

class AcademicService:
    def calculate_gpa(self, grades): ...

class PaymentService:
    def process_payment(self, amount): ...
```

**Smell 4: Magic Numbers/Strings**

```python
# SEBELUM (BURUK) — angka dan string "ajaib"
if user.role == 1:             # Apa itu 1?
    if order.total > 500000:   # Kenapa 500000?
        discount = 0.15        # 15% dari mana?
    if user.age >= 17:         # Apa signifikansi 17?
        allow_registration()

# SESUDAH (BAIK) — konstanta yang bermakna
ROLE_ADMIN = 1
ROLE_USER = 2
ROLE_GUEST = 3

MIN_ORDER_FOR_DISCOUNT = 500_000  # Rp 500.000
LOYALTY_DISCOUNT_RATE = 0.15       # 15% diskon loyalitas
MIN_AGE_REGISTRATION = 17         # Minimal 17 tahun (KTP)

if user.role == ROLE_ADMIN:
    if order.total > MIN_ORDER_FOR_DISCOUNT:
        discount = LOYALTY_DISCOUNT_RATE
    if user.age >= MIN_AGE_REGISTRATION:
        allow_registration()
```

**Smell 5: Feature Envy**

```python
# SEBELUM (BURUK) — Method terlalu banyak akses data class lain
class OrderPrinter:
    def print_order_details(self, order):
        print(f"Customer: {order.customer.name}")
        print(f"Email: {order.customer.email}")
        print(f"Phone: {order.customer.phone}")
        print(f"Address: {order.customer.address}")
        # Method ini lebih "tertarik" pada Customer daripada Order!

# SESUDAH (BAIK) — Pindahkan logic ke class yang memiliki data
class Customer:
    def get_contact_info(self) -> str:
        return f"{self.name}\n{self.email}\n{self.phone}\n{self.address}"

class OrderPrinter:
    def print_order_details(self, order):
        print(order.customer.get_contact_info())
```

**Smell 6-12: Ringkasan**

| No | Code Smell | Gejala | Refactoring |
|----|-----------|--------|-------------|
| 6 | **Shotgun Surgery** | Satu perubahan → edit banyak file | Move Method, Inline Class |
| 7 | **Dead Code** | Kode tidak pernah dieksekusi | Delete — jangan takut, ada Git! |
| 8 | **Primitive Obsession** | Menggunakan primitif untuk konsep domain | Extract Class (misal: `Money` bukan `float`) |
| 9 | **Long Parameter List** | Fungsi dengan 4+ parameter | Introduce Parameter Object |
| 10 | **Data Clumps** | Sekelompok data selalu muncul bersama | Extract Class |
| 11 | **Switch Statements** | `if/elif` panjang untuk tipe berbeda | Replace with Polymorphism |
| 12 | **Comments** | Comment untuk menjelaskan kode yang buruk | Refactor kode agar self-documenting |

```python
# Smell 9: Long Parameter List — Before/After
# SEBELUM
def create_student(nim, nama, email, phone, address, prodi, semester, ipk):
    pass

# SESUDAH — gunakan dataclass sebagai Parameter Object
@dataclass
class StudentRegistration:
    nim: str
    nama: str
    email: str
    phone: str
    address: str
    prodi: str
    semester: int = 1
    ipk: float = 0.0

def create_student(registration: StudentRegistration):
    pass
```

---

## 7.3 Teknik Refactoring

### 7.3.1 Apa Itu Refactoring?

> "Refactoring is the process of changing a software system in a way that does not alter the external behavior of the code yet improves its internal structure." — Martin Fowler

**Aturan emas refactoring:**
- Input dan output TIDAK BERUBAH
- Semua test yang pass sebelum refactoring harus tetap pass setelahnya
- Refactoring dilakukan dalam langkah kecil — commit sering

### 7.3.2 Katalog Teknik Refactoring

**Teknik 1: Extract Method**

```python
# SEBELUM
def print_invoice(invoice):
    print("=" * 40)
    print("     INVOICE PENJUALAN")
    print("     Toko Berkah Jaya")
    print("=" * 40)
    print(f"Customer: {invoice.customer.name}")
    print(f"Email   : {invoice.customer.email}")
    print(f"Tanggal : {invoice.date}")
    print("-" * 40)
    total = 0
    for item in invoice.items:
        line_total = item.price * item.qty
        total += line_total
        print(f"  {item.name:<20s} {item.qty:>3d} x Rp {item.price:>10,.0f} = Rp {line_total:>12,.0f}")
    ppn = total * 0.11
    grand_total = total + ppn
    print("-" * 40)
    print(f"  Subtotal: Rp {total:>12,.0f}")
    print(f"  PPN 11% : Rp {ppn:>12,.0f}")
    print(f"  TOTAL   : Rp {grand_total:>12,.0f}")
    print("=" * 40)

# SESUDAH — Extract Method
PPN_RATE = 0.11

def print_invoice(invoice):
    """Cetak invoice penjualan lengkap."""
    print_header()
    print_customer_info(invoice.customer, invoice.date)
    subtotal = print_line_items(invoice.items)
    print_totals(subtotal)

def print_header():
    print("=" * 40)
    print("     INVOICE PENJUALAN")
    print("     Toko Berkah Jaya")
    print("=" * 40)

def print_customer_info(customer, date):
    print(f"Customer: {customer.name}")
    print(f"Email   : {customer.email}")
    print(f"Tanggal : {date}")
    print("-" * 40)

def print_line_items(items) -> float:
    total = 0
    for item in items:
        line_total = item.price * item.qty
        total += line_total
        print(f"  {item.name:<20s} {item.qty:>3d} x "
              f"Rp {item.price:>10,.0f} = Rp {line_total:>12,.0f}")
    return total

def print_totals(subtotal: float):
    ppn = subtotal * PPN_RATE
    grand_total = subtotal + ppn
    print("-" * 40)
    print(f"  Subtotal: Rp {subtotal:>12,.0f}")
    print(f"  PPN 11% : Rp {ppn:>12,.0f}")
    print(f"  TOTAL   : Rp {grand_total:>12,.0f}")
    print("=" * 40)
```

**Teknik 2: Rename Variable/Method**

```python
# SEBELUM — nama tidak jelas
def calc(lst):
    t = 0
    for i in lst:
        t += i.p * i.q
    return t

# SESUDAH — nama bermakna
def calculate_order_subtotal(order_items: list) -> float:
    """Hitung subtotal pesanan (sebelum pajak dan diskon)."""
    subtotal = 0
    for item in order_items:
        subtotal += item.price * item.quantity
    return subtotal
```

**Teknik 3: Replace Conditional with Polymorphism**

```python
# SEBELUM — Switch statements untuk hitung biaya pengiriman
def calculate_shipping(order, shipping_type):
    if shipping_type == "reguler":
        if order.weight <= 1:
            return 10000
        else:
            return 10000 + (order.weight - 1) * 5000
    elif shipping_type == "express":
        if order.weight <= 1:
            return 25000
        else:
            return 25000 + (order.weight - 1) * 10000
    elif shipping_type == "same_day":
        return 50000 + order.weight * 15000
    else:
        raise ValueError(f"Tipe pengiriman tidak dikenal: {shipping_type}")


# SESUDAH — Polymorphism
from abc import ABC, abstractmethod

class ShippingStrategy(ABC):
    @abstractmethod
    def calculate(self, weight: float) -> int:
        pass

class RegulerShipping(ShippingStrategy):
    def calculate(self, weight: float) -> int:
        base = 10_000
        extra = max(0, (weight - 1)) * 5_000
        return int(base + extra)

class ExpressShipping(ShippingStrategy):
    def calculate(self, weight: float) -> int:
        base = 25_000
        extra = max(0, (weight - 1)) * 10_000
        return int(base + extra)

class SameDayShipping(ShippingStrategy):
    def calculate(self, weight: float) -> int:
        return int(50_000 + weight * 15_000)


# Penggunaan — mudah extend tanpa ubah kode yang ada
SHIPPING_STRATEGIES = {
    "reguler": RegulerShipping(),
    "express": ExpressShipping(),
    "same_day": SameDayShipping(),
}

def calculate_shipping(order, shipping_type: str) -> int:
    strategy = SHIPPING_STRATEGIES.get(shipping_type)
    if not strategy:
        raise ValueError(f"Tipe pengiriman tidak dikenal: {shipping_type}")
    return strategy.calculate(order.weight)
```

**Teknik 4: Introduce Parameter Object**

```python
# SEBELUM — terlalu banyak parameter
def search_books(title=None, author=None, year_from=None,
                 year_to=None, category=None, publisher=None,
                 min_price=None, max_price=None, in_stock=None):
    pass

# SESUDAH — Parameter Object
@dataclass
class BookSearchCriteria:
    """Kriteria pencarian buku perpustakaan."""
    title: str | None = None
    author: str | None = None
    year_from: int | None = None
    year_to: int | None = None
    category: str | None = None
    publisher: str | None = None
    min_price: float | None = None
    max_price: float | None = None
    in_stock: bool | None = None

def search_books(criteria: BookSearchCriteria) -> list:
    """Cari buku berdasarkan kriteria."""
    pass

# Penggunaan — lebih bersih dan extensible
criteria = BookSearchCriteria(
    category="Rekayasa Perangkat Lunak",
    year_from=2020,
    in_stock=True,
)
results = search_books(criteria)
```

**Teknik 5: Extract Class**

```python
# SEBELUM — class Address "tertempel" di class Student
class Student:
    def __init__(self, nim, nama, jalan, kota, provinsi, kode_pos):
        self.nim = nim
        self.nama = nama
        self.jalan = jalan
        self.kota = kota
        self.provinsi = provinsi
        self.kode_pos = kode_pos

    def get_full_address(self):
        return f"{self.jalan}, {self.kota}, {self.provinsi} {self.kode_pos}"


# SESUDAH — Extract Address ke class terpisah
@dataclass
class Address:
    jalan: str
    kota: str
    provinsi: str
    kode_pos: str

    def full_address(self) -> str:
        return f"{self.jalan}, {self.kota}, {self.provinsi} {self.kode_pos}"

@dataclass
class Student:
    nim: str
    nama: str
    address: Address
```

---

## 7.4 Version Control dengan Git

### 7.4.1 Git Internals: Memahami Dasar

Git menyimpan **snapshot** dari seluruh repository di setiap commit, bukan diff per file. Pemahaman internal membantu mengatasi masalah Git yang kompleks.

```
┌────────────────────────────────────────────┐
│              GIT OBJECT MODEL               │
│                                             │
│  ┌──────────┐    ┌──────────┐               │
│  │  Commit   │───→│   Tree   │               │
│  │  abc123   │    │  (root)  │               │
│  │           │    └────┬─────┘               │
│  │ author    │         │                     │
│  │ message   │    ┌────┴─────┐               │
│  │ parent    │    ▼          ▼               │
│  └──────────┘  ┌──────┐  ┌──────────┐       │
│                │ Blob  │  │  Tree     │       │
│                │app.py │  │  /tests   │       │
│                │(file) │  │  (folder) │       │
│                └──────┘  └────┬─────┘       │
│                               ▼              │
│                          ┌──────────┐        │
│                          │  Blob     │        │
│                          │test_app.py│        │
│                          └──────────┘        │
│                                             │
│  4 jenis objek Git:                         │
│  • Blob   = isi file                        │
│  • Tree   = directory (berisi blob & tree)  │
│  • Commit = snapshot + metadata             │
│  • Tag    = named reference ke commit       │
│                                             │
│  Refs (references):                          │
│  • Branch = pointer yang bergerak ke commit  │
│  • HEAD   = pointer ke branch aktif saat ini │
│  • Tag    = pointer tetap ke commit tertentu │
└────────────────────────────────────────────┘
```

```python
# Demonstrasi: Bagaimana Git menyimpan data (konseptual)
import hashlib
import json

def git_hash_object(content: str) -> str:
    """Simulasi git hash-object — menghitung SHA-1 dari content."""
    header = f"blob {len(content)}\0"
    full_content = header + content
    return hashlib.sha1(full_content.encode()).hexdigest()

# Setiap file mendapat hash unik berdasarkan isi
file_content_v1 = "print('Hello, World!')"
file_content_v2 = "print('Hello, Indonesia!')"

hash_v1 = git_hash_object(file_content_v1)
hash_v2 = git_hash_object(file_content_v2)

print(f"v1 hash: {hash_v1}")  # Contoh: 8d0e41234...
print(f"v2 hash: {hash_v2}")  # Hash berbeda = content berbeda
print(f"Sama? {hash_v1 == hash_v2}")  # False
```

### 7.4.2 Branching Strategies

**Strategy 1: Git Flow (Vincent Driessen, 2010)**

```
main      ─●───────────────────────────────────●─── (production)
            │                                   ▲
            │   ┌───────────────────────────────┤
            │   │         release/1.0            │
            │   │  ┌──→ ●──●──●──────────────→ ─┤
            │   │  │                             │
develop   ──●──●──●──●──●──●──●──●──●──●──●──●── (integration)
               │     ▲  │     ▲     │     ▲
feature/   ────●──●──┘  │     │     │     │
login                   │     │     │     │
feature/   ─────────●──●──┘     │     │
search                          │     │
bugfix/    ─────────────────●──●──┘     │
typo                                    │
hotfix/    ────────────────────────●──┘
fix-crash  (dari main, merge ke main + develop)
```

| Branch | Asal | Merge ke | Lifetime | Naming |
|--------|------|----------|----------|--------|
| `main` | — | — | Permanent | `main` |
| `develop` | `main` | `main` (via release) | Permanent | `develop` |
| `feature/*` | `develop` | `develop` | Sampai merge | `feature/nama-fitur` |
| `bugfix/*` | `develop` | `develop` | Sampai merge | `bugfix/deskripsi-bug` |
| `release/*` | `develop` | `main` + `develop` | Sampai merge | `release/1.0.0` |
| `hotfix/*` | `main` | `main` + `develop` | Sampai merge | `hotfix/fix-crash` |

**Strategy 2: GitHub Flow (Simplified)**

```
main       ──●──●──●──●──●──●──●──●── (selalu deployable)
              │     ▲  │     ▲
feature/   ───●──●──┘  │     │
login         (PR)      │     │
feature/   ─────────●──●──┘
search                (PR)

Aturan:
1. main selalu deployable
2. Buat branch dari main
3. Buat Pull Request
4. Review + CI pass → Merge ke main
5. Deploy segera setelah merge
```

**Strategy 3: Trunk-Based Development**

```
main (trunk)  ──●──●──●──●──●──●──●── (semua commit langsung ke main)
                │  ▲  │  ▲
short-lived  ───●──┘  ●──┘
branches       (max 1-2 hari)

Prinsip:
- Branch sangat pendek (< 2 hari)
- Merge ke main sesering mungkin
- Feature flags untuk fitur yang belum siap
- Butuh CI/CD yang kuat
```

**Perbandingan Branching Strategies:**

| Aspek | Git Flow | GitHub Flow | Trunk-Based |
|-------|----------|-------------|-------------|
| Kompleksitas | Tinggi | Rendah | Rendah |
| Cocok untuk | Tim besar, release formal | Continuous deployment | Continuous deployment, tim mature |
| Branch lifetime | Bisa lama | Pendek-sedang | Sangat pendek (< 2 hari) |
| Release process | Explicit release branch | Deploy dari main | Deploy dari main + feature flags |
| Tim proyek kuliah? | Terlalu kompleks | **Recommended** | Butuh CI/CD matang |

> **Tips untuk proyek kuliah:** Gunakan **GitHub Flow** — sederhana namun efektif. Buat branch per fitur, buat PR, review, merge ke main. Git Flow terlalu complex untuk tim 4 orang.

### 7.4.3 Conventional Commits

Format: `<type>(<scope>): <description>`

```
feat(auth): tambah login dengan Google OAuth
^    ^       ^
|    |       |
|    |       └─── Deskripsi singkat (imperative mood, lowercase)
|    └─────────── Scope (opsional): bagian yang diubah
└──────────────── Type: jenis perubahan
```

| Type | Deskripsi | Contoh |
|------|-----------|--------|
| `feat` | Fitur baru | `feat(katalog): tambah fitur pencarian buku` |
| `fix` | Perbaikan bug | `fix(login): perbaiki redirect setelah login` |
| `docs` | Dokumentasi saja | `docs(readme): tambah panduan instalasi` |
| `style` | Formatting, tanpa ubah logic | `style: perbaiki indentasi di models.py` |
| `refactor` | Refactoring tanpa ubah behavior | `refactor(user): extract validasi ke helper` |
| `test` | Tambah/ubah test | `test(produk): tambah unit test search` |
| `chore` | Build, tools, deps | `chore: upgrade Flask ke 3.0` |
| `perf` | Peningkatan performa | `perf(query): optimasi query daftar produk` |
| `ci` | Perubahan CI/CD | `ci: tambah job deploy ke staging` |

```python
# Script helper: Validasi conventional commit message
import re

COMMIT_PATTERN = re.compile(
    r"^(feat|fix|docs|style|refactor|test|chore|perf|ci)"
    r"(\([a-z0-9-]+\))?: "
    r".{1,72}$"
)

def validate_commit_message(message: str) -> bool:
    """Validasi apakah commit message mengikuti conventional commits."""
    first_line = message.split("\n")[0]
    is_valid = bool(COMMIT_PATTERN.match(first_line))

    if is_valid:
        print(f"✓ Valid: '{first_line}'")
    else:
        print(f"✗ Invalid: '{first_line}'")
        print("  Format: <type>(<scope>): <description>")
        print("  Types: feat, fix, docs, style, refactor, test, chore, perf, ci")
    return is_valid


# Test
validate_commit_message("feat(auth): tambah login Google OAuth")   # ✓ Valid
validate_commit_message("fix: perbaiki bug di halaman checkout")   # ✓ Valid
validate_commit_message("Update file")                             # ✗ Invalid
validate_commit_message("WIP commit")                              # ✗ Invalid
```

### 7.4.4 Pull Request Workflow: Step-by-Step

```
┌─────────────────────────────────────────────────────────┐
│                 PULL REQUEST WORKFLOW                     │
│                                                          │
│  1. CREATE BRANCH                                        │
│     git checkout -b feature/search                       │
│                    ↓                                     │
│  2. DEVELOP                                              │
│     Tulis kode + test                                    │
│     git add . && git commit -m "feat(search): ..."       │
│                    ↓                                     │
│  3. PUSH                                                 │
│     git push -u origin feature/search                    │
│                    ↓                                     │
│  4. CREATE PR (di GitHub)                                │
│     • Title: "feat(search): tambah pencarian buku"       │
│     • Description: apa yang berubah, mengapa, cara test  │
│     • Assign reviewer                                    │
│     • Link ke Issue (jika ada)                           │
│                    ↓                                     │
│  5. CI CHECKS                                            │
│     GitHub Actions: lint → test → build                  │
│     (harus semua pass sebelum review)                    │
│                    ↓                                     │
│  6. CODE REVIEW                                          │
│     Reviewer: review kode, berikan feedback              │
│     Author: revisi jika perlu, push commit baru          │
│                    ↓                                     │
│  7. APPROVE + MERGE                                      │
│     Reviewer approve → Merge (squash/rebase/merge)       │
│                    ↓                                     │
│  8. CLEANUP                                              │
│     Delete feature branch (otomatis di GitHub)           │
│     git checkout main && git pull                        │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

**Template PR Description:**

```markdown
## Summary
Menambahkan fitur pencarian buku berdasarkan judul, penulis, dan kategori.

## Changes
- Tambah endpoint GET /api/books/search
- Tambah SearchService dengan filter query
- Tambah unit test untuk search (15 test cases)
- Update dokumentasi API

## How to Test
1. Jalankan `pytest tests/test_search.py`
2. Buka http://localhost:5000/api/books/search?q=python
3. Verifikasi hasil pencarian sesuai query

## Screenshots (jika ada UI)
[screenshot di sini]

## Checklist
- [x] Code follows coding standards (PEP 8)
- [x] Unit tests added/updated
- [x] CI pipeline passes
- [x] Documentation updated
- [ ] Manual testing done
```

---

## 7.5 Code Review: Best Practices

### 7.5.1 Mengapa Code Review?

```
┌──────────────────────────────────────────────────────────────┐
│                  MANFAAT CODE REVIEW                          │
├──────────────────────┬───────────────────────────────────────┤
│  Bug Detection       │ 60-90% bug ditemukan sebelum           │
│                      │ production (IBM study)                 │
├──────────────────────┼───────────────────────────────────────┤
│  Knowledge Sharing   │ Semua anggota tim memahami kode        │
│                      │ (mengurangi bus factor)                │
├──────────────────────┼───────────────────────────────────────┤
│  Consistency         │ Coding standards ditegakkan secara     │
│                      │ organik oleh peer                     │
├──────────────────────┼───────────────────────────────────────┤
│  Mentoring           │ Junior belajar dari feedback senior    │
│                      │ → mempercepat onboarding              │
├──────────────────────┼───────────────────────────────────────┤
│  Design Improvement  │ Reviewer sering melihat solusi yang    │
│                      │ lebih baik dari perspektif berbeda    │
└──────────────────────┴───────────────────────────────────────┘
```

### 7.5.2 Code Review Checklist

| Aspek | Pertanyaan yang Diajukan |
|-------|-------------------------|
| **Correctness** | Apakah logika benar dan sesuai requirements/user story? |
| **Design** | Apakah sesuai arsitektur dan design patterns yang disepakati? |
| **Readability** | Apakah kode bisa dipahami tanpa penjelasan verbal? |
| **Naming** | Apakah variabel dan fungsi memiliki nama yang descriptive? |
| **Testing** | Apakah ada test yang memadai? Edge cases tercovered? |
| **Security** | Apakah ada SQL injection, XSS, hardcoded credentials? |
| **Performance** | Apakah ada N+1 query, loop tidak efisien, memory leak? |
| **Error Handling** | Apakah error ditangani dengan baik? Pesan error jelas? |
| **DRY** | Apakah ada duplikasi kode yang bisa di-extract? |
| **Dependencies** | Apakah dependency baru benar-benar dibutuhkan? |

### 7.5.3 Cara Memberikan Feedback yang Konstruktif

```
┌────────────────────────────────────────────────────────────┐
│                ETIKA CODE REVIEW                            │
│                                                             │
│  ✓ DO:                                                      │
│    • Fokus pada KODE, bukan orangnya                        │
│    • Berikan saran yang actionable + contoh kode            │
│    • Apresiasi kode yang bagus ("Nice approach!")            │
│    • Review dalam 24 jam (jangan blocking terlalu lama)     │
│    • Bedakan: blocker vs suggestion vs nit                  │
│    • Tanya "mengapa" sebelum suggest perubahan              │
│                                                             │
│  ✗ DON'T:                                                   │
│    • "Ini salah semua" → "Ada beberapa area yang bisa       │
│       diperbaiki, terutama di bagian validasi"              │
│    • Block PR untuk hal yang tidak penting (nitpicking)     │
│    • Abaikan PR berhari-hari tanpa feedback                 │
│    • Review dengan ego — "Saya akan menulis ini berbeda"    │
│    • Terlalu banyak komentar di satu PR (max 10-15)         │
│                                                             │
│  Label feedback:                                            │
│    [BLOCKER] — harus diperbaiki sebelum merge               │
│    [SUGGESTION] — saran perbaikan, bisa diskusi             │
│    [NIT] — minor, tidak block merge                         │
│    [QUESTION] — minta penjelasan, bukan kritik              │
│    [PRAISE] — apresiasi kode yang bagus                     │
└────────────────────────────────────────────────────────────┘
```

**Contoh feedback yang baik:**

```markdown
# [BLOCKER] SQL Injection vulnerability
Baris 45: `db.execute(f"SELECT * FROM users WHERE id = {user_id}")`

Ini rentan SQL injection. Gunakan parameterized query:
```python
db.execute("SELECT * FROM users WHERE id = ?", (user_id,))
```

# [SUGGESTION] Bisa lebih readable dengan early return
Baris 23-35: Nested if bisa disederhanakan:
```python
# Sebelum
def process(data):
    if data:
        if data.is_valid():
            return do_something(data)

# Sesudah (early return)
def process(data):
    if not data or not data.is_valid():
        return None
    return do_something(data)
```

# [NIT] Typo di nama variabel
Baris 12: `studet_name` → `student_name`

# [PRAISE]
Nice use of dataclass di baris 5-15! Jauh lebih clean dari dict.
```

### 7.5.4 Pola Kolaborasi Tim di Indonesia

| Aspek | Startup Kecil (5-10 dev) | Perusahaan Tech (50+ dev) |
|-------|--------------------------|---------------------------|
| Review policy | 1 approval | 2 approvals, 1 dari senior |
| Review waktu | Same day | < 24 jam (SLA) |
| Merge strategy | Squash merge | Rebase atau squash |
| Tools | GitHub PR | GitHub/GitLab + CODEOWNERS |
| Bahasa review | Campuran ID/EN | Biasanya English |
| Kultur | Informal, chat | Formal labels, checklist |

> **Tips:** Di Gojek dan Tokopedia, code review adalah mekanisme utama knowledge transfer. Engineer baru biasanya menjadi reviewer (belajar codebase) sebelum menjadi contributor aktif. Di tim proyek kuliah, rotasi reviewer memastikan semua anggota memahami seluruh bagian kode.

---

## Studi Kasus Komprehensif: Refactoring Legacy Code di Tim Proyek Kuliah

### Konteks
Tim proyek RPL (4 orang) sedang mengerjakan Sprint 2 dari proyek "Perpustakaan Digital UAI." Sprint 1 sudah selesai, tetapi kode dari Sprint 1 memiliki banyak code smells karena terburu-buru mengejar deadline.

### Kode Asli (Sprint 1 — Banyak Code Smells)

```python
# routes.py — SEBELUM refactoring (Sprint 1)
from flask import Flask, request, jsonify
app = Flask(__name__)

books = []  # Smell: Global mutable state
id_counter = [0]  # Smell: Magic pattern

@app.route('/books', methods=['GET', 'POST'])
def handle_books():
    if request.method == 'GET':
        q = request.args.get('q', '')  # Smell: unclear variable name
        if q:
            result = []
            for b in books:  # Smell: unclear variable name
                if q.lower() in b['title'].lower() or q.lower() in b['author'].lower():
                    result.append(b)
            return jsonify(result)
        return jsonify(books)
    elif request.method == 'POST':
        data = request.get_json()
        # Smell: no validation
        id_counter[0] += 1
        book = {
            'id': id_counter[0],
            'title': data['title'],
            'author': data['author'],
            'year': data['year'],
            'isbn': data.get('isbn', ''),
            'available': True
        }
        books.append(book)
        return jsonify(book), 201
```

### Proses Refactoring (Sprint 2)

**Langkah 1:** Identifikasi code smells
- Global mutable state (`books`, `id_counter`)
- Unclear variable names (`q`, `b`)
- No input validation
- Long method (GET + POST in one function)
- No separation of concerns

**Langkah 2:** Refactoring bertahap

```python
# models.py — Extract Class untuk Book
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Book:
    """Representasi buku di perpustakaan digital."""
    id: int
    title: str
    author: str
    year: int
    isbn: str = ""
    available: bool = True

    def matches_query(self, query: str) -> bool:
        """Cek apakah buku cocok dengan query pencarian."""
        query_lower = query.lower()
        return (
            query_lower in self.title.lower()
            or query_lower in self.author.lower()
        )

    def to_dict(self) -> dict:
        """Convert ke dictionary untuk JSON response."""
        return {
            "id": self.id, "title": self.title,
            "author": self.author, "year": self.year,
            "isbn": self.isbn, "available": self.available,
        }


# services.py — Extract business logic ke Service
class BookService:
    """Service untuk mengelola buku perpustakaan."""

    def __init__(self):
        self._books: list[Book] = []
        self._next_id: int = 1

    def get_all(self) -> list[Book]:
        return list(self._books)

    def search(self, query: str) -> list[Book]:
        if not query:
            return self.get_all()
        return [book for book in self._books if book.matches_query(query)]

    def create(self, title: str, author: str, year: int,
               isbn: str = "") -> Book:
        book = Book(
            id=self._next_id, title=title,
            author=author, year=year, isbn=isbn,
        )
        self._books.append(book)
        self._next_id += 1
        return book


# validators.py — Extract validation
class BookValidator:
    """Validasi input data buku."""

    REQUIRED_FIELDS = ["title", "author", "year"]

    @classmethod
    def validate_create(cls, data: dict) -> list[str]:
        """Validasi data untuk membuat buku baru."""
        errors = []
        for field_name in cls.REQUIRED_FIELDS:
            if not data.get(field_name):
                errors.append(f"Field '{field_name}' wajib diisi")
        if data.get("year") and not isinstance(data["year"], int):
            errors.append("Field 'year' harus berupa angka")
        return errors


# routes.py — SESUDAH refactoring (Sprint 2)
from flask import Flask, request, jsonify

app = Flask(__name__)
book_service = BookService()

@app.route('/books', methods=['GET'])
def list_books():
    """Endpoint: Daftar dan pencarian buku."""
    search_query = request.args.get('q', '')
    books = book_service.search(search_query)
    return jsonify([book.to_dict() for book in books])

@app.route('/books', methods=['POST'])
def create_book():
    """Endpoint: Tambah buku baru."""
    data = request.get_json()
    errors = BookValidator.validate_create(data)
    if errors:
        return jsonify({"errors": errors}), 400

    book = book_service.create(
        title=data["title"],
        author=data["author"],
        year=data["year"],
        isbn=data.get("isbn", ""),
    )
    return jsonify(book.to_dict()), 201
```

### Hasil Refactoring
- 4 code smells teridentifikasi dan dihilangkan
- Kode terbagi menjadi 4 file dengan tanggung jawab jelas
- Input validation ditambahkan
- Setiap fungsi hanya melakukan satu hal
- Variable names lebih descriptive
- Mudah ditambahkan fitur baru (Open-Closed Principle)

---

## AI Corner: AI sebagai Pair Programmer (Level: Intermediate)

### 7.AI.1 AI untuk Mendeteksi Code Smells

**Prompt:**
```
Identifikasi semua code smells dalam kode Python berikut.
Untuk setiap smell, jelaskan: (1) nama smell, (2) lokasi di kode,
(3) mengapa ini masalah, (4) cara refactoring-nya dengan contoh kode.

[paste kode di sini]
```

**Evaluasi:** AI biasanya sangat baik mendeteksi code smells. Verifikasi bahwa:
- AI memberikan nama smell yang standar (dari katalog Fowler)
- Saran refactoring tidak mengubah behavior (jalankan test sebelum dan sesudah)
- AI tidak over-refactor — kadang kode sederhana tidak perlu abstraksi

### 7.AI.2 AI untuk Refactoring

**Prompt:**
```
Refactor fungsi Python ini agar memenuhi prinsip Single Responsibility
dan Clean Code. Pertahankan behavior yang sama (input/output tidak berubah).
Jelaskan setiap perubahan yang kamu lakukan.

[paste fungsi di sini]
```

**Batasan:** JANGAN langsung copy-paste hasil AI. Selalu:
1. Baca dan pahami setiap perubahan
2. Jalankan test suite — pastikan tidak ada regression
3. Review apakah refactoring masuk akal untuk konteks proyek

### 7.AI.3 AI untuk Generate Commit Messages

**Prompt:**
```
Berdasarkan diff berikut, buatkan commit message yang mengikuti
Conventional Commits specification. Berikan penjelasan singkat
mengapa perubahan ini dilakukan.

[paste git diff]
```

### 7.AI.4 AI untuk Code Review

**Prompt:**
```
Review kode berikut dari perspektif: security, performance,
readability, dan maintainability. Berikan feedback menggunakan
format: [BLOCKER], [SUGGESTION], atau [NIT].

[paste kode]
```

### 7.AI.5 Batasan AI dalam Software Construction

| AI Bisa | AI Tidak Bisa |
|---------|--------------|
| Detect pattern-based smells | Memahami business context secara penuh |
| Suggest refactoring standar | Tahu apakah refactoring worth it (trade-off) |
| Generate boilerplate code | Menjamin kode bebas bug (selalu test!) |
| Format commit messages | Memahami arsitektur keseluruhan proyek |
| Identify security patterns | Menggantikan code review oleh manusia |

> **Prinsip:** AI adalah **second opinion**, bukan pengganti critical thinking. Dalam konteks tim, AI bisa membantu reviewer menemukan isu teknis, tetapi keputusan desain tetap ada di tangan manusia yang memahami konteks bisnis.

---

## Latihan Soal

### Level Dasar (C1-C2)

1. Sebutkan dan jelaskan 5 prinsip Clean Code menurut Robert C. Martin.
2. Apa itu code smell? Jelaskan 5 contoh code smell beserta teknik refactoring yang sesuai.
3. Jelaskan perbedaan antara `git merge` dan `git rebase`. Kapan masing-masing digunakan?
4. Sebutkan dan jelaskan 7 tipe dalam Conventional Commits.
5. Apa manfaat code review? Sebutkan minimal 4 manfaat.

### Level Menengah (C3-C4)

6. Diberikan kode Python berikut yang memiliki 5 code smells. Identifikasi semua smells dan lakukan refactoring:
   ```python
   def p(d):
       t = 0
       for i in d:
           if i[2] == 1:
               t += i[1] * 0.9
           elif i[2] == 2:
               t += i[1] * 0.8
           else:
               t += i[1]
       if t > 500000:
           t = t * 0.95
       return t
   ```
7. Buatlah Git Flow branching diagram (ASCII) untuk proyek tim 4 orang yang membangun fitur login, search, dan checkout. Sertakan conventional commit messages untuk setiap commit.
8. Lakukan code review pada kode berikut — berikan minimal 5 feedback menggunakan format label ([BLOCKER], [SUGGESTION], [NIT], [QUESTION], [PRAISE]):
   ```python
   def get_data(id):
       data = db.execute(f"SELECT * FROM users WHERE id = {id}")
       if data != None:
           return data
       else:
           return "not found"
   ```
9. Bandingkan Git Flow, GitHub Flow, dan Trunk-Based Development. Untuk proyek akhir RPL (tim 4 orang, 10 minggu), strategi mana yang paling cocok? Jelaskan alasannya.
10. Tunjukkan proses refactoring step-by-step dari sebuah God Class yang menangani user authentication, email sending, dan report generation menjadi 3 class terpisah.

### Level Mahir (C5-C6)

11. Evaluasi: apakah Git Flow atau Trunk-Based Development lebih cocok untuk perusahaan e-commerce Indonesia yang melakukan 50+ deployment per hari? Argumentasikan dari perspektif DORA metrics.
12. Rancang coding standards document untuk tim proyek akhir RPL Anda yang mencakup: (a) naming conventions, (b) function rules, (c) file structure, (d) Git workflow, (e) PR template, (f) code review checklist, (g) Definition of Done.
13. Analisis kritis: "Code coverage 100% berarti kode bebas bug." Setujukah? Jelaskan hubungan antara code quality, code coverage, dan refactoring.
14. Sebuah tim mewarisi codebase legacy 50.000 baris tanpa test, tanpa documentation, dan penuh code smells. Rancang strategi refactoring bertahap yang: (a) tidak menghentikan delivery fitur baru, (b) membangun test safety net, (c) memprioritaskan bagian mana yang di-refactor dulu.
15. Evaluasi penggunaan AI (GitHub Copilot) untuk code review. Apa kelebihannya dibanding human review? Apa kelemahannya? Kapan human review tidak bisa digantikan oleh AI?

---

## Rangkuman

1. **Clean Code** adalah kode yang mudah dibaca, dipahami, dan diubah — berdasarkan 10 prinsip utama: meaningful names, small functions, DRY, KISS, YAGNI, Boy Scout Rule, minimize comments, error handling, consistent formatting.
2. **Coding standards** (PEP 8 untuk Python, ESLint untuk JavaScript) memastikan konsistensi penulisan kode dalam tim. Gunakan linter dan formatter otomatis.
3. **Code smells** (Long Method, God Class, Magic Number, Feature Envy, dll.) adalah indikasi masalah desain yang perlu refactoring. Identifikasi rutin selama code review.
4. **Refactoring** mengubah struktur internal kode tanpa mengubah behavior eksternal. Teknik utama: Extract Method, Rename Variable, Replace Conditional with Polymorphism, Introduce Parameter Object, Extract Class.
5. **Git** menyimpan snapshot (bukan diff) melalui 4 tipe objek: blob, tree, commit, tag. Refs (branch, HEAD, tag) adalah pointer ke commit.
6. **Branching strategies**: Git Flow (kompleks, tim besar), GitHub Flow (sederhana, CD), Trunk-Based (sangat sederhana, butuh CI matang). Untuk proyek kuliah, **GitHub Flow** paling cocok.
7. **Conventional Commits** (`feat`, `fix`, `docs`, dll.) memberikan format standar yang memudahkan changelog generation dan semantic versioning.
8. **Pull Request workflow** terdiri dari: buat branch → develop → push → create PR → CI checks → code review → approve → merge → cleanup.
9. **Code review** bukan hanya mencari bug — juga knowledge sharing, consistency, mentoring, dan design improvement. Gunakan label ([BLOCKER], [SUGGESTION], [NIT]) untuk feedback yang jelas.
10. **AI sebagai pair programmer** sangat baik untuk detect smells dan suggest refactoring, tetapi tidak menggantikan human judgment tentang konteks bisnis dan trade-off desain.

---

## Referensi

1. Martin, R. C. (2009). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall.
2. Fowler, M. (2019). *Refactoring: Improving the Design of Existing Code* (2nd ed.). Addison-Wesley.
3. Chacon, S. & Straub, B. (2014). *Pro Git* (2nd ed.). Apress. Available free at git-scm.com.
4. Conventional Commits. (2024). *Conventional Commits Specification v1.0.0*. conventionalcommits.org.
5. Van Rossum, G. et al. (2001). *PEP 8 — Style Guide for Python Code*. python.org/peps/pep-0008.
6. Driessen, V. (2010). "A Successful Git Branching Model." nvie.com.
7. Hunt, A. & Thomas, D. (2019). *The Pragmatic Programmer* (20th Anniversary ed.). Addison-Wesley.
8. Google Engineering Practices. (2024). "How to do a code review." google.github.io/eng-practices.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
