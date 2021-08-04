def main() :
# Program
    n = int(input("n: "))
    #Pengulangan
    for i in range(1,n+1,1):
        for j in range(1,4,1):
            for k in range (1,n+1,1):
                print(j, end = " ")
            if (j>=1 and j<=2):
                print("|",end=" ")
        print()
if __name__ == '__main__':
    main()
