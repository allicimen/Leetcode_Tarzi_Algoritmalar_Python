def hedefi_bulan_indeksler(sayilar, hedef):


    for i in range (0,len(sayilar)): #i nin değeri range  içinden gelmekte 

        for j in  range(i+1,len(sayilar)):  # j nin değeri  range içinden gelmekte

            if  sayilar[i]+sayilar[j] == hedef:
                return [i,j]


sayilar = [2,7,11,15]
print(hedefi_bulan_indeksler(sayilar,13))


#iterasyon durumu
# i = 0 , j = 1     i = 1 , j = 2    i= 2 , j = 3 
# i = 0 , j = 2     i = 1 , j = 3 
# i = 0 , j = 3