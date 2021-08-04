# File : PR05C_2072037.py
# Nama : Willy Natanael Sijabat 2072037
# Deskripsi : membuat program segitiga siku-siku yang parameter sisi (tinggi) nya
#             ditentukan oleh n , dan parameter jumlah n juga menentukan banyak nya segitiga
# Kamus : n = Tipe Integer
#         i = Tipe Integer
#         j = tipe Integer
#         k = tipe Integer
def main ():
    n = int(input("n : "))
    for i in range (1,n+1,1):
        for j in range (1,n+1,1):
            for k in range (1,i+1,1):
                print("*",end=" ")
            print("  "*(n-i),end="")
            if (j == 1 or j < n):
                print("|",end=" ")
        print()
if __name__ == '__main__':
    main()
