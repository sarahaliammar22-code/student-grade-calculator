import tkinter as tk
from tkinter import messagebox
import webbrowser

def calculate_gpa(perc):
    # دالة فرعية لحساب الـ GPA التراكمي من 4.0 بناءً على النسبة
    if perc >= 90: return 4.0
    elif perc >= 85: return 3.7
    elif perc >= 80: return 3.3
    elif perc >= 75: return 3.0
    elif perc >= 70: return 2.7
    elif perc >= 65: return 2.4
    elif perc >= 60: return 2.0
    elif perc >= 50: return 1.0
    else: return 0.0

def calculate():
    try:
        # 1. سحب درجات الـ 5 مواد من الخانات
        grades = [
            float(entry1.get()),
            float(entry2.get()),
            float(entry3.get()),
            float(entry4.get()),
            float(entry5.get())
        ]
        
        # التأكد أن الدرجات منطقية (بين 0 و 100)
        for g in grades:
            if g < 0 or g > 100:
                messagebox.showerror("خطأ في القيمة", "الدرجات يجب أن تكون بين 0 و 100!")
                return
        
        # 2. العمليات الحسابية
        total = sum(grades)
        perc = (total / 500) * 100  # المجموع الكلي من 500
        gpa = calculate_gpa(perc)
        
        # 3. تحديد التقدير العام
        if perc >= 90: grade = "امتياز 🌟"
        elif perc >= 80: grade = "جيد جداً ✅"
        elif perc >= 65: grade = "جيد 🆗"
        elif perc >= 50: grade = "مقبول ⚠️"
        else: grade = "راسب ❌"
        
        # 4. عرض النتيجة بشكل منسق ومفصل
        result_text = (
            f"📊 النتيجة الكلية:\n\n"
            f"🔹 المجموع: {total} / 500\n"
            f"🔹 النسبة المئوية: {perc:.2f}%\n"
            f"🔹 المعدل التراكمي (GPA): {gpa:.2f} / 4.0\n"
            f"🔹 التقدير العام: {grade}"
        )
        messagebox.showinfo("التقرير الدراسي المطور", result_text)
        
    except ValueError:
        messagebox.showerror("خطأ في الإدخال", "برجاء التأكد من كتابة أرقام صحيحة في جميع الخانات!")

def open_github():
    webbrowser.open("github.com")

# --- تصميم واجهة المستخدم الحديثة ---
app = tk.Tk()
app.title("نظام حساب المعدلات الذكي")
app.geometry("360x520")
app.configure(bg="#2c3e50") # خلفية داكنة واحترافية (Dark Slate)

# عنوان رئيسي علوي للبرنامج
title_label = tk.Label(app, text="🎓 حاسبة الدرجات والمعدل الدراسي", bg="#2c3e50", fg="#ecf0f1", font=("Arial", 12, "bold"))
title_label.pack(pady=15)

# دالة مساعدة لإنشاء العناوين وخانات الإدخال بتنسيق ثابت ومتناسق
def create_input_field(label_text):
    lbl = tk.Label(app, text=label_text, bg="#2c3e50", fg="#bdc3c7", font=("Arial", 10, "bold"))
    lbl.pack(pady=2)
    entry = tk.Entry(app, font=("Arial", 11), justify="center", bd=2, width=15)
    entry.pack(pady=2)
    return entry

# توليد خانات الإدخال للمواد الخمسة
entry1 = create_input_field("درجة المادة الأولى:")
entry2 = create_input_field("درجة المادة الثانية:")
entry3 = create_input_field("درجة المادة الثالثة:")
entry4 = create_input_field("درجة المادة الرابعة:")
entry5 = create_input_field("درجة المادة الخامسة:")

# زر الحساب المطور بألوان متناسقة وحجم أوضح
btn_calc = tk.Button(app, text="⚙️ احسب المعدل والتقرير", command=calculate, bg="#27ae60", fg="white", font=("Arial", 11, "bold"), width=22, cursor="hand2", bd=0)
btn_calc.pack(pady=20)

# زر الجيت هاب في الأسفل بشكل أنيق
btn_git = tk.Button(app, text="🌐 تابع المشروع على GitHub", command=open_github, bg="#34495e", fg="#ecf0f1", font=("Arial", 9, "bold"), width=25, cursor="hand2", bd=0)
btn_git.pack(pady=5)

app.mainloop()

