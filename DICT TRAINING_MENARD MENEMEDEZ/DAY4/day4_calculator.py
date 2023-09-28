

import math

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def modulo(x,y):
    return x % y

def floor_division(x,y):
    return x // y


def power(x,y):
    return x**y

def summation(x,y):
    num = 0
    for i in range(x, y+1):
        num += i
    return num

def factorial(x):
    i = 1
    for n in range(i, x + 1):
        i *= n
    
    return i

def circumference(x):
    return 2 * math.pi * x












