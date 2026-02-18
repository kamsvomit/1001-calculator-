# Ini 'Resepsionis'. Dia yang nerima data dari web 
# terus dikirim ke dapur (engines).

from flask import Flask, render_template, request
from engines.finance import calculate_finance # Import mesin lu

app = Flask(__name__, template_folder='../templates')

@app.route("/", methods=["GET", "POST"])
def home():
    hasil = None
    
    if request.method == "POST":
        # 1. Cek user pilih alat apa di dropdown
        tipe = request.form.get("tool_type")
        
        # 2. Kalo milih finance, ambil data dan panggil mesinnya
        if tipe == "finance":
            m = float(request.form.get("masa_kerja", 0))
            g = float(request.form.get("gaji", 0))
            hasil = calculate_finance(m, g) # Masuk ke dapur finance
            
        # 3. Kalo milih sticker, lu bakal isi logikanya nanti
        elif tipe == "sticker":
            hasil = "Mesin sticker lagi dirakit, Beb!"
            
    # Balikin hasil ke halaman web buat diliat user
    return render_template("index.html", hasil=hasil)
