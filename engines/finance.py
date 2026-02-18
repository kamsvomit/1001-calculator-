# File: engines/finance.py

def calculate_finance(masa_kerja, gaji):
        # Sekarang baru kita hitung: (Bulan / 12) * Gaji
        hasil = (masa_kerja / 12) * gaji
        
        # Balikin hasilnya dengan format Rupiah
        return f"Rp {hasil:,.0f}"
        
