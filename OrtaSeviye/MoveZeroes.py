
# elimize  bir liste  verilecek ...

# biz bu  listedeki  sıfırları sona  taşıyacağız
#----------------------------------------------------------------
def sifirlari_sona_tasi(sayilar):
    hedef_indeks = 0  # 0 olmayanları koyacağımız yer
    
    # Listeyi indeksleriyle gez
    for i in range(len(sayilar)):
        
        # Eğer sayilar[i] sıfıra eşit DEĞİLSE (!=) :
        if sayilar [i] != 0:
            
            # sayilar[i] ile sayilar[hedef_indeks] elemanlarını takas et
            sayilar[i], sayilar[hedef_indeks] =  sayilar[hedef_indeks], sayilar[i]
            
            # hedef_indeks değerini 1 artır
            hedef_indeks+=1
            
    return sayilar

# Test Etmek İçin:
print(sifirlari_sona_tasi([0, 1, 0, 3, 12]))

#-------------------------
# iterasyon durumlarını yazalım . 


# i = 0 ,  hedef_indeks = 0 
# i = 1 ,  hedef_indeks = 1  ,  swat işlemi olur... dizi = 1,0,0,3,12 olur
# i = 2 ,  hedef_indeks = 1  ,  swat  yok 
# i = 3 ,  hedef_indeks = 2  ,  swat işlemi olur... dizi = 1,3,0,0,12 olur
# i = 4 ,  hedef_indeks = 3  ,  swat işlemi olur....dizi = 1,3,12,0,0 olur

