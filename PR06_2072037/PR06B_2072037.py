# File : PR06B_2072037.py
# Nama : Willy Natanael Sijabat 2072037
# Deskripsi : Membuat program membentuk persegi (n x n) dengan metode perulangan
#             dan didalam kotak dibuat pengkondisian untuk membentuk segitiga siku-siku
# Kamus : i = tipe integer
#         j = tipe integer
#         k = tipe integer
#         n = tipe integer
def main() :
# Program
    n = int(input("n: "))
    for i in range(1,n+1,1):
        for j in range(1,4,1):
            for k in range (1,n+1,1):
                if (i <= 1 or i >= n or k <= 1 or k >= n):
                    print(n,end=" ")
                elif(k >= i):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            if (j>=1 and j<=2):
                print("|",end=" ")
        print()
if __name__ == '__main__':
    main()
