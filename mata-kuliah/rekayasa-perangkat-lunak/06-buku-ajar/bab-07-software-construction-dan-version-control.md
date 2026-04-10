# BAB 7: SOFTWARE CONSTRUCTION DAN VERSION CONTROL

**Oleh: Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi | Level Bloom |
|-----------|-----------|-------------|
| 4.1 | Menerapkan prinsip Clean Code, coding standards, dan teknik refactoring | C3 (Menerapkan) |
| 4.2 | Menggunakan Git branching strategy dan melakukan code review yang efektif | C3-C4 (Menerapkan-Menganalisis) |

---

## 7.1 Clean Code

### 7.1.1 Apa Itu Clean Code?

> "Any fool can write code that a computer can understand. Good programmers write code that humans can understand." — Martin Fowler

Clean Code adalah kode yang **mudah dibaca, dipahami, dan diubah** oleh developer lain (dan oleh diri sendiri 6 bulan kemudian).

### 7.1.2 Prinsip Penamaan

| Prinsip | Buruk | Baik |
|---------|-------|------|
| Descriptive | `d`, `temp`, `data` | `days_until_deadline`, `user_count` |
| Pronounceable | `gen_ymdhms` | `generate_timestamp` |
| Searchable | `7`, `"admin"` | `MAX_RETRY = 7`, `ROLE_ADMIN = "admin"` |
| Consistent | `get_user`, `fetch_book`, `retrieve_order` | `get_user`, `get_book`, `get_order` |

### 7.1.3 Prinsip Fungsi

```python
# BURUK: Fungsi terlalu panjang, banyak tanggung jawab
def process_order(order_data):
    # Validasi (20 baris)
    # Hitung total (15 baris)
    # Proses pembayaran (25 baris)
    # Kirim email konfirmasi (20 baris)
    # Update inventory (15 baris)
    # Generate laporan (10 baris)
    pass  # 100+ baris

# BAIK: Setiap fungsi satu tanggung jawab
def process_order(order_data):
    validated_data = validate_order(order_data)
    total = calculate_total(validated_data)
    payment_result = process_payment(validated_data, total)
    send_confirmation_email(validated_data, payment_result)
    update_inventory(validated_data)
```

**Aturan fungsi:**
- Fungsi harus **kecil** (idealnya < 20 baris)
- Fungsi harus melakukan **satu hal** (Single Responsibility)
- Fungsi harus pada **satu level abstraksi** yang sama
- Parameter idealnya **0-2**, maksimal 3

### 7.1.4 Coding Standards

**Python (PEP 8):**
- Indentasi 4 spasi
- Nama variabel/fungsi: `snake_case`
- Nama class: `PascalCase`
- Konstanta: `UPPER_SNAKE_CASE`
- Maksimal 79 karakter per baris

**JavaScript (ESLint + Prettier):**
- Indentasi 2 spasi
- Nama variabel/fungsi: `camelCase`
- Nama class: `PascalCase`
- Gunakan `const` dan `let`, hindari `var`
- Semicolons: konsisten (selalu atau tidak pernah)

## 7.2 Code Smells dan Refactoring

### 7.2.1 Code Smells

| Code Smell | Gejala | Refactoring |
|-----------|--------|-------------|
| **Long Method** | Fungsi > 20 baris | Extract Method |
| **Duplicate Code** | Kode sama di 2+ tempat | Extract Method/Class |
| **God Class** | Class terlalu banyak responsibility | Split Class |
| **Magic Number** | `if status == 3` | Extract Constant: `STATUS_APPROVED = 3` |
| **Feature Envy** | Method lebih banyak akses data class lain | Move Method |
| **Shotgun Surgery** | Satu perubahan → edit banyak file | Move Method, Inline Class |
| **Dead Code** | Kode tidak pernah dieksekusi | Delete |
| **Comments** | Komentar menjelaskan kode yang buruk | Refactor kode agar self-documenting |

### 7.2.2 Teknik Refactoring

**Extract Method:**
```python
# Sebelum
def print_invoice(invoice):
    print("=== INVOICE ===")
    print(f"Customer: {invoice.customer.name}")
    print(f"Email: {invoice.customer.email}")
    total = 0
    for item in invoice.items:
        total += item.price * item.quantity
    print(f"Total: Rp {total:,.0f}")

# Sesudah
def print_invoice(invoice):
    print_header()
    print_customer_info(invoice.customer)
    total = calculate_total(invoice.items)
    print_total(total)
```

**Extract Constant:**
```python
# Sebelum
if user.role == 1:  # Apa itu 1?
    allow_access()

# Sesudah
ROLE_ADMIN = 1
ROLE_USER = 2

if user.role == ROLE_ADMIN:
    allow_access()
```

## 7.3 Version Control dengan Git

### 7.3.1 Git Internals (Konsep)

Git menyimpan snapshot, bukan diff. Setiap commit berisi:
- **Tree** — snapshot dari semua file
- **Parent** — pointer ke commit sebelumnya
- **Author** — siapa yang menulis perubahan
- **Message** — deskripsi perubahan

### 7.3.2 Git Flow Branching Strategy

```
main        ──●──────────────────────●──── (production)
              │                      ▲
develop     ──●──●──●──●──●──●──●──●── (integration)
                  │     ▲  │     ▲
feature/login  ───●──●──┘  │     │
feature/search ────────●──●──┘     │
bugfix/typo    ────────────────●──┘
```

