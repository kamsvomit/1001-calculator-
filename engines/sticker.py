# File: engines/sticker.py

def calculate_sticker(lebar, panjang, qty):
    try:
        # Kita rubah jadi angka di sini, biar index.py gak usah repot [cite: 2026-01-25]
        l = float(lebar or 0)
        p = float(panjang or 0)
        q = float(qty or 0)
        
        if l == 0 or p == 0 or q == 0:
            return "Isi dulu semua ukuran stikernya, Beb!"

        # Rumus Stiker Frameless Industries [cite: 2026-01-31]
        harga_dasar = 10 
        total = (l * p * harga_dasar) * q
        
        return f"Rp {total:,.0f}"
    except Exception as e:
        return f"Error Stiker: {str(e)}"
