# File : PR06A_2072037.py
# Nama : Willy Natanael Sijabat 2072037
# Deskrpsi : Membuat program while dummy (inputan != 0), dengan tujuan program
#            untuk mencetak bon pembelian kopi dan non kopi dengan pengkondisian
#            yang benar
# Kamus : pilih = tipe integer
#         temp1 = tipe integer
#         temp2 = tipe integer
#         temp3 = tipe integer
#         temp4 = tipe integer
#         pilih = tipe integer
#         jenis = tipe integer
#         priceA = tipe integer
#         priceB = tipe integer
#         priceC = tipe integer
#         priceD = tipe integer
#         totalbayar = tipe integer
def main() :
    print("="*40)
    print("Menu: 1 Kopi 2 Non-Kopi 0.Selesai")
    pilih = int(input("pilih : "))
    temp1 = 0
    temp2 = 0
    temp3 = 0
    temp4 = 0
    while(pilih != 0):
        if(pilih == 1):
            print("-"*40)
            print("Jenis: 1 Americano, 2 Latte")
            jenis = int(input("pilih : "))
            if(jenis == 1):
                temp1 = temp1 + 1
                print("="*40)
                print("Menu: 1 Kopi 2 Non-Kopi 0.Selesai")
                pilih = int(input("pilih : "))
            elif(jenis == 2):
                temp2 = temp2 + 1
                print("="*40)
                print("Menu: 1 Kopi 2 Non-Kopi 0.Selesai")
                pilih = int(input("pilih : "))
        elif(pilih == 2):
            print("-"*40)
            print("Jenis: 1 Susu, 2 Teh")
            jenis = int(input("Jenis : "))
            if(jenis == 1):
                temp3 = temp3 + 1
                print("="*40)
                print("Menu: 1 Kopi 2 Non-Kopi 0.Selesai")
                pilih = int(input("pilih : "))
            elif(jenis == 2):
                temp4 = temp4 + 1
                print("="*40)
                print("Menu: 1 Kopi 2 Non-Kopi 0.Selesai")
                pilih = int(input("pilih : "))
    print("="*40)
    priceA = temp1*14000
    priceB = temp2*14000
    priceC = temp3*12000
    priceD = temp4*12000
    totalbayar = priceA+priceB+priceC+priceD
    print("Pesanan: ")
    print(temp1,"Americano \tRp. ",priceA)
    print(temp2,"Latte \tRp. ",priceB)
    print(temp3,"Susu \t\tRp. ",priceC)
    print(temp4,"Teh \t\tRp. ",priceD)
    print("-"*40)
    print("Total Bayar \tRp. ",totalbayar)
if __name__ == '__main__':
    main()

        
    
