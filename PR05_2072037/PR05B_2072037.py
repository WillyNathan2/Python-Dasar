# File : PR05B_2072037.py
# Nama : Willy Natanael Sijabat
# Deskripsi : membuat program pembelian makanan , dengan sistem while nested , serta
#             pengkondisian yang tepat untuk melakukan perhitungan total makanan
#             serta total harga yang harus dibayar
# Kamus : temp1 = tipe integer
#         temp2 = tipe integer
#         temp3 = tipe integer
#         total = tipe integer
#         ayam = tipe integer
#         bubur = tipe integer
#         caj = tipe integer
#         pilih = tipe integer
#         priceall = tipe integer
#         bayar = tipe integer
#         kembalian = tipe integer
def main ():
#Program include input and process
    temp1 = 0
    temp2 = 0
    temp3 = 0
    total = 0
    ayam = 0
    bubur = 0
    caj = 0
    pilih = 1
    while(pilih != 0):
        print("="*50)
        print("Menu :")
        print("1. Ayam Goreng \t\t Rp. 15000")
        print("2. Bubur Ayam \t\t Rp. 12000")
        print("3. Cah Ayam Jamur \t Rp. 17000")
        print("0. Selesai")
        pilih = int(input("Pilih : "))
        while(pilih > 3 or pilih < 0):
            print("Maaf tidak ada menu",pilih,"silahkan pilih ,menu yang tersedia.")
            pilih = int(input("Pilih : "))
        if(pilih == 1):
            total = int(input("Jumlah Ayam Goreng yang dibeli : "))
            ayam = ayam + 1
            temp1 = temp1 + total
        elif(pilih == 2 or pilih == 3 or pilih == 4):
            ayam = ayam + 0
        if(pilih == 2):
            total = int(input("Jumlah Bubur Ayam yang dibeli : "))
            bubur = bubur + 1
            temp2 = temp2 + total
        elif(pilih == 1 or pilih == 3 or pilih == 4):
            bubur = bubur + 0
        if(pilih == 3):
            total = int(input("Jumlah Cah Ayam Jamur yang dibeli : "))
            caj = caj + 1
            temp3 = temp3 + total
        elif(pilih == 1 or pilih == 2 or pilih == 4):
            caj = caj + 0
#Program include process and output
    print("="*50)
    print(temp1,"Ayam Goreng \t \t Rp. ",temp1*15000)
    print(temp2,"Bubur Ayam \t \t Rp. ",temp2*12000)
    print(temp3,"Cah Ayam Jamur \t Rp. ",temp3*17000)
    priceall = (temp1*15000) + (temp2*12000) + (temp3*17000)
    print("Total \t \t \t Rp. ",priceall)
    print("="*50)
    bayar = int(input("Bayar : \t \t Rp. "))
    kembalian = bayar - priceall
    print("Kembalian \t \t Rp. ",kembalian)
    print("="*50)
if __name__ == '__main__':
    main()

   
