# # print("tayyab abdul hannan")
# # print("Hello, World!")
# # print("Welcome to Python programming.")
# # print("This is a sample Python script.")
# # print("Enjoy coding!")
# # print("Have a great day!")
# # print("Let's learn Python together.")
# # print("Keep practicing to improve your skills.")
# print(3+2)
# import pandas
# print(pandas.__version__)
# print("tayyab")
# import hashlib
# from unittest import case
# print("\'tayyab \n \"abdul hannan\"")
# print ("good boy" , 4 , 5 ,7, sep="~" , end="$$")
# print("hello" , end=" #")
# print("world")
# a=12
# b="tayyab"
# print(a,b)
# print(type(a))
# print(type(b))
# list = [1,2,3,4.5,5,"tayyab",True, None, [1,2,3], (4,5,6), {7,8,9}]
# print(list)
# print(15+10)
# print(15-10)
# print(15*10.5)
# print(15/10)
# print(15//10)
# print(15%10)
# print(15**2)
# a=5
# b=2
# print("the value of a=",a , "the value of b=",b , "the sum of a and b is=", a+b)
# print("the value of a=",a , "the value of b=",b , "the subtraction of a and b is=", a-b)
# print("the value of a=",a , "the value of b=",b , "the multiplication of a and b is=", a*b)
# print("the value of a=",a , "the value of b=",b , "the division of a and b is=", a/b)
# print("the value of a=",a , "the value of b=",b , "the floor division of a and b is=", a//b)
# print("the value of a=",a , "the value of b=",b , "the modulo of a and b is=", a%b)
# print(a%b)
# a="2"
# b="3"
# print(a+b)
# print(int(a)+int(b))
# print(str(2)+str(3))
# a=5
# b=2.5
# # print(a+b)
# print(a+b)
# x=input()
# print("my name is",x)
# print(type(x))
# a= input("Enter first number: ")
# b= input("Enter second number: ")
# print(a+b) 
# print("the sum is: ", int(a)+int(b))
# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)
# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)
# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)
# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z)
# x = "Python "
# y = "is "
# z = "awesome"
# print(x + y + z)
#lets do  sequence data types list tuple and range
# lst = [1, 2, 3, 4, 5]
# tup = (1, 2, 3, 4, 5)
# rng = range(1, 6)
# print(type(lst))
# print(type(tup))
# print(type(rng))
# r = range(10)
# print(r)
# print(list(r))
# print(tuple(r))
# lets do mapping data types dict
# mydict = {"name": "Tayyab Abdul Hannan", "age": 30, "city": "Faisalabad"}
# print(type(mydict))
# print(mydict)
# print(mydict.values())
# print(mydict.keys())
# print(mydict.items())
# print(mydict.get("name"))
# print(mydict["age"])
# lets do set data type
# myset = {1, 2, 3, 4, 5}
# print(type(myset))
# print(myset)


# x = "awesome"
# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)
# myfunc()
# print("Python is " + x)

