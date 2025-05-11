# Program untuk merekap data nilai mahasiswa dalam sebuah kelas

# Dictionary untuk menyimpan data mahasiswa, key = NIM
data_mahasiswa = {}

# Meminta pengguna memasukkan jumlah mahasiswa
jumlah = int(input("Masukkan jumlah mahasiswa: "))

# Perulangan untuk setiap mahasiswa
for i in range(jumlah):
    print(f"\nData Mahasiswa ke-{i+1}")
    nim = input("Masukkan NIM: ")            # Input NIM
    nama = input("Masukkan Nama: ")          # Input Nama

    nilai_mk = []  # List untuk menyimpan tuple (mata kuliah, nilai)

    jml_mk = int(input("Masukkan jumlah mata kuliah: "))

    # Input untuk setiap mata kuliah
    for j in range(jml_mk):
        mk = input(f"  Mata kuliah ke-{j+1}: ")         # Nama mata kuliah
        nilai = float(input(f"  Nilai untuk {mk}: "))   # Nilai mata kuliah
        nilai_mk.append((mk, nilai))  # Simpan sebagai tuple dalam list

    # Simpan ke dictionary dengan format:
    # { NIM: [Nama, [(mata_kuliah, nilai), ...]] }
    data_mahasiswa[nim] = [nama, nilai_mk]

# Menampilkan seluruh data mahasiswa
print("\n=== Daftar Data Mahasiswa ===")
for nim, data in data_mahasiswa.items():
    nama = data[0]
    daftar_nilai = data[1]

    print(f"\nNIM       : {nim}")
    print(f"Nama      : {nama}")
    print("Nilai     :")
    total = 0
    for mk, nilai in daftar_nilai:
        print(f"  {mk} : {nilai}")
        total += nilai

    rata2 = total / len(daftar_nilai) if daftar_nilai else 0
    print(f"Rata-rata : {rata2:.2f}")