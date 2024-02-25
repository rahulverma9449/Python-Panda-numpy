def factorial(num):
  if num == 0 or num ==1:
    return 1
  else:
    return num*factorial(num-1)
for i in range(1,11):
  fact = factorial(i)
  print(f"The Factorial of {i} is : {fact}")