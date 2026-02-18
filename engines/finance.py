# File: engines/finance.py

def calculate_finance(masa_kerja, gaji):
    try:
        # Konversi aman: Kalo kosong ganti jadi 0 [cite: 2026-01-25]
        m = float(masa_kerja or 0)
        g = float(gaji or 0)
        
        if m == 0 or g == 0:
            return "Isi dulu angkanya yang bener, Beb!"

        # Rumus Jatah Frameless Industries [cite: 2026-01-31]
        $$Hasil = \left( \frac{m}{12} \right) \times g$$
        
        total = (m / 12) * g
        return f"Rp {total:,.0f}"
        
    except Exception as e:
        return f"Ada masalah di mesin: {str(e)}"
        
