
TestList = [7,1,5,3,6,4]
#listedeki sayıları bir tane şirketin günlük  hisse senedi  fiyatı gibi düşün 
#listediki sayırlardan en büyük farkını bulacak olan kod (yani en büyük karı bulacaz )
# ama birine alış  birine satış dedik diye  satış günü alış  gününden önce olamaz
#---------------------------------------------

    #ZAMAN KARMAŞIKLIĞI DAHA İYİ OLAN YÖNTEM 

def en_yuksek_kari_bul(fiyatlar):
    # En düşük fiyatı başta çok büyük bir sayı yapalım ki ilk gelen fiyat onu hemen güncellesin
    en_dusuk_fiyat = float('inf') # infinity den gelmekte 
    maksimum_kar = 0

    for i in  range(0,len(fiyatlar)):
        if fiyatlar[i]<en_dusuk_fiyat:
            en_dusuk_fiyat=fiyatlar[i]
        else:
            potansiyel_kar = fiyatlar[i]-en_dusuk_fiyat
            if potansiyel_kar >maksimum_kar:
                maksimum_kar= potansiyel_kar        
    return maksimum_kar

# Test etmek için:
print(en_yuksek_kari_bul(TestList))

#iterasyon durumunu adım adım yazalım 

# i = 0  , en_dusuk_fiyat = 7 
# i = 1  , en_dusuk_fiyat = 1
# i = 2  , en_dusuk_fiyat = 1 ,  maksimum_kar = 4

# i = 3  , en_dusuk_fiyat = 1 ,  maksimum_kar = 4
# i = 4  , en_dusuk_fiyat = 1 ,  maksimum_kar = 5 
# i = 5  , en_dusuk_fiyat = 1 ,  maksimum_kar = 5

#--------------------------------------------------------------
 
   # FARKLI  BİR YÖNTEM 

# İç İçe Döngü (Brute Force) Yöntemi
# Bu yöntem her alış günü için olası tüm satış günlerini tek tek dener. 
# Küçük listelerde çalışır ama veri büyüdükçe çok yavaşlar (Zaman karmaşıklığı: $O(n^2)$).
def kaba_kuvvet_kar(fiyatlar):
    maks_kar = 0
    
    # i alış gününü temsil eder
    for i in range(len(fiyatlar)):
        
        # j satış gününü temsil eder (alıştan sonra başlar)
        for j in range(i + 1, len(fiyatlar)):
            kar = fiyatlar[j] - fiyatlar[i]
            
            # Yeni kar eskisinden büyükse güncelle
            if kar > maks_kar:
                maks_kar = kar
                
    return maks_kar

print(kaba_kuvvet_kar(TestList))

#dizimiz şurda dursun  = [7,1,5,3,6,4]
#iterasyon durumunu adım adım yazalım daha iyi anlamak için

# i = 0 , j = 1  ,kar = -6 ,     i = 1 , j = 2 ,kar = 4 , maks_kar = 4     
# i = 0 , j = 2  ,kar = -2 ,     i = 1 , j = 3 ,kar = 2 , maks_kar = 4 
# i = 0 , j = 3  ,kar = -4 ,     i = 1 , j = 4 ,kar = 5 , maks_kar = 5
# i = 0 , j = 4  ,kar = -1 ,     i = 1 , j = 5 ,kar = 3 , maks_kar = 5
# i = 0 , j = 5  ,kar = -3 , 

# bu şekilde  i = 2  , i = 3 , i = 4  olacak şekilde iterasyonlar devam eder 
# ve en büyük farkı bulmuş olur o da 5 tir 

# diziye bakınca en büyük fark 6 gibi ama ne dedik : 
# satış , alıiştan sonra olur.. (sonrakini öncekinden çıkaracağız)
# j degiskenini bir fazla başlatarak ,
# hem sonrakini öncekinden çıkarmış olduk (tabiki  döngü içindeki kodlarda j - i olmak zorunda )
#  hem  gereksiz yere ilk iterasyonun ilk işleminde  aynı iki sayıyı birbirinden çıkarmadık  