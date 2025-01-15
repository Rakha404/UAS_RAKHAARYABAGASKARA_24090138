nilai = [
    [90,80],
    [50,60],
    [65,70],
]

index = ['Mahasiswa 1','Mahasiswwa 2', 'Mahasiswa 3'],
columns= ['Nama','Algoritma dan Struktur Data 2','Matematika Numerik']

def hitung_rata_rata(nilai):
    rata_mk = [sum(col) / len(col) for col in zip(*nilai)]
    rata_mhs = [sum(row) / len(row) for row in nilai]
    return rata_mk, rata_mhs

def hasil(nilai):
    print("Tabel Nilai:")
    for i, baris in enumerate(nilai, start=1):
        print(f"Mahasiswa {i}: {baris}")

    rata_mk, rata_mhs = hitung_rata_rata(nilai)
    print("Rata-rata per Mata Kuliah:")
    for i, rata in enumerate(rata_mk, start=1):
        print(f"Mata Kuliah {i}: {rata:.2f}")

    print("Rata-rata per Mahasiswa:")
    for i, rata in enumerate(rata_mhs, start=1):
        print(f"Mahasiswa {i}: {rata:.2f}")

hasil(nilai)