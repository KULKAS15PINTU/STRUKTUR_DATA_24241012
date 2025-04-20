# Menentukan jumlah baris segitiga
# Karena kita ingin baris dengan jumlah bintang ganjil: 1, 3, 5
# Maka kita butuh 3 baris
baris = 3

# Melakukan perulangan sebanyak jumlah baris
for i in range(baris):
    # Hitung jumlah spasi yang dibutuhkan di sebelah kiri agar segitiga rapi
    # Semakin ke bawah, spasi makin sedikit
    spasi = baris - i - 1

    # Hitung jumlah bintang ganjil yang akan dicetak
    # Rumusnya: 2*i + 1 akan menghasilkan 1, 3, 5, dst
    bintang = 2 * i + 1

    # Cetak spasi terlebih dahulu, lalu bintang
    print(" " * spasi + "*" * bintang)