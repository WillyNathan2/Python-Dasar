# File : T08A_2072037.py
# Nama : Willy Natanael Sijabat
# Deskripsi : Membuat program konversi volume,luas,keliling berdasarkan parameter
#             panjang,lebar dan tinggi dengan membuat fungsi terpisah sesuai dengan apa
#             yang diminta


# Nama Fungsi : volume
# Tujuan Fungsi : untuk mencari volume
# kamus data : panjang (parameter)
#              lebar (parameter)
#              tinggi (parameter)
#              vl = tipe integer

def volume (panjang,lebar,tinggi):
    vl = panjang*lebar*tinggi
    print("Volume kubus berukuran",panjang,"x",lebar,"x",tinggi,"adalah ",vl,"cm^3")
    

# Nama Fungsi : luas
# Tujuan Fungsi : untuk mencari luas
# kamus data : panjang (parameter)
#              lebar (parameter)
#              tinggi (parameter)
#              lu = tipe integer
def luas (panjang,lebar,tinggi):
    lu = 2*((panjang*lebar)+(panjang*tinggi)+ (lebar*tinggi))
    print("Volume kubus berukuran",panjang,"x",lebar,"x",tinggi,"adalah ",lu,"cm^2")
    return lu

# Nama Fungsi : keliling
# Tujuan Fungsi : untuk mencari keliling
# kamus data : panjang (parameter)
#              lebar (parameter)
#              tinggi (parameter)
#              kel = tipe integer
def keliling (panjang,lebar,tinggi):
    kel = 4*(panjang+lebar+tinggi)
    print("Volume kubus berukuran",panjang,"x",lebar,"x",tinggi,"adalah ",kel,"cm")
    return kel

# Input
def main ():
    panjang = int(input("panjang (cm) : "))
    lebar = int(input("lebar (cm) : "))
    tinggi = int(input("tinggi (cm) : "))
    confirm = str(input("Nilai yang dicari (v volume, l luas, k keliling) : "))
# Process(in funtion) with output
    if(confirm == "v"):
        volume(panjang,lebar,tinggi)
    elif(confirm == "l"):
        luas(panjang,lebar,tinggi)
    elif(confirm == "k"):
        keliling(panjang,lebar,tinggi)
        
if __name__=='__main__':
    main()
