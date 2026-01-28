# print("tayyab abdul hannan")
# print("Hello, World!")
# print("Welcome to Python programming.")
# print("This is a sample Python script.")
# print("Enjoy coding!")
# print("Have a great day!")
# print("Let's learn Python together.")
# print("Keep practicing to improve your skills.")
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

# lets do mapping data types dictionary
# mydict = : "Tayyab Abdul Hannan", "age": 30, "city": "Faisalabad"}
# print(type(mydict))
# print(mydict)
# print(mydict.values())
# print(mydict.keys())
# print(mydict.items())
# print(mydict.get("name")) #it will not generate error if value not found
# print(mydict["name"]) #it will generate error if value not found
# print(mydict["age"])
# for key in mydict.keys():
#   print(mydict[key])
# for key,value in mydict.items():
#   print(f"the value corresponding to {key} is {value}")

# emp = {
#     1:  "Tayyab", 
#     2:  "Shazain", 
#     3:  "Ahmed", 
#     4:  "Ali"
# }

# print(emp)
# print(emp.get(2))
# print(emp.get(5 , "value not found"))
# emp.update()  # updating age of employee with id 4
# print(emp)
# emp2 = emp.copy()
# print(emp.pop(3))
# print(emp)
# print("the copy of employ",emp2)
# for k,v in emp2.items():
#     print(k,v)
# print(emp2.popitem())  #will remove value at the end of list

# print(emp.keys())
# print(emp.values())
# emp2 = emp.copy()
# print("the copied dictionary is:", emp2)
# Methods of dictionary
# mydict2 = {"id1":"tayyab" , "id2":"shazain"}
# print(mydict2)
# mydict.update(mydict2)  # merges mydict2 into mydict and updates the values of mydict if keys are same
# print("the value of mydict after merge",mydict)
# mydict2.clear() # clears the dictionary will not delete it
# print("the value of mydict after clear",mydict2)
# mydict.pop("age")
# print("the value of mydict after pop age",mydict)
# mydict.popitem() # it will remove last inserted item
# print("the value of mydict after popitem",mydict)
# del mydict2
# print("the value of mydict2 after del",mydict2) # it will raise an error because mydict2 is deleted
# del mydict["city"]
# print("the value of mydict after del city",mydict)
# mydict_copy = mydict.copy()
# print("the value of mydict_copy",mydict_copy)
# mydict_fromkeys = dict.fromkeys(["key1", "key2", "key3"], "default_value") # it will create a dictionary with keys from the list and all values set to default_value
# print("the value of mydict_fromkeys",mydict_fromkeys)
# mydict_setdefault = mydict.setdefault("country", "Pakistan") # it will add the key country with value Pakistan if country key is not present in the dictionary if it is present it will return the value of country key
# print("the value of mydict after setdefault",mydict)
# print("the value returned by setdefault",mydict_setdefault)




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
# lets do string methods always remember strings are immutable
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

# myemail = "tayyab123@gmail.com" #our task is to extract username and domain name from this email using string methods and also find the position of @ and . symbols also separate digit part too  like 123 from username
# at_position = myemail.find("@")
# dot_position = myemail.find(".")
# username = myemail[:at_position]
# domain = myemail[at_position+1:dot_position]
# domain_extension = myemail[dot_position+1:]
# digits = ""
# letters = ""
# for ch in username:
#     if ch.isdigit():
#         digits += ch
#     else:
#         letters += ch

# print("Email:", myemail)
# print("Username:", username)
# print("Domain:", domain)
# print("Domain Extension:", domain_extension)
# print("Digits in Username:", digits)
# print("Letters in Username:", letters)
# print("Position of @ symbol:", at_position)
# print("Position of . symbol:", dot_position)

