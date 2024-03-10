#-------------------------------------------------------------------------------
# Name:        Program 19
# Author:      Gaurish Uniyal
#-------------------------------------------------------------------------------

def remove_char(s, i):
    a = s[ : i]
    b = s[i + 1: ]

    return a+b

string = "I'am a student of Doon University"

i = 5
print(remove_char(string,i-1))