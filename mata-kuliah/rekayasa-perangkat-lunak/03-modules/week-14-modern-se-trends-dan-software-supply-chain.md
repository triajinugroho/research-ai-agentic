# Minggu 14: Modern SE Trends dan Software Supply Chain

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak |
| **Kode** | IF2205 |
| **Minggu** | 14 dari 16 |
| **Topik** | Modern SE Trends dan Software Supply Chain |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **Bahasa Pemrograman** | Python 3.x + JavaScript |
| **CPMK** | CPMK-7: Merancang dan membangun web app end-to-end dalam tim Agile/Scrum dengan AI sebagai co-developer secara bertanggung jawab |
| **Sub-CPMK** | Sub-CPMK-7.3: Mengevaluasi tren modern SE (supply chain security, green software, platform engineering) (C5) |
| | Sub-CPMK-7.4: Merancang roadmap pengembangan karir sebagai software engineer (C6) |
| **Durasi** | 150 menit (3 x 50 menit) |
| **Metode** | Ceramah interaktif, guest lecture simulation, industry trend analysis, career planning |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Mengevaluasi** risiko software supply chain dan memahami konsep SBOM serta SCA (C5)
2. **Menganalisis** strategi dependency scanning dan vulnerability management dengan tools aktual (C4)
3. **Merancang** pendekatan green/sustainable software engineering (C6)
4. **Menganalisis** tren platform engineering, developer experience, dan masa depan SE (C5)
5. **Merancang** roadmap pengembangan karir sebagai software engineer di Indonesia (C6)

---

## Materi Pembelajaran

### 14.1 Software Supply Chain Security

Aplikasi modern bergantung pada ratusan *open-source dependencies*. Serangan melalui supply chain semakin meningkat -- analogi: Anda membangun rumah dengan 200 bahan bangunan dari supplier berbeda, satu bahan cacat bisa meruntuhkan seluruh bangunan.

```
Dependency Tree -- Risiko Tersembunyi:
+--------------------+
|  Aplikasi Kamu     |
+--------------------+
| express v4.18      |--+
| lodash v4.17       |  +-- Langsung (direct dependencies)
| jsonwebtoken v9    |--+
|   +-- jws v3.2     |--+
|   +-- semver v7.5  |  +-- Tidak langsung (transitive)
|   +-- ms v2.1      |--+
|       +-- ???       | <-- Kamu mungkin tidak tahu ada apa di sini!
+--------------------+

Fakta:
+-- Rata-rata aplikasi Node.js punya 300-1000+ dependencies
+-- ~80% kode di aplikasi modern berasal dari open-source
+-- 1 dependency rusak = seluruh aplikasi berisiko
```

#### Insiden Supply Chain Terkenal

| Insiden | Tahun | Apa yang Terjadi | Dampak |
|---------|-------|-----------------|--------|
| **Log4Shell** (Log4j) | 2021 | Vulnerability di library logging Java | Jutaan server rentan, termasuk server di Indonesia |
| **event-stream** | 2018 | Maintainer baru menyisipkan malware di npm package | Crypto wallet dicuri |
| **SolarWinds** | 2020 | Build system di-compromise, malware masuk ke update resmi | 18.000+ organisasi terkompromi |
| **colors/faker** | 2022 | Maintainer sengaja merusak package sendiri (protes) | Ribuan aplikasi terganggu |
| **ua-parser-js** | 2021 | npm package dibajak, di-inject crypto miner | 8 juta unduhan/minggu teraffect |

**Konteks Indonesia:**
- **Log4Shell**: Banyak instansi pemerintah dan perbankan Indonesia yang menggunakan Java enterprise apps rentan terhadap Log4Shell. BSSN mengeluarkan peringatan darurat.
- **Supply chain awareness** di startup Indonesia masih rendah -- banyak yang tidak rutin menjalankan `npm audit` atau `pip-audit`.

#### SBOM -- Software Bill of Materials

SBOM adalah **daftar lengkap** semua komponen (dependencies) dalam perangkat lunak -- seperti daftar bahan pada kemasan makanan yang diawasi BPOM.

