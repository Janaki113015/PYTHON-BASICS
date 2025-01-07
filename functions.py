# -*- coding: utf-8 -*-
"""Functions.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_DmwXg1KHGM8rGUoSw_9BeMvIPGFNXov
"""

print(dir(str))

a="Hello World"
print(a.lower())

a="Hello World"
print(a.upper())

a="Hello World"
print(a.swapcase())

a="hello world"
print(a.title())

a="hello World"
b=a.replace('hello','holaa')
print(b)

a='12345a'
b=a.isdigit()
print(b)

a=range(10)
print(a)

a=range(10)
b=list(a)
print(b)

#start,stop then steps
a=range(1,10,2)
b=list(a)
print(b)

#Function with return
def add_numbers(a,b):
  result=a+b;
  return result
print(add_numbers(10,20))

def greet(name,greeting='hello'):
  print(f"{greeting},{name}!")
greet("Alice")  # Uses the default greeting
# Output: hello, Alice!

greet("Bob", "Hi")  # Overrides the default greeting
# Output: Hi, Bob!

def calculate_sum(*args):
  total=sum(args)
  return total
print("Sum of 1,2,3",calculate_sum(1,2,3))
print("Sum of 1,2,3,4",calculate_sum(1,2,3,4))

correct_username='admin'
correct_password='1234'
while True:
  username=input("Enter your username")
  password=input("Enter your password")
  if username==correct_username and password==correct_password:
    print("Login successful")
    break
  else:
    print("Invalid username or password.Try Again.")

#join() - Used to join elements of a sequence (list, tuple, etc.) into a single string with a separator.
words = ['Hello', 'World']
result = " ".join(words)
print(result)

#lstrip() and rstrip() - Removes whitespace from the left or right side of the string, respectively.
text = "   Hello World   "
print(text.lstrip())
print(text.rstrip())

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
result = check_even_odd(4)
print(result)