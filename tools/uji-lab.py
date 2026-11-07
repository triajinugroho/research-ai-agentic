#!/usr/bin/env python3
"""Menjalankan seluruh sel Python pada lab sebuah mata kuliah dan melaporkan galatnya.

Setiap berkas `04-labs/lab-*.md` dijalankan dalam proses tersendiri. Blok
```python dieksekusi berurutan dalam satu ruang nama, meniru notebook Colab:
  - bila folder lab memuat `lab-01-*.md`, blok pertamanya (sel pembuka baku,
    mis. impor dan RANDOM_STATE) dijalankan lebih dulu untuk lab lain;
  - direktori kerja adalah folder `datasets/` mata kuliah bila ada, sehingga
    `pd.read_csv("nama.csv")` menemukan berkas latihan;
  - `display` dipetakan ke `print`, dan grafik tidak ditampilkan.
Galat karena modul khusus Colab (`google.colab`) tidak dihitung sebagai kegagalan.

Pemakaian (dari akar repositori; butuh numpy, pandas, scipy, scikit-learn,
matplotlib, seaborn, statsmodels):

    python3 tools/uji-lab.py mata-kuliah/semester-5/dasar-kecerdasan-artifisial-dan-pembelajaran-mesin
    python3 tools/uji-lab.py <folder-mk> --seed 7      # ganti RANDOM_STATE = 42
    python3 tools/uji-lab.py <folder-mk> --lab 14      # satu lab saja

Keluar dengan kode 1 bila ada blok yang gagal. Alat ini memeriksa bahwa kode
BERJALAN; kesesuaian angka dengan narasi lab tetap perlu dibaca manusia.
"""
import glob
import os
import re
import subprocess
import sys

PEMBUNGKUS = r'''
import contextlib, io, os, re, sys, traceback, warnings
warnings.filterwarnings("ignore")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.show = lambda *a, **k: plt.close("all")

lab, pembuka, cwd, seed = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

def blok(path):
    return re.findall(r"```python\n(.*?)```", open(path, encoding="utf-8").read(), re.S)

def ganti_seed(kode):
    return kode.replace("RANDOM_STATE = 42", f"RANDOM_STATE = {seed}") if seed else kode

ns = {"__name__": "__main__", "display": print}
if pembuka:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(ganti_seed(blok(pembuka)[0]), ns)
os.chdir(cwd)
gagal = 0
for i, kode in enumerate(blok(lab), 1):
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            exec(ganti_seed(kode), ns)
    except ModuleNotFoundError as e:
        if "google" in str(e):
            print(f"  blok {i}: dilewati (khusus Colab)")
            continue
        gagal += 1
        print(f"  blok {i}: GALAT {type(e).__name__}: {e}")
    except Exception as e:
        gagal += 1
        print(f"  blok {i}: GALAT {type(e).__name__}: {str(e)[:160]}")
print(f"__GAGAL__={gagal}")
'''


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    folder = os.path.abspath(sys.argv[1])
    seed = sys.argv[sys.argv.index("--seed") + 1] if "--seed" in sys.argv else ""
    satu = sys.argv[sys.argv.index("--lab") + 1].zfill(2) if "--lab" in sys.argv else None

    labs = sorted(glob.glob(os.path.join(folder, "04-labs", "lab-*.md")))
    if satu:
        labs = [p for p in labs if os.path.basename(p).startswith(f"lab-{satu}-")]
    if not labs:
        print("Tidak ada berkas 04-labs/lab-*.md di", folder)
        sys.exit(2)
    lab01 = [p for p in labs if os.path.basename(p).startswith("lab-01-")] or \
        glob.glob(os.path.join(folder, "04-labs", "lab-01-*.md"))
    pembuka = lab01[0] if lab01 else ""
    # sel pembuka hanya dipakai bila memang mendefinisikan RANDOM_STATE
    if pembuka and "RANDOM_STATE" not in open(pembuka, encoding="utf-8").read().split("```python", 2)[1]:
        pembuka = ""
    cwd = os.path.join(folder, "datasets") if os.path.isdir(os.path.join(folder, "datasets")) \
        else os.path.join(folder, "04-labs")

    total_gagal = 0
    print(f"# Uji lab — {os.path.relpath(folder)}" + (f" (seed {seed})" if seed else "") + "\n")
    for lab in labs:
        nama = os.path.basename(lab)
        pakai_pembuka = pembuka if pembuka and lab != pembuka else ""
        hasil = subprocess.run(
            [sys.executable, "-c", PEMBUNGKUS, lab, pakai_pembuka, cwd, seed],
            capture_output=True, text=True, timeout=900)
        keluaran = hasil.stdout + hasil.stderr
        m = re.search(r"__GAGAL__=(\d+)", keluaran)
        gagal = int(m.group(1)) if m else 1
        total_gagal += gagal
        print(f"- {'OK   ' if gagal == 0 else 'GAGAL'} {nama}")
        for baris in keluaran.splitlines():
            if baris.startswith("  blok"):
                print("   ", baris.strip())
        if not m:
            print("    proses berhenti:", keluaran.strip().splitlines()[-1:] or "")
    print(f"\n**{len(labs)} lab, {total_gagal} blok gagal.**")
    sys.exit(1 if total_gagal else 0)


if __name__ == "__main__":
    main()
