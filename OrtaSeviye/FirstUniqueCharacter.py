
#bir kelimedeki ilk tekrar etmeyen harfi  bulacağız 
#-------------------------------------------------------------
def ilk_tekil_harfi_bul(metin):
    harf_sayilari = {}
    
    # 1. Aşama: Harfleri sözlüğe kaydet ve say
    #burda dönen şey key
    # yani harf degiskeni sırasıy a ,k falan almakta 
    #  ama diğer for döngüsünde  len(metin) yazınca dönen şey int
    for harf in metin:
        if harf in harf_sayilari:
            harf_sayilari[harf] += 1  # Varsa 1 artır
        else:
            harf_sayilari[harf] = 1   # Yoksa 1 olarak ekle
            
    # 2. Aşama: Metni tekrar gez ve değeri 1 olanı bul
    for i in range(len(metin)):
        if harf_sayilari[metin[i]] == 1:
            return i  # Bulduğumuz ilk tekil harfin indeksini döndür
            
    return -1  # Hepsi tekrar ediyorsa -1 dön

#--------------------------------------------------

metin = "akademi"
print (ilk_tekil_harfi_bul(metin))

# adım adım iterasyonları yazıp  kodun çalışma  mantığını anlayalım 
# harf  değişkeni sırasıyla : 'a' ,'k' ,'a' ,'d' ,'e','m','i'  olur (bu sefer ideksler sayı değil key dir)

#  a harfi  yok  {'a' : 1}  olur ,
#  k harfi  yok  {'k' : 1}  olur , 
#  a harfi  var  {'a' : 2}  olur, 
#  d harfi  yok  {'d' : 1}  olur , 
#  e harfi  yok  {'e' : 1}  olur , 
#  m harfi  yok  {'m' : 1}  olur ,
#  i harfi  yok  {'i' : 1}  olur ,  

#  SON DURUMDA ŞU OLUR :

# harf_sayilari =  

#   {
#      'a':2, 
#      'k':1,
#      'd':1,
#      'e':1,
#      'm':1,
#      'i':1
#   }
 

