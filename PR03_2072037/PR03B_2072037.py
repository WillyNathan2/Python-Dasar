#File : PR03B_2072037.py
#Nama : Willy Natanael Sijabat 2072037
#Deskripsi : Membuat deret fibonachi dengan sistem perulangan while , 
#Kamus : n = tipe int
#        a = tipe int
#        b = tipe int
#        jumlah = tipe int
#        i = tipe int


def main ():
#Program
    
    n = int(input("n: "))
    a = 0
    b = 1
    jumlah = 0
    i = 0

    while(i < n):
      print(jumlah, end = " ")
      i += 1
      a = b
      b = jumlah
      jumlah = a + b


if __name__ == '__main__':
    main()
