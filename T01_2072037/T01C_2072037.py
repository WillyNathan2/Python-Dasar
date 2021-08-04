# File : T01C_2072037
# Penulis : < Willy Natanael Sijabat >
# Deskripsi :
# Saya pertama menentukan value dari masing-masing bunga yang berbentuk integer,dengan cara dikalikan dengan harga yang sesuai dengan soal
# Lalu saya Membuat Input untuk Jumlah Bunga dalam bentuk Satuan
# Hasil dari value Jumlah bunga dengan Harga bunga saya kalikan masing-masing di dalam beberapa variabel yaitu TotalMawar,TotalMatahari,TotalTulip
# lalu untuk harga Total seluruhnya saya deklarasikan var TotalSeluruhnya dan isinya berupa penjumlahan Hasil dari variabel TotalMawar,TotalMatahari,TotalTulip

#untuk output sudah sesuai dengan yang diminta dengan soal , untuk beberapa properti seperti string saya sesuaikan dengan tampilan yang ada pada soal 





def main ():
 # Program
    Mawar = int(input("Bunga Mawar :"))
    Matahari = int(input("Bunga Matahari :"))
    Tulip = int(input("Bunga Tulip :"))

    TotalMawar = Mawar*75000
    TotalMatahari = Matahari*115000
    TotalTulip = Tulip*220000

    TotalSeluruhnya = TotalMawar + TotalMatahari + TotalTulip

    print("=======================")
    print("Pesanan Hari Ini :")
    
    print("Bunga Mawar :", Mawar)
    print("Bunga Matahari :", Matahari)
    print("Bunga Tulip :", Tulip)

    print("Total pendapatan hari ini :")
    print("Total bunga mawar: Rp.",TotalMawar)
    print("Total bunga matahari: Rp.",TotalMatahari)
    print("Total bunga tulip: Rp.",TotalTulip)
    
    print("Total Seluruhnya: Rp",TotalSeluruhnya)
    print("=======================")
if __name__ == '__main__':
    main()
