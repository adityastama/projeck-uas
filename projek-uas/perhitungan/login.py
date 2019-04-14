def login():
    import getpass
    ulang = "y"

    while ulang == "y":
        username =input("Masukan user name anda : ")
        sandi = getpass.getpass("masukan sandi : ")
        if (username == "adi" and sandi == "123"):
            print ("anda telah login\n")
            break
        else:
            print ("nama atau password anda salah\n")
