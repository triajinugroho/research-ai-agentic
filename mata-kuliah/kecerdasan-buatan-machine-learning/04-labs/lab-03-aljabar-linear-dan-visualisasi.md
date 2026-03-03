# Lab 03: Aljabar Linear dan Visualisasi

**Mata Kuliah:** Kecerdasan Buatan dan Machine Learning
**Program Studi:** Informatika, Universitas Al Azhar Indonesia
**Minggu:** 3
**Penilaian:** Dinilai (submit notebook)

---

## Tujuan Praktikum

Setelah menyelesaikan lab ini, mahasiswa mampu:

- Melakukan operasi vektor dengan NumPy (penjumlahan, perkalian skalar, dot product)
- Melakukan operasi matriks (perkalian, transpose, invers)
- Menghitung eigenvalues dan eigenvectors menggunakan NumPy
- Memvisualisasikan vektor dan transformasi linear dengan matplotlib
- Memvisualisasikan gradient descent dan konvergensi cost function
- Memvisualisasikan decision boundary pada ruang 2D

---

## Persiapan

1. Buka Google Colab dan buat notebook baru
2. Nama file: `Lab03_NamaAnda_NIM.ipynb`
3. Pastikan library numpy dan matplotlib sudah tersedia
4. Pahami konsep dasar vektor dan matriks dari kuliah teori

---

## Langkah-langkah

### Langkah 1: Operasi Vektor dengan NumPy

```python
# =============================================
# LANGKAH 1: Operasi Vektor
# =============================================

import numpy as np
import matplotlib.pyplot as plt

print("=" * 50)
print("OPERASI VEKTOR DENGAN NUMPY")
print("=" * 50)

# --- Definisi Vektor ---
v1 = np.array([3, 2])
v2 = np.array([1, 4])

print(f"Vektor v1: {v1}")
print(f"Vektor v2: {v2}")

# --- Penjumlahan Vektor ---
v_jumlah = v1 + v2
print(f"\nPenjumlahan (v1 + v2): {v_jumlah}")

# --- Pengurangan Vektor ---
v_kurang = v1 - v2
print(f"Pengurangan (v1 - v2): {v_kurang}")

# --- Perkalian Skalar ---
skalar = 3
v_skalar = skalar * v1
print(f"Perkalian skalar ({skalar} * v1): {v_skalar}")

# --- Dot Product (Perkalian Titik) ---
dot = np.dot(v1, v2)
print(f"\nDot product (v1 . v2): {dot}")
print(f"  Cara hitung: ({v1[0]}*{v2[0]}) + ({v1[1]}*{v2[1]}) = {v1[0]*v2[0]} + {v1[1]*v2[1]} = {dot}")

# --- Magnitude (Panjang Vektor) ---
mag_v1 = np.linalg.norm(v1)
mag_v2 = np.linalg.norm(v2)
print(f"\nMagnitude |v1|: {mag_v1:.4f}")
print(f"Magnitude |v2|: {mag_v2:.4f}")

# --- Sudut Antara Dua Vektor ---
cos_theta = np.dot(v1, v2) / (mag_v1 * mag_v2)
theta_rad = np.arccos(cos_theta)
theta_deg = np.degrees(theta_rad)
print(f"\nSudut antara v1 dan v2: {theta_deg:.2f} derajat")

# --- Vektor 3D ---
v3d_a = np.array([1, 2, 3])
v3d_b = np.array([4, 5, 6])

# Cross product (hanya untuk 3D)
cross = np.cross(v3d_a, v3d_b)
print(f"\nCross product (v3d_a x v3d_b): {cross}")
```

### Langkah 2: Operasi Matriks

