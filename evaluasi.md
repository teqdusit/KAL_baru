---
title: Evaluasi determinan dan invers
date: 2026-04-20
---

## A. Hitunglah determinan matrik berikut dengan menggunakan rumus expansi baris

$$
\sum_{k=1}^{n} (-1)^{i+k} a_{ik} M_{ik}
$$
dengan $M_{ij}$ adalah minior dari matrik A dan

$$
M_{ij} = det A_{ij}.
$$

$A_{ij}$  adalah submatrik dengan menghapus baris i dan kolom kolom j dari matrix $A_{mxn}$ dengan $1 \le i,j \le n$

# 1. 
$$
A =
\begin{bmatrix}
-7 & -5 \\
1 & 4
\end{bmatrix}
$$
determinan:
$$
\det(A) = (-7)(4) - (-5)(1) = -28 + 5 = -23
$$
hasil:
$$
\det(A) = -23
$$

# 2. 
$$
A =
\begin{bmatrix}
0 & 2 & -3 \\
1 & -2 & -1 \\
0 & 0 & 1
\end{bmatrix}
$$
Ambil ekspansi baris ke-1:
$$
\det(A) &= 0 \cdot M_{11} - 2 \cdot M_{12} + (-3) \cdot M_{13} \\[6pt]
$$
Hitung minor:

M 12 = 1

M 13 = 0

$$
\det(A) &= -2(1) + (-3)(0) \\[4pt] &= -2
$$

$$
\det(A) = -2
$$

# 3. 
$$
A =
\begin{bmatrix}
1 & -3 & 1 & 1 \\
-3 & 1 & 1 & 1 \\
1 & 1 & -3 & 1 \\
1 & 1 & 1 & -3
\end{bmatrix}
$$

Matriks ini simetris dengan pola khusus.

- Matriks ini = J−4I (dengan pola tertentu)

- Hasil determinan bisa dihitung atau disederhanakan

Hasil:

$$
\det(A) = -256
$$

## B. Gunakan rumus matriks adjoin untuk menghitung invers dari matriks berikut dengan rumus

$$
(\mathrm{adj}\, A)_{ij} = (-1)^{i+j} M_{ji}
$$
dan
$$
A^{-1} = \frac{1}{\det A} \, \mathrm{adj}\, A
$$

# 4. 
$$
A =
\begin{bmatrix}
-7 & -5 \\
1 & 4
\end{bmatrix}
$$
Determinan: 
$$
\det(A) = -23
$$

Adjoint:

$$
\mathrm{adj}\,A =
\begin{bmatrix}
4 & 5 \\
-1 & -7
\end{bmatrix}
$$

invers: 

$$
A^{-1} =
\frac{1}{-23}
\begin{bmatrix}
4 & 5 \\
-1 & -7
\end{bmatrix}
=
\begin{bmatrix}
-\frac{4}{23} & -\frac{5}{23} \\
\frac{1}{23} & \frac{7}{23}
\end{bmatrix}
$$

# 5. 
$$
A =
\begin{bmatrix}
0 & 2 & -3 \\
1 & -2 & -1 \\
0 & 0 & 1
\end{bmatrix}
$$

$$
\det(A) = -23
$$

Adjoint:

$$
\mathrm{adj}\,A =
\begin{bmatrix}
-2 & -1 & 0 \\
-2 & 0 & 0 \\
-8 & -3 & -2
\end{bmatrix}
$$

invers:

$$
A^{-1} =
\frac{1}{-2}
\begin{bmatrix}
-2 & -1 & 0 \\
-2 & 0 & 0 \\
-8 & -3 & -2
\end{bmatrix}
=
\begin{bmatrix}
1 & \frac{1}{2} & 0 \\
1 & 0 & 0 \\
4 & \frac{3}{2} & 1
\end{bmatrix}
$$

# 6. 
$$
A =
\begin{bmatrix}
1 & -3 & 1 & 1 \\
-3 & 1 & 1 & 1 \\
1 & 1 & -3 & 1 \\
1 & 1 & 1 & -3
\end{bmatrix}
$$

$$
\det(A) = -256
$$

Karena matriks simetris khusus, hasil inversnya:

$$
A^{-1} =
-\frac{1}{16}
\begin{bmatrix}
5 & 1 & 1 & 1 \\
1 & 5 & 1 & 1 \\
1 & 1 & 5 & 1 \\
1 & 1 & 1 & 5
\end{bmatrix}
$$