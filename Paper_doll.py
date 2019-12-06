# Given a string, return a string where for every character in the original there are three characters
def paper_doll(text):
 str = ""
 for i in text:
  str += i * 3
 return(str)
 
print(paper_doll("Hello"))
print(paper_doll("Missisippi"))
