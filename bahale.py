import tkinter as tk
import tkinter.messagebox as messagebox
import random

move_count = 0

def move_cancel_button():
    global move_count
    move_count += 1
    if move_count >= 5:
        messagebox.showinfo("Warning", "Please don't hurt yourself!")
        move_count = 0
    else:
        new_x = random.randint(10, 400)
        new_y = random.randint(10, 400)
        cancel_button.place(x=new_x, y=new_y)

def show_second_message():
    messagebox.showinfo("Message", "I agree")

root = tk.Tk()
root.title("Are you dumb?")

header_label = tk.Label(root, text="Are you dumb?")
header_label.pack()

ok_button = tk.Button(root, text="yes,I'm :)", bg="green", fg="#fff", command=show_second_message)
ok_button.pack()

cancel_button = tk.Button(root, text="Not at all", bg="red", fg="#fff")
cancel_button.pack()

cancel_button.bind("<Enter>", lambda e: move_cancel_button())

root.geometry("500x500")  # Set a fixed window size
root.resizable(False, False)  # Disable window resizing

root.mainloop()
