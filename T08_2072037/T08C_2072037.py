# File : T08C_2072037.py
# Nama : Willy Natanael Sijabat
# Deskripsi : Membuat Program slip gaji dengan pengkondisian fungsi
def gajipokok(gol):
    
    if (gol == "I"):
        print("Gaji Pokok : 6.000.000")
    elif(gol == "II"):
        print("Gaji Pokok : 5.000.000")
    elif(gol == "III"):
        print("Gaji Pokok : 4.500.000")

def tunjangankes(gol):
    if (gol == "I"):
        print("Tunjangan Kesehatan : 450.000")
    elif(gol == "II"):
        print("Tunjangan Kesehatan : 350.000")
    elif(gol == "III"):
        print("Tunjangan Kesehatan : 300.000")

def tunjangankel(status,kelamin,gol):
    if(status == "m" and kelamin == "l"):
        if (gol == "I"):
            print("Tunjangan Keluarga : ",round(6000000*0.15))
        elif(gol == "II"):
            print("Tunjangan Keluarga : ",round(5000000*0.15))
        elif(gol == "III"):
            print("Tunjangan Keluarga : ",round(4500000*0.15))
            
def gajikotor(gol,status,kelamin):
    if (gol == "I" ):
        seluruh = 6000000
        if(gol == "I" and status == "m" and kelamin == "l"):
            seluruh = 6000000 + 450000 + 900000
            print("Gaji Kotor : ",seluruh)
        else:
            print("Gaji Kotor : ",seluruh)
    elif (gol == "II"):
        seluruh = 5000000
        if(gol == "II" and status == "m" and kelamin == "l"):
            seluruh = 5000000 + 350000 + (5000000*0.15)
            print("Gaji Kotor : ",seluruh)
        else:
            print("Gaji Kotor : ",seluruh)
    elif(gajipokok == "III"):
        if(gol == "II" and status == "m" and kelamin == "l"):
            seluruh = 4500000 + 300000 + (4500000*0.15)
            print("Gaji Kotor : ",seluruh)
        else:
            print("Gaji Kotor : ",seluruh)
            
def pajak (gol,status,kelamin):
    if (gol == "I" ):
        seluruh = 6000000
        if(gol == "I" and status == "m" and kelamin == "l"):
            seluruh = 6000000 + 450000 + 900000
            pajak = 0
            if(seluruh >= 5000000):
                pajak = seluruh*0.05
                print("pajak : ",pajak)
            else :
                print("pajak : ",pajak)
        else:
            print("pajak : ",pajak)
    elif (gol == "II"):
        seluruh = 5000000
        pajak = seluruh*0.05
        if(gol == "II" and status == "m" and kelamin == "l"):
            seluruh = 5000000 + 350000 + (5000000*0.15)
            pajak = 0
            if(seluruh >= 5000000):
                pajak = seluruh*0.05
                print("pajak : ",pajak)
            else:
                print("pajak : ",pajak)
        else:
            print("pajak : ",pajak)
    elif(gajipokok == "III"):
        if(gol == "II" and status == "m" and kelamin == "l"):
            seluruh = 4500000 + 300000 + (4500000*0.15)
            pajak = seluruh*0.05
            print("pajak : ",pajak)
        else:
            print("pajak : ",pajak)

def main ():
    nama = str(input("Nama : "))
    kelamin = str(input("Jenis Kelamin (1/p): "))
    status = str(input("Status menikah (m/t) : "))
    gol = str(input("Golongan (I/II/III): "))
    print("Nama : ",nama)
    gajipokok(gol)
    tunjangankes(gol)
    tunjangankel(status,kelamin,gol)
    print("="*30)
    gajikotor(gol,status,kelamin)
    pajak(gol,status,kelamin)
    
if __name__=='__main__':
    main()
