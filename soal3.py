gaji = int(input("masukkan gaji perjam yang anda inginkan:"))
jam  = int(input("masukkan jumlah jam kerja yang akan dilakukan dalam 1 minggu:"))
gaji_kotor = gaji*jam*5
gaji_bersih = gaji_kotor*((100-14)/100)

print("Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak adalah:",round(gaji_kotor))
print("Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak adalah:",round(gaji_bersih))

pakaian = gaji_bersih*(10/100)
alat_tulis = gaji_bersih*(1/100)
gaji_bersih = gaji_bersih - (pakaian+alat_tulis)
sumbangan = gaji_bersih*(25/100)
yatim = (1000*(sumbangan//1000))*(30/100)
dhuafa = sumbangan - yatim

print("Jumlah uang yang akan Budi habiskan untuk membeli baju dan aksesoris:",round(pakaian))
print("Jumlah uang yang akan Budi habiskan untuk membeli alat tulis:",round(alat_tulis))
print("Uang yang akan Budi sedekahkan adalah:",round(sumbangan))
print("Uang yang akan diterima oleh yatim:",round(yatim))
print("Uang yang akan diterima oleh dhuafa:",round(dhuafa))