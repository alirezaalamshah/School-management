# pages/major_management.py
import customtkinter as ctk
from tkinter import messagebox

class MajorManagementPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        
        # عنوان صفحه
        title_label = ctk.CTkLabel(
            self,
            text="مدیریت پایه‌ها، رشته‌ها و دروس",
            font=("B Titr", 20, "bold"),
        )
        title_label.pack(pady=15, padx=20, anchor="e")

        # تب‌های اصلی
        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(fill="both", expand=True, padx=20, pady=10)
        
        # ایجاد تب‌ها
        self.tabview.add("دروس")
        self.tabview.add("کلاس‌ها")
        self.tabview.add("پایه‌ها")
        self.tabview.add("رشته‌ها")
        self.tabview.set("رشته‌ها")
        
        # طراحی هر تب
        self.create_majors_tab()
        self.create_grades_tab()
        self.create_classes_tab()
        self.create_courses_tab()

    def create_input_section(self, parent, title):
        # قالب مشترک برای بخش‌های ورودی
        frame = ctk.CTkFrame(parent,)
        frame.pack(fill="x", pady=10, padx=10)
        
        ctk.CTkLabel(
            frame,
            text=title,
            font=("B Nazanin", 14, "bold"),
        ).pack(side="right", padx=10, pady=5)
        
        return frame

    def create_majors_tab(self):
        tab = self.tabview.tab("رشته‌ها")
        
        # بخش افزودن رشته جدید
        add_frame = self.create_input_section(tab, "افزودن رشته جدید:")
        
        self.major_entry = ctk.CTkEntry(
            add_frame,
            placeholder_text="نام رشته (مثال: کامپیوتر)",
            font=("B Nazanin", 13),
            width=300,
            height=35,
            justify = "right"
        )
        self.major_entry.pack(side="right", padx=10, pady=5)
        
        ctk.CTkButton(
            add_frame,
            text="➕ افزودن",
            font=("B Nazanin", 13),
            width=100,
            height=35,
            command=self.add_major
        ).pack(side="right", padx=10)
        
        # لیست رشته‌ها
        self.majors_list = ctk.CTkScrollableFrame(tab, )
        self.majors_list.pack(fill="both", expand=True, padx=10, pady=10)

    def create_grades_tab(self):
        tab = self.tabview.tab("پایه‌ها")
        
        # بخش افزودن پایه جدید
        add_frame = self.create_input_section(tab, "افزودن پایه جدید:")
        
        self.grade_entry = ctk.CTkEntry(
            add_frame,
            placeholder_text="نام پایه (مثال: دهم، یازدهم)",
            font=("B Nazanin", 13),
            width=300,
            height=35,
            justify = "right"
        )
        self.grade_entry.pack(side="right", padx=10, pady=5)
        
        ctk.CTkButton(
            add_frame,
            text="➕ افزودن",
            # fg_color="#27AE60",
            font=("B Nazanin", 13),
            width=100,
            height=35,
            command=self.add_grade
        ).pack(side="right", padx=10)
        
        # لیست پایه‌ها
        self.grades_list = ctk.CTkScrollableFrame(tab, )
        self.grades_list.pack(fill="both", expand=True, padx=10, pady=10)

    def create_classes_tab(self):
        tab = self.tabview.tab("کلاس‌ها")
        
        # بخش افزودن کلاس جدید
        add_frame = self.create_input_section(tab, "افزودن کلاس جدید:")
        
        # انتخاب رشته
        self.major_combo = ctk.CTkComboBox(
            add_frame,
            values=["انتخاب رشته"],
            font=("B Nazanin", 13),
            width=150,
            height=35,
            justify = "right",
            state= "readonly"
        )
        self.major_combo.pack(side="right", padx=5)
        self.major_combo.set("انتخاب رشته")
        
        # انتخاب پایه
        self.grade_combo = ctk.CTkComboBox(
            add_frame,
            values=["انتخاب پایه"],
            font=("B Nazanin", 13),
            width=150,
            height=35,
            justify = "right",
            state= "readonly"
        )
        self.grade_combo.pack(side="right", padx=5)
        self.grade_combo.set("انتخاب پایه")
        
        # نام کلاس
        self.class_entry = ctk.CTkEntry(
            add_frame,
            placeholder_text="شناسه کلاس (مثال: 101)",
            font=("B Nazanin", 13),
            width=150,
            height=35,
            justify = "right"
        )
        self.class_entry.pack(side="right", padx=5)
        
        ctk.CTkButton(
            add_frame,
            text="➕ افزودن",
            # fg_color="#27AE60",
            font=("B Nazanin", 13),
            width=100,
            height=35,
            command=self.add_class
        ).pack(side="right", padx=10)
        
        # لیست کلاس‌ها
        self.classes_list = ctk.CTkScrollableFrame(tab, )
        self.classes_list.pack(fill="both", expand=True, padx=10, pady=10)

    def create_courses_tab(self):
        tab = self.tabview.tab("دروس")

        # بخش افزودن درس جدید
        add_frame = self.create_input_section(tab, "افزودن درس جدید:")

        # انتخاب رشته
        self.course_major_combo = ctk.CTkComboBox(
            add_frame,
            values=["انتخاب رشته"],
            font=("B Nazanin", 13),
            width=150,
            height=35,
            justify = "right",
            state= "readonly"
        )
        self.course_major_combo.pack(side="right", padx=5)
        self.course_major_combo.set("انتخاب رشته")

        # انتخاب پایه
        self.course_grade_combo = ctk.CTkComboBox(
            add_frame,
            values=["انتخاب پایه"],
            font=("B Nazanin", 13),
            width=150,
            height=35,
            justify = "right",
            state= "readonly"
        )
        self.course_grade_combo.pack(side="right", padx=5)
        self.course_grade_combo.set("انتخاب پایه")

        # نام درس
        self.course_entry = ctk.CTkEntry(
            add_frame,
            placeholder_text="نام درس (مثال: ریاضی)",
            font=("B Nazanin", 13),
            width=150,
            height=35,
            justify = "right",
        )
        self.course_entry.pack(side="right", padx=5)

        ctk.CTkButton(
            add_frame,
            text="➕ افزودن",
            font=("B Nazanin", 13),
            width=100,
            height=35,
            command=self.add_course
        ).pack(side="right", padx=10)

        # لیست دروس
        self.courses_list = ctk.CTkScrollableFrame(tab,)
        self.courses_list.pack(fill="both", expand=True, padx=10, pady=10)



    def add_item_to_list(self, parent, text):
        # افزودن آیتم به لیست‌ها
        item_frame = ctk.CTkFrame(parent)
        item_frame.pack(fill="x", pady=2, padx=5)
        
        ctk.CTkLabel(
            item_frame,
            text=text,
            font=("B Nazanin", 13),
        ).pack(side="right", padx=10)
        
        ctk.CTkButton(
            item_frame,
            text="✏️",
            fg_color="transparent",
            hover_color="#EBF5FB",
            text_color="#3498DB",
            width=30,
            height=30,
            font=("B Nazanin", 13)
        ).pack(side="left")
        
        ctk.CTkButton(
            item_frame,
            text="🗑️",
            fg_color="transparent",
            hover_color="#FDEDEC",
            text_color="#E74C3C",
            width=30,
            height=30,
            font=("B Nazanin", 13)
        ).pack(side="left")

    # توابع موقت برای افزودن آیتم‌ها
    def add_major(self):
        if self.major_entry.get():
            self.add_item_to_list(self.majors_list, self.major_entry.get())
            self.major_entry.delete(0, "end")

    def add_grade(self):
        if self.grade_entry.get():
            self.add_item_to_list(self.grades_list, self.grade_entry.get())
            self.grade_entry.delete(0, "end")

    def add_class(self):
        class_info = f"{self.grade_combo.get()} - {self.major_combo.get()} - {self.class_entry.get()}"
        self.add_item_to_list(self.classes_list, class_info)
        self.class_entry.delete(0, "end")

    def add_course(self):
        course_info = (
            f"{self.course_entry.get()} "
            f"(پایه {self.course_grade_combo.get()} - "
            f"رشته {self.course_major_combo.get()})"
        )
        self.add_item_to_list(self.courses_list, course_info)
        self.course_entry.delete(0, "end")