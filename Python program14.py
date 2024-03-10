#-------------------------------------------------------------------------------
# Name:        Program 14
# Author:      Gaurish Uniyal
#-------------------------------------------------------------------------------

def remove_vowels(string):
    vowels = 'aeiouAEIOU'
    vowel_free_string = ''.join(char for char in string if char not in vowels)
    return vowel_free_string


input_string = 'Gaurish Uniyal'
vowel_free = remove_vowels(input_string)
print("String without vowels:", vowel_free)