# Ini 'Dapur' tempat lu masak rumus. 
# Lu bikin fungsinya mandiri di sini.

def calculate_finance(masa_kerja, gaji):
    # Rumus: Masa kerja dibagi 12 bulan dikali gaji
    hasil = (masa_kerja / 12) * gaji
    
    # Balikin hasilnya dalam format Rupiah biar cantik
    return f"Rp {hasil:,.0f}"
