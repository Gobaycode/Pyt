persen_tunjangan = 0.2
persen_pajak = 0.15

Nama_karyawan = str(input("Masukan Nama : "))
Gaji_Pokok = int(input("Masukan Gaji : "))

tunjangan = persen_tunjangan * Gaji_Pokok
pajak = persen_pajak * (Gaji_Pokok + tunjangan)
Gaji_Bersih = Gaji_Pokok + tunjangan - pajak
#MUHAMAD DAFFA ABYAN (251011701231)
print("-----------------")
print("NAMA :",Nama_karyawan)
print("Gaji Bersih :", Gaji_Bersih)