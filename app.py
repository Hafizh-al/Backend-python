# 1. Impor "cetakan" Flask
from flask import Flask

# 2. Buat "objek" aplikasi dari cetakan tersebut
app = Flask(__name__)

# 3. Buat "alamat" attau "rute" untuk halaman utama
@app.route('/')
def halaman_utama():
    # 4. Tentukan apa yang harus ditampilkan di alamt ini
    return "Website pertamaku dengan Python!"
# 2. membuat halaman baru
@app.route('/profil')
def halaman_profil():
    return("Ini adalah halaman profil saya.")
# 5. (Opsional tapi bagus) Baris untuk menjalankan aplikasi
if __name__ == "__main__":
    app.run(debug=True)
