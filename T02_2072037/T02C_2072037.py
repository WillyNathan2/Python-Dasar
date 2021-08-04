# File    : T02C_2072037
# Penulis : Willy Natanael Sijabat
# Deskripsi : program menentukan gaji berdasarkan absen
# kamus : NIK,Name,IZIN,,Kategori = tipe string
# kamus : ON,OFF = integer
# keterangan : program tidak sempurna dikarenakan saya tidak sempat mengerjakan
def main ():
#Program
    print("==========================================")
    NIK = str(input("NIK \t\t\t : "))
    Name = str(input("Nama \t\t\t : "))
    ON = int(input("Masuk \t\t\t :"))
    IZIN = int(input("Izin \t\t\t :"))
    OFF = int(input("Alpha \t\t\t :"))
    Kategori = str(input("Kategori (I,II,III) \t"))
    print("==========================================")
    
if __name__ == '__main__':
    main()
