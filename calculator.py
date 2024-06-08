import tkinter as tk

def button_click(event):
    current = entry.get()
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

row = 1
col = 0
for button in buttons:
    btn = tk.Button(root, text=button, font=("Arial", 14), padx=20, pady=20)
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()