# File: PR02B_2072037.py
# Penulis : Willy Natanael Sijabat 2072037
# Deskripsi : membuat program penyesuaian value variabel berdasarkan input dan pengkondisian
#             serta jumlah total dari keseluruhan value , yang diterapkan ke program penyesuaian
#             petak dan jenis turnip,cabbage,cucumber berdasarkan muatan petaknya lalu
#             mentotalkan keseluruhan petak untuk melihat sisa apakah kurang atau masih ada lebih
#Kamus      :  ResultPetak   : TIPE INTEGER
#              JenisONE      : STRING
#              JenisTWO      : STRING
#              JenisTHREE    : STRING
#              x1,x2,x3,y1,y2,y3,z1,z2,z3  : integer
#              TOTALPETAK    : integer
#              sisapetak     : integer

def main ():
    #program include input,process and output
    ResultPetak = int(input("Jumlah petak: "))
    print("======= Penanaman ke-1 =======")
    JenisONE = str(input("Jenis: "))
    if(JenisONE == "1"):
        x1 = int(input("Jumlah turnip :"))
    else:
        x1 = 0
    if(JenisONE == "2"):
        y1 = int(input("Jumlah cabbage :"))
    else:
        y1 = 0
    if(JenisONE == "3"):
        z1 = int(input("Jumlah cucumber :"))
    else:
        z1 = 0

        
    print("======= Penanaman ke-2 =======")

    JenisTWO = str(input("Jenis: "))
    if(JenisTWO == "1"):
        x2 = int(input("Jumlah turnip :"))
    else:
        x2 = 0
    if(JenisTWO == "2"):
        y2 = int(input("Jumlah cabbage :"))
    else:
        y2 = 0
    if(JenisTWO == "3"):
        z2 = int(input("Jumlah cucumber :"))
    else:
        z2 = 0


    print("======= Penanaman ke-3 =======")
    JenisTHREE = str(input("Jenis: "))
    if(JenisTHREE == "1"):
        x3 = int(input("Jumlah turnip :"))
    else:
        x3 = 0
    if(JenisTHREE == "2"):
        y3 = int(input("Jumlah cabbage :"))
    else:
        y3 = 0
    if(JenisTHREE == "3"):
        z3 = int(input("Jumlah cucumber :"))
    else:
        z3 = 0


    print("======= Total Penanaman =======")


    print((x1+x2+x3),"turnip pada",(x1+x2+x3),"petak")
    print( (z1+z2+z3),"cucumber pada " , ((z1*2)+(z2*2)+(z3*2)),"petak")
    print((y1+y2+y3),"cabbage pada",((y1*3) + (y2*3) + (y3*3) ),"petak")
    TOTALPETAK = ((x1+x2+x3)+((z1*2)+(z2*2)+(z3*2))+((y1*3) + (y2*3) + (y3*3)))
    sisapetak = ResultPetak - TOTALPETAK
    print("Total",TOTALPETAK,"petak, tersisa",sisapetak,"petak")
if __name__ == '__main__':
    main()
