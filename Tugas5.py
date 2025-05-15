# Input data dari user
nama = input("Masukkan nama: ")
umur = input("Masukkan umur: ")
alamat = input("Masukkan alamat: ")

# Output biodata dengan format()
biodata = "Nama saya adalah {}, umur saya {} tahun, dan saya tinggal di {}.".format(nama, umur, alamat)
print(biodata)
