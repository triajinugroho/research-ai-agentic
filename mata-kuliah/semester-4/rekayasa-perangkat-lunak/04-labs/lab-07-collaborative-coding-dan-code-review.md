# Lab 07: Collaborative Coding dan Code Review

## Informasi Lab

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak (IF2205) |
| **Lab** | 7 dari 13 |
| **Topik** | Code Smells, Refactoring, Git Flow, Conventional Commits, Pull Request, Code Review |
| **CPMK** | CPMK-4 (Mengimplementasikan software dengan coding standards, version control, code review, dan kolaborasi tim Agile/Scrum) |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |
| **Prasyarat** | Lab 01-06 selesai, memahami clean code dan Git workflow dari modul Minggu 7 |

---

## Tujuan

Setelah menyelesaikan lab ini, mahasiswa mampu:

1. **Mengidentifikasi** (C4) minimal 5 code smells dalam kode yang diberikan dan menjelaskan dampaknya
2. **Menerapkan** (C3) teknik refactoring untuk memperbaiki code smells tanpa mengubah perilaku program
3. **Menggunakan** (C3) Git Flow branching strategy dan conventional commits dalam workflow kolaborasi
4. **Melakukan** (C5) code review yang konstruktif pada Pull Request dengan komentar spesifik dan actionable

---

## Konsep Singkat

### Clean Code dan Code Smells

**Clean code** adalah kode yang mudah dibaca, dipahami, dan diubah oleh developer lain. Robert C. Martin (penulis Clean Code) menyatakan: "Any fool can write code that a computer can understand. Good programmers write code that humans can understand."

**Code smells** adalah indikator bahwa ada masalah dalam desain kode. Code smell bukan bug -- kode tetap berjalan, tapi sulit di-maintain dan rentan terhadap bug di masa depan.

```
10 Code Smells yang Paling Umum:

  1. Long Method        -> Method > 20 baris, sulit dipahami
  2. Magic Numbers      -> Angka tanpa penjelasan (if x > 86400)
  3. Bad Naming         -> Nama variabel tidak deskriptif (d, t, x)
  4. Duplicate Code     -> Kode yang sama di beberapa tempat
  5. God Class          -> Class yang tahu/melakukan terlalu banyak
  6. Long Parameter     -> Fungsi dengan 5+ parameter
  7. Dead Code          -> Kode yang tidak pernah dieksekusi
  8. Nested Conditionals-> if di dalam if di dalam if...
  9. Feature Envy       -> Method lebih banyak akses data class lain
  10. Primitive Obsession-> Pakai string/int untuk konsep domain
```

### Refactoring

**Refactoring** adalah proses memperbaiki struktur internal kode tanpa mengubah perilaku eksternalnya. Prinsip utama: "Make it work, make it right, make it fast."

| Teknik Refactoring | Sebelum | Sesudah |
|---------------------|---------|---------|
| Extract Method | Fungsi panjang 50 baris | 5 fungsi @ 10 baris |
| Rename Variable | `d = calc(t, u)` | `denda = hitung_denda(peminjaman, user)` |
| Replace Magic Number | `if days > 14:` | `if days > MAX_LOAN_DAYS:` |
| Introduce Parameter Object | `f(a, b, c, d, e)` | `f(config)` |
| Extract Class | God class 500 baris | 3 class @ 170 baris |

### Git Flow

Git Flow adalah branching strategy yang terstruktur untuk kolaborasi tim:

```
Git Flow Branching Model:

  main ─────────────────●──────────────────●──────── (production)
                       /                   /
  develop ────●───●──●─────●───●──●───●──●────────── (integration)
             /   /       / /       \
  feature/  ●──●       ●●          \
  login                              \
                                      \
  feature/  ─────────────────●──●──●───● (merged to develop)
  search
```

| Branch | Tujuan | Nama |
|--------|--------|------|
| `main` | Kode production yang stabil | `main` |
| `develop` | Branch integrasi untuk fitur baru | `develop` |
| `feature/*` | Pengembangan fitur individual | `feature/pencarian-buku` |
| `hotfix/*` | Perbaikan bug urgent di production | `hotfix/fix-login-error` |