```
SBOM untuk Aplikasi Toko UMKM:
+--------------+--------+---------+-------------+---------+
| Komponen     | Versi  | Lisensi | Kerentanan  | Sumber  |
+--------------+--------+---------+-------------+---------+
| flask        | 3.0.0  | BSD     | Tidak ada   | PyPI    |
| sqlalchemy   | 2.0.25 | MIT     | Tidak ada   | PyPI    |
| requests     | 2.31.0 | Apache  | CVE-2024-XX | PyPI    |
| pillow       | 10.1.0 | MIT     | CVE-2024-YY | PyPI    |
| jinja2       | 3.1.3  | BSD     | Tidak ada   | PyPI    |
| gunicorn     | 21.2.0 | MIT     | Tidak ada   | PyPI    |
| werkzeug     | 3.0.1  | BSD     | Tidak ada   | PyPI    |
+--------------+--------+---------+-------------+---------+

Regulasi SBOM:
+-- US Executive Order 14028 (2021): software untuk pemerintah WAJIB punya SBOM
+-- EU Cyber Resilience Act (2024): produk digital di EU wajib SBOM
+-- Indonesia: belum ada regulasi formal, tapi BSSN mulai mendorong
```

#### SCA -- Software Composition Analysis

SCA adalah proses otomatis untuk menganalisis dependencies di proyek kita:

```
Alur SCA dalam CI/CD:
+----------+    +----------+    +----------+    +----------+
| Developer|    | Git Push |    | CI/CD    |    | SCA Scan |
| menambah |    | ke repo  |    | pipeline |    | cek deps |
| library  |--->|          |--->|          |--->|          |
+----------+    +----------+    +----------+    +----+-----+
                                                     |
                                              +------v------+
                                              | Vulnerable? |
                                              +------+------+
                                                     |
                                          +----------+----------+
                                          |                     |
                                     +----v----+          +----v----+
                                     | PASS    |          | FAIL    |
                                     | (aman)  |          | (block) |
                                     +---------+          +---------+
```

#### Dependency Scanning Tools

| Tool | Platform | Fitur | Gratis? |
|------|----------|-------|---------|
| **Dependabot** | GitHub (built-in) | Auto PR untuk update vulnerable deps | Ya |
| **Snyk** | Multi-platform | Scan + fix suggestions + monitoring | Free tier |
| **npm audit** | npm | Scan dan auto-fix npm packages | Ya |
| **pip-audit** | Python | Cek vulnerability di pip packages | Ya |
| **Trivy** | Container | Scan Docker image untuk CVE | Ya |
| **OWASP Dependency-Check** | Multi | Scan dependencies vs NVD database | Ya |

```bash
# ===== Python: pip-audit =====
pip install pip-audit
pip-audit
# Output contoh:
# Name     Version  ID           Fix Versions
# requests 2.31.0   PYSEC-2024-XX  2.32.0
#
# Found 1 vulnerability

# Fix:
pip install requests==2.32.0  # Upgrade ke versi aman

# ===== Node.js: npm audit =====
npm audit
# Output contoh:
# 3 vulnerabilities (1 moderate, 2 high)
#
# To fix:
npm audit fix                  # Auto-fix yang aman
npm audit fix --force          # Fix semua (mungkin breaking)

# ===== Docker: Trivy =====
# Scan Docker image untuk CVE
trivy image toko-umkm:latest
# Output: daftar CVE di base image dan packages
```

```python
# Contoh: Script sederhana untuk cek dependencies
import subprocess
import json

def audit_python_deps():
    """Jalankan pip-audit dan parse hasilnya."""
    result = subprocess.run(
        ["pip-audit", "--format=json", "--output=-"],
        capture_output=True, text=True
    )
    
    if result.returncode == 0:
        print("Semua dependencies aman!")
        return []
    
    try:
        vulns = json.loads(result.stdout)
        print(f"Ditemukan {len(vulns)} vulnerability:")
        for v in vulns:
            print(f"  - {v['name']} {v['version']}: {v['id']}")
            if v.get('fix_versions'):
                print(f"    Fix: upgrade ke {v['fix_versions'][0]}")
        return vulns
    except json.JSONDecodeError:
        print("Tidak bisa parse output pip-audit")
        return []

# Jalankan audit
vulnerabilities = audit_python_deps()
```

