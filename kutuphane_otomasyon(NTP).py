class Kitap:
    def __init__(self, ad, yazar, sayfa_sayisi, yayinevi, basim_yili, id_no):
        self.ad = ad
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.basim_yili = basim_yili
        self.yayinevi = yayinevi
        self.id_no = id_no

    def __str__(self):
        return "Kitap: {} -- Yazar: {} -- Sayfa Sayısı: {} -- Basım Yılı: {} -- Yayınevi: {} -- ID: {}".format(self.ad, self.yazar, self.sayfa_sayisi, self.basim_yili, self.yayinevi, self.id_no)


class Uye:
    def __init__(self, isim, soyisim, dogum_tarihi):
        self.ad = isim
        self.soyad = soyisim
        self.dogum_tarihi = dogum_tarihi
        self.alinan_kitaplar = list()
        self.son_alinan_kitap = None # Kitap alındığında değişecek.
        self.favoriler = list()
        self.alinan_etkin_kiap_sayisi = 0 # En fazla 3 kitaba aynı anda sahip olunabilir
        self.etkin_kitaplar = list()

    def favori_ekle(self, kitap):
        if kitap not in self.favoriler:
            self.favoriler.append(kitap)

        else:
            print("Bu kitap zaten favorilerde ekli!")


    def favori_sil(self, kitap):
        if kitap in self.favoriler:
            self.favoriler.remove(kitap)

        else:
            print("Bu kitap favorilerinizde bulunmuyor!")


    def kitap_al(self, kitap):
        if self.alinan_etkin_kiap_sayisi < 3:
            if kitap not in self.alinan_kitaplar:
                self.alinan_kitaplar.append(kitap)
            
            self.etkin_kitaplar.append(kitap)
            self.alinan_etkin_kiap_sayisi += 1
            self.son_alinan_kitap = kitap

        else:
            print("Daha fazla kitap alamazsınız!")

    def kitap_teslim_et(self, kitap):
        if kitap in self.etkin_kitaplar:
            self.etkin_kitaplar.remove(kitap)
            self.alinan_etkin_kiap_sayisi -= 1


        else:
            print("Kitap bu üyede mevcut değil!")

    def __str__(self):
        return "Ad: {} -- Soyad: {} -- Son Alınan Kitap: {}".format(self.ad, self.soyad, self.son_alinan_kitap)


class Kutuphane:
    def __init__(self):
        self.kitaplar = list()
        self.uyeler = list()
        self.yazarlar = set()



    def uye_ekle(self, uye):
        if uye not in self.uyeler:
            self.uyeler.append(uye)

        else:
            print("Üye zaten mevcut!")
    

    def uye_sil(self, uye):
        if uye in self.uyeler:
            self.uyeler.remove(uye)
        
        else:
            print("Bu üyenin zaten kaydı yok!")


    def yazar_kume_yenile(self):
        self.yazarlar = set()
        
        for i in self.kitaplar:
            self.yazarlar.add(i.yazar)


    def kitap_ekle(self, kitap):
        if kitap not in self.kitaplar:
            self.kitaplar.append(kitap)
            self.yazar_kume_yenile()

        else:
            print("Bu kitap zaten kütüphanede!")


    def kitap_cikar(self, kitap):
        if kitap in self.kitaplar:
            self.kitaplar.remove(kitap)
            self.yazar_kume_yenile()

        else:
            print("Kütüphanede mevcut olmayan bir kitabı çıkarmaya çalışıyorsunuz!")


    def yazarlar_bilgi(self):
        return self.yazarlar
