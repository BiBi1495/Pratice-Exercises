# Write a function that returns the number of prime numbers that exist up to and including a given number

def count_primes(n):
 prime = 0
 count = 0
 for i in range(2,n+1):
  for k in range(2,i):
   if i % k == 0:
	break
  else:
   count += 1
 return(count)

print(count_primes(100))
print(count_primes(53))
