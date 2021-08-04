# File : PR08C_2072037.py
# Nama : Willy Natanael Sijabat 2072037
# Nama Fungsi : uangmuka(dp,pricecar) -- > untuk mencari uang muka
#               plafon(pricecar,dp) -- > untuk melakukan perhitungan plafon pinjaman
#               cicilanbln(pricecar,dp,bunga,tenor) -- > menentukan cicilan per bulan
#               subtotal(dp,pricecar,bunga,tenor) -- > total pembayaran pertama (uang muka + plafon + cicilan per bulan)
#               hrgmobil(dp,pricecar,bunga,tenor) -- > total harga mobil
# Kamus Data : pricecar = tipe integer
#              dp = tipe integer
#              bunga = tipe integer
#              tenor = tipe integer



# Proccess
def uangmuka(dp,pricecar):
    moneyface = round((dp/100)*pricecar)
    
    return 

def plafon(pricecar,dp):
    pinjaman = pricecar - uangmuka(dp,pricecar)
    
    return pinjaman

def cicilanbln(pricecar,dp,bunga,tenor):
    cicilan = (plafon(pricecar,dp))*((1 + (bunga/100))/(tenor*12))
    
    return cicilan

def subtotal(dp,pricecar,bunga,tenor):
    totalfirst = uangmuka(dp,pricecar) + cicilanbln(pricecar,dp,bunga,tenor) + 500000
    
    return totalfirst

def hrgmobil(dp,pricecar,bunga,tenor):
    hargamobil = subtotal(dp,pricecar,bunga,tenor) + (cicilanbln(pricecar,dp,bunga,tenor)*(tenor*12 - 1))
    print("Total harga mobil : Rp. ",round(hargamobil))
                                                      
# Input & Output
def main():
    pricecar = int(input("Harga mobil : Rp. "))
    dp = int(input("Uang muka (%) : "))
    bunga = int(input("Suku bunga flat per tahun (%) : "))
    tenor = int(input("Lama tenor (tahun): "))
    print("="*47)
    print("Uang Muka : Rp. ",uangmuka(dp,pricecar))
    print("Plafon pinjaman : Rp. ",plafon(pricecar,dp))
    print("Cicilan per bulan : Rp. ",round(cicilanbln(pricecar,dp,bunga,tenor)))
    print("Total pembayaran pertama : Rp. ",round(subtotal(dp,pricecar,bunga,tenor)))
    print("="*47)
    hrgmobil(dp,pricecar,bunga,tenor)
    
if __name__=='__main__':
    main()
