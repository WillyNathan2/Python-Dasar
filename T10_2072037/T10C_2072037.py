# File : T10C_2072037.py
# Nama : Willy Natanael Sijbat 2072037
# Deskripsi : membuat program angka unik dan munculnya berapa kali

def cekBilangan(n):
    a = [None] * n
    for i in range (0,n,1):
        a[i] = int(input())

    for i in range (0,n,1):
        print(a[i],end=" ")
    print()
    return

def cekMuncul(n):
    a = [None] * n
    j = 0
    print("Angka unik : ", end = " ")
    for i in range (0,n,1):
        if(a[i] != None):
            print(a[i], end = " ")
    print()
    return

def main():
    n = int(input("N : "))
    cekBilangan(n)
    cekMuncul(n)
if __name__ == '__main__':
    main()
