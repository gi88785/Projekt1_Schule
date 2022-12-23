print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

print("Programming","Essentials","in", sep="***",  end="...")
print("Python")

print("    *" * 2)
print("   * *" * 2)
print("  *   *" * 2)
print(" *     * *     *")
print("***   ***" * 2)
print("  *   *" * 2)
print("  *   *  *   *")
print("  *****  *****") 

print("I'm", end=" ")
print("\"learning\"", end=" ")
print("\"\"\"python\"\"\"")

john = 3
mary = 5
adams = 6

print(john,",",mary,",",adams)

total_apples = john + mary + adams

print("Total number of apples:",total_apples)

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles*1.61
kilometers_to_miles = kilometers/1.61

print(miles, "miles is", miles_to_kilometers, "kilometers")
print(kilometers, "kilometers is", kilometers_to_miles, "miles")

x = 0
x = float(x)
y = (3*(x**3)) - (2*(x**2)) + (3*x) -1
print("y =", y)

x = 1
x = float(x)
y = (3*(x**3)) - (2*(x**2)) + (3*x) -1
print("y =", y)

x = -1
x = float(x)
y = (3*(x**3)) - (2*(x**2)) + (3*x) -1
print("y =", y)

x = 4 #print("Enter the Value of X:")
#x = input()
x = float(x)
y = (3*(x**3)) - (2*(x**2)) + (3*x) -1
print("y =", y)

#anything = input("Tell me anything...")
#print("Hmm...", anything, "...Really?")

x = 5.789 #x = input("Enter the Value of X: ")
y = (3*(x**3)) - (2*(x**2)) + (3*x) -1
print("y =", round(y,2))

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

a = 2#float(input("value for variable a: "))
b = 5#float(input("value for variable b: "))
c = a + b
d = a - b
e = a * b
f = a / b
print("output the result of addition here: ", c)
print("output the result of subtraction here:", d)
print("output the result of multiplication here", e)
print("output the result of division here:", f)

print("\nThat's all, folks!")

hour = 12#int(input("Starting time (hours): "))
mins = 54#int(input("Starting time (minutes): "))
dura = 30#int(input("Event duration (minutes): "))

endtime_hour = (int((mins + dura)/60) + hour)%24
endtime_mins = (mins + dura)%60

print("END TIME:", str(endtime_hour) + ":" + str(endtime_mins))

a = 123 + 0.0
print(a)

a = "Spathiphyllum"#input("Enter: ")

if a == "Spathiphyllum":
    print("yes - Spathiphyllum is the best plant ever!")
elif a == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("I want Spathiphyllum! Not " + str(a) + " !")

income = 10000#float(input("Enter the annual income: "))

if income <= 85528:
    if (income * (18/100)) - 556.2 > 0:
        tax = (income * (18/100)) - 556.2
    else:
        tax = 0.0

year = 1996#int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
else:
    if year%4 != 0:
        print("This is a common year")
    elif year%100 != 0:
        print("This is a Leap year")
    elif year%400 != 0:
        print("This is a common year")
    else: 
        print("This is a Leap year")

        
#else:
    #tax = 14839.2 + ((income - 85528)* (32/100))

#tax = round(tax, 0)
#print("The tax is:", tax, "thalers")

#while True:
    #print("I'm stuck inside a loop.")

# Store the current largest number here.
largest_number = -999999999

# Input the first value.
number = -1#int(input("Enter a number or type -1 to stop: "))

# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))

# Print the largest number.
print("The largest number is:", largest_number)

secret_number = 777

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
trials = 0
guess_number = 777#int(input("enter a number please: "))

while guess_number != secret_number:
    if trials > 2:
        print("Ha ha! You're stuck in my loop!")
        guess_number = int(input("enter a number please: "))
        trials += + 1
    else:
        print("That was the wrong number, try again!")
        guess_number = int(input("enter a number please: "))
        trials += + 1
print("Well done, muggle! You are free now.")

for i in range(10):
    print("The value of i is currently", i)

print("-----------------------------")

for i in range(1,10):
    print("The value of i is currently", i)

print("-----------------------------")

for i in range(1,10,2):
    print("The value of i is currently", i)

print("-----------------------------")

for i in range(1, 1):
    print("The value of i is currently", i)

print("-----------------------------")

for i in range(2, 1):
    print("The value of i is currently", i)

print("-----------------------------")

for i in range(2, 1, -1):
    print("The value of i is currently", i)

print("-----------------------------")

for i in range(0):
    print("The value of i is currently", i)

power = 1
for expo in range(17):
    print("2 to the power of", expo, "is", power)
    power *= 2

print("-----------------------------")

for count in range(1,6):
    print( count, "Mississippi")
print("Ready or not, here I come!")

print("-----------------------------")

#import time
for count in range(1,6):
    print( count, "Mississippi")
    #time.sleep(1) #delays the progression of the program by 1s

print("Ready or not, here I come!")

print("-----------------------------")
    
largest_number = -99999999
counter = 0

while True:
    number = -1#int(input("Enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

print("-----------------------------")

largest_number = -99999999
counter = 0

number = -7#int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = -1#int(input("Enter a number or type -1 to end program: "))

if counter: #i donot understand this.--------------------------------------
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

print("-----------------------------")

wordx = "Please"#input("What is the magic word?: ")

while True :
    if wordx != "Please":
        wordx = input("wrong, enter the magic word: ")
    else:
        break
print("You've successfully left the loop.")

print("-----------------------------")

user_word = "abstemious"#input("Enter a word: ")
user_word = user_word.upper()

for letter in user_word: # i really have to be more ope minded!
    if "A" == letter:
        continue
    elif "E" == letter:
        continue
    elif "I" == letter:
        continue
    elif "O" == letter:
        continue
    elif "U" == letter:
        continue
    else:
        print(letter)

print("-----------------------------")

user_word = "abstemious"#input("Enter a word: ")
user_word = user_word.upper()
word_without_vowels = ""

for letter in user_word: # i really have to be more ope minded!
    if "A" == letter:
        continue
    elif "E" == letter:
        continue
    elif "I" == letter:
        continue
    elif "O" == letter:
        continue
    elif "U" == letter:
        continue
    else:
        word_without_vowels += letter

print("here is the word without any vowels:", word_without_vowels)

print("-----------------------------")

i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

print("-----------------------------")

blocks = 1000#int(input("Enter the number of blocks: "))
counter = 0
height = 0

while blocks > 0:
    if counter == 0:
        height = 1
        blocks -= height
        counter += 1
        print("Counter0:", blocks)
        
        if int(blocks) < 0:
            print("you have no blocks")
            height = 0
            continue
        
    else:
        height += 1
        blocks -= height
        counter += 1
        print("Counter:", blocks)

        if int(blocks) < 0:
            height -= 1
            continue
print("The height of the pyramid:", height)

print("""
      *******
      *     *
      *     *
      *******
      """)

print("-----------------------------")

c0 = 15#int(input("Enter any non-negative and non-zero integer number: "))
counter = 0

while c0 != 1:
    if c0%2 == 0:
        c0 /= 2
        print(c0)
        counter += 1
    else:
        c0 = 3 * c0 + 1
        print("-------")
        print(c0)
        counter += 1

print("It took",str(counter)," steps")

print("-----------------------------")




















