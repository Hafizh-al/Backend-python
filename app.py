# 1. Impor "cetakan" Flask
from flask import Flask, render_template

# 2. Buat "objek" aplikasi dari cetakan tersebut
app = Flask(__name__)

# 3. Buat "alamat" attau "rute" untuk Halaman utama
@app.route('/')
def halaman_utama():
    # 4. Tentukan apa yang harus ditampilkan di alamt ini
    return render_template('index.html')

# 2. membuat halaman baru
@app.route('/profil')
def halaman_profil():
    # Data yang ingin di kirim ke HTML
    name = "Muhammad Daffa Al Hafizh"
    hobby = "Coding | Membaca"
    school = "HSI Boarding School"
    age="seventeen (17) years old"
    # Kirim data ke profil.html
    return render_template('profil.html',
                           user_name=name,
                           user_hobby=hobby,
                           user_school=school,
                           user_age=age)

# Buat Halaman Daftar Teman Dinamis
@app.route('/teman')
def daftar_teman():
    daftar_teman = ["Abdulloh", "Farros", "Bariq", "Musa", "Faiz"]
    return render_template('teman.html', teman=daftar_teman)

# Halaman About
@app.route('/about')
def about():
    return render_template('about.html')

# 5. (Opsional tapi bagus) Baris untuk menjalankan aplikasi
if __name__ == "__main__":
    app.run(debug=True)
