# Praktek 1 : Membuat array
# impor library numpy
import numpy as np

# membuat array dengan numpy
nilai_siswa = np.array([85, 55, 40, 90])

# akses data pada array
print(nilai_siswa[3])

print("========== PEMBATAS ==========")

# Praktek 2 : Mengakses, Mengubah, dan Cek Ukuran dan Dimensi Array
# impor libaray numpy
import numpy as np

# membuat array dengan numpy
nilai_siswa_1 = np.array([75, 65, 45, 80])
nilai_siswa_2 = np.array([[85, 55, 40], [50, 40, 99]])

# cara akses elemen array
print(nilai_siswa_1[0])
print(nilai_siswa_2[1][1])

# mengubah nilai elemen array
nilai_siswa_1[0] = 88
nilai_siswa_2[1][1] = 70

# cek perubahannya 
print(nilai_siswa_1[0])
print(nilai_siswa_2[1][1])

# Cek ukuran dan dimensi array
print("Ukuran Array : ", nilai_siswa_1.shape)
print("Ukuran Array : ", nilai_siswa_2.shape)
print("Dimensi Array : ", nilai_siswa_2.ndim)

print("========== PEMBATAS ==========")

# Praktek 3 : Operasi Aritmatika Pada Array
# impor library numpy
import numpy as np

# membuat array
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# menggunakan operasi penjumlahan pada 2 array
print(a + b)       # array([5, 7, 9])

# Indexing dan Slicing pada Array
arr = np.array([10, 20, 30, 40])
print(arr[1:3])    # array([20, 30])


# iterasi pada array
for x in arr:
    print(x)

print("========== PEMBATAS ==========")

# Praktek 4 : Linear Traversal
# membuat array
arr = [1, 2, 3, 4, 5]

# Linear Traversal ke tiap elemen arr
print("Linear Traversal: ", end=" ")
for i in arr:
    print(i, end=" ")
print()

print("========== PEMBATAS ==========")

# Praktek 5 : Reverse Traversal
# membuat array
arr = [1, 2, 3, 4, 5]

# Reverse Traversal dari elemen akhir 
print("Reverse Traversal: ", end="")
for i in range(len(arr) - 1, -1, -1):
    print(arr[i], end=" ")
print()

print("========== PEMBATAS ==========")

# Praktek 7 : Linear Traversal dengan Metode While
# membuat array
arr = [1, 2, 3, 4, 5]

# mendeklarasikan nilai awal
n = len(arr)
i = 0

print("Linear Traversal using while loop: ", end=" ")
# Linear Traversal dengan while
while i < n:
    print(arr[i], end=" ")
    i += 1
print()

print("========== PEMBATAS ==========")

# Praktek 8 : Reverse Traversal dengan Metode While
# membuat array
arr = [1, 2, 3, 4, 5]

# mendeklarasikan nilai awal
start = 0
end = len(arr) - 1

print("Reverse Traversal using while loop: ", end=" ")
# Reverse Traversal dengan while
while start < end:
    # mengubah indeks array
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1
print(arr)

print("========== PEMBATAS ==========")

# Praktek 9 : Insertion pada akhir elemen array
# membuat array
arr = [12, 16, 20, 40, 50, 70]

# cetak arr sebelum penyisipan
print("Array Sebelum Insertion : ", arr)

# cetak panjang array sebelum penyisipan
print("Panjang Array : ", len(arr))

# menyisipkan array di akhir elemen menggunakan .append()
arr.append(26)

# cetak arr setelah penyisipan
print("Array Setelah Insertion : ", arr)

# cetak panjang array setelah penyisipan
print("Panjang Array : ", len(arr))

print("========== PEMBATAS ==========")

# Praktek 10 : Insertion pada tengah elemen array
# membuat array
arr = [12, 16, 20, 40, 50, 70]

# cetak arr sebelum penyisipan
print("Array Sebelum Insertion : ", arr)

# cetak panjang array sebelum penyisipan
print("Panjang Array : ", len(arr))

# menyisipkan array pada tengah elemen menggunakan .insert(pos, x)
arr.insert(4, 5)

# cetak arr setelah penyisipan
print("Array Setelah Insertion : ", arr)

# cetak panjang array setelah penyisipan
print("Panjang Array : ", len(arr))

print("========== PEMBATAS ==========")

# jika tidak menggunakan fungsi .insert()
# membuat array dan cetak array
arr = [12, 16, 20, 40, 50, 70]
print("Array Sebelum Penyisipan : " , arr)

# Deklarasi elemen tengah yang disisipkan
pos = 4

# Deklarasi nilai yang akan disisipkan
x = 5

# menambah elemen dummy agar menambah panjang array
arr.append(0) # arr = [12, 16, 20, 40, 50, 70, 0]

# melakukan pergeseran elemen mulai dari belakang
for i in range(len(arr) - 2, pos-1, -1):
    arr[i + 1] = arr[i]

# memasukkan nilai x pada elemen yang diinginkan
arr[pos] = x

# Cetak array baru
print("Array Sesudah Penyisipan : ", arr)

print("========== PEMBATAS ==========")

# Praktek 11 : Menghapus array
# membuat array
a = [10, 20, 30, 40, 50]
print("Array Sebelum Deletion : ", a)

# menghapus elemen array pertama yang nilainya 30
a.remove(30)  
print("Setelah remove(30):", a)

