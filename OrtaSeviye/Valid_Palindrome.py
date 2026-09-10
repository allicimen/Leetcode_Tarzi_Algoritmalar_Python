
# palindrom kontrolü olan kod  yazacağız
# palindrom : baştan  ve sondan okunuşu aynı olan kelimeler

def palindrom_mu(kelime):
    # 1. İşaretçileri (pointer) başlat
    sol = 0
    sag = len(kelime) - 1 # 1 çıkardık   çünkü indeksi atayacağız (len , 1'den başlar.indeks , 0'dan)
    
    # 2. İşaretçiler ortada çarpışana kadar döngüyü çalıştır
    while sol < sag:
        
        # 3. Eğer sol ve sağdaki harfler EŞİT DEĞİLSE (!=):
        if kelime[sol] != kelime[sag]:
            # False döndür ve bitir
            return False
        # 4. Eğer eşitse, işaretçileri birer adım ortaya yaklaştır
        else:
            # sol'u artır, sag'ı azalt
            sol+=1
            sag-=1
    # Döngü hiç False dönmeden bittiyse, kelime palindromdur
    return True

# Test Etmek İçin:
print(palindrom_mu("radar"))
print(palindrom_mu("kalem"))