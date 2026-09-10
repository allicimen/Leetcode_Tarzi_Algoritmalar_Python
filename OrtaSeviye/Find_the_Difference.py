def araya_sizan_harfi_bul(orijinal, bozulmus):

   kelime = orijinal + bozulmus
   sonuc = 0 

   for harf in kelime:
        sayi = ord(harf)
        sonuc= sonuc^sayi
        
   return chr(sonuc)
    
# Test Etmek İçin:
print(araya_sizan_harfi_bul("kredi", "dikrek"))