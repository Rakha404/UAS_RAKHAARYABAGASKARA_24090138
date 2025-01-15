while True:
  nama = input("Masukkan Nama: ")
  nim = input("Masukkan NIM: ")

  print ("Mahasiswa bernama : ",nama,"dengan NIM : ",nim)

  ulangi = input('Apakah anda ingin melanjutkan? y/ t :')

  if ulangi == "y":
    continue
  elif ulangi == "t":
    print("Terima Kasih :)")
    break
  else:
      print("Inputan salah")
      ulangi = input('Apakah anda ingin melanjutkan? y/t : ')
  if ulangi == "y":
    continue
  elif ulangi == "t":
    print("Terima Kasih :)")
    break