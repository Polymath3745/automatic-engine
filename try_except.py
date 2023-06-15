# Handles the error without breaking the program



try:
    
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)

# except for a specific error so it is not too broad
except ZeroDivisionError as err:
    print(err)

except ValueError:
    print("Invalid input")

# this is where try and except comes in 