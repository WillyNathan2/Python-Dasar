# File : PR11B_2072037.py
# Penulis : Willy Natanael Sijabat 2072037
# Deskripsi Program : Membuat Program Matriks dengan menggunakan Array
#                     sistem nya adalah dengan menginput
#                     matriks , lalu program akan meminta konfirmasi
#                     terkait apakah kita ingin mengetahui jumlah
#                     baris / kolom serta total dari masing-masing konfirmasi


# Kamus Lokal :
# Funtion Insert
# untuk meminta input matriks yang akan dimasukan kedalam array
# i = var counter
# j = var counter
# MM = array of int (matriks)
def insert(n,MM):
    for i in range (0,n,1):
        for j in range (0,n,1):
            MM[i][j] = int(input())
    return MM

# Kamus Lokal
# Funtion deklarasi
# untuk mendeklarasi array 2 dimensi yang akan dibuat
# m = tipe int (alokasi memory)
# n = batas data (tipe int)
# i var counter
# MM  = Array of int
def deklarasi(n):
    m = n
    MM = n * [None]
    for i in range (0,n,1):
        MM[i] = m * [None] 
    return MM

# Kamus Lokal
# funtion hitungKolom berguna untuk pemrosesan
# perhitungan kolom masing-masing
# hasil = tipe int (untuk penampung -- > jumlah total )
# i,j,k = var counter
def hitungKolom(n,MM):
    hasil = 0
    for i in range (0,n,1):
        for j in range (0,n,1):
            for k in range (0,n,1):
                if (k == i):
                    print(MM[j][k] , end = " ")
                    hasil = hasil + MM[j][k]
                    if(j < (n-1)):
                        print("+", end = " ")
                    else:
                        print("=", end = " ")
        print(hasil)

# Kamus Lokal
# funtion hitungBaris berguna untuk menghitung
# pemrosesan perhitungan jumlah baris masing-masing
# i,j = var counter
# hasil = tipe int (untuk total (perhitungan baris))
def hitungBaris(n,MM):
    hasil = 0
    for i in range (0,n,1):
        for j in range (0,n,1):
            hasil = hasil + MM[i][j]
            print(MM[i][j] , end = " ")
            if(j < (n-1)):
                print("+", end = " ")
            else:
                print("=", end = " ")
        print(hasil)

# Kamus Data :
# n = tipe int (alokasi data) (besaran matriks)
# MM = array of int
# confirm = tipe str (validasi untuk meminta apakah mau memunculkan baris/kolom)
def main ():
    n = int(input("besar matrikx : "))
    MM = deklarasi(n)
    MM = insert(n,MM)
    confirm = str(input("Hitung (k kolom / b baris) : "))
    if(confirm == "k"):
        hitungKolom(n,MM)
    elif(confirm == "b"):
        hitungBaris(n,MM)
       
if __name__ == '__main__':
    main()
