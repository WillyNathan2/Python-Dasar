# File : PR09C_2072037.py
# Penulis : Willy Natanael Sijabat 2072037
# Deskripsi program : mencari irisan berupa angka unik
# kamus data = n : tipe int (alokasi memory untuk array n)
#              array1 : type array of int (array penyimpanan data n)
#              m : tipe int (alokasi memory untuk array m)
#              array2 : type array of int (array penyimpanan data m)
#              gabungan : type array of int (array untuk gabungan dari kedua array m dan n)
#              indeks : untuk temp , jika data pada m dan n sama maka akan dimasukan ke
#                       array gabungan [indeks]
#              i = var counter
#              j = var counter

#Program Include Input Proccess and output
def main():
    # Input
    n = int(input("n : "))
    array1 = [None] * n
    for i in range (0,n,1):
        array1[i] = int(input())

    # Input
    m = int(input("m : "))
    array2 = [None] * m
    for i in range (0,m,1):
        array2[i] = int(input())

    gabungan = [None] * (m + n)
    indeks = 0

    # Proccess
    for i in range (0,n,1):
        for j in range (0,m,1):
            if(array1[i] == array2[j] not in gabungan):
                gabungan[indeks] = array1[i]
                indeks += 1

    # Output
    print("Intersection : ",end = " ")
    for i in range (0,(m+n),1):
        if(gabungan[i] != None):
            print(gabungan[i], end = " ")
if __name__ =='__main__':
    main()

