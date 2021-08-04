# File : T06B_2072037.py
# Nama : Willy Natanael Sijabat 2072037
# Deskripsi : Membuat Program pengkondisian untuk membeli menu minuman
#             yang sesuai dengan soal yang ditentutkan
# Kamus : pilih = Tipe Integer
#         kopi = Tipe Integer & Tipe String
#         nonkops = Tipe Integer & Tipe String
#         suhu = Tipe Integer & Tipe String

def main ():
    # Program include input process and output
    print("Menu : ")
    print("1. Kopi \n2. Non-Kopi ")
    pilih = int(input("Pilih : "))
    print("="*50)
    if(pilih == 1):
        print("Rasa")
        print("1. Americano \n2. Latte \n3. Cappucino")
        kopi = int(input("Pilih : "))
        if(kopi == 1):
            kopi = "Americano"
            print("1. Panas \n2. Dingin")
            suhu = int(input("Pilih : "))
            if(suhu == 1):
                suhu = "Panas"
                print("Pesanan : ")
                print("1.",kopi,suhu,"Rp. 12000")
            elif(suhu == 2):
                suhu = "Dingin"
                print("Pesanan : ")
                print("1.",kopi,suhu,"Rp. 13000")
            
        elif(kopi == 2):
            kopi = "Latte"
            print("1. Panas \n2. Dingin")
            suhu = int(input("Pilih : "))
            if(suhu == 1):
                suhu = "Panas"
                print("Pesanan : ")
                print("1.",kopi,suhu,"Rp. 12000")
            elif(suhu == 2):
                suhu = "Dingin"
                print("Pesanan : ")
                print("1.",kopi,suhu,"Rp. 13000")

        elif(kopi == 3):
            kopi = "Cappucino"
            print("1. Panas \n2. Dingin")
            suhu = int(input("Pilih : "))
            if(suhu == 1):
                suhu = "Panas"
                print("Pesanan : ")
                print("1.",kopi,suhu,"Rp. 12000")
            elif(suhu == 2):
                suhu = "Dingin"
                print("Pesanan : ")
                print("1.",kopi,suhu,"Rp. 13000")
    elif(pilih == 2):
        print("Rasa")
        print("1. Susu \n2. Teh \n3. Air Mineral")
        nonkops = int(input("Pilih : "))
        if(nonkops == 1):
            nonkops = "Susu"
            print("1. Panas \n2. Dingin")
            suhu = int(input("Pilih : "))
            if(suhu == 1):
                suhu = "Panas"
                print("Pesanan : ")
                print("1.",nonkops,suhu,"Rp. 12000")
            elif(suhu == 2):
                suhu = "Dingin"
                print("Pesanan : ")
                print("1.",nonkops,suhu,"Rp. 13000")
        elif(nonkops == 2):
            nonkops = "Teh"
            print("1. Panas \n2. Dingin")
            suhu = int(input("Pilih : "))
            if(suhu == 1):
                suhu = "Panas"
                print("Pesanan : ")
                print("1.",nonkops,suhu,"Rp. 12000")
            elif(suhu == 2):
                suhu = "Dingin"
                print("Pesanan : ")
                print("1.",nonkops,suhu,"Rp. 13000")
        elif(nonkops == 3):
            nonkops = "Air Mineral"
            print("1.",nonkops,"Rp. 6000")
if __name__ == '__main__':
    main()
