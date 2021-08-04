# File : T09C_2072037.py
# Nama : Willy Natanael Sijabat 2072037
# Deskripsi : Membuat program himpunan
# Kamus : N = Tipe Integer
#         M = Tipe Integer
def main ():
    #process include input process and output
    N = int(input("n : ")) 
    n = [None]*N # Type Array of int
    for i in range (0,N,1):
        n[i] = int(input())

    M = int(input("m : "))
    m = [None]*M  # Type Array of int
    for i in range (0,M,1):
        m[i] = int(input())

    A = M + N
    a = [None]*A
    for i in range (0,A,1):
        m[i] = a[i]
    for i in range (0,A,1):
        n[i] = a[i]
    for i in range (0,A,1):
        print(a[i])
        
if __name__ =='__main__':
    main()
