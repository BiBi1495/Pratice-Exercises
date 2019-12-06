# Write a function takes a two-word string and returns True if both words begin with same letter
def Animal_crackers(text):
 newtext = text.split()
 if newtext[0][0] == newtext[1][0]:
  return(True)
 else:
  return(False)
  
print(Animal_crackers("Bibi Bobo"))
print(Animal_crackers("Bibi Hehe"))
