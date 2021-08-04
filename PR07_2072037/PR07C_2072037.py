# file : PR07C_2072037.py
# nama : willy natanael sijabat 2072037
# deskripsi : membuat program pattern arrow menggunakan 3 fungsi, untuk setiap
#             bagian arrow (atas,tengah,bawah) dengan pengkondisian arah arrow
# kamus lokal (parameter): n,confirm
# kamus data : k = tipe integer
#              i = tipe integer
#              j = tipe integer
#              a = tipe integer
#              b = tipe integer
#              x = tipe integer
#              y = tipe integer


# Program include process 
def segitigaup(n,confirm):
    if(confirm == 1):
        k = n - 1
        for i in range(0,n,1):#atas kiri
            print(" ",end = " ")
            for j in range(0,k,1):
                print(" ",end=" ")
            k = k - 1
            for j in range(0, i+1,1):
                print("*", end=" ")
            print()
    elif(confirm == 2):
        for i in range (1,n+1,1):#atas kanan
            print("  " * ((n * 2) - 1 ), end= "")
            for j in range (1,i+1,1):
                print("*", end=" ")
            print()
def segitigamid(n,confirm):
    if(confirm == 1):
        for a in range (1,n+1,1):#tengah kiri
            for b in range (1,((n+1)*3)-2,1):
                print("*", end = " ")
            print()
    elif(confirm == 2):
        for a in range (1,n+1,1):#tengah kanan
            for b in range (1,((n+1)*3)-2,1):
                print("*",end = " ")
            print()

def segitigadown(n,confirm):
    if(confirm == 1):
        for i in range (1,n+1,1):#bawah kiri
            print("  "*i,end = "")
            for j in range (n,i-1,-1):
                print("*",end = " ")
            print()
    elif(confirm == 2):
        for x in range (1,n + 1,1):#bawah kanan
            print("  "  * ((n * 2) - 1), end = "")
            for y in range (n,x - 1,-1):
                print("*", end = " ")
            print()

def main ():
    #Input
    n = int(input("ukuran panah : "))
    confirm = int(input("Arah (1 Kiri / 2 Kanan) : "))
    #Output
    segitigaup(n,confirm)
    segitigamid(n,confirm)
    segitigadown(n,confirm)
if __name__=='__main__':
    main()
    

    
