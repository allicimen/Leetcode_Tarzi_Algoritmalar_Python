# Girdi: metin = "abbaca"
# Çıktı: "ca"
# (Açıklama: Önce yanyana duran "bb" harflerini sileriz. Geriye "aaca" kalır. 
#  Şimdi "aa" harfleri yanyana geldiği için onları da sileriz. Geriye sadece "ca" kalır.)

# Örnek 2:
# Girdi: metin = "azxxzy"
# Çıktı: "ay"
# (Açıklama: "xx" silinir -> "azzy" kalır. Yeni oluşan "zz" silinir -> Geriye "ay" kalır.)

def yanyana_harfleri_sil(metin):

    stack = []

    for karakter in metin :
         
            if len(stack) > 0 and stack[-1] == karakter:
                stack.pop()


        #stackte değilse ekle 
            else :
                stack.append(karakter)

    # Stack'in içinde kalan harfleri string (metin) olarak birleştirip döndür
    return "".join(stack)

# Test Etmek İçin:
print(yanyana_harfleri_sil("abbaca")) # "ca" dönmeli
print(yanyana_harfleri_sil("azxxzy")) # "ay" dönmeli

#string metini for da döneriz no problem
# sözlük kullanmaya  gerek var mı yok gibi 
#ama stack kullanmalıyız  çünkü stack.pop yapacaz

# Aslında `stack.pop()` sadece **bir** karakteri (içeride bekleyeni) siliyor.

# Yeni gelen aynı harfi de yığına (`append` ile) **hiç eklemediğimiz** için; biri içeriden çöpe atılıyor, diğeri içeri hiç alınmıyor. 
# Böylece ikisi birden yok olmuş (patlamış) oluyor! 💥