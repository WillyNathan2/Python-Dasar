# File : T06C_2072037.py
# Nama : Willy Natanael Sijabat 2072037
# Deskripsi : Membuat program sesuai dengan permintaan di soal , dengan
#             program dummy dan perhitungan modal , untung , dsb (buah-buahan)
# Kamus : kgapel = Tipe Integer
#         kgjeruk = Tipe Integer
#         kgmangga = Tipe Integer
#         pilih = Tipe Integer
#         apel = Tipe Integer
#         jeruk = Tipe Integer
#         mangga = Tipe Integer
#         pa = Tipe Integer
#         pj = Tipe Integer
#         pm = Tipe Integer
#         modalapel = Tipe Integer
#         modaljeruk = Tipe Integer
#         modalmangga = Tipe Integer
#         untung = Tipe Integer
#         modalall = Tipe Integer
#         bersih = Tipe Integer


def main ():
# Program Include input , process , and output
    kgapel = 0
    kgjeruk = 0
    kgmangga = 0
    print("Jenis Buah : 1, Apel, 2. Jeruk, 3. Mangga, 0.Selesai")
    pilih = int(input("Pilih: "))
    while(pilih != 0):
        if(pilih == 1):
            apel = int(input("Berat (kg): "))
            kgapel = kgapel + apel
        elif(pilih == 2):
            jeruk = int(input("Berat (kg): "))
            kgjeruk = kgjeruk + jeruk
        elif(pilih == 3):
            mangga = int(input("Berat (kg): "))
            kgmangga = kgmangga + mangga
        print("="*40)
        print("Jenis Buah : 1, Apel, 2. Jeruk, 3. Mangga, 0.Selesai")
        pilih = int(input("Pilih: "))
    pa = kgapel*9000
    modalapel = round(pa*(0.5))
    pj = kgjeruk*12000
    modaljeruk = round(pj*(0.4))
    pm = kgmangga*15000
    modalmangga = round(pm*(0.6))
    untung = pa + pj + pm
    modalall = modalapel + modaljeruk + modalmangga
    bersih = untung - modalall
    print("Panen hari ini selesai")
    print("="*40)
    print("Detail Panen : ")
    print(kgapel,"kg",end = " ")
    print("Apel Rp. ",pa)
    print("Modal Apel Rp. ",modalapel)
    print("="*40)
    print(kgjeruk,"kg",end = " ")
    print("jeruk  Rp. ",pj)
    print("Modal jeruk Rp. ",modaljeruk)
    print("="*40)
    print(kgmangga,"kg",end = " ")
    print("mangga Rp. ",pm)
    print("Modal mangga Rp. ",modalmangga)
    print("="*40)
    print("Total Pendapatan Rp. ",untung)
    print("Total Modal      Rp. ",modalall)
    print("="*40)
    print("Total Keuntungan Rp. ",bersih)
    print("="*40)
if __name__ == '__main__':
    main()
