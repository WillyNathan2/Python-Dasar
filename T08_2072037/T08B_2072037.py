# File : T08B_2072037.py
# Nama : Willy Natanael Sijabat 2072037
# Deskripsi : membuat program sistem convert mata uang (3 jenis ) dengan menggunakan
#             function untuk masing2 yang mau di convert
# kamus data : convert = tipe integer
#              euro = tipe integer(parameter) fungsi eurotoidr dan eurotousd
#              idr = tipe integer (parameter) fungsi idrtoeuro dan idrtousd
#              usd = tipe integer(parameter) fungsi usdtoeuro dan usdtoidr
              

# Funtion (proccess convert)
def eurotoidr(euro):
    convert = 17393*euro
    return convert

def eurotousd(euro):
    convert = round((17393*euro)/14438)
    return convert

def idrtoeuro(idr):
    convert = round(idr/17393)
    return convert

def idrtousd(idr):
    convert = round(idr/14438)
    return convert

def usdtoeuro(usd):
    convert = round((usd*14438)/17393)
    return convert

def usdtoidr(usd):
    convert = usd*14438
    return convert

# input
def main ():
    print("Mata Uang : ")
    print("1. EUR")
    print("2. IDR")
    print("3. USD")
    confirm = int(input("Mata uang awal : "))
    if(confirm == 1):
        euro = int(input("Jumlah dalam €  "))
    elif(confirm == 2):
        idr = int(input("Jumlah dalam Rp . "))
    elif(confirm == 3):
        usd = int(input("Jumlah dalam $ "))
    last = int(input("Mata uang akhir : "))
#output
    if(confirm == 1 and last == 2):
        print("Rp. ",eurotoidr(euro))
    elif(confirm == 1 and last == 3):
        print("$",eurotousd(euro))
    elif(confirm == 2 and last == 1):
        print("€",idrtoeuro(idr))
    elif(confirm == 2 and last == 3):
        print("$",idrtousd(idr))
    elif(confirm == 3 and last == 1):
        print("€",usdtoeuro(usd))
    elif(confirm == 3 and last == 2):
        print("Rp.",usdtoidr(usd))
        
        
if __name__=='__main__':
    main()
