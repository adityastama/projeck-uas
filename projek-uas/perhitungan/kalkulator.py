def kalkulator():
    from texttable import Texttable
    table = Texttable()
    
    #dictionary
    jawab = "y"
    no = 0
    num1 = []
    operator = []
    num2 = []
    
    # menu operasi
    print ("=== PROGRAM KALKULATOR ===\n")
    print("Pilih Operasi.")
    print("+.Jumlah")
    print("-.Kurang")
    print("*.Kali")
    print("/.Bagi")

    #pilihan
    while (jawab == "y"):
        
        bil1 = input("masukan angka pertama : ")
    
        num1.append(bil1)

        pilih = input("\nMasukkan operator : ")
        
        if pilih == '+':
            operator.append("+")
            bil2 = input ("\nmasukan angka kedua : ")   
            num2.append(bil2)
            hasil = float(bil1) + float(bil2)
            jawab = input("\nada lagi? (y/t)")
            no += 1
            
        elif pilih == '-':
            operator.append("-")
            bil2 = input ("\nmasukan angka kedua : ")
            num2.append(bil2)
            hasil = float(bil1) - float(bil2)
            jawab = input("\nada lagi? (y/t)")
            no += 1
            
        elif pilih == '*':
            operator.append("*")
            bil2 = input ("\nmasukan angka kedua : ")
            num2.append(bil2)
            hasil = float(bil1) * float(bil2)
            jawab = input("\nada lagi? (y/t)")
            no += 1
           
            
        elif pilih == '/':
            operator.append("/")
            bil2 = input ("\nmasukan angka kedua : ")
            num2.append(bil2)
            hasil = float(bil1) / float(bil2)
            jawab = input("\nada lagi? (y/t)")
            no += 1
        else:
            print ("input salah!")
            break
            
        
        for i in range (no):
            bil1 = (num1[i])
            bil2 = (num2[i])

        
        table.add_rows([["bilangan 1","operator","bilangan kedua","hasil"],[num1[i],operator[i],num2[i],hasil]])
    print (table.draw()) 
 
