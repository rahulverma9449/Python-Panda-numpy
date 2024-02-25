#1. Using For Loop

def reverseString(string):
  revstr = ""
  for i in string:
    revstr = i + revstr
  return revstr

string = str(input("Enter String: "))
print("Original String: " + string)
print("Reversed String is : ",reverseString(string))