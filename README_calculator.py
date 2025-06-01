import tkinter as tk

def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(expression))
            entry.set(result)
            expression = result
        except Exception:
            entry.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        entry.set("")
    else:
        expression += text
        entry.set(expression)

def toggle_mode():
    global dark_mode
    dark_mode = not dark_mode
    apply_theme()

def apply_theme():
    bg = "#121212" if dark_mode else "#ffffff"
    fg = "#ffffff" if dark_mode else "#000000"
    btn_bg = "#1f1f1f" if dark_mode else "#f0f0f0"
    
    root.config(bg=bg)
    entry_field.config(bg=bg, fg=fg, insertbackground=fg)
    for button in buttons:
        button.config(bg=btn_bg, fg=fg, activebackground=bg)
    toggle_btn.config(bg=btn_bg, fg=fg, activebackground=bg)

# Setup
root = tk.Tk()
root.geometry("400x600")
root.title("Calculator with Dark Mode")

expression = ""
entry = tk.StringVar()
dark_mode = False

entry_field = tk.Entry(root, textvar=entry, font="Arial 24", bd=10, relief=tk.SUNKEN, justify='right')
entry_field.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

btns = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

buttons = []
for row in btns:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        b = tk.Button(frame, text=btn, font="Arial 20")
        b.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        b.bind("<Button-1>", click)
        buttons.append(b)

toggle_btn = tk.Button(root, text="Toggle Dark Mode", command=toggle_mode, font="Arial 14")
toggle_btn.pack(pady=10)

apply_theme()
root.mainloop()
