sides= input("insert lenghts of side a, b, c (example: A=1, B=2, C=3): ")

a= sides[2]
b= sides[7]
c= sides[12]

if a==b==c:print("equilateral triangle")
elif a==b or b==c or a==c:print("isosceles triangle")
else:print("scalene triangle")