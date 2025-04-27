# فایل: pages/student_management.py

import customtkinter as ctk
from tkinter import messagebox

class StudentManagementPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True)

        # عنوان صفحه
        title_label = ctk.CTkLabel(self, text="مدیریت دانش‌آموزان", font=("B Nazanin", 24))
        title_label.pack(pady=20)

        # دکمه‌های بالای صفحه
        top_frame = ctk.CTkFrame(self)
        top_frame.pack(pady=10)

        add_button = ctk.CTkButton(top_frame, text="افزودن دانش‌آموز", command=self.add_student)
        add_button.pack(side="right", padx=10)

        search_entry = ctk.CTkEntry(top_frame, placeholder_text="جستجو بر اساس نام یا کدملی...")
        search_entry.pack(side="right", padx=10)
        search_entry.bind("<Return>", lambda event: self.search_student(search_entry.get()))

        # جدول نمایش دانش‌آموزان
        self.student_table = ctk.CTkScrollableFrame(self)
        self.student_table.pack(pady=20, fill="both", expand=True)

        self.students = []  # لیست دانش‌آموزان به صورت موقت
        self.refresh_student_table()

    def add_student(self):
        # تابع افزودن دانش‌آموز (بعداً فرم جداگانه می‌سازیم)
        messagebox.showinfo("افزودن دانش‌آموز", "فرم افزودن دانش‌آموز در حال توسعه است...")

    def search_student(self, query):
        # تابع جستجوی دانش‌آموز
        messagebox.showinfo("جستجو", f"دنبال {query} گشتیم! (تابع در حال توسعه...)")

    def refresh_student_table(self):
        # پاک کردن قبلی
        for widget in self.student_table.winfo_children():
            widget.destroy()

        # ساخت جدول ساده
        for student in self.students:
            label = ctk.CTkLabel(self.student_table, text=f"{student['name']} - {student['national_id']}")
            label.pack(pady=5)

