import tkinter as tk
from tkinter import messagebox

timer_seconds = 0
update_id = None

def start_timer():
    global timer_seconds, update_id
    timer_seconds = int(entry.get())
    update_timer()

def stop_timer():
    global update_id
    if update_id:
        root.after_cancel(update_id)

def update_timer():
    global timer_seconds, update_id
    if timer_seconds > 0:
        timer_seconds -= 1
        label['text'] = f"Залишилося часу: {timer_seconds} sec."
        update_id = root.after(1000, update_timer)
    else:
        messagebox.showinfo("Timer", "Час минув!")
        root.wait_window()

root = tk.Tk()
root.title("Timer")

root.configure(bg='yellow')

label = tk.Label(root, text="Введіть кількість секунд:", font=('Arial', 18), bg='lightblue')
label.pack()

entry = tk.Entry(root, font=('Arial', 14))
entry.pack()

start_button = tk.Button(root, text="Старт", command=start_timer, font=('Arial', 14))
start_button.pack()

stop_button = tk.Button(root, text="Стоп", command=stop_timer, font=('Arial', 14))
stop_button.pack()

bottom_frame = tk.Frame(root, bg='yellow')
bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

root.mainloop()