# lets study arrays with examples
#it is different from list data type as it can only one type of data but list can store multiple types of data
# import array as arr
# myarray = arr.array('i', [1, 2, 3, 4, 5]) # 'i' is used for integer type array
# from array import * #means import full module with all functions of array
# myarray = array('i', [1, 2, 3, 4, 5]) # 'i' is used for integer type array
# print(type(myarray)) # data type should be same as written values otherwise
# print(myarray)       # you will get an error
# myarray.append(6)  # appends 6 at the end of the array
# print("Array after append:", myarray)
# myarray.insert(2, 10) # inserts 10 at index 2
# print("Array after insert:", myarray)
# myarray.remove(3) # removes first occurrence of 3
# print("Array after remove:", myarray)
# myarray.pop() # removes and returns the last element
# print("Array after pop:", myarray)
# print("First element:", myarray[0]) # accessing first element
# print("Last element:", myarray[-1]) # accessing last element
# myarray.reverse() # reverses the array
# print("Array after reverse:", myarray)
# myarray[1] = 20 # updating value at index 2
# print("Array after update:", myarray)
# print(type(myarray.tolist())) # converts array to list
# myarray2 = myarray  # copying array to another array just attaching reference
# print("the copied array is:", myarray2)
# myarray2[0] = 100
# print("the original array after modifying copied array is:", myarray)
# print("the copied array after modification is:", myarray2)
# myarray3 = array('i', myarray.tolist()) # creating a new array by copying existing array
# myarray3 = array('i' , (n for n in myarray)) # another way to copy array using generator expression
# print("the new copied array is:", myarray3)
# print("Array length:", len(myarray)) # length of array
# for i in myarray:
#     print(i)









#lets do condtional statements from here
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


#lets make a calculator using if else statements use all operators and input operator from user too
# num1 = float(input("Enter first number: "))
# operator = input("Enter operator (+, -, *, /): ")
# num2 = float(input("Enter second number: "))

# if operator == "+":
#     print(num1 + num2)
# elif operator == "-":
#     print(num1 - num2)
# elif operator == "*":
#     print(num1 * num2)
# elif operator == "/":
#     if num2 != 0:
#         print(num1 / num2)
#     else:
#         print("Error: Division by zero is not allowed.")
# else:
#     print("Invalid operator.")

#short hand if else 

# a = int(input("enter value of a:"))
# b = int(input("enter value of b:"))
# print("A") if a>b else print("=") if a==b else print("B")


# lets do another example of short hand if else
# 
# lets do another example of short hand if else with multiple conditions
# num = int(input("Enter a number: "))
# result = "Positive" if num > 0 else "Zero" if num == 0 else "Negative"
# print(result)

#for loop with else
# else executed when loop is completed successfully without break statement
# for i in range(1, 6):
#     print(i)
# else:
#     print("for Loop completed successfully.")

#we can do the same with while loop
# count = 1
# while count <= 5:
#     print(count)
#     count += 1
# else:
#     print("While loop completed successfully.")

#we can do another example of for loop with else
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)
# else:
#     print("All fruits have been printed.")

#another example of do while loop with while and else
# count = 1
# while True:
#     print(count)
#     count += 1
#     if count > 5:
#         break
# else:
#     print("While loop completed successfully.") # this else will not be executed because of break statement in the loop else block will be executed only if loop is not terminated by break statement

# for i in []:
#     print(i)
# else:
#     print("The loop did not execute because the iterable was empty.")

# for x in range(3):
#     print("Iteration no {} in for loop".format(x+1)) # it will print from 0 to 2 the {} is used to format the string and x+1 is used to print the iteration number starting from 1
# else:
#     print("for Loop completed successfully after {} iterations.".format(x+1))
# print("End of for loop.")

#lets do anexample using nested for loop
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"i = {i}, j = {j}")
#     print("Inner loop completed for i =", i)
# print("Outer loop completed.")

# lets do an example using nested while loop
# i = 1
# while i <= 3:
#     j = 1
#     while j <= 3:
#         print(f"i = {i}, j = {j}")
#         j += 1
#     print("Inner loop completed for i =", i)
#     i += 1
# print("Outer loop completed.")


# countries = ["USA", "Canada", "UK", "Pakistan"]
# for country in countries:
#     print(country)

# words = "helloworld"
# for word in words:
#     print(word)

