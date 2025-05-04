# pages/attendance_management.py

import customtkinter as ctk

class AttendanceManagementPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        self.configure(corner_radius=10)

        # عنوان صفحه
        title = ctk.CTkLabel(self, text="مدیریت حضور و غیاب دانش‌آموزان", font=("B Nazanin", 22, "bold"))
        title.pack(pady=10)

        # فیلد جستجو
        self.search_var = ctk.StringVar()
        search_entry = ctk.CTkEntry(self, placeholder_text="جستجوی نام دانش‌آموز...", textvariable=self.search_var)
        search_entry.pack(pady=10, padx=20)
        search_entry.bind("<KeyRelease>", self.filter_students)

        # ✅ اسکرول‌فریم برای نمایش دانش‌آموزان
        self.scrollable_frame = ctk.CTkScrollableFrame(self, height=400)
        self.scrollable_frame.pack(fill="both", expand=True, padx=20, pady=(0, 10))

        # لیست دانش‌آموزان فرضی
        self.students = [
            "علی رضایی", "مریم احمدی", "سینا محمدی", "زهرا یوسفی",
            "نوید شریفی", "سارا موسوی", "محمد کیانی", "هلیا کرمی",
            "نیما رضوانی", "نگار عباسی", "رضا توسلی", "فرناز قربانی"
        ]

        self.attendance_status = {}
        self.student_widgets = {}

        self.display_students(self.students)

        # ✅ دکمه ثبت نهایی - زیر اسکرول‌فریم
        save_btn = ctk.CTkButton(self, text="ثبت وضعیت‌ها", height=40, command=self.submit_attendance)
        save_btn.pack(pady=10)

    def display_students(self, student_list):
        # حذف ویجت‌های قبلی
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        for student in student_list:
            frame = ctk.CTkFrame(self.scrollable_frame)
            frame.pack(fill="x", pady=4)

            name_label = ctk.CTkLabel(frame, text=student, font=("B Nazanin", 18))
            name_label.pack(side="right", padx=10)

            status_var = self.attendance_status.get(student, ctk.StringVar(value="present"))
            self.attendance_status[student] = status_var

            absent_rb = ctk.CTkCheckBox(
                frame, text="غایب", variable=status_var, onvalue="absent", offvalue="present"
            )
            absent_rb.pack(side="left", padx=10)

            self.student_widgets[student] = frame

    def filter_students(self, event=None):
        query = self.search_var.get().strip()
        filtered = [s for s in self.students if query in s]
        self.display_students(filtered)

    def submit_attendance(self):
        for name, status_var in self.attendance_status.items():
            print(f"{name}: {status_var.get()}")
