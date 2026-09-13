#  Soru: İkili Arama (Binary Search)
# Sana küçükten büyüğe doğru sıralanmış (sorted) bir sayilar listesi ve bulman gereken bir hedef sayı veriliyor.
# Görevin; bu hedef sayının liste içindeki indeksini (konumunu) bulmak.
# Eğer sayı listede varsa, o sayının indeksini döndür.
# Eğer sayı listede yoksa, -1 döndür.
# Kritik Kural: Mülakatçı senden bu soruyu O(log n) zaman karmaşıklığında çözmeni istiyor.
# Yani listeyi baştan sona for döngüsü ile tek tek gezmek (O(n)) kesinlikle yasak! Ortadan bölme mantığını kullanmalısın.
    
# Örnek 1:
# Girdi: sayilar = [-1, 0, 3, 5, 9, 12], hedef = 9
# Çıktı: 4
# (Açıklama: 9 sayısı listede var ve 4. indekste yer alıyor.)

# Örnek 2:
# Girdi: sayilar = [-1, 0, 3, 5, 9, 12], hedef = 2
# Çıktı: -1
# (Açıklama: 2 sayısı listede bulunmuyor, bu yüzden -1 döndürüyoruz.)

def ikili_arama(sayilar, hedef):

    sol = 0
    sag = len(sayilar)-1  #5

    #sol ve sağ üst üste gelene kadar  devam et 
    while sol<=sag:

        orta = (sol+sag)//2 #2

        if sayilar[orta]== hedef: 
            return orta
        elif sayilar [orta]< hedef:
            sol = orta +1 
        elif sayilar[orta]> hedef:
            sag = orta -1
    #döngü bitti ama sayi bulunamadıysa 
    return - 1
# Test Etmek İçin:
print(ikili_arama([-1, 0, 3, 5, 9, 12], 9)) # 4 dönmeli
print(ikili_arama([-1, 0, 3, 5, 9, 12], 2)) # -1 dönmeli