### Conventional Commits

Conventional Commits memberikan format standar untuk pesan commit:

```
<type>(<scope>): <deskripsi>

Tipe:
  feat:     Fitur baru
  fix:      Perbaikan bug
  docs:     Perubahan dokumentasi saja
  style:    Formatting, tidak mengubah logika (whitespace, titik koma)
  refactor: Perubahan kode yang bukan fitur baru atau perbaikan bug
  test:     Menambah atau memperbaiki test
  chore:    Perubahan build, tools, dependencies

Contoh:
  feat(auth): tambah fitur login dengan NIM
  fix(search): perbaiki pencarian case-insensitive
  refactor(buku): extract method hitung_denda dari class Peminjaman
  docs(api): update dokumentasi endpoint peminjaman
  test(auth): tambah unit test untuk validasi NIM
```

> **Referensi:** Materi lengkap tersedia di modul Minggu 7 (week-07) dan Bab 7 Buku Ajar.

---

## Persiapan

| Kebutuhan | Detail |
|-----------|--------|
| Repository | Repository GitHub dari Lab 01-06 |
| Tim | Kelompok 3-4 orang (sama dengan tim proyek) |
| Partner Review | Setiap anggota akan me-review PR anggota lain |
| Pengetahuan | Konsep clean code, PEP 8, dan Git dasar |

---

## Langkah-langkah

### Langkah 1: Identifikasi Code Smells (20 menit)

**Mengapa:** Sebelum bisa menulis clean code, mahasiswa harus bisa mengenali code yang bermasalah. Latihan ini melatih "mata" untuk melihat code smells yang sering tersembunyi di kode sehari-hari.

**Instruksi:**

Berikut adalah kode Python dengan **minimal 8 code smells** yang sengaja ditanamkan. Tugas Anda: identifikasi setiap smell, jelaskan mengapa bermasalah, dan tentukan teknik refactoring yang tepat.

Buat file `exercises/smelly_code.py`:

```python
# exercises/smelly_code.py - KODE DENGAN SENGAJA BERMASALAH
# Tugas: identifikasi code smells dan refactor

import smtplib
from datetime import datetime

# [SMELL 1: Magic Numbers]
# [SMELL 2: Bad Naming]
# [SMELL 3: God Function - terlalu banyak tanggung jawab]
# [SMELL 4: Duplicate Code]
# [SMELL 5: Long Parameter List]
# [SMELL 6: Nested Conditionals]
# [SMELL 7: Primitive Obsession]
# [SMELL 8: Dead Code]

def process(d, t, u, n, e, p, s):
    """Proses peminjaman buku."""
    result = {}
    
    # Cek tipe transaksi
    if t == 1:  # Peminjaman
        if d['stok'] > 0:
            if u != None:
                # Cek batas peminjaman
                count = 0
                for item in d.get('peminjaman_list', []):
                    if item['user'] == u and item['status'] == 'aktif':
                        count = count + 1
                
                if count < 3:
                    d['stok'] = d['stok'] - 1
                    result['status'] = 'ok'
                    result['message'] = 'Berhasil pinjam'
                    
                    # Kirim email
                    try:
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login('perpus@uai.ac.id', p)
                        msg = f'Subject: Peminjaman Buku\n\nHalo {n}, Anda meminjam {d["judul"]}'
                        server.sendmail('perpus@uai.ac.id', e, msg)
                        server.quit()
                    except:
                        pass
                    
                    # Catat log
                    f = open('log.txt', 'a')
                    f.write(f'{datetime.now()} - {u} meminjam {d["judul"]}\n')
                    f.close()
                    
                    # Hitung biaya jika premium
                    if s == 'premium':
                        result['biaya'] = 0
                    elif s == 'regular':
                        result['biaya'] = 5000
                    elif s == 'trial':
                        result['biaya'] = 10000
                else:
                    result['status'] = 'error'
                    result['message'] = 'Batas peminjaman tercapai (max 3)'
            else:
                result['status'] = 'error'
                result['message'] = 'User tidak valid'
        else:
            result['status'] = 'error'
            result['message'] = 'Stok habis'
    
    elif t == 2:  # Pengembalian
        d['stok'] = d['stok'] + 1
        result['status'] = 'ok'
        result['message'] = 'Berhasil kembalikan'
        
        # Hitung denda (KODE DUPLIKAT!)
        hari_terlambat = 0
        if d.get('deadline'):
            selisih = datetime.now() - d['deadline']
            hari_terlambat = selisih.days
        
        if hari_terlambat > 0:
            result['denda'] = hari_terlambat * 1000
        
        # Kirim email (DUPLIKAT!)
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('perpus@uai.ac.id', p)
            msg = f'Subject: Pengembalian Buku\n\nHalo {n}, buku {d["judul"]} dikembalikan'
            server.sendmail('perpus@uai.ac.id', e, msg)
            server.quit()
        except:
            pass
        
        # Catat log (DUPLIKAT!)
        f = open('log.txt', 'a')
        f.write(f'{datetime.now()} - {u} mengembalikan {d["judul"]}\n')
        f.close()
    
    elif t == 3:  # Perpanjangan (DEAD CODE - fitur belum diimplementasi)
        pass
    
    return result
```

