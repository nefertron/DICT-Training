from tkinter import *

root = Tk()

root.geometry('400x420')
root.title('My Tkinter Calculator')
root.configure(bg='lightblue')


MyEntry = Entry(root, font='Arial 20', width=22, justify=RIGHT)

# // works like margin
# MyEntry.place(x=50,y=50)

MyEntry.grid(row=0, column=0, padx=32, pady=30, columnspan=4)


num1 = Button(root, text='1', font='Arial 20', width=3, height=1,command=lambda:num_display('1'))
num1.grid(row=1, column=0)

num2 = Button(root, text='2', font='Arial 20', width=3, height=1,command=lambda:num_display('2'))
num2.grid(row=1, column=1)

num3 = Button(root, text='3', font='Arial 20', width=3, height=1,command=lambda:num_display('3'))
num3.grid(row=1, column=2)

add = Button(root, text='+', font='Arial 20', width=3, height=1,command=lambda:select_operator('+'))
add.grid(row=1, column=3, pady=6)


num4 = Button(root, text='4', font='Arial 20', width=3, height=1,command=lambda:num_display('4'))
num4.grid(row=2, column=0)

num5 = Button(root, text='5', font='Arial 20', width=3, height=1,command=lambda:num_display('5'))
num5.grid(row=2, column=1)

num6 = Button(root, text='6', font='Arial 20', width=3, height=1,command=lambda:num_display('6'))
num6.grid(row=2, column=2)

subtract = Button(root, text='-', font='Arial 20', width=3, height=1,command=lambda:select_operator('-'))
subtract.grid(row=2, column=3, pady=6)


num7 = Button(root, text='7', font='Arial 20', width=3, height=1,command=lambda:num_display('7'))
num7.grid(row=3, column=0)

num8 = Button(root, text='8', font='Arial 20', width=3, height=1,command=lambda:num_display('8'))
num8.grid(row=3, column=1)

num9 = Button(root, text='9', font='Arial 20', width=3, height=1,command=lambda:num_display('9'))
num9.grid(row=3, column=2)

multiply = Button(root, text='*', font='Arial 20', width=3, height=1,command=lambda:select_operator('*'))
multiply.grid(row=3, column=3, pady=6)


dot = Button(root, text='.', font='Arial 20', width=3, height=1,command=lambda:num_display('.'))
dot.grid(row=4, column=0)

zero = Button(root, text='0', font='Arial 20', width=3, height=1,command=lambda:num_display('0'))
zero.grid(row=4, column=1)

equal = Button(root, text='=', font='Arial 20', width=3, height=1,command=lambda:calculate())
equal.grid(row=4, column=2)

divide = Button(root, text='÷', font='Arial 20', width=3, height=1,command=lambda:select_operator('÷'))
divide.grid(row=4, column=3, pady=6)




def num_display(number):
    current_value = MyEntry.get() #get the current value // e.g. 123
    new_value = current_value + number # add the new number at the bottom of the current value // if new=4, then 1234

    MyEntry.delete(0, END) #delete all values
    MyEntry.insert(0,new_value) # replace with new_value


def select_operator(operator):
    global first_num
    global opr

    opr = operator
    first_num = int(MyEntry.get())
    MyEntry.delete(0, END)




def calculate():
    second_num = int(MyEntry.get())

    answer = 0
    if opr == '+':
        answer = first_num + second_num
    elif opr == '-':
        answer = first_num - second_num
    elif opr == '*':
        answer = first_num * second_num
    elif opr == '÷':
        answer = first_num / second_num

    MyEntry.delete(0, END)
    MyEntry.insert(0, answer)




root.mainloop()


