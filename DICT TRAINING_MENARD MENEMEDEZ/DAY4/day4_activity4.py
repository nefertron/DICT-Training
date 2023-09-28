

try:
    with open('text.txt', 'r') as file:
        contents = file.read()
        print('File contents : ')
        print(contents)

except FileNotFoundError:
    print("Error : The file 'text.txt' was not found")

except Exception as e:
    print(f'An error occured : {e}')

finally:
    if 'file' in locals():
        file.close()