Buat file `exercises/smell-analysis.md` dan identifikasi setiap smell:

```markdown
# Code Smell Analysis

| No | Baris | Code Smell | Penjelasan | Dampak | Teknik Refactoring |
|----|-------|-----------|-----------|--------|-------------------|
| 1 | 19 | Magic Number | t == 1, t == 2 tidak jelas artinya | Developer baru harus tebak arti angka | Replace Magic Number with Named Constant |
| 2 | 9 | Bad Naming | d, t, u, n, e, p, s tidak deskriptif | Kode sulit dipahami | Rename Variable |
| 3 | 9-80 | God Function | Satu fungsi menangani pinjam, kembali, email, log, denda | Sulit di-test, sulit diubah | Extract Method |
| 4 | 36-42, 63-69 | Duplicate Code | Kode kirim email diulang 2x | Perubahan harus di 2 tempat | Extract Method |
| 5 | 9 | Long Parameter List | 7 parameter | Sulit dipanggil, mudah salah urutan | Introduce Parameter Object |
| 6 | 19-55 | Nested Conditionals | 4 level if bersarang | Sulit dibaca dan di-debug | Guard Clause / Early Return |
| 7 | 19 | Primitive Obsession | t=1/2/3 untuk tipe transaksi | Tidak ada type safety | Replace with Enum |
| 8 | 77-78 | Dead Code | t == 3 hanya pass | Membingungkan, apakah sengaja? | Remove Dead Code |
```

**Diskusi kelas (5 menit):** Setiap tim mempresentasikan 2-3 smell yang mereka temukan. Apakah ada smell yang terlewat oleh tim lain?

**Expected Output:** Minimal 8 code smells teridentifikasi dengan penjelasan dan teknik refactoring.

**Estimasi waktu:** 20 menit

---

### Langkah 2: Refactoring Practice (25 menit)

**Mengapa:** Mengidentifikasi smell saja tidak cukup -- mahasiswa harus bisa memperbaikinya. Refactoring adalah keterampilan harian software engineer. Kuncinya: ubah struktur tanpa mengubah perilaku.

**Instruksi:**

Buat file `exercises/clean_code.py` -- versi refactored dari smelly_code.py:

