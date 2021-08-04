# File : PR09A_2072037
# Penulis : Willy Natanael Sijabat
# Deskripsi : Membuat program menyeleksi data dalam array yang bilangannya adalah
#             ganjil , lalu hasilnya di print
# Kamus data : N = tipe int = var untuk alokasi data (muatan data)
#              bil = array
#              i = var counter

#Program Include input process and output
def main():
    N = int(input("n: "))
    bil = N * [None] # type arrray of integer

    for i in range(0,N,1):
        bil[i] = int(input())

    for i in range(0,N,1):
        if(bil[i] % 2 != 0):
            print(bil[i],end = " ")
if __name__=='__main__':
    main()
