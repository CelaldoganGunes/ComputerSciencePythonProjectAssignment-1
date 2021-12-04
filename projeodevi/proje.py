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

def sinif_kodundan_arac_sinifini_ogren(sinif_kodu):
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

def sure_hesaplama(dakika):
    saat = dakika//60
    artik_dakika = dakika % 60
    gun = saat//24
    artik_saat = saat % 24
    return gun, artik_saat, artik_dakika

def main():
    arac_var = "e"

    while arac_var == "e":

        #region INPUT

        arac_plakasi = input("Plakayı girin: ")
        arac_sinifi_kodu = int(input("Araç sınıfı kodunu girin [1-6]: "))

        while not arac_sinifi_kodu in range(1, 7):
            arac_sinifi_kodu = int(input("Araç sınıfı kodunu girin [1-6]: "))

        arac_agirligi = float(input("Araç ağırlığını kg cinsinden girin: "))

        while arac_agirligi <= 0:
            arac_agirligi = float(input("Araç ağırlığını kg cinsinden girin: "))

        arac_otoparkta_kaldigi_sure = int(input("Aracın otoparkta kaç dakika kaldığını yazın:"))

        while arac_otoparkta_kaldigi_sure <= 0:
            arac_otoparkta_kaldigi_sure = int(input("Aracın otoparkta kaç dakika kaldığını yazın:"))

        surucu_ad_soyad = input("Sürücünün adını ve soyadını girin:")

        ozel_durum = "y"
        if arac_sinifi_kodu == 1 or arac_sinifi_kodu == 2:
            ozel_durum = input("(Varsa) Sürücünün özel durumunu girin:")
            while not (ozel_durum == "y" or ozel_durum == "Y" or ozel_durum == "G" or ozel_durum == "g" or ozel_durum == "E" or ozel_durum == "e"):
                ozel_durum = input("(Varsa) Sürücünün özel durumunu girin:")

        #endregion

        #region PRINT

        print(f"Aracın plakası: {arac_plakasi}")

        sinif_adi, sinif_katsayi = sinif_kodundan_arac_sinifini_ogren(arac_sinifi_kodu)
        print(f"Aracın sınıfı: {sinif_adi}")
        print(f"Aracın ağırlığı: {arac_agirligi:.2f} KG")
        dd, hh, mm = sure_hesaplama(arac_otoparkta_kaldigi_sure)
        print(f"Aracın otoparkta kaldığı süre: {dd} gün {hh} saat {mm} dakika")



        print(f"Sürücünün adı ve soyadı: {surucu_ad_soyad}")
        if ozel_durum == "g" or ozel_durum == "E" or ozel_durum == "e":
            print(f"Sürücünün özel durumu:{ozel_durum}")
            if ozel_durum == "g" or ozel_durum == "G":
                print(f"Gazi indirim oranı: {INDIRIM_ORANI_GAZI}")
            else:
                print(f"Engelli indirim oranı:{INDIRIM_ORANI_ENGELLI}")



        ucret_gun = dd * SURE_HER_YIRMIDORT_SAAT
        if hh < 1:
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
        toplam_ucret = ucret_giris + ucret_sure

        print(f"Otopark ücreti: {toplam_ucret}")
        #endregion

main()