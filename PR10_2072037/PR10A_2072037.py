# File : PR10A_2072037.py
# Penulis : Willy Natanael Sijabat 2072037
# Deskripsi program : membuat program array , dengan ketentuan output
#                     yang harus menampilkan baris deret yang di mulai dari
#                     indeks ke 0 dan indeks genap , dan array ditaruh dalam
#                     bentuk fungsi getEven(arr)

#Kamus Lokal :
# i = var counter -- > untuk pengulangan dalam proses memasukan data
# arr = array type of int
def getEven(arr):
    for i in range (0,len(arr),1):
        if (i % 2 == 0):
            print(arr[i],end = " ")
    return

# Kamus data :
# N = tipe int --- > untuk alokasi data (memory data)
# temp = tipe int --- > untuk input data dan nanti diproses menggunakan pengkondisian
#                       untuk memasukan data temp yang indeks nya genap
# i = var counter -- > proses 
def main ():
    N = int(input(" "))
    arr = N * [None] #Type array of integer
    
    for i in range (0,N,1):
        temp = int(input())
        if (i % 2 == 0):
            arr[i] = temp
    getEven(arr)

if __name__=='__main__':
    main()
    
