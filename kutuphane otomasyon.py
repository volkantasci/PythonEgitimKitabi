sira = ('ID','AD','SOYAD','DOGUM TARIHI', 'UYELIK TARIHI', 'SON ISLEM TARIHI', 'SON ALINAN KITAP', 'SON YAPILAN ISLEM ADI')

kolon_bul = lambda kolon_adi:sira.index(kolon_adi)


def bilgi_cek(id_no:int, kolon:str):
    dosya = open('C:\\Users\\propr\\Desktop\\uyeler.csv',encoding='utf-8')
    satirlar = dosya.readlines()
    dosya.close()

    satirlar.remove(satirlar[0])

    for indeks,i in enumerate(satirlar):
        satirlar[indeks] = i.split(',')

    
    for i in satirlar:
        if int(i[0]) == id_no:
            return i[kolon_bul(kolon)]
    
    return("Aranan ID numarasına ait üye bulunamadı!")
    



def uye_ekle():
    isim = input('Ad: ')
    soyisim = input('Soyad: ')
    dogum_tarihi = input('Doğum Tarihi Örnek(01-01-1992): ')
    uyelik_tarihi = input('Üyelik Tarihi Örnek(01-01-1992): ')
    son_islem_tarihi = input('Son İşlem Tarihi Örnek(01-01-1992 14:30): ')
    #son_alinan_kitap = input('Son Alınan Kitap: ')
    son_yapilan_islem = input('Son Yapılan İşlem: Örnek(Kitap Alındı): ')

    dosya = open('C:\\Users\\propr\\Desktop\\uyeler.csv',encoding='utf-8', mode='r')
    satirlar = dosya.readlines()
    dosya.close()
    
    satirlar.remove(satirlar[0])

    for indeks,i in enumerate(satirlar):
        satirlar[indeks] = i.split(',')
    
    if satirlar:
        son_id = int(satirlar[-1][0])
    else:
        son_id = 0
    yeni_uye = [
        str(son_id+1),
        isim,
        soyisim,
        dogum_tarihi,
        uyelik_tarihi,
        son_islem_tarihi,
        '--',
        son_yapilan_islem
    ]

    text = ",".join(yeni_uye) + '\n'
    
    dosya = open('C:\\Users\\propr\\Desktop\\uyeler.csv',encoding='utf-8', mode='a')
    dosya.write(text)
    dosya.close()

    print('Üye işlemi tamamlandı!')


def kayit_dosyasi_olustur(dizin_yolu:str):
    dosya = open(dizin_yolu + '\\uyeler.csv', 'x')
    text = "ID,AD,SOYAD,DOGUM TARIHI,UYELIK TARIHI,SON ISLEM TARIHI,SON ALINAN KITAP,SON YAPILAN ISLEM ADI"
    dosya.write(text+"\n")
    dosya.close()


def uye_sil(id_no:int):
    dosya = open('C:\\Users\\propr\\Desktop\\uyeler.csv',encoding='utf-8', mode='r')
    satirlar = dosya.readlines()
    dosya.close()
    
    satirlar.remove(satirlar[0])

    for indeks,i in enumerate(satirlar):
        satirlar[indeks] = i.split(',')
    
    yeni_liste = satirlar.copy()

    for i in satirlar:
        if id_no == int(i[0]):
            yeni_liste.remove(i)
            dosya = open('C:\\Users\\propr\\Desktop\\uyeler.csv', 'w',encoding='utf-8')
            kolonlar = "ID,AD,SOYAD,DOGUM TARIHI,UYELIK TARIHI,SON ISLEM TARIHI,SON ALINAN KITAP,SON YAPILAN ISLEM ADI"
            dosya.write(kolonlar + '\n')
            
            for i in yeni_liste:
                satir = ",".join(i)
                dosya.write(satir)
            
            dosya.close()
            return None
    
    print("Bu ID numarasına sahip üye bulunamadı!")


def kitaplik_olustur(dizin_yolu:str):
    dosya = open(dizin_yolu + '\\kitaplar.csv', 'x')
    dosya.write('ID,ADI,YAZAR ADI,BASIM TARIHI,BASKI SAYISI,SAYFA SAYISI,YAYINEVI,ALAN UYE\n')
    dosya.close()


