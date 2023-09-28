from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
root.geometry('400x500')
root.title('My Tkinter Calculator')
root.configure(bg='lightsalmon')

# NAME
name_label  = Label(root, text='NAME', font='Arial 16',bg='lightsalmon')
name_label.grid(row=0, column=0, padx=3, pady=1)

name = Entry(root, width=35)
name.grid(row=0, column=1, padx=3, pady=1)
# NAME


# AGE
age_label  = Label(root, text='AGE', font='Arial 16', bg='lightsalmon', justify='left', anchor='w')
age_label.grid(row=1, column=0, padx=3, pady=1)

age_list = list(range(12, 99))

age_selector = IntVar()

age_combo = ttk.Combobox(root, width=32, values = age_list, textvariable=age_selector)
age_combo.grid(row=1, column=1, padx=3, pady=1)
# AGE


# GENDER
genderSelect = StringVar(root, 'Male')

gender_label  = Label(root, text='GENDER', font='Arial 16', bg='lightsalmon')
gender_label.grid(row=2, column=0, padx=3, pady=1)

gender1 = Radiobutton(root, text='Male', variable=genderSelect, value='Male', bg='lightsalmon')
gender1.place(x=158, y=67)

gender2 = Radiobutton(root, text='Female', variable=genderSelect, value='Female', bg='lightsalmon')
gender2.grid(row=2, column=1, padx=8, pady=1)
# GENDER


# ADDRESS
address_label  = Label(root, text='ADDRESS', font='Arial 16', bg='lightsalmon')
address_label.grid(row=3, column=0, padx=3, pady=1)

address = Entry(root, width=35)
address.grid(row=3, column=1, padx=3, pady=1)
# ADDRESS


# SKILLS
skills_label  = Label(root, text='SKILLS', font='Arial 16', bg='lightsalmon')
skills_label.grid(row=4, column=0, padx=3, pady=1)

skills = Entry(root, width=35)
skills.grid(row=4, column=1, padx=3, pady=1)
# SKILLS


# PHONE
phone_label  = Label(root, text='PHONE', font='Arial 16', bg='lightsalmon')
phone_label.grid(row=5, column=0, padx=3, pady=1)

phone = Entry(root, width=35)
phone.grid(row=5, column=1, padx=3, pady=1)
# PHONE



# EDUCATION
education_label  = Label(root, text='EDUCATION', font='Arial 16', bg='lightsalmon')
education_label.grid(row=6, column=0, padx=3, pady=1)

education_list = [
    'Elementary',
    'Bachelor`s Degree',
    'Masteral',
    'PhD'
]

education_selector = StringVar()
education_combo = ttk.Combobox(root, width=32, values = education_list, textvariable=education_selector)
education_combo.grid(row=6, column=1, padx=3, pady=1)
# EDUCATION


############## HOBBIES
hobbies_label  = Label(root, text='HOBBIES : ', font='Arial 16', bg='lightsalmon')
hobbies_label.grid(row=7, column=0, padx=3, pady=1)

hobby_selected_1 = IntVar()
hobby_1 = Checkbutton(root, width=27, text='Reading Books', bg='lightsalmon', onvalue=1, offvalue=0, textvariable='Reading Books', variable=hobby_selected_1)
hobby_1.grid(row=8, column=1, padx=3, pady=1)

hobby_selected_2 = IntVar()
hobby_2 = Checkbutton(root, width=27, text='Watching Movies', bg='lightsalmon', onvalue=1, offvalue=0, textvariable='Watching Movies', variable=hobby_selected_2)
hobby_2.grid(row=9, column=1, padx=3, pady=1)

hobby_selected_3 = IntVar()
hobby_3 = Checkbutton(root, width=27, text='Cooking', bg='lightsalmon', onvalue=1, offvalue=0, textvariable='Cooking', variable=hobby_selected_3)
hobby_3.grid(row=10, column=1, padx=0, pady=1)

hobby_selected_4 = IntVar()
hobby_4 = Checkbutton(root, width=27, text='Sports', bg='lightsalmon', onvalue=1, offvalue=0, textvariable='Sports', variable=hobby_selected_4)
hobby_4.grid(row=11, column=1, padx=3, pady=1)
############## HOBBIES


# DESCRIPTION
description_label  = Label(root, text='DESCRIPTION', font='Arial 16', bg='lightsalmon')
description_label.grid(row=12, column=0, padx=3, pady=1)

description = Text(root, width=27, height=4)
description.grid(row=12, column=1, padx=3, pady=1)
# DESCRIPTION


# SUBMIT BUTTON
submit = Button(root, text='SUBMIT', font='Arial 10', width=10, height=2, command=lambda:compile_data())
submit.grid(row=13, column=1, padx=3, pady=8)
# SUBMIT BUTTON


def compile_data():
    nameTxt = name.get()
    ageTxt = age_selector.get()
    genderTxt = genderSelect.get()
    addressTxt = address.get()
    skillsTxt = skills.get()
    phoneTxt = phone.get()
    educationTxt = education_selector.get()
    hobbiesTxt = ''

    if hobby_selected_1.get() == 1:
        hobbiesTxt += 'Reading Books'
        
    if hobby_selected_2.get() == 1:
        hobbiesTxt += 'Watching Movies'
        
    if hobby_selected_3.get() == 1:
        hobbiesTxt += 'Cooking'
        
    if hobby_selected_4.get() == 1:
        hobbiesTxt += 'Sports'

    descriptionTxt = description.get("1.0", "end-1c")
    msg = f"""
        NAME            : {nameTxt}
        AGE             : {ageTxt}
        GENDER          : {genderTxt}
        ADDRESS         : {addressTxt}
        SKILLS          : {skillsTxt}
        PHONE           : {phoneTxt}
        EDUCATION       : {educationTxt}
        HOBBIES         : {hobbiesTxt}
        DESCRIPTOPM     : {descriptionTxt}
    """
    messagebox.showinfo("Success", msg)

root.mainloop()



