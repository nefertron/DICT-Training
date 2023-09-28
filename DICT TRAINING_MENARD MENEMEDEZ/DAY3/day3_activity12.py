# TRANSLATOR 

english_to_spanish = {
    'hello' : 'hola',
    'goodbye' : 'adios',
    'cat' : 'gato',
    'dog' : 'perro',
    'food' : 'comida'
}

def translate_to_spanish(word):
    if word in english_to_spanish:
        return english_to_spanish[word]
    else:
        return 'Translation not found'

word_to_translate = input('\n\nEnter an English word to translate to Spanish : ')

translation = translate_to_spanish(word_to_translate)
if translation != 'Translation not found':
    print(f'The translation of [ {word_to_translate} ] is [ {translation} ]\n\n')
else:
    print(f'{translation}\n\n')
