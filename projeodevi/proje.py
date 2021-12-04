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

arac_var = "e"

while arac_var == "e":

    #region INPUT

    arac_plakasi = input("Plakayı girin: ")
    arac_sinifi_kodu = int(input("Araç sınıfı kodunu girin [1-6]: "))

    while arac_sinifi_kodu in range(1,7):
        arac_sinifi_kodu = int(input("Araç sınıfı kodunu girin [1-6]: "))

    arac_agirligi = float(input("Araç ağırlığını kg cinsinden girin: "))

    while arac_agirligi <= 0:
        arac_agirligi = float(input("Araç ağırlığını kg cinsinden girin: "))

    arac_otoparkta_kaldigi_sure = int(input("Aracın otoparkta kaç dakika kaldığını yazın:"))

    while arac_otoparkta_kaldigi_sure <= 0:
        arac_otoparkta_kaldigi_sure = int(input("Aracın otoparkta kaç dakika kaldığını yazın:"))

    surucu_ad_soyad = input("Sürücünün adını ve soyadını girin:")

    if arac_sinifi_kodu == 1 or arac_sinifi_kodu == 2:
        ozel_durum = input("(Varsa) Sürücünün özel durumunu girin:")
        while not (ozel_durum == "y" or ozel_durum == "Y" or ozel_durum == "G" or ozel_durum == "g" or ozel_durum == "E" or ozel_durum == "e"):
            ozel_durum = input("(Varsa) Sürücünün özel durumunu girin:")

    #endregion