# n=int(input("Enter a number to print its table: "))
# for i in range(1,11):
#   print(f"{n} * {i} = {n*i}")


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
#     case _ if day==0:    # default case will not work with condition
#         print("Day number cannot be zero") 
#     case _ if day<0 or day>7: #  wildcard case with condition
#         print("Day number must be between 1 and 7") # added condition to wildcard case
#     case _: # default case will work without condition will catch all other cases at input value not matched with any case
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
# def arithmetic_operations(num1, num2):
#     sum_result = num1 + num2
#     difference_result = num1 - num2
#     print("Sum:", sum_result)
#     print("Difference:", difference_result)
# a, b = map(int, input("Enter two numbers separated by space: ").split())
# arithmetic_operations(a , b)

# def pass_function():
#     pass # it is used when we want to create a function but we don't want to write any code in it yet
# pass_function()
# function arguments with examples
# def function_arguments(arg1, arg2, arg3="default value"):
#     print("Argument 1:", arg1)
#     print("Argument 2:", arg2)
#     print("Argument 3:", arg3)
# function_arguments("value1", "value2")
# function_arguments("value1", "value2", "custom value3")
# function_arguments(arg2="value2", arg1="value1") # calling function with keyword arguments order doesn't matter
# function_arguments(arg3="custom value3", arg1="value1", arg2="value2")

# def average(*args): #this is example of variable length arguments and tuple unpacking 
#     total = sum(args) #here sum is a built in function 
#     print("Total = ", total)
#     avg = total // len(args)
#     return avg
# result = average( 45, 76, 50,60,70,80,90,100)
# print("Average:", result)
# another example for variable length inputs using unpacking of tuple
# def avg(*numbers):
#     sum=0
#     for i in numbers:
#         sum = sum+i
#     print("average is:",sum//len(numbers))
# avg(50,70,90,100)
#lets do an example of dictionary unpacking with function
# def display_info(name, age, city):
#     print("Name:", name)
#     print("Age:", age)
#     print("City:", city)    
# info = : "Tayyab Abdul Hannan", "age": 30, "city": "Faisalabad"} 
# display_info(**info) # dictionary unpacking with ** operator **operator will unpack the dictionary and pass the key value pairs as arguments to the function


# lets do another example of functions
# def fun(a,b):
#     c = a + b
#     print(c)
#     print(a%b) # it will calculate

# x = 30 ; y = 20
# fun(x , y)


# lets do a function that calculates tax rate
def calculate_tax_rate(income, tax_paid):
    if income == 0:
        return "Cannot calculate tax rate"
    tax_rate = (tax_paid / income) * 100
    return tax_rate

income = float(input("Enter your income: "))
tax_paid = float(input("Enter the tax paid: "))
tax_rate = calculate_tax_rate(income, tax_paid)
print("Tax Rate:", tax_rate, "%")









#lets do another example of dictionary unpacking with function
# def name_print(**name):
#   print("Hello", name["fname"], name["mname"], name["lname"])

# name_print(mname="abdul", lname = "hannan" , fname = "tayyab")  
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

# lets do recursion in function
# def factorial(n):
#   if(n==0 or n==1 ):
#      return 1
#   elif(n>=2):
#      return n*factorial(n-1)
#   else:
#      return print("please enter a valid input")
# # print(factorial(3))
# print(f"factorial of given number: ", factorial(5))
#5*fact(4)
#5*4*fact(3)
#5*4*3*fact(2)
#5*4*3*2*fact(1)
#5*4*3*2*1

# lets do aonother example of recusion fibonacci sequence

# def fib(n):
#    if(n==0 or n==1):
#       return 1
#    else:
#       return (fib(n-1)+fib(n-2))
   
