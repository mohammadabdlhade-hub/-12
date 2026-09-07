import tkinter as tk

def press(item):
    global expression
    expression += str(item)
    equation.set(expression)

def equalpress():
    try:
        global expression
        # استخدام eval لحساب النتيجة الرياضية
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except Exception:
        equation.set("خطأ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    gui = tk.Tk()
    gui.configure(background="light gray")
    gui.title("آلة حاسبة بايثون")
    gui.geometry("300x400")
    gui.resizable(False, False)

    expression = ""
    equation = tk.StringVar()

    # شاشة العرض
    expression_field = tk.Entry(gui, textvariable=equation, font=('Arial', 20), justify='right')
    expression_field.grid(columnspan=4, ipadx=8, ipady=20, padx=10, pady=10)

    # تعريف الأزرار
    buttons = [
        ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
        ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
        ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
        ('0', 5, 0), ('.', 5, 1), ('+', 5, 2), ('=', 5, 3)
    ]

    for (text, row, col) in buttons:
        if text == '=':
            b = tk.Button(gui, text=text, fg='white', bg='green',
                          command=equalpress, font=('Arial', 14, 'bold'))
        else:
            b = tk.Button(gui, text=text, fg='black', bg='white',
                          command=lambda t=text: press(t), font=('Arial', 14))
        b.grid(row=row, column=col, sticky="nsew", ipadx=10, ipady=10, padx=2, pady=2)

    # زر الحذف (C)
    clear_btn = tk.Button(gui, text='C', fg='white', bg='red',
                          command=clear, font=('Arial', 14, 'bold'))
    clear_btn.grid(row=6, column=0, columnspan=4, sticky="nsew", ipadx=10, ipady=10, padx=2, pady=2)

    # ضبط أبعاد الشبكة
    for i in range(7):
        gui.grid_rowconfigure(i, weight=1)
    for i in range(4):
        gui.grid_columnconfigure(i, weight=1)

    gui.mainloop()