def kitap_ekle(isim,yazar,basim_tarihi,baski_sayisi,sayfa_sayisi,yayinevi):
    dosya = open('C:\\Users\\propr\\Desktop\\kitaplar.csv', 'r', encoding='utf-8')
    satirlar = dosya.readlines()
    dosya.close()

    satirlar.remove(satirlar[0])

    if satirlar:
        for indeks,i in enumerate(satirlar):
            satirlar[indeks] = i.split(',')

        son_id = int(satirlar[-1][0])
    
    else:
        son_id = 0
    
    id_no = str(son_id + 1)
    baski_sayisi = str(baski_sayisi)
    sayfa_sayisi = str(sayfa_sayisi)

    kitap = [
        id_no,
        isim,
        yazar,
        basim_tarihi,
        baski_sayisi,
        sayfa_sayisi,
        yayinevi,
        '--' #Değiştirilen kısım burası. Yeni bir öğe ekleniyor.
    ]

    text = ','.join(kitap) + '\n'
    dosya = open('C:\\Users\\propr\\Desktop\\kitaplar.csv', 'a', encoding='utf-8')
    dosya.write(text)
    dosya.close()



def kitap_al(kitap_id, uye_id):
    # kitaplar ve üyeler veritabanını değişkenlere almalıyız.

    with open('C:\\Users\\propr\\Desktop\\kitaplar.csv', encoding='utf-8') as kitaplar:
        k_satirlar = kitaplar.readlines()
    
    with open('C:\\Users\\propr\\Desktop\\uyeler.csv', encoding='utf-8') as uyeler:
        u_satirlar = uyeler.readlines()

    kitap_flag = False
    uye_flag = False

    for indeks, i in enumerate(k_satirlar):
        k_satirlar[indeks] = i.split(',')
        
        if i[0] == str(kitap_id) and i[-1] == '--\n':
            kitap_flag = True
    

    for indeks, i in enumerate(u_satirlar):
        u_satirlar[indeks] = i.split(',')
        
        if i[0] == str(uye_id) and i[-2] == '--':
            uye_flag = True

    
    if uye_flag and kitap_flag:

        for i in k_satirlar:
            if i[0] == str(kitap_id):
                i[-1] = str(uye_id) + '\n'  #!! Değişiklik burada yapıldı. kitaplar verisi değiştirildi
                break

        with open('C:\\Users\\propr\\Desktop\\kitaplar.csv', mode='w', encoding='utf-8') as kitaplar:
            for i in k_satirlar:  #!! değişiklik yapıldı
                kitaplar.write(",".join(i))  #kitaplar veritabanı değiştirildi
        
        with open('C:\\Users\\propr\\Desktop\\uyeler.csv', mode='w', encoding='utf-8') as uyeler:
            for i in u_satirlar:
                if i[0] == str(uye_id):
                    i[kolon_bul('SON ALINAN KITAP')] = str(kitap_id)
                    i[kolon_bul('SON YAPILAN ISLEM ADI')] = "Kitap Alındı\n" 
                    # Üyeler veritabanı değiştirldi
                uyeler.write(",".join(i))
    
    else:
        print("Kitap ya da Üye meşgul yahut bulunamadı!")


def kitap_teslim_et(kitap_id, uye_id):

    with open('C:\\Users\\propr\\Desktop\\kitaplar.csv', encoding='utf-8') as kitaplar:
        k_satirlar = kitaplar.readlines()
    
    with open('C:\\Users\\propr\\Desktop\\uyeler.csv', encoding='utf-8') as uyeler:
        u_satirlar = uyeler.readlines()

    kitap_flag = False
    uye_flag = False

    for indeks, i in enumerate(k_satirlar):
        k_satirlar[indeks] = i.split(',')
        
    
    for indeks, i in enumerate(k_satirlar):
        if i[0] == str(kitap_id) and i[-1] == str(uye_id) +'\n': #değişiklik burada
            kitap_flag = True
            
    

    for indeks, i in enumerate(u_satirlar):
        u_satirlar[indeks] = i.split(',')
        
    for indeks, i in enumerate(u_satirlar):
        if i[0] == str(uye_id) and i[-2] == str(kitap_id):
            uye_flag = True
            

    
    if uye_flag and kitap_flag:

        for i in k_satirlar:
            if i[0] == str(kitap_id):
                i[-1] = '--' + '\n'  #değişiklik burada
                break

        with open('C:\\Users\\propr\\Desktop\\kitaplar.csv', mode='w', encoding='utf-8') as kitaplar:
            for i in k_satirlar:
                kitaplar.write(",".join(i))
        
        with open('C:\\Users\\propr\\Desktop\\uyeler.csv', mode='w', encoding='utf-8') as uyeler:
            for i in u_satirlar:
                if i[0] == str(uye_id):
                    i[kolon_bul('SON ALINAN KITAP')] = '--' #değişiklik burada
                    i[kolon_bul('SON YAPILAN ISLEM ADI')] = "Kitap Teslim Edildi\n"  #değişiklik burada

                uyeler.write(",".join(i))
    
    else:
        print("Kitap ya da Üye bilgilerinin doğruluğunu kontrol ediniz!") #değişiklik burada