```python
# exercises/clean_code.py - Hasil refactoring dari smelly_code.py

from enum import Enum
from datetime import datetime
from typing import Optional
import logging

# Refactoring 1: Replace Magic Number with Enum
class TransactionType(Enum):
    """Tipe transaksi peminjaman."""
    PINJAM = "pinjam"
    KEMBALI = "kembali"

class MembershipTier(Enum):
    """Tier keanggotaan perpustakaan."""
    PREMIUM = "premium"
    REGULAR = "regular"
    TRIAL = "trial"

# Refactoring 2: Replace Magic Number with Named Constant
MAX_BOOKS_PER_USER = 3
DENDA_PER_HARI = 1000  # Rp 1.000

# Refactoring 3: Rename variables + Introduce Parameter Object
class TransactionRequest:
    """Objek yang merangkum data request transaksi."""
    
    def __init__(self, user_id: str, user_name: str, user_email: str,
                 membership: MembershipTier = MembershipTier.REGULAR):
        self.user_id = user_id
        self.user_name = user_name
        self.user_email = user_email
        self.membership = membership


# Refactoring 4: Setup logging (menggantikan file I/O manual)
logger = logging.getLogger('perpustakaan')
logging.basicConfig(level=logging.INFO)


# Refactoring 5: Extract Method - Email
class EmailService:
    """Service untuk mengirim email notifikasi."""
    
    @staticmethod
    def send_notification(recipient_email: str, subject: str, body: str) -> bool:
        """Kirim email notifikasi.
        
        Returns:
            True jika berhasil, False jika gagal
        """
        try:
            # Simulasi pengiriman email (di production, gunakan library email)
            logger.info(f"[EMAIL] To: {recipient_email}, Subject: {subject}")
            return True
        except Exception as e:
            logger.error(f"Gagal kirim email ke {recipient_email}: {e}")
            return False


# Refactoring 6: Extract Method - Denda Calculator
class DendaCalculator:
    """Menghitung denda keterlambatan."""
    
    @staticmethod
    def hitung(deadline: Optional[datetime]) -> int:
        """Hitung denda berdasarkan keterlambatan.
        
        Args:
            deadline: Tanggal batas pengembalian
        
        Returns:
            Jumlah denda dalam Rupiah (0 jika tidak terlambat)
        """
        if not deadline:
            return 0
        selisih = datetime.now() - deadline
        hari_terlambat = max(0, selisih.days)
        return hari_terlambat * DENDA_PER_HARI


# Refactoring 7: Extract Method - Biaya Calculator
class BiayaCalculator:
    """Menghitung biaya peminjaman berdasarkan tier."""
    
    BIAYA_PER_TIER = {
        MembershipTier.PREMIUM: 0,
        MembershipTier.REGULAR: 5000,
        MembershipTier.TRIAL: 10000,
    }
    
    @classmethod
    def hitung(cls, tier: MembershipTier) -> int:
        """Hitung biaya peminjaman berdasarkan tier membership."""
        return cls.BIAYA_PER_TIER.get(tier, 5000)


# Refactoring 8: Single Responsibility - Main Service
class PeminjamanService:
    """Service untuk mengelola peminjaman buku."""
    
    def __init__(self):
        self.email_service = EmailService()
        self.denda_calculator = DendaCalculator()
        self.biaya_calculator = BiayaCalculator()
    
    def pinjam_buku(self, buku: dict, request: TransactionRequest) -> dict:
        """Proses peminjaman buku.
        
        Refactoring: Guard Clause menggantikan nested conditionals
        """
        # Guard clause 1: validasi user
        if not request.user_id:
            return {"status": "error", "message": "User tidak valid"}
        
        # Guard clause 2: cek stok
        if buku.get('stok', 0) <= 0:
            return {"status": "error", "message": "Stok habis"}
        
        # Guard clause 3: cek batas peminjaman
        jumlah_aktif = self._hitung_peminjaman_aktif(buku, request.user_id)
        if jumlah_aktif >= MAX_BOOKS_PER_USER:
            return {
                "status": "error",
                "message": f"Batas peminjaman tercapai (max {MAX_BOOKS_PER_USER})"
            }
        
        # Proses peminjaman
        buku['stok'] -= 1
        biaya = self.biaya_calculator.hitung(request.membership)
        
        # Notifikasi dan logging
        self.email_service.send_notification(
            request.user_email,
            "Peminjaman Buku",
            f"Halo {request.user_name}, Anda meminjam '{buku['judul']}'"
        )
        logger.info(f"{request.user_id} meminjam '{buku['judul']}'")
        
        return {
            "status": "ok",
            "message": "Berhasil pinjam",
            "biaya": biaya
        }
    
    def kembalikan_buku(self, buku: dict, request: TransactionRequest) -> dict:
        """Proses pengembalian buku."""
        buku['stok'] += 1
        
        # Hitung denda
        denda = self.denda_calculator.hitung(buku.get('deadline'))
        
        # Notifikasi dan logging
        self.email_service.send_notification(
            request.user_email,
            "Pengembalian Buku",
            f"Halo {request.user_name}, buku '{buku['judul']}' dikembalikan"
        )
        logger.info(f"{request.user_id} mengembalikan '{buku['judul']}'")
        
        result = {"status": "ok", "message": "Berhasil kembalikan"}
        if denda > 0:
            result["denda"] = denda
        return result
    
    def _hitung_peminjaman_aktif(self, buku: dict, user_id: str) -> int:
        """Hitung jumlah peminjaman aktif user."""
        return sum(
            1 for item in buku.get('peminjaman_list', [])
            if item['user'] == user_id and item['status'] == 'aktif'
        )


# === Demo ===
if __name__ == "__main__":
    service = PeminjamanService()
    
    buku = {
        "judul": "Clean Code",
        "stok": 3,
        "peminjaman_list": [],
        "deadline": None
    }
    
    request = TransactionRequest(
        user_id="20230001",
        user_name="Andi",
        user_email="andi@uai.ac.id",
        membership=MembershipTier.REGULAR
    )
    
    # Test peminjaman
    result = service.pinjam_buku(buku, request)
    print(f"Peminjaman: {result}")
    print(f"Stok setelah pinjam: {buku['stok']}")
    
    # Test pengembalian
    result = service.kembalikan_buku(buku, request)
    print(f"Pengembalian: {result}")
    print(f"Stok setelah kembali: {buku['stok']}")
```

