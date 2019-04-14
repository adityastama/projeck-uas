def gaji():
    from texttable import Texttable
    table = Texttable ()

    print ("\n\tPROGRAM PENGGAJIAN\n")
    print ("DAFTAR GAJI :\n")
    print ("1. programmer = 3000.000")
    print ("2. leader     = 3500.000")
    print ("3. supervisor = 4000.000")
    print ("\n jika jabatan tidak ada, tidak akan di proses....\n")
    jawab = "y"
    no = 0
    nama = []
    jabatan = []
    gaji = []

    while (jawab == 'y'):
        NAMA = input("masukan nama: ")
        jab = input ("jabatan: ")
        if (jab == 'programmer' ):
            nama.append(NAMA)
            jabatan.append(jab)
            gaji.append(3000000)
            jawab = input("\n ada lagi? (y/t)")
            no += 1
        elif(jab == 'leader' ):
            nama.append(NAMA)
            jabatan.append(jab)
            gaji.append(3500000)
            jawab = input("\n ada lagi? (y/t)")
            no += 1
        elif (jab == 'supervisor' ):
            nama.append(NAMA)
            jabatan.append(jab)
            gaji.append(4000000)
            jawab = input("\n ada lagi? (y/t)")
            no += 1
        else:
            print ("jabatan tidak ditemukan...!")
            jawab = input("\n ada lagi? (y/t)")
    
    for i in range (no) :
    
        table.add_rows([['No','Nama','Jabatan','gaji'],[i+1,nama[i],jabatan[i],gaji[i]]])
       
    print (table.draw())

