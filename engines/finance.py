def calculate_finance(masa_kerja, gaji):
    try:
        # Ubah teks jadi angka di sini. 'or 0' biar gak error kalo kosong [cite: 2026-01-25]
        m_angka = float(masa_kerja or 0)
        g_angka = float(gaji or 0)
        
        if m_angka == 0:
            return "Bulan kerja gak boleh 0 atau kosong, Beb!"

        # Rumus Jatah Frameless: (Bulan / 12) * Gaji [cite: 2026-01-31]
        perhitungan = (m_angka / 12) * g_angka
        
        return f"Rp {perhitungan:,.0f}"
    except Exception as e:
        return f"Dapur mogok karena: {str(e)}"
        
