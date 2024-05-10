import tkinter as tk
from tkinter import messagebox


def calculate_bmi():
    weight_str = weight_entry.get()
    height_str = height_entry.get()

    # Girilen değerlerin sayısal olup olmadığını kontrol etme
    if not weight_str.replace(".", "").isdigit() or not height_str.replace(".", "").isdigit():
        messagebox.showwarning("Uyarı", "Lütfen sayısal değerler girin.")
        return

    weight = float(weight_str)
    height = float(height_str)

    bmi = weight / (height ** 2)
    interpretation = interpret_bmi(bmi)

    result_label.config(text=f"Vücut Kitle İndeksiniz (BMI): {bmi:.2f}\nDurumunuz: {interpretation}")


def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Zayıf"
    elif bmi < 24.9:
        return "Normal"
    elif bmi < 29.9:
        return "Fazla Kilolu"
    else:
        return "Obez"


# Tkinter GUI oluşturma
window = tk.Tk()
window.title("BMI Calc")
window.minsize(width=250, height=250)

# Etiketler ve Giriş Kutuları
weight_label = tk.Label(window, text="Ağırlık (kg):")
weight_label.grid(row=0, column=0, padx=10, pady=5)
weight_entry = tk.Entry(window)
weight_entry.grid(row=0, column=1, padx=10, pady=5)

height_label = tk.Label(window, text="Boy (m):")
height_label.grid(row=1, column=0, padx=10, pady=5)
height_entry = tk.Entry(window)
height_entry.grid(row=1, column=1, padx=10, pady=5)

# Hesapla düğmesi
calculate_button = tk.Button(window, text="Hesapla", command=calculate_bmi)
calculate_button.grid(row=2, column=1, columnspan=1, pady=5)

# Sonuç etiketi
result_label = tk.Label(window, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=5)

window.mainloop()
