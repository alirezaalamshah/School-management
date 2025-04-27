import customtkinter as ctk

class DashboardPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # تیتر اصلی داشبورد
        self.title_label = ctk.CTkLabel(self, text="داشبورد", font=("IRANSans", 24, "bold"))
        self.title_label.pack(pady=(20,10))

        # خوش‌آمدگویی
        self.welcome_label = ctk.CTkLabel(self, text="به نرم افزار مدیریت هنرستان خوش آمدید", font=("IRANSans", 18))
        self.welcome_label.pack(pady=(10,30))

        # اطلاعات آماری نمونه (بعداً به دیتابیس وصل می‌کنیم)
        self.stats_frame = ctk.CTkFrame(self, corner_radius=10)
        self.stats_frame.pack(pady=10, padx=20, fill="x")

        # کارت‌های آماری
        self.major_count = ctk.CTkLabel(self.stats_frame, text="تعداد رشته‌ها: 0", font=("IRANSans", 16))
        self.major_count.grid(row=0, column=0, padx=20, pady=20)

        self.student_count = ctk.CTkLabel(self.stats_frame, text="تعداد دانش‌آموزان: 0", font=("IRANSans", 16))
        self.student_count.grid(row=0, column=1, padx=20, pady=20)

        self.classes_count = ctk.CTkLabel(self.stats_frame, text="تعداد کلاس‌ها: 0", font=("IRANSans", 16))
        self.classes_count.grid(row=0, column=2, padx=20, pady=20)



