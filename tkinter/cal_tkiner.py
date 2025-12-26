import tkinter as tk

root = tk.Tk()
root.title("calculator")
root.geometry("300x200")

entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

result = tk.DoubleVar()
result_label = tk.Label(root, textvariable=result)
result_label.pack()

#for adding
def add():
  result.set(float(entry1.get()) + float(entry2.get()))
add_button = tk.Button(root, text="Add", command=add)
add_button.pack()

#for sub.
def sub():
  result.set(float(entry1.get()) - float(entry2.get()))
sub_button = tk.Button(root, text="sub", command=sub)
sub_button.pack()
  
#for mul.
def mul():
  result.set(float(entry1.get()) * float(entry2.get()))
mul_button = tk.Button(root, text="mul", command=mul)
mul_button.pack()
  
#for div.
def div():
  result.set(float(entry1.get()) / float(entry2.get()))
div_button = tk.Button(root, text="div", command=div)
div_button.pack()
  
root.mainloop()