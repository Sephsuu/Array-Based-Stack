from tkinter import messagebox

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        messagebox.showinfo("Item Added", f"{item} was added successfully!" )

    def pop(self):
        if len(self.stack) != 0:
            self.stack.pop()
            messagebox.showinfo("Deleted", "The last item on stack was deleted successfully!")
        else:
            messagebox.showwarning("Empty Stack", "There was no item to remove from the stack.")

    def peek(self):
        if len(self.stack) != 0:
            messagebox.showinfo("Peek", f"The last item on the stack was \"{self.stack[-1]}\"")
        else:
            messagebox.showwarning("Empty Stack", "There was no item to remove from the stack.")

    def size(self):
        messagebox.showinfo("Size", f"Size of the stack: {len(self.stack)}")


