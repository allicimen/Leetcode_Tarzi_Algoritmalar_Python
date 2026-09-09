def en_uzun_kelimeyi_bul(metin):
    # 1. Metni .split() ile kelimelerine ayırıp bir listeye kaydet
    Liste = metin.split()
    # 2. Döngüde karşılaştırma yapabilmek için başlangıç değerleri tanımla
    en_uzun_kelime = ""
    maks_uzunluk = 0
    
    # 3. Listedeki her bir kelime için for döngüsü kur
    for i in range (0,len(Liste)):
        if len(Liste[i]) > maks_uzunluk:
            maks_uzunluk = len(Liste[i])
            en_uzun_kelime = Liste[i]
        
            
    # Döngü bitince en uzun kelimeyi döndür
    return en_uzun_kelime

# Test etmek için:
metin = "kahve dadkjabdnjakdhbaj atmosferi harikaydı"
print(en_uzun_kelimeyi_bul(metin))

#------------------------------------------------------------------------------------------------------------------

# 💡 Pythonic (Daha Kısa) Yol
# Python'da listeleri gezerken range() ve indeks (i) kullanmak zorunda değilsin.
# Öğeleri doğrudan bir değişkene atayarak döngüyü çok daha okunabilir hale getirebilirsin. 
# Buna "Pythonic" yazım denir:
def en_uzun_kelimeyi_bul_kisa(metin):
    Liste = metin.split()
    en_uzun = ""
    maks_uzunluk = 0
    
    # İndeksle uğraşma, kelimeleri doğrudan al!
    for kelime in Liste:
        if len(kelime) > maks_uzunluk:
            maks_uzunluk = len(kelime)
            en_uzun = kelime
            
    return en_uzun