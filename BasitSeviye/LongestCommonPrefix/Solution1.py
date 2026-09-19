def longestCommonPrefix(strs):
    prefix = strs[0]

    for i in range(len(prefix)):
        char = prefix[i]
        for word in strs[1:]:
            if i >= len(word) or word[i] != char:
                return prefix[:i]

    return prefix


strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))  

   ##  LONGEST COMMON PREFIX

#   prefix = flower  , i = 0 , char = f , word = flow , if bloğuna girmedi
#   her şey aynı  içteki for bu sefer word un diğer değerini alack o da "flight"
#   prefix = flower  , i = 0 , char = f , word = flight , yine if bloğuna girmedi

# dıştaki for çalışacak bu sefer i = 1 olacak

#   prefix = flower  , i = 1 , char = l , word = flow , yine if bloğuna girmedi
#   her şey aynı  içteki for bu sefer word un diğer değerini alacak o da "flight"
#   prefix = flower  , i = 1 , char = l , word = flight , yine if bloğuna girmedi

# dıştaki for çalışacak bu sefer i = 2 olacak

#   prefix = flower  , i = 2 , char = o , word = flow , yine if bloğuna girmedi
#   her şey aynı  içteki for bu sefer word un diğer değerini alacak o da "flight"
#   prefix = flower  , i = 2 , char = o , word = flight , if bloğuna girer prefix =  fl 
#  olur ve fl döner 




