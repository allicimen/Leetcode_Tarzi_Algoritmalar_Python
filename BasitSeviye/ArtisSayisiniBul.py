# def artis_sayisini_bul(satislar):
#     # Artış sayısını tutacağın bir sayaç değişkeni
#     artis_sayaci = 0

#     satislar = [10,15,12,18,20]

#     for i in satislar:
    
#         if satislar [i] > satislar [i+1]:

#             artis_sayaci+1

#         else:
#             artis_sayaci = 0    
                
#     # En son toplam sayıyı geri döndür
#     return print artis_sayaci

#----------------------------------------------------------------------------
#DOĞRUSU



def artis_sayisini_bul(satislar):
    artis_sayaci = 0
    

    # 1. indeksten başlayarak listenin sonuna kadar git (0. indeksi atlıyoruz)
    for i in range(1, len(satislar)): # i nin değerini range in içinden gelmekte... len 5  bu yüzden i değiskeni sırasıyla 1, 2,3,4 olur
        
        # O anki gün (i), bir önceki günden (i-1) büyük mü?
        if satislar[i] > satislar[i-1]:
            artis_sayaci += 1  # Evetse sayacı 1 artır ve kaydet
            
    # Döngü bitince toplam sonucu geri ver
    return artis_sayaci



satislar = [10, 15, 12, 18, 20]  #len yapınca sonuc 5 cikar...  
print (artis_sayisini_bul(satislar))


#iterasyon durumu  (unutmak istemediğim kritik değişkenleri  not alıyorum)

# i = 1 , artis_sayaci = 1 
# i = 2 , artis_sayaci = 1 (değismedi) 
# i = 3 ,  artis_sayaci = 2 
# i = 4 , artis_sayaci = 3 
