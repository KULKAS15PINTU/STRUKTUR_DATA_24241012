# Meminta input dari user untuk menentukan jumlah deret Fibonacci
jumlah = int(input("Masukkan jumlah deret Fibonacci: "))

# Inisialisasi dua angka pertama dalam deret Fibonacci
a, b = 1, 1

print("Fibonacci:", end=" ")

# Melakukan perulangan sebanyak jumlah deret
for i in range(jumlah):
    # Menampilkan angka Fibonacci saat ini
    print(a, end=", " if i < jumlah - 1 else "")  # Cetak koma hanya jika belum angka terakhir

    # Menghitung nilai Fibonacci berikutnya
    a, b = b, a + b  # Geser nilai: a menjadi b, b menjadi a+b (sesuai rumus Fibonacci)