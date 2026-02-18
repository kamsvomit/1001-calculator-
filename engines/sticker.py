# Ini mesin khusus buat ngitung harga stiker
def calculate_sticker(lebar, panjang, qty):
    # Rumus: Luas (cm2) x Harga per cm
    # Kita asumsikan harga per cm adalah Rp 10
    luas = lebar * panjang
    harga_dasar = 10
    total = luas * harga_dasar * qty

    # Logika Diskon: Kalo beli lebih dari 500 lembar, diskon 10%
    if qty > 500:
        total = total * 0.9
        catatan = " (Sudah termasuk diskon 10%)"
    else:
        catatan = ""

    return f"Rp {total:,.0f}{catatan}"
