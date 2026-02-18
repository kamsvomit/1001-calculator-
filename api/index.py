# File: api/index.py
@app.route("/", methods=["GET", "POST"])
def home():
    hasil = None
    tipe = "finance" # Default
    
    if request.method == "POST":
        tipe = request.form.get("tool_type")
        
        if tipe == "finance":
            # Ambil data murni, jangan diconvert di sini!
            m = request.form.get("masa_kerja")
            g = request.form.get("gaji")
            
            # Cek manual: Kalo datanya beneran nyampe, baru panggil mesin
            if m and g:
                hasil = calculate_finance(m, g)
            else:
                hasil = "Duh Beb, datanya nggak nyampe ke Python. Cek input lu!"
                
        elif tipe == "sticker":
            l = request.form.get("lebar")
            p = request.form.get("panjang")
            q = request.form.get("qty")
            hasil = calculate_sticker(l, p, q)

    return render_template("index.html", hasil=hasil, tool_aktif=tipe)
    
