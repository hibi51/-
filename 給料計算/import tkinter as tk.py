import tkinter as tk
from tkinter import messagebox

def calculate_salary():
    try:
        base_salary = float(base_salary_entry.get())
        night_base_salary = float(night_base_salary_entry.get())
        hours_worked = float(hours_worked_entry.get())
        night_hours_worked = float(night_hours_worked_entry.get())
        daily_allowance_days = float(daily_allowance_days_entry.get())  # 日当
        transportation_allowance = float(transportation_allowance_entry.get())  # 交通費
        days_worked = float(days_worked_entry.get())  # 総出勤日数

    
       
       # 基本給での給与 +　深夜給 + 日当での給与 + 交通費
        total_salary= (base_salary * hours_worked ) + (night_base_salary * night_hours_worked) + (6000 * daily_allowance_days ) + (transportation_allowance * days_worked )
        messagebox.showinfo("給与計算結果", f"給与: {total_salary} 円")
    except ValueError:
        messagebox.showerror("エラー", "有効な数字を入力してください")

# GUIの作成
root = tk.Tk()
root.title("給料計算システム")

base_salary_label = tk.Label(root, text="基本給:")
base_salary_label.grid(row=0, column=0)
base_salary_entry = tk.Entry(root)
base_salary_entry.grid(row=0, column=1)

night_base_salary_label = tk.Label(root, text="深夜給料:")
night_base_salary_label.grid(row=1, column=0)
night_base_salary_entry = tk.Entry(root)
night_base_salary_entry.grid(row=1, column=1)

hours_worked_label = tk.Label(root, text="勤務時間:")
hours_worked_label.grid(row=2, column=0)
hours_worked_entry = tk.Entry(root)
hours_worked_entry.grid(row=2, column=1)

night_hours_worked_label = tk.Label(root, text="深夜勤務時間:")
night_hours_worked_label.grid(row=3, column=0)
night_hours_worked_entry = tk.Entry(root)
night_hours_worked_entry.grid(row=3, column=1)

daily_allowance_days_label = tk.Label(root, text="日当での出勤日数:")
daily_allowance_days_label.grid(row=4, column=0)
daily_allowance_days_entry = tk.Entry(root)
daily_allowance_days_entry.grid(row=4, column=1)

transportation_allowance_label = tk.Label(root, text="交通費:")
transportation_allowance_label.grid(row=5, column=0)
transportation_allowance_entry = tk.Entry(root)
transportation_allowance_entry.grid(row=5, column=1)

days_worked_label = tk.Label(root, text="出勤日数:")
days_worked_label.grid(row=6, column=0)
days_worked_entry = tk.Entry(root)
days_worked_entry.grid(row=6, column=1)

calculate_button = tk.Button(root, text="計算", command=calculate_salary)
calculate_button.grid(row=7, column=0, columnspan=2)

root.mainloop()