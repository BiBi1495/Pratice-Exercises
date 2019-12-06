# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(list):
 for i in range(len(list) - 1):
  if list[i] == 3 and list[i+1] == 3:
   return(True)
   break
 else:
   return(False)

print(has_33([1,3,1,3]))
print(has_33([1,3,3,1]))
print(has_33([3,1,3]))
