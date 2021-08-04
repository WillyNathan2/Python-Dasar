# File : T07A_2072037
# Nama : Willy Natanael Sijabat 2072037
# Deskripsi : Membuat kalkulator sederhana dengan fungsi
# Kamus : a = var integer
#         b = var integer
#         operation = var string
#         temp = var integer

def CalculatorW(a,b,operation):
    if (a < b):
        temp = b
        b = a
        a = temp
    if(operation == "+"):
        print(a,"+",b,"=",int(a+b))
    elif(operation == "-"):
        print(a,"-",b,"=",int(a-b))
    elif(operation == "*" or operation == "x"):
        print(a,"*",b,"=",int(a*b))
    elif(operation == "/"):
        print(a,"/",b,"=",a/b)
    return

def main ():
    a = int(input("a : "))
    b = int(input("b : "))
    operation = str(input("c : "))
    print("Perhitungan: ")
    CalculatorW(a,b,operation)
if __name__=='__main__':
    main()
    