```python
# =============================================
# LANGKAH 2: Operasi Matriks
# =============================================

print("=" * 50)
print("OPERASI MATRIKS")
print("=" * 50)

# --- Definisi Matriks ---
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(f"Matriks A:\n{A}")
print(f"\nMatriks B:\n{B}")

# --- Perkalian Matriks ---
C = A @ B  # atau np.matmul(A, B) atau np.dot(A, B)
print(f"\nPerkalian Matriks (A @ B):\n{C}")
print(f"Verifikasi: C[0,0] = {A[0,0]}*{B[0,0]} + {A[0,1]}*{B[1,0]} = {A[0,0]*B[0,0] + A[0,1]*B[1,0]}")

# --- Transpose ---
A_T = A.T
print(f"\nTranspose A:\n{A_T}")

# --- Determinan ---
det_A = np.linalg.det(A)
print(f"\nDeterminan A: {det_A:.4f}")
print(f"  Cara hitung: ({A[0,0]}*{A[1,1]}) - ({A[0,1]}*{A[1,0]}) = {A[0,0]*A[1,1] - A[0,1]*A[1,0]}")

# --- Invers Matriks ---
if det_A != 0:
    A_inv = np.linalg.inv(A)
    print(f"\nInvers A:\n{A_inv}")

    # Verifikasi: A * A^(-1) = I (matriks identitas)
    identitas = A @ A_inv
    print(f"\nVerifikasi (A @ A_inv ≈ I):\n{np.round(identitas, 4)}")
else:
    print("\nMatriks A singular (tidak memiliki invers)")

# --- Sistem Persamaan Linear ---
# Selesaikan: Ax = b
# 2x + y = 5
# x + 3y = 7
A_spl = np.array([[2, 1], [1, 3]])
b_spl = np.array([5, 7])

x_solusi = np.linalg.solve(A_spl, b_spl)
print(f"\nSistem Persamaan Linear:")
print(f"  2x + y  = 5")
print(f"  x  + 3y = 7")
print(f"  Solusi: x = {x_solusi[0]:.4f}, y = {x_solusi[1]:.4f}")

# Verifikasi
print(f"  Verifikasi: {A_spl @ x_solusi} = {b_spl}")
```

### Langkah 3: Eigenvalues dan Eigenvectors

```python
# =============================================
# LANGKAH 3: Eigenvalues dan Eigenvectors
# =============================================

print("=" * 50)
print("EIGENVALUES DAN EIGENVECTORS")
print("=" * 50)

# Matriks contoh
M = np.array([[4, 2], [1, 3]])
print(f"Matriks M:\n{M}")

# Hitung eigenvalues dan eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(M)

print(f"\nEigenvalues  : {eigenvalues}")
print(f"Eigenvectors :\n{eigenvectors}")

# Verifikasi: M @ v = lambda * v
for i in range(len(eigenvalues)):
    lam = eigenvalues[i]
    v = eigenvectors[:, i]
    Mv = M @ v
    lam_v = lam * v
    print(f"\nEigenvalue λ_{i+1} = {lam:.4f}")
    print(f"  Eigenvector v_{i+1}  = {v}")
    print(f"  M @ v_{i+1}         = {Mv}")
    print(f"  λ_{i+1} * v_{i+1}   = {lam_v}")
    print(f"  Cocok? {np.allclose(Mv, lam_v)}")

# Aplikasi: Matriks kovariansi (dasar PCA)
print(f"\n--- Aplikasi: Matriks Kovariansi ---")
np.random.seed(42)
data = np.random.multivariate_normal(
    mean=[5, 3],
    cov=[[2.0, 1.5], [1.5, 1.0]],
    size=100
)
cov_matrix = np.cov(data.T)
print(f"Matriks kovariansi:\n{cov_matrix.round(4)}")

eig_vals, eig_vecs = np.linalg.eig(cov_matrix)
print(f"Eigenvalues: {eig_vals.round(4)}")
print(f"Arah variansi terbesar (PC1): {eig_vecs[:, 0].round(4)}")
```

### Langkah 4: Visualisasi Vektor dan Transformasi

