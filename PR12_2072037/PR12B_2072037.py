# File : PR12B_2072037.py
# Nama : Willy Natanael Sijabat 2072037
# Deskripsi : membuat program dengan 2 pilihan program,
#             sorted dari terendah hingga value tertinggi , begitupun sebaliknya


# Kamus Lokal
# Arr : arry of  int
# Amin : var int (akan dijadikan acuan pengulangan dari var counter i)
# temp : penampung
# i : var counter
# j : var counter
def SortAtas(Arr,n):
    for i in range(0,n-1,1):
        Amin = i
        for j in range(i+1,n,1):
            if(Arr[j] < Arr[Amin]):
                Amin = j
        temp = Arr[i]
        Arr[i] = Arr[Amin]
        Arr[Amin] = temp


# Kamus Lokal
# Arr : arry of  int
# Amax : var int (akan dijadikan acuan pengulangan dari var counter i)
# temp : penampung
# i : var counter
# j : var counter        
def SortBawah(Arr,n):
    for i in range(0,n,1):
        Amax = i
        for j in range(i+1,n,1):
            if(Arr[j] > Arr[Amax]):
                Amax = j
        temp = Arr[i]
        Arr[i] = Arr[Amax]
        Arr[Amax] = temp

# Kamus Data
# n = tipe int
# Arr = array of int
# cari = tipe str
def main():
    # Input
    n = int(input("N : "))
    Arr = [None]*n
    print("Data:")
    for i in range (0,n,1):
        Arr[i] = int(input())

        
    # Pengkondisian
    cari = str(input("Jenis Sorting (up: menaik, down: menurun): "))
    if(cari == "up"):
        SortAtas(Arr,n)
    elif(cari == "down"):
        SortBawah(Arr,n)
        
    # Output 
    for i in range (0,n,1):
        print(Arr[i],end=" ")
    
if __name__ == '__main__':
    main()

    
    
    
    

    
