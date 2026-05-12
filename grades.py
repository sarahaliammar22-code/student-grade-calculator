import tkinter as tk
from tkinter import messagebox
import webbrowser  # مكتبة أساسية لفتح الروابط في المتصفح

def calculate():
    try:
        # سحب درجات المواد الثلاثة
        m1 = float(entry1.get())
        m2 = float(entry2.get())
        m3 = float(entry3.get())
        
        # حساب المجموع الكلي والنسبة المئوية
        total = m1 + m2 + m3
        perc = (total / 300) * 100
        
        # تحديد التقدير بناءً على النسبة
        if perc >= 90: grade = "امتياز 🌟"
        elif perc >= 80: grade = "جيد جداً ✅"
        elif perc >= 65: grade = "جيد 🆗"
        elif perc >= 50: grade = "مقبول ⚠️"
        else: grade = "راسب ❌"
        
        # إظهار رسالة النتيجة للمستخدم
        messagebox.showinfo("النتيجة النهائية", f"المجموع: {total} من 300\nالنسبة: {perc:.1f}%\nالتقدير: {grade}")
    except ValueError:
        # إظهار رسالة خطأ في حال إدخال نصوص بدلاً من أرقام
        messagebox.showerror("خطأ في الإدخال", "برجاء كتابة أرقام صحيحة في خانات المواد!")

# دالة فتح رابط المشروع الخاص بكِ على GitHub
def open_github():
    webbrowser.open("https://github.com/sarahaliammar22-code/student-grade-calculator")

# إعداد النافذة الرئيسية للبرنامج (GUI)
app = tk.Tk()
app.title("حاسبة التقديرات")
app.geometry("320x400")
app.configure(bg="#f5f5f5") # لون خلفية رمادي فاتح مريح للعين

# واجهة إدخال البيانات (العناوين وخانات الكتابة)
tk.Label(app, text="درجة المادة الأولى:", bg="#f5f5f5", font=("Arial", 10, "bold")).pack(pady=5)
entry1 = tk.Entry(app, font=("Arial", 10), justify="center")
entry1.pack()

tk.Label(app, text="درجة المادة الثانية:", bg="#f5f5f5", font=("Arial", 10, "bold")).pack(pady=5)
entry2 = tk.Entry(app, font=("Arial", 10), justify="center")
entry2.pack()

tk.Label(app, text="درجة المادة الثالثة:", bg="#f5f5f5", font=("Arial", 10, "bold")).pack(pady=5)
entry3 = tk.Entry(app, font=("Arial", 10), justify="center")
entry3.pack()

# زر حساب النتيجة والتقدير
tk.Button(app, text="احسب النتيجة والتقدير", command=calculate, bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), cursor="hand2").pack(pady=20)

# زر الانتقال إلى حساب GitHub الخاص بكِ
tk.Button(app, text="🌐 عرض المشروع على GitHub", command=open_github, bg="#24292e", fg="white", font=("Arial", 10, "bold"), cursor="hand2").pack(pady=10)

# تشغيل نافذة البرنامج واستمرارها في استقبال الأوامر
app.mainloop()
