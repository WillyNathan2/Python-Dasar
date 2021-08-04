# File : PR12C_2072037.py
# Nama : Willy Natanael Sijabat 2072037
# Deskripsi : membuat program sorted melalui 2 jenis array dengan pengkondisian tertentu

# Kamus Lokal
# x = var counter
# imin = tipe int
# arr = array of int
# i = var counter
def Sorted(arr, n):
    for x in range(0,n-1,1):
        imin = x
        for i in range(x+1, n, 1):
            if arr[i][0] < arr[imin][0]:
                imin = i
        arr[x], arr[imin] = arr[imin], arr[x]

# kamus data :
# n = tipe int
# arr = arr of int and str
# i = var counter
# rslt = penampung -- > tipe int and str
def main():
    # Input
    n = int(input("Jenis Buah : "))
    arr =  n * [None] 
    for i in range(0,n,1):
        arr[i] = [None] * n
    
    print("=" * 25)
    for i in range(0,n,1):
        arr[i][0] = str(input("Buah : "))
        arr[i][1] = int(input("Jumlah : "))
        print("=" * 25)
    #Process
    Sorted(arr, n)
    for i in range(0,n,1):
        print(arr[i][0], "\t", arr[i][1], "kg")

    rslt = 0
    for i in range(1,n,1):
        if (arr[i][1] > arr[rslt][1]):
            rslt = i
    # Output
    print("Jumlah buah terbanyak adalah", arr[rslt][0], "seberat", arr[rslt][1], "kg")
    for i in range(1,n,1):
        if (arr[i][1] < arr[rslt][1]):
            rslt = i
    print("Jumlah buah tersedikit adalah", arr[rslt][0], "seberat", arr[rslt][1], "kg")

if __name__ == '__main__':
    main()
