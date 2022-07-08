# print('Hello World Welcome')
# print('my name is udoy and my age is ', 100)
# print('udoy', 436)


# name = 'Udoy'
# age = 18

# print(name)

# print(name + ' is from Bangladesh')

# print(name, ' is ', age)

# -----------String-------------

# name = 'Udoy'

# print('Hi.\\n How are you')

# print("Hi ' im udoy")
# print(""" Hi im Udoy 'im the honest " is the best""")

# print(name)

# # print(name.upper())

# # var = ('this is the best comment').upper()
# # var = ('This is the best Comment').lower()

# # print(var)

# print(len(name))
# print(name.index('o'))
# print(name.replace('o', '0'))


# ---------------Number In Python------------

# from math import *

# num = 79
# number = str(num)


# print(78 + 22)
# print(33 + 33.43)
# print(50 - 30)
# print(10 * 5)
# print(100 / 6)
# print(100 % 9)
# # print(num)

# print(number)
# print('number is ' + number)
# print(-5)

# print(abs(-5))
# print(abs(+9))

# print(round(4.4))
# print(round(5.8))

# print(bin(3))

# print(sqrt(100))


# ------------------Getting User's Input-----------------


# name =  input('Enter Your Name: ')
# age = int(input('Enter Your Age: '))

# print('Your name is ' + name + ' and your age is ', age)


# -------------Word Replacement Exercise----------

# sentence = input('Enter Your Sentence: ')

# print('Your Sentence is: ', sentence)

# word1 = input('Enter the word to replace: ')
# word2 = input('Enter the word to replace it with: ')
# print(sentence.replace(word1, word2))


# ----------------List In Python------------

# countries = ['United Kingdom', 2, True, 33.2, 'Bangladesh', 'America', 'Pakistan', 'Canada']

# lis = list(('Bangldesh', 43, False))

# # print(countries[0][0])
# # print(countries[1:4])

# name = 'Udoy'
# print(type(name))

# print(type(countries))

# # countries[0] = 'United States'
# # countries[3] = 'India'

# print(countries)

# # print(countries[-2])
# print(len(countries))
# print(countries[1])
# print(type(countries[3]))

# print(lis)
# print(type(lis))


# -----------List Method------------

# list1 = [1, 2, 3, 4, 5]

# list2 = ['banana', 'apples', 'mango', 'mango', 'oranges', 'cherry']

# list3 = [4, 3, 5, 1, 2]

# list4 = list2.copy()
# list2.pop(0)

# del list1[3]

# print(list1)
# print(list2)

# list1.extend(list2)
# list2.append('tomatto')
# list2.insert(1, 'stobary')
# list2.remove('cherry')
# list2.clear()

# list3.sort()
# list3.reverse()
# print(list3)

# print(list1)
# print(list2)
# print(list2.index('mango'))
# print(list2.count('mango'))

# print(len(list2))


# -----------Tuples In Python----------


# three_numbers = (1, 2, 1, 'home', True, 3)
# string = ('home', 'about', 'earth', 'land')
# # three_numbers[1] = 23

# print(string)
# print(three_numbers)

# print(len(three_numbers))
# print(type(three_numbers))
# print(type(string))
# print(type(three_numbers[3]))


# -------------Functions In Python----------


# def greetings_funtion(name, age):
#     # print('Welcome ' + str(name))
#     print('Welcome ' + name + ' Your age ' + str(age) + ' years old')
#     # print('Welcome ' + name)


# name = input('Enter Your Name: ')
# age = input('Enter Your Age: ')

# greetings_funtion('Udoy', 'Tim', 'Tom')
# greetings_funtion(name = 'Udoy', age = 27)
# greetings_funtion(name, age)


# -----------The Return Keyword----------


# def add_numbers(num1, num2):

#     # return 5 + 4
#     return num1 + num2

# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))

# print(add_numbers(num1, num2))


# -------------IF Statements In Python--------------

# a = 4

# b = 3

# c = 'Udoy'

# d = 'Udoy'

# e = 43

# d = False

# boy = True
# short = True

# if a > b:
#     print(str(a) + ' is greater then ' + str(b))


# if e != True:
#     print('a is True')


# if a >= b:
#     print('True')


# if a == b:
#     print('A equals B')

# else:
#     print('a not equals b')


# if e == True:
#     print('e is true')

# elif e == False:
#     print('e is False')

# else:
#     print('a is none of the two')


