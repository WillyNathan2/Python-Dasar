# File : T11A_2072037.py
# Nama : Willy Natanael Sijabat 2072037
# Deskripsi : Membuat program array dimensi , dengan ketentuan output

# Kamus Lokal
# Fungsi Deklarasimatriks() untuk membuat alokasi memori data
# dari matriks
# arr = type array of int
# dimensi1 , dimensi2 = parameter n
# i = var counter

def Deklarasimatriks(dimensi1,dimensi2):
    A = [None]*dimensi1
    for i in range(0,dimensi1,1):
        A[i] = [None]*dimensi2
    return A

# Kamus lokal
# Fungsi addMatriks() -- > untuk penambahan value matriks yang sudah di input
# matriks type array of int
# x = var int , untuk menambahkan value matriks dan di kondisikan pada
# perulangan
# i = var counter
# j = var counter


def addMatriks(n,matriks,x):
    for i in range (0,n,1):
        for j in range (0,n,1):
            matriks[i][j] += x      
    return matriks


def printMatrix(n,matriks):
    print("Matriks akhir:",end = " ")
    print()
    for i in range (0,n,1):
        for j in range (0,n,1):
            print(matriks[i][j],end=" ")
        print()

#Kamus data
# n = tipe int
# matriks = array
# i dan j = var counter untuk input value ke matriks
def main():
    #input ukuran matriks
    n = int(input("n:"))
    matriks = Deklarasimatriks(n,n) 
    
    # input matriks 
    print ("Isi matriks : ")
    for i in range (0,n,1):
        for j in range (0,n,1):
            matriks[i][j] = int(input())
    
    x = int(input("Penambahan : "))
    print()
    addMatriks(n,matriks,x)
    printMatrix(n,matriks)

if __name__ == '__main__':
    main()
