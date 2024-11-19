from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operator = ''
food_prices = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
drink_prices = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
dessert_prices = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


def click_button(number):
    global operator
    operator = operator + number
    calculator_viewer.delete(0, END)
    calculator_viewer.insert(END, operator)


def get_result():
    global operator
    result = str(eval(operator))
    calculator_viewer.delete(0, END)
    calculator_viewer.insert(0, result)
    operator = ''


def revisar_check():
    x = 0
    for c in food_box:
        if food_variables[x].get() == 1:
            food_box[x].config(state=NORMAL)
            if food_box[x].get() == '0':
                food_box[x].delete(0, END)
                food_box[x].focus()
        else:
            food_box[x].config(state=DISABLED)
            food_text[x].set('0')
        x += 1
    x = 0
    for c in drink_box:
        if drink_variables[x].get() == 1:
            drink_box[x].config(state=NORMAL)
            if drink_box[x].get() == '0':
                drink_box[x].delete(0, END)
                drink_box[x].focus()
        else:
            drink_box[x].config(state=DISABLED)
            drink_text[x].set('0')
        x += 1
    x = 0
    for c in dessert_box:
        if dessert_variables[x].get() == 1:
            dessert_box[x].config(state=NORMAL)
            if dessert_box[x].get() == '0':
                dessert_box[x].delete(0, END)
                dessert_box[x].focus()
        else:
            dessert_box[x].config(state=DISABLED)
            dessert_text[x].set('0')
        x += 1


def delete():
    global operator
    operator = ''
    calculator_viewer.delete(0, END)


def total():
    sub_total_food = 0
    p = 0
    for quantity in food_text:
        sub_total_food = sub_total_food + (float(quantity.get()) * food_prices[p])
        p += 1

    sub_total_drink = 0
    p = 0
    for quantity in drink_text:
        sub_total_drink = sub_total_drink + (float(quantity.get()) * drink_prices[p])
        p += 1

    sub_total_dessert = 0
    p = 0
    for quantity in dessert_text:
        sub_total_dessert = sub_total_dessert + (float(quantity.get()) * dessert_prices[p])
        p += 1

    sub_total = sub_total_food + sub_total_drink + sub_total_dessert
    taxes = sub_total * .16
    total1 = sub_total + taxes

    food_cost_var.set(f'{round(sub_total_food, 2)}')
    drink_cost_var.set(f'{round(sub_total_drink, 2)}')
    dessert_cost_var.set(f'{round(sub_total_dessert, 2)}')
    subtotal_var.set(f'{round(sub_total, 2)}')
    taxes_var.set(f'{round(taxes, 2)}')
    total_var.set(f'{round(total1, 2)}')


def receipt():
    billing_text.delete(1.0, END)
    num_receipt = f'N# - {random.randint(1000,9999)}'
    date = datetime.datetime.now()
    date_receipt = f'{date.day}/{date.month}/{date.year} - {date.hour}:{date.minute}'
    billing_text.insert(END, f'Datos:\t{num_receipt}\t\t{date_receipt}\n')
    billing_text.insert(END, f'*'*52+'\n')
    billing_text.insert(END, f'Items\t\tQuantity\t   Items Cost\n')
    billing_text.insert(END, f'-'*54+'\n')

    x = 0
    for food in food_text:
        if food.get() != '0':
            billing_text.insert(END, f'{food_list[x]}\t\t      {food.get()}\t      ${int(food.get())*food_prices[x]}\n')
        x += 1

    x = 0
    for drink in drink_text:
        if drink.get() != '0':
            billing_text.insert(END, f'{drink_list[x]}\t\t      {drink.get()}\t      ${int(drink.get()) * drink_prices[x]}\n')
        x += 1

    x = 0
    for dessert in dessert_text:
        if dessert.get() != '0':
            billing_text.insert(END, f'{dessert_list[x]}\t\t      {dessert.get()}\t      ${int(dessert.get()) * dessert_prices[x]}\n')
        x += 1

    billing_text.insert(END, f'-'*54+'\n')
    billing_text.insert(END, f'Cost of the Food: \t\t\t{food_cost_var.get()}\n')
    billing_text.insert(END, f'Cost of the Drink: \t\t\t{drink_cost_var.get()}\n')
    billing_text.insert(END, f'Cost of the Dessert: \t\t\t{dessert_cost_var.get()}\n')
    billing_text.insert(END, f'-' * 54 + '\n')
    billing_text.insert(END, f'Sub-total: \t\t\t{subtotal_var.get()}\n')
    billing_text.insert(END, f'Taxes: \t\t\t{taxes_var.get()}\n')
    billing_text.insert(END, f'Total: \t\t\t{total_var.get()}\n')
    billing_text.insert(END, f'*' * 52 + '\n')
    billing_text.insert(END, f'Thank you for your visit')