# menghapus elemen array pada index 1 (20)
popped_val = a.pop(1)  
print("Popped element:", popped_val)
print("Setelah pop(1):", a) 

# Menghapus elemen pertama (10)
del a[0]  
print("Setelah del a[0]:", a)

print("========== PEMBATAS ==========")

# Praktek 12 : Membuat Matriks 2 Dimensi
# impor library numpy
import numpy as np

# membuat matiks dengan numpy
matriks_np = np.array([[1,2,3],
                        [4,5,6],
                        [7,8,9]])

print(matriks_np[2][2])

print("========== PEMBATAS ==========")

# Praktek 13 : Operasi Penjumlahan Matriks dengan list
# Program penjumlahan matriks yang dibuat dari list

X = [[12,7,3],
    [4,5,6],
    [7,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# proses penjumlahan dua matriks menggunakan nested loop
# mengulang sebanyak row (baris)
for i in range(len(X)):
   # mengulang sebanyak column (kolom)
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

print("Hasil Penjumlahan Matriks dari LIST") 

# cetak hasil penjumlahan secara iteratif
for r in result:   
   print(r)

print("========== PEMBATAS ==========")

# Praktek 14 : Operasi Penjumlahan Matriks dengan numpy
# impor library numpy
import numpy as np

# Membuat matriks dengan numpy
X = np.array([
    [12,7,3],
    [4,5,6],
    [7,8,9]])

Y = np.array(
    [[5,8,1],
    [6,7,3],
    [4,5,9]])

# Operasi penjumlahan dua matrik numpy
result = X + Y

# cetak hasil
print("Hasil Penjumlahan Matriks dari NumPy")
print(result)

print("========== PEMBATAS ==========")

# Praktek 15 : Operasi Pengurangan Matriks dengan numpy
# impor library numpy
import numpy as np

# Membuat matriks dengan numpy
X = np.array([
    [12,7,3],
    [4,5,6],
    [7,8,9]])

Y = np.array(
    [[5,8,1],
    [6,7,3],
    [4,5,9]])

# Operasi pengurangan dua matrik numpy
result = X - Y

# cetak hasil
print("Hasil Pengurangan Matriks dari NumPy")
print(result)

print("========== PEMBATAS ==========")

# Praktek 16 : Operasi Perkalian Matriks dengan numpy
# impor library numpy
import numpy as np

# Membuat matriks dengan numpy
X = np.array([
    [12,7,3],
    [4,5,6],
    [7,8,9]])

Y = np.array(
    [[5,8,1],
    [6,7,3],
    [4,5,9]])

# Operasi perkalian dua matrik numpy
result = X * Y

# cetak hasil
print("Hasil Perkalian Matriks dari NumPy")
print(result)

print("========== PEMBATAS ==========")

# Praktek 17 : Operasi Pembagian Matriks dengan numpy
# impor library numpy
import numpy as np

# Membuat matriks dengan numpy
X = np.array([
    [12,7,3],
    [4,5,6],
    [7,8,9]])

Y = np.array(
    [[5,8,1],
    [6,7,3],
    [4,5,9]])

# Operasi pembagian dua matrik numpy
result = X / Y

# cetak hasil
print("Hasil Pembagian Matriks dari NumPy")
print(result)

print("========== PEMBATAS ==========")

# Praktek 18 : transpose()
# impor library numpy
import numpy as np

# membuat matriks
matriks_a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# cetak matriks
print("Matriks Sebelum Transpose")
print(matriks_a)

# transpose matriks_a
balik = matriks_a.transpose()

# cetak matriks setelah dibalik
print("Matriks Setelah Transpose")
print(balik)

print("========== PEMBATAS ==========")

# Praktek 19 : reshape()
# impor library numpy
import numpy as np

# membuat array 1 dimensi
arr_1d = np.array([50, 70, 89, 99, 103, 35])

# cetak matriks sebelum reshape
print("Matriks Sebelum Reshape")
print(arr_1d)
print("Ukuran Matriks : ", arr_1d.shape)
print("\n")

# mengubah matriks menjadi ordo 3 x 2
ubah = arr_1d.reshape(3, 2)

# cetak matriks setelah reshape ke ordo 3 x 2
print("Matriks Setelah Reshape")
print(ubah)
print("Ukuran Matriks : ", ubah.shape)

print("========== PEMBATAS ==========")

# Praktek 20 : Vektor
# vektor baris
vek_1 = np.array([1, 2, 3])

# vektor kolom
vek_2 = np.array([[1], 
                  [2], 
                  [3]])
# atau menggunakan transpose()
vek_3 = np.array([[1, 2, 3]]).T

print("Vektor Baris")
print(vek_1)
print("vektor Kolom")
print(vek_2)
print("Vektor Kolom dengan transpose()")
print(vek_3)

print("========== PEMBATAS ==========")

# Praktek 21 : Flatten()
# impor library numpy
import numpy as np

# membuat matriks
matriks_a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# cetak matriks awal
print("Matriks Awal")
print(matriks_a)
print("Ukuran : ", matriks_a.shape)
print("\n")

# ubah matriks menjadi vektor
jd_vektor = matriks_a.flatten()

# cetak vektor
print("Hasil Konversi Matriks ke Vektor")
print(jd_vektor)
print("Ukuran : ", jd_vektor.shape)