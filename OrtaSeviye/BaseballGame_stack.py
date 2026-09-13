# ⚾ Soru: Tuhaf Bir Beyzbol Oyunu (Baseball Game)
# Garip kuralları olan bir beyzbol maçında skor tutuyorsun. 
# Sana maçtaki hamleleri sırasıyla gösteren bir islemler listesi veriliyor. 
# Listedeki her bir eleman bir kuralı (operasyonu) temsil eder.

# Kurallarımız şunlar:

# Sayı (Örn: "5", "-2"): Bu sayıyı yeni bir skor olarak kayda (stack'e) ekle. '
# '(Not: Gelen sayılar metin formatındadır, onları integer'a çevirmen gerekir).
# "+" (Artı İşareti): Kayıttaki son iki skoru topla ve yeni bir skor olarak kayda ekle.
# "D" (Double): Kayıttaki en son skorun 2 katını (çarpı 2) al ve yeni bir skor olarak kayda ekle.
# "C" (Cancel): Kayıttaki en son skorun geçersiz olduğunu anladık. Onu kayıttan tamamen sil.
# Görevin: Bütün işlemler bittiğinde, kayıttaki tüm skorların toplamını bulup döndürmek. (Eğer kayıt boşsa 0 döndür).
# (Not: Test senaryolarında her zaman +, D veya C işlemi için öncesinde yeterli sayıda skor olacağı garanti edilmiştir. 
#  Yani hata kontrolü yapmana gerek yok).

# Örnek 1:
# Girdi: islemler = ["5", "2", "C", "D", "+"]
# Çıktı: 30
# Açıklama:
# "5" -> Kayıt: [5]
# "2" -> Kayıt: [5, 2]
# "C" -> Son skoru sil. Kayıt: [5]
# "D" -> Son skorun 2 katı (5*2=10). Kayıt: [5, 10]
# "+" -> Son iki skoru topla (5+10=15). Kayıt: [5, 10, 15]
# Genel Toplam: 5 + 10 + 15 = 30



def toplam_skoru_hesapla(islemler):

    stacklist_kayit= []

    for islem in islemler:
        if  islem == 'C':
            stacklist_kayit.pop()
        elif islem == 'D':
            son_skor = stacklist_kayit[-1]
            stacklist_kayit.append(son_skor*2)
        elif islem == '+':
            son_skor =stacklist_kayit[-1]
            sondan_ikinci = stacklist_kayit[-2]
            stacklist_kayit.append(son_skor +sondan_ikinci)
        else:
            sayi = int(islem)
            stacklist_kayit.append(sayi)
    return sum (stacklist_kayit)        

# Test Etmek İçin:
print(toplam_skoru_hesapla(["5", "2", "C", "D", "+"])) # 30 dönmeli
print(toplam_skoru_hesapla(["5", "-2", "4", "C", "D", "9", "+", "+"])) # 27 dönmeli


