

def en_uzun_seriyi_bul(gunler):
    guncel_seri = 0
    en_uzun_seri = 0

    for i in range(0,len(gunler)): # i degiskeni 0,1,2,3,4,5,6,7 degerlerini alır

        if gunler[i] == 1:
            guncel_seri = guncel_seri +1
            if guncel_seri>en_uzun_seri:
                en_uzun_seri = guncel_seri
        else:
            guncel_seri=0    
    
  
    return en_uzun_seri


gunler = [1, 1, 0, 1, 1, 1, 0, 1] #aliskanligin yapıldigi günler 1 yapılmamışsa 0 diye yazılmış
print(en_uzun_seriyi_bul(gunler))
print(len(gunler))

#iterasyon durumu

# i = 0 , guncel_seri = 1 , en_uzun_seri = 1 
# i = 1 , guncel_seri = 2 , en_uzun_seri = 2 
# i = 2 , guncel_seri = 0 , en_uzun_seri = 2
# i = 3 , guncel_seri = 1 , en_uzun_seri = 2 
# i = 4 , guncel_seri = 2 , en_uzun_seri = 2
# i = 5 , guncel_seri = 3 , en_uzun_seri = 3
# i = 6 , guncel_seri = 0 , en_uzun_seri = 3 
# i = 7 , guncel_seri = 1 , en_uzun_seri = 3 