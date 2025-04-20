# Minta input dari user: berapa jumlah deret genap
jumlah = int(input("Masukkan jumlah deret genap: "))

# Melakukan perulangan sebanyak jumlah deret
for i in range(jumlah):
    # Hitung jumlah bintang genap ke-i
    # Deret genap: 2, 4, 6, ... => Rumus: 2 * (i + 1)
    bintang = 2 * (i + 1)

    # Hitung jumlah spasi untuk membuat segitiga rata tengah
    # Semakin besar bintang, semakin sedikit spasi
    spasi = jumlah * 2 - bintang

    # Cetak spasi di sebelah kiri + bintang
    print(" " * (spasi // 2) + "*" * bintang)