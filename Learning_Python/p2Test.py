var = 1
print(var)
var = "3.10.8"
print("Python version: " + var)
#---------------------------------------
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)
#----------------------------------------
john = 3
mary = 5
adam = 6
print(john, mary, adam, sep=',')
total_apples = john + mary + adam
print("Total number of apples:", total_apples)
#----------------------------------------------
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 7.38

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
#----------------------------------------------
x =  -1
x = float(x)
y = (3 * (x ** 3)) - (2 * (x ** 2)) + (3 * x) -1
print("y =", y)
#----------------------------------------------
print("+" + 10 * "-" + "+")
print(("|" + 10 * " " + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
#----------------------------------------------
#leg_a = float(input("Input first leg length: "))
#leg_b = float(input("Input second leg length: "))
#print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))
#-----------------------------------------------------
#x = float(input("Enter value for x: "))
x = 1
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)
#--------------------------------------
#starthour = int(input("starting hour: "))
#startmins = int(input("starting mins: "))
#print("real time: " + str(starthour) + ":" + str(startmins))
#print("real time in minutes = " + str((starthour*60) + startmins))
#Endhour = int(input("End hour: "))
#Endmins = int(input("End mins: "))
#--------------------------------------
#a = float(input("Enter first value(floater): "))
#b = float(input("Enter second value(floater): "))
print("Addition: ", a+b)
print("Substraction: ", a-b)
print("Multiplication: ", a*b)
print("Divsion: ", a/b)
print(1/(a+(1/(a+(1/(a+1/a))))))
print(123 +0.0)
#--------------------------------------
var = 0  # Assigning 0 to var
print(var == 0)
var = 1  # Assigning 1 to var
print(var == 0)
# Important characters ≤, ≥
#--------------------------------------
#a = int(input("Enter: "))
print(a >= 100)
if a < 100:
    print("False")
elif a < 200:
    print("Oui Groß")
else:
    print("True")
#--------------------------------------
largest_number = -999999999
#number = int(input("Enter the a number: "))
number = 54546
if number == -1:
    print(largest_number)
    exit()
if number > largest_number:
    largest_number = number
    print(largest_number)
# Go to line 02
#--------------------------------------
# Read three numbers.
#number1 = int(input("Enter the first number: "))
#number2 = int(input("Enter the second number: "))
#number3 = int(input("Enter the third number: "))
# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.
#largest_number = max(number1, number2, number3)
# Print the result.
#print("The largest number is:", largest_number)
#--------------------------------------
#income = float(input("Enter the annual income: "))
income = 50000
if income < 85528:
    tax = (income * (18/100)) - 556.02
else:
    tax = ((income - 85528) * (32/100)) + 14839.02
if tax < 0.0:
    tax = 0.0
tax = round(tax, 0)
print("The tax is:", tax, "thalers")
#-----------------------------------------------
#year = int(input("Enter a year: "))
year = 2022
if year < 1582:
    print("Not within the Gregorian calendar period")
else:
    if year % 4 != 0:
    	print("Common year")
    else:
        print("Leap year")
print(2+3*5.)
#-----------------------------------------------
# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.
odd_numbers = 0
even_numbers = 0
# Read the first number.
#number = int(input("Enter a number or type 0 to stop: "))
number = 0
# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))
# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)
#-----------------------------------------------
counter = 10
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

secret_number = 777
#-----------------------------------------------
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
#user_number = int(input("Enter the number: "))
user_number = 777
while user_number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    user_number = int(input("Enter the number again: "))
print(secret_number, "Well done, muggle! You are free now.")
#-----------------------------------------------
for i in range(10):
    # do_something()
    pass
#-----------------------------------------------
print("-------------------------------------------")
for i in range(10):
    print("The value of i is currently", i)
#-----------------------------------------------
print("-------------------------------------------")
for i in range(2, 8):
    print("The value of i is currently", i)
#-----------------------------------------------
print("-------------------------------------------")
for i in range(2, 8, 3):
    print("The value of i is currently", i)
print("-------------------------------------------")
#-----------------------------------------------
import time
for second in range(1, 6):
    print(second, "Mississippi")
    time.sleep(1)
print("Ready or not, here I come!")
print("-------------------------------------------")
#-----------------------------------------------
# break - example
print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")
# continue - example
print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")
print("-------------------------------------------")
#-----------------------------------------------
largest_number = -99999999
counter = 0

number = -1 #int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")
print("-------------------------------------------")
#-----------------------------------------------
largest_number = -99999999
counter = 0
while True:
    number = -1 #int(input("Enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")
print("-------------------------------------------")
#-----------------------------------------------
user_word = "Gilles Theodore Johnny Bang" #input("Enter your word: ")
user_word = user_word.upper()

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        print(letter)
print("-------------------------------------------")
#-----------------------------------------------
hat_List = [1, 2, 3, 4, 5]
print(hat_List)
print(len(hat_List))
hat_List[2] = 2
#hat_List[2] = int(input("Enter an integer number:"))
print(hat_List)
print(len(hat_List))
hat_List[2] = "Anna"
#hat_List[-1] = input("Enter something:")
print(hat_List)
print(len(hat_List))
del hat_List[-2]
print(hat_List)
print(len(hat_List))
print("-------------------------------------------")
#-----------------------------------------------
my_list = []  # Creating an empty list.
for i in range(79):
    my_list.append(i + 1)
print(my_list)
print("-------------------------------------------")
#-------------------- Reversing the order of a List -------------------------
my_list = [10, 1, 8, 3, 5]
length = len(my_list)
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
print(my_list)