#### Dependabot Configuration

```yaml
# .github/dependabot.yml
# Konfigurasi Dependabot untuk auto-update dependencies

version: 2
updates:
  # Python pip dependencies
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"      # Cek setiap minggu
    open-pull-requests-limit: 5
    labels:
      - "dependencies"
      - "security"
    
  # Node.js npm dependencies
  - package-ecosystem: "npm"
    directory: "/frontend"
    schedule:
      interval: "weekly"
    
  # GitHub Actions versions
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "monthly"
```

```
Alur Dependabot:
1. Dependabot scan dependencies setiap minggu
2. Jika ada versi baru / vulnerability fix:
   --> Dependabot buat PR otomatis
   --> CI/CD jalankan test
   --> Jika test pass, developer tinggal merge
3. Tidak perlu cek manual!

Contoh PR dari Dependabot:
+--------------------------------------------------+
| Bump flask from 3.0.0 to 3.0.2                  |
| Fixes CVE-2024-XXXXX (moderate severity)          |
| +-- Changelog: [link]                             |
| +-- Compatibility: [verified]                     |
| +-- CI: All checks passed                         |
+--------------------------------------------------+
```

### 14.2 Green / Sustainable Software Engineering

Software memiliki *carbon footprint* -- dari data center yang mengkonsumsi listrik hingga perangkat pengguna. Industri ICT menyumbang **2-4% emisi CO2 global** -- setara dengan industri penerbangan.

```
Dampak Lingkungan dari Software:
+--------------+    +--------------+    +--------------+
| Data Center  |    |   Network    |    |    Device    |
| (Cloud, GPU) |    | (Transfer)   |    | (CPU, RAM)   |
| Energi +++   |    |  Energi ++   |    |  Energi +    |
| Pendingin +++|    |  Bandwidth   |    |  Baterai     |
+--------------+    +--------------+    +--------------+
       |                  |                    |
       v                  v                    v
   +-------------------------------------------------+
   |          Total Carbon Footprint Software         |
   |    ICT = 2-4% emisi CO2 global (= penerbangan)  |
   +-------------------------------------------------+
```

#### Prinsip Green Software Engineering (GSF)

| Prinsip | Deskripsi | Praktik Konkret |
|---------|-----------|-----------------|
| **Energy Efficiency** | Kurangi konsumsi energi | Optimasi algoritma, lazy loading, efisiensi query |
| **Carbon Awareness** | Perhatikan sumber energi | Deploy di region dengan energi terbarukan |
| **Hardware Efficiency** | Maksimalkan penggunaan hardware | Right-sizing server, auto-scaling |
| **Demand Shaping** | Sesuaikan beban kerja | Batch processing di off-peak hours |

```python
# Contoh: Optimasi query database -- hemat energi
from sqlalchemy.orm import joinedload

# BURUK -- N+1 query problem (boros energi, boros bandwidth)
# Jika ada 100 produk, ini menghasilkan 101 query!
products = Product.query.all()
for product in products:
    print(product.category.name)  # +1 query per iterasi!

# BAIK -- Eager loading (hemat energi, 1 query saja)
products = Product.query.options(
    joinedload(Product.category)
).all()
for product in products:
    print(product.category.name)  # Tidak ada query tambahan

# Perbandingan:
# N+1: 101 queries x ~5ms = ~505ms, bandwidth tinggi
# Eager: 1 query x ~15ms = ~15ms, bandwidth rendah
# Hemat: 97% lebih efisien!
```

```python
# Contoh: Lazy loading gambar untuk hemat bandwidth
# (Frontend JavaScript, tapi konsep penting)

# BURUK -- load semua gambar sekaligus
# <img src="produk-batik-1.jpg" />   <!-- 2MB -->
# <img src="produk-batik-2.jpg" />   <!-- 1.5MB -->
# Total: 3.5MB langsung di-load, meski user belum scroll

# BAIK -- lazy loading
# <img src="produk-batik-1.jpg" loading="lazy" />
# Gambar hanya di-load saat mendekati viewport
# Hemat bandwidth = hemat energi network + device
```

