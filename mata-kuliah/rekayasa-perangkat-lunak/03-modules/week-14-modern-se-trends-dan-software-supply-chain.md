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
| **CPMK** | CPMK-7: Merancang dan membangun web app end-to-end dalam tim Agile/Scrum dengan AI sebagai co-developer |
| **Sub-CPMK** | 14.1 Mengevaluasi risiko software supply chain dan strategi mitigasinya (C5) |
| | 14.2 Merancang pendekatan sustainable software engineering (C6) |
| | 14.3 Menganalisis tren modern SE dan implikasinya terhadap karier (C5) |
| **Durasi** | 150 menit (3 × 50 menit) |
| **Metode** | Ceramah interaktif, guest lecture simulation, industry trend analysis |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Mengevaluasi** risiko software supply chain dan memahami konsep SBOM (C5)
2. **Menganalisis** strategi dependency scanning dan vulnerability management (C5)
3. **Merancang** pendekatan green/sustainable software engineering (C6)
4. **Menganalisis** tren platform engineering, developer experience, dan masa depan SE (C5)
5. **Mengevaluasi** jalur karier software engineer di era AI (C5)

---

## Materi Pembelajaran

### 14.1 Software Supply Chain Security

Aplikasi modern bergantung pada ratusan *open-source dependencies*. Serangan melalui supply chain semakin meningkat.

```
Dependency Tree — Risiko Tersembunyi
┌────────────────┐
│  Aplikasi Kamu  │
├────────────────┤
│ express v4.18   │──┐
│ lodash v4.17    │  ├── Langsung (direct)
│ jsonwebtoken    │──┘
│   └── jws       │──┐
│   └── semver    │  ├── Tidak langsung (transitive)
│   └── ms        │──┘
│       └── ???   │ ← Kamu mungkin tidak tahu ada apa di sini!
└────────────────┘
```

#### Insiden Supply Chain Terkenal

| Insiden | Tahun | Dampak |
|---------|-------|--------|
| **Log4Shell** (Log4j) | 2021 | Jutaan server rentan, termasuk di Indonesia |
| **event-stream** | 2018 | Malware di npm package populer |
| **SolarWinds** | 2020 | 18.000+ organisasi terkompromi |
| **colors/faker** | 2022 | Maintainer sengaja merusak package sendiri |

#### SBOM — Software Bill of Materials

SBOM adalah **daftar lengkap** semua komponen (dependencies) dalam perangkat lunak — seperti daftar bahan pada kemasan makanan.

```
SBOM untuk Aplikasi E-Commerce UAI:
┌────────────────────────────────────────────────────┐
│ Komponen          │ Versi  │ Lisensi │ Kerentanan  │
├───────────────────┼────────┼─────────┼─────────────┤
│ flask             │ 3.0.0  │ BSD     │ Tidak ada   │
│ sqlalchemy        │ 2.0.25 │ MIT     │ Tidak ada   │
│ requests          │ 2.31.0 │ Apache  │ CVE-2024-XX │
│ pillow            │ 10.1.0 │ MIT     │ CVE-2024-YY │
│ jinja2            │ 3.1.3  │ BSD     │ Tidak ada   │
│ ...               │ ...    │ ...     │ ...         │
└────────────────────────────────────────────────────┘
```

#### Dependency Scanning Tools

| Tool | Platform | Fitur |
|------|----------|-------|
| **Dependabot** | GitHub (built-in) | Auto PR untuk update vulnerable deps |
| **Snyk** | Multi-platform | Scan + fix suggestions |
| **npm audit** | npm | `npm audit` dan `npm audit fix` |
| **pip-audit** | Python | `pip-audit` untuk cek vulnerability |
| **Trivy** | Container | Scan Docker image untuk CVE |

```bash
# Cek vulnerability di proyek Python
pip install pip-audit
pip-audit

# Cek vulnerability di proyek Node.js
npm audit
npm audit fix  # Auto-fix jika memungkinkan
```

### 14.2 Green / Sustainable Software Engineering

Software memiliki *carbon footprint* — dari data center yang mengkonsumsi listrik hingga perangkat pengguna.

```
Dampak Lingkungan dari Software:
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│ Data Center  │    │   Network    │    │    Device    │
│ (Cloud, GPU) │    │ (Transfer)   │    │ (CPU, RAM)   │
│  Energi ↑    │    │  Energi ↑    │    │  Energi ↑    │
│  Pendingin ↑ │    │  Bandwidth ↑ │    │  Baterai ↓   │
└──────────────┘    └──────────────┘    └──────────────┘
```

#### Prinsip Green Software Engineering

| Prinsip | Deskripsi | Praktik |
|---------|-----------|---------|
| **Energy Efficiency** | Kurangi konsumsi energi | Optimasi algoritma, lazy loading |
| **Carbon Awareness** | Perhatikan sumber energi | Deploy di region dengan energi terbarukan |
| **Hardware Efficiency** | Maksimalkan penggunaan hardware | Right-sizing server, auto-scaling |
| **Demand Shaping** | Sesuaikan beban kerja | Batch processing di off-peak hours |

