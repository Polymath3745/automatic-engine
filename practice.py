def somethingwhile():
    a = 3
    while(a < 10):
        print("Hello world")
        a += 1

def addnum(a, b):
    return a + b

x = int(input("Enter a number: "))
y = int(input("Enter antoher number: "))

print("The sum of the two numbers is: ",addnum(x, y))

fruit = ("apple", "bananas", "grapes")

sum = 0
for x in fruit:
    sum += 1

print(sum)