Jalankan untuk memverifikasi:

```bash
python exercises/clean_code.py
```

**Expected Output:**

```
INFO:perpustakaan:[EMAIL] To: andi@uai.ac.id, Subject: Peminjaman Buku
INFO:perpustakaan:20230001 meminjam 'Clean Code'
Peminjaman: {'status': 'ok', 'message': 'Berhasil pinjam', 'biaya': 5000}
Stok setelah pinjam: 2
INFO:perpustakaan:[EMAIL] To: andi@uai.ac.id, Subject: Pengembalian Buku
INFO:perpustakaan:20230001 mengembalikan 'Clean Code'
Pengembalian: {'status': 'ok', 'message': 'Berhasil kembalikan'}
Stok setelah kembali: 3
```

Buat tabel perbandingan sebelum dan sesudah refactoring:

```markdown
## Refactoring Summary

| Aspek | Sebelum | Sesudah |
|-------|---------|---------|
| Jumlah fungsi | 1 (God function) | 8+ (single responsibility) |
| Baris per fungsi | 80+ baris | 10-20 baris |
| Parameter | 7 (d, t, u, n, e, p, s) | Parameter Object |
| Naming | d, t, u | buku, transaction_type, user_id |
| Duplicate code | Email dan log duplikat | Extract ke class terpisah |
| Testability | Tidak bisa di-test | Setiap class bisa di-test mandiri |
| Nesting depth | 4 level | 1 level (guard clauses) |
```

**Estimasi waktu:** 25 menit

> **Diskusi kelas:** Apakah refactoring mengubah output program? Apa risiko refactoring tanpa automated test?

---

### Langkah 3: Setup Git Flow dan Feature Branch (10 menit)

**Mengapa:** Dalam tim, setiap developer bekerja di branch terpisah agar tidak mengganggu kode orang lain. Git Flow memberikan konvensi yang jelas tentang branch mana untuk apa.

**Instruksi:**

1. Setup branch develop:

```bash
# Pastikan di branch main dan up-to-date
git checkout main
git pull origin main

# Buat branch develop
git checkout -b develop
git push -u origin develop
```

2. Setiap anggota tim membuat feature branch masing-masing:

```bash
# Anggota 1:
git checkout -b feature/refactor-peminjaman

# Anggota 2:
git checkout -b feature/refactor-pencarian

# Anggota 3:
git checkout -b feature/refactor-notifikasi
```

3. Commit kode refactored di feature branch masing-masing menggunakan conventional commits:

```bash
# Contoh commit sequence yang baik:
git add exercises/smelly_code.py
git commit -m "docs: tambah kode sample dengan code smells untuk latihan"

git add exercises/smell-analysis.md
git commit -m "docs: tambah analisis code smells dari smelly_code.py"

git add exercises/clean_code.py
git commit -m "refactor: extract God function menjadi service classes terpisah"

git add exercises/clean_code.py
git commit -m "refactor: replace magic numbers dengan Enum dan Named Constants"

git add exercises/clean_code.py
git commit -m "refactor: replace nested conditionals dengan guard clauses"
```

**Expected Output:** Branch develop dan feature branches terbuat, kode ter-commit dengan conventional commits.

**Estimasi waktu:** 10 menit

---

### Langkah 4: Buat Pull Request (15 menit)

**Mengapa:** Pull Request (PR) adalah mekanisme utama kolaborasi di GitHub. PR memungkinkan code review sebelum kode masuk ke branch utama, mencegah bug dan menjaga kualitas kode.

**Instruksi:**

1. Push feature branch ke remote:

```bash
git push -u origin feature/refactor-peminjaman
```

2. Di GitHub, buat Pull Request:
   - **Base:** develop
   - **Compare:** feature/refactor-peminjaman
   - **Title:** mengikuti conventional commits: `refactor: extract dan perbaiki code smells di modul peminjaman`

3. Isi description PR dengan template berikut:

```markdown
## Deskripsi
Refactoring kode peminjaman buku untuk menghilangkan code smells
yang ditemukan di latihan Lab 07.

## Perubahan
- [x] Replace magic numbers dengan Enum (TransactionType, MembershipTier)
- [x] Extract God function menjadi service classes terpisah
- [x] Replace nested conditionals dengan guard clauses
- [x] Extract duplicate code (email, logging)
- [x] Rename variables agar deskriptif

## Code Smells yang Diperbaiki
| Smell | Teknik | File |
|-------|--------|------|
| Magic Number | Replace with Enum | clean_code.py:7-15 |
| God Function | Extract Method | clean_code.py:85-140 |
| Bad Naming | Rename Variable | Semua file |
| Duplicate Code | Extract Class | clean_code.py:50-65 |
| Nested Conditionals | Guard Clause | clean_code.py:95-105 |

## Cara Testing
1. Jalankan `python exercises/clean_code.py`
2. Verifikasi output sama dengan sebelum refactoring
3. Periksa bahwa tidak ada code smell baru

## Checklist
- [x] Kode mengikuti PEP 8
- [x] Conventional commits digunakan
- [x] Output tidak berubah (refactoring, bukan fitur baru)
```

4. Assign reviewer (anggota tim lain)

**Expected Output:** PR terbuat dengan deskripsi lengkap dan reviewer ter-assign.

**Estimasi waktu:** 15 menit

> **Tips:** PR yang baik memiliki deskripsi yang menjelaskan APA yang berubah, MENGAPA berubah, dan BAGAIMANA cara testing. Reviewer tidak harus membaca setiap baris diff jika deskripsi PR sudah jelas.

---

### Langkah 5: Code Review (20 menit)

**Mengapa:** Code review adalah quality gate terakhir sebelum kode masuk ke codebase bersama. Review bukan tentang menemukan kesalahan -- tetapi tentang learning, knowledge sharing, dan menjaga standar kode tim.

**Instruksi:**

Setiap anggota me-review PR anggota lain. Gunakan checklist review berikut:

