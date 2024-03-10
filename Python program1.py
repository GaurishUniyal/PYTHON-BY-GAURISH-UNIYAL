#-------------------------------------------------------------------------------
# Name:        Program 1
# Author:      Gaurish Uniyal
#-------------------------------------------------------------------------------

def ispalindrome(s):
    return s==s[::-1]
s="madam"
ans= ispalindrome(s)

if ans:
    print("Yes")
else:
    print("No")