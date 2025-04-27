import customtkinter as ctk
from tkinter import messagebox

class TeacherManagementPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label = ctk.CTkLabel(self, text="مدیریت معلمان", font=("B Nazanin", 24))
        self.label.pack(pady=20)

        # دکمه افزودن معلم
        self.add_teacher_button = ctk.CTkButton(self, text="➕ افزودن معلم", command=self.add_teacher)
        self.add_teacher_button.pack(pady=10)

        # اینجا در آینده جدول معلمان اضافه میشه
        self.teacher_table_placeholder = ctk.CTkLabel(self, text="(اینجا لیست معلمان نمایش داده می‌شود)", font=("B Nazanin", 16))
        self.teacher_table_placeholder.pack(pady=20)

    def add_teacher(self):
        # بعداً فرم اضافه کردن معلم اینجا باز میشه
        messagebox.showinfo("افزودن پرسنل", "فرم افزودن پرسنل در حال توسعه است...")
