#Swap two integer variables without using a third variable
a = int(input("a = "))
b = int(input("b = "))

a = a+b
b = a-b
a = a-b

print(f"a = {a}, b = {b}")