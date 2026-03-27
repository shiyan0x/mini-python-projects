import tkinter as tk

def display_details():
  name = entry_name.get()
  roll = entry_roll.get()
  course = entry_course.get()

  result_label.config(text= f"Name : {name}\n Roll Number : {roll}\n Course: {course}")

root=tk.Tk()
root.title("Student Details")
root.geometry("350x300")

tk.Label(root, text="Name").grid(row=0,column=0,padx=10,pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Roll number").grid(row=1,column=0,padx=10,pady=5)
entry_roll = tk.Entry(root)
entry_roll.grid(row=1,column=1)

tk.Label(root, text="course").grid(row=2, column=0, padx=10,pady=5)
entry_course = tk.Entry(root)
entry_course.grid(row=2, column=1)

tk.Button(root, text="submit", command=display_details).grid(row=3,column=1, pady=10)

result_label = tk.Label(root, text="", fg="blue")
result_label.grid(row=4, column=0 , columnspan=2)

root.mainloop()