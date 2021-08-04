# File    : T03A_2072037.py
# Penulis : Willy Natanael Sijabat 2072037
# Deskripsi : Membuat Kelipatan baris deret dari input dengan rentang yang ditentukan oleh
#             2 variabel
# Kamus : n = Tipe Integer
#         m = Tipe Integer
#         x = Tipe Integer


def main ():
#Program

    #begin , end , increment
    n = int(input("n :"))
    m = int(input("m :"))
    x = int(input("x :"))
    for i in range (n,m,x):
        print(i,",", end=" ")
if __name__ == '__main__':
    main()
