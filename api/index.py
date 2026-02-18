import os
from flask import Flask, render_template, request

# --- MESIN FINANCE (Kita taruh sini dulu biar gak error import) ---
def calculate_finance(masa_kerja, gaji):
    hasil = (float(masa_kerja) / 12) * float(gaji)
    return f"Rp {hasil:,.0f}"

# --- SETTING KABEL (Vercel Safe) ---
# Kita kasih tau Flask posisi folder template secara detail
base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(base_dir, '..', 'templates')

app = Flask(__name__, template_folder=template_dir)

@app.route("/", methods=["GET", "POST"])
def home():
    hasil = None
    tipe = "finance"
    
    try:
        if request.method == "POST":
            tipe = request.form.get("tool_type")
            if tipe == "finance":
                m = request.form.get("masa_kerja", 0)
                g = request.form.get("gaji", 0)
                hasil = calculate_finance(m, g)
    except Exception as e:
        # Kalo error, tampilin pesannya di web biar kita tau salahnya apa
        hasil = f"Error: {str(e)}"
        
    return render_template("index.html", hasil=hasil, tool_aktif=tipe)
