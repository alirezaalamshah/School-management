# pages/teacher_management.py
import customtkinter as ctk
from tkinter import messagebox

class TeacherManagementPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        self.teachers = []
        self.courses = ["ریاضی", "فیزیک", "شیمی", "ادبیات"]

        self.configure(fg_color="#F5F5F5")

        title_label = ctk.CTkLabel(self, text="مدیریت اساتید و مدرسین", font=("B Titr", 20, "bold"), text_color="#2C3E50")
        title_label.pack(pady=15, padx=20, anchor="e")

        self.toolbar_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.toolbar_frame.pack(fill="x", padx=20, pady=5)

        self.search_entry = ctk.CTkEntry(
            self.toolbar_frame,
            placeholder_text="جستجو بر اساس نام یا کد ملی...",
            font=("B Nazanin", 13),
            width=300,
            height=32
        )
        self.search_entry.pack(side="right", padx=10)

        ctk.CTkButton(
            self.toolbar_frame,
            text="➕ افزودن استاد",
            fg_color="#2E86C1",
            hover_color="#2874A6",
            font=("B Nazanin", 13),
            height=32,
            width=150,
            command=self.show_add_form
        ).pack(side="right", padx=5)

        self.content_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.add_form_frame = None  # برای نمایش فرم افزودن
        self.teachers_list = None   # برای نمایش لیست اساتید

        self.show_teachers_list()

    def show_add_form(self):
        # پنهان‌سازی لیست
        if self.teachers_list:
            self.teachers_list.pack_forget()

        if self.add_form_frame:
            self.add_form_frame.destroy()

        self.add_form_frame = ctk.CTkFrame(self.content_frame, fg_color="white")
        self.add_form_frame.pack(fill="both", expand=True, pady=10)

        ctk.CTkLabel(self.add_form_frame, text="فرم ثبت استاد جدید", font=("B Titr", 16), text_color="#2C3E50").pack(pady=10)

        self.first_name = self.create_form_field(self.add_form_frame, "نام:")
        self.last_name = self.create_form_field(self.add_form_frame, "نام خانوادگی:")
        self.national_id = self.create_form_field(self.add_form_frame, "کد ملی:")
        self.phone = self.create_form_field(self.add_form_frame, "شماره تماس:")

        ctk.CTkLabel(
            self.add_form_frame, text="دروس تدریس:", font=("B Nazanin", 13), text_color="#34495E"
        ).pack(pady=(20, 5), anchor="w", padx=20)

        self.courses_frame = ctk.CTkScrollableFrame(self.add_form_frame, height=120)
        self.courses_frame.pack(fill="x", padx=20, pady=5)

        self.course_vars = {}
        for course in self.courses:
            var = ctk.BooleanVar()
            chk = ctk.CTkCheckBox(self.courses_frame, text=course, variable=var, font=("B Nazanin", 12))
            chk.pack(anchor="w", pady=2)
            self.course_vars[course] = var

        btn_frame = ctk.CTkFrame(self.add_form_frame, fg_color="transparent")
        btn_frame.pack(pady=20)

        ctk.CTkButton(
            btn_frame, text="💾 ذخیره", fg_color="#27AE60", hover_color="#219A52",
            font=("B Nazanin", 14), width=120, height=36,
            command=self.save_teacher
        ).pack(side="right", padx=15)

        ctk.CTkButton(
            btn_frame, text="↩️ بازگشت", fg_color="#E74C3C", hover_color="#C0392B",
            font=("B Nazanin", 14), width=120, height=36,
            command=self.back_to_list
        ).pack(side="left", padx=15)

    def back_to_list(self):
        if self.add_form_frame:
            self.add_form_frame.destroy()
        self.show_teachers_list()

    def show_teachers_list(self):
        if self.teachers_list:
            self.teachers_list.destroy()

        self.teachers_list = ctk.CTkScrollableFrame(self.content_frame, fg_color="white")
        self.teachers_list.pack(fill="both", expand=True)

        self.refresh_teachers_list()

    def create_form_field(self, parent, label_text):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", padx=20, pady=5)

        ctk.CTkLabel(frame, text=label_text, font=("B Nazanin", 13), width=100, anchor="e").pack(side="right", padx=10)

        entry = ctk.CTkEntry(frame, font=("B Nazanin", 13), height=32)
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def save_teacher(self):
        required_fields = {
            self.first_name: "نام",
            self.last_name: "نام خانوادگی",
            self.national_id: "کد ملی"
        }

        for field, name in required_fields.items():
            if not field.get().strip():
                messagebox.showerror("خطا", f"فیلد {name} الزامی است!")
                return

        selected_courses = [course for course, var in self.course_vars.items() if var.get()]

        teacher_data = {
            "first_name": self.first_name.get(),
            "last_name": self.last_name.get(),
            "national_id": self.national_id.get(),
            "phone": self.phone.get(),
            "courses": selected_courses
        }

        self.teachers.append(teacher_data)
        messagebox.showinfo("موفقیت", "اطلاعات استاد با موفقیت ثبت شد!")
        self.back_to_list()

    def refresh_teachers_list(self):
        for widget in self.teachers_list.winfo_children():
            widget.destroy()

        for idx, teacher in enumerate(self.teachers, 1):
            teacher_frame = ctk.CTkFrame(self.teachers_list, fg_color="#F8F9FA")
            teacher_frame.pack(fill="x", pady=2, padx=5)

            info_label = ctk.CTkLabel(
                teacher_frame,
                text=f"{idx}. {teacher['first_name']} {teacher['last_name']} - کد ملی: {teacher['national_id']}",
                font=("B Nazanin", 13),
                text_color="#2C3E50",
                anchor="w"
            )
            info_label.pack(side="right", fill="x", expand=True, padx=10)

            courses_label = ctk.CTkLabel(
                teacher_frame,
                text="، ".join(teacher['courses']),
                font=("B Nazanin", 12),
                text_color="#7F8C8D",
                wraplength=400
            )
            courses_label.pack(side="right", padx=10)

            btn_frame = ctk.CTkFrame(teacher_frame, fg_color="transparent")
            btn_frame.pack(side="left", padx=5)

            ctk.CTkButton(
                btn_frame, text="✏️", fg_color="transparent", hover_color="#EBF5FB",
                text_color="#3498DB", width=30, height=30, font=("B Nazanin", 13)
            ).pack(side="left", padx=2)

            ctk.CTkButton(
                btn_frame, text="🗑️", fg_color="transparent", hover_color="#FDEDEC",
                text_color="#E74C3C", width=30, height=30, font=("B Nazanin", 13)
            ).pack(side="left", padx=2)