def save():
    receipt_info = billing_text.get(1.0, END)
    archive = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archive.write(receipt_info)
    archive.close()
    messagebox.showinfo('Information', 'The receipt saved succesfully')


def reset():
    billing_text.delete(0.1, END)
    for text in food_text:
        text.set('0')
    for text in drink_text:
        text.set('0')
    for text in dessert_text:
        text.set('0')

    for box in food_box:
        box.config(state=DISABLED)
    for box in drink_box:
        box.config(state=DISABLED)
    for box in dessert_box:
        box.config(state=DISABLED)

    for v in food_variables:
        v.set(0)
    for v in drink_variables:
        v.set(0)
    for v in dessert_variables:
        v.set(0)

    food_cost_var.set('')
    drink_cost_var.set('')
    dessert_cost_var.set('')
    subtotal_var.set('')
    taxes_var.set('')
    total_var.set('')


def center_window(window):
    """
    Centers a Tkinter window on the screen.
    """
    window.update_idletasks()  # Update the window size
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


# start tkinter
application = Tk()
application.title('My Shopping Store - Billing System')

# window size
application.geometry('1020x640')

# center the window
center_window(application)

# background
application.config(bg='DarkGray')

# top panel
top_panel = Frame(application, bd=1, relief=RAISED)
top_panel.pack(side=TOP)

# title label
title_label = Label(top_panel, text='Billing System', fg='black', font=('Dosis', 44), bg='DarkGray', width=30)
title_label.grid(row=0, column=0)

# left panel
left_panel = Frame(application, bd=1, relief=FLAT)
left_panel.pack(side=LEFT)

# costs dashboard
costs_dashboard = Frame(left_panel, bd=1, relief=FLAT, bg='azure4', padx=65)
costs_dashboard.pack(side=BOTTOM)

# food dashboard
food_dashboard = LabelFrame(left_panel, text='Food', font=('Dosis', 17, 'bold'), bd=1, relief=FLAT, fg='black')
food_dashboard.pack(side=LEFT)

# drink dashboard
drink_dashboard = LabelFrame(left_panel, text='Drink', font=('Dosis', 17, 'bold'), bd=1, relief=FLAT, fg='black')
drink_dashboard.pack(side=LEFT)

# dessert dashboard
dessert_dashboard = LabelFrame(left_panel, text='Dessert', font=('Dosis', 17, 'bold'), bd=1, relief=FLAT, fg='black')
dessert_dashboard.pack(side=LEFT)

# right panel
right_panel = Frame(application, bd=1, relief=FLAT)
right_panel.pack(side=RIGHT)

# calculator dashboard
calculator_dashboard = Frame(right_panel, bd=1, relief=FLAT, bg='DarkGray')
calculator_dashboard.pack()

# billing dashboard
billing_dashboard = Frame(right_panel, bd=1, relief=FLAT, bg='DarkGray')
billing_dashboard.pack()

# button dashboard
button_dashboard = Frame(right_panel, bd=1, relief=FLAT, bg='DarkGray')
button_dashboard.pack()

# products list
food_list = ['Chicken', 'Meat', 'Wagyu', 'Kebab', 'Sushi', 'Ramen', 'Pizza', 'Carbonara']
drink_list = ['Water', 'Soda', 'Juice', 'Wine', 'Beer', 'Tequila', 'Sydra', 'Vodka']
dessert_list = ['Icecream', 'Fruit', 'Brownie', 'Cake', 'Flan', 'Choco-flan', 'Mousse', 'Dorilocos']

