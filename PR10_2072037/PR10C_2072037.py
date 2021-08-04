# File : PR10C_2072037.py
# Nama : Willy Natanael Sijabat
# Deskripsi Program : membuat program dari kode akan dibuat kalimat
#                     dengan menggunakan array

# Kamus Lokal
# Fungsi Translator adalah untuk mentranslate code int
# N = tipe int (untuk alokasi data)
# arr = array
# c = indeks
# i = var counter
# j = var counter
# word = string
def translator(arrHuruf,arrDigitAngka):
    N = len(arrDigitAngka)
    c = 0
    arr = N * [None]
    for i in range(0,N,1):
        if(arrDigitAngka[i] != None):
            arr[c] = arrDigitAngka[i]
            c = c + 1
            
    c = c - 1    
    arrC = c * [None]
    for i in range(0,c,1):
        word = ""
        for j in range(0,5,1):
            for k in range(0,10,1):
                if(str(arr[i])[j] == str(k)):
                    word = word + arrHuruf[k]
        arrC[i] = word
    return arrC, c

#Kamus data
# arrHuruf = array of string
# arrDigitAngka = array of int
# indeks = tipe int

def main ():
    arrHuruf = [None] * 10
    for i in range(0,10,1):
        arrHuruf[i] = str(input())

    arrDigitAngka = 100 * [None]
    indeks = 0
    arrDigitAngka[indeks]= int(input("5 digit angka : "))
    while (arrDigitAngka[indeks] != 99999):
        indeks = indeks + 1
        arrDigitAngka[indeks] = int(input("5 digit angka : "))

    arrC, batas = translator(arrHuruf,arrDigitAngka)
    print()
    print("Hasil mengartikan : ")    
    for i in range(0,batas,1):
        print(arrC[i])

if __name__ == '__main__':
    main()
