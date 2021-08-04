# File : PR10B_2072037
# Penulis : Willy Natanael Sijabat 2072037
# Deskripsi : Membuat program array dengan menentukan huruf apa yg dicari
#             lalu nama yg sudah di input ke dalam array
#             akan muncul jika huruf nya mengandung huruf yg sama dengan array

# kamus lokal
# confirm = tipe bolean --- > validasi
# word = var counter
# arr = array of string -- > nama 
def tampilNama(huruf,arr):
    confirm = False
    print("Daftar Nama yang dicari mengandung huruf",huruf,":")
    for word in arr:
        if (huruf in word):
            print(word,end = " ")
            confirm = True

    if(confirm == False):
        print("No Data")

# Kamus data
# N = tipe int -- > untuk alokasi data
# arr = type array of str
# i = tipe int
# huruf = tipe str -- > untuk mencari huruf
def main ():
    N = int(input("Jumlah Orang :"))
    arr = [None]*N

    for i in range(0,N,1):
        arr[i] = str(input())

    huruf = str(input("Huruf yang di cari : "))
    
    tampilNama(huruf,arr)

if __name__=='__main__':
    main()