# generate food items
food_variables = []
food_box = []
food_text = []
index = 0
for food in food_list:
    # create checkbutton
    food_variables.append('')
    food_variables[index] = IntVar()
    food = Checkbutton(food_dashboard,
                       text=food.title(),
                       font=('Dosis', 17, 'bold'),
                       onvalue=1,
                       offvalue=0,
                       variable=food_variables[index],
                       command=revisar_check)
    food.grid(row=index, column=0, sticky=W)

    # create input box
    food_box.append('')
    food_text.append('')
    food_text[index] = StringVar()
    food_text[index].set('0')
    food_box[index] = Entry(food_dashboard,
                            font=('Dosis', 16, 'bold'),
                            bd=1,
                            width=6,
                            state=DISABLED,
                            textvariable=food_text[index])
    food_box[index].grid(row=index, column=1)

    index += 1

# generate drink items
drink_variables = []
drink_box = []
drink_text = []
index = 0
for drink in drink_list:
    # create checkbutton
    drink_variables.append('')
    drink_variables[index] = IntVar()
    drink = Checkbutton(drink_dashboard,
                        text=drink.title(),
                        font=('Dosis', 17, 'bold'),
                        onvalue=1,
                        offvalue=0,
                        variable=drink_variables[index],
                        command=revisar_check)
    drink.grid(row=index, column=0, sticky=W)

    # create input box
    drink_box.append('')
    drink_text.append('')
    drink_text[index] = StringVar()
    drink_text[index].set('0')
    drink_box[index] = Entry(drink_dashboard,
                             font=('Dosis', 16, 'bold'),
                             bd=1,
                             width=6,
                             state=DISABLED,
                             textvariable=drink_text[index])
    drink_box[index].grid(row=index, column=1)

    index += 1

# generate dessert items
dessert_variables = []
dessert_box = []
dessert_text = []
index = 0
for dessert in dessert_list:
    # create checkbutton
    dessert_variables.append('')
    dessert_variables[index] = IntVar()
    dessert = Checkbutton(dessert_dashboard,
                          text=dessert.title(),
                          font=('Dosis', 17, 'bold'),
                          onvalue=1,
                          offvalue=0,
                          variable=dessert_variables[index],
                          command=revisar_check)
    dessert.grid(row=index, column=0, sticky=W)

    # create input box
    dessert_box.append('')
    dessert_text.append('')
    dessert_text[index] = StringVar()
    dessert_text[index].set('0')
    dessert_box[index] = Entry(dessert_dashboard,
                               font=('Dosis', 16, 'bold'),
                               bd=1,
                               width=6,
                               state=DISABLED,
                               textvariable=dessert_text[index])
    dessert_box[index].grid(row=index, column=1)

    index += 1

# variables
food_cost_var = StringVar()
drink_cost_var = StringVar()
dessert_cost_var = StringVar()
subtotal_var = StringVar()
taxes_var = StringVar()
total_var = StringVar()

# labels for costs y entrance fields

# FOOD COST LABEL
food_cost_label = Label(costs_dashboard,
                        text='Food Cost',
                        font=('Dosis', 11, 'bold'),
                        bg='azure4',
                        fg='black')
food_cost_label.grid(row=0, column=0)

