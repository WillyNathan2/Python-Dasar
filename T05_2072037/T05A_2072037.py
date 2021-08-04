# File : T05A_2072037
# Nama : Willy Natanael Sijabat
# Deskrpsi : membuat program yang akan membentuk sebuah persegi panjang
#            berukuran (inputan * (2 * inputan)
#            prinsip nya sama dengan module yang diberikan bu mewati (module 5)
# Kamus Data : n = tipe integer
#              i = tipe integer
#              x = tipe integer


def main ():

# Program include input , process and output
    n = int(input(""))
    for i in range (1, n+1 ,1):
        for x in range(1,(n*2)+1,1):
            print("*", end=" ")
        print()
if __name__ == '__main__':
    main()
