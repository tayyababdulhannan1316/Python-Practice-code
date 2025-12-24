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
import time
current_time = time.localtime()
hour = current_time.tm_hour
print("Current hour:", hour)
if hour < 12:
    print("Good morning!")
elif 12 <= hour < 18:
    print("Good afternoon!")
elif 18 <= hour < 21:
    print("Good evening!")
else:
    print("Good night!")


    