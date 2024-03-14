import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from stack import Stack

button_names = ["Push", "Pop", "Peek", "Size", "Exit"]
def main():
    root =tk.Tk()
    root.geometry("500x500")
    root.title("Abstract Data Structure")
    h1 = tkFont.Font(family="Verdana", size=20, weight="bold")
    p = tkFont.Font(family="Verdana", size=16)
    b = tkFont.Font(family="Verdana", size=16, weight="bold")

    stack = Stack()

    header = tk.Label(root, text="Enter your item", font=h1)
    header.pack(pady=10)

    item = tk.Entry(root, font=p, width=20)
    item.pack(pady=10)

    for i in button_names:
        button = tk.Button(root, text=i, font=b, bg="black", fg="white", width=15)
        if i == button_names[0]:
            button.config(command=lambda: push_item())
        elif i == button_names[1]:
            button.config(command=lambda: pop_item())
        elif i == button_names[2]:
            button.config(command=lambda: peek_item())
        elif i == button_names[3]:
            button.config(command=lambda: size())
        elif i == button_names[4]:
            button.config(command=lambda: exit_program())

        button.pack(pady=10)

    def push_item():
        value = item.get()
        if value != "":
            stack.push(value)
        else:
            messagebox.showwarning("Empty Field", "Please enter an item to push.")

    def pop_item():
        stack.pop()

    def peek_item():
        stack.peek()

    def size():
        stack.size()

    def exit_program():
        root.destroy()

    root.mainloop()

if __name__ == "__main__":
    main()