```markdown
## Code Review Checklist

### Correctness (Kebenaran)
- [ ] Logika bisnis sudah benar?
- [ ] Edge cases ditangani (null, empty, boundary)?
- [ ] Error handling ada dan informative?

### Readability (Keterbacaan)
- [ ] Nama variabel dan fungsi deskriptif?
- [ ] Komentar/docstring ada untuk logika yang kompleks?
- [ ] Kode bisa dipahami tanpa penjelasan tambahan?

### Design (Desain)
- [ ] Single Responsibility Principle diikuti?
- [ ] Tidak ada code smell baru?
- [ ] DRY (Don't Repeat Yourself)?

### Style (Gaya)
- [ ] Mengikuti PEP 8?
- [ ] Formatting konsisten?
- [ ] Import terurut?

### Security (Keamanan)
- [ ] Tidak ada hardcoded password/secret?
- [ ] Input divalidasi?
- [ ] Tidak ada SQL injection / XSS potential?
```

**Cara memberikan review di GitHub:**

1. Buka PR partner di GitHub
2. Klik tab **"Files changed"**
3. Klik **"+"** di sebelah baris kode untuk menambah komentar
4. Tulis komentar yang **spesifik dan actionable**

**Contoh review comments yang BAIK:**

```markdown
### Comment 1 (Suggestion):
> Baris 45: `result['biaya'] = 5000`
Saran: Gunakan named constant `BIAYA_REGULAR = 5000` agar jelas
dan mudah diubah di satu tempat. Sekarang magic number masih ada.

### Comment 2 (Question):
> Baris 70: `except: pass`
Mengapa exception di-silent? Setidaknya log error-nya agar
bisa di-debug jika ada masalah. Saran: `except Exception as e: logger.error(e)`

### Comment 3 (Praise):
> Baris 85-90: Guard clause pattern
Bagus! Penggunaan guard clause di sini jauh lebih readable
dibanding nested if sebelumnya. Pola ini konsisten dengan clean code.

### Comment 4 (Nitpick):
> Baris 12: `from typing import Optional`
nit: Import ini belum digunakan di file ini. Hapus untuk kebersihan.
```

**Contoh review comments yang BURUK:**

```markdown
# BURUK - tidak spesifik
"Kode ini kurang bagus" -> BAGAIMANA kurang bagusnya? APA yang harus diubah?

# BURUK - tidak actionable
"Perlu diperbaiki" -> DIPERBAIKI bagaimana? Apa solusinya?

# BURUK - personal attack
"Siapa yang nulis kode seperti ini?" -> Fokus pada KODE, bukan ORANG
```

Berikan **minimal 3 review comments** yang konstruktif (1 suggestion, 1 question, 1 praise).

Setelah semua review selesai:
- Author memperbaiki kode berdasarkan feedback
- Reviewer approve PR
- Merge ke develop

```bash
# Setelah PR di-approve dan di-merge via GitHub:
git checkout develop
git pull origin develop
```

**Expected Output:** Setiap PR memiliki minimal 3 review comments, semua PR di-merge ke develop.

**Estimasi waktu:** 20 menit

> **Budaya Review:** Di perusahaan seperti Google, SETIAP perubahan kode harus di-review sebelum di-merge. Ini bukan tentang tidak percaya developer, tapi tentang knowledge sharing dan menjaga kualitas.

---

### Langkah 6: Refleksi dan Dokumentasi (10 menit)

**Mengapa:** Mendokumentasikan standar kode tim memastikan konsistensi sepanjang proyek. Tim yang punya coding standards tertulis menghasilkan kode yang lebih konsisten.

**Instruksi:**

Buat file `docs/coding-standards.md`:

