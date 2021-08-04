#File : PR03C_2072037.py
#Nama : Willy Natanael Sijabat 2072037
#Deskripsi : Membuat program menghitung total untuk penjumlahan value tahun,bulan,hari
#kamus : year = tipe int
#        bulan = tipe int
#        days = tipe int
#        satuan = tipe int
#        jumlah = tipe int

def main ():
#program include input,procces and output
    print("Usia saat ini")
    year = int(input("Tahun : "))
    bulan = int(input("Bulan :"))
    days = int(input("Hari : "))
    print("Usia saat ini :",year,"tahun",bulan,"bulan",days,"hari")
    print("="*40)
    print("Tambah dalam satuan : \n 1. Tahun \n 2. Bulan \n 3. Hari \n 0. Selesai")
    satuan = int(input("Jenis satuan yang diinginkan : "))
    while(satuan != 0):
        if(satuan == 1):
            jumlah = int(input("Tahun :"))
            year = year + jumlah
            print("Usia saat ini :",year,"tahun",bulan,"bulan",days,"hari")
            print("="*40)

        elif(satuan == 2):
            jumlah = int(input("Bulan :"))
            bulan = bulan + jumlah
            if(bulan >= 12):
                year = year + (bulan // 12)
                bulan = bulan % 12
                print("Usia saat ini :",year,"tahun",bulan,"bulan",days,"hari")
                print("="*40)
            else:
                print("Usia saat ini :",year,"tahun",bulan,"bulan",days,"hari")
                print("="*40)

        elif(satuan == 3):
            jumlah = int(input("Hari :"))
            days = days + jumlah
            if(days >= 365):
                year = year + (days // 365)
                days = days % 365
                if(days >= 30):
                    bulan = bulan + (days//30)
                    days = days % 30
                    print("Usia saat ini :",year,"tahun",bulan,"bulan",days,"hari")
                    print("="*40)
            elif(days < 365):
                if(days >= 30):
                    bulan = bulan + (days//30)
                    days = days % 30
                    if(bulan >= 12):
                        year = year + (bulan //12)
                        bulan = bulan % 12
                        print("Usia saat ini :",year,"tahun",bulan,"bulan",days,"hari")
                        print("="*40)
                    else:
                        print("Usia saat ini :",year,"tahun",bulan,"bulan",days,"hari")
                        print("="*40)
                elif(days <30):
                    print("Usia saat ini :",year,"tahun",bulan,"bulan",days,"hari")
                    print("="*40)
        print("Tambah dalam satuan : \n 1. Tahun \n 2. Bulan \n 3. Hari \n 0. Selesai")
        satuan = int(input("Jenis satuan yang diinginkan : "))
    print("="*40)
    print("Perhitungan selesai!")
    print("Usia saat ini :",year,"tahun",bulan,"bulan",days,"hari")
    print("="*40)
        
if __name__ == '__main__':
    main()          
                


        
        
    
