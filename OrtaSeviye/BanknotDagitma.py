# Girdi: tutar = 370, banknotlar = [200, 100, 50, 20, 10]

# Çıktı: 4

 

# -----------------------------------------------------
def minimum_banknot_sayisi(tutar, banknotlar):
    toplam_banknot = 0
    
    # Banknotlar listesini döngüyle büyükten küçüğe gez
    for banknot in banknotlar:
        if tutar == 0:
            break 
        # bir banknotttan (ör : 200) kaç tane vereceğimizi adet değişkenine atıyoruz
        adet = tutar// banknot 
        toplam_banknot+=adet

        #kalan tutarı güncelle 
        tutar = tutar % banknot
        
    return toplam_banknot

# Test Etmek İçin:
print(minimum_banknot_sayisi(400, [200, 100, 50, 20, 10]))


