from tkinter import *


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

# calculator panel
calculator_panel = Frame(right_panel, bd=1, relief=FLAT, bg='DarkGray')
calculator_panel.pack(side=RIGHT)

# billing panel
billing_panel = Frame(right_panel, bd=1, relief=FLAT, bg='DarkGray')
billing_panel.pack(side=RIGHT)

# button panel
button_panel = Frame(right_panel, bd=1, relief=FLAT, bg='DarkGray')
button_panel.pack(side=RIGHT)

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
                       variable=food_variables[index])
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
                        variable=drink_variables[index])
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
    dessert = Checkbutton(dessert_dashboard, text=dessert.title(), font=('Dosis', 17, 'bold'),
                          onvalue=1, offvalue=0, variable=dessert_variables[index])
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

# keep the window open
application.mainloop()
