# File: engines/finance.py

def calculate_finance(masa_kerja, gaji):
    # STEP 1: Kita liat dulu datanya ada atau nggak
    if not masa_kerja or not gaji:
        return f"Waduh! Python dapet data kosong. Cek 'name' di HTML lu, Beb. (Data: m={masa_kerja}, g={gaji})"

    try:
        # STEP 2: Paksa jadi angka [cite: 2026-01-25]
        m = float(masa_kerja)
        g = float(gaji)
        
        # STEP 3: Hitung matematika murni [cite: 2026-01-31]
        hasil = (m / 12) * g
        return f"Rp {hasil:,.0f}"
        
    except Exception as e:
        # STEP 4: Kalo gagal, kasih tau error-nya apa
        return f"Gagal Hitung! Error: {str(e)}. Data dapetnya: {masa_kerja}"
        
