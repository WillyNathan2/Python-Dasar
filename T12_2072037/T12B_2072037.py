# File : T12B_2072037
# Nama : Willy Natanael Sijabat 2072037
# Deskirpsi : Membuat program yang akan menerima masukan N buah bilangan lalu akan
# menampilkan N bilangan tersebut secara terurut menaik.

# Kamus Lokal :
# p = var counter
# i = var counter --- > untuk array
# temp = tipe int --- > penampung
# MM = array of int
# imin = akan dijadikan parameter array untuk urutan dari min
def minSorted(MM,n):
    for p in range (0,(n-1),1):
        imin = p
        for i in range (p+1,n,1):
            if(MM[i] < MM [imin]):
                imin = i
        temp = MM[p]
        MM[p] = MM[imin]
        MM[imin] = temp
    return MM

# kamus data :
# n = tipe int
# MM = array of int
# i = var counter
# arr = array of int
def main():
    n = int(input("N : "))
    MM = n * [None]
    print("Kondisi awal : ")
    for i in range (0,n,1):
        MM[i] = int(input())
    print("Setelah diurutkan : ")
    arr = minSorted(MM,n)
    for i in range (0,n,1):
        print(arr[i], end = " ")
if __name__ == '__main__':
    main()