```markdown
# Coding Standards - Tim [Nama Tim]

## Bahasa dan Framework
- Python 3.12+ dengan Flask
- Mengikuti PEP 8

## Naming Convention
- Variables/functions: snake_case (contoh: hitung_denda)
- Classes: PascalCase (contoh: BukuService)
- Constants: UPPER_SNAKE_CASE (contoh: MAX_LOAN_DAYS)
- File names: snake_case (contoh: buku_service.py)

## Git Workflow
- Branching: Git Flow (main, develop, feature/*)
- Commit messages: Conventional Commits
- Merge: via Pull Request dengan minimal 1 reviewer
- Branch protection: develop dan main dilindungi

## Code Review Rules
- Setiap PR harus di-review oleh minimal 1 anggota tim lain
- Reviewer memberikan minimal 1 suggestion dan 1 praise
- Author harus merespons semua komentar sebelum merge
- Tidak boleh merge PR sendiri tanpa review (kecuali hotfix)

## Definition of Done
- [ ] Kode mengikuti PEP 8
- [ ] Nama variabel dan fungsi deskriptif (tidak ada single-letter names)
- [ ] Tidak ada magic numbers
- [ ] Docstring ada untuk setiap class dan method publik
- [ ] Code review selesai (approved)
- [ ] Conventional commit digunakan
```

Commit:

```bash
git add docs/coding-standards.md exercises/
git commit -m "docs: tambah coding standards dan latihan refactoring"
git push origin develop
```

**Expected Output:** File coding standards dan semua exercise tersimpan di repository.

---

## Tantangan Tambahan

### Tantangan 1: Dasar
Cari **3 code smells tambahan** di kode proyek tim Anda sendiri (dari Lab 01-06). Dokumentasikan dan perbaiki dengan refactoring. Buat PR terpisah untuk setiap perbaikan.

### Tantangan 2: Menengah
Setup **branch protection rules** di GitHub repository tim. Konfigurasi: (a) require PR review sebelum merge ke develop, (b) require status checks to pass (jika sudah ada CI), (c) disallow force push ke main. Dokumentasikan langkah-langkah konfigurasi.

### Tantangan 3: Lanjutan
Buat **automated linting** menggunakan flake8 atau ruff. Buat file `.flake8` dengan konfigurasi tim, tambahkan script `lint.sh` yang menjalankan linter, dan demonstrasikan bagaimana linter bisa mendeteksi code smells secara otomatis. Integrasikan ke `pre-commit` hook Git sehingga kode yang melanggar standar tidak bisa di-commit.

---

## Refleksi & AI Usage Log

Sebelum meninggalkan lab, isi refleksi berikut di file `docs/refleksi-lab-07.md`:

1. **Code smell mana yang paling sulit diidentifikasi? Mengapa?**
2. **Apakah refactoring mengubah cara kerja program? Bagaimana Anda memastikannya?**
3. **Apa yang Anda pelajari dari menerima code review? Apakah ada feedback yang mengejutkan?**
4. **Mengapa conventional commits penting untuk kolaborasi tim?**
5. **Bagaimana pengalaman pertama kali melakukan code review? Apa yang sulit?**

Jika menggunakan AI selama lab, catat di **AI Usage Log**:

| Prompt yang Diberikan | Output AI | Modifikasi yang Dilakukan | Refleksi |
|----------------------|-----------|--------------------------|----------|
| (contoh prompt) | (ringkasan output) | (apa yang diubah) | (apa yang dipelajari) |

---

## Checklist Penyelesaian

- [ ] Minimal 8 code smells diidentifikasi di `exercises/smell-analysis.md`
- [ ] Kode di-refactor di `exercises/clean_code.py` dengan output yang sama
- [ ] Tabel perbandingan sebelum/sesudah refactoring didokumentasikan
- [ ] Branch `develop` dan minimal 1 `feature/*` branch dibuat
- [ ] Minimal 5 conventional commits tercatat
- [ ] Pull Request dibuat dengan deskripsi lengkap (perubahan, testing, checklist)
- [ ] Code review dilakukan: minimal 3 comments per PR (1 suggestion, 1 question, 1 praise)
- [ ] PR di-merge ke develop setelah review
- [ ] File `docs/coding-standards.md` tersimpan dengan standar tim
- [ ] File refleksi `docs/refleksi-lab-07.md` terisi

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