# x="tayyab "
# y="abdul 'hannan"
# print(x+y)
# z="hello every one " \
# "this is long string " \
# "on multiple line"
# print(z)
# a="""hello every one 
# this is long string 
# on multiple line"""
# print(a)
# print(a[1])
# print(a[-2])
# b="tayyab abdul hannan"
# x="shazain!"
# for character in b:
#   print(character)
# print(len(b))
# print(b.capitalize())
# print(b.upper())
# print(b.lower())
# print(b.title()) # each word's first letter will be capitalized
# print(b[0:4])  # it will print from index 0 to index 3 ,4 is excluded
# print(b[1:4])  # it will print from index 1 to index 3 ,4 is excluded
# print(b[:4])  # it will print from index 0 to index 3 ,4 is excluded
# print(b[0:])  # it will print from index 0 to end of string
# print(b[:])  # it will print the whole string
# print(b[0:-4])  # it will do this print(b[0:len(b)-4])
# print(b[-3:-1])  # it will print from index len(b)-3 to len(b)-2 ,len(b)-1 is excluded
# print(b[-1:-3])  # it will return empty string because in negative indexing it will start from right to left
# print(x[-4:-2])
#strings are immutable
# print(x.strip()) # removes any whitespace from the beginning or the end
# print(x.rstrip("!")) # removes any whitespace from the end
# print(x.lstrip("s")) # removes any whitespace from the beginning
# print(x.replace("shazain", "tayyab"))
# print(x.split("!")) # returns a list where the string has been split at each "!"
# print(len(x.center(50))) # returns the length of the string after centering it with spaces to a total length of 50
# print(x.count("a")) # returns the number of times a specified value occurs in a string
# print(x.endswith("!")) # returns true if the string ends with the specified value
# print(x.find("z")) # searches the string for a specified value and returns the position of where it was found
# print(x.find("l")) # searches the string for a specified value and returns the position of where it was found if not found it will return -1
# print(x.index("z")) # searches the string for a specified value and returns the position of where it was found
# print(x.index("l")) # searches the string for a specified value and returns the position of where it was found if not found it will raise an error
# print(x.isalnum()) # returns True if all characters in the string are alphanumeric
# print(x.isalpha()) # returns True if all characters in the string are in the alphabet
# print(x.isdecimal()) # returns True if all characters in the string are decimals
# print(x.islower()) # returns True if all characters in the string are lower case
# print(x.isupper()) # returns True if all characters in the string are upper case
# print(x.isspace()) # returns True if all characters in the string are whitespaces
# print(x.isprintable()) # returns True if all characters in the string are printable
# print(x.startswith("s")) # returns true if the string starts with the specified value
# print(x.swapcase()) # Swaps cases, lower case becomes upper case and vice versa

#condtional statements just starts from here
#membership operators is used to check if a value is present in a sequence such as string ,list ,tuple ,set ,dictionary
# x = "hello world"
# print("h" in x)
# print("H" in x)
# print("H" not in x)
#identity operators is used to check if two variables are same object in memory or not 
# print(x is x)
# print(x is not x)
# # more examples of identity operators
# y = x
# print(y is x)
# print(y is not x)
# a = [1, 2, 3]
# b = a
# print(b is a)
# print(b is not a)
# c = [1, 2, 3]
# print(c is a)
#logical operators
# a = 10
# b = 5
# print(a > 5 and b < 10) # True and True = True
# print(a > 5 and b > 10) # True and False = False
# print(a < 5 and b < 10) # False and True = False
# print(a < 5 and b > 10) # False and False = False
# print(a > 5 or b < 10) # True or True = True
# print(a > 5 or b > 10) # True or False = True
# print(a < 5 or b < 10) # False or True = True
# print(a < 5 or b > 10) # False or False = False
# print(not(a > 5)) # not True = False
# print(not(a < 5)) # not False = True

#relational operators
# age=int(input("Enter your age: "))
# print("Your age is:", age)
# print(age>18)
# print(age<18)
# print(age>=18)
# print(age<=18)
# print(age==18)
# print(age!=18)
# if(age>=18):
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

#else if ladder
# marks=int(input("Enter your marks: "))
# if marks>=90:
#     print("Grade A")
# elif marks>=80:
#     print("Grade B")
# elif marks>=70:
#     print("Grade C")
# elif marks>=60:
#     print("Grade D")
# elif marks>=50:
#     print("Grade E")
# else:
#     print("Grade F")

# print("Thank you!")    


#lets do nested if else
# num=int(input("Enter a number: "))
# if num>=0:
#     if num==0:
#         print("You entered zero.")
#     else:
#         print("You entered a positive number.")
# else:
#     print("You entered a negative number.")
    

#lets do an exercise using time module
# import time
# current_time = time.localtime()
# print("Current time:", current_time)
# hour = current_time.tm_hour
# print("Current hour:", hour)
# if hour >=0 and hour < 12:
#     print("Good morning!")
# elif hour >=12 and hour < 18:
#     print("Good afternoon!")
# elif hour >=18 and hour < 21 :
#     print("Good evening!")
# else:
#     print("Good night!")
# timestamp = time.strftime("%H:%M:%S")
# print(timestamp)
# timestamp = time.strftime("%H")
# print(timestamp)
# timestamp = time.strftime("%M")
# print(timestamp)
# timestamp = time.strftime("%S")
# print(timestamp)

