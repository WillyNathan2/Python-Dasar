# File : T11B_2072037.py
# Nama : Willy Natanael Sijabat 2072037
# Deskripsi Program : membuat program array 2 dimensi dengan ketentuan program
#                     untuk mencari nama / lantai/kamar penghuni serta
#                     menentukan output kondisi gedung dengan deskripsi lantai

# kamus data :
# n = tipe int
# m = tipe int
# a = type array of str
# i = var counter
# j = var counter
# hayo = tipe str (berfungsi untuk mengkonfirmasi mau mencari kondisi apa)
# lantai = tipe int
# kamar = tipe int
def main():
    n = int(input("n: "))
    m = int(input("m: "))
    print("Daftar nama penyewa:")

    a = [None]*n
    for i in range(0,n,1):
        a[i] = [None]*m

    for i in range(0,n,1):
        print("Lantai",i,":")
        for j in range(0,m,1):
            print("kamar",j,":",end=" ")
            a[i][j] = str(input())

    print("Kondisi gedung kos saat ini:")
    for i in range(0,n,1):
        print("Lantai",i,":",end=" ")
        for j in range(0,m,1):
            print(a[i][j],end=" ")
        print()

    hayo = str(input("Cari berdasarkan (n nama/k kamar): "))
    if(hayo == "n"):
        nama = str(input("Nama yang dicari: "))
        for i in range(0,n,1):
            for j in range(0,n,1):
                if (a[i][j]== nama) :
                    print(nama,"ada di lantai",i,"kamar",j,".")

    elif(hayo == "k"):
        lantai = int(input("Lantai yang dicari: "))
        kamar = int(input("Kamar yang dicari: "))
        print("Lantai",lantai,"kamar",kamar,"disewa oleh",end=" ")
        print(a[lantai][kamar])
        
        
if __name__ == '__main__':
    main()

