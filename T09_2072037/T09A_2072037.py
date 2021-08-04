# File = T09A_2072037.py
# Nama = Willy Natanael Sijabat 2072037
# Deskripsi program = membuat program bilangan deret integer yang
#                     jika di input nya bil apapun , maka result nya
#                     harus mengeprint indeks array ke 0 dan index genap
# Kamus = N : Tipe INT
#         temp : Tipe INT
def main ():
    N = int(input("n : "))
    bil = N * [None] #Type array of integer
    
    for i in range (0,N,1):
        temp = int(input())
        if (i == 0 or i % 2 == 0):
            bil[i] = temp
    for i in range (0,N,1):
        if (i == 0 or i % 2 == 0):
            print(bil[i],end = " ")
            
if __name__ =='__main__':
    main()
