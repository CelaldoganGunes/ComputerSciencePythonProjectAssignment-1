# Sabitler

SURE_BIR_SAATTEN_AZ = 3
SURE_UC_SAATTEN_AZ = 5
SURE_BES_SAATTEN_AZ = 7
SURE_ON_SAATTEN_AZ = 10
SURE_YIRMIDORT_SAATTEN_AZ = 14
SURE_HER_YIRMIDORT_SAAT = 15

KATSAYI_MOTORSIKLET = 1
KATSAYI_BINEK = 2
KATSAYI_MINIBUS = 3
KATSAYI_OTOBUS = 3
KATSAYI_KAMYON = 4
KATSAYI_TIR = 4

SINIF_KODU_MOTORSIKLET = 1
SINIF_KODU_BINEK = 2
SINIF_KODU_MINIBUS = 3
SINIF_KODU_OTOBUS = 4
SINIF_KODU_KAMYON = 5
SINIF_KODU_TIR = 6

INDIRIM_ORANI_GAZI = 100
INDIRIM_ORANI_ENGELLI = 50

#Fonksiyonlar

def sinif_kodundan_arac_sinifini_ogren(sinif_kodu):  # araç sınıfını girerek string cinsinden türü ve katsayı değeri elde edilir.
    if sinif_kodu == SINIF_KODU_MOTORSIKLET:
        return "motorsiklet", KATSAYI_MOTORSIKLET
    elif sinif_kodu == SINIF_KODU_BINEK:
        return "binek", KATSAYI_BINEK
    elif sinif_kodu == SINIF_KODU_MINIBUS:
        return "minibus", KATSAYI_MINIBUS
    elif sinif_kodu == SINIF_KODU_OTOBUS:
        return "otobüs", KATSAYI_OTOBUS
    elif sinif_kodu == SINIF_KODU_KAMYON:
        return "kamyon", KATSAYI_KAMYON
    elif sinif_kodu == SINIF_KODU_TIR:
        return "tır", KATSAYI_TIR

def sure_hesaplama(dakika,donus_tipi):  # dakika cinsinden girilen süreyi gün, saat, ve dakikaya string ve int cinsinden yazdırıyor.
    saat = dakika//60
    artik_dakika = dakika % 60
    gun = saat//24
    artik_saat = saat % 24

    # Fonksiyonun kullanıldığı yerin ihtiyacına göre zamanı farklı veri tipinde döndürüyoruz.
    if donus_tipi == "sayi":
        return gun, artik_saat, artik_dakika
    elif donus_tipi == "metin":
        return f"{gun} gün, {artik_saat} saat, {artik_dakika} dakika"

