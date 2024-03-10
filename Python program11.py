#-------------------------------------------------------------------------------
# Name:        Program 11
# Author:      Gaurish Uniyal
#-------------------------------------------------------------------------------

def long_words(n, str):
    word_len = []
    txt = str.split(" ")


    for x in txt:

        if len(x) > n:
            word_len.append(x)


    return word_len

print(long_words(6, "I study in Doon University"))