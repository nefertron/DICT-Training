# TRY AND EXCEPT FOR ERROR HANDLING

def divide(x,y):
    try:
        result = x / y

    except ZeroDivisionError:
        print('Cannot divide by zero!')
        return None
    
    else:
        return result
    

result = divide(1, 0)
print(result)