# print(f"the fib sequence is:",fib(5))   
      




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
# empty = {}
# empty2 = set ()
# print(type(empty))
# print(type(empty2))
# mixset = {1, 2.5, "hello", True, None}
# print(mixset)
# for value in mixset:
#     print(value)
# myset = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
# print("myset:", myset) # duplicates will be removed
# # # print(type(myset))
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
# union_set2 = myset | set2  # another way to do union of sets
# print("Union of sets:", union_set)
# print("Union of sets using | operator:", union_set2)
# intersection_set = myset.intersection(set2) # returns a new set with elements common to both sets
# print("Intersection of sets:", intersection_set)
# intersection_set2 = myset & set2  # another way to do intersection of sets
# print("Intersection of sets using & operator:", intersection_set2)
# intersection_update_set = myset.intersection_update(set2) # updates myset with elements common to both sets
# print("After intersection update myset:", myset)
# difference_set = myset.difference(set2) # returns a new set with elements in myset but not in set2
# print("Difference of sets (myset - set2):", difference_set)
# difference_set2 = myset - set2  # another way to do difference of sets
# print("Difference of sets using - operator (myset - set2):", difference_set2)
# symmetric_difference_set = myset.symmetric_difference(set2) # returns a new set with elements in either set but not in both actually it will perform (myset - set2) union (set2 - myset)
# print("Symmetric difference of sets:", symmetric_difference_set)
# symmetric_difference_set2 = myset ^ set2  # another way to do symmetric difference of sets
# print("Symmetric difference of sets using ^ operator:", symmetric_difference_set2)
# print("Is 2 present in myset?", 2 in myset) # membership operator
# print("Is 10 present in myset?", 10 in myset) # membership operator
# print("Is myset a superset of set2?", myset.issuperset(set2)) # checks if myset is a superset of set2
# print("Is set2 a subset of myset?", set2.issubset(myset)) # checks if set2 is a subset of myset
# print("Is myset disjoint with set2?", myset.isdisjoint(set2)) # checks if myset is disjoint with set2
# delete_set = myset.copy() # creates a copy of the set
# print("Copy of myset delete_set:", delete_set)
# del delete_set # deletes the set
# print("After deleting delete_set trying to print delete_set:")  
# print(delete_set) # this will raise an error because delete_set variable is deleted
# clean_set = myset.copy() # creates a copy of the set
# print("Copy of myset clean_set:", clean_set)
# clean_set.clear() # clears the set
# print("After clearing clean_set:", clean_set) # it will print empty set but clean_set variable is still present that's why no error will be raised





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


#lets do math functions
# print(min(10,45,20,3,9,50,190,35,77,60))
# print(max(10,45,20,3,9,50,190,35,77,60))
# print(sum([10,45,20,3,9,50,190,35,77,60]))
# print(abs(-10))
# print(round(10.5678))
# print(pow(2,3)) # 2 raised to the power 3
# import math
# print(math.sqrt(16)) # square root of 16
# print(math.ceil(10.2)) # rounds up to the nearest integer
# print(math.floor(10.8)) # rounds down to the nearest integer
# print(math.factorial(5)) # factorial of 5
# print(math.gcd(48, 18)) # greatest common divisor of 48 and 18
# print(math.lcm(4, 6)) # least common multiple of 4 and 6
# print(math.pi) # value of pi
# print(math.e) # value of e
# print(math.sin(math.pi/2)) # sine of 90 degrees
# print(math.cos(0)) # cosine of 0 degrees
# print(math.tan(math.pi/4)) # tangent of 45 degrees
# print(math.log(100, 10)) # logarithm of 100 to the base 10
# print(math.exp(2)) # e raised to the power 2
# print(math.radians(180)) # converts degrees to radians
# print(math.degrees(math.pi)) # converts radians to degrees
# print(math.copysign(-5, 3)) # returns a float with the magnitude of the first argument and the sign of the second argument
# print(math.isqrt(20)) # returns the integer square root of the non-negative integer n
# print(math.dist((1,2), (4,6))) # returns the Euclidean distance between two points
# print(math.hypot(3,4)) # returns the Euclidean norm, sqrt(x*x + y*y)
# print(math.prod([1,2,3,4])) # returns the product of a start value (default: 1) times an iterable of numbers
# print(math.trunc(10.5678)) # returns the truncated integer value of a float
# the evaluate function evaluates a string as a python expression and returns the result it can be used to dynamically execute python code stored in a string format
# expression = "3 + 5 * 2 - (4 / 2)"
# result = eval("3 + 5 * 2 - (4 / 2)")
# print("The result of the expression is:", result)



