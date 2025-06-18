import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox
import string
import random

class Password:
    """Create Password Class"""
    def __init__(self, pass_len):
        self.pass_len = pass_len
        self.special = '!@#$%^&*()_+-?'

    def create_pass(self):
        """Creates Password"""
        t = random.choices(string.ascii_letters + string.digits + self.special, k=self.pass_len)
        return (''.join(t))
    
def generate_pass():
    output.delete(0, tk.END)

    try:
        pass_length = int(entry1.get())
        number_of_pass = int(entry2.get())

        if pass_length < 4 or pass_length > 128:
            messagebox.showinfo("Invalid Input", "Please enter a length between 4 and 128!")
            entry1.delete(0, tk.END)
            entry2.delete(0, tk.END)

        else:
            generate_pass = []

            for i in range(1,number_of_pass+1):
                password = Password(pass_length)
                password = password.create_pass()
                generate_pass.append(password)
                output.insert(tk.END, f"{i}. {password}")
            entry1.delete(0, tk.END)

    except ValueError:
        messagebox.showinfo("Invalid Input", "Please enter a NUMBER between 4 and 128!")
        clear_box()

def clear_box():
    entry1.delete(0, tk.END)
    output.delete(0,tk.END)

def save_file():
    file = fd.asksaveasfile(initialdir="C:/Users/sheha/Downloads",
                            defaultextension=".txt", 
                            filetypes=[("Text file",".txt"), ("All files", ".*")],
                            mode="w")
    paswd = output.get(0, tk.END)
    for password in paswd:
        file.write(password + '\n')
    file.close()

root = tk.Tk()
root.title("Password Generator")
root.geometry("500x400")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = tk.Frame(root, padx=20, pady=20)
frame.grid(sticky="nsew")

# Configure columns to stretch
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=2)
frame.columnconfigure(2, weight=1)

header = tk.Label(frame, text="Password Generator", font=("Arial", 16, "bold"))
header.grid(row=0, column=0, columnspan=3, pady=(0, 20))

lbl1 = tk.Label(frame, text="Password Length:")
lbl1.grid(row=1, column=0, sticky="e", pady=5)

entry1 = tk.Entry(frame)
entry1.grid(row=1, column=1, sticky="ew", pady=5)

lbl2 = tk.Label(frame, text="Passwords to Generate:")
lbl2.grid(row=2, column=0, sticky="e", pady=5)

entry2 = tk.Entry(frame)
entry2.insert(0,"1")
entry2.grid(row=2, column=1, sticky="ew", pady=5)

gen_btn = tk.Button(frame, text="Generate", command=generate_pass)
gen_btn.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

clear_btn = tk.Button(frame, text="Clear", command=clear_box)
clear_btn.grid(row=3, column=2, columnspan=2, pady=10, sticky="ew")

output = tk.Listbox(frame)
output.grid(row=4, column=0, columnspan=3, sticky="nsew", pady=10)

save_btn = tk.Button(frame, text="Save", command=save_file)
save_btn.grid(row=5, column=0, columnspan=3, sticky="nsew", pady=(0,20))

tk.mainloop()
