class islemler :
    def tarif_ekle(self) :
        tarif_adi = input("tarif adi : ")
        tarif.append(tarif_adi)
        while True :  
            tarif_adim = input("tarif adim(adımlar bittiyse -1 giriniz) : ")
            if tarif_adim == "-1" :
                tarifler_listesi.append(tarif)
                tarif.append("\n")
                break
            else :
                tarif.append(tarif_adim)
            

    def listele(self) :
        sayi = len(tarifler_listesi)
        print("Tüm Tarifler")    
        for adim in tarif :
                print(adim)



        
def ana_menu() :
    while True :
        print("\nYeni tarif eklemek için : 1\nVar olan tarifleri listelemek için : 2\nÇıkış yapmak için : 3 ")
        secim = input("yapmak istediğiniz işlem numarasını giriniz : ")
        islem = islemler()
        if secim == "1" :
            islem.tarif_ekle()
        elif secim == "2" :
            islem.listele()
        elif secim == "3" :
            exit(0)
        else :
            print("hatalı seçim lütfen yapacağınız işlemi tekrar seçiniz")



tarifler_listesi = []
tarif = []

ana_menu()

