def rectangle(length, width):
  area = length * width
  return area

length = float(input("Enter value"))
width = float(input("Enter another value: "))

area = rectangle(length, width)
print("The area of the rectangle is", area)