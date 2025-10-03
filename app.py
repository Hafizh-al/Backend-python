# 1. Impor "cetakan" Flask
from flask import Flask, render_template

# 2. Buat "objek" aplikasi dari cetakan tersebut
app = Flask(__name__)

# 3. Buat "alamat" attau "rute" untuk Halaman utama
@app.route('/')
def home():
    # 4. Tentukan apa yang harus ditampilkan di alamt ini
    return render_template("index.html")

# 2. membuat halaman baru
@app.route('/profil')
def profil():
    return render_template("profil.html")
# 5. (Opsional tapi bagus) Baris untuk menjalankan aplikasi
if __name__ == "__main__":
    app.run(debug=True)
