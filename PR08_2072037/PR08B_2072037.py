# File : PR08B_2072037.py
# Nama : Willy Natanael Sijabat 2072037
# Deskripsi Program : membuat program perhitungan umur berdasarkan tanggal lahir (ulang tahun)
# Kamus Data : nama = tipe string
#              tgl  = tipe integer
#              bln  = tipe integer
#              thn  = tipe integer
          

# Funtion validitas
# berfungsi untuk menentukan apakah tanggal ultah yg di input valid /tidak,
# berdasarkan aturan soal yang tidak memperbolehkan tgl kabisat / 31 februari
# kamus : x = tipe integer
def validitas(tgl,bln):
    x = 1
    if (bln == 2 and tgl >= 29):
        x = -1
    else:
        x = 1
    return x 


# Funtion count
# berfungsi melakukan perhitungan umur
# kamus : tahun = tipe integer
#         bulan = tipe integer
def count(tgl,bln,thn,nama):
    #untuk membuat patokan waktu
    import datetime
    d = datetime.date(2021,4,28)
    #patokan waktu - waktu yang sudah di input
    tahun = d.year - thn
    bulan = d.month - bln 
    if(bulan <= 0):
        tahun = tahun - 1
        bulan = bulan + 12
        if(bulan == 12):
            tahun = tahun + 1
            bulan = bulan - 12
            print("Usia",nama,"saat ini adalah ",tahun,"Tahun",bulan,"bulan")
        else:
            print("Usia",nama,"saat ini adalah ",tahun,"Tahun",bulan,"bulan")
    else:
        print("Usia",nama,"saat ini adalah ",tahun,"Tahun",bulan,"bulan")

# Program main untuk input dan output (serta pengkondsian dimana jika def validitas bernilai -1, maka tgl yg di input tidak valid)
def main():
    print("Tanggal Ulang Tahun")
    nama = str(input("Nama    : "))
    tgl = int(input("Tanggal : "))
    bln = int(input("Bulan   : "))
    thn = int(input("Tahun   : "))
    if(validitas(tgl,bln)== -1):
        print("Tanggal Ulang Tahun",nama,"tidak Valid")
    else:
        count(tgl,bln,thn,nama)
if __name__=='__main__':
    main()
