#File : T05C_2072037.py
#Nama : Willy Natanael Sijabat 2072037
#Deskripsi : menentukan value input apakah prima atau bukan dengan dibuatkan
#            sebuah process program looping double , di process for sendiri , dibuat
#            var baru dengan value , jika hasil modulo inputan di modulokan dengan increment
#            (i) , jika sama dengan = 0 , maka variabel baru tadi akan bertambah 1
#            fungsinya var baru ini sebagai checker , karena jika looping while sudah beres , maka dia
#            akan mengecek apakah var baru ini bernilai 2 / bukan , dan jika 2 maka bisa dipastikan
#            angka yang diinput merupakan bilangan prima , dan jika bukan , maka akan masuk ke codingan
#            else yang membuat output bahwa angka tersebut bukan angka prima
#            dan program while ini juga prinsip nya sama seperti program dummy , jika diinput 999, maka
#            akan muncul ke print luar while yang menyatakan bahwa program berhenti
#Kamus data : number = tipe integer
#             tes = tipe integer
#             i   = tipe integer

def main ():
# Prgram

    #input
    number = int(input(""))
    #procces with output
    while(number != 999):
        tes = 0
        for i in range (1,number + 1,1):
            if(number % i == 0):
                tes = tes + 1
        if(number < 0):
            print(number,"bukan bilangan bulat positif")
        elif(tes == 2):
            print(number,"adalah bilangan prima")
        else:
            print(number,"bukan bilangan prima")

        number = int(input(""))
    #Finish
    print("Program Berhenti")
if __name__ == '__main__':
    main()   

