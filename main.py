# print text to console
print("Hello, World!")
print("Goodbye, World!")

# declare variables using snake_case: separate words using underscores (ex: first_name)
# camelCase (JS) instead you capatialize the first letter of each word after the first (ex: firstName)
first_name = "Steve"
age = 127

# print variable to console
print(first_name)

age = 128
age += 1 # add 1 to the value of age variable
print(age)

last_name = "mystery"
print(f"{first_name} is {age} years old.") # use f-string to add varibales to printed string of text

# type coercion - > coding language automatically changes data type from number to string
# python does not do this, use str(variable) to manually invoke this conversion
print(first_name+" is " +str(age)+" years old.")

# comparisions
a=2
print(a > 1) # should return true
print(a == 1) # should return false
print(a < 1) # should return false
print(a !=  1) # should return true

# Create a list and print it
fave_bands = ["The Beatles", "Gorillaz", "Daft Punk"]
print (fave_bands)

# Print first indexed item in fave_bands list, aka fave_bands at 0
print (fave_bands[0])

# Print 3rd item in list (at index 2)
print (fave_bands[2])

# selecting -1 chooses last index in list
print (fave_bands[-1])

# print index item 0 and 1
print (fave_bands[0],fave_bands[1])

# print everything starting at index item 1 on
print (fave_bands[1:])

# dictonary, contains Keys and associated values. Keys must be strings and unique.
phonebook = {
    'Taylor': '555-555-5555',
    'Jeremy': '000-000-0000',
    'Steve': '+31 4566-37588'
}

# print value of phonebook dictionary's value at Jeremy's key (the phone number)
print(phonebook['Jeremy'])

# for loop to print string using each band in fave_bands
for band in fave_bands:
    print(f"I love {band}")

# conditionals example, check credit score
credit_score = 675
if credit_score >= 740:
    print("Okay you don't have to brag")
# elif = else if
elif credit_score >= 670:
    print("Good!")
elif credit_score >= 580:
    print("Fair")
else:
    print("womp womp, poor credit")

# functions, named blocks of code that perform a specific job.
# Called using the name of the function.
# Alleviates the need for writing the same code multiple times

# def = function definition
def rocket():
    for num in range(10, -1, -1): # use range to count down
        print(num)
    print("Blast off!🚀")

# run the rocket function
rocket()
rocket()