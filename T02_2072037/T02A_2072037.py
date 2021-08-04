# File    : T02A_2072037
# Penulis : Willy Natanael Sijabat
# Deskripsi : Mencari karakter dalam string yang sudah diberi value integer
# Kamus : NamaDepan = string
#       : NamaBelakang = string
#       : Words = integer
#       : FineWords = code (string)  

def main ():
#program
    NamaDepan = str(input("Nama Depan :"))
    Namabelakang = str(input("Nama Belakang :"))
    Words = int(input("Kode huruf yang ingin dicari :"))
    NamaLengkap = NamaDepan+" "+Namabelakang
    if(Words == 1):
        Code = "a"
    elif(Words == 2):
        Code = "b"
    elif(Words == 3):
        Code = "c"
    elif(Words == 4):
        Code = "d"
    elif(Words == 5):
        Code = "e"
    elif(Words == 6):
        Code = "f"
    elif(Words == 7):
        Code = "g"
    elif(Words == 8):
        Code = "h"
    elif(Words == 9):
        Code = "i"
    elif(Words == 10):
        Code = "j"
    elif(Words == 11):
        Code = "k"
    elif(Words == 12):
        Code = "l"
    elif(Words == 13):
        Code = "m"
    elif(Words == 14):
        Code = "n"
    elif(Words == 15):
        Code = "o"
    elif(Words == 16):
        Code = "p"
    elif(Words == 17):
        Code = "q"
    elif(Words == 18):
        Code = "r"
    elif(Words == 19 ):
        Code = "s"
    elif(Words == 20 ):
        Code = "t"
    elif(Words == 21 ):
        Code = "u"
    elif(Words == 22 ):
        Code = "v"
    elif(Words == 23 ):
        Code = "w"
    elif(Words == 24 ):
        Code = "x"
    elif(Words == 25 ):
        Code = "y"
    elif(Words == 26 ):
        Code = "z"
    FindWords = Code in NamaLengkap
         
         
    print("Nama Lengkap :",NamaLengkap)
    if (FindWords == True):
        print(Code,"ditemukan dalam nama", NamaLengkap)
    else:
        print(Code,"tidak ditemukan dalam",NamaLengkap)
if __name__ == '__main__':
    main()


     
