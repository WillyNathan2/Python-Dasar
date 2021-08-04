# File : T10A_2072037.py
# Nama : Willy Natanael Sijabat 2072037
# Deskripsi : membuat asc list array berdasarkan urutan inputnya


# bil = alokasi array memori
def array(n):
    bil = n * [None]

    for i in range (0,n,1):
        bil[i] = int(input())
    print(bil[::-1])
    
def main ():
    n = int(input(""))
    array(n)
if __name__ =='__main__':
    main()
