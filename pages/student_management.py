# student_management.py
import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

class StudentManagementPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        self.students = []
        
        # تنظیمات ظاهری پیشرفته
        self.configure(fg_color="#F5F5F5")
        self.grid_columnconfigure(0, weight=1)
        
        # عنوان صفحه
        title_frame = ctk.CTkFrame(self, fg_color="transparent")
        title_frame.pack(pady=15, fill="x")
        
        ctk.CTkLabel(
            title_frame,
            text="سیستم مدیریت دانش آموزان",
            font=("B Titr", 20, "bold"),
            text_color="#2C3E50"
        ).pack(side="right", padx=20)

        # نوار ابزار
        self.toolbar_frame = ctk.CTkFrame(self, fg_color="transparent", height=40)
        self.toolbar_frame.pack(fill="x", padx=20, pady=5)
        self.create_toolbar()

        # بدنه اصلی
        self.content_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        self.show_list_view()

    def create_toolbar(self):
        # پاک کردن ابزارهای قبلی
        for widget in self.toolbar_frame.winfo_children():
            widget.destroy()

        # دکمه‌ها و فیلد جستجو
        self.search_entry = ctk.CTkEntry(
            self.toolbar_frame,
            placeholder_text="جستجو بر اساس نام، نام خانوادگی یا کد ملی...",
            font=("B Nazanin", 13),
            width=300,
            height=32,
            border_width=1,
            corner_radius=6
        )
        self.search_entry.pack(side="right", padx=10)
        self.search_entry.bind("<Return>", lambda e: self.search_student())

        ctk.CTkButton(
            self.toolbar_frame,
            text="➕ افزودن دانش آموز",
            fg_color="#2E86C1",
            hover_color="#2874A6",
            font=("B Nazanin", 13),
            height=32,
            width=150,
            command=self.show_form_view
        ).pack(side="right", padx=5)

    def show_list_view(self):
        # پاک کردن محتوای قبلی
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # ایجاد جدول
        table_container = ctk.CTkFrame(self.content_frame, fg_color="white")
        table_container.pack(fill="both", expand=True)

        # هدرهای جدول
        headers = ["ردیف", "نام", "نام خانوادگی", "کد ملی", "تاریخ تولد", "کلاس", "عملیات"]
        self.create_table_row(table_container, headers, is_header=True)

        # داده‌های دانش آموزان
        for idx, student in enumerate(self.students, 1):
            row_data = [
                idx,
                student['first_name'],
                student['last_name'],
                student['national_id'],
                student['birth_date'],
                student['class_name'],
                "✏️ 🗑️"
            ]
            self.create_table_row(table_container, row_data)

    def create_table_row(self, parent, data, is_header=False):
        row_frame = ctk.CTkFrame(parent, fg_color="transparent")
        row_frame.pack(fill="x", pady=1)
        
        colors = {
            "bg": "#E8F8F5" if is_header else "white",
            "text": "#2C3E50" if is_header else "#34495E"
        }

        for item in data:
            lbl = ctk.CTkLabel(
                row_frame,
                text=str(item),
                font=("B Nazanin", 13, "bold" if is_header else None),
                width=120,
                height=35,
                fg_color=colors["bg"],
                text_color=colors["text"],
                anchor="center"
            )
            lbl.pack(side="right", padx=1)

    def show_form_view(self):
        # پاک کردن محتوای قبلی
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # قالب اصلی فرم
        form_container = ctk.CTkFrame(self.content_frame, fg_color="white")
        form_container.pack(fill="both", expand=True, padx=10, pady=10)
        form_container.grid_columnconfigure(1, weight=1)

        # بخش اطلاعات هویتی
        ctk.CTkLabel(
            form_container,
            text="مشخصات فردی",
            font=("B Titr", 16),
            text_color="#2C3E50",
            anchor="e"
        ).grid(row=0, column=0, columnspan=2, pady=(10,20), sticky="e")

        # ردیف اول
        self.first_name = self.create_form_field(form_container, "نام:", 1)
        self.last_name = self.create_form_field(form_container, "نام خانوادگی:", 2)
        self.father_name = self.create_form_field(form_container, "نام پدر:", 3)

        # کد ملی و تاریخ تولد
        self.national_id = self.create_form_field(form_container, "کد ملی (10 رقمی):", 4)
        
        # تاریخ تولد
        birth_frame = ctk.CTkFrame(form_container, fg_color="transparent")
        birth_frame.grid(row=5, column=0, columnspan=2, sticky="ew", padx=20, pady=5)
        
        ctk.CTkLabel(birth_frame, text="تاریخ تولد:", font=("B Nazanin", 13)).pack(side="right", padx=5)
        
        # سال
        self.year_combo = ctk.CTkComboBox(
            birth_frame,
            values=[str(y) for y in range(1380, 1405)],
            width=90,
            height=32,
            font=("B Nazanin", 12),
            dropdown_font=("B Nazanin", 12)
        )
        self.year_combo.pack(side="right", padx=5)
        
        # ماه
        self.month_combo = ctk.CTkComboBox(
            birth_frame,
            values=[f"{m:02d} - {self.persian_month(m)}" for m in range(1, 13)],
            width=110,
            height=32,
            font=("B Nazanin", 12)
        )
        self.month_combo.pack(side="right", padx=5)
        
        # روز
        self.day_combo = ctk.CTkComboBox(
            birth_frame,
            values=[f"{d:02d}" for d in range(1,32)],
            width=70,
            height=32,
            font=("B Nazanin", 12)
        )
        self.day_combo.pack(side="right", padx=5)

        # بخش اطلاعات تماس
        ctk.CTkLabel(
            form_container,
            text="اطلاعات تماس",
            font=("B Titr", 16),
            text_color="#2C3E50",
            anchor="e"
        ).grid(row=6, column=0, columnspan=2, pady=(30,20), sticky="e")

        # فیلدهای تماس
        self.student_mobile = self.create_form_field(form_container, "موبایل دانش آموز:", 7)
        self.father_mobile = self.create_form_field(form_container, "موبایل پدر:", 8)
        self.father_work = self.create_form_field(form_container, "تلفن محل کار پدر:", 9)
        self.mother_mobile = self.create_form_field(form_container, "موبایل مادر:", 10)
        self.mother_work = self.create_form_field(form_container, "تلفن محل کار مادر:", 11)
        self.home_phone = self.create_form_field(form_container, "تلفن منزل:", 12)

        # آدرس
        ctk.CTkLabel(
            form_container,
            text="آدرس دقیق:",
            font=("B Nazanin", 13),
            anchor="e"
        ).grid(row=13, column=0, padx=(20,5), pady=10, sticky="e")
        
        self.address_entry = ctk.CTkTextbox(
            form_container,
            font=("B Nazanin", 13),
            height=80,
            border_width=1,
            corner_radius=4
        )
        self.address_entry.grid(row=13, column=1, padx=(0,20), pady=10, sticky="ew")

        # دکمه‌های پایین فرم
        btn_frame = ctk.CTkFrame(form_container, fg_color="transparent")
        btn_frame.grid(row=14, column=0, columnspan=2, pady=20)

        ctk.CTkButton(
            btn_frame,
            text="💾 ذخیره اطلاعات",
            fg_color="#27AE60",
            hover_color="#219A52",
            font=("B Nazanin", 14),
            width=140,
            height=36,
            command=self.save_student
        ).pack(side="right", padx=15)

        ctk.CTkButton(
            btn_frame,
            text="❌ انصراف",
            fg_color="#E74C3C",
            hover_color="#C0392B",
            font=("B Nazanin", 14),
            width=140,
            height=36,
            command=self.show_list_view
        ).pack(side="left", padx=15)

    def create_form_field(self, parent, label_text, row):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.grid(row=row, column=0, columnspan=2, sticky="ew", padx=20, pady=5)
        
        ctk.CTkLabel(
            frame,
            text=label_text,
            font=("B Nazanin", 13),
            width=140,
            anchor="e"
        ).pack(side="right", padx=5)
        
        entry = ctk.CTkEntry(
            frame,
            font=("B Nazanin", 13),
            height=32,
            border_width=1,
            corner_radius=4
        )
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def persian_month(self, month_num):
        months = [
            "", "فروردین", "اردیبهشت", "خرداد", 
            "تیر", "مرداد", "شهریور", 
            "مهر", "آبان", "آذر", 
            "دی", "بهمن", "اسفند"
        ]
        return months[month_num]

    def validate_inputs(self):
        # اعتبارسنجی فیلدهای الزامی
        required_fields = {
            self.first_name: "نام",
            self.last_name: "نام خانوادگی",
            self.father_name: "نام پدر",
            self.national_id: "کد ملی"
        }
        
        for field, name in required_fields.items():
            if not field.get().strip():
                messagebox.showerror("خطا", f"فیلد {name} الزامی است!")
                return False

        # اعتبارسنجی کدملی
        national_id = self.national_id.get().strip()
        if len(national_id) != 10 or not national_id.isdigit():
            messagebox.showerror("خطا", "کدملی باید 10 رقم عددی باشد!")
            return False

        # اعتبارسنجی تاریخ تولد
        try:
            # استخراج عدد ماه از مقدار Combobox
            month_number = self.month_combo.get().split(" - ")[0]
            date_str = f"{self.year_combo.get()}-{month_number}-{self.day_combo.get()}"
            datetime.strptime(date_str, "%Y-%m-%d")
        except (ValueError, IndexError):
            messagebox.showerror("خطا", "تاریخ وارد شده نامعتبر است!")
            return False

    def save_student(self):
        if not self.validate_inputs():
            return

        student_data = {
            'first_name': self.first_name.get().strip(),
            'last_name': self.last_name.get().strip(),
            'father_name': self.father_name.get().strip(),
            'national_id': self.national_id.get().strip(),
            'birth_date': f"{self.year_combo.get()}-{self.month_combo.get().split('-')[0]}-{self.day_combo.get()}",
            'student_mobile': self.student_mobile.get().strip(),
            'father_mobile': self.father_mobile.get().strip(),
            'father_work': self.father_work.get().strip(),
            'mother_mobile': self.mother_mobile.get().strip(),
            'mother_work': self.mother_work.get().strip(),
            'home_phone': self.home_phone.get().strip(),
            'address': self.address_entry.get("1.0", "end").strip(),
            'class_name': "پایه دهم"  # جایگزین با سیستم واقعی
        }

        self.students.append(student_data)
        messagebox.showinfo("موفقیت", "اطلاعات دانش آموز با موفقیت ثبت شد!")
        self.show_list_view()

    def search_student(self):
        query = self.search_entry.get().strip().lower()
        filtered = [
            s for s in self.students
            if query in s['first_name'].lower() or
            query in s['last_name'].lower() or
            query in s['national_id']
        ]
        self.show_list_view(filtered)