#lets do match case statement it is similar to switch case in other languages
# it is available in python 3.10 and later versions
# it is a new feature in python 3.10 and later versions
# day=int(input("Enter day number (1-7): "))
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _ if day<1 or day>7: #  wildcard case with condition
#         print("Day number must be between 1 and 7") # added condition to wildcard case
#     case _ if day==0:    # default case will not work with condition
#         print("Day number cannot be zero") 
#     case _: # default case
#         print("Invalid day number")
# lets do for loop
# fruits = ["apple", "banana", "cherry"]
# for counter in fruits:
#     print(counter)
#     for character in counter:
#         print(character)
# x = input("Enter your name: ")
# for character in x:
#     print(character)
#     if character=="a":
#         print("This is letter a")

# for c in "tayyab":
#     print(c)
#     if c=="a":
#         print("This is letter a")

# for i in range(6):
#     print(i)
# for i in range(1, 6): # it will print from 1 to 5 ,6 is excluded
#     print(i)
# for i in range(1, 50001, 5000):
#     print(i)

# for i in range(10, 0, -1): # it will print from 10 to 1 ,0 is excluded
#     print(i)
# lets do while loop using while loop
# count=1
# while count<=5:
#     print("Count is:", count)
#     count+=1
# i=int(input("Enter starting of loop: "))
# while i<=10:
#     i=int(input("Enter a number: "))
#     print(i)

#lets print even numbers between 1 to 100 using while loop
# num=int(input("Enter starting number: "))
# while num<=20:
#     if num%2==0:
#         print("its even number:", num)
#     num+=1
#lets print table of a number using while loop
# num=int(input("Enter a number to print its table: "))
# i=1
# while i<=10:
    # print(f"{num} x {i} = {num*i}") # it will print num multiplied by i and f string is used for formatting
    # print(num ,"*" , i, "=", num*i) # it will print num multiplied by i
    # i+=1

# lets use continue and break statements in loops
# for i in range(1, 11):
#     if i==5:   # it will skip the iteration when i is 5
#         continue
#     print(i)
# for i in range(1, 11):
#     if i==5:
#         break
#     print(i)

# a,b = input("Enter two numbers separated by space: ").split()
# print("First number is:", a)  
# print("Second number is:", b)  
# a, b,c,d = map(int, input("Enter four numbers: ").split())
# print(a, b , c , d)
# lets do functions in python
# def greet(name):
#     print("Hello " + name + ". \nGood morning!")
# greet("Tayyab Abdul Hannan")

#let do another function with basic arithmetic operations take 2 numbers as input and return and print their sum and difference
def arithmetic_operations(num1, num2):
    sum_result = num1 + num2
    difference_result = num1 - num2
    print("Sum:", sum_result)
    print("Difference:", difference_result)
a, b = map(int, input("Enter two numbers separated by space: ").split())
arithmetic_operations(a , b)

# def pass_function():
#     pass # it is used when we want to create a function but we don't want to write any code in it yet
# pass_function()
#function arguments with examples
# def function_arguments(arg1, arg2, arg3="default value"):
#     print("Argument 1:", arg1)
#     print("Argument 2:", arg2)
#     print("Argument 3:", arg3)
# function_arguments("value1", "value2")
# function_arguments("value1", "value2", "custom value3")
# function_arguments(arg2="value2", arg1="value1") # calling function with keyword arguments order doesn't matter
# function_arguments(arg3="custom value3", arg1="value1", arg2="value2")

# def average(*args): #this is example of variable length arguments and tuqple unpacking 
#     total = sum(args)
#     print("Total = ", total)
#     count = len(args)
#     print("Count = ", count)
#     avg = total / count
#     return avg
# result = average(10, 20, 30, 40, 50,60,70,80,90,100)
# print("Average:", result)

