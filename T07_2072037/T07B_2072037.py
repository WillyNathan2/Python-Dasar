#File = T07B_2072037.py
#Nama = Willy Natanael Sijabat
#Deskripsi = Membuat baris deret menggunakan perulangan dengan
#parameter bentuk baris deret yang ditentukan oleh ganjil genap dari input n
def normal (n,m):
    b = n
    for i in range (1,m + 1, 1):
        print (b,end = " ")
        b = b + n
    return

def mundur(n,m):
    b = n
    c = m*n
    for i in range (1,m + 1, 1):
        print(c, end = " ")
        c = c - b
    return

def main ():
    n = int(input("n : "))
    m = int(input("m : "))
    if (n % 2 == 0):
        normal(n,m)
    else:
        mundur(n,m)

if __name__=='__main__':
    main()

