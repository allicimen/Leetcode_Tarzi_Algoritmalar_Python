# kanka  burada  yine bir listedeki  yalnız sayiyi bulacağız

# ama bu sefer XOR kullanacağız :

#      XOR NEDİR ?

# Bilgisayar bilimlerinde Bitwise XOR (Dışlayan Veya) adında, Python'da ^ işareti ile kullanılan özel bir operatör vardır. 
# Bu operatörün algoritma sorularında hayat kurtaran iki altın kuralı bulunur:

# Aynı iki sayı XOR'lanırsa sonuç SIFIR olur: A ^ A = 0 (Sayılar birbirini yok eder).

# Bir sayı SIFIR ile XOR'lanırsa sonuç KENDİSİ olur: A ^ 0 = A.

# Mantık Nasıl İşliyor?

# Listemiz [4, 1, 2, 1, 2] olsun. Bütün sayıları sırayla birbirleriyle XOR'larsak ne olur biliyor musun?
# İşlemin sırası hiç önemli değildir, arka planda şu gerçekleşir:

# 4 ^ 1 ^ 2 ^ 1 ^ 2
# (Aynı olanlar birbiriyle eşleşip 0'a dönüşür)
# = (1 ^ 1) ^ (2 ^ 2) ^ 4
# = 0 ^ 0 ^ 4
# = 4
#-------------------------------------------------------------------------------
def yalniz_sayiyi_bul_xor(sayilar):
    sonuc = 0
    
    for sayi in sayilar:
        sonuc ^= sayi  # Bu ifade şunun kısaltmasıdır: sonuc = sonuc ^ sayi
        
    return sonuc

# Test İçin:
print(yalniz_sayiyi_bul_xor([4, 1, 2, 1, 2])) 
# Çıktı: 4