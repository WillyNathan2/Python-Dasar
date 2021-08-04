# File    : T03C_2072037.py
# Penulis : Willy Natanael Sijabat 2072037
# Deskripsi : membuat program bon dengan looping while
# Kamus :     snack = 0
    #result1 = int
    #biskuit = int
    #result2 = int
    #yogurt = int
    #susu = int
    #result3 = int
    #result4 = int
    #TOTALKESELURUHAN = int
    #INPUTDOET
    #KEMBALIAN
    #total = int
    #i = int

def main ():
#Program

    snack = 0
    result1 = 0
    biskuit = 0
    result2 = 0
    yogurt = 0
    susu = 0
    result3 = 0
    result4 = 0
    i = 1
    print("Selamat Jajan !")
    while(i != 0):
        
        print("==========================")
        print("Pilihan menu :")
        print("1. Snack ringan")
        print("2. Biskuit gandum")
        print("3. Yogurt mix berry")
        print("4. Susu Cokelat")
        print("0. Selesai")

        i = int(input("Menu :"))
        if( i == 1):
            total = int(input("Jumlah :"))
            snack = snack + 1
            result1 = result1 + total
        elif( i == 2 or i == 3 or i == 4):
            snack = snack + 0
        if( i == 2):
            total = int(input("Jumlah :"))
            biskuit = biskuit + 1
            result2 = result2 + total
        elif( i == 1 or i == 3 or i == 4):
            biskuit = biskuit + 0
        if( i == 3):
            total = int(input("Jumlah :"))
            yogurt = yogurt + 1
            result3 = result3 + total
        elif( i == 2 or i == 1 or i == 4):
            biskuit = biskuit + 0
        if( i == 4):
            total = int(input("Jumlah :"))
            susu = susu + 1
            result4 = result4 + total
        elif(i == 1 , i == 2 , i == 3 ):
            susu = susu + 0


        if(i == 0):
            if (i == 0  ):
                print("Selesai Jajan")
                print("==========================")
            if(result1 > 0):
                print(result1,"Snack Ringan Rp.",(result1*4000))
            if(result2 > 0):
                print(result2,"Biskuit gandum Rp.",(result2*7000))
            if(result3 > 0):
                print(result3,"Yoghurt Mix Berry Rp.",result3*9000)
            if(result4 > 0):
                print(result4,"Susu Cokelat Rp.",result4*6000)
            print("==========================")
            TOTALKESELURUHAN = (result1*4000) + (result2*7000) + (result3*9000) + (result4*6000)

            if(result1 > 0 or result2 > 0 or result3 > 0 or result4 > 0):
                print("Total Bayar Rp.",TOTALKESELURUHAN)
                INPUTDOET = int(input("Uang yang dibayarkan Rp."))

                KEMBALIAN = INPUTDOET - TOTALKESELURUHAN
                print("Kembalian Rp",KEMBALIAN)

     
    if(result1 > 0 or result2 > 0 or result3 > 0 or result4 > 0 ):
        print("Terimakasih dan sampai jumpa lagi")
    else :
        print("Tidak ada yang dibeli nih!")
        print("==========================")
        print("Terimakasih , sampai jumpa lagi !")
        
if __name__ == '__main__':
    main()
