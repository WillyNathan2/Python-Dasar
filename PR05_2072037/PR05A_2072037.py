# File : PR05A_2072037.py
# Nama : Willy Natanael Sijabat 2072037
# Deskripsi : Membuat program yang memunculkan pola berderet yang panjang nya
#             ditentukan oleh parameter n , dengan perulangan yang akan membentuk
#             pola persegi (kotak / n*n),dan dibuat perulangan lagi dengan pengkondisian jika increment pertamnya 1 atau n,
#             maka pada baris pertama mencetak
#             deret 1 sampai n yang jika pada perulangan keduanya > 1 & < n akan mencetak bintang
#             lalu pada perulangan pertama di increment yang lebih dari > 1 dan < n
#             akan mencetak pola deret 1 sampai n namun jika increment di perulangan kedua nya lebih
#             dari 1 dan kurang dari n akan mencetak kosong (" ")
# Kamus : n = tipe integer
#         i = tipe integer
#         j = tipe integer
def main ():
    n = int(input("n : "))
    for i in range (1,n+1,1):
        for j in range (1,n+1,1):
            if(i == 1 or i == n):
                if(j > 1 and j < n):
                    print("*",end = " ")
                else:
                    print(j,end = " ")
            else:
                if(j > 1 and j < n):
                    print(" ",end = " ")
                else:
                    print(j,end = " ")      
        print()
if __name__ == '__main__':
    main()