```python
# Contoh: Caching untuk mengurangi beban server
from functools import lru_cache

# BURUK -- hitung ulang setiap request
def get_kategori_populer():
    """Query database setiap kali dipanggil."""
    return db.session.execute(
        "SELECT kategori, COUNT(*) as total "
        "FROM produk GROUP BY kategori ORDER BY total DESC"
    ).fetchall()

# BAIK -- cache hasilnya (hemat CPU + DB)
@lru_cache(maxsize=1)
def get_kategori_populer_cached():
    """Cache hasil query selama 5 menit."""
    return db.session.execute(
        "SELECT kategori, COUNT(*) as total "
        "FROM produk GROUP BY kategori ORDER BY total DESC"
    ).fetchall()

# Atau gunakan Redis cache:
import redis
cache = redis.Redis()

def get_kategori_populer_redis():
    """Cache di Redis dengan TTL 5 menit."""
    cached = cache.get("kategori_populer")
    if cached:
        return json.loads(cached)  # Tidak perlu query DB
    
    result = query_database()
    cache.setex("kategori_populer", 300, json.dumps(result))
    return result
```

**Konteks Indonesia:**
- Indonesia masih bergantung pada energi fosil (~60% pembangkit listrik). Software engineer yang membuat kode efisien secara langsung mengurangi konsumsi listrik data center.
- Gojek melaporkan bahwa optimasi backend mereka menghemat jutaan rupiah per bulan dalam biaya cloud computing.

### 14.3 Platform Engineering dan Developer Experience

#### Platform Engineering

Platform engineering membangun **Internal Developer Platform (IDP)** -- infrastruktur self-service agar developer bisa deploy tanpa menunggu ops team.

```
Tanpa Platform Engineering:
  Developer --> Tiket ke Ops --> Tunggu 2-3 hari --> Deploy
  
Dengan Platform Engineering:
  Developer --> Self-service platform --> Deploy (menit)

Contoh IDP:
+----------------------------------------------------+
|            Internal Developer Platform               |
|                                                     |
|  +-------------+  +------------+  +--------------+  |
|  | Template    |  | CI/CD      |  | Monitoring   |  |
|  | Generator   |  | Self-serve |  | Dashboard    |  |
|  | (new app)   |  | (1-click)  |  | (auto-setup) |  |
|  +-------------+  +------------+  +--------------+  |
|                                                     |
|  +-------------+  +------------+  +--------------+  |
|  | Database    |  | Secret     |  | Logging      |  |
|  | Provisioning|  | Management |  | Aggregation  |  |
|  | (self-serve)|  | (Vault)    |  | (ELK/Loki)   |  |
|  +-------------+  +------------+  +--------------+  |
+----------------------------------------------------+
```

**Konteks Indonesia:**
- **Gojek**: Memiliki internal platform "Turing" untuk deploy microservices secara self-service
- **Tokopedia**: Platform team membangun tools internal untuk mempercepat developer onboarding

#### Developer Experience (DevEx)

DevEx mengukur seberapa produktif dan puas developer dalam bekerja. Tiga dimensi utama:

| Dimensi | Metrik | Contoh Perbaikan |
|---------|--------|-----------------|
| **Feedback Loops** | Waktu build, CI/CD speed | Cache dependencies, parallel jobs |
| **Cognitive Load** | Kompleksitas onboarding | Good docs, starter templates, conventions |
| **Flow State** | Interupsi, context switching | Deep work blocks, async communication |

```
DevEx Score -- Self Assessment:
+---------------------+-------+-------+-------+-------+-------+
| Dimensi             |   1   |   2   |   3   |   4   |   5   |
+---------------------+-------+-------+-------+-------+-------+
| CI/CD speed         |       |       |   X   |       |       |
| Documentation       |       |   X   |       |       |       |
| Onboarding ease     |       |       |       |   X   |       |
| Tool availability   |       |       |       |       |   X   |
| Meeting overhead    |   X   |       |       |       |       |
+---------------------+-------+-------+-------+-------+-------+
1=Buruk  5=Sangat Baik
```

### 14.4 Tren Modern SE Lainnya