```python
# =============================================
# LANGKAH 4: Visualisasi Vektor dan Transformasi
# =============================================

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# --- Plot 1: Operasi Vektor ---
ax = axes[0]
origin = np.array([0, 0])

# Gambar vektor
ax.quiver(*origin, *v1, angles='xy', scale_units='xy', scale=1, color='blue', label='v1')
ax.quiver(*origin, *v2, angles='xy', scale_units='xy', scale=1, color='red', label='v2')
ax.quiver(*origin, *v_jumlah, angles='xy', scale_units='xy', scale=1, color='green', label='v1+v2')

# Garis putus-putus untuk paralelogram
ax.plot([v1[0], v_jumlah[0]], [v1[1], v_jumlah[1]], 'g--', alpha=0.5)
ax.plot([v2[0], v_jumlah[0]], [v2[1], v_jumlah[1]], 'g--', alpha=0.5)

ax.set_xlim(-1, 7)
ax.set_ylim(-1, 7)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.legend()
ax.set_title('Penjumlahan Vektor', fontsize=13)
ax.set_xlabel('x')
ax.set_ylabel('y')

# --- Plot 2: Transformasi Linear ---
ax = axes[1]

# Matriks transformasi (rotasi + scaling)
T = np.array([[2, -1], [1, 1.5]])

# Titik-titik asli (persegi satuan)
persegi = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]).T

# Transformasi
persegi_trans = T @ persegi

ax.plot(persegi[0], persegi[1], 'b-o', linewidth=2, label='Asli', markersize=6)
ax.plot(persegi_trans[0], persegi_trans[1], 'r-o', linewidth=2, label='Setelah transformasi', markersize=6)
ax.fill(persegi[0], persegi[1], alpha=0.2, color='blue')
ax.fill(persegi_trans[0], persegi_trans[1], alpha=0.2, color='red')

ax.set_xlim(-2, 4)
ax.set_ylim(-1, 4)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.legend()
ax.set_title(f'Transformasi Linear\ndet(T) = {np.linalg.det(T):.1f}', fontsize=13)
ax.set_xlabel('x')
ax.set_ylabel('y')

# --- Plot 3: Eigenvectors dari Matriks Kovariansi ---
ax = axes[2]

ax.scatter(data[:, 0], data[:, 1], alpha=0.5, s=20, color='gray', label='Data')

# Gambar eigenvector (skalakan untuk visibilitas)
mean = data.mean(axis=0)
for i in range(2):
    skala = np.sqrt(eig_vals[i]) * 2
    vektor = eig_vecs[:, i] * skala
    ax.annotate('', xy=mean + vektor, xytext=mean,
                arrowprops=dict(arrowstyle='->', color=['blue', 'red'][i], lw=2.5))
    ax.text(mean[0] + vektor[0] + 0.1, mean[1] + vektor[1],
            f'PC{i+1} (λ={eig_vals[i]:.2f})', fontsize=10,
            color=['blue', 'red'][i], fontweight='bold')

ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.legend()
ax.set_title('Eigenvectors (Arah Variansi)', fontsize=13)
ax.set_xlabel('x')
ax.set_ylabel('y')

plt.suptitle('Visualisasi Aljabar Linear', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.show()
```

### Langkah 5: Visualisasi Gradient Descent

```python
# =============================================
# LANGKAH 5: Gradient Descent Visualization
# =============================================

print("=" * 50)
print("VISUALISASI GRADIENT DESCENT")
print("=" * 50)

# Definisi fungsi cost: f(x) = (x - 3)^2 + 1
# Turunan: f'(x) = 2(x - 3)
def cost_function(x):
    return (x - 3) ** 2 + 1

def gradient(x):
    return 2 * (x - 3)

# --- Jalankan Gradient Descent ---
learning_rate = 0.1
x_current = 10.0       # Titik awal
n_iterasi = 30

# Simpan history
history_x = [x_current]
history_cost = [cost_function(x_current)]

for i in range(n_iterasi):
    grad = gradient(x_current)
    x_current = x_current - learning_rate * grad
    history_x.append(x_current)
    history_cost.append(cost_function(x_current))

print(f"Titik awal    : x = {history_x[0]:.4f}, cost = {history_cost[0]:.4f}")
print(f"Titik akhir   : x = {history_x[-1]:.4f}, cost = {history_cost[-1]:.4f}")
print(f"Minimum sebenarnya: x = 3.0000, cost = 1.0000")

# --- Visualisasi ---
fig, axes = plt.subplots(1, 2, figsize=(15, 5))

# Plot 1: Cost function dengan jejak gradient descent
ax = axes[0]
x_plot = np.linspace(-2, 12, 100)
ax.plot(x_plot, cost_function(x_plot), 'b-', linewidth=2, label='f(x) = (x-3)² + 1')
ax.plot(history_x, history_cost, 'ro-', markersize=5, alpha=0.7, label='Gradient Descent')
ax.plot(history_x[0], history_cost[0], 'g*', markersize=15, label=f'Start (x={history_x[0]:.1f})')
ax.plot(history_x[-1], history_cost[-1], 'r*', markersize=15, label=f'End (x={history_x[-1]:.2f})')
ax.axvline(x=3, color='gray', linestyle='--', alpha=0.5, label='Minimum (x=3)')
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('Cost f(x)', fontsize=12)
ax.set_title('Gradient Descent pada Cost Function', fontsize=13)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Plot 2: Konvergensi cost per iterasi
ax = axes[1]
ax.plot(range(len(history_cost)), history_cost, 'b-o', markersize=4, linewidth=1.5)
ax.set_xlabel('Iterasi', fontsize=12)
ax.set_ylabel('Cost', fontsize=12)
ax.set_title('Konvergensi Cost Function', fontsize=13)
ax.axhline(y=1.0, color='red', linestyle='--', alpha=0.5, label='Minimum cost = 1.0')
ax.legend()
ax.grid(True, alpha=0.3)

plt.suptitle(f'Gradient Descent (learning_rate = {learning_rate})', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.show()

# --- Eksperimen learning rate ---
print("\n--- Eksperimen Learning Rate ---")
for lr in [0.01, 0.1, 0.5, 0.9]:
    x = 10.0
    for _ in range(30):
        x = x - lr * gradient(x)
    print(f"  lr = {lr:.2f} → x akhir = {x:.6f}, cost = {cost_function(x):.6f}")
```

