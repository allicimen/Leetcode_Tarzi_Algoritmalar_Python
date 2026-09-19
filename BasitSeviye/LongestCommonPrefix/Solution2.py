class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        candidate = strs[0]

        for word in strs:
            while not word.startswith(candidate):
                candidate = candidate[:-1]

        return candidate


  #  for 1.döngü :  candidate = flower ,  word = flower 
  #  for 2.döngü :  candidate  = flower ,  word = flow  (while döngüsü çalışır)  
  #  candidate = flowe  olur tekrar while çalışır  candidate = flow olur ...while biter for çalışır
  #  for 3. döngü :  candidate = flow , word = flight  (while döngüsü çalışır)
  #  candidate = flo olur.  sonra  candidate  =  fl  olur.. for döngüsü biter.
  #  return candidate çalışır ve çıktı olarak fl yi verir...  