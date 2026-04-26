---
title: Persamaan liniar
date: 2026-04-12
---

## Eliminasi Gauss

Buat sistem persamaan linier 5 variabel yang menghasilkan:

x1 = 1, x2 = 2, x3 = 3, x4 = 4, x5 = 5

## Sistem Persamaan

$$
\begin{aligned}
x_1 + x_2 + x_3 + x_4 + x_5 &= 15 \\
2x_1 + x_2 + x_3 + x_4 + x_5 &= 16 \\
x_1 + 2x_2 + x_3 + x_4 + x_5 &= 16 \\
x_1 + x_2 + 2x_3 + x_4 + x_5 &= 18 \\
x_1 + x_2 + x_3 + 2x_4 + x_5 &= 19
\end{aligned}
$$

## Matriks Augmented

$$
\left[
\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 15 \\
2 & 1 & 1 & 1 & 1 & 16 \\
1 & 2 & 1 & 1 & 1 & 16 \\
1 & 1 & 2 & 1 & 1 & 18 \\
1 & 1 & 1 & 2 & 1 & 19
\end{array}
\right]
$$

## Operasi Baris Elementer

Langkah 1

$$
R_2 = R_2 - 2R_1
$$

$$
R_3 = R_3 - R_1
$$

$$
R_4 = R_4 - R_1
$$

$$
R_5 = R_5 - R_1
$$

Hasil:

$$
\left[
\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 15 \\
0 & -1 & -1 & -1 & -1 & -14 \\
0 & 1 & 0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0 & 0 & 3 \\
0 & 0 & 0 & 1 & 0 & 4
\end{array}
\right]
$$

## Hasil Akhir

$$
x_1 = 1,\quad
x_2 = 2,\quad
x_3 = 3,\quad
x_4 = 4,\quad
x_5 = 5
$$