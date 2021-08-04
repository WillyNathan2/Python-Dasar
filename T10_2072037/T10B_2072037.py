# File : T10B_2072037.py
# Deskripsi : Membuat program mencari nilai terkecil serta di indeks ke berapanya


# Funtion inputOdd
# untuk memasukan number dengan pengkondsian selain 999 maka akan
# mengstop perulangan while
# n = tipe integer
# j = tipe integer

def inputOdd(arr):
    n = int(input())
    j = 0
    while (n != 999):
        if (n % 2 == 1):
            arr[j] = n
            j += 1
        n = int(input())
    return arr,j

# untuk mencari value terkecil dari array
# terkecil = array 
def findingMini(arr,j):
    indeks = 0
    terkecil = arr[indeks]
    for i in range (0,j,1):
        if (terkecil > arr[i]):
            terkecil = arr[i]
            indeks = i
    return terkecil, indeks

#nmax = tipe integer (alokasi memori)
# Program Utama
def main():
    nmax =  100
    A = [None]*nmax 
    arr,j = inputOdd(A)
    terkecil, indeks = findingMini(arr,j)
    print("Isi Array:",end=" ")
    for i in range (0,j,1):
        print(arr[i],end=" ")
    print()
    print("Bilangan terkecil adalah",terkecil,"pada indeks",indeks,".")

if __name__ == '__main__':
    main()
