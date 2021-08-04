# File      : PR04C_2072037.py
# Penulis   : Willy Natanael Sijabat 2072037
# Deskripsi : Membuat program memunculkan tipe-tipe pola bintang yang terbagi atas
#             3 tipe , mencetak urutan tipe berdasar value deret awal sampai deret ke 3
#             dengan parameter ketentuan panjang deret ditentukan oleh inputan batas pola
#             dan jika lebih dari 3 , maka deret akan berulang dari tipe 1 sampai dengan seterusnya
# Kamus Data : p = tipe integer
#              i = integer
#              j = integer
#              x = integer



def main ():
# Program include process and output
    #Input
    p = int(input("Batas Pola: "))
    i = 1

    while(i <= 3):
        print("|",end = "  ")
        j = 1
        x = 1
        while(j <= p):

            if(i == 1 and x == 1):
                print("    *",end = " | ")
            elif(i == 2 and x == 1):
                print("  * *",end = " | ")            
            elif(i == 3 and x == 1):
                print("* * *",end = " | ")

            if(i == 1 and x == 2):
                print("* * *",end = " | ")
            elif(i == 2 and x == 2):
                print("*   *",end = " | ")            
            elif(i == 3 and x == 2):
                print("* * *",end = " | ")

            if(i == 1 and x == 3):
                print("* * *",end = " | ")
            elif(i == 2 and x == 3):
                print("* * ",end = "  | ")            
            elif(i == 3 and x == 3):
                print("*   ",end = "  | ")

            x = x + 1
            if(x > 3):
                x = 1
            j += 1
        i += 1
        print("\n",end="")

if __name__ == '__main__':
    main()
        
