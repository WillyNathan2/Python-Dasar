# File : T11C_2072037
# Penulis : Willy Natanael Sijabat 2072037
# Deskripsi : membuat program dummy , dengan menyimpan data secara 2 dimensi , lalu output
#             dari kode program , nama , harga , dan semua informasinya di tampilkan

# Kamus Lokal :
# fungsi deklarasiMatriks() --> untuk alokasi memory data
# dimensi1 dan dimensi2 --> ukuran matriks
# a = type array of int
def deklarasiMatriks(dimensi1,dimensi2):
    a = [None]*dimensi1
    for i in range(0,dimensi1,1):
        a[i] = [None]*dimensi2
    return a

# Kamus lokal :
# fungsi hasilHariIni untuk menampilkan data yang di input
# tot = var int --> untuk temp total harga
# harga = tipe int (hasil perkalian array)
# i = var counter untuk proses perulangan dan output

def hasilHariIni(a,b,i):
    tot = 0
    for i in range(0,i,1):
        if(a[i][0] != None):
            if(a[i][1] != None):
                harga = b[i][0] * b[i][1]
                print(i+1,". Barang",a[i][0],a[i][1],"terjual",b[i][0],"x",b[i][1],"=",harga)
                tot = tot + harga
    print("Total pendapatan hari ini : ",tot,".")

#Kamus data :
# array1 , array2 = untuk deklarasi matriks
# dummy = tipe str -- > untuk batas
# i = var counter (increment pada while)

def main():
    array1 = deklarasiMatriks(99999,2)
    array2 = deklarasiMatriks(99999,2)
    print("="*45)
    dummy = " "
    i = 0

    while(dummy != "000"):
        dummy = str(input("Kode Barang : "))
        array1[i][0] = dummy
        if (dummy!= "000"):
            array1[i][1] = str(input("Nama Barang : "))
            array2[i][0] = int(input("Jumlah Terjual : "))
            array2[i][1] = int(input("Harga Jual : "))
        i = i + 1
        print("="*45)

    hasilHariIni(array1,array2,i)   
if __name__ == '__main__':
    main()
