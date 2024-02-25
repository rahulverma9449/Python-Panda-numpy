memo = {}
def fib(n):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    result = fib(n-1) + fib(n-2)
    memo[n] = result
    return result
for i in range(1,10):
  fibo = fib(i)
  print(fibo)
# // Method 2

def f(n):
  if n<=1:
    return n
  else:
    return f(n-1) + f(n-2)
for i in range(1,11):
  fib = f(i)
  print(fib)





  
  
  