| Tren | Deskripsi | Status | Relevansi Indonesia |
|------|-----------|--------|-------------------|
| **AI-Native Development** | AI terintegrasi di setiap fase SDLC | Sekarang | Tinggi -- startup mulai adopt |
| **Low-Code/No-Code** | Abstraksi semakin tinggi | Sekarang | Tinggi -- UMKM digitalisasi |
| **Edge Computing** | Komputasi dekat pengguna | 2025-2030 | Sedang -- IoT growing |
| **WebAssembly (Wasm)** | High-performance di browser | 2025-2028 | Sedang |
| **Quantum-Ready Software** | Persiapan untuk quantum computing | 2028+ | Rendah (jangka panjang) |
| **Shift-Left Security** | Security dari awal SDLC, bukan akhir | Sekarang | Tinggi -- regulasi OJK |

```python
# Contoh: Shift-Left Security -- validasi input sejak awal
from dataclasses import dataclass
import re

@dataclass
class InputValidator:
    """Validasi input di awal (shift-left) untuk cegah vulnerability."""
    
    @staticmethod
    def sanitize_string(value: str, max_length: int = 255) -> str:
        """Sanitize string input -- cegah XSS dan injection."""
        if not isinstance(value, str):
            raise ValueError("Input harus berupa string")
        # Trim dan batasi panjang
        value = value.strip()[:max_length]
        # Escape karakter berbahaya
        value = value.replace("<", "&lt;").replace(">", "&gt;")
        return value
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """Validasi format email."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def validate_phone_id(phone: str) -> bool:
        """Validasi nomor telepon Indonesia."""
        # Format: +62xxx atau 08xxx
        pattern = r'^(\+62|62|0)8[1-9][0-9]{7,11}$'
        return bool(re.match(pattern, phone))

# Penggunaan
validator = InputValidator()
nama = validator.sanitize_string("<script>alert('xss')</script>Budi")
print(nama)  # &lt;script&gt;alert('xss')&lt;/script&gt;Budi

print(validator.validate_email("budi@uai.ac.id"))   # True
print(validator.validate_phone_id("081234567890"))   # True
print(validator.validate_phone_id("+6281234567890")) # True
```

### 14.5 Sertifikasi dan Jalur Karir Software Engineer

```
Jalur Karir Software Engineer:
Entry-Level (0-2 tahun):
+-- Junior Frontend Developer
+-- Junior Backend Developer
+-- Junior QA Engineer
+-- Junior DevOps Engineer

Mid-Level (2-5 tahun):
+-- Full-Stack Developer
+-- Software Engineer
+-- SRE (Site Reliability Engineer)
+-- Security Engineer

Senior (5+ tahun):
+-- Senior Software Engineer
+-- Tech Lead
+-- Staff Engineer
+-- Engineering Manager
+-- Solutions Architect

Spesialisasi:
+-- AI/ML Engineer
+-- Platform Engineer
+-- Developer Advocate
+-- CTO / VP Engineering
```

#### Gaji dan Demand di Indonesia (2025)

| Level | Gaji Bulanan (Jakarta) | Demand |
|-------|----------------------|--------|
| Junior (0-2 th) | Rp 5-12 juta | Tinggi |
| Mid (2-5 th) | Rp 12-25 juta | Sangat Tinggi |
| Senior (5+ th) | Rp 25-50+ juta | Tinggi |
| Tech Lead | Rp 35-70+ juta | Sedang-Tinggi |
| Staff/Principal | Rp 50-100+ juta | Rendah (langka) |

**Sumber: Glints, Kalibrr, Stack Overflow Developer Survey 2024*

#### Sertifikasi yang Relevan

| Sertifikasi | Vendor | Level | Biaya | Relevansi |
|-------------|--------|-------|-------|-----------|
| **AWS Cloud Practitioner** | Amazon | Entry | ~$100 | Tinggi |
| **Google Associate Cloud Engineer** | Google | Mid | ~$200 | Tinggi |
| **Certified Kubernetes Administrator** | CNCF | Mid-Senior | ~$395 | Sedang |
| **ISTQB Foundation** | ISTQB | Entry | ~$250 | Untuk QA path |
| **Certified ScrumMaster** | Scrum Alliance | Entry-Mid | ~$500 | Untuk PM path |
| **GitHub Certification** | GitHub | Entry | $99 | Tinggi |

