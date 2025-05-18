import customtkinter as ctk
import tkinter as tk

class TeacherManagementPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        self.teachers = []
        self.selected_subjects = []
        self.selected_days = []

        self.grid_columnconfigure(0, weight=1)

        # عنوان صفحه
        title_frame = ctk.CTkFrame(self, fg_color="transparent")
        title_frame.pack(pady=15, fill="x")

        ctk.CTkLabel(
            title_frame,
            text="سیستم مدیریت اساتید",
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
            text="➕ افزودن استاد",
            font=("B Nazanin", 13),
            height=32,
            width=150,
            command=self.show_form_view
        ).pack(side="right", padx=5)

    def show_list_view(self, teachers=None):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        table_container = ctk.CTkFrame(self.content_frame)
        table_container.pack(fill="both", expand=True, padx=10, pady=10)

        headers = ["ردیف", "نام", "نام خانوادگی", "کد ملی", "تلفن‌ها", "دروس", "روزهای حضور", "عملیات"]
        self.create_table_row(table_container, headers, is_header=True)

        for idx, teacher in enumerate(teachers or self.teachers, 1):
            row_data = [
                idx,
                teacher.get('first_name', ''),
                teacher.get('last_name', ''),
                teacher.get('national_id', ''),
                f"{teacher.get('phone1', '')}\n{teacher.get('phone2', '')}",
                ", ".join(teacher.get('subjects', [])),
                ", ".join(teacher.get('days', [])),
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
            text="فرم ثبت اطلاعات استاد",
            font=("B Titr", 18),
            anchor="center"
        ).grid(row=0, column=0, columnspan=3, pady=(0, 20), sticky="ew")

        # ردیف اول - اطلاعات پایه
        self.first_name = self.create_form_field(form_container, "نام استاد", 1, 2)
        self.last_name = self.create_form_field(form_container, "نام خانوادگی", 1, 1)
        self.national_id = self.create_form_field(form_container, "کد ملی (10 رقمی)", 1, 0)

        # ردیف دوم - تاریخ تولد
        self.birth_date_frame = self.create_date_selector(form_container, 2, 1, columnspan=2)

        # ردیف سوم - شماره تماس
        self.phone1 = self.create_form_field(form_container, "شماره تماس ۱", 3, 2)
        self.phone2 = self.create_form_field(form_container, "شماره تماس ۲", 3, 1)

        # ردیف چهارم - بخش دروس و روزها
        subjects_days_frame = ctk.CTkFrame(form_container, fg_color="transparent")
        subjects_days_frame.grid(row=4, column=0, columnspan=3, sticky="nsew", pady=10)
        subjects_days_frame.grid_columnconfigure((0, 1), weight=1)

        # بخش دروس تدریسی
        subjects_frame = ctk.CTkFrame(subjects_days_frame, fg_color="transparent")
        subjects_frame.grid(row=0, column=0, sticky="nsew", padx=10)
        self.create_subjects_section(subjects_frame)

        # بخش روزهای حضور
        days_frame = ctk.CTkFrame(subjects_days_frame, fg_color="transparent")
        days_frame.grid(row=0, column=1, sticky="nsew", padx=10)
        self.create_days_section(days_frame)

        # دکمه‌ها
        btn_frame = ctk.CTkFrame(form_container, fg_color="transparent")
        btn_frame.grid(row=5, column=0, columnspan=3, pady=20)

        ctk.CTkButton(
            btn_frame,
            text="💾 ذخیره اطلاعات",
            font=("B Nazanin", 14),
            width=140,
            height=36,
            command=self.save_teacher
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
            placeholder_text=placeholder_text,
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
            justify="right"
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
            justify="right"
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
            justify="right"
        )
        self.day_combo.set("روز")
        self.day_combo.pack(side="right", padx=5)

        return frame

    def create_subjects_section(self, parent):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="both", expand=True)

        ctk.CTkLabel(
            frame,
            text="دروس تدریسی:",
            font=("B Nazanin", 13),
            anchor="e"
        ).pack(side="top", anchor="e", fill="x")

        selector_frame = ctk.CTkFrame(frame, fg_color="transparent")
        selector_frame.pack(fill="x")

        self.subjects_combo = ctk.CTkComboBox(
            selector_frame,
            values=["ریاضی", "فیزیک", "برنامه‌نویسی", "هنر", "تاریخ"],
            font=("B Nazanin", 13),
            width=200,
            height=32,
            state="readonly"
        )
        self.subjects_combo.pack(side="right", padx=5)

        ctk.CTkButton(
            selector_frame,
            text="➕ افزودن درس",
            font=("B Nazanin", 12),
            width=100,
            height=28,
            command=self.add_subject
        ).pack(side="right", padx=5)

        self.subjects_list_frame = ctk.CTkScrollableFrame(
            frame,
            height=100,
            fg_color="transparent"
        )
        self.subjects_list_frame.pack(fill="both", expand=True, pady=5)

    def create_days_section(self, parent):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="both", expand=True)

        ctk.CTkLabel(
            frame,
            text="روزهای حضور:",
            font=("B Nazanin", 13),
            anchor="e"
        ).pack(side="top", anchor="e", fill="x")

        selector_frame = ctk.CTkFrame(frame, fg_color="transparent")
        selector_frame.pack(fill="x")

        self.days_combo = ctk.CTkComboBox(
            selector_frame,
            values=["شنبه", "یکشنبه", "دوشنبه", "سه‌شنبه", "چهارشنبه","پنجشنبه"],
            font=("B Nazanin", 13),
            width=200,
            height=32,
            state="readonly",
            justify = "right"
        )
        self.days_combo.pack(side="right", padx=5)

        ctk.CTkButton(
            selector_frame,
            text="➕ افزودن روز",
            font=("B Nazanin", 12),
            width=100,
            height=28,
            command=self.add_day
        ).pack(side="right", padx=5)

        self.days_list_frame = ctk.CTkScrollableFrame(
            frame,
            height=100,
            fg_color="transparent"
        )
        self.days_list_frame.pack(fill="both", expand=True, pady=5)

    def add_subject(self):
        subject = self.subjects_combo.get()
        if subject and subject not in self.selected_subjects:
            self.selected_subjects.append(subject)
            self.update_subjects_list()

    def add_day(self):
        day = self.days_combo.get()
        if day and day not in self.selected_days:
            self.selected_days.append(day)
            self.update_days_list()

    def update_subjects_list(self):
        for widget in self.subjects_list_frame.winfo_children():
            widget.destroy()

        for subject in self.selected_subjects:
            item_frame = ctk.CTkFrame(self.subjects_list_frame, fg_color="transparent")
            item_frame.pack(fill="x", pady=2)

            ctk.CTkLabel(
                item_frame,
                text=subject,
                font=("B Nazanin", 13)
            ).pack(side="right", padx=5)

            ctk.CTkButton(
                item_frame,
                text="×",
                width=30,
                height=24,
                fg_color="#E74C3C",
                hover_color="#C0392B",
                command=lambda s=subject: self.remove_subject(s)
            ).pack(side="left")

    def update_days_list(self):
        for widget in self.days_list_frame.winfo_children():
            widget.destroy()

        for day in self.selected_days:
            item_frame = ctk.CTkFrame(self.days_list_frame, fg_color="transparent")
            item_frame.pack(fill="x", pady=2)

            ctk.CTkLabel(
                item_frame,
                text=day,
                font=("B Nazanin", 13)
            ).pack(side="right", padx=5)

            ctk.CTkButton(
                item_frame,
                text="×",
                width=30,
                height=24,
                fg_color="#E74C3C",
                hover_color="#E74C3C",
                command=lambda d=day: self.remove_day(d)
            ).pack(side="left")

    def remove_subject(self, subject):
        self.selected_subjects.remove(subject)
        self.update_subjects_list()

    def remove_day(self, day):
        self.selected_days.remove(day)
        self.update_days_list()

    def save_teacher(self):
        teacher_data = {
            'first_name': self.first_name.get(),
            'last_name': self.last_name.get(),
            'national_id': self.national_id.get(),
            'birth_date': f"{self.year_combo.get()}/{self.month_combo.get().split()[0]}/{self.day_combo.get()}",
            'phone1': self.phone1.get(),
            'phone2': self.phone2.get(),
            'subjects': self.selected_subjects,
            'days': self.selected_days
        }
        print("اطلاعات استاد ذخیره شد:", teacher_data)
        self.show_list_view()