import customtkinter as ctk
from tkinter import messagebox

class LessonManagementPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label = ctk.CTkLabel(self, text="مدیریت دروس", font=("B Nazanin", 24))
        self.label.pack(pady=20)

        # دکمه افزودن درس
        self.add_lesson_button = ctk.CTkButton(self, text="➕ افزودن درس", command=self.add_lesson)
        self.add_lesson_button.pack(pady=10)

        # اینجا در آینده جدول دروس اضافه میشه
        self.lesson_table_placeholder = ctk.CTkLabel(self, text="(اینجا لیست دروس نمایش داده می‌شود)", font=("B Nazanin", 16))
        self.lesson_table_placeholder.pack(pady=20)

    def add_lesson(self):
        # بعداً فرم اضافه کردن درس اینجا باز میشه
        messagebox.showinfo("افزودن دروس", "در حال توسعه")
