# File    : T03B_2072037.py
# Penulis : Willy Natanael Sijabat 2072037
# Deskripsi : Membuat program untuk checker value int apakah positif/negatif
#             dan apabila 0 , dia akan berhenti melooping dan memberi alert selesai/(sampai jumpa lagi)
# Kamus : n = tipe integer


def main ():
#Program
    n = int(input("n :"))
    while(n != 0):
        if ( n%2 == 0 and n > 0):
            print(n,"adalah bilangan genap positif")
        if(n%2 == 0 and n < 0):
            print(n,"adalah bilangan genap negatif")
        if( n%2 != 0 and n > 0):
            print(n,"adalah bilangan ganjil positif")
        if(n%2 != 0 and n < 0):
            print(n,"adalah bilangan ganjil negatif")
        n = int(input("n :"))

    print("sampai jumpa lagi !")

            
    
if __name__ == '__main__':
    main()
