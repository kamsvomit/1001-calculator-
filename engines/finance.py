# File: engines/finance.py

def calculate_finance(masa_kerja, gaji):
    try:
        # Ubah teks jadi angka. Kalo kosong jadi 0 [cite: 2026-01-25]
        m = float(masa_kerja or 0)
        g = float(gaji or 0)
        
        if m == 0 or g == 0:
            return "Woi Beb, angkanya diisi dulu! Wkwk"

        # Rumus: (Bulan / 12) * Gaji [cite: 2026-01-31]
        total = (m / 12) * g
        
        return f"Rp {total:,.0f}"
    except Exception as e:
        # Kalo ada error, munculin pesannya di layar
        return f"Error Mesin: {str(e)}"
        
