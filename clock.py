import tkinter as tk
import time

root = tk.Tk()
root.title("Digital Clock")

def update_time():
    string = time.strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000, update_time)

label = tk.Label(
    root,
    font=('calibri', 40, 'bold'),
    background='purple',
    foreground='white'
)

label.pack(anchor='center')

update_time()
root.mainloop()