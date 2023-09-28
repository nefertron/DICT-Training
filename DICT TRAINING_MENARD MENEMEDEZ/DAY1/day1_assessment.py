num = int(input('Enter a number : '))

thousand = num // 1000
five_hundred = (num % 1000) // 500
two_hundred = ((num % 1000) % 500) // 200
one_hundred = (((num % 1000) % 500) % 200) // 100
fifty = ((((num % 1000) % 500) % 200) % 100) // 50
twenty = (((((num % 1000) % 500) % 200) % 100) % 50) // 20
ten = ((((((num % 1000) % 500) % 200) % 100) % 50) % 20) // 10
five = (((((((num % 1000) % 500) % 200) % 100) % 50) % 20) % 10) // 5
one = ((((((((num % 1000) % 500) % 200) % 100) % 50) % 20) % 10) % 5) // 1


print(f"""
    {thousand} - 1000
    {five_hundred} - 500
    {two_hundred} - 200
    {one_hundred} - 100
    {fifty} - 50
    {twenty} - 20
    {ten} - 10
    {five} - 5
    {one} - 1
""")


thousand = num // 1000
amount = num % 1000
five_hundred = amount // 500
amount = amount % 500
two_hundred = amount // 200
amount = amount % 200
one_hundred = amount // 100
amount = amount % 100
fifty = amount // 50
amount = amount % 50
twenty = amount // 20
amount = amount % 20
ten = amount // 10
amount = amount % 10
five = amount // 5
amount = amount % 5
one = amount // 1


print(f"""
    {thousand} - 1000
    {five_hundred} - 500
    {two_hundred} - 200
    {one_hundred} - 100
    {fifty} - 50
    {twenty} - 20
    {ten} - 10
    {five} - 5
    {one} - 1
""")

