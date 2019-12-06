# Write a function that returns the lesser of two given numbers if both numbers are even, 
# but returns the greater if one or both numbers are odd
def lesser_of_two_even(a,b):
 if a % 2 == 0 and b % 2 == 0:
  if a < b:
   return(a)
  else:
   return(b)
 else:
  if a > b:
   return(a)
  else:
   return(b)
   
print(lesser_of_two_even(2,5))
print(lesser_of_two_even(2,4))