#lets do error handling in python
# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     result = num1 / num2
#     print("Result:", result)
# except ZeroDivisionError: #Catches division by zero error
#     print("Error: Cannot divide by zero.")
# except ValueError: #Catches value error if user enters non numeric value
#     print("Error: Invalid input. Please enter numeric values.")
# except Exception as e: #Catches any other error not handled above
#  e stores the error message
#     print("An unexpected error occurred:", str(e))
# else: # executes if no exception occurs and the try block is successful it is optional
#     print("Division completed successfully.")
# finally: # always executes regardless of whether an exception occurred or not it is also optional
#     print("Thank you for using the division program.")

# lets make another program for try except finally

# try:
#      a=int(input("enter a number whose table is to be printed:"))
#      print(f"the table of {a} is :")
#      for i in range(1,11):
#          print(f"{a}*{i} = {a*i}")
# except:
#      print("an invalid input is enterred:")
# finally:
#      print("table printed successfully")

# another example of try except finally which focus on importance of finally block
# try:
#      file = open("sample.txt", "r") # trying to open a file in read mode named sample.txt and assigning it to variable file
#      content = file.read() # reading the content of the file
#      print(content) # printing the content of the file
# except FileNotFoundError: # catching file not found error
#      print("Error: The file was not found.")
# except Exception as e: # catching any other exception
#      print("An unexpected error occurred:", str(e))
# finally: # finally block to close the file if it was opened
#      print("Closing the file.")
#      try:
#          file.close()
#      except:
#          print("File was not opened, so cannot be closed.")

#another example of try except finally which focus on importance of finally block
# def func():
#           try:
#                lst = [10 ,20,30, 40, 50]
#                i = int(input("enter index"))
#                print(lst[i])
#                return 1
#           except:
#                print("an error occured")
#                return 0
#           finally:
#                print("execution of finally block")
#                print("function execution completed")

# result = func()
# print("function returned:", result)

# in this program we defined a function check_age that raises a ValueError if the age is negative or greater than 150 we then use a try except block to catch and handle the exception when the user inputs an invalid age  
# lets raise custom exceptions in python
# def check_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative.")
#     elif age > 150:
#         raise ValueError("Age is too high.")
#     else:
#         print("Age is valid.")
# try:
#     user_age = int(input("Enter your age: "))
#     check_age(user_age)
# except ValueError as ve:
#     print("Invalid age:", ve)
# except Exception as e:
#     print("An unexpected error occurred:", str(e))

# a = int(input("Enter a number between 1 and 10: "))
# if a < 1 or a > 10:
#         raise ValueError("Please enter a number between 1 and 10.")

#lets do another example of raising custom error
# class NegativeNumberError(Exception):
#     """Custom exception for negative numbers."""
#     pass
# def calculate_square_root(number):
#     if number < 0:
#         raise NegativeNumberError("Cannot calculate square root of a negative number.")
#     return number ** 0.5 # calculate square root
# try:
#     num = float(input("Enter a number to calculate its square root: "))
#     result = calculate_square_root(num)
#     print(f"The square root of {num} is {result}")
# except NegativeNumberError as nne: # catching custom negative number error
#     print("Error:", nne)
# except ValueError: # catching value error for non numeric input
#     print("Invalid input. Please enter a numeric value.")
# except Exception as e: # catching any other exception
#     print("An unexpected error occurred:", str(e))
# In this program we defined a custom exception NegativeNumberError to handle cases where the user tries to calculate the square root of a negative number the calculate_square_root function raises this exception if the input number is negative we then use a try except block to catch and handle the custom exception as well as other potential exceptions like ValueError for non numeric inputs

