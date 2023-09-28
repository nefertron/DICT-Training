num = int(input('Enter a number : '))

list = [1000, 500, 200, 100, 50, 20, 10, 5, 1]

for pera in list:
    denomination = num // pera
    print(denomination , f' - {pera}')
    num = num % pera