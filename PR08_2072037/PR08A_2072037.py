# File : PR08A_2072037
# Nama : Willy Natanael Sijabat 2072037
# Deskripsi Program : Membuat program input bilangan , serta pengkondisian mau diapakan angka yang
#                     sudah dinput (dicari rata-ratanya/maks nya/min nya) dengan menggunakan fungsi
#                     untuk outputnya
# parameter (kamus lokal): a,b,c,d


# Fungsi mencari nilai maksimal dari keempat bilangan yang di input
# kamus data : konklusi1 = tipe integer (untuk mencari nilai maks dari 2 var)
#              konklusi2 = tipe integer (untuk mencari nilai maks dari 2 var)
#              konklusi  = tipe integer (untuk mencari nilai maks dari 2 var)
def maks(a,b,c,d):
    konklusi1 = max(a,b)
    konklusi2 = max(c,d)
    konklusi = max(konklusi1,konklusi2)
    print("bilangan terbesar adalah",konklusi)



# Fungsi mencari nilai minimal dari keempat bilangan yang di input
# kamus data : konklusi1 = tipe integer (untuk mencari nilai man dari 2 var)
#              konklusi2 = tipe integer (untuk mencari nilai min dari 2 var)
#              konklusi  = tipe integer (untuk mencari nilai min dari 2 var)

def minim(a,b,c,d):
    konklusi1 = min(a,b)
    konklusi2 = min(c,d)
    konklusi = min(konklusi1,konklusi2)
    print("bilangan terkecil adalah",konklusi)

# Fungsi mencari nilai rata-rata dari keempat bilangan yang di input
# kamus data :  konklusi = tipe integer (untuk memproses perhitungan mencari rata-rata)

def avg(a,b,c,d):
    konklusi = (a + b + c + d) / 4
    print("Rata-rata bilangan yang di input adalah",konklusi)


# input serta pengkondisian
def main():
    a = int(input("bilangan 1: "))
    b = int(input("bilangan 2: "))
    c = int(input("bilangan 3: "))
    d = int(input("bilangan 4: "))

    confirm = str(input("Pilih perhitungan (k terkecil, b terbesar, r rata-rata): "))
    if(confirm == "k"):
        minim(a,b,c,d)
    elif(confirm == "b"):
        maks(a,b,c,d)
    elif(confirm == "r"):
        avg(a,b,c,d)
        

if __name__=='__main__':
    main()