#lets do an example of dictionary unpacking with function
# def display_info(name, age, city):
#     print("Name:", name)
#     print("Age:", age)
#     print("City:", city)    
# info = {"name": "Tayyab Abdul Hannan", "age": 30, "city": "Faisalabad"}
# display_info(**info) # dictionary unpacking with ** operator

#lets do an example of returning multiple values from a function
# def calculate_operations(num1, num2):
#     sum_result = num1 + num2
#     difference_result = num1 - num2
#     product_result = num1 * num2
#     quotient_result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
#     return sum_result, difference_result, product_result, quotient_result
# a, b = map(int, input("Enter two numbers separated by space: ").split())
# sum_val, diff_val, prod_val, quot_val = calculate_operations(a, b)
# print("Sum:", sum_val)
# print("Difference:", diff_val)
# print("Product:", prod_val)
# print("Quotient:", quot_val)

#lets code on lists in python
# fruits = ["apple", "banana", "cherry" ,10.5 , True , None]
# fruits2 = ["mango", "orange"]
# # fruits.clear() # clears the list
# fruits2.sort() # sorts the list
# print(fruits)
# mixfruits = fruits + fruits2 # concatenation of two lists
# print(mixfruits)
# mixfruits2 = [fruits , fruits2] # nested list
# print(mixfruits2)
# print(fruits)
# print(fruits[0])  # accessing first element
# print(fruits[1])  # accessing second element    
# print(fruits[2])  # accessing third element
# print(fruits[-1]) # accessing last element
# print(fruits[-2]) # accessing second last element
# print(fruits[len(fruits)-3]) # accessing third last element
# print(fruits[1:7]) # accessing elements from index 1 to 3 ,4 is excluded
# print(fruits[:3]) # accessing elements from index 0 to 2 ,3 is excluded
# print(fruits[2:]) # accessing elements from index 2 to end of list
# print(fruits[:]) # accessing all elements
# print(fruits[-4:-1]) # accessing elements from index len(fruits)-4 to len(fruits)-2 ,len(fruits)-1 is excluded
# print(fruits[0:7:2]) # accessing all elements with step of 2
# print(fruits[0:7:3]) # accessing all elements with step of 3

