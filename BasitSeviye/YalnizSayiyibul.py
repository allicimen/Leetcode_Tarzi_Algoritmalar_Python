

#bir tane sayi listesi var 
# bu sayi listesinde eşi olmayan sayiyi  bulmaya çalişacağiz


# Örnek Durumlar:
# Girdi: sayilar = [2, 2, 1]

# Çıktı: 1

# Girdi: sayilar = [4, 1, 2, 1, 2]

# Çıktı: 4
#----------------------------------------------

def yalniz_sayiyi_bul(sayilar):

    sayacDictionary = {}

    for sayi in sayilar:
        if sayi in sayacDictionary:  #eğer 4 sözlüğün (sayacDictionary) içinde varsa
            sayacDictionary[sayi]+=1 # değeri 1 arttır
        else:# eğer yoksa ekle 
            sayacDictionary[sayi] = 1

    #.items()  kullanarak sözlüğü döngüde kullanabiliriz
    for sayi ,miktar in sayacDictionary.items():  
        if miktar==1:
            return sayi

# Test için
print(yalniz_sayiyi_bul([2, 1, 9, 1, 2]))


# 1 .deneme yolum :
# # for döngüsü içinde if olacak 
# # 0. indeksi al sırayla  kontrol et eşi varsa bitir
# #olmaz çünkü  diğer elemanlarda eşi olabilir ilk iterasyonda  bitirebilir 

# yoksa ekrana ver 

# 2.deneme yolum :
# sol sağ işaretçi...  tanimla ama bu da olmaz


# 3. deneme yolum:
# bize her sayıdan kaç tane olduğunu tutan bir  liste ya da dictonary lazım:
# for ile  dön sayac koy.. 

