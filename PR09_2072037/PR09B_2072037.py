# File : PR09B_2072037.py
# Penulis : Willy Natanael Sijabat 2072037
# Deskripsi Program : membuat program dengan menerima data
#                     baik itu data nama dan warna kesukaannya
#                     lalu outputnya harus menampilkan jika
#                     warna yg dicari sudah ditentukan , maka namanya akan keluar
#                     dengan informasi detail berdasarkan berapa orangnya
# Kamus Data : N = Tipe Int (untuk meminta brp total data)
#              datanama = array nama
#              datawarna = array warna
#              jumlahmanusia = tipe int
#              hayo = tipe string
#              validasi = tipe int
#              confrim2 = tipe int
#              i = var counter
#              
def main():
    #input
    N = int(input("Jumlah Data : "))
    datanama = N * [None] #Type array of string
    datawarna = N * [None] #Type array of string
    jumlahmanusia = 0
    #Proccess with Output
    for i in range (0,N,1):
        datanama[i] = str(input("nama : "))
        datawarna[i] = str(input("warna kesukaan : "))

    hayo = str(input("Siapa saja yang menyukai warna : "))
    validasi = 0
    confirm = 0
    jumlahmanusia = 0
    for i in range (0,N,1):
        if(datawarna[i] == hayo):
            jumlahmanusia += 1
            validasi = 1
            
    if(validasi == 1):
        print("ada",jumlahmanusia,"orang yang menyukai warna",hayo,"yaitu",end = " ")
        confirm2 = 0
        for i in range (0,N,1):
            if(datawarna[i] == hayo):
                confirm2 = i
                print(datanama[confirm2],end = " ")

    elif(validasi != 1):
        print("Tidak ada orang yang menyukai warna ",hayo,"pada data")

if __name__ =='__main__':
    main()
