import tkinter as tk

root = tk.Tk()
root.title("display")
root.geometry("300x300")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="click me", command=lambda: entry.insert(0, "hello"))
button.pack()
botton = tk.Button(root, text="clear", command=lambda:entry.delete(0, tk.END))
botton.pack()

Label = tk.Label(root, text="enter your name")
Label.pack()

Label = tk.Label(root, text="shivam kashyap")
Label.pack()


root.mainloop()