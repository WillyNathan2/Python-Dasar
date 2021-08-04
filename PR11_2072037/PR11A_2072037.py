# File : PR11A_2072037.py
# Penulis : Willy Natanael Sijabat 2072037
# Deskripsi : Membuat pattern x dengan matriks yang sudah di reverse
#             (matriks merupakan array 2 dimensi)

# Kamus Lokal :
# function insert berfungsi untuk memasukan value matriks
# i = var counter
# j = var counter
# MM = array of int
def insert(n,MM):
    for i in range (0,n,1):
        for j in range (0,n,1):
            MM[i][j] = int(input())
    print()
    return MM

# Kamus Lokal :
# function deklarasi berfungsi untuk mendeclare
# array
# i = var counter

def deklarasi(n):
    m = n
    MM = n * [None]
    for i in range (0,n,1):
        MM[i] = m * [None] 
    return MM


# Kamus Lokal :
# xMirror = berfungsi untuk membuat pattern x dan mirror pada
#           matriks yg terbentuk
# i = var counter
# j = var counter
def xMirror(n,MM):

    for i in range (n-1,-1,-1):
        for j in range (0,n,1):
            if( i == j or ((n - j) - 1) == i ):
                print(MM[i][j] , end = " ")
            else:
                print(" ", end = " ")
        print()

# Kamus data
# n = tipe int = (alokasi memory array(batas n*n -- > untuk matriks))
# MM = array of int

def main ():
    n = int(input("besar matrikx : "))
    MM = deklarasi(n)
    MM = insert(n,MM)
    xMirror(n,MM)
if __name__ == '__main__':
    main()
