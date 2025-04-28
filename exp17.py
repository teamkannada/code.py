import tkinter as tk
win =tk.Tk()
win.title("simple GUI")
win.geometry("300x200")
def show_text():
    label.config(text="hello Pyhton",fg="blue",font=("arial black",16,"bold"))

label=tk.Label(win,fg="green",font=("Arial black",14))
label.pack(pady=20)
btn=tk.Button(win,text="click me",bg="orange",fg="white",font=("arial black",12),command=show_text)
btn.pack()
win.mainloop()
                                                