food_cost_text = Entry(costs_dashboard,
                       font=('Dosis', 11, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=food_cost_var)
food_cost_text.grid(row=0, column=1, padx=41)

# DRINK COST LABEL
drink_cost_label = Label(costs_dashboard,
                         text='Drink Cost',
                         font=('Dosis', 11, 'bold'),
                         bg='azure4',
                         fg='black')
drink_cost_label.grid(row=1, column=0)

drink_cost_text = Entry(costs_dashboard,
                        font=('Dosis', 11, 'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=drink_cost_var)
drink_cost_text.grid(row=1, column=1, padx=41)

# DESSERT COST LABEL
dessert_cost_label = Label(costs_dashboard,
                           text='Dessert Cost',
                           font=('Dosis', 11, 'bold'),
                           bg='azure4',
                           fg='black')
dessert_cost_label.grid(row=2, column=0)

dessert_cost_text = Entry(costs_dashboard,
                          font=('Dosis', 11, 'bold'),
                          bd=1,
                          width=10,
                          state='readonly',
                          textvariable=dessert_cost_var)
dessert_cost_text.grid(row=2, column=1, padx=41)

# SUBTOTAL LABEL
subtotal_label = Label(costs_dashboard,
                       text='Subtotal Cost',
                       font=('Dosis', 11, 'bold'),
                       bg='azure4',
                       fg='black')
subtotal_label.grid(row=0, column=2)

subtotal_text = Entry(costs_dashboard,
                      font=('Dosis', 11, 'bold'),
                      bd=1,
                      width=10,
                      state='readonly',
                      textvariable=subtotal_var)
subtotal_text.grid(row=0, column=3, padx=41)

# TAXES LABEL
taxes_label = Label(costs_dashboard,
                    text='Taxes',
                    font=('Dosis', 11, 'bold'),
                    bg='azure4',
                    fg='black')
taxes_label.grid(row=1, column=2)

taxes_text = Entry(costs_dashboard,
                   font=('Dosis', 11, 'bold'),
                   bd=1,
                   width=10,
                   state='readonly',
                   textvariable=taxes_var)
taxes_text.grid(row=1, column=3, padx=41)

# TOTAL LABEL
total_label = Label(costs_dashboard,
                    text='Total',
                    font=('Dosis', 11, 'bold'),
                    bg='azure4',
                    fg='black')
total_label.grid(row=2, column=2)

total_text = Entry(costs_dashboard,
                   font=('Dosis', 11, 'bold'),
                   bd=1,
                   width=10,
                   state='readonly',
                   textvariable=total_var)
total_text.grid(row=2, column=3, padx=41)

# buttons
buttons = ['total', 'billing', 'save', 'reset']
buttons_created = []
columns = 0
for button in buttons:
    button = Button(button_dashboard,
                    text=button.title(),
                    font=('Dosis', 12, 'bold'),
                    fg='white',
                    bg='azure4',
                    bd=1,
                    width=8)

    buttons_created.append(button)

    button.grid(row=0,
                column=columns)
    columns += 1

buttons_created[0].config(command=total)
buttons_created[1].config(command=receipt)
buttons_created[2].config(command=save)
buttons_created[3].config(command=reset)

# billing
billing_text = Text(billing_dashboard,
                    font=('Dosis', 11, 'bold'),
                    bd=1,
                    width=42,
                    height=10)
billing_text.grid(row=0,
                  column=0)

# calculator
calculator_viewer = Entry(calculator_dashboard,
                          font=('Dosis', 14, 'bold'),
                          width=32,
                          bd=1)
calculator_viewer.grid(row=0,
                       column=0,
                       columnspan=4)

calculator_buttons = ['7', '8', '9', '+',
                      '4', '5', '6', '-',
                      '1', '2', '3', 'x',
                      'R', 'E', '0', '/']

saved_buttons = []

row = 1
column = 0

for button in calculator_buttons:
    button = Button(calculator_dashboard,
                    text=button.title(),
                    font=('Dosis', 13, 'bold'),
                    fg='white',
                    bg='azure4',
                    bd=1,
                    width=7)
    saved_buttons.append(button)

    button.grid(row=row,
                column=column)

    if column == 3:
        row += 1

    column += 1

    if column == 4:
        column = 0

saved_buttons[0].config(command=lambda: click_button('7'))
saved_buttons[1].config(command=lambda: click_button('8'))
saved_buttons[2].config(command=lambda: click_button('9'))
saved_buttons[3].config(command=lambda: click_button('+'))
saved_buttons[4].config(command=lambda: click_button('4'))
saved_buttons[5].config(command=lambda: click_button('5'))
saved_buttons[6].config(command=lambda: click_button('6'))
saved_buttons[7].config(command=lambda: click_button('-'))
saved_buttons[8].config(command=lambda: click_button('1'))
saved_buttons[9].config(command=lambda: click_button('2'))
saved_buttons[10].config(command=lambda: click_button('3'))
saved_buttons[11].config(command=lambda: click_button('*'))
saved_buttons[12].config(command=get_result)
saved_buttons[13].config(command=delete)
saved_buttons[14].config(command=lambda: click_button('0'))
saved_buttons[15].config(command=lambda: click_button('/'))


# keep the window open
application.mainloop()
