# File : T12C_2072037.py
# Nama : Willy Natanael Sijabat 2072037
# Deskripsi : Membuat program mencari nrp dengan sentinel

# Kamus Lokal :
# nrp : array of str
# cari : validation , tipe str
# ix : indeks (tipe of int)
# i : var counter
def sentinelSearch(nrp,n,cari):
    nrp = nrp + [None]
    nrp[n] = cari
        
    i = 0
    while (nrp[i] != cari):
        i = i + 1
    if(i < n):
        ix = i
    else:
        ix = -1
    return ix

# Kamus Lokal :
# validasi = untuk memanggil fungsi sentinel Search
def printALL(n,nama,nrp,cari):
    while (cari != "99999"):
        validasi = sentinelSearch(nrp,n,cari)
        if(validasi >= 0):
            print("Nama dari",nrp[validasi],"adalah",nama[validasi])
        else:
            print("Data NRP yang dicari tidak ditemukan")
        cari = str(input("NRP yang dicari : "))
    print("Selesai")

# kamus data :
# n = tipe int (alokasi data)
# nama = array of str
# nrp = array of str
# i = var counter
def main ():
    n = int(input("Jumlah data : "))
    nama = n * [None]
    nrp = n * [None]
    for i in range (0,n,1):
        nrp[i] = str(input("NRP : ")) 
        nama[i] = str(input("Nama : "))
               
    cari = str(input("NRP yang dicari : "))
    printALL(n,nama,nrp,cari)
            
if __name__ == '__main__':
    main()