# KBC 20 questions python quiz improved version
# Questions = [
#   ["What is the output of print(2**3)?", "8", "6", "9", "12", 1],
#   ["Which keyword is used to define a function in Python?", "func", "def", "function", "define", 2],
#   ["What is the correct way to create a list in Python?", "list = {}", "list = []", "list = ()", "list = <>", 2],
#   ["Which of the following is a valid variable name in Python?", "1variable", "variable_name", "variable-name", "variable name", 2],
#   ["What does the 'len()' function do in Python?", "Returns the number of elements in a list/string", "Returns the last element of a list/string", "Returns the first element of a list/string", "Returns the sum of elements in a list", 1],
#   ["What is the output of print(2+3*4)?", "20", "14", "24", "None of the above", 2],
#   ["What is the correct file extension for Python files?", ".pyth", ".pt", ".pyt", ".py", 4],
#   ["Which of the following is used to define a block of code in Python?", "Braces {}", "Parentheses ()", "Indentation", "Quotes ''", 3],
#   ["What is the output of print(10//3)?", "3.33", "3", "4", "None of the above", 2],
#   ["Which of the following is a mutable data type in Python?", "Tuple", "String", "List", "Integer", 3],
#   ["What is the output of print(10%3)?", "1", "3", "0", "None of the above", 1],
#   ["Which of the following is used to define a block of code in Python?", "Braces {}", "Parentheses ()", "Indentation", "Quotes ''", 3],
#   ["What is the output of print(5 in [1,2,3,4,5])?", "True", "False", "Error", "None of the above", 1],
#   ["Which of the following is a valid way to create a dictionary in Python?", "{}", "[]", "()","{}", 1],
#   ["What is the output of print(type(2+3j))?", "<class 'int'>","<class 'float'>","<class 'complex'>","<class 'bool'>",3],
#   ["Which method is used to add an element to a list in Python?", ".append()",".add()",".insert()",".extend()",1],
#   ["What does the 'is' operator do in Python?", "Checks if two variables refer to the same object","Checks if two variables have the same value","Checks if two variables are equal in value and type","None of the above",1],
#   ["Which keyword is used to import a module in Python?", "import","include","using","module",1],
#   ["What is the output of print(bool(0))?", "True","False","Error","None of the above",2],
#   ["Which of the following is used to create a set in Python?", "[]","()","{}","<>",3]
# ]

# Levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 3276800, 640000, 1250000, 2500000,5000000, 10000000, 20000000, 30000000,50000000, 70000000, 100000000] #list of levels in rs for each question
# money = 0
# for i in range(0, len(Questions)):
#     Question = Questions[i]
#     print(f"\nQuestion for Rs.{Levels[i]}:")
#     print(f"{i+1}. {Question[0]}")
#     print(f"a. {Question[1]}    b. {Question[2]}    c. {Question[3]}    d. {Question[4]}")   
#     reply = int(input("Enter your answer  as (1-4): or enter 0 to quit:\n "))
#     if(reply == 0):
#         print("You have chosen to quit the game.")
#         money = Levels[i-1] if i > 0 else 0
#         break  
#     if (reply == Question[-1]): # checking if the answer is correct -1 index contains the correct option number
#         print("Correct answer! You have won Rs.", Levels[i])
#         if(i == 4):
#             money = 10000
#         elif(i == 9 ):
#             money = 320000
#         elif(i == 14):
#             money = 10000000
#         elif(i == 19):
#             money = 700000000
#     else:
#         print("Wrong answer! You lost all your winnings.")
#         break
# print(f"You have won a total of Rs.{money}")


#lets understand random module in python
# import random
# print(random.randint(1, 100)) # prints a random integer between 1 and 100 inclusive
# print(random.choice(['apple', 'banana', 'cherry'])) # prints a random element from the list
# print(random.random()) # prints a random float between 0.0 and 1.0
# print(random.uniform(1.5, 10.5)) # prints a random float between 1.5 and 10.5
# my_list = [1, 2, 3, 4, 5]
# random.shuffle(my_list) # shuffles the list in place
# print(my_list) # prints the shuffled list





