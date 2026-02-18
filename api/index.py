# File: api/index.py
from flask import Flask, render_template, request

# Import mesin lu dari folder engines
from engines.finance import calculate_finance
# (Kalo sticker.py belum ada, baris di bawah ini di-comment dulu pake #)
from engines.sticker import calculate_sticker 

app = Flask(__name__, template_folder='../templates')

@app.route("/", methods=["GET", "POST"])
def home():
    hasil = None
    tipe = "finance" # Default pas web pertama kali dibuka
    
    if request.method == "POST":
        # Ambil pilihan dari dropdown
        tipe = request.form.get("tool_type")
        
        # JALUR 1: KALKULATOR FINANCE
        if tipe == "finance":
            m = float(request.form.get("masa_kerja", 0))
            g = float(request.form.get("gaji", 0))
            hasil = calculate_finance(m, g) # Panggil dapur finance
            
        # JALUR 2: KALKULATOR STIKER FRAMELESS [cite: 2026-01-31]
        elif tipe == "sticker":
            l = float(request.form.get("lebar", 0))
            p = float(request.form.get("panjang", 0))
            q = int(request.form.get("qty", 0))
            hasil = calculate_sticker(l, p, q) # Panggil dapur stiker

    # KUNCINYA: Lempar balik 'tipe' ke web sebagai 'tool_aktif'
    return render_template("index.html", hasil=hasil, tool_aktif=tipe)
        
