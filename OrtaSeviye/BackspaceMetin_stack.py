# Örnek 1:
# Girdi: metin = "ab#c"
# Çıktı: "ac"
# (Açıklama: 'a' yazıldı, 'b' yazıldı, '#' ile son yazılan 'b' silindi, 'c' yazıldı. Ekranda "ac" kaldı.)

# Örnek 2:
# Girdi: metin = "ab##"
# Çıktı: "" (Boş Metin)
# (Açıklama: 'a' yazıldı, 'b' yazıldı, '#' ile 'b' silindi, '#' ile 'a' silindi. Ekran boş kaldı.)

# Örnek 3:
# Girdİ: metin = "a##c"
# Çıktı: "c"
# (Açıklama: 'a' yazıldı. İlk '#' ile 'a' silindi. 
#  İkinci '#' geldiğinde silinecek bir şey olmadığı için hiçbir şey olmadı. 
#  Sonra 'c' yazıldı. Ekranda "c" kaldı.)

def ekranda_kalan_metin(metin):

    stacklist = []
    for karakter in metin:

        if karakter == '#':
                if len(stacklist)>0:
                    stacklist.pop()


        else:
                stacklist.append(karakter)
    return "".join(stacklist)       
    
# Test Etmek İçin:
print(ekranda_kalan_metin("ab#c")) # "ac" dönmeli
print(ekranda_kalan_metin("ab##")) # "" (boş) dönmeli
print(ekranda_kalan_metin("a##c")) # "c" dönmeli

