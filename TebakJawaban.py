def tebak(x):
    tebak = int(input(f"Masukkan angka antara 1 dan {x}: "))

    while tebak <1 or tebak > x:
        tebak = int(input(f"Masukkan angka antara 1 dan {x}: "))
        if tebak < 1:
            print("Coba lagi, Angka Terlalu Rendah")
        elif tebak > x:
            print("Coba lagi, Angka Terlalu Tinggi")
    

       
    gasskeun = input("Kemudian Tambahkan dengan angka 6 [Tekan Enter]")
    if gasskeun == "":
        tebak2 = tebak + 6 
        gasskeun = input("Kemudian Kurangkan dengan angka 3 [Tekan Enter]")
        if gasskeun == "":
            tebak3 = tebak2 - 3
            gasskeun = input("Kemudian Kurangkan dengan angka yang pertama kali diinputkan [Tekan Enter]")
            if gasskeun == "":
                y = tebak3 - tebak
                print("Semoga Tebakan Komputer Benar ya teman-teman\U0001F604")
    jawaban()
    tebakan(y)

def jawaban():
    print("\n")
    print(50*"=")
    print("Kode Jawaban\n")
    print("1. Lamborghini\t 6. Bugatti")
    print("2. Artis\t 7. Musisi")
    print("3. Jeruk\t 8. Speaker")
    print("4. Bolide\t 9. Indomie")
    print("5. Bunga\t 0. Kamboja")
    print(50*"=")
    print("\n")






















def tebakan(y):

   hasil = input(f"Apakah hasilnya adalah... [Tekan Enter]")
   if hasil == "":
       print(y)
       if y == 1:
           print("Kode : Lamborghini")
       elif y == 2:
           print("Kode : Artis")
       elif y == 3:
           print("Kode : Jeruk")
       elif y == 4:
           print("Kode : Bolide")
       elif y == 5:
           print("Kode : Bunga")
       elif y == 6:
           print("Kode : Bugatti")
       elif y == 7:
           print("Kode : Musisi")
       elif y == 8:
           print("Kode : Speaker")
       elif y == 9:
           print("Kode : Indomie")
       elif y == 0:
           print("Kode : Kamboja")
       else:
           print("Pasti Ngitungnya salah\U0001F928 ")

       jawaban = input("\nApakah Jawaban Tersebut benar? [y / n]\n>").lower()
       if jawaban == "y":
           print("Yeyyy... Jawabanku Tepat\U0001F60D")
       elif jawaban == "n":
            print("Masa sih salah\U0001F62D ")
       else:
           print("Ini Bener ga sehh\U0001F611 ")
           tebakan(y)
   else:
       print("Malahhhhh\U0001F612")
       tebakan()


tebak(9)