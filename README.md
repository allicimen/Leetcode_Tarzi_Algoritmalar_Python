#  Python Algorithm & Problem Solving Practice (TR)

Bu depo, teknik mülakatlara, algoritma testlerine  hazırlık amacıyla çözdüğüm problemlerden ve optimize ettiğim kodlardan oluşmaktadır. 

Amacım sadece çalışan kodlar yazmak değil; zaman karmaşıklığını (Time Complexity) düşüren, temiz ve Pythonic algoritmalar geliştirmektir.

##  Çalışılan Temel Konular ve Veri Yapıları

Bu repodaki çözümler aşağıdaki temel algoritma mantıklarını içermektedir:

*   **Diziler (Arrays) ve Döngü Optimizasyonu:** `O(n²)` iç içe döngülerden kaçınarak `O(n)` hızında çalışan tek döngülü çözümler (Örn: Borsada En Yüksek Kâr problemi).
*   **Hash Maps / Dictionaries (Sözlükler):** Veri setlerindeki elemanların frekanslarını sayma ve çok hızlı (O(1)) arama işlemleri (Örn: En çok tekrar eden elemanı bulma, Anagram kontrolü).
*   **Metin İşleme (String Manipulation):** Karakter dizilerini analiz etme, parçalama ve karşılaştırma algoritmaları.
 

## Çözülen Örnek Problemler

**Basit Seviye (Easy)**

| `ArtisSayisiniBul.py` | Dizilerde (Array) bir önceki güne göre artışları sayma. |


| `EnUzunAliskanlik.py` | Bir listedeki ardışık 1'lerin en uzun serisini bulma (Max Consecutive Ones). |


| `EnUzunKelime.py` | Metin (String) parçalama ve uzunluk karşılaştırması yapma. |

**Orta Seviye (Medium)**

| `EnyuksekKar.py` | Hisse senedinden elde edilebilecek en yüksek kârı O(n) hızında hesaplama. |


| `FirstUniqueCharacter.py` | Bir metindeki ilk tekrar etmeyen harfi Sözlük (Hash Map) ile bulma. |


| `İkiKelimeAnagram.py` | İki kelimenin anagram olup olmadığını kontrol etme. |


| `MajorityElement.py` | Liste içinde en çok tekrar eden elemanı Sözlük mantığı ile bulma. |

## Nasıl Çalıştırılır?

Projeyi bilgisayarınıza klonladıktan sonra, herhangi bir Python dosyasını terminal üzerinden çalıştırabilirsiniz:






------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------





# Python Algorithm & Problem Solving Practice (EN)

This repository consists of problems I have solved and codes I have optimized in preparation for technical interviews and algorithm tests.

My goal is not only to write working code, but also to develop clean and Pythonic algorithms that reduce time complexity.

## Core Topics and Data Structures Studied

The solutions in this repository include the following core algorithmic concepts:

*   **Arrays and Loop Optimization:** Single-loop solutions that run at `O(n)` speed, avoiding `O(n²)` nested loops (e.g., Best Time to Buy and Sell Stock problem).
*   **Hash Maps / Dictionaries:** Counting frequencies of elements in datasets and performing very fast (`O(1)`) search operations (e.g., Finding the majority element, Valid Anagram check).
*   **String Manipulation:** Algorithms for analyzing, splitting, and comparing character strings.

## Solved Example Problems

**Easy Level**

| File Name | Description |
| :--- | :--- |
| `ArtisSayisiniBul.py` | Counting increases compared to the previous day in arrays. |
| `EnUzunAliskanlik.py` | Finding the longest sequence of consecutive 1s in a list (Max Consecutive Ones). |
| `EnUzunKelime.py` | String splitting and length comparison. |

**Medium Level**

| File Name | Description |
| :--- | :--- |
| `EnyuksekKar.py` | Calculating the maximum profit achievable from a stock at O(n) speed. |
| `FirstUniqueCharacter.py` | Finding the first non-repeating character in a string using a Dictionary (Hash Map). |
| `İkiKelimeAnagram.py` | Checking whether two words are anagrams. |
| `MajorityElement.py` | Finding the most frequently occurring element in a list using Dictionary logic. |

## How to Run?

After cloning the project to your computer, you can run any Python file via the terminal: