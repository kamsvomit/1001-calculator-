# File: engines/finance.py

def calculate_finance(masa_kerja, gaji):
    # Pake try...except biar mesin gak pingsan kalo inputnya aneh [cite: 2026-01-25]
    try:
        # Kita jinakkan data teks jadi angka di sini [cite: 2026-01-25]
        # 'or 0' fungsinya biar kalo user gak ngisi, Python anggep angkanya 0
        m = float(masa_kerja or 0)
        g = float(gaji or 0)
        
        # Cek kalo salah satu nol, jangan dihitung dulu
        if m == 0 or g == 0:
            return "Woi Beb, isi dulu angkanya! Wkwk"
        
        # RUMUS MATEMATIKA JATAH FRAMELESS [cite: 2026-01-31]
        # (Masa Kerja / 12 Bulan) x Gaji
        hitung = (m / 12) * g
        
        # Balikin hasil dengan format Rp dan pemisah ribuan
        return f"Rp {hitung:,.0f}"
        
    except Exception as e:
        # Kalo ada error teknis, munculin pesannya di layar
        return f"Error Mesin: {str(e)}"
            
