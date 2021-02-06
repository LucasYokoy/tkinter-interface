import tkinter as tk

root = tk.Tk()
root.title("Calculator")
# iconbitmap could add an icon to the top left of the window, instead of the standard feather.
# root.iconbitmap('c:/path/to/icon')

e = tk.Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3)

first_num = 0
operation = ''
is_result = False


def button_click(value):
    def pressed_op(op):
        number = e.get()
        global first_num
        global operation
        first_num = float(number)
        operation = op
        e.delete(0, tk.END)

    def pressed_eq():
        number = e.get()
        second_num = float(number)
        global first_num
        global operation
        result = operation_dict[operation](first_num, second_num)
        first_num = 0
        operation = ''
        global is_result
        is_result = True
        e.delete(0, tk.END)
        e.insert(0, result)

    button_dict = {
        'C': lambda: e.delete(0, tk.END),
        '+': lambda: pressed_op('+'),
        '-': lambda: pressed_op('-'),
        '*': lambda: pressed_op('*'),
        '/': lambda: pressed_op('/'),
        '=': lambda: pressed_eq(),
    }

    operation_dict = {
        '+': lambda x, y: x+y,
        '-': lambda x, y: x-y,
        '*': lambda x, y: x*y,
        '/': lambda x, y: x/y,
    }

    if type(value) == int:
        global is_result
        if is_result:
            e.delete(0, tk.END)
            is_result = False
        current = e.get()
        # you have to delete what was in the field before, or they will concatenate.
        e.delete(0, tk.END)
        e.insert(0, str(current) + str(value))
    else:
        button_dict[value]()


button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1)).grid(row=1, column=0)
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2)).grid(row=1, column=1)
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3)).grid(row=1, column=2)
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4)).grid(row=2, column=0)
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5)).grid(row=2, column=1)
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6)).grid(row=2, column=2)
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7)).grid(row=3, column=0)
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8)).grid(row=3, column=1)
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9)).grid(row=3, column=2)
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0)).grid(row=4, column=0)
button_clear = tk.Button(root, text="C", padx=40, pady=20, command=lambda: button_click("C")).grid(row=4, column=1)
button_equal = tk.Button(root, text="=", padx=40, pady=20, command=lambda: button_click("=")).grid(row=4, column=2)
button_add = tk.Button(root, text="+", padx=40, pady=20, command=lambda: button_click("+")).grid(row=4, column=3)
button_sub = tk.Button(root, text="-", padx=40, pady=20, command=lambda: button_click("-")).grid(row=3, column=3)
button_mul = tk.Button(root, text="*", padx=40, pady=20, command=lambda: button_click("*")).grid(row=2, column=3)
button_div = tk.Button(root, text="/", padx=40, pady=20, command=lambda: button_click("/")).grid(row=1, column=3)

root.mainloop()
