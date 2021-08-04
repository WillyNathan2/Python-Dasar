# File : PR12A_2072037.py
# Nama : Willy Natanael Sijabat 2072037
# Deskripsi Program : Buatlah sebuah program yang menerima N buah bilangan.
#                     Lalu program akan menerima angka yang dicari.

# Kamus Lokal
# Fungsi sequentialSearch() berguna untuk validasi data
# dengan verifikasi boelean
# Found = tipe boolean
# i = var counter
# ix = var int -- > validasi
def sequentialSearch(n,cari,Arr):
    i = 0
    Found = False
    while (i < n and Found == False):
        if (Arr[i] == cari):
            Found = True
        else:
            i = i + 1
    if (Found == True):
        ix = i
    else:
        ix = -1
    return ix

# Kamus Data
# n = tipe int
# Arr = array of int
# cari = tipe int
# a = panggil fungsi (hasil return)(tipe int)
def main ():
    n = int(input("N = "))
    Arr = [None] * n

    for i in range (0,n,1):
        Arr[i] = int(input(""))
         
    cari = int(input("Angka yang dicari: "))
    a = sequentialSearch(n,cari,Arr)
    if (a >= 0):
        print ("Angka",cari,"ditemukan pada indeks ke-",a,".")
    else:
        print ("Angka",cari,"tidak ditemukan.")

if __name__ == '__main__':
    main()
