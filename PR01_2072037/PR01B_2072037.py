# File: PR01B_2072037.py
# Penulis : <Willy Natanael Sijabat>
# Deskripsi : Membuat program dapat menukar value variabel menggunakan temp
# Kamus
# Tuang1 , Tuang2 , Tuang3 = variabel bertipe string, X , Y = variabel bertiper string

def main ():
# Program
    Tuang1 = str(input("Gelas 01 :"))
    Tuang2 = str(input("Gelas 02 :"))
    Tuang3 = str(input("Gelas 03 :"))
    print("setelah ditukar")

    X = Tuang1
    Y = Tuang2
    Tuang1 = Tuang3
    Tuang2 = X
    Tuang3 = Y

    print("Gelas 01:",Tuang1)
    print("Gelas 02:",Tuang2)
    print("Gelas 03:",Tuang3)
if __name__ == '__main__':
    main()
