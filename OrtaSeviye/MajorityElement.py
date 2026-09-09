
# bir sayı listesinde  en çok tekrar eden sayıyı  döndüreceğiz
# yani frekansı en yüksek olanı bulup geri döndüreceğiz
# ----------------------------------------------
def en_cok_tekrar_edeni_bul(sayilar):
    frekanslar = {}  #dictionary tanimlamasi

    for sayi in sayilar:
        if sayi in frekanslar:
            frekanslar[sayi] +=1
        else :
            frekanslar[sayi]  =1 


    en_cok_gecen_sayi = 0 
    en_cok_gecen_frekans = 0 

    for sayi in frekanslar:

        if frekanslar[sayi] > en_cok_gecen_frekans:
            en_cok_gecen_frekans = frekanslar[sayi]
            en_cok_gecen_sayi = sayi 
    

    return en_cok_gecen_sayi, en_cok_gecen_frekans 

#-------------------------------------
# 

SayiListesi = [2,2,1,1,2,2]
print(en_cok_tekrar_edeni_bul(SayiListesi))   