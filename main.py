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
import hashlib
from unittest import case
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
# hour = current_time.tm_hour
# print("Current hour:", hour)
# if hour < 12:
#     print("Good morning!")
# elif 12 <= hour < 18:
#     print("Good afternoon!")
# elif 18 <= hour < 21:
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
a, b,c,d = map(int, input("Enter four numbers: ").split())
print(a, b , c , d)