```python
# Contoh: Optimasi query database
# BURUK — N+1 query problem (boros energi)
products = Product.query.all()
for product in products:
    print(product.category.name)  # Query per iterasi!

# BAIK — Eager loading (hemat energi)
products = Product.query.options(
    joinedload(Product.category)
).all()
for product in products:
    print(product.category.name)  # Tidak ada query tambahan
```

> **Nilai Islami — Khalifah (Penjaga Bumi):** Manusia adalah khalifah (pengelola) di bumi. Sustainable software engineering sejalan dengan prinsip Islam untuk tidak berbuat kerusakan di bumi (*fasad*) dan menjaga alam sebagai amanah dari Allah SWT.

### 14.3 Platform Engineering dan Developer Experience

#### Platform Engineering

Platform engineering membangun **Internal Developer Platform (IDP)** — infrastruktur self-service agar developer bisa deploy tanpa menunggu ops team.

```
Tanpa Platform Engineering:
  Developer → Tiket ke Ops → Tunggu → Deploy (berhari-hari)

Dengan Platform Engineering:
  Developer → Self-service platform → Deploy (menit)
```

#### Developer Experience (DevEx)

DevEx mengukur seberapa produktif dan puas developer dalam bekerja:

| Dimensi | Metrik | Contoh Perbaikan |
|---------|--------|-----------------|
| **Feedback Loops** | Waktu build, CI/CD speed | Cache dependencies, parallel jobs |
| **Cognitive Load** | Kompleksitas onboarding | Good docs, starter templates |
| **Flow State** | Interupsi, context switching | Deep work blocks, async communication |

### 14.4 Masa Depan Software Engineering

| Tren | Deskripsi | Timeline |
|------|-----------|----------|
| **AI-Native Development** | AI terintegrasi di setiap fase SDLC | Sekarang - 2026 |
| **Low-Code/No-Code** | Abstraksi semakin tinggi | Sekarang |
| **Edge Computing** | Komputasi dekat pengguna | 2025-2030 |
| **WebAssembly (Wasm)** | High-performance di browser | 2025-2028 |
| **Quantum-Ready Software** | Persiapan untuk quantum computing | 2028+ |

### 14.5 Jalur Karier Software Engineer

```
Entry-Level (0-2 tahun):
├── Junior Frontend Developer
├── Junior Backend Developer
├── Junior QA Engineer
└── Junior DevOps Engineer

Mid-Level (2-5 tahun):
├── Full-Stack Developer
├── Software Engineer
├── SRE (Site Reliability Engineer)
└── Security Engineer

Senior (5+ tahun):
├── Senior Software Engineer
├── Tech Lead
├── Staff Engineer
├── Engineering Manager
└── Solutions Architect

Spesialisasi:
├── AI/ML Engineer
├── Platform Engineer
├── Developer Advocate
└── CTO / VP Engineering
```

**Konteks Indonesia:** Ekosistem tech Indonesia berkembang pesat. Perusahaan seperti Gojek, Tokopedia, Traveloka, dan berbagai startup di kawasan BSD/SCBD membutuhkan software engineer yang kompeten di DevOps, cloud, dan AI.

---

## Kegiatan Pembelajaran

### Pre-class (15 menit)

- Jalankan `npm audit` atau `pip-audit` pada proyek kelompok dan catat hasilnya
- Baca: "Principles of Green Software Engineering" dari Green Software Foundation
- Refleksi: "Di mana kamu ingin berkarier 5 tahun dari sekarang?"

### In-class (120 menit)

| Waktu | Aktivitas | Metode |
|-------|-----------|--------|
| 0-30 menit | Software supply chain security, SBOM, insiden | Ceramah + diskusi |
| 30-50 menit | Dependency scanning demo + hands-on audit proyek | Demo + hands-on |
| 50-55 menit | *Break* | — |
| 55-75 menit | Green software engineering — prinsip dan praktik | Ceramah + contoh |
| 75-95 menit | Guest lecture simulation: "Sehari Menjadi Software Engineer di Startup Indonesia" | Simulasi + diskusi |
| 95-115 menit | Industry trend analysis: setiap kelompok presentasi 1 tren yang paling relevan untuk proyek mereka | Presentasi kelompok |
| 115-120 menit | Karier SE, wrap-up, persiapan presentasi Minggu 15 | Diskusi kelas |

### Post-class (15 menit)

- Persiapkan presentasi proyek akhir untuk Minggu 15
- Lengkapi dependency audit dan perbaiki vulnerability jika ada
- Finalisasi AI Usage Log untuk dilampirkan dalam laporan proyek

---

## Referensi

1. OWASP. (2023). *Software Component Verification Standard (SCVS)*. [owasp.org](https://owasp.org/)
2. Green Software Foundation. (2023). *Software Carbon Intensity Specification*. [greensoftware.foundation](https://greensoftware.foundation/)
3. Forsgren, N. et al. (2018). *Accelerate: The Science of Lean Software and DevOps*. IT Revolution.
4. The Linux Foundation. (2023). *SBOM Everywhere*. [linuxfoundation.org](https://www.linuxfoundation.org/)
5. Pressman, R. S. & Maxim, B. R. (2020). *Software Engineering*, 9th ed. Chapter 30-31.
6. Stack Overflow. (2024). *Developer Survey 2024*. [survey.stackoverflow.co](https://survey.stackoverflow.co/)

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
