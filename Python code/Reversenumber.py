num = int(input("Enter number"))
 
reverse = 0
while(num > 0):
  reminder = num % 10
  reverse = (reverse * 10) + reminder
  num = num //10
  
print("\n Reverse of entered number is  = %d" %reverse)