

print('\n\n')
for i in range(1, 11):
    if i != 10:
        print(i, end='   ')
    else:
        print(i, end='  ')

    for j in range(1, 11):
        product = j * i
        if product < 10:
            print(f'0{product}', end=' | ')
        elif product == 100:
            print(product, end='|')
        else:
            print(product, end=' | ')
    print()
print('\n\n')
