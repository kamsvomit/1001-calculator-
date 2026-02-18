from flask import Flask, render_template, request
from engines.finance import calculate_finance
from engines.sticker import calculate_sticker # <-- Import mesin baru lu

app = Flask(__name__, template_folder='../templates')

@app.route("/", methods=["GET", "POST"])
def home():
    hasil = None
    tipe = "finance" # Default pas dibuka

    if request.method == "POST":
        tipe = request.form.get("tool_type")
        
        # Pintu 1: Kalo user pilih finance
        if tipe == "finance":
            m = float(request.form.get("masa_kerja", 0))
            g = float(request.form.get("gaji", 0))
            hasil = calculate_finance(m, g)
            
        # Pintu 2: Kalo user pilih sticker
        elif tipe == "sticker":
            l = float(request.form.get("lebar", 0))
            p = float(request.form.get("panjang", 0))
            q = int(request.form.get("qty", 0))
            hasil = calculate_sticker(l, p, q) # <-- Panggil mesin stiker
            
    return render_template("index.html", hasil=hasil, tool_aktif=tipe)
            
