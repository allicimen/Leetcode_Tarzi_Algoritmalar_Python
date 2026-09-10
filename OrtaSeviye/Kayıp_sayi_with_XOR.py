def eksik_sayiyi_bul_xor(sayilar):
    sonuc = 0
    n = len(sayilar)

    # 1. BİZDE OLAN sayıları kasaya atıp XOR'la
    for sayi in sayilar:
         sonuc = sonuc ^ sayi 
        # sonuç değişkenine XOR işlemini üst üste atabilirsin no problem...(kasa lafını ezberle şimdilik)
        
    # 2. OLMASI GEREKEN tüm sayıları kasaya atıp XOR'la
    for i in range(n + 1):  # n dahil olsun diye +1 dedik
        sonuc = sonuc ^ i 
        
    # Kasada sadece yalnız (eksik) sayı kalacak!
    return sonuc

# Test Etmek İçin:
print(eksik_sayiyi_bul_xor([3, 0, 1]))