# if boy == True or short == True:
#     print('He is a boy or he is short')


# value = input('Input a value: ')

# if type(value) == str:
#     print(value + ' is a string')

# else:
#     print(value + ' is not a string')


# value = input('Enter a number: ')


# if value % 5 == 0:
#     print(value, ' can be divided by 5')

# else:
#     print(value, 'cannot be divided by 5')


# if value < 10:
#     print(value, 'is less then 10')

# else:
#     print(value, ' is more then 10')


# ---------------Building An Even Number Checker Program-----------

# num = int(input('Enter a number: '))

# if num % 2 == 0:
#     print('Even number')
# else:
#     print('Odd number')


# -----------Dictonaries In Python------------


# my_dict = {
#     'name':'Udoy',
#     'name2':'John',
#     'age':18,
#     'is_tall':True,
#     'nationality':'Bangladesh',
#     'Qualification':'Programmer',
#     'friends':['Mahi', 'Mariyam', 'Fariha', 'Harry', 'Hamim', 'Akhi']
# }

# x = my_dict['name']

# # print(my_dict['friends'])
# # print(my_dict)
# # print(len(my_dict))
# # print(type(my_dict))

# print(x)


# --------------While Loops In Python--------------

# i = 10

# while i < 16 or i == 10:
#     print(i)
#     i += 1


# ----------------For Loop In Python--------------

# mylist = ['ji', 'ju', 'jo']

# mydict = {
#     'name':'Udoy',
#     'age': 18,
#     'country':'bangaldesh'
# }

# for letter in 'Hello':
#     print(letter)


# for values in mylist:
#     print(values)


# for items in mydict['name']:
#     print(items)


# for x in mylist:
#     print(x)
#     if x == 'ju':
#         break
#     print(x)


# for x in range(10):
#     print(x)

# else:
#     print('Finished Looping')



# ------------2D List-------------


# my_list = [1, 2, 3, 4]

# second_list = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(my_list)
# print(second_list[2])
# print(second_list[1][2])


# for lists in second_list:
#     for row in lists:
#         print(row)
#     else:
#         print('Finished')

# else:
#     print('Conpleted')


# -------------Building A Basic Calculator-------------


# num1 = int(input('Enter First Number: '))
# op = input('Enter Operator: ')
# num2 = int(input('Enter Second Number: '))

# if op == '+':
#     print('Output: ', num1 + num2)
# elif op == '-':
#     print('Output: ', num1 - num2)
# elif op == '*':
#     print('Output: ', num1 * num2)

# elif op == '/':
#     print('Output: ', num1 / num2)

# else:
#     print('Invalid Operator: Please Try Again...')


# -----------Try Except In Python-----------


# try:
#     x = int(input('Enter an interger: '))
#     print(x)
# except:
#     print('Value not a interger...')
# else:
#     print('nothing went wrong')

# finally:
#     print('Try except finished')



# --------------Reading Files---------------


# file = open('file.txt', 'r')

# print(file.readable())
# print(file.readline())
# print(file.readline())

# for lines in file.readlines():
#     print(lines)

# print(file.readlines())

# file.close()


# ------------Writing Files------------

# file = open('new.txt', 'w')

# # file.write('\nThis is the new country file')
# file.write('print("This is a new file")')

# file.close()


# -----------Classes And Objects In Python-------------


# class Myclass:
#     x = 5

# p1 = Myclass()
# print(p1.x)



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# # name = input('Enter Your Name: ')
# # age = input('Enter Your Name: ')

# c1 = Person('Udoy', 18)
# # c2 = Person(name, age)

# # print(c1.name)
# # print(c1.age)
# # print(c2.age)

# del c1

# print(c1)


# --------------Inheritance In Python------------

# from new import Student

# class Person(Student):
#     pass

# p1 = Person()
# print(p1.name)
# print(p1.gender)
# print(p1.age)



# --------------The Python Shell------------


# Open Python IDLE or Python Shell and code here ( not recomendent )



# ----------------Building A Simple Login And SignUp System with Python--------------

# print('Create Your account now!')
# username = input('Enter Your Username: ')
# password = input('Enter Your Password: ')

# print('Your account has been created successfully')
# print('Login Now')

# username2 = input('Enter Your Username: ')
# password2 = input('Enter Your Password: ')

# if username == username2 and password == password2:
#     print('Logged in successfully')
# else:
#     print('Invalid credentails')




# ------------Modules In Python---------------


import new


new.say_hi()