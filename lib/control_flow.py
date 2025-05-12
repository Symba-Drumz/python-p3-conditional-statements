#!/usr/bin/env python3

def admin_login(username, password):
    if (username == "ADMIN" or username == "admin") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
    
print(admin_login("ADMIN", "12345"))  # Access granted
   
def hows_the_weather(temperature):
   if temperature < 40:
       return "It's brisk out there!"
   elif temperature >= 40 and temperature <= 60:
        return "It's a little chilly out there!"
   elif temperature > 85:
        return "It's too dang hot out there!"
   else:
        return "It's perfect out there!"
   
print(hows_the_weather(35)) 
print(hows_the_weather(55))
print(hows_the_weather(99)) 

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
    
print(fizzbuzz(15))  # FizzBuzz
print(fizzbuzz(9))   # Fizz
print(fizzbuzz(10))  # Buzz
    

def calculator(operation, num1, num2):
    if operation == "+" or operation == "-" or operation == "*" or operation == "/":
        return eval(f"{num1} {operation} {num2}")
    else:
        print("Invalid operation!")
        return None
    
print(calculator("+", 5, 3))  # 8
print(calculator("-", 5, 3))  # 2
print(calculator("*", 5, 3))  # 15
print(calculator("/", 5, 3))  # 1.6666666666666667
print(calculator("**", 5, 3)) # Invalid operation and None
