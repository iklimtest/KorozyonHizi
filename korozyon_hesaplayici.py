import tkinter as tk
from tkinter import messagebox

def calculate_corrosion_rate():
    try:
        # Kullanıcı girdilerini al
        weight_loss_mg = float(weight_loss_entry.get())
        density_g_cm3 = float(density_entry.get())
        area_cm2 = float(area_entry.get())
        time_hours = float(time_entry.get())
        
        # Korozyon oranı hesaplama
        constant = 87.6
        corrosion_rate = (constant * weight_loss_mg) / (density_g_cm3 * area_cm2 * time_hours)
        
        # Sonucu kutuda göster
        result_entry.config(state="normal")  # Yazma modunu aç
        result_entry.delete(0, tk.END)      # Mevcut içeriği temizle
        result_entry.insert(0, f"{corrosion_rate:.4f} mm/yıl")  # Sonucu ekle
        result_entry.config(state="readonly")  # Yalnızca okuma moduna geç
    except ValueError:
        # Hatalı girişler için uyarı
        messagebox.showerror("Hata", "Lütfen tüm alanlara geçerli bir sayı girin!")

# Ana pencere
window = tk.Tk()
window.title("Korozyon Oranı Hesaplayıcı")
window.geometry("500x300")
window.config(padx=20, pady=20)

# Başlık
title_label = tk.Label(window, text="Korozyon Oranı Hesaplayıcı", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Girdi alanları
frame = tk.Frame(window)
frame.pack(pady=10)

tk.Label(frame, text="Kaybedilen Ağırlık (mg):").grid(row=0, column=0, sticky="e", padx=5, pady=5)
weight_loss_entry = tk.Entry(frame)
weight_loss_entry.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Yoğunluk (g/cm³):").grid(row=1, column=0, sticky="e", padx=5, pady=5)
density_entry = tk.Entry(frame)
density_entry.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Yüzey Alanı (cm²):").grid(row=2, column=0, sticky="e", padx=5, pady=5)
area_entry = tk.Entry(frame)
area_entry.grid(row=2, column=1, pady=5)

tk.Label(frame, text="Süre (saat):").grid(row=3, column=0, sticky="e", padx=5, pady=5)
time_entry = tk.Entry(frame)
time_entry.grid(row=3, column=1, pady=5)

# Hesaplama butonu ve sonuç kutusu
action_frame = tk.Frame(window)
action_frame.pack(pady=10)

calculate_button = tk.Button(action_frame, text="Hesapla", command=calculate_corrosion_rate, bg="green", fg="white")
calculate_button.grid(row=0, column=0, padx=10)

result_entry = tk.Entry(action_frame, font=("Arial", 12, "bold"), justify="center", width=20, state="readonly", bg="lightyellow")
result_entry.grid(row=0, column=1)

# Uygulama çalıştırma
window.mainloop()
