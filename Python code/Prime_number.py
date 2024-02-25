primes =[]
for num in range(2,21):
  isPrime = True
  for n in range(2, num):
    if num % n ==0:
      isPrime = False
  if isPrime:
    primes.append(num)
print("The prime numbers between 2 and 20 are: ",primes)





# start = int(input("Enter number:"))
# end = int(input("Enter number: "))

# for n in range(start, end+1):
#   if n > 1:
#     for i in range(3, int(n*0.5)+1,2):
#       if(n%i==0):
#         break
#       else:
#         print(n)