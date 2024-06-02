import tkinter as tk

def evaluate(expression):
    try:
        result = str(eval(expression))
        display_var.set(result)
    except Exception as e:
        display_var.set("Error")


def click(button_value):
    current_expression = display_var.get()
    if current_expression == "Error":
        display_var.set("")
        current_expression = ""
    display_var.set(current_expression + str(button_value))


def clear_display():
    display_var.set("")


root = tk.Tk()
root.title("Basic Calculator")


display_var = tk.StringVar()


display = tk.Entry(root, textvariable=display_var, font=('Arial', 20), bd=10, insertwidth=4, width=14, borderwidth=4, bg="lightgrey")
display.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0, 'lightblue'), ('8', 1, 1, 'lightblue'), ('9', 1, 2, 'lightblue'), ('/', 1, 3, 'lightblue'),
    ('4', 2, 0, 'lightblue'), ('5', 2, 1, 'lightblue'), ('6', 2, 2, 'lightblue'), ('*', 2, 3, 'lightblue'),
    ('1', 3, 0, 'lightblue'), ('2', 3, 1, 'lightblue'), ('3', 3, 2, 'lightblue'), ('-', 3, 3, 'lightblue'),
    ('0', 4, 0, 'lightblue'), ('.', 4, 1, 'lightblue'), ('+', 4, 2, 'lightblue'), ('=', 4, 3, 'lightblue')]

for (text, row, col, color) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 20), bg=color,
                        command=lambda t=text: evaluate(display_var.get()))
    else:
        btn = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 20), bg=color,
                        command=lambda t=text: click(t))
    btn.grid(row=row, column=col, sticky="nsew")


clear_btn = tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 20), bg='black', fg='white', command=clear_display)
clear_btn.grid(row=5, column=0, columnspan=4, sticky="nsew")

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)


root.mainloop()

