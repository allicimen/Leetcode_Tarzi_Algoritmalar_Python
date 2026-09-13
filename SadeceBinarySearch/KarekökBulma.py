#  Soru: Karekök Bulma (Sqrt(x))
# Sana negatif olmayan bir x tam sayısı veriliyor. 
# Görevin, bu x sayısının karekökünü bulmak ve tam sayı (integer) olarak döndürmektir.
# Eğer sayının karekökü küsuratlı çıkıyorsa (örneğin 2.82...), 
# sadece tam sayı kısmını almalı ve küsuratı atmalısın (yani 2 döndürmelisin).
# Kritik Kural:
# Mülakatçı senden bu işlemi O(log n) hızında yapmanı istiyor. Bu yüzden:
# math.sqrt() gibi hazır matematik kütüphanelerini kullanmak YASAK
# x ** 0.5 gibi üs alma işlemleri YASAK.
# Birden başlayıp x'e kadar for döngüsü ile sayıları tek tek kendisiyle çarparak denemek (Brute Force) YASAK.
# İpucu: Elinde 1'den x'e kadar giden "sıralı" bir sayı listesi varmış gibi düşün.

# Örnek 1:
# Girdi: x = 4
# Çıktı: 2
# (Açıklama: 2 * 2 = 4 olduğu için karekök 2'dir.)

# Örnek 2:
# Girdi: x = 8
# Çıktı: 2
# (Açıklama: 8'in karekökü 2.82842... şeklindedir. Küsuratı attığımızda geriye 2 kalır.)

# Örnek 3:
# Girdi: x = 1
# Çıktı: 1

def karekok_bul(x):

    if  x == 1 or x == 0 :
        return x

    sol = 1
    sag = x 

    while sol<=sag:
        orta = (sol+sag)//2
        kare = orta*orta

        if kare == x:
            return orta
        elif kare> x:
            sag = orta-1
        elif kare<x:
            sol=orta+1
    return sag  # x=8 in gidişatını yazınca neden return a sag koydugumuz ortaya çıkıyor



# Test Etmek İçin:
print(karekok_bul(4)) # 2 dönmeli
print(karekok_bul(8)) # 2 dönmeli
print(karekok_bul(100)) # 1 dönmeli