# File : PR07A_2072037.py
# Nama : Willy Natanael Sijabat 2072037
# Deskripsi : Membuat program perulangan sistem faktorial dengan menggunakan  fungsi
# kamus lokal (parameter fungsi): faktorial,n
# kamus data :
# x = tipe integer
# vact = tipe integer
# i = tipe integer

#Program include procees
def factor(faktorial,n):
    for i in range(1,n + 1,1):
        faktorial = faktorial * i
        if(faktorial > 99):
            print("|",i,"!","|        ",faktorial,"     |")
        elif(faktorial > 9 ):
            print("|",i,"!","|        ",faktorial,"      |")
        elif(faktorial < 10):
            print("|",i,"!","|        ",faktorial,"       |")
def main():
    #input
    x = int(input('n: '))
    vact = 1
    print("|","n  ","|"," nilai faktorial |")
    #output
    factor(vact,x)
if __name__ == '__main__':
    main()
