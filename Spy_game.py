# Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(list):
 l = len(list)
 for i in range(l-1):
  if list[i] == 0:
   for k in range(i+1,l):
	if list[k] == 0:
	 for n in range(k+1,l):
	  if list[n] == 7:
	   return(True)
 else:
  return(False)
   
print(spy_game([1,0,7,2,0,1]))
print(spy_game([1,0,3,8,0,2,7,1]))
print(spy_game([1,0,7,2,0,1,7]))
