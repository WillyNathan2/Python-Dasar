# File: PR01C_2072037.py
# Penulis : <Willy Natanael Sijabat>
# Deskripsi : Membuat converter nilai uang per tiap jenis lembar(value)
# Kamus
# NominalRslt,NominalAkhir,Sisa,Nominal20k,Nominal10k,Nominal5k,Nominal2k = variabel bertipe integer
# Nominal1k,Nominal5ratus,Nominal2ratus,Nominalseratus = variabel bertipe integer


def main ():
 # Program
    print("====================================")
    NominalRslt = int(input("Nominal ="))
    print("====================================")
    print("Dalam lembaran:")
    NominalAkhir = NominalRslt // 100000
    Sisa = NominalRslt % 100000 // 50000
    Nominal20k = NominalRslt % 100000 % 50000 // 20000
    Nominal10k = NominalRslt % 100000 % 50000 % 20000 // 10000
    Nominal5k = NominalRslt % 100000 % 50000 % 20000 % 10000 // 5000
    Nominal2k = NominalRslt % 100000 % 50000 % 20000 % 10000 % 5000 // 2000
    Nominal1k = NominalRslt % 100000 % 50000 % 20000 % 10000 % 5000 % 2000 // 1000
    Nominal5ratus = NominalRslt % 100000 % 50000 % 20000 % 10000 % 5000 % 2000 % 1000 // 500
    Nominal2ratus = NominalRslt % 100000 % 50000 % 20000 % 10000 % 5000 % 2000 % 1000 % 500 // 200
    Nominalseratus = NominalRslt % 100000 % 50000 % 20000 % 10000 % 5000 % 2000 % 1000 % 500 % 200 // 100
    print(NominalAkhir,"lembar uang seratus ribu")
    print(Sisa,"lembar uang lima puluh ribu")
    print(Nominal20k,"lembar uang dua puluh ribu")
    print(Nominal10k,"lembar uang sepuluh ribu")
    print(Nominal5k,"lembar uang lima ribu ")
    print(Nominal2k,"lembar uang dua ribu")
    print(Nominal1k,"lembar uang seribu")
    print(Nominal5ratus,"lembar uang lima ratus")
    print(Nominal2ratus,"lembar uang dua ratus")
    print(Nominalseratus,"lembar uang seratus")
    print("==================================")
if __name__ == '__main__':
    main()
