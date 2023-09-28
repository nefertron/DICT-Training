

def summation(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
    return sum

print(summation(50))

def factorial(num):
    factorial = 1
    for x in range(1, num + 1):
        factorial = factorial * x
    return factorial


print(factorial(5))