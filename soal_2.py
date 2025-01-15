import pandas as p

nilai = [
    [90,80],
    [50,60],
    [65,70],
]

index = ['Mahasiswa 1','Mahasiswwa 2', 'Mahasiswa 3'],
columns= ['Nama','Algoritma dan Struktur Data 2','Matematika Numerik']

mean = nilai.mean(axis=0)
rata = nilai.mean(axis=1)

print (nilai)
print(mean)
print(rata)