def eksik_sayiyi_bul(sayilar):
    n = len(sayilar)

    beklenen_toplam = n*(n+1)//2
    eksik_toplam = sum(sayilar)

    

    return beklenen_toplam-eksik_toplam

#test

liste= [0,1,2,4]

print(eksik_sayiyi_bul(liste))