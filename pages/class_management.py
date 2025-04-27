import customtkinter as ctk

class ClassManagementPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # self.configure(fg_color="#2b2b2b")  # ✅ درست شد

        # --- عنوان صفحه ---
        title_label = ctk.CTkLabel(self, text="مدیریت کلاس‌ها", font=("IRANSans", 24, "bold"))
        title_label.pack(pady=20)

        # --- دکمه اضافه کردن کلاس جدید ---
        add_button = ctk.CTkButton(self, text="افزودن کلاس جدید", command=self.add_class)
        add_button.pack(pady=10)

        # --- لیست کلاس‌های موجود ---
        self.class_listbox = ctk.CTkTextbox(self, width=400, height=300, font=("IRANSans", 16))
        self.class_listbox.pack(pady=20)

        # --- بارگذاری اولیه کلاس‌ها ---
        self.load_classes()

    def load_classes(self):
        sample_classes = ["کلاس ۱۰۱", "کلاس ۱۰۲", "کلاس ۲۰۱", "کلاس ۳۰۱"]

        self.class_listbox.delete("1.0", "end")

        for class_name in sample_classes:
            self.class_listbox.insert("end", f"{class_name}\n")

    def add_class(self):
        self.class_listbox.insert("end", "کلاس جدید\n")
