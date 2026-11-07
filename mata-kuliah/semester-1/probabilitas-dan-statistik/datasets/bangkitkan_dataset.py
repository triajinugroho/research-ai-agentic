"""Pembangkit dataset latihan — Probabilitas dan Statistik (IF52510033).

Seluruh berkas yang dihasilkan skrip ini SINTETIS: dibangkitkan dengan
numpy dari seed tetap, meniru pola yang wajar untuk konteks Indonesia,
dan BUKAN statistik resmi. Dipakai untuk latihan teknik, bukan untuk
menarik kesimpulan tentang dunia nyata.

Cara pakai (dari folder datasets/ atau di Google Colab):
    python bangkitkan_dataset.py
Hasil: delapan berkas .csv di folder yang sama dengan skrip ini.
Menjalankan ulang selalu menghasilkan berkas yang identik (seed = 2026).
"""
from pathlib import Path

import numpy as np
import pandas as pd

SEED = 2026
FOLDER = Path(__file__).resolve().parent


def nilai_mahasiswa(rng):
    # 240 mahasiswa dari dua kelas paralel: IF26A dan IF26H
    n = 240
    kelas = np.repeat(["IF26A", "IF26H"], n // 2)
    asal = rng.choice(["SMA", "SMK", "MA", "Pesantren"], size=n,
                      p=[0.55, 0.20, 0.15, 0.10])
    # Jam belajar per minggu: miring ke kanan, sedikit berbeda antarasal sekolah
    tambah_jam = pd.Series(asal).map({"SMA": 0.0, "SMK": -1.0, "MA": 0.5,
                                      "Pesantren": 1.5}).values
    jam = np.clip(rng.gamma(4.0, 2.0, size=n) + tambah_jam, 0.5, 30).round(1)
    # UTS dan UAS berkorelasi dengan jam belajar; IF26H rata-rata sedikit lebih tinggi
    efek_kelas = np.where(kelas == "IF26H", 3.0, 0.0)
    kemampuan = rng.normal(0, 8, size=n)
    uts = np.clip(52 + 1.5 * jam + kemampuan + efek_kelas
                  + rng.normal(0, 6, size=n), 20, 100).round(0)
    uas = np.clip(50 + 1.7 * jam + kemampuan + efek_kelas
                  + rng.normal(0, 7, size=n), 15, 100).round(0)
    nim = [f"0102526{i:03d}" for i in range(1, n + 1)]
    return pd.DataFrame({"nim": nim, "kelas": kelas, "nilai_uts": uts.astype(int),
                         "nilai_uas": uas.astype(int), "jam_belajar": jam,
                         "asal_sekolah": asal})


def waktu_respons_server(rng):
    # 1.000 permintaan API; waktu respons lognormal (miring kanan, ada ekor panjang)
    n = 1000
    ts = pd.date_range("2026-09-01", periods=n, freq="7min")
    endpoint = rng.choice(["/api/login", "/api/krs", "/api/nilai", "/api/jadwal"],
                          size=n, p=[0.25, 0.35, 0.25, 0.15])
    dasar = pd.Series(endpoint).map({"/api/login": 180, "/api/krs": 260,
                                     "/api/nilai": 220, "/api/jadwal": 160}).values
    waktu = (dasar * rng.lognormal(-0.05, 0.45, size=n)).round(1)
    status = np.where(rng.random(n) < 0.03, 500, 200)
    return pd.DataFrame({"timestamp": ts.strftime("%Y-%m-%d %H:%M:%S"),
                         "endpoint": endpoint, "waktu_ms": waktu,
                         "status_code": status})


def bug_report_harian(rng):
    # 365 hari; laju bug tidak konstan (hari kerja lebih sibuk, minggu rilis lonjakan)
    tanggal = pd.date_range("2025-01-01", periods=365, freq="D")
    hari_kerja = tanggal.dayofweek < 5
    minggu_rilis = (tanggal.isocalendar().week.values % 6) == 0
    lam = np.where(hari_kerja, 4.0, 1.5) * np.where(minggu_rilis, 1.8, 1.0)
    jumlah = rng.poisson(lam)
    modul = rng.choice(["Autentikasi", "Pembayaran", "Laporan", "Antarmuka"],
                       size=365, p=[0.2, 0.25, 0.2, 0.35])
    prioritas = rng.choice(["Rendah", "Sedang", "Tinggi", "Kritis"], size=365,
                           p=[0.40, 0.35, 0.20, 0.05])
    return pd.DataFrame({"tanggal": tanggal.strftime("%Y-%m-%d"),
                         "jumlah_bug": jumlah, "modul": modul,
                         "prioritas": prioritas})


def email_spam(rng):
    # 800 pesan pendek; 35% spam
    kata_spam = ["gratis", "hadiah", "menang", "promo", "klik", "transfer",
                 "undian", "diskon", "pulsa", "segera", "bonus", "rekening"]
    kata_ham = ["rapat", "tugas", "kuliah", "jadwal", "laporan", "dosen",
                "kelompok", "revisi", "besok", "presentasi", "praktikum", "nilai"]
    kata_umum = ["anda", "kami", "hari", "ini", "untuk", "dan", "yang", "mohon",
                 "info", "terima", "kasih", "silakan"]
    baris = []
    for _ in range(800):
        spam = rng.random() < 0.35
        utama, lain = (kata_spam, kata_ham) if spam else (kata_ham, kata_spam)
        panjang = rng.integers(6, 14)
        kata = []
        for _ in range(panjang):
            r = rng.random()
            sumber = utama if r < 0.45 else (kata_umum if r < 0.92 else lain)
            kata.append(sumber[rng.integers(len(sumber))])
        baris.append({"teks": " ".join(kata), "label": "spam" if spam else "ham"})
    return pd.DataFrame(baris)


def transjakarta(rng):
    # 1.200 catatan harian: 6 koridor × 200 hari; rata-rata koridor berbeda
    koridor = ["K1 Blok M-Kota", "K2 Pulogadung-Monas", "K3 Kalideres-Monas",
               "K4 Pulogadung-Dukuh Atas", "K6 Ragunan-Dukuh Atas",
               "K9 Pinang Ranti-Pluit"]
    rata = [72000, 38000, 41000, 30000, 35000, 64000]
    baris = []
    for k, m in zip(koridor, rata):
        for _ in range(200):
            hari = rng.choice(["Hari kerja", "Akhir pekan"], p=[5 / 7, 2 / 7])
            cuaca = rng.choice(["Cerah", "Berawan", "Hujan"], p=[0.45, 0.35, 0.20])
            faktor = (1.0 if hari == "Hari kerja" else 0.65) * \
                     {"Cerah": 1.0, "Berawan": 1.0, "Hujan": 0.9}[cuaca]
            jumlah = int(rng.normal(m * faktor, m * 0.12))
            baris.append({"koridor": k, "hari": hari,
                          "jumlah_penumpang": max(jumlah, 0), "cuaca": cuaca})
    return pd.DataFrame(baris)


def harga_rumah(rng):
    # 600 rumah tapak; harga (juta rupiah) naik terhadap luas dan bergantung lokasi
    n = 600
    lokasi = rng.choice(["Jakarta Selatan", "Jakarta Timur", "Depok", "Bekasi",
                         "Tangerang Selatan", "Bogor"], size=n,
                        p=[0.15, 0.15, 0.18, 0.18, 0.19, 0.15])
    harga_m2 = pd.Series(lokasi).map({"Jakarta Selatan": 28, "Jakarta Timur": 18,
                                      "Depok": 11, "Bekasi": 10,
                                      "Tangerang Selatan": 15, "Bogor": 8}).values
    luas_bangunan = np.clip(rng.gamma(5.0, 22, size=n), 30, 450).round(0)
    luas_tanah = np.clip(luas_bangunan * rng.uniform(0.8, 1.6, size=n), 40, 600).round(0)
    kamar = np.clip((luas_bangunan / 35).round() + rng.integers(-1, 2, size=n), 1, 7)
    harga = (harga_m2 * (0.6 * luas_tanah + 0.5 * luas_bangunan)
             * rng.lognormal(0, 0.18, size=n)).round(0)
    return pd.DataFrame({"luas_tanah": luas_tanah.astype(int),
                         "luas_bangunan": luas_bangunan.astype(int),
                         "kamar": kamar.astype(int), "lokasi": lokasi,
                         "harga_juta": harga.astype(int)})


def ab_test(rng):
    # 2.000 pengguna; grup A (lama) 8% konversi, grup B (fitur baru) 11%
    n = 2000
    grup = np.repeat(["A", "B"], n // 2)
    p = np.where(grup == "A", 0.08, 0.11)
    konversi = (rng.random(n) < p).astype(int)
    durasi = np.round(rng.gamma(3.0, 40, size=n) * np.where(grup == "B", 0.92, 1.0), 1)
    return pd.DataFrame({"user_id": [f"U{i:05d}" for i in range(1, n + 1)],
                         "grup": grup, "konversi": konversi,
                         "durasi_detik": durasi})


def ispu_jakarta(rng):
    # 365 hari; PM2.5 lebih tinggi pada musim kemarau (Juni–Oktober)
    tanggal = pd.date_range("2025-01-01", periods=365, freq="D")
    kemarau = tanggal.month.isin([6, 7, 8, 9, 10])
    stasiun = rng.choice(["DKI1 Bundaran HI", "DKI2 Kelapa Gading",
                          "DKI3 Jagakarsa", "DKI4 Lubang Buaya",
                          "DKI5 Kebon Jeruk"], size=365)
    pm25 = np.clip(rng.lognormal(np.log(np.where(kemarau, 55, 35)), 0.35), 5, 250).round(1)
    pm10 = np.clip(pm25 * rng.uniform(1.3, 1.8, size=365), 10, 400).round(1)
    kategori = pd.cut(pm25, bins=[0, 15.5, 55.4, 150.4, 250.4, 1000],
                      labels=["Baik", "Sedang", "Tidak Sehat", "Sangat Tidak Sehat",
                              "Berbahaya"]).astype(str)
    return pd.DataFrame({"tanggal": tanggal.strftime("%Y-%m-%d"), "stasiun": stasiun,
                         "pm25": pm25, "pm10": pm10, "kategori": kategori})


BERKAS = {
    "nilai_mahasiswa_if.csv": nilai_mahasiswa,
    "waktu_respons_server.csv": waktu_respons_server,
    "bug_report_harian.csv": bug_report_harian,
    "email_spam_indonesia.csv": email_spam,
    "transjakarta_koridor.csv": transjakarta,
    "harga_rumah_jabodetabek.csv": harga_rumah,
    "ab_test_fitur_checkout.csv": ab_test,
    "ispu_jakarta_2025.csv": ispu_jakarta,
}

if __name__ == "__main__":
    for nama, fungsi in BERKAS.items():
        # Setiap berkas punya aliran acak sendiri agar mengubah satu tidak menggeser yang lain
        rng = np.random.default_rng([SEED, list(BERKAS).index(nama)])
        df = fungsi(rng)
        df.to_csv(FOLDER / nama, index=False)
        print(f"{nama:32s} {df.shape[0]:>5} baris × {df.shape[1]} kolom")
