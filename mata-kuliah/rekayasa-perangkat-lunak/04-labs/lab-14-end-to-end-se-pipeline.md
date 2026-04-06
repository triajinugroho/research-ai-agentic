# Lab 14: End-to-End SE Pipeline

## Informasi Lab

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak (IF2205) |
| **Lab** | 13 dari 13 (Minggu 14) |
| **Topik** | Full SDLC in One Session: Requirement → Deploy |
| **CPMK** | CPMK-7 |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |

## Tujuan

1. **Mendemonstrasikan** seluruh SDLC dalam satu sesi untuk satu mini-feature
2. **Mengintegrasikan** requirements, design, implementation, testing, dan deployment

## Langkah-langkah

### Langkah 1: Requirement & User Story (10 menit)
Pilih mini-feature baru:
```
User Story: "As a mahasiswa, I want melihat riwayat peminjaman saya,
so that saya tahu buku apa saja yang pernah saya pinjam"

Acceptance Criteria:
Given mahasiswa sudah login
When mahasiswa membuka halaman /riwayat
Then sistem menampilkan daftar peminjaman (judul, tanggal, status)
```

### Langkah 2: Design (10 menit)
- Sequence Diagram (sketch):
  Browser → Controller → Service → Database → return list
- API: `GET /api/peminjaman/riwayat`
- Response: `[{judul, tanggal_pinjam, status}, ...]`

### Langkah 3: Implementation (30 menit)
```python
# Backend
@buku_bp.route('/api/peminjaman/riwayat')
@login_required
def riwayat():
    data = Peminjaman.query.filter_by(user_id=current_user.id).all()
    return jsonify([{
        'judul': p.buku.judul,
        'tanggal': p.tanggal_pinjam.isoformat(),
        'status': p.status
    } for p in data])
```

```html
<!-- Frontend: riwayat.html -->
<h1>Riwayat Peminjaman</h1>
<table id="riwayat-table">
  <tr><th>Judul</th><th>Tanggal</th><th>Status</th></tr>
</table>
<script>
fetch('/api/peminjaman/riwayat')
  .then(r => r.json())
  .then(data => {
    const table = document.getElementById('riwayat-table');
    data.forEach(p => {
      table.innerHTML += `<tr><td>${p.judul}</td><td>${p.tanggal}</td><td>${p.status}</td></tr>`;
    });
  });
</script>
```

### Langkah 4: Testing (15 menit)
```python
def test_riwayat_empty(client, auth):
    auth.login()
    resp = client.get('/api/peminjaman/riwayat')
    assert resp.status_code == 200
    assert resp.json == []

def test_riwayat_with_data(client, auth, sample_peminjaman):
    auth.login()
    resp = client.get('/api/peminjaman/riwayat')
    assert len(resp.json) == 1
```

### Langkah 5: CI/CD & Deploy (15 menit)
```bash
git checkout -b feature/riwayat
git add .
git commit -m "feat(riwayat): tambah halaman riwayat peminjaman"
git push -u origin feature/riwayat
# Buat PR → CI pipeline jalan → review → merge → auto-deploy
```

### Langkah 6: Verifikasi (10 menit)
- Buka URL production → test fitur riwayat
- Cek CI pipeline hijau
- Cek test coverage masih ≥ 70%

## Tantangan Tambahan

1. Tambahkan fitur filter riwayat by status (dipinjam/dikembalikan)
2. Ukur waktu total dari requirement → deploy

## Checklist Penyelesaian

- [ ] User story + acceptance criteria tertulis
- [ ] Design (API + sequence) ter-sketch
- [ ] Backend + frontend implemented
- [ ] Tests pass
- [ ] CI pipeline hijau
- [ ] Deployed dan bisa diakses

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
