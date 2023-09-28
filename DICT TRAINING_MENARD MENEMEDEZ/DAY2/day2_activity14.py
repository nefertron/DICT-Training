# ODD AND EVEN NUMBERS

odd_count = 0
even_count = 0
all_odds = None
all_even = None

print('\n\n')
for i in range(1, 11):
    num = int(input(f'Enter #{i} : '))
    
    if num % 2 == 0:
        if all_even:
            all_even = all_even + ', ' + str(num)
        else:
            all_even = str(num)
        even_count = even_count + 1
    else:
        if all_odds:
            all_odds = all_odds + ', ' + str(num)
        else:
            all_odds = str(num)
        odd_count = odd_count + 1
    i = i + 1

if all_even:
    if even_count > 1:
        print(f'\n\nThere are {even_count} EVEN numbers - {all_even}')
    else:
        print(f'\n\nThere is {even_count} EVEN number - {all_even}')
else:
    print(f'\n\nThere is no EVEN number in your inputs.')

if all_odds:
    if odd_count > 1:
        print(f'\n\nThere are {odd_count} ODD numbers - {all_odds}')
    else:
        print(f'\n\nThere is {odd_count} ODD number - {all_odds}')
else:
    print(f'\n\nThere is no ODD number in your inputs.')


print('\n\n')
        


    

