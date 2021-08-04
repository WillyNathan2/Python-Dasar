# File: PR02C_2072037.py
# Penulis : Willy Natanael Sijabat 2072037
# Deskripsi : Membuat Bon pembelian pakaian sesuai parameter jenis,bahan,ukuran
# kamus : PILIH      = TIPE STRING
#         BAHAN      = TIPE STRING
#         SIZE       = TIPE STRING
#         paying     = TIPE INTEGER
#         backpaying = TIPE INTEGER


def main ():
#PROGRAM INCLUDE INPUT AND OUTPUT
    print("=====================================================")
    print("Jenis Pakaian : 1. kaos, 2. kemeja, 3.jaket")
    PILIH = str(input("Jenis : "))
    if(PILIH == "1"):
        print("Pilihan Warna: m. maroon, n. navy, l.lilac")
    if(PILIH == "2"):
        print("Motif Kemeja k. kotak-kotak, p. polos")
    if(PILIH == "3"):
        print("Bahan Jaket b. baby terry, d. denim, t. taslan")
    BAHAN = str(input("Bahan :"))
    print("Ukuran Pakaian: s,m,l")
    SIZE = str(input("Ukuran: "))
    print("=====================================================")
    print("Barang yang dibeli :")
    if(PILIH == "1" and BAHAN == "m" and SIZE == "s"):
        print("1 Kaos berwarna maroon berukuran s ")
        print("Harga : Rp. 70000")
        print("=====================================================")
        paying = int(input("Uang yang dibayarkan Rp. "))
        backpaying = paying - 70000
        print("Kembalian Rp.",backpaying)
        print("=====================================================")
    if(PILIH == "1" and BAHAN == "m" and SIZE == "m"):
        print("1 Kaos berwarna maroon berukuran m ")
        print("Harga : Rp. 84000")
        print("=====================================================")
        paying = int(input("Uang yang dibayarkan Rp. "))
        backpaying = paying - 84000
        print("Kembalian Rp.",backpaying)
        print("=====================================================")
    if(PILIH == "1" and BAHAN == "m" and SIZE == "l"):
        print("1 Kaos berwarna maroon berukuran l ")
        print("Harga : Rp. 98000")
        print("=====================================================")
        paying = int(input("Uang yang dibayarkan Rp. "))
        backpaying = paying - 98000
        print("Kembalian Rp.",backpaying)
        print("=====================================================")


    if(PILIH == "1" and BAHAN == "n" and SIZE == "s"):
        print("1 Kaos berwarna navy berukuran s ")
        print("Harga : Rp. 70000")
        print("=====================================================")
        paying = int(input("Uang yang dibayarkan Rp. "))
        backpaying = paying - 70000
        print("Kembalian Rp.",backpaying)
        print("=====================================================")
    if(PILIH == "1" and BAHAN == "n" and SIZE == "m"):
        print("1 Kaos berwarna navy berukuran m ")
        print("Harga : Rp. 84000")
        print("=====================================================")
        paying = int(input("Uang yang dibayarkan Rp. "))
        backpaying = paying - 84000
        print("Kembalian Rp.",backpaying)
        print("=====================================================")
    if(PILIH == "1" and BAHAN == "n" and SIZE == "l"):
        print("1 Kaos berwarna navy berukuran l ")
        print("Harga : Rp. 98000")
        print("=====================================================")
        paying = int(input("Uang yang dibayarkan Rp. "))
        backpaying = paying - 98000
        print("Kembalian Rp.",backpaying)
        print("=====================================================")


    if(PILIH == "1" and BAHAN == "l" and SIZE == "s"):
        print("1 Kaos berwarna lilac berukuran s ")
        print("Harga : Rp. 70000")
        print("=====================================================")
        paying = int(input("Uang yang dibayarkan Rp. "))
        backpaying = paying - 70000
        print("Kembalian Rp.",backpaying)
        print("=====================================================")
    if(PILIH == "1" and BAHAN == "l" and SIZE == "m"):
        print("1 Kaos berwarna lilac berukuran m ")
        print("Harga : Rp. 84000")
        print("=====================================================")
        paying = int(input("Uang yang dibayarkan Rp. "))
        backpaying = paying - 84000
        print("Kembalian Rp.",backpaying)
        print("=====================================================")
    if(PILIH == "1" and BAHAN == "l" and SIZE == "l"):
        print("1 Kaos berwarna lilac berukuran l ")
        print("Harga : Rp. 98000")
        print("=====================================================")
        paying = int(input("Uang yang dibayarkan Rp. "))
        backpaying = paying - 98000
        print("Kembalian Rp.",backpaying)
        print("=====================================================")

    if(PILIH == "2" and BAHAN == "k" and SIZE == "s"):
        print("1 kemeja bermotif kotak-kotak berukuran s ")
        print("Harga : Rp. 100000")
        print("=====================================================")
        paying = int(input("Uang yang dibayarkan Rp. "))
        backpaying = paying - 100000
        print("Kembalian Rp.",backpaying)
        print("=====================================================")
    if(PILIH == "2" and BAHAN == "p" and SIZE == "s"):
        print("1 kemeja bermotif polos berukuran s ")
        print("Harga : Rp. 100000")
        print("=====================================================")
        paying = int(input("Uang yang dibayarkan Rp. "))
        backpaying = paying - 100000
        print("Kembalian Rp.",backpaying)
        print("=====================================================")

    if(PILIH == "2" and BAHAN == "k" and SIZE == "m"):
        print("1 kemeja bermotif kotak-kotak berukuran m ")
        print("Harga : Rp. 120000")
        print("=====================================================")
        paying = int(input("Uang yang dibayarkan Rp. "))
        backpaying = paying - 120000
        print("Kembalian Rp.",backpaying)
        print("=====================================================")
    if(PILIH == "2" and BAHAN == "p" and SIZE == "m"):
        print("1 kemeja bermotif polos berukuran m ")
        print("Harga : Rp. 120000")
        print("=====================================================")
        paying = int(input("Uang yang dibayarkan Rp. "))
        backpaying = paying - 120000
        print("Kembalian Rp.",backpaying)
        print("=====================================================")

    if(PILIH == "2" and BAHAN == "k" and SIZE == "l"):
        print("1 kemeja bermotif kotak-kotak berukuran l ")
        print("Harga : Rp. 140000")
        print("=====================================================")
        paying = int(input("Uang yang dibayarkan Rp. "))
        backpaying = paying - 140000
        print("Kembalian Rp.",backpaying)
        print("=====================================================")
    if(PILIH == "2" and BAHAN == "p" and SIZE == "l"):
        print("1 kemeja bermotif polos berukuran l ")
        print("Harga : Rp. 140000")
        print("=====================================================")
        paying = int(input("Uang yang dibayarkan Rp. "))
        backpaying = paying - 140000
        print("Kembalian Rp.",backpaying)
        print("=====================================================")



    if(PILIH == "3" and BAHAN == "b" and SIZE == "s"):
        print("1 jacket berbahan baby terry berukuran s ")
        print("Harga : Rp. 150000")
        print("=====================================================")
        paying = int(input("Uang yang dibayarkan Rp. "))
        backpaying = paying - 150000
        print("Kembalian Rp.",backpaying)
        print("=====================================================")
    if(PILIH == "3" and BAHAN == "d" and SIZE == "s"):
        print("1 jacket berbahan denim berukuran s ")
        print("Harga : Rp. 150000")
        print("=====================================================")
        paying = int(input("Uang yang dibayarkan Rp. "))
        backpaying = paying - 150000
        print("Kembalian Rp.",backpaying)
        print("=====================================================")
    if(PILIH == "3" and BAHAN == "t" and SIZE == "s"):
        print("1 jacket berbahan taslan berukuran s ")
        print("Harga : Rp. 150000")
        print("=====================================================")
        paying = int(input("Uang yang dibayarkan Rp. "))
        backpaying = paying - 150000
        print("Kembalian Rp.",backpaying)
        print("=====================================================")

    if(PILIH == "3" and BAHAN == "b" and SIZE == "m"):
        print("1 jacket berbahan baby terry berukuran m ")
        print("Harga : Rp. 180000")
        print("=====================================================")
        paying = int(input("Uang yang dibayarkan Rp. "))
        backpaying = paying - 180000
        print("Kembalian Rp.",backpaying)
        print("=====================================================")
    if(PILIH == "3" and BAHAN == "d" and SIZE == "m"):
        print("1 jacket berbahan denim berukuran m ")
        print("Harga : Rp. 180000")
        print("=====================================================")
        paying = int(input("Uang yang dibayarkan Rp. "))
        backpaying = paying - 180000
        print("Kembalian Rp.",backpaying)
        print("=====================================================")
    if(PILIH == "3" and BAHAN == "t" and SIZE == "m"):
        print("1 jacket berbahan taslan berukuran m ")
        print("Harga : Rp. 180000")
        print("=====================================================")
        paying = int(input("Uang yang dibayarkan Rp. "))
        backpaying = paying - 180000
        print("Kembalian Rp.",backpaying)
        print("=====================================================")

    if(PILIH == "3" and BAHAN == "b" and SIZE == "l"):
        print("1 jacket berbahan baby terry berukuran l ")
        print("Harga : Rp. 210000")
        print("=====================================================")
        paying = int(input("Uang yang dibayarkan Rp. "))
        backpaying = paying - 210000
        print("Kembalian Rp.",backpaying)
        print("=====================================================")
    if(PILIH == "3" and BAHAN == "d" and SIZE == "l"):
        print("1 jacket berbahan denim berukuran l ")
        print("Harga : Rp. 210000")
        print("=====================================================")
        paying = int(input("Uang yang dibayarkan Rp. "))
        backpaying = paying - 210000
        print("Kembalian Rp.",backpaying)
        print("=====================================================")
    if(PILIH == "3" and BAHAN == "t" and SIZE == "l"):
        print("1 jacket berbahan taslan berukuran l ")
        print("Harga : Rp. 210000")
        print("=====================================================")
        paying = int(input("Uang yang dibayarkan Rp. "))
        backpaying = paying - 210000
        print("Kembalian Rp.",backpaying)
        print("=====================================================")
if __name__ == '__main__':
    main()