| Branch | Tujuan | Lifetime |
|--------|--------|----------|
| `main` | Production code | Permanent |
| `develop` | Integration | Permanent |
| `feature/*` | Fitur baru | Sampai merge |
| `bugfix/*` | Perbaikan bug | Sampai merge |
| `release/*` | Persiapan release | Sampai merge |
| `hotfix/*` | Fix urgent production | Sampai merge |

### 7.3.3 Conventional Commits

Format: `<type>(<scope>): <description>`

| Type | Deskripsi | Contoh |
|------|-----------|--------|
| `feat` | Fitur baru | `feat(auth): tambah login Google OAuth` |
| `fix` | Perbaikan bug | `fix(search): perbaiki case-insensitive` |
| `docs` | Dokumentasi | `docs(readme): update instalasi` |
| `style` | Formatting | `style: fix indentation` |
| `refactor` | Refactoring | `refactor(user): extract validation` |
| `test` | Testing | `test(buku): tambah unit test search` |
| `chore` | Maintenance | `chore: update dependencies` |

### 7.3.4 Pull Request Workflow

```
1. Buat branch    → git checkout -b feature/search
2. Kerjakan       → git add . && git commit -m "feat: ..."
3. Push           → git push -u origin feature/search
4. Buat PR        → di GitHub, feature/search → develop
5. Review         → Reviewer memberikan feedback
6. Revisi         → Commit tambahan jika perlu
7. Merge          → Squash merge ke develop
8. Cleanup        → Delete feature branch
```

## 7.4 Code Review

### 7.4.1 Mengapa Code Review?

1. **Bug detection** — menemukan bug sebelum production
2. **Knowledge sharing** — semua anggota tim paham kode
3. **Consistency** — menjaga coding standards
4. **Mentoring** — junior belajar dari feedback senior

### 7.4.2 Code Review Checklist

| Aspek | Pertanyaan |
|-------|------------|
| **Correctness** | Apakah logika benar sesuai requirements? |
| **Design** | Apakah sesuai arsitektur dan patterns? |
| **Readability** | Apakah bisa dipahami tanpa penjelasan tambahan? |
| **Testing** | Apakah ada test yang memadai? |
| **Security** | Apakah ada SQL injection, XSS, atau data exposure? |
| **Performance** | Apakah ada N+1 query atau loop tidak efisien? |
| **Naming** | Apakah nama variabel dan fungsi descriptive? |

### 7.4.3 Etika Code Review

**Do:**
- Fokus pada kode, bukan orangnya
- Berikan saran yang actionable
- Apresiasi kode yang bagus
- Review dalam 24 jam

**Don't:**
- "Ini salah semua" → "Saya punya saran untuk bagian ini"
- Memblokir PR untuk hal yang tidak penting (nitpicking)
- Mengabaikan PR berhari-hari

---

## AI Corner: AI sebagai Pair Programmer (Level: Intermediate)

| Aktivitas | Prompt Contoh | Catatan |
|-----------|---------------|---------|
| Detect code smells | "Identifikasi code smells dalam kode Python ini: [paste]" | AI bagus mendeteksi smells |
| Refactoring | "Refactor fungsi ini agar memenuhi Single Responsibility: [paste]" | Review hasil — jangan langsung copy |
| Generate commit message | "Buatkan commit message conventional commit untuk perubahan ini: [paste diff]" | Verifikasi scope dan type |
| Code review | "Review kode ini dari sisi security, performance, dan readability" | Gunakan sebagai second opinion |

---

## Latihan Soal

### Level Dasar (C1-C2)
1. Sebutkan 5 prinsip Clean Code.
2. Jelaskan 4 jenis code smell dan cara refactoring-nya.
3. Apa perbedaan antara `git merge` dan `git rebase`?
4. Sebutkan 7 tipe conventional commits.

### Level Menengah (C3-C4)
5. Identifikasi 5 code smells dalam kode berikut dan lakukan refactoring.
6. Buatlah Git Flow branching diagram untuk proyek tim 4 orang yang membangun fitur login, search, dan checkout.
7. Lakukan code review pada kode berikut — berikan 5 feedback yang konstruktif.

### Level Mahir (C5-C6)
8. Evaluasi: apakah Git Flow atau GitHub Flow lebih cocok untuk proyek open-source dengan kontributor global?
9. Rancang coding standards document untuk tim proyek akhir Anda — cover naming, formatting, Git workflow, dan review process.

---

## Rangkuman

1. **Clean Code** adalah kode yang mudah dibaca, dipahami, dan diubah — naming, fungsi kecil, satu abstraksi level.
2. **Code smells** (Long Method, God Class, Magic Number, dll.) menandakan kode perlu refactoring.
3. **Refactoring** mengubah struktur internal tanpa mengubah perilaku eksternal.
4. **Git Flow** mengorganisasi development dengan branch main, develop, feature, bugfix, release, hotfix.
5. **Conventional Commits** memberikan format standar untuk commit messages.
6. **Code Review** bukan hanya mencari bug — tapi juga knowledge sharing, consistency, dan mentoring.

---

## Referensi

1. Martin, R. C. (2009). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall.
2. Fowler, M. (2019). *Refactoring: Improving the Design of Existing Code* (2nd ed.). Addison-Wesley.
3. Chacon, S. & Straub, B. (2014). *Pro Git* (2nd ed.). Apress.
4. Conventional Commits. (2024). *Conventional Commits Specification v1.0.0*. conventionalcommits.org.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