# if 10.5 in fruits:
#     print("10.5 is present in the list")
# else:
#     print("10.5 is not present in the list")  
# if "grape" in fruits:
#     print("grape is present in the list")
# else:
#     print("grape is not present in the list")
# if "apple" not in fruits:
#     print("apple is not present in the list")
# else:
#     print("apple is present in the list")
# if "ch" in "cherry":
#     print("ch is present in cherry")
# else:
#     print("ch is not present in cherry")
#list in comprehension
# lst = [x for x in range(10)]
# print(lst)
# squares = [x**2 for x in range(1, 11)]
# print(squares)
# even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
# print(even_squares)
# odd_squares = [x**2 for x in range(1, 11) if x % 2 != 0]
# print(odd_squares)
# list methods with examples
# numbers = [5, 2, 9, 1, 5, 6]
# print("Original list:", numbers)
# numbers.append(15) # adds 15 at the end of the list
# numbers.append(10) # adds 10 at the end of the list
# print("After append:", numbers)
# numbers.insert(2, 20) # inserts 20 at index 2
# print("After insert 20 at index 2:", numbers)
# numbers.sort() # sorts the list in ascending order
# print("After sort:", numbers)
# numbers.sort(reverse=True) # sorts the list in descending order
# print("After sort in descending order:", numbers)
# numbers.reverse() # reverses the list
# print("After reverse:", numbers)
# print(numbers.index(2)) # returns the index of first occurrence of 2
# numbers.remove(5) # removes first occurrence of 5
# print("After remove 5:", numbers)
# popped_value = numbers.pop() # removes and returns the last element
# print("Popped value:", popped_value)
# print("After pop:", numbers)
# # returns the count of 5 in the list
# print("Count of 5:", numbers.count(5))
# numbers_copy = numbers.copy() # creates a copy of the list
# print("Copy of the list:", numbers_copy)
# numbers2=numbers # this will not create a copy but will create a reference to the original list
# numbers2.append(100)
# print("2nd list after modifying copy:", numbers2)
# print("Original list after modifying copy:", numbers)
# numbers3 = numbers + numbers2 # concatenates two lists
# print("After concatenation new list:", numbers3)
# numbers.extend(numbers2) # extends the list by adding elements from another list
# print("After extend original list:", numbers)
# lets do tuple in python
# tuples can't be changed immutable
# mytuple = (1, 2, 3, 4, 5)
# mytuple = (1, 2, 3, 4, 5, 5, 4, 3, 2, 1)
# mytuple.count(2) # returns the count of 2 in the tuple but we are not printing it
# print("Count of 2:", mytuple.count(2))
# print(mytuple)
# mytuple1 = ("tayyab", "abdul", "hannan")
# print("after concatenation",mytuple + mytuple1)
# # mytuple[0] = 10  # this will raise an error because tuples are immutable
# # if we want to change some value in tuple we have to convert it to list then change the value and then convert it back to tuple
# mylist = list(mytuple)
# mylist[0] = 10
# mytuple = tuple(mylist)
# print("after update", mytuple)
# tup = (1,2)
# tup2 = (1)
# tup3 = (1,)
# print(type(tup))  # it will print <class 'tuple'>
# print(type(tup2))  # it will print <class 'int'>
# print(type(tup3))  # it will print <class 'tuple'>
# if 5 in mytuple:
#     print("5 is present in the tuple")
# print(type(mytuple))
# print(mytuple)
# print(mytuple[0])  # accessing first element
# print(mytuple[1])  # accessing second element
# print(mytuple[2])  # accessing third element
# print(mytuple[-1]) # accessing last element
# print(mytuple[-2]) # accessing second last element
# print(mytuple[len(mytuple)-3]) # accessing third last element
# print(mytuple[1:4]) # accessing elements from index 1 to 3 ,4 is excluded
# print(mytuple[:3]) # accessing elements from index 0 to 2 ,3 is excluded
# print(mytuple[2:]) # accessing elements from index 2 to end of tuple
# print(mytuple[:]) # accessing all elements
# print(mytuple[-4:-1]) # accessing elements from index len(mytuple)-4 to len(mytuple)-2 ,len(mytuple)-1 is excluded
# print(mytuple[0:5:2]) # accessing all elements with step of 2
# print(mytuple[0:5:3]) # accessing all elements with step of 3
# tuple methods with examples
# mytuple = (1, 2, 3, 4, 5, 5, 4, 3, 2, 1)
# print("Original tuple:", mytuple)
# print("Count of 5:", mytuple.count(5)) # returns the count of 5 in the tuple
# print("Index of first occurrence of 3:", mytuple.index(3)) # returns the index of first occurrence of 3
# print("Index of first occurrence of 4:", mytuple.index(4 , 3 , 7)) # returns the index of first occurrence of 4 between index 3 and 6
# print(len(mytuple)) # returns the length of the tuple

# lets create a program capable of displaying  questions to the user and storing the questions and user answers in a list display the final answers at the end and final score and final grade based on the score. questions should be from python that we have studied so far. from starting input user name and his age. lets get started

