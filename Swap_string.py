#Swap string values in two variables without using a third variable
a = input("a = ")
b = input("b = ")

a = a+" "+b
b,a = map(str, a.split(" "))
print("a = "+ a +" b = "+ b)