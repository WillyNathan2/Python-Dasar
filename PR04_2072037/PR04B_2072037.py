# File : PR04B_2072037.py
# Nama : Willy Natanael Sijabat 2072037
# Deskripsi = membuat deret yang akan memunculkan inputan n dengan pemrosesan
#             di n1 & n2 = n  dan di deret 3 nya n3 = n1 + n2, untuk deret selanjutnya
#             n1 akan dijumlahkan dengan n , n2 akan dikalikan n , dan n3 nya akan dijumlahkan lagi
#             seperti diawal , dan untuk parameter panjang deretnya ditentukan oleh variabel x (input).
# Kamus : n = tipe integer
#         x = tipe integer
#         n1 = tipe integer
#         n2 = tipe integer
#         n3 = tipe integer

def main ():
#Program

    #Input
    n = int(input("n: "))
    x = int(input("x: "))
    n1 = n
    n2 = n
    n3 = n1 + n2
    i = 0
    # process include output
    while(i < x):
        print(n1,n2,n3, end = " ")  
        n1 = n1 + n
        n2 = n2*n
        n3 = n1 + n2
        i += 1
if __name__ == '__main__':
    main()

