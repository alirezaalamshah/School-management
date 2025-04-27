import customtkinter as ctk

class ScoreRegistrationPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label = ctk.CTkLabel(self, text="ثبت نمرات", font=("B Nazanin", 24))
        self.label.pack(pady=20)

        # انتخاب رشته
        self.major_optionmenu = ctk.CTkOptionMenu(self, values=["رشته ۱", "رشته ۲"])
        self.major_optionmenu.pack(pady=10)

        # انتخاب کلاس
        self.class_optionmenu = ctk.CTkOptionMenu(self, values=["کلاس ۱", "کلاس ۲"])
        self.class_optionmenu.pack(pady=10)

        # انتخاب درس
        self.lesson_optionmenu = ctk.CTkOptionMenu(self, values=["درس ۱", "درس ۲"])
        self.lesson_optionmenu.pack(pady=10)

        # دکمه بارگذاری لیست دانش‌آموزان
        self.load_students_button = ctk.CTkButton(self, text="📋 بارگذاری دانش‌آموزان", command=self.load_students)
        self.load_students_button.pack(pady=10)

        # جایی برای لیست دانش‌آموزان (بعداً جدول میسازیم)
        self.students_frame = ctk.CTkFrame(self)
        self.students_frame.pack(pady=20, expand=True, fill="both")

        # دکمه ذخیره نمرات
        self.save_scores_button = ctk.CTkButton(self, text="💾 ذخیره نمرات", command=self.save_scores)
        self.save_scores_button.pack(pady=10)

    def load_students(self):
        # بعداً لیست دانش‌آموزان رو از دیتابیس بارگذاری میکنیم
        print("لیست دانش‌آموزان بارگذاری شد")

    def save_scores(self):
        # بعداً نمرات ذخیره میشه
        print("نمرات ذخیره شد")
