# REVERSE OF THE INPUT

# palindrome logic
a = input('\n\nEnter a word to be reversed : ').upper()
print(f'\nINPUT\t: {a} \nOUTPUT\t: {a[::-1]} ({len(a)} ', 'character)' if len(a) == 1 else 'characters)', end='\n\n')


# using for loop
for i in range(len(a)-1 , -1, -1):
    print(a[i], end='')