# File : T12A_2072037.py
# Nama : Willy Natanael Sijabat 2072037
# Deskripsi program : membuat program sequential search data terurut,
#                     serta jika diinput maka akan menampilkan data yang
#                     dicari

#Kamus Lokal :
# ix = tipe int -- > untuk validasi
# i = var counter
# MM = array of int
# cari = tipe int(pada main) --> untuk mencari data
def SortedSearch(n,MM,cari):
    ix = 0
    i = 0
    while(i < (n - 1) and MM[i] < cari):
        i += 1
    if (MM[i] == cari):
        ix = i
    else:
        ix = -1
    return ix
    
# Kamus data :
# n = tipe int(alokasi data)
# MM = array of int
# cari = tipe int --> untuk mencari data
def main():
    n = int(input("N : "))
    MM = n * [None]
    for i in range (0,n,1):
        MM[i] = int(input())
    cari = int(input("Angka yang dicari : "))
    MM = SortedSearch(n,MM,cari)
    if(MM >= 0):
        print("Angka",cari,"ditemukan pada indeks ke-",MM)
    else:
        print("Angka",cari,"tidak ditemukan")
if __name__ == '__main__':
    main()
