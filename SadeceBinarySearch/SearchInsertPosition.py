# Soru: Araya Ekleme Konumu (Search Insert Position)
# Sana küçükten büyüğe doğru sıralanmış, 
# içinde birbirinin aynısı (tekrar eden) sayı bulunmayan bir sayilar listesi ve bir hedef sayı veriliyor.

# Görevin:
# Eğer hedef sayı listede varsa, onun indeksini döndür.
# Eğer hedef sayı listede yoksa, sıralamayı bozmayacak şekilde listeye eklenseydi hangi indekste olması gerektiğini bul ve o indeksi döndür.
# Kritik Kural: Mülakatçı bu soruyu da O(log n) zaman karmaşıklığında çözmeni bekliyor
# (Yani for döngüsü kullanmak yasak, ortadan bölme mantığıyla ilerlemelisin).

# Örnek 1:
# Girdi: sayilar = [1, 3, 5, 6], hedef = 5
# Çıktı: 2
# (Açıklama: 5 sayısı listede var ve 2. indekste yer alıyor.)

# Örnek 2:
# Girdi: sayilar = [1, 3, 5, 6], hedef = 2
# Çıktı: 1
# (Açıklama: 2 sayısı listede yok. Eğer eklenseydi 1 ile 3'ün arasına girerdi, yani yeni indeksi 1 olurdu.)

# Örnek 3:
# Girdi: sayilar = [1, 3, 5, 6], hedef = 7
# Çıktı: 4
# (Açıklama: 7 listede yok. Eklenseydi en sona (6'nın sağına) gelirdi. Mevcut son indeks 3 olduğu için 7'nin indeksi 4 olurdu.)

def yerini_bul(sayilar, hedef):

        sol = 0
        sag = len(sayilar)-1  #3
    
        #sol ve sağ üst üste gelene kadar  devam et 
        while sol<=sag:
    
            orta = (sol+sag)//2 #1
    
            if sayilar[orta]== hedef: 
                return orta
            elif sayilar [orta]< hedef:
                sol = orta +1 
            elif sayilar[orta]> hedef:
                sag = orta -1
        # Döngü bitti ve sayı bulunamadıysa, 
        # 'sol' işaretçisi tam olarak sayının eklenmesi gereken yerde kalır!
        # sag =>  sol olunca while dan çıkacak return a girecek
        return sol
                 
# Test Etmek İçin:
print(yerini_bul([1, 3, 5, 6], 5)) # 2 dönmeli
print(yerini_bul([1, 3, 5, 6], 2)) # 1 dönmeli
print(yerini_bul([1, 3, 5, 6], 7)) # 4 dönmeli
