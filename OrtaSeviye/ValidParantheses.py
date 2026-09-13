#  Soru: Geçerli Parantezler (Valid Parentheses)
# Sana sadece şu karakterlerden oluşan bir metin veriliyor: '(', ')', '{', '}', '[' ve ']'.
# Bu metnin "geçerli" (valid) olup olmadığını bulmanı sağlayan bir algoritma yazmalısın.
# Geçerlilik Kuralları:
# Açılan her parantez, aynı türden bir parantez ile kapatılmalıdır.
# Açılan parantezler, doğru sırayla kapatılmalıdır. (Yani en son açılan, ilk kapatılmalıdır).
# Örnek Durumları
# Girdi: metin = "()"
# Çıktı: True
# Girdi: metin = "()[]{}"
# Çıktı: True
# Girdi: metin = "(]"
# Çıktı: False (Türler uyuşmuyor)
# Girdi: metin = "([)]"
# Çıktı: False (Sıra bozuk: köşeli kapanmadan normal parantez kapanmış)
# Girdi: metin = "{[]}"
# Çıktı: True (Doğru sıra: Önce köşeli kapandı, sonra süslü)

#-------------------------------------------
def gecerli_parantezler(metin):
    Stack = [] #açık parantezleri buraya koyacağız

    dictionary = {
        ')': '(',
        '}': '{',
        ']': '['
    }
  
    for karakter in metin:
        #önce kapalı parantezi  yapmaktayız 
        if karakter in dictionary: 
            if len(Stack) ==0 or Stack.pop() != dictionary [karakter]:
                return False
        #şimdi de açık parantez     
        else:
            Stack.append(karakter)

    # Bütün metin bittiğinde yığın tamamen boşalmış olmalı. 
    # Boşsa True (Herkes eşini buldu), doluysa False (Açıkta kalan var).
    return len(Stack) == 0

# Test Etmek İçin:
print(gecerli_parantezler("([{}])")) # True dönmeli

#şimdi şöyle yapacaz 
# stack kullanmak normal liste tanımlamakla aynıdır
#son giren ilk çıkar tam olarak parantez mantığına  uygun zaten
#sözlük tanımlayacağız key = açık parantez olacak 
# value =  kapalı  parantez olacak
# açık parantez gelirse boş olan yığına ekleyeceğiz
#kapalı gelirse stack.pop yapacaksın ama eşit mi kontrolü de yapacaz