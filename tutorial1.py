from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog


def main():
    # just as in flutter, everything is a widget. We begin with the root widget
    root = Tk()
    # geometry can define the dimensions of the window
    root.geometry("1000x800")
    # applies a label on the root widget
    # packing keeps the object in a fixed relative position in the middle, when the window is resized
    label1 = Label(root, text="Hello World!")
    label2 = Label(root, text="My name is John")
    # label1.pack()

    # grid splits the window into a grid, and positions them on a fixed spot in the grid
    # The positions in the grid are relative. If there are empty columns or rows,
    # they are ignored until something is put in them
    # widgets can also use the parameters anchor, relief and stretch to stick to positions
    label1.grid(row=0, column=0)
    label2.grid(row=1, column=10)

    click_count = 0

    def my_click1():
        nonlocal click_count
        click_count += 1
        my_label = Label(root, text=f"Button has been\nclicked {click_count} times!")
        my_label.grid(row=2, column=0)

    def my_click2():
        message = e.get()
        my_label = Label(root, text=f"Message: {message}")
        my_label.grid(row=2, column=1)

    # creating Buttons
    # can be associated with a function to be executed when clicked
    # fg and bg represent the foreground and background colors respectively. Can be defined with hex color codes
    # use the syntax lambda: func(args) to pass arguments to the function, through the command= parameter
    button1 = Button(root, text="Click Me!", pady=10, command=my_click1, fg="yellow", bg="red")
    button1.grid(row=1, column=0)
    button2 = Button(root, text="Click Me!", pady=10, command=my_click2, fg="yellow", bg="blue")
    button2.grid(row=1, column=1)

    # input forms are called Entry widgets
    # they can also take the parameters fg and bg like buttons
    # can also set a hint text
    e = Entry(width=50)
    e.grid(row=0, column=1)
    e.insert(0, "Hint Text")

    # Images can be inserted using the PIL library, then put the image into a widget such as a Label
    # only png and gif are accepted
    img = ImageTk.PhotoImage(Image.open("icon.png"))
    Label(root, image=img).grid(row=4, column=0)

    # the function root.quit closes the program
    Button(root, text="Exit", pady=10, command=root.quit, fg="white", bg="black").grid(row=4, column=1)

    # frames can be used to highlight an object within the window. It's like a window within a window.
    frame = LabelFrame(root, text="Label frame", padx=5, pady=5)
    frame.grid(row=3, column=2)
    button_frame = Button(frame, text="Frame Button")
    button_frame.pack()

    # radio buttons are those buttons in multiple choice forms where you can only choose one option
    # IntVar can be used to store the value set by the options. Could also be StrVar for strings, or other types
    # you can also use loops to create buttons
    def clicked_radio(value):
        my_label = Label(frame, text=value)
        frame.pack_forget()
        my_label.pack()
    r = IntVar()
    r.set(2)
    for index in range(1, 11):
        radio_button = Radiobutton(
            frame,
            text=f"Option {index}",
            variable=r,
            value=index,
            command=lambda: clicked_radio(r.get())
        )
        radio_button.pack()

    # checkboxes are similar to radio buttons, but they are multiple choice.
    # .deselect() turns the button off, so it's deselected by default
    check_button = Checkbutton(
        frame,
        text=f"Choice",
        variable=r,
        onvalue=11,
        offvalue=0,
        command=lambda: clicked_radio(r.get())
    )
    check_button.deselect()
    check_button.pack()

    # you can also use the messagebox to show a popup.
    # Remember to import messagebox separately: from tkinter import messagebox; regardless of the general import
    # there example below shows an error message, but there are other kinds of popup windows to choose from.
    def show_popup():
        messagebox.showerror("Popup message", "You clicked the popup button")

    Button(frame, text="Popup", command=show_popup).pack()

    # opening new windows:
    # this of course can be called from buttons, and behaves just like a regular widget.
    # top.destroy closes it
    top = Toplevel()
    Label(top, text="Second Window").pack()
    Button(top, text="close", command=top.destroy).pack()

    # Opening file dialog window: from tkinter import filedialog
    # initial directory is the directory where the window will open
    # file_types are the allowed file types
    # the window then returns the path to the selected file. The actual access to it should be done separately.
    initial_directory = "/Documentos/Tutorials/tkinter-interface"
    file_types = (("png files", "*.png"), ("all files", "*.*"))
    title = "Select a file"
    root.filename = filedialog.askopenfilename(initialdir=initial_directory, title=title, filetypes=file_types)
    Label(root, text=root.filename).grid(row=4, column=2)

    # sliders are continuous scales:
    # you can use the method .get() to get the value on the scale at any given time
    # you can also use the command parameter to apply a function in real time as the scale slides
    def slider(var):
        Label(frame, text=var).pack()
    scale = Scale(frame, from_=0, to=200, orient=HORIZONTAL, command=slider)
    scale.pack()

    # displays the window on the screen, looping for scanning updates such as mouse position and typed characters
    root.mainloop()


if __name__ == '__main__':
    main()
