# File : T04A_2072037.py
# Nama : Willy Natanael Sijabat 2072037
# Deskripsi : Membuat Program Hasil Faktorial
# Kamus = n    : Tipe Integer
#         awal : Tipe Integer
#         i    : Tipe Integer

def main ():
# Program
    n = int(input("n :"))
    awal = 1

    for i in range(1,n + 1):
        awal = awal*i
    print(n,"! =",awal)
if __name__ == '__main__':
    main()    