# questions = [
#     "What is the output of print(2**3)?",
#     "Which keyword is used to define a function in Python?",
#     "What is the correct way to create a list in Python?",
#     "Which of the following is a valid variable name in Python?",
#     "What does the 'len()' function do in Python?"
# ]
# options = [
#     ["6", "8", "9", "12"],
#     ["func", "def", "function", "define"],
#     ["list = {}", "list = []", "list = ()", "list = <>"],
#     ["1variable", "variable_name", "variable-name", "variable name"],
#     ["Returns the number of elements in a list/string", "Returns the last element of a list/string", "Returns the first element of a list/string", "Returns the sum of elements in a list"]
# ]
# answers = [2, 2, 2, 2, 1] # correct options index
# user_answers = []
# score = 0
# user_name = input("Enter your name: ")
# user_age = input("Enter your age: ")
# print(f"Welcome {user_name}, age {user_age}, to the Python Quiz!")
# for i in range(len(questions)):
#     print(f"Q{i+1}: {questions[i]}")
#     for j in range(len(options[i])):
#         print(f"{j+1}. {options[i][j]}")
#     user_answer = int(input("Enter your answer (1-4): "))
#     user_answers.append(user_answer)
#     if user_answer == answers[i]:
#         score += 1
# print("\nQuiz Completed!")
# print("Your Answers are:")
# for i in range(len(questions)):
#     print(f"Q{i+1}: {questions[i]}")
#     print(f"Your answer: {options[i][user_answers[i]-1]}")
#     print(f"Correct answer: {options[i][answers[i]-1]}\n")
# print(f"Your total score: {score} out of {len(questions)}")
# questions = [
#     "What is the output of print(2**3)?",
#     "Which keyword is used to define a function in Python?",
#     "What is the correct way to create a list in Python?",
#     "Which of the following is a valid variable name in Python?",
#     "What does the 'len()' function do in Python?"
# ]

# options = [
#     ["6", "8", "9", "12"],
#     ["func", "def", "function", "define"],
#     ["list = {}", "list = []", "list = ()", "list = <>"],
#     ["1variable", "variable_name", "variable-name", "variable name"],
#     [
#         "Returns the number of elements in a list/string",
#         "Returns the last element of a list/string",
#         "Returns the first element of a list/string",
#         "Returns the sum of elements in a list"
#     ]
# ]

# # correct option numbers (NOT index)
# answers = [2, 2, 2, 2, 1]

# user_answers = []
# score = 0

# user_name = input("Enter your name: ")
# user_age = input("Enter your age: ")

# print(f"\nWelcome {user_name}, age {user_age}, to the Python Quiz!\n")

# # ===================== QUIZ START =====================
# for i in range(len(questions)):
#     print(f"Q{i+1}: {questions[i]}")

#     for j in range(len(options[i])):
#         print(f"{j+1}. {options[i][j]}")

#     user_choice = int(input("Enter your answer (1-4): "))
#     user_answers.append(user_choice)

#     if user_choice == answers[i]:
#         score += 1

#     print()

# # ===================== RESULTS =====================
# print("Quiz Completed!\n")
# print("Your Answers are:\n")

# for i in range(len(questions)):
#     print(f"Q{i+1}: {questions[i]}")

#     # user answer (step by step)
#     user_choice = user_answers[i]
#     user_index = user_choice - 1
#     user_answer_text = options[i][user_index]

#     # correct answer (step by step)
#     correct_choice = answers[i]
#     correct_index = correct_choice - 1
#     correct_answer_text = options[i][correct_index]

#     print("Your answer:", user_answer_text)
#     print("Correct answer:", correct_answer_text)
#     print()

# print(f"Your total score: {score} out of {len(questions)}")

# percentage = (score / len(questions)) * 100
# if percentage >= 90:
#     grade = "A"
# elif percentage >= 80:
#     grade = "B"
# elif percentage >= 70:
#     grade = "C"
# elif percentage >= 60:
#     grade = "D"
# elif percentage >= 50:
#     grade = "E"
# else:
#     grade = "F"
# print(f"Your grade: {grade}")