# write a program to translate a message in to secret code language. Use the rules below to translate normal english language into secret code language.
#coding rules:
# if the word contains atleast 3 characters then remove first letter and append at the end
#now append 3 random characters at starting and ending of the word
#else reverse the string
#decoding rules:
#if the word contains less than 3 characters then reverse the string
#esle 
#remove 3 random characters from starting and ending of the word
#remove last letter and append at the starting of the word
#your program should ask user whether he wants to encode or decode a message and then perform the operation accordingly
#after encoding or decoding display the final message to the user and ask if he wants to perform another operation or exit the program
# import random #importing random module to generate random characters
# def generate_random_string(length=3): #function to generate random string of given length
#     letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' #list of characters to choose from
#     return ''.join(random.choice(letters) for _ in range(length)) #joining random characters to form a string _ is used when the loop variable is not needed
# def encode_message(message):
#     words = message.split() #splitting the message into words based on space actually it will split on any whitespace character
#     encoded_words = []
#     for word in words:
#         if len(word) >= 3:
#             first_letter = word[0]
#             rest_of_word = word[1:]
#             random_prefix = generate_random_string()
#             random_suffix = generate_random_string()
#             encoded_word = random_prefix + rest_of_word + first_letter + random_suffix
#         else:
#             encoded_word = word[::-1] #reversing the string by slicing with step -1
#         encoded_words.append(encoded_word)
#     return ' '.join(encoded_words)
# def decode_message(encoded_message):
#     words = encoded_message.split()
#     decoded_words = []
#     for word in words:
#         if len(word) > 6:  # since we added 3 random characters at start and end
#             core_word = word[3:-3]  # remove first 3 and last 3 characters
#             last_letter = core_word[-1]
#             rest_of_word = core_word[:-1]
#             decoded_word = last_letter + rest_of_word
#         else:
#             decoded_word = word[::-1]
#         decoded_words.append(decoded_word)
#     return ' '.join(decoded_words) #joining the decoded words to form the final message
# action = input("Do you want to encode or decode a message? (e/d): ").lower()
# if action == 'e':
#     message = input("Enter the message to encode: ")
#     encoded_message = encode_message(message)
#     print("Encoded message:", encoded_message)
# elif action == 'd':
#     encoded_message = input("Enter the message to decode: ")
#     decoded_message = decode_message(encoded_message)
#     print("Decoded message:", decoded_message)
# else:
#     print("Invalid action. Please enter 'e' to encode or 'd' to decode.")





#enumerate function in python
#it is used to iterate over a list or any other iterable and get both the index and the value of each element in the iterable
# mylist = ['apple', 'banana', 'cherry']
# for index, value in enumerate(mylist):
#     print(f"Index: {index}, Value: {value}")


# # another example of enumerate function
# fruits = ['apple', 'banana', 'cherry', 'date']
# for indx, fruit in enumerate(fruits, start=1): # starting index from 1 instead of 0
#     print(f"Fruit {indx}: {fruit}")

# lets do another example of enumerate function with better understandings 

# Example 1: Basic usage
# numbers = [10, 20, 30, 40]
# for i, num in enumerate(numbers):
#     print(f"Index: {i}, Value: {num}")

# # Example 2: Starting index from a different value
# colors = ['red', 'green', 'blue']
# for i, color in enumerate(colors, start=1):
#     print(f"Position {i}: {color}")

# lets discuss virtual environments in python it is used to create isolated python environments 
# for different projects allowing you to manage dependencies and packages separately for each project without interfering with other projects or the global python installation
# lets understand it with example

# Example 1: Creating and using a virtual environment
# Virtual environments allow you to manage project-specific dependencies.

# Step 1: Create a virtual environment named 'myenv'
# Command: python -m venv myenv

# Step 2: Activate the virtual environment
# On Windows: myenv\Scripts\activate
# (After activation, your prompt will show (myenv) indicating it's active)

# Step 3: Install packages in the virtual environment
# Command: pip install requests

# Step 4: Use the installed package in your Python code
# import requests
# response = requests.get('https://httpbin.org/get')
# print(response.json())

# Step 5: Deactivate the virtual environment
# Command: deactivate
# (This returns you to the global Python environment)

# Example 2: Checking installed packages in venv
# Command: pip list
# This shows only packages installed in the current venv, not globally.

# Example 3: Creating requirements.txt for reproducibility
# Command: pip freeze > requirements.txt
# Then, in another venv: pip install -r requirements.txt

# Benefits: Isolated dependencies, no conflicts between projects, easy to share requirements.