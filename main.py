import customtkinter as ctk
from pages.major_management import MajorManagementPage
from pages.dashboard import DashboardPage
from pages.class_management import ClassManagementPage
from pages.student_management import StudentManagementPage
from pages.teacher_management import TeacherManagementPage
from pages.lesson_management import LessonManagementPage
from pages.score_registration import ScoreRegistrationPage
from pages.report_generation import ReportGenerationPage
from pages.attendance_management import AttendanceManagementPage

# تنظیمات اولیه
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("green")

# ساخت پنجره اصلی
app = ctk.CTk()
app.geometry("1000x600")
app.minsize(1000,600)
app.title("نرم افزار مدیریت هنرستان")

# ساخت سایدبار و فریم اصلی محتوا
sidebar_frame = ctk.CTkFrame(master=app, width=200, corner_radius=10)
sidebar_frame.grid(row=0, column=1, sticky="ns", padx=10, pady=10)  # استفاده از grid

content_frame = ctk.CTkFrame(master=app, corner_radius=10)
content_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# تنظیم کشسانی برای تغییر اندازه
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

# تابع تغییر حالت روشن/تاریک
def toggle_appearance_mode():
    current_mode = ctk.get_appearance_mode()
    new_mode = "Dark" if current_mode == "Light" else "Light"
    ctk.set_appearance_mode(new_mode)
    appearance_switch.configure(text=f"حالت: {new_mode}")

# تابع پاک کردن محتوای صفحه
def clear_content():
    for widget in content_frame.winfo_children():
        widget.destroy()

# توابع باز کردن صفحات
def open_dashboard():
    clear_content()
    page = DashboardPage(content_frame)
    page.pack(fill="both", expand=True)

def open_major_management():
    clear_content()
    page = MajorManagementPage(content_frame)
    page.pack(fill="both", expand=True)

def open_class_management():
    clear_content()
    page = ClassManagementPage(content_frame)
    page.pack(fill="both", expand=True)

def open_student_management():
    clear_content()
    page = StudentManagementPage(content_frame)
    page.pack(fill="both", expand=True)

def open_teacher_management():
    clear_content()
    page = TeacherManagementPage(content_frame)
    page.pack(fill="both", expand=True)

def open_lesson_management():
    clear_content()
    page = LessonManagementPage(content_frame)
    page.pack(fill="both", expand=True)

def open_score_registration():
    clear_content()
    page = ScoreRegistrationPage(content_frame)
    page.pack(fill="both", expand=True)

def open_report_generation():
    clear_content()
    page = ReportGenerationPage(content_frame)
    page.pack(fill="both", expand=True)

def Attendance_Management():
    clear_content()
    page = AttendanceManagementPage(content_frame)
    page.pack(fill="both", expand=True)


# تابع خروج
def exit_app():
    app.destroy()

# سوییچ تغییر حالت روشن/تاریک
appearance_switch = ctk.CTkSwitch(
    master=sidebar_frame,
    text="حالت: Light",
    command=toggle_appearance_mode,
    width=180
)
appearance_switch.pack(pady=(10, 5), padx=10)

# ساخت دکمه‌های سایدبار
buttons = [
    ("داشبورد", open_dashboard),
    ("مدیریت رشته‌ها", open_major_management),
    ("مدیریت کلاس‌ها", open_class_management),
    ("مدیریت دانش‌آموزان", open_student_management),
    ("مدیریت پرسنل", open_teacher_management),
    ("مدیریت دروس", open_lesson_management),
    ("مدیریت نمرات", open_score_registration),
    ("گزارشات", open_report_generation),
    ("حضور غیاب", Attendance_Management)
]

for text, command in buttons:
    btn = ctk.CTkButton(
        master=sidebar_frame, 
        text=text, 
        width=180, 
        height=40, 
        corner_radius=8, 
        command=command
    )
    btn.pack(pady=5, padx=10)

# دکمه خروج
exit_btn = ctk.CTkButton(
    master=sidebar_frame,
    text="🚪 خروج",
    width=180,
    height=40,
    corner_radius=8,
    fg_color="red",
    hover_color="#cc0000",
    command=exit_app
)
exit_btn.pack(pady=(20, 5), padx=10)

# اجرای برنامه
open_dashboard()  # اولین صفحه داشبورد باز شود
app.mainloop()