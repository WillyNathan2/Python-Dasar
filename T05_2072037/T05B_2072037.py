# File : T05B_2072037.py
# Nama : Willy Natanael Sijabat
# Deskripsi : Membuat program trianngle , prinsip nya adalah membuat program
#             dengan bentukan persegi terlebih dahulu (n x n)
#             dan untuk patokan membuat triangle nya adalah , didalam looping for
#             terdapat pengkondisian , jika value x dikurang dengan (input + 1), maka
#             dia akan mengeluarkan output var value i , dan jika sudah tidak memenuhi
#             maka dia akan memberikan output bintang
# Kamus Data : i      = tipe integer
#              number = tipe integer
#              x      = tipe integer


def main ():
# Program

    #Input
    number = int(input(""))
    i = 1
    #process with output
    while(i <= number):
        for x in range (1,number + 1 , 1):
            if (x <= (number - i)):
                print(i,end=" ")
            else:
                print("*",end=" ")
        i += 1
        print()
if __name__ == '__main__':
    main()
