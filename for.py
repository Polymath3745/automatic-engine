def somefor():
    for letter in "Giraffe Academy":
        print(letter)

names = ["jim", "karen", "mike"]

def names():
    for name in names:
        print(name)

def cube(x, power):
    prod = 1
    for idx in range(power):
        prod *= x
    return prod

num = int(input("Enter a number: "))
exp = int(input("Enter the exponent value: "))

result = cube(num, exp)

print(result)