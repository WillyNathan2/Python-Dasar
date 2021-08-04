# File : PR11C_2072037.py
# Penulis : Willy Natanael Sijabat 2072037
# Deskripsi Program : Membuat program perhitungan nilai rata-rata uts,uas,kat serta
#                     menyimpan data , dan menampilkan output yg diminta pada soal

# Kamus Lokal :
# dataRataRata() berfungsi untuk menampilkan nilai rata2 dengan informasi lengkap
# dengan memanfaatkan parameter indeks sebagai patokan
# baris = tipe int
# highrata = tipe int
# kelas = tipe int
# total = tipe int
# i = var counter
# j = var counter
# rata = tipe int -- > penampung nilai rata-rata (untuk perhitungan nilai rata-rata)
def dataRataRata(matriksSiswa,matriksNilai):
    print("Data rata-rata:")
    baris = 0
    highrata = 0
    for i in range(len(matriksSiswa)):
        kelas = 0
        total = 0
        print("Kelas",end=" ")
        print(matriksSiswa[i][kelas],end=" ")
        kelas = kelas + 1
        print("dengan nama",end=" ")
        print(matriksSiswa[i][kelas],end=" ")
        print("rata-ratanya",end=" ")
        for j in range(0,3,1):
            total = total + matriksNilai[i][j]
        rata = total / 3
        if(rata > highrata):
            highrata = rata
            nama = i
        print(round(rata,2),end=" ")
        print()
    print("Rata-rata tertinggi",round(highrata,2),"diperoleh",matriksSiswa[nama][1],"dari kelas",matriksSiswa[nama][0],".")

# Kamus Lokal
# inputALL() -- > berfungsi untuk meminta data kelas,nama , uts,uas,kat
# Siswa -- > array of str
# Nilai -- > array of int
# i = var counter
# j = var counter
def inputALL (n,Siswa,Nilai):
    for i in range(0,n,1):
        print("="*25)
        for j in range(0,2,1):
            if(j == 0):
                Siswa[i][j] = str(input("Kelas: "))
            elif(j == 1):
                Siswa[i][j] = str(input("Nama: "))
        #input nilai
        for j in range(0,3,1):
            if(j == 0):
                Nilai[i][j] = int(input("Nilai UTS: "))
            elif(j == 1):
                Nilai[i][j] = int(input("Nilai UAS: "))
            elif(j == 2):
                Nilai[i][j] = int(input("Nilai KAT: "))
    return Nilai,Siswa

# Kamus Lokal :
# insertSiswa() ----> untuk melakukan deklarasi array
# Siswa = array of str
# i = var counter
# j = var counter

def insertSiswa(n):
    Siswa = [None]*n
    for i in range(0,n,1):
        for j in range(0,n,1):
            Siswa[i] = [None]*2
    return Siswa
# Kamus Lokal :
# insertNilai() berfungsi untuk deklarasi array nilai
# Nilai = array of int
# i = tipe int
# j = tipe int

def insertNilai(n):
    Nilai = [None]*n
    for i in range(0,n,1):
        for j in range(0,n,1):
            Nilai[i] = [None]*3
    return Nilai

# Kamus data
# n = tipe int (jumlah siswa)-- alokasi data memory
# Siswa = array of str
# Nilai = array of int
def main() :
    n = int(input("Jumlah siswa: "))
    Siswa = insertSiswa(n)
    Nilai = insertNilai(n)
    inputALL(n,Siswa,Nilai)  
    print("="*30)
    dataRataRata(Siswa,Nilai)
if __name__ == '__main__':
    main()
