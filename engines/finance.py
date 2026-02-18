# File: engines/finance.py

def calculate_finance(masa_kerja, gaji):
    # Kita paksa input jadi angka (float) biar bisa dihitung matematikanya
    # [cite: 2026-01-25]
    try:
        angka_masa_kerja = float(masa_kerja)
        angka_gaji = float(gaji)
        
        # Sekarang baru kita hitung: (Bulan / 12) * Gaji
        hasil = (angka_masa_kerja / 12) * angka_gaji
        
        # Balikin hasilnya dengan format Rupiah
        return f"Rp {hasil:,.0f}"
    except:
        # Kalo user masukin huruf, bukan angka, kasih tau biar gak error
        return "Input harus angka, Beb!"
        
