# PRINTING THE INPUT CHAR BY CHAR

entered = input('\n\nPlease enter word to be printed : ')

print(f'\n\nYour entered value is {entered}\n')
print('Here is the breakdown\n')
for i in entered:
    print(i)
print('\n')


x = 'Sample String'
print(x)             # output - Sample String
print(x[2:5])        # output - mpl

s = 'Vietnam,Indonesia,Philippines'
a = s.split(',')
print(a)            # output - ['Vietnam', 'Indonesia', 'Philippines']