from perhitungan.nilai import nilai
from perhitungan.gaji import gaji
from perhitungan.login import login
from perhitungan.pembayaran import pembayaran
from perhitungan.kalkulator import kalkulator
from texttable import Texttable
table = Texttable()
login()

def menu():
    
    print ("\n\tSELAMAT DATANG DI SISTEM ADITYAS")
    print ("\tprogram yang tersedia : \n")
    print("1. NILAI")
    print("2. GAJI")
    print("3. KALKULATOR")
    print("4. PEMBAYARAN")
    pilihan()
def pilihan():
    pilih = (input("\nmasukan pilihan anda : "))
    if pilih == "1":
        nilai ()
        lagi ()
        
    elif pilih == "2":
        gaji ()
        lagi ()

    elif pilih == "3":
        kalkulator()
        lagi()

    elif pilih == "4":
        pembayaran()
        lagi()

    else:
        print ("input salah...!")
        pilihan()
        
        
def lagi ():
    tanya = input("\nkembali ke menu utama(y/t)?/" )
    if tanya == "y":
        menu()
        

    elif tanya == "t":
        print ("\n\t----------terima kasih--------")
        exit

    else:
        print("\n\tsalah input........!")
        lagi()
menu()
