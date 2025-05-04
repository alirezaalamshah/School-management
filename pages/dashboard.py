# pages/dashboard.py

import customtkinter as ctk
import jdatetime
from datetime import datetime

class DashboardPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        self.configure(corner_radius=10)

        # === فریم بالای صفحه - تاریخ و ساعت ===
        header_frame = ctk.CTkFrame(self, corner_radius=15)
        header_frame.pack(fill="x", padx=20, pady=15)

        self.datetime_label = ctk.CTkLabel(
            header_frame,
            text="",
            font=("B Nazanin", 18, "bold"),
            text_color=("#2e2e2e", "#dddddd"),  # تطبیق با دارک/لایت مود
            anchor="center"
        )
        self.datetime_label.pack(pady=10)
        self.update_datetime()

        # === عنوان داشبورد ===
        title = ctk.CTkLabel(self, text="داشبورد مدیریت هنرستان", font=("B Nazanin", 22, "bold"))
        title.pack(pady=10)

        # === بخش آمار کلی ===
        stats_frame = ctk.CTkFrame(self, corner_radius=12)
        stats_frame.pack(pady=10, padx=20, fill="x")

        student_stat = self.create_stat_box(stats_frame, "تعداد کل دانش‌آموزان", "۱۲۰")
        class_stat = self.create_stat_box(stats_frame, "تعداد کلاس‌ها", "۸")

        student_stat.pack(side="right", padx=10, fill="both", expand=True)
        class_stat.pack(side="right", padx=10, fill="both", expand=True)

        # === بخش دانش‌آموزان غایب ===
        absents_frame = ctk.CTkFrame(self, corner_radius=12)
        absents_frame.pack(fill="both", expand=True, padx=20, pady=15)

        ctk.CTkLabel(
            absents_frame,
            text="لیست دانش‌آموزان غایب امروز",
            font=("B Nazanin", 18, "bold")
        ).pack(pady=10)

        scrollable_absents = ctk.CTkScrollableFrame(absents_frame, height=250, corner_radius=10)
        scrollable_absents.pack(fill="both", expand=True, padx=10, pady=5)

        absent_students = [
            "سینا محمدی", "هلیا کرمی", "نوید شریفی",
            "زهرا یوسفی", "رضا توسلی", "سارا موسوی"
        ]
        for name in absent_students:
            label = ctk.CTkLabel(scrollable_absents, text=name, font=("B Nazanin", 16), anchor="w")
            label.pack(fill="x", padx=10, pady=4)

    def update_datetime(self):
        now = datetime.now()
        now_jalali = jdatetime.datetime.fromgregorian(datetime=now)

        weekdays = {
            "Saturday": "شنبه",
            "Sunday": "یکشنبه",
            "Monday": "دوشنبه",
            "Tuesday": "سه‌شنبه",
            "Wednesday": "چهارشنبه",
            "Thursday": "پنج‌شنبه",
            "Friday": "جمعه"
        }

        months = {
            "Farvardin": "فروردین",
            "Ordibehesht": "اردیبهشت",
            "Khordad": "خرداد",
            "Tir": "تیر",
            "Mordad": "مرداد",
            "Shahrivar": "شهریور",
            "Mehr": "مهر",
            "Aban": "آبان",
            "Azar": "آذر",
            "Dey": "دی",
            "Bahman": "بهمن",
            "Esfand": "اسفند"
        }

        weekday = weekdays[now_jalali.strftime("%A")]
        day = now_jalali.day
        month = months[now_jalali.strftime("%B")]
        year = now_jalali.year
        time = now.strftime("%H:%M:%S")

        full_text = f"{weekday}، {day} {month} {year} - ساعت {time}"
        self.datetime_label.configure(text=full_text)

        self.datetime_label.after(1000, self.update_datetime)

    def create_stat_box(self, parent, title, number):
        frame = ctk.CTkFrame(parent, corner_radius=10)
        ctk.CTkLabel(frame, text=title, font=("B Nazanin", 16)).pack(pady=(10, 5))
        ctk.CTkLabel(frame, text=number, font=("B Nazanin", 20, "bold")).pack(pady=(0, 10))
        return frame
