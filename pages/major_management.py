import customtkinter as ctk
import tkinter.messagebox as mbox

class MajorManagementPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        # تیتر
        self.title_label = ctk.CTkLabel(self, text="مدیریت رشته‌ها", font=("IRANSans", 24, "bold"))
        self.title_label.pack(pady=(20,10))

        # فیلد ورود نام رشته
        self.major_entry = ctk.CTkEntry(self, placeholder_text="نام رشته جدید را وارد کنید")
        self.major_entry.pack(pady=10)

        # لیست رشته‌ها
        self.major_listbox = ctk.CTkTextbox(self, width=400, height=300)
        self.major_listbox.pack(pady=20)

        # فریم دکمه‌ها
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=10)

        self.add_btn = ctk.CTkButton(self.button_frame, text="افزودن رشته", command=self.add_major)
        self.add_btn.grid(row=0, column=0, padx=5)

        self.delete_btn = ctk.CTkButton(self.button_frame, text="حذف رشته", command=self.delete_major)
        self.delete_btn.grid(row=0, column=1, padx=5)

        self.save_btn = ctk.CTkButton(self.button_frame, text="ذخیره تغییرات", command=self.save_majors)
        self.save_btn.grid(row=0, column=2, padx=5)

    def add_major(self):
        major = self.major_entry.get().strip()
        if major != "":
            current_text = self.major_listbox.get("1.0", "end-1c").split("\n")
            if major not in current_text:
                self.major_listbox.insert("end", major + "\n")
                self.major_entry.delete(0, "end")
            else:
                mbox.showinfo("هشدار", "این رشته قبلا ثبت شده است.")
        else:
            mbox.showinfo("خطا", "نام رشته نمی‌تواند خالی باشد.")

    def delete_major(self):
        try:
            selected_text = self.major_listbox.get("sel.first", "sel.last").strip()
            if selected_text:
                all_text = self.major_listbox.get("1.0", "end")
                updated_text = all_text.replace(selected_text + "\n", "")
                self.major_listbox.delete("1.0", "end")
                self.major_listbox.insert("1.0", updated_text)
        except:
            mbox.showinfo("خطا", "لطفاً یک رشته را انتخاب کنید.")

    def save_majors(self):
        majors = self.major_listbox.get("1.0", "end-1c").split("\n")
        majors = [m.strip() for m in majors if m.strip()]
        try:
            with open("majors.txt", "w", encoding="utf-8") as file:
                for major in majors:
                    file.write(major + "\n")
            mbox.showinfo("ذخیره شد", "لیست رشته‌ها با موفقیت ذخیره شد.")
        except Exception as e:
            mbox.showerror("خطا", f"خطا در ذخیره سازی: {str(e)}")
