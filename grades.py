import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        m1 = float(entry1.get())
        m2 = float(entry2.get())
        m3 = float(entry3.get())
        total = m1 + m2 + m3
        perc = (total / 300) * 100
        if perc >= 90: grade = "امتياز 🌟"
        elif perc >= 80: grade = "جيد جداً ✅"
        elif perc >= 65: grade = "جيد 🆗"
        elif perc >= 50: grade = "مقبول ⚠️"
        else: grade = "راسب ❌"
        messagebox.showinfo("النتيجة", f"المجموع: {total}\nالتقدير: {grade}")
    except:
        messagebox.showerror("خطأ", "ادخل أرقام فقط!")

app = tk.Tk()
app.title("حاسبة الدرجات")
app.geometry("300x300")

tk.Label(app, text="المادة 1:").pack()
entry1 = tk.Entry(app)
entry1.pack()

tk.Label(app, text="المادة 2:").pack()
entry2 = tk.Entry(app)
entry2.pack()

tk.Label(app, text="المادة 3:").pack()
entry3 = tk.Entry(app)
entry3.pack()

tk.Button(app, text="احسب", command=calculate).pack(pady=20)
app.mainloop()
