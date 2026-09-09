def anagram_mi(metin1, metin2):
    # 1. Uzunluklar eşit değilse hemen False dön
    if len(metin1) != len(metin2):
        return False
        
    # 2. İki boş sözlük oluştur
    frekans1 = {}
    frekans2 = {}
    
    # 3. İlk metnin harflerini say (Önceki soruda kurduğun mantığın aynısı)
    for harf in metin1:
        if harf in frekans1:
            frekans1[harf] +=1
        else:
            frekans1[harf] = 1
        
        
    # 4. İkinci metnin harflerini say
    for harf in metin2:
        if harf in frekans2:
            frekans2[harf] +=1
        else:
            frekans2[harf] = 1

    
        
    # 5. İki sözlük birbiriyle tamamen aynı mı diye kontrol et ve döndür
    return frekans1 == frekans2

metin1 = "elmam"
metin2 = "alem"
print(anagram_mi(metin1,metin2))

