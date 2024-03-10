#-------------------------------------------------------------------------------
# Name:        Program 20
# Author:      Gaurish Uniyal
#-------------------------------------------------------------------------------

sam_list = [11, 15, 13, 16, 13, 15, 16, 11]
print ("The list is: " + str(sam_list))

sam_list = list(set(sam_list))


print ("The list after removing duplicates: " + str(sam_list))