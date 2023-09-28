# TEMPERATURE CONVERTER

print(f"""\n\n
        TEMPERATURE CONVERTER
      
        [1] Celcius
        [2] Fahrenheit
\n\n""")

temp = int(input('Please select the unit to be converted : '))

if temp == 1:
    degree = float(input('\nPlease enter the degree : '))
    fahrenheit = (degree * (9/5)) + 32
    print(f'\n\n{degree}° C is equal to {fahrenheit}° F\n\n')
elif temp == 2:
    degree = float(input('\nPlease enter the degree : '))
    celcius = (degree - 32) * (5/9)
    print(f'\n\n{degree}° F is equal to {celcius}° C\n\n')
else:
    print('Sorry, your input is invalid!')