### Langkah 6: Visualisasi Decision Boundary

```python
# =============================================
# LANGKAH 6: Visualisasi Decision Boundary
# =============================================

from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification

print("=" * 50)
print("VISUALISASI DECISION BOUNDARY")
print("=" * 50)

# --- Buat dataset 2D untuk klasifikasi ---
np.random.seed(42)
X, y = make_classification(
    n_samples=200, n_features=2, n_redundant=0,
    n_informative=2, n_clusters_per_class=1,
    class_sep=1.5, random_state=42
)

# --- Latih model Logistic Regression ---
model = LogisticRegression(random_state=42)
model.fit(X, y)
akurasi = model.score(X, y)
print(f"Akurasi model: {akurasi:.4f}")

# --- Buat grid untuk decision boundary ---
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(
    np.arange(x_min, x_max, 0.02),
    np.arange(y_min, y_max, 0.02)
)
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# --- Visualisasi ---
fig, ax = plt.subplots(figsize=(10, 7))

# Gambar decision boundary
ax.contourf(xx, yy, Z, alpha=0.3, cmap='RdBu')
ax.contour(xx, yy, Z, colors='black', linewidths=0.5)

# Gambar titik data
scatter = ax.scatter(X[:, 0], X[:, 1], c=y, cmap='RdBu',
                     edgecolors='black', s=50, alpha=0.8)

# Koefisien model
w = model.coef_[0]
b = model.intercept_[0]
print(f"Koefisien (w): {w}")
print(f"Bias (b): {b:.4f}")
print(f"Persamaan decision boundary: {w[0]:.3f}*x1 + {w[1]:.3f}*x2 + {b:.3f} = 0")

ax.set_xlabel('Fitur 1 (x₁)', fontsize=12)
ax.set_ylabel('Fitur 2 (x₂)', fontsize=12)
ax.set_title(f'Decision Boundary - Logistic Regression\nAkurasi: {akurasi:.2%}', fontsize=14)
ax.legend(*scatter.legend_elements(), title='Kelas')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print(f"""
Catatan:
- Decision boundary adalah garis/kurva pemisah antara dua kelas
- Model linear menghasilkan decision boundary berupa garis lurus
- Titik di satu sisi garis diprediksi kelas 0, sisi lain kelas 1
""")
```

---

## Tantangan Tambahan

1. **Gradient Descent 2D:** Implementasikan gradient descent untuk fungsi 2 variabel f(x, y) = x^2 + y^2. Visualisasikan konvergensi menggunakan contour plot dengan jejak gradient descent. Eksperimen dengan berbagai learning rate.

2. **Perbandingan Decision Boundary:** Latih 3 model berbeda (LogisticRegression, SVM linear, DecisionTree) pada dataset yang sama. Buat visualisasi 3 subplot yang membandingkan decision boundary masing-masing model.

3. **Animasi Transformasi Linear:** Buat visualisasi yang menunjukkan bagaimana matriks transformasi mengubah sebuah lingkaran satuan menjadi elips. Gunakan berbagai matriks transformasi (rotasi, scaling, shearing).

---

## Checklist Penyelesaian

- [ ] Operasi vektor (penjumlahan, dot product, magnitude) berhasil dijalankan
- [ ] Operasi matriks (perkalian, transpose, invers, determinan) berhasil dijalankan
- [ ] Eigenvalues dan eigenvectors berhasil dihitung dan diverifikasi
- [ ] Visualisasi vektor dan transformasi linear berhasil ditampilkan
- [ ] Gradient descent berhasil diimplementasi dan divisualisasi
- [ ] Decision boundary berhasil divisualisasi
- [ ] Notebook disimpan dengan nama `Lab03_NamaAnda_NIM.ipynb`
- [ ] Minimal 1 tantangan tambahan diselesaikan

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
