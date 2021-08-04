# File : T04_C_2072037.py
# Nama : Willy Natanael Sijabat
# Deskripsi : menentukan apakah bilangan input adalah prima atau bukan
# Kamus : number = tipe integer
#         tes = tipe integer
#         i   = tipe integer

def main ():
#Program
    number = int(input("n : "))
    tes = 0
    if (number > 1):
        for i in range(2,number,1):
            if (number % i == 0):
                tes = 1
                break
    if tes:
        print(number, "bukan bilangan prima")
    else:
        print(number, "adalah bilangan prima")
if __name__ == '__main__':
    main()   
