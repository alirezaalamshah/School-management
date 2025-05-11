import customtkinter as ctk
from database.student_queries import create_student_table


class StudentManagementPage(ctk.CTkFrame):
    create_student_table() 
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        self.students = []

        self.grid_columnconfigure(0, weight=1)

        # عنوان صفحه
        title_frame = ctk.CTkFrame(self, fg_color="transparent")
        title_frame.pack(pady=15, fill="x")

        ctk.CTkLabel(
            title_frame,
            text="سیستم مدیریت دانش آموزان",
            font=("B Titr", 20, "bold"),
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
        for widget in self.toolbar_frame.winfo_children():
            widget.destroy()

        self.search_entry = ctk.CTkEntry(
            self.toolbar_frame,
            placeholder_text="...جستجو",
            font=("B Nazanin", 20),
            width=300,
            height=32,
            border_width=1,
            corner_radius=6,
            justify="right"
        )
        self.search_entry.pack(side="right", padx=10)

        ctk.CTkButton(
            self.toolbar_frame,
            text="➕ افزودن دانش آموز",
            font=("B Nazanin", 13),
            height=32,
            width=150,
            command=self.show_form_view
        ).pack(side="right", padx=5)

    def show_list_view(self, students=None):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        table_container = ctk.CTkFrame(self.content_frame)
        table_container.pack(fill="both", expand=True, padx=10, pady=10)

        headers = ["ردیف", "نام", "نام خانوادگی", "کد ملی", "تاریخ تولد", "کلاس", "عملیات"]
        self.create_table_row(table_container, headers, is_header=True)

        for idx, student in enumerate(students or self.students, 1):
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

        for item in data:
            lbl = ctk.CTkLabel(
                row_frame,
                text=str(item),
                font=("B Nazanin", 13, "bold" if is_header else None),
                width=120 if not is_header else 140,
                height=40,
                anchor="center",
                corner_radius=6 if is_header else 0
            )
            lbl.pack(side="right", padx=1, fill="x", expand=True)

    def show_form_view(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        form_container = ctk.CTkFrame(self.content_frame)
        form_container.pack(fill="both", expand=True, padx=20, pady=20)

        form_container.grid_columnconfigure((0, 1, 2), weight=1, uniform="form_col")

        ctk.CTkLabel(
            form_container,
            text="فرم ثبت اطلاعات دانش آموز",
            font=("B Titr", 18),
            anchor="center"
        ).grid(row=0, column=0, columnspan=3, pady=(0, 20), sticky="ew")

        self.first_name = self.create_form_field(form_container, "نام دانش آموز", 1, 2)
        self.last_name = self.create_form_field(form_container, "نام خانوادگی", 1, 1)
        self.father_name = self.create_form_field(form_container, "نام پدر", 1, 0)
        self.class_info = self.create_class_info_selector(form_container, 2, 1,columnspan=2)

        self.national_id = self.create_form_field(form_container, "کد ملی (10 رقمی)", 3, 2)
        self.birth_date_frame = self.create_date_selector(form_container, 3, 0, columnspan=2)

        self.student_mobile = self.create_form_field(form_container, "موبایل دانش آموز", 5, 2)
        self.father_mobile = self.create_form_field(form_container, "موبایل پدر", 5, 1)
        self.mother_mobile = self.create_form_field(form_container, "موبایل مادر", 5, 0)

        self.father_work = self.create_form_field(form_container, "تلفن محل کار پدر", 6, 2)
        self.mother_work = self.create_form_field(form_container, "تلفن محل کار مادر", 6, 1)
        self.home_phone = self.create_form_field(form_container, "تلفن منزل", 6, 0)

        ctk.CTkLabel(
            form_container,
            text="آدرس محل سکونت",
            font=("B Nazanin", 13),
            anchor="e"
        ).grid(row=7, column=2, padx=10, sticky="e")

        self.address_entry = ctk.CTkTextbox(
            form_container,
            font=("B Nazanin", 13),
            height=80,
            border_width=1,
            corner_radius=6,
        )
        self.address_entry.grid(row=8, column=0, columnspan=3, padx=10, sticky="ew")

        btn_frame = ctk.CTkFrame(form_container, fg_color="transparent")
        btn_frame.grid(row=9, column=0, columnspan=3, pady=20)

        ctk.CTkButton(
            btn_frame,
            text="💾 ذخیره اطلاعات",
            font=("B Nazanin", 14),
            width=140,
            height=36,
            command=lambda: print("اطلاعات ذخیره شد")
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

    def create_form_field(self, parent, placeholder_text, row, column):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.grid(row=row, column=column, sticky="nsew", padx=10, pady=5)

        entry = ctk.CTkEntry(
            frame,
            placeholder_text= placeholder_text,
            font=("B Nazanin", 13),
            height=32,
            border_width=1,
            corner_radius=6,
            justify="right"
        )
        entry.pack(side="top", fill="x")
        return entry

    def create_date_selector(self, parent, row, column, columnspan=1):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.grid(row=row, column=column, columnspan=columnspan, sticky="nsew", padx=10, pady=5)

        selector_frame = ctk.CTkFrame(frame, fg_color="transparent")
        selector_frame.pack(fill="x")

        months = [
            "فروردین", "اردیبهشت", "خرداد",
            "تیر", "مرداد", "شهریور",
            "مهر", "آبان", "آذر",
            "دی", "بهمن", "اسفند"
        ]

        # سال
        year_values = [str(y) for y in range(1380, 1405)]
        self.year_combo = ctk.CTkComboBox(
            selector_frame,
            values=year_values,
            width=90,
            height=32,
            font=("B Nazanin", 12),
            state="readonly",
            justify = "right"
        )
        self.year_combo.set("سال تولد")
        self.year_combo.pack(side="right", padx=5)

        # ماه
        month_values = [f"{i+1:02d} - {months[i]}" for i in range(12)]
        self.month_combo = ctk.CTkComboBox(
            selector_frame,
            values=month_values,
            width=110,
            height=32,
            font=("B Nazanin", 12),
            state="readonly",
            justify = "right"
        )
        self.month_combo.set("ماه تولد")
        self.month_combo.pack(side="right", padx=5)

        # روز
        day_values = [f"{d:02d}" for d in range(1, 32)]
        self.day_combo = ctk.CTkComboBox(
            selector_frame,
            values=day_values,
            width=70,
            height=32,
            font=("B Nazanin", 12),
            state="readonly",
            justify = "right"
        )
        self.day_combo.set("روز")
        self.day_combo.pack(side="right", padx=5)

        return frame
    
    def create_class_info_selector(self, parent, row, column, columnspan=1):
        selector_frame = ctk.CTkFrame(parent, fg_color="transparent")
        selector_frame.grid(row=row, column=column, columnspan=columnspan, padx=10, pady=(5), sticky="e")

        selector_frame.grid_columnconfigure((0, 1, 2), weight=1)

        # لیست‌ها (قابل تنظیم با دیتابیس در آینده)
        field_options = ["شبکه", "برق", "الکترونیک", "کامپیوتر", "مکانیک"]
        grade_options = ["دهم", "یازدهم", "دوازدهم"]
        class_number_options = ["1", "2", "3", "4"]

        # کمبوباکس رشته
        self.field_combo = ctk.CTkComboBox(
            selector_frame,
            values=field_options,
            font=("B Nazanin", 13),
            justify="right",  # توجه: ممکنه نیاز به تغییر دستی Widget داشته باشه چون CustomTkinter پشتیبانی نکنه
            width=100,
            height=30,
            corner_radius=6,
            state="readonly"
        )
        self.field_combo.set("رشته")
        self.field_combo.grid(row=0, column=2, padx=5)

        # کمبوباکس پایه
        self.grade_combo = ctk.CTkComboBox(
            selector_frame,
            values=grade_options,
            font=("B Nazanin", 13),
            justify="right",
            width=100,
            height=30,
            corner_radius=6,
            state="readonly"
        )
        self.grade_combo.set("پایه")
        self.grade_combo.grid(row=0, column=1, padx=5)

        # کمبوباکس شماره کلاس
        self.class_number_combo = ctk.CTkComboBox(
            selector_frame,
            values=class_number_options,
            font=("B Nazanin", 13),
            justify="right",
            width=100,
            height=30,
            corner_radius=6,
            state="readonly",
        )
        self.class_number_combo.set("شماره کلاس")
        self.class_number_combo.grid(row=0, column=0, padx=5)

        return selector_frame
