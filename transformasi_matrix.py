import matplotlib.pyplot as plt

# objek awal (4 titik)
titik = [(2, 1), (4, 1), (4, 3), (2, 3)]

def geser(titik, dx, dy):
    return [(x + dx, y + dy) for x, y in titik]

def skala(titik, s):
    return [(x * s, y * s) for x, y in titik]

def cermin_sumbu_x(titik):
    return [(x, -y) for x, y in titik]

def gambar(titik, label):
    x = [p[0] for p in titik] + [titik[0][0]]
    y = [p[1] for p in titik] + [titik[0][1]]
    plt.plot(x, y, marker='o', label=label)

plt.figure()

for i in range(5):
    plt.clf()

    # objek asli berubah
    titik = geser(titik, 1, 1)   # geser kanan & atas
    titik = skala(titik, 0.9)    # mendekat (mengecil)

    # bayangan dari objek terbaru
    bayangan = cermin_sumbu_x(titik)

    # tampilkan keduanya
    gambar(titik, "Objek Asli")
    gambar(bayangan, "Hasil Pencerminan")

    # sumbu (cermin)
    plt.axhline(0)
    plt.axvline(0)

    plt.legend()
    plt.grid()
    plt.xlim(-1, 8)
    plt.ylim(-8, 8)

    plt.title("Objek dan Pencerminan (Selalu Mengikuti)")
    plt.pause(0.5)

plt.show()
