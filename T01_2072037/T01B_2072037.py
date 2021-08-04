# File T01B_2072037.py
# Penulis : < Willy Natanael Sijabat >
# Deskripsi :
# Saya medeklarasikan beberapa variabel , yang pertama adalah X lalu Y , dan yang terakhir , penggunaannya untuk Temp yaitu C
# Saya membuat input yang value nya berupa Integer untuk Variabel yang di input antara lain X dan Y
# Hasil Outpunya nanti adalah , setiap variabel yang dimaksukan angka yang berjenis integer , value nya akan ditukarkan


def main ():
# Program
    X = int(input("Nilai X :"))
    Y= int(input("Nilai Y :"))

    print("Sebelum Ditukar")
    print("Nilai X:", X)
    print("Nilai Y:", Y)

    print("Setelah Ditukar")

    C = X
    X = Y
    Y = C

    print ("Nilai X:", X)
    print ("Nilai Y:", Y)
    
if __name__ == '__main__':
    main()
