# File : PR07B_20U72037.py
# Nama : Willy Natanael Sijabat 2072037
# Deskripsi : membuat kotak yang pattern percetak nya adalah deret mundur , dengan
#             pengkondisian jika yang tercetaknya terdapat 2 digit angka
#             seperti (10/11 dan seterusnya), maka angka sisanya (<9) harus ditambah 0 dibelakang
#             angkanya, sedangka jika tidak terdapat 2 digit angka maka tidak perlu ditambah 0 dibelakang angkanya
# kamus lokal : parameter fungsi kotak adalah (n)
# Kamus data : m = tipe integer (di pengkondisian tertentu diubah menjadi string)
#              n = tipe integer
#              i = tipe integer
#              j = tipe integer

#Program include process and output
def kotak(n):
    m = (n*n)
    for i in range (1,n+1,1):
        for j in range(1,n+1,1):
            if(n >= 4):
                print(str(m).zfill(2),end = " ")
            elif(n <= 3):
                print(m, end = " ")
            m = m - 1
        print()
    
def main ():
    # Input
    n = int(input("n : "))
    kotak(n)
if __name__=='__main__':
    main()
