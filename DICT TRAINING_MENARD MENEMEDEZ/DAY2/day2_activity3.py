# RANDOM NUMBERS OR CHARACTERS GENERATOR
import random

print('\n\ninteger : ', random.randint(1,20))
print('float : ',random.random())
print('wifi password : ',''.join(random.choices('abcdefghijklmnopqrstuvwxyz@#$%^&*()_-+=[].,\\/', k=15)))
print('\n\n')
