# File    : T02B_2072037
# Penulis : Willy Natanael Sijabat
# Deskripsi : Convert Dus yang dipakai sesuai dengan value muatan dus dan menghitung total dus
# Kamus : BoxA,BoxB,BoxC,BoxD,BoxE,BoxF,IBarang,JUMLAHTotal tipe integer
def main ():
# Program
    IBarang = int(input("Jumlah barang yang dibeli ="))
    print("Dus yang akan Gavin Kirim :")
    print("============")
    BoxA = IBarang // 100
    BoxB = IBarang % 100 // 50
    BoxC = IBarang % 100 % 50 // 20
    BoxD = IBarang % 100 % 50 % 20 // 10
    BoxE = IBarang % 100 % 50 % 20 % 10 // 3
    BoxF = IBarang % 100 % 50 % 20 % 10 % 3 // 1

    if(BoxA > 0):
        print("|",BoxA,"Dus A |")
        print("============")
    if(BoxB > 0):
        print("|",BoxB,"Dus B |")
        print("============")
    if(BoxC > 0):
        print("|",BoxC,"Dus C |")
        print("============")
    if(BoxD > 0):
        print("|",BoxD,"Dus D |")
        print("============")
    if(BoxE > 0):
        print("|",BoxE,"Dus E |")
        print("============")
    if(BoxF > 0):
        print("|",BoxF,"Dus F |")
        print("============")

    JUMLAHTotal = BoxA+BoxB+BoxC+BoxD+BoxE+BoxF
    print("Total ada",JUMLAHTotal,"yang harus Gavin kirim.")
if __name__ == '__main__':
    main()

    

