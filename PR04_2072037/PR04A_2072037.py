#File : PR04A_2072037.py
#Nama : Willy Natanael Sijabat 2072037
#Deskripsi : Membuat program value total bintang(*) maupun garis lurus (|) , sama dengan n
#            Dengan Ketentuan perjarak dari variabel m dengan memberikan tanda garis lurus
#            (|)
#            n = integer
#            m = integer
#            i = integer


def main ():
#Program

    #input 
    n = int(input("n: "))
    m = int(input("m :"))

    i = 0
    garis = 1

    #process include output
    while (i < n):
        if((garis%m) == 0):
            garis = garis + 1       
            print("|", end = " ")
        else:
            garis = garis + 1
            print("*", end = " ") 
        i += 1
if __name__ == '__main__':
    main()

            

        
