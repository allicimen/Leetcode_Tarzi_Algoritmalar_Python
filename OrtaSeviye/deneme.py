

def longestcommon (metin ):

    candidate = metin[0]

    for word  in metin :
        while candidate > word:
            candidate = candidate[:-1]

        if metin startswith(candidate)





metin =  ["flower" ,"flow","flight"] #output :fl