import tkinter as tk
def upvalue():
  name = entry.get()
  label2.config(text = f"Hello, {name}!")

#create the main window 
root = tk.Tk()
root.title("GUI")
root.geometry("300x200")

#create and pack label widget
label = tk.Label(root, text="Enter you name")
label.pack(pady=10)

#create and pack entry widget
entry = tk.Entry(root)
entry.pack(pady=5)

#label for upvalue function
label2 = tk.Label(root )
label2.pack()

#create and pack button widget 
button = tk.Button(root, text="submit", command=upvalue)
button.pack(pady=10)

#main loop 
root.mainloop()