#lets do sets in python
# myset = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
# print("myset:", myset) # duplicates will be removed
# # print(type(myset))
# myset2 = {5, 6, 10, 8, 3}
# print("myset2:", myset2)
# print(myset2)
# print(myset2)
# print(myset2)
# myset2[0] = 10  # this will raise an error because sets are unordered and do not support indexing
# myset.add(6) # adds 6 to the set
# print("After adding 6:", myset)
# myset.remove(3) # removes 3 from the set , raises error if 3 is not present
# print("After remove 3:", myset)
# myset.discard(4) # removes 4 from the set , does not raise error if 4 is not present
# print("After discard 4:", myset)
# popped_value = myset.pop() # removes and returns an arbitrary element from the set
# print("Popped value:", popped_value)
# print("After pop:", myset)
# myset.add(1) # adds 1 to the set
# print("After adding 1 again:", myset)
# myset.clear() # clears the set
# print("After clear:", myset)
# set2 = {4, 5, 6, 7, 8}
# print("Set2:", set2)
# union_set = myset.union(set2) # returns a new set with elements from both sets
# print("Union of sets:", union_set)
# intersection_set = myset.intersection(set2) # returns a new set with elements common to both sets
# print("Intersection of sets:", intersection_set)
# difference_set = myset.difference(set2) # returns a new set with elements in myset but not in set2
# print("Difference of sets (myset - set2):", difference_set)
# symmetric_difference_set = myset.symmetric_difference(set2) # returns a new set with elements in either set but not in both actually it will perform (myset - set2) union (set2 - myset)
# print("Symmetric difference of sets:", symmetric_difference_set)

# lets do format string it is used to format strings in python and make them more readable and easier to understand we can use format string to insert variables into strings and control the formatting of the output we can also use format string to create dynamic strings that can change based on the values of variables
# str = "My name is {}. I am {} years old and my height is {} feet."
# print(str.format("Tayyab Abdul Hannan", 37, 5.6))
# name = "Tayyab Abdul Hannan"
# age = 37
# height = 5.60000
# # formatted_string = f"My name is {name}. I am {age} years old and my height is {height:.1f} feet."
# formatted_string = f"My name is {{name}}. I am {age} years old and my height is {height:.1f} feet."
# print(formatted_string)
# print(f"{2*3}")
# print(type(f"{2*3}"))

#docstrings in python
# def my_function():
#     """This is a docstring. 
#     It is used to describe the function.
#     It can span multiple lines."""
#     print("Hello, World!")
# my_function() # calling the function
# # print(my_function.__doc__)  # printing the docstring of the function
# print(help(my_function))   # printing the docstring using help function  provides more detailed information about the function and its usage we can use help function to get information about any built-in function or module in python as well as user-defined functions and modules

#now study pep 8 python enhanced perposel guidelines for python code style
# PEP 8 is the style guide for Python code it provides guidelines and best practices on how to write Python code in a way that is readable and consistent with the rest of the Python community following PEP 8 guidelines can help improve the readability and maintainability of your code making it easier for others to understand and collaborate on your projects some key PEP 8 guidelines include using 4 spaces per indentation level limiting lines to a maximum of 79 characters using blank lines to separate functions and classes using descriptive variable and function names using spaces around operators and after commas and using comments to explain complex code constructs
# following PEP 8 guidelines can help you write clean and readable Python code that is easy to understand and maintain
# a=10
# b=3
# print("the value of a=",a , "the value of b=",b , "the addition of a and b is=", a+b)
# print("the value of a=",a , "the value of b=",b , "the subtraction of a and b is=", a-b)
# print("the value of a=",a , "the value of b=",b , "the multiplication of a and b is=", a*b)
# print("the value of a=",a , "the value of b=",b , "the division of a and b is=", a/b)
# print("the value of a=",a , "the value of b=",b , "the floor division of a and b is=", a//b)
# print("the value of a=",a , "the value of b=",b , "the modulus of a and b is=", a%b)
# print("the value of a=",a , "the value of b=",b , "the exponentiation of a and b is=", a**b)
# formatted_string = f"""the value of a={a} the value of b={b} the addition of a and b is={a+b}
# the subtraction of a and b is={a-b}
# the multiplication of a and b is={a*b}
# the division of a and b is={a/b}
# the floor division of a and b is={a//b}
# the modulus of a and b is={a%b}
# the exponentiation of a and b is={a**b}"""
# print(formatted_string)
# import this is used to display the zen of python which is a collection of guiding principles for writing computer programs in python
# import this
# it was written by tim peters and is included as an easter egg in the python programming language