import tkinter as tk



window = tk.Tk()
window.minsize(width=280, height=420)
window.maxsize(width=280, height=420)
window.title('Calculator')

equation = ''

Display = tk.Label(window, text=equation,fg='yellow' ,bg='red', height=4, width=39)
Display.grid(row=0, column=0, columnspan=4)

tk.Button(window, text='1', command= lambda: calculate('1'), height=4, width=8).grid(row=4, column=0)
tk.Button(window, text='2', command= lambda: calculate('2'), height=4, width=8).grid(row=4, column=1)
tk.Button(window, text='3', command= lambda: calculate('3'), height=4, width=8).grid(row=4, column=2)
tk.Button(window, text='4', command= lambda: calculate('4'), height=4, width=8).grid(row=3, column=0)
tk.Button(window, text='5', command= lambda: calculate('5'), height=4, width=8).grid(row=3, column=1)
tk.Button(window, text='6', command= lambda: calculate('6'), height=4, width=8).grid(row=3, column=2)
tk.Button(window, text='7', command= lambda: calculate('7'), height=4, width=8).grid(row=2, column=0)
tk.Button(window, text='8', command= lambda: calculate('8'), height=4, width=8).grid(row=2, column=1)
tk.Button(window, text='9', command= lambda: calculate('9'), height=4, width=8).grid(row=2, column=2)
tk.Button(window, text='0', command= lambda: calculate('0'), height=4, width=8).grid(row=5, column=0)
tk.Button(window, text='+', command= lambda: calculate('+'), height=4, width=8).grid(row=4, column=3)
tk.Button(window, text='/', command= lambda: calculate('/'), height=4, width=8).grid(row=1, column=3)
tk.Button(window, text='*', command= lambda: calculate('*'), height=4, width=8).grid(row=2, column=3)
tk.Button(window, text='-', command= lambda: calculate('-'), height=4, width=8).grid(row=3, column=3)
tk.Button(window, text='C', command= lambda: calculate('c'), height=4, width=18).grid(row=1, column=0, columnspan=2)
tk.Button(window, text='=', command= lambda: calculate('='), height=4, width=18).grid(row=5, column=2, columnspan=2)
tk.Button(window, text='<--', command= lambda: calculate('b'), height=4, width=8).grid(row=1, column=2)
tk.Button(window, text='.', command= lambda: calculate('.'), height=4, width=8).grid(row=5, column=1)



def calculate(value):

    global equation

    if value == '=':
        equation = str(eval(equation))
        Display.config(text= equation)
    elif value == 'c':
        equation = ''
        Display.config(text=equation)

    elif value == 'b':
        equation = equation[:len(equation)-1]
        Display.config(text=equation)
    else:
        equation += value
        Display.config(text=equation)





window.mainloop()