def pembayaran():
    from texttable import Texttable
    table = Texttable(max_width=1000)

    print ("\n\tSISTEM PEMBAYARAN MAHASISWA\n")
    jawab ="y"
    no = 0
    nim = []
    nama = []
    kelas = []
    uts = []
    uas = []
    spp = []
    seminar = []
    kas = []
    administrasi = []
    total = []
    
    while (jawab == "y"):
        nim.append(input("masukan nim : "))
        nama.append(input("masukan nama : "))
        kelas.append(input("masukan kelas : "))
        print ("\n=============================================")   
        print ("biaya spp perbulan = Rp.500000")
        Spp = int(input("\nmasukan jumlah spp yang ingin dibayar: "))
        spp.append(int(Spp) * 500000)
        print ("anda akan membayar spp sebesar Rp.", Spp*500000)
        print("\n================================")
        print("pilih pembayaran yang diinginkan?\n")
        print("1. UTS = 250.000")
        print("2. UAS = 250.000")
        print("3. Tidak membayar UTS/UAS")
        
        pilih = input("\ntentukan pilihan anda ( 1 / 2 /3 ) : ")
        if (pilih == "1"):
            print ("\nanda akan membayar UTS sebesar Rp.250.000")
            uts.append(250000)
            uas.append(0)
            
        elif(pilih == "2"):
            print ("\nanda akan membayar UAS sebesar Rp.250.000")
            uts.append(0)
            uas.append(250000)

        elif(pilih == "3"):
            uts.append(0)
            uas.append(0)
            
        else:
            print("kode invalid...")
            break

        print("\nbiaya seminar 1x pertemuan = Rp.100000")
        SEMINAR = input("\nApakah anda ingin membayar seminar? ( y / t ) : ")
        if (SEMINAR == 'y'):
            print ("\nanda akan membayar seminar sebesar Rp.100000")
            seminar.append(100000)
        elif(SEMINAR == 't'):
            seminar.append(0)
        else:
            print("input salah")
            break
        KAS = input("\nApakah anda ingin membayar uang kas? ( y / t ) : ")
        if(KAS == 'y'):
            KAS2 = input ("\nuntuk berapa bulan : ")
            kas.append(int(KAS2) * 20000)
        elif(KAS == 't'):
            kas.append(0)
        else:
            print("input salah")
            break

        print ("\ntambahan biaya adminstrasi dikenakan sebesar Rp.5000")
        administrasi.append(5000)
        
        jawab = input ("\nada lagi? (y/t) : ")
        no += 1
        
    for i in range (no):
        buas = int(uas[i])
        buts = int(uts[i])
        bspp = int(spp[i])
        bseminar = int(seminar[i])
        bkas = int(kas[i])
        badministrasi = int(administrasi[i])

        total =(buas + buts + bspp + bseminar + bkas + badministrasi)

        table.set_cols_dtype(['a','i','i','i','i','i','i','i','i','i','i'])
        table.add_rows([["NO","NAMA","NIM","KELAS","UTS","UAS","SPP","SEMINAR","KAS","ADMINSTRASI","TOTAL"],[i+1,nama[i],nim[i],kelas[i],uts[i],uas[i],spp[i],seminar[i],kas[i],administrasi[i],total]])
    print(table.draw())          
            
