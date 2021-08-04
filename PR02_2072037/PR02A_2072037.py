# File: PR02A_2072037.py
# Penulis : Willy Natanael Sijabat 2072037
# Deskripsi : Membuat kalkulator sederhana dengan inputan value var integer serta
#             input ekspresi / operasinya
# Kamus     : VarX : TIPE INTEGER
#             VarY : TIPE INTEGER
#             KALI : TIPE INTEGER
#             MODULO : TIPE INTEGER
#             KUADRAD : TIPW INTEGER
#             Operator : TIPE STRING

def main ():
    #program include input , process and output
    VarX = int(input("x: "))
    VarY = int(input("y: "))
    Operator = str(input("ekspresi: "))

    TAMBAH = VarX + VarY
    KURANG = VarX - VarY
    KALI = VarX * VarY
    MODULO = VarX % VarY
    KUADRAD = VarX ** VarY
    if(Operator == "+"):
        print(VarX,Operator,VarY,"=",TAMBAH)
    elif(Operator == "-"):
        print(VarX,Operator,VarY,"=",KURANG)
    elif(Operator == "x" or Operator == "*"):
        print(VarX,Operator,VarY,"=",KALI)
    elif(Operator == "/" or Operator == ":"):
        if(VarX % VarY == 0):
            print(VarX,Operator,VarY,"=",int(VarX / VarY))
        else:
            print(VarX,Operator,VarY,"=",float(VarX / VarY))
    elif(Operator == "%"):
        print(VarX,Operator,VarY,"=",MODULO)
    elif(Operator == "^"):
        print(VarX,Operator,VarY,"=",KUADRAD)
if __name__ == '__main__':
    main()
