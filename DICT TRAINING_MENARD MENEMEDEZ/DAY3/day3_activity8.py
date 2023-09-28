# TAX

global tax_rate
tax_rate = 0.08

# subtotal  = []
# total_cost = []

def calculate_total(array):
    print(f'\n\t{"=" * 70}')
    print('\n')
    subtotal = 0
    with_tax = []
    j = 1
    for i in array:
        subtotal = subtotal + i
        with_tax = i + (i * tax_rate)
        print(f'\tItem [{j}] \t-   {i}\t\t - {with_tax}')
        j += 1

    all_taxes = subtotal * tax_rate
    total_cost = subtotal + all_taxes

    print(f'\n\t{"-" * 35}')
    
    print(f"""\n
        SUBTOTAL        :   {subtotal}
        TAX             :   {all_taxes}
        TOTAL COST      :   {total_cost}
    """)

    print(f'\n\t{"=" * 70}')






calculate_total([
    150, 160, 170, 180, 190, 200, 650, 1000, 1250
])








