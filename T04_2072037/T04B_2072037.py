# File : T01B_2072037.py
# Nama : Willy Natanael Sijabat 2072037
# Deskripsi : Membuat program sistem perhitungan waktu dengan ketentuan jam digital
# Kamus : hour,minutes,seconds = tipe integer

def main ():
# Program include input and output
    print("="*50)
    hour = int(input("jam: "))
    while(hour <= 0 or hour > 23):
        print("rentang jam dimulai dari 0 sampai 23")
        hour = int(input("jam: "))
    minutes = int(input("menit: "))
    while(minutes <= 0 or minutes > 59):
        print("rentang menit dimulai dari 0 sampai 59")
        minutes = int(input("menit: "))
    seconds = int(input("detik: "))
    while(seconds <=0 or seconds > 59):
        print("rentang detik dimulai dari 0 sampai 59")
        seconds = int(input("detik: "))
    if(hour >= 0 and hour <= 23):
        if(minutes >= 0 and minutes <= 59):
            if(seconds >= 0 and seconds <= 59):
                print("="*50)
                print("waktu: ",hour,":",minutes,":",seconds)
             
if __name__ == '__main__':
    main() 