def main():

    #Değişkenler

    arac_var = "e"

    arac_sayisi_toplam = 0
    arac_sayisi_motorsiklet = 0
    arac_sayisi_binek = 0
    arac_sayisi_minibus = 0
    arac_sayisi_otobus = 0
    arac_sayisi_kamyon = 0
    arac_sayisi_tir = 0

    ucret_toplam_tum_araclar = 0
    ucret_toplam_motorsiklet = 0
    ucret_toplam_binek = 0
    ucret_toplam_minibus = 0
    ucret_toplam_otobus = 0
    ucret_toplam_kamyon = 0
    ucret_toplam_tir = 0

    sure_dakika_motorsiklet = 0
    sure_dakika_binek = 0
    sure_dakika_minibus = 0
    sure_dakika_otobus = 0
    sure_dakika_kamyon = 0
    sure_dakika_tir = 0

    bir_tondan_hafif_binek_arac_sayisi = 0
    on_tondan_agir_buyuk_arac_sayisi = 0
    otuz_dakika_alti_arac = 0
    bir_gunden_fazla_otobus_minibus = 0
    otuz_gunden_fazla_veya_bin_tlden_fazla_arac_sayisi = 0
    gazi_arac_sayisi = 0
    engelli_arac_sayisi = 0
    gazi_arac_park_suresi = 0
    engelli_arac_park_suresi = 0

    indirimli_uc_saatten_cok_arac_sayisi = 0

    en_uzun_kalan_aracin_suresi = 0
    en_uzun_kalan_aracin_tutari = 0
    en_masrafli_binek_aracin_suresi = 0
    en_masrafli_binek_aracin_ucreti = 0

    while arac_var == "e" or arac_var == "E":

        #Inputlar

        arac_plakasi = input("Plakayı girin: ")
        arac_sinifi_kodu = int(input("Araç sınıfı kodunu girin (1: motor, 2:binek, 3:minibus, 4:otobus, 5:kamyon, 6:tır): "))

        while not arac_sinifi_kodu in range(1, 7):
            arac_sinifi_kodu = int(input("Araç sınıfı kodunu girin (1: motor, 2:binek, 3:minibus, 4:otobus, 5:kamyon, 6:tır): "))

        arac_agirligi = float(input("Araç ağırlığını kg cinsinden girin: "))

        while arac_agirligi <= 0:
            arac_agirligi = float(input("Araç ağırlığını kg cinsinden girin: "))

        arac_otoparkta_kaldigi_sure = int(input("Aracın otoparkta kaç dakika kaldığını yazın: "))

        while arac_otoparkta_kaldigi_sure <= 0:
            arac_otoparkta_kaldigi_sure = int(input("Aracın otoparkta kaç dakika kaldığını yazın: "))

        surucu_ad_soyad = input("Sürücünün adını ve soyadını girin: ")

        ozel_durum = "y"
        if arac_sinifi_kodu == 1 or arac_sinifi_kodu == 2:
            ozel_durum = input("(Varsa) Sürücünün özel durumunu girin (y/Y/g/G/e/E): ")
            while not (ozel_durum == "y" or ozel_durum == "Y" or ozel_durum == "G" or ozel_durum == "g" or ozel_durum == "E" or ozel_durum == "e"):
                ozel_durum = input("(Varsa) Sürücünün özel durumunu girin (y/Y/g/G/e/E): ")

        # Araç Bilgileri Print

        print()
        print(f"Aracın plakası: {arac_plakasi}")

        sinif_adi, sinif_katsayi = sinif_kodundan_arac_sinifini_ogren(arac_sinifi_kodu)
        print(f"Aracın sınıfı: {sinif_adi}")
        print(f"Aracın ağırlığı: {arac_agirligi:.2f} KG")
        dd, hh, mm = sure_hesaplama(arac_otoparkta_kaldigi_sure,"sayi")
        print(f"Aracın otoparkta kaldığı süre: {dd} gün {hh} saat {mm} dakika")

        print(f"Sürücünün adı ve soyadı: {surucu_ad_soyad}")

        # İndirim Oranı Hesaplama

        indirim_orani = 0
        if ozel_durum == "g" or ozel_durum == "G":
            print(f"Gazi indirim oranı: %{INDIRIM_ORANI_GAZI}")
            indirim_orani = INDIRIM_ORANI_GAZI
            print(f"Sürücünün özel durumu: Gazi")
            gazi_arac_sayisi += 1
            gazi_arac_park_suresi += arac_otoparkta_kaldigi_sure
            if arac_otoparkta_kaldigi_sure > 180:
                indirimli_uc_saatten_cok_arac_sayisi += 1
        elif ozel_durum == "e" or ozel_durum == "E":
            print(f"Engelli indirim oranı: %{INDIRIM_ORANI_ENGELLI}")
            indirim_orani = INDIRIM_ORANI_ENGELLI
            print(f"Sürücünün özel durumu: Engelli")
            engelli_arac_sayisi += 1
            engelli_arac_park_suresi += arac_otoparkta_kaldigi_sure
            if arac_otoparkta_kaldigi_sure > 180:
                indirimli_uc_saatten_cok_arac_sayisi += 1

        # Ucret Hesaplama

        ucret_gun = dd * SURE_HER_YIRMIDORT_SAAT

        if hh == 0 and mm == 0:
           ucret_saat = 0
        elif hh == 0 and mm > 0:
            ucret_saat = SURE_BIR_SAATTEN_AZ
        elif hh < 3:
            ucret_saat = SURE_UC_SAATTEN_AZ
        elif hh < 5:
            ucret_saat = SURE_BES_SAATTEN_AZ
        elif hh < 10:
            ucret_saat = SURE_ON_SAATTEN_AZ
        elif hh < 24:
            ucret_saat = SURE_YIRMIDORT_SAATTEN_AZ

        ucret_sure = sinif_katsayi * (ucret_gun + ucret_saat)

        ucret_giris = (arac_agirligi / 1000) * 2.5
        ucret_toplam = ucret_giris + ucret_sure

        ucret_toplam -= ucret_toplam * indirim_orani / 100
        ucret_toplam_tum_araclar += ucret_toplam

        print(f"Otopark ücreti: {round(ucret_toplam,2)} TL")

        # Araç İstatistiklerine Dair Hesaplamalar

        arac_sayisi_toplam += 1
        if sinif_adi == "motorsiklet":
            arac_sayisi_motorsiklet += 1
            ucret_toplam_motorsiklet += ucret_toplam
            sure_dakika_motorsiklet += arac_otoparkta_kaldigi_sure

        elif sinif_adi == "binek":
            arac_sayisi_binek += 1
            ucret_toplam_binek += ucret_toplam
            sure_dakika_binek += arac_otoparkta_kaldigi_sure
            if en_masrafli_binek_aracin_ucreti < ucret_toplam:
                en_masrafli_binek_aracin_ucreti = ucret_toplam
                en_masrafli_binek_aracin_suresi = arac_otoparkta_kaldigi_sure
        elif sinif_adi == "minibus":
            arac_sayisi_minibus += 1
            ucret_toplam_minibus += ucret_toplam
            sure_dakika_minibus += arac_otoparkta_kaldigi_sure

        elif sinif_adi == "otobüs":
            arac_sayisi_otobus += 1
            ucret_toplam_otobus += ucret_toplam
            sure_dakika_otobus += arac_otoparkta_kaldigi_sure

        elif sinif_adi == "kamyon":
            arac_sayisi_kamyon += 1
            ucret_toplam_kamyon += ucret_toplam
            sure_dakika_kamyon += arac_otoparkta_kaldigi_sure

        elif sinif_adi == "tır":
            arac_sayisi_tir += 1
            ucret_toplam_tir += ucret_toplam
            sure_dakika_tir += arac_otoparkta_kaldigi_sure

        # En Son İstenen Özel Veriler için Hesaplamalar

        if arac_sinifi_kodu == SINIF_KODU_BINEK and arac_agirligi < 1000:
            bir_tondan_hafif_binek_arac_sayisi += 1

        if (arac_sinifi_kodu == SINIF_KODU_OTOBUS or arac_sinifi_kodu == SINIF_KODU_KAMYON or arac_sinifi_kodu == SINIF_KODU_TIR) and arac_agirligi > 10000:
            on_tondan_agir_buyuk_arac_sayisi += 1

        if arac_otoparkta_kaldigi_sure < 30 and (arac_sinifi_kodu == SINIF_KODU_MOTORSIKLET or arac_sinifi_kodu == SINIF_KODU_BINEK):
            otuz_dakika_alti_arac += 1

        if arac_otoparkta_kaldigi_sure > 24 * 60 and (arac_sinifi_kodu == SINIF_KODU_OTOBUS or arac_sinifi_kodu == SINIF_KODU_MINIBUS):
            bir_gunden_fazla_otobus_minibus += 1

        if arac_otoparkta_kaldigi_sure > 30 * 24 * 60 or ucret_toplam > 1000:
            otuz_gunden_fazla_veya_bin_tlden_fazla_arac_sayisi += 1

        if en_uzun_kalan_aracin_suresi < arac_otoparkta_kaldigi_sure:
            en_uzun_kalan_aracin_suresi = arac_otoparkta_kaldigi_sure
            en_uzun_kalan_aracin_tutari = ucret_toplam

        # Döngü devamı için girdi alma
        print()
        arac_var = input("Başka araç var mı? (e/E/h/H): ")
        while not (arac_var == "e" or arac_var == "E" or arac_var == "H" or arac_var == "h"):
            arac_var = input("Başka araç var mı? (e/E/h/H): ")
    print()

    #  otoparkı kullanan toplam araç sayısı, her araç sınıfı için araç sayıları ve tüm araçlar içindeki oranları (%)
    print(f"Otoparktaki toplam araç sayısı: {arac_sayisi_toplam}")
    print(f"Motorsiklet sayısı: {arac_sayisi_motorsiklet}, Tüm araçlara oranı: %{arac_sayisi_motorsiklet * 100 / arac_sayisi_toplam: .2f}")
    print(f"Binek sayısı: {arac_sayisi_binek}, Tüm araçlara oranı: %{arac_sayisi_binek * 100 / arac_sayisi_toplam: .2f}")
    print(f"Minibus sayısı: {arac_sayisi_minibus}, Tüm araçlara oranı: %{arac_sayisi_minibus * 100 / arac_sayisi_toplam: .2f}")
    print(f"Otobüs sayısı: {arac_sayisi_otobus}, Tüm araçlara oranı: %{arac_sayisi_otobus * 100 / arac_sayisi_toplam: .2f}")
    print(f"Kamyon sayısı: {arac_sayisi_kamyon}, Tüm araçlara oranı: %{arac_sayisi_kamyon * 100 / arac_sayisi_toplam: .2f}")
    print(f"Tır sayısı: {arac_sayisi_tir}, Tüm araçlara oranı: %{arac_sayisi_tir * 100 / arac_sayisi_toplam: .2f}")
    print()

    #  otoparkın toplam geliri (TL), her araç sınıfı için toplam gelirler (TL) ve otoparkın toplam geliri içindeki oranları (%)
    print(f"Otoparkın toplam geliri: {round(ucret_toplam_tum_araclar,2)} TL")
    print(f"Motorsiklet geliri: {round(ucret_toplam_motorsiklet,2)}, Toplam gelire oranı: %{ucret_toplam_motorsiklet * 100 / ucret_toplam_tum_araclar: .2f}")
    print(f"Binek geliri: {round(ucret_toplam_binek,2)}, Toplam gelire oranı: %{ucret_toplam_binek * 100 / ucret_toplam_tum_araclar: .2f}")
    print(f"Minibus geliri: {round(ucret_toplam_minibus,2)}, Toplam gelire oranı: %{ucret_toplam_minibus * 100 / ucret_toplam_tum_araclar: .2f}")
    print(f"Otobüs geliri: {round(ucret_toplam_otobus,2)}, Toplam gelire oranı: %{ucret_toplam_otobus * 100 / ucret_toplam_tum_araclar: .2f}")
    print(f"Kamyon geliri: {round(ucret_toplam_kamyon,2)}, Toplam gelire oranı: %{ucret_toplam_kamyon * 100 / ucret_toplam_tum_araclar: .2f}")
    print(f"Tır geliri: {round(ucret_toplam_tir,2)}, Toplam gelire oranı: %{ucret_toplam_tir * 100 / ucret_toplam_tum_araclar: .2f}")
    print()

    #  her araç sınıfı için araç başına ortalama otoparkta kalma süresi (gün, saat, dakika) ve araç başına ortalama gelir (TL)
    print(f"Motorsiklet Park Süresi Ortalaması: {sure_hesaplama(sure_dakika_motorsiklet//arac_sayisi_motorsiklet, 'metin')}, Araç Başı Ortalama Gelir: {round(ucret_toplam_motorsiklet/arac_sayisi_motorsiklet,2)} TL")
    print(f"Binek Park Süresi Ortalaması: {sure_hesaplama(sure_dakika_binek//arac_sayisi_binek, 'metin')}, Araç Başı Ortalama Gelir: {round(ucret_toplam_binek/arac_sayisi_binek,2)} TL")
    print(f"Minibüs Park Süresi Ortalaması: {sure_hesaplama(sure_dakika_minibus//arac_sayisi_minibus, 'metin')}, Araç Başı Ortalama Gelir: {round(ucret_toplam_minibus/arac_sayisi_minibus,2)} TL")
    print(f"Otobüs Park Süresi Ortalaması: {sure_hesaplama(sure_dakika_otobus//arac_sayisi_otobus, 'metin')}, Araç Başı Ortalama Gelir: {round(ucret_toplam_otobus/arac_sayisi_otobus,2)} TL")
    print(f"Kamyon Park Süresi Ortalaması: {sure_hesaplama(sure_dakika_kamyon//arac_sayisi_kamyon, 'metin')}, Araç Başı Ortalama Gelir: {round(ucret_toplam_kamyon/arac_sayisi_kamyon,2)} TL")
    print(f"Tır Park Süresi Ortalaması: {sure_hesaplama(sure_dakika_tir//arac_sayisi_tir, 'metin')}, Araç Başı Ortalama Gelir: {round(ucret_toplam_tir/arac_sayisi_tir,2)} TL")
    print()

    # ağırlığı 1 tondan az olan binek araçların, tüm binek araçlar içindeki oranı (%)
    print(f"Ağırlığı 1 tondan az olan binek araç sayısının tüm binek araçlara oranı: %{bir_tondan_hafif_binek_arac_sayisi * 100 / arac_sayisi_binek: .2f}")

    # ağırlığı 10 tondan fazla olan otobüs, kamyon ve tır sınıfı araçların, tüm otobüs, kamyon ve tır sınıfı araçlar içindeki oranı (%)
    print(f"Ağırlığı 10 tondan fazla olan otobüs, kamyon ve tır sınıfı araçların, tüm otobüs, kamyon ve tır sınıfı araçlar içindeki oranı: %{on_tondan_agir_buyuk_arac_sayisi * 100 / (arac_sayisi_otobus + arac_sayisi_kamyon + arac_sayisi_tir):.2f}")

    # otoparkta 30 dakika veya daha kısa süre kalan motosiklet ve binek tipi araçların, tüm motosiklet ve binek tipi araçlar içindeki oranı (%)
    print(f"Otoparkta 30 dakika veya daha kısa süre kalan motosiklet ve binek tipi araçların, tüm motosiklet ve binek tipi araçlar içindeki oranı: %{otuz_dakika_alti_arac * 100 / (arac_sayisi_motorsiklet+arac_sayisi_binek): .2f}")

    # otoparkta 1 günden daha uzun süre kalan minibüs ve otobüs tipi araçların, tüm minibüs ve otobüs tipi araçlar içindeki oranı (%)
    print(f"Otoparkta 1 günden daha uzun süre kalan minibüs ve otobüs tipi araçların, tüm minibüs ve otobüs tipi araçlar içindeki oranı: %{bir_gunden_fazla_otobus_minibus * 100 / (arac_sayisi_otobus + arac_sayisi_minibus) :.2f}")

    # otoparkta 30 günden daha uzun süre kalan veya 1000 TL’den daha yüksek gelir edilen araçların, tüm araçlar içindeki oranı (%)
    print(f"Otoparkta 30 günden daha uzun süre kalan veya 1000 TL’den daha yüksek gelir edilen araçların, tüm araçlar içindeki oranı: %{otuz_gunden_fazla_veya_bin_tlden_fazla_arac_sayisi * 100 / arac_sayisi_toplam :.2f}")

    # sürücüsü gazi veya engelli olan araçların sayıları, tüm araçlar içindeki oranları (%) ve araç başına ortalama otoparkta kalma süreleri (gün, saat, dakika)
    print(f"Sürücüsü gazi olan araçların sayısı: {gazi_arac_sayisi}, tüm araçlar içindeki oranları: %{gazi_arac_sayisi * 100 / arac_sayisi_toplam:.2f}, araç başına ortalama park süresi: {sure_hesaplama(gazi_arac_park_suresi//(gazi_arac_sayisi), 'metin')}")
    print(f"Sürücüsü engelli olan araçların sayısı: {engelli_arac_sayisi}, tüm araçlar içindeki oranları: %{engelli_arac_sayisi * 100 / arac_sayisi_toplam:.2f}, araç başına ortalama park süresi: {sure_hesaplama(engelli_arac_park_suresi//engelli_arac_sayisi, 'metin')}")

    #  otoparkta 3 saatten daha uzun süre kalan indirim uygulanan araçların, tüm indirim uygulanan araçlar içindeki oranı (%)
    print(f"Otoparkta 3 saatten daha uzun süre kalan indirim uygulanan araçların, tüm indirim uygulanan araçlar içindeki oranı: %{indirimli_uc_saatten_cok_arac_sayisi * 100 / (engelli_arac_sayisi + gazi_arac_sayisi) :.2f}")

    # en uzun süre otoparkta kalan aracın otoparkta kaldığı süre (gün, saat, dakika) ve elde edilen gelir (TL)
    print(f"En uzun süre otoparkta kalan aracın otoparkta kaldığı süre: {sure_hesaplama(en_uzun_kalan_aracin_suresi,'metin')}, elde edilen gelir: {round(en_uzun_kalan_aracin_tutari,2)} TL")

    #en çok gelir elde edilen binek aracın otoparkta kaldığı süre (gün, saat, dakika) ve elde edilen gelir (TL)
    print(f"En çok gelir elde edilen binek aracın otoparkta kaldığı süre: {sure_hesaplama(en_masrafli_binek_aracin_suresi,'metin')}, elde edilen gelir: {round(en_masrafli_binek_aracin_ucreti,2)} TL")

main()