```python
# Contoh: Personal career roadmap planner
from dataclasses import dataclass, field
from typing import List

@dataclass
class CareerMilestone:
    tahun: int
    target: str
    skills: List[str]
    sertifikasi: str = ""
    
@dataclass
class CareerRoadmap:
    nama: str
    goal: str
    milestones: List[CareerMilestone] = field(default_factory=list)
    
    def tampilkan(self):
        print(f"Career Roadmap: {self.nama}")
        print(f"Goal: {self.goal}\n")
        for m in self.milestones:
            print(f"  Tahun {m.tahun}: {m.target}")
            print(f"    Skills: {', '.join(m.skills)}")
            if m.sertifikasi:
                print(f"    Sertifikasi: {m.sertifikasi}")
            print()

# Contoh roadmap lulusan UAI
roadmap = CareerRoadmap(
    nama="Ahmad (Lulusan Informatika UAI 2027)",
    goal="Senior Full-Stack Engineer dalam 5 tahun",
    milestones=[
        CareerMilestone(
            2027, "Junior Backend Developer di startup Jakarta",
            ["Python/Flask", "PostgreSQL", "Docker", "Git"],
            "GitHub Certification"
        ),
        CareerMilestone(
            2028, "Mid-Level Full-Stack Developer",
            ["React/Next.js", "TypeScript", "CI/CD", "AWS"],
            "AWS Cloud Practitioner"
        ),
        CareerMilestone(
            2030, "Senior Software Engineer",
            ["System Design", "Microservices", "Leadership"],
            "AWS Solutions Architect"
        ),
        CareerMilestone(
            2032, "Tech Lead / Staff Engineer",
            ["Architecture", "Mentoring", "Cross-team collaboration"],
            ""
        ),
    ]
)

roadmap.tampilkan()
```

**Ekosistem Tech Indonesia:**
- **Unicorn/Decacorn**: GoTo (Gojek+Tokopedia), Traveloka, Bukalapak, OVO/Dana
- **Startup hub**: Jakarta (SCBD, Sudirman), Bandung (ITB area), Yogyakarta
- **Remote work**: Semakin banyak perusahaan Indonesia yang menerima remote -- peluang bagi lulusan di luar Jakarta
- **Komunitas**: GDG (Google Developer Groups), JakartaJS, Python ID, Flutter ID, DevOps Indonesia

> **Nilai Islami -- Khalifah (Penjaga Bumi):** Manusia adalah khalifah (pengelola) di bumi. Sustainable software engineering sejalan dengan prinsip Islam untuk tidak berbuat kerusakan di bumi (*la tufsidu fil ardh*) dan menjaga alam sebagai amanah dari Allah SWT. Seorang software engineer Muslim tidak hanya bertanggung jawab membuat software yang berfungsi, tetapi juga yang efisien dan ramah lingkungan.

---

## Kegiatan Pembelajaran

### Pre-class (20 menit)

- Jalankan `npm audit` atau `pip-audit` pada proyek kelompok dan catat hasilnya
- Baca: "Principles of Green Software Engineering" dari Green Software Foundation ([greensoftware.foundation](https://greensoftware.foundation/))
- Setup Dependabot di repo proyek kelompok (buat file `.github/dependabot.yml`)
- Refleksi tertulis: "Di mana kamu ingin berkarir 5 tahun dari sekarang? Skill apa yang perlu dikembangkan?"

### In-class (110 menit)

| Waktu | Aktivitas | Metode |
|-------|-----------|--------|
| 0-25 menit | Software supply chain security, SBOM, SCA, insiden terkenal | Ceramah + diskusi |
| 25-45 menit | Dependency scanning demo: pip-audit, npm audit, Dependabot setup | Demo + hands-on |
| 45-50 menit | *Break* | -- |
| 50-70 menit | Green software engineering -- prinsip GSF, optimasi kode, contoh Indonesia | Ceramah + code example |
| 70-90 menit | Guest lecture simulation: "Sehari Menjadi Software Engineer di Startup Indonesia" -- presentasi dosen tentang realita industri | Simulasi + diskusi |
| 90-105 menit | Industry trend analysis: setiap kelompok presentasi 1 tren yang paling relevan untuk proyek mereka (5 menit per kelompok) | Presentasi kelompok |
| 105-110 menit | Karir SE di Indonesia, sertifikasi, roadmap, persiapan presentasi Minggu 15 | Diskusi kelas |

### Post-class (20 menit)

- Persiapkan presentasi proyek akhir untuk Minggu 15 (slide, demo environment, backup video)
- Lengkapi dependency audit dan perbaiki vulnerability jika ada: `npm audit fix` atau upgrade versions
- Finalisasi AI Usage Log untuk dilampirkan dalam laporan proyek
- Buat draft personal career roadmap (1 halaman, 5 tahun ke depan)
- Finalisasi Sprint 4 proyek kelompok

---

## Latihan & Diskusi

### Soal 1 (C2 -- Memahami)
Jelaskan apa itu SBOM (Software Bill of Materials) dan mengapa semakin penting di era modern. Berikan analogi dengan industri makanan (label BPOM) untuk menjelaskan konsep ini kepada non-teknis.

### Soal 2 (C4 -- Menganalisis)
Proyek kelompok Anda memiliki dependencies berikut di `requirements.txt`:
```
flask==2.3.0
sqlalchemy==1.4.49
requests==2.28.0
pillow==9.5.0
```
Jelaskan langkah-langkah untuk:
a) Mengidentifikasi apakah ada vulnerability (tools dan commands)
b) Memprioritaskan mana yang harus di-update lebih dulu
c) Memastikan update tidak merusak aplikasi yang sudah berjalan
d) Mengkonfigurasi Dependabot agar otomatis memantau ke depan

### Soal 3 (C5 -- Mengevaluasi)
Evaluasi trade-off antara dua pendekatan berikut untuk mengurangi carbon footprint aplikasi web:
a) Optimasi kode backend (N+1 query fix, caching, efisiensi algoritma)
b) Pindah ke cloud provider yang menggunakan 100% energi terbarukan tapi lebih mahal 30%

Pertimbangkan: biaya, effort, dampak lingkungan, dan feasibility untuk startup Indonesia.

### Soal 4 (C6 -- Mencipta)
Buatlah personal career roadmap 5 tahun sebagai software engineer. Sertakan:
- Target posisi per tahun
- Skills yang perlu dikembangkan
- Sertifikasi yang akan diambil (minimal 2)
- Kontribusi ke komunitas (open-source, tech talks, mentoring)
- Bagaimana nilai-nilai Islam akan Anda integrasikan dalam karir SE

### Soal 5 (C5 -- Mengevaluasi)
Bandingkan konsep "Shift-Left Security" dengan pendekatan tradisional di mana security testing dilakukan di akhir SDLC. Berikan 3 contoh konkret bagaimana shift-left security diterapkan dalam proyek kelompok IF2205 (dari requirements sampai deployment).

---

## Referensi

1. OWASP. (2023). *Software Component Verification Standard (SCVS)*. [owasp.org](https://owasp.org/)
2. Green Software Foundation. (2023). *Software Carbon Intensity Specification*. [greensoftware.foundation](https://greensoftware.foundation/)
3. Forsgren, N. et al. (2018). *Accelerate: The Science of Lean Software and DevOps*. IT Revolution.
4. The Linux Foundation. (2023). *SBOM Everywhere*. [linuxfoundation.org](https://www.linuxfoundation.org/)
5. Pressman, R. S. & Maxim, B. R. (2020). *Software Engineering*, 9th ed. Chapter 30-31.
6. Stack Overflow. (2024). *Developer Survey 2024*. [survey.stackoverflow.co](https://survey.stackoverflow.co/)
7. GitHub. (2024). *Dependabot documentation*. [docs.github.com](https://docs.github.com/en/code-security/dependabot)
8. Sommerville, I. (2016). *Software Engineering*, 10th ed. Pearson. Chapter 26.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* -- Program Studi Informatika, Universitas Al Azhar Indonesia
