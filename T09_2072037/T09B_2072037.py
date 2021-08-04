# File : T09B_2072037.py
# Nama : WIlly Natanael Sijabat 2072037
# Deskripsi : Membuat program validasi binatang kesayangan sesuai dengan data
#             yang diinput

# Kamus data : N = Tipe integer
#              hayo = tipe integer
def main ():
    #Input
    N = int(input("Jumlah Data : "))
    datanama = N * [None] # Type array of string
    datahewan = N * [None] # Type array of string

    for i in range (0,N,1):
        datanama[i] = str(input("nama : "))
        datahewan[i] = str(input("hewan kesayangan : "))

    hayo = str(input("Hewan Kesayangan siapa yang ingin dicari : "))
    validasi = 0
    confirm = 0
    #process with output
    for i in range (0,N,1):
        if(datanama[i] == hayo):
            confirm = i
            validasi = 1
    if(validasi == 1):
        print("Hewan kesayangan",hayo,"adalah",datahewan[confirm])
    elif(validasi != 1):
        print("Tidak ada siswa bernama",hayo,"di dalam data")
       

if __name__ =='__main__':
    main()
