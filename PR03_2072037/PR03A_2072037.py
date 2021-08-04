# File : PR03A_2072037.py
# Nama : Willy Natanael Sijabat 2072037
# Deskripsi : Menentukan Bilangan deret dengan kelipatan nya serta jumlah total dari bilangan deret
# Kamus : en = tipe integer
#         em = tipe integer
#         ex = tipe integer
#         i  = tipe integer
#         temp1 = tipe integer
#         total = tipe integer


def main ():
#Program
        #input
        en = int(input("n: "))
        em = int(input("m: "))
        ex = int(input("x: "))
        print("Deret",em,"dimulai dari",en,"dengan kelipatan",ex,".")

        #Proces include output
        i = 1
        temp1 = en
        total = 0
        while(i <= em):
                total = total + temp1
                if(i > 1):
                        print(",",end=" ")
                        
                print(temp1, end =" ")
                temp1 = temp1 + ex
                i += 1
        print("")
        #output total
        print("Total seluruh deret adalah",total)
if __name__ == '__main__':
    main()


        
        
        
