import customtkinter as ctk

class ReportGenerationPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label = ctk.CTkLabel(self, text="گزارش‌گیری", font=("B Nazanin", 24))
        self.label.pack(pady=20)

        # انتخاب رشته
        self.major_optionmenu = ctk.CTkOptionMenu(self, values=["رشته ۱", "رشته ۲"])
        self.major_optionmenu.pack(pady=10)

        # انتخاب کلاس
        self.class_optionmenu = ctk.CTkOptionMenu(self, values=["کلاس ۱", "کلاس ۲"])
        self.class_optionmenu.pack(pady=10)

        # انتخاب درس
        self.lesson_optionmenu = ctk.CTkOptionMenu(self, values=["همه دروس", "ریاضی", "فیزیک"])
        self.lesson_optionmenu.pack(pady=10)

        # دکمه تولید گزارش
        self.generate_report_button = ctk.CTkButton(self, text="📋 تولید گزارش", command=self.generate_report)
        self.generate_report_button.pack(pady=10)

        # جایی برای نمایش گزارش
        self.report_frame = ctk.CTkFrame(self)
        self.report_frame.pack(pady=20, expand=True, fill="both")

        # دکمه ذخیره خروجی
        self.save_button = ctk.CTkButton(self, text="💾 ذخیره خروجی", command=self.save_report)
        self.save_button.pack(pady=10)

    def generate_report(self):
        # بعداً دیتا را از دیتابیس میاریم و نمایش میدیم
        print("گزارش تولید شد")

    def save_report(self):
        # بعداً گزارش رو تو فایل ذخیره میکنیم
        print("گزارش ذخیره شد")
