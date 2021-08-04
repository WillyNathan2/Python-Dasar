# File : T06A_2072037.py
# Nama : Willy Natanael Sijabat 2072037
# Deskripsi : latihan uts , membuat program menghitung jumlah potongan
# Kamus : lelang = tipe integer
#         first  = tipe integer
#         second = tipe integer
#         lelang1 = tipe integer
#         lelang2 = tipe integer

def main ():
    # Program include input process and output
    lelang = int(input("Harga Lelang Rp. "))
    print("="*40)
    first = int(input("Potongan Pertama (%) : "))
    second = int(input("Potongan Kedua (%) : "))
    print("="*40)
    lelang1 = lelang - (round (lelang*(first/100)))
    lelang2 = lelang1 -(round (lelang1*(second/100))) 
    print("Setelah potongan pertama : Rp. ",round(lelang1))
    print("Setelah potongan kedua Rp. ",round (lelang2))
    print("Total Potongan : Rp. ",round(lelang*(first/100))+round(lelang1*(second/100)))
    print("="*40)
if __name__ == '__main__':
    main()
