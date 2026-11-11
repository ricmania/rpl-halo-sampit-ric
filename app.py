from flask import Flask, render_template, request
from datetime import datetime

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Fungsi menentukan salam berdasarkan jam server
def salam_waktu(jam):
    if 4 <= jam <= 10:
        return "Selamat pagi"
    elif 11 <= jam <= 14:
        return "Selamat siang"
    elif 15 <= jam <= 17:
        return "Selamat sore"
    else:
        return "Selamat malam"

@app.route('/', methods=['GET', 'POST'])
def index():
    # Mengambil tanggal dan waktu server saat ini
    sekarang = datetime.now()
    waktu_sekarang = sekarang.strftime("%d-%m-%Y %H:%M:%S")
    salam = salam_waktu(sekarang.hour)
    nama = None

    # Memeriksa apakah formulir dikirim via POST
    if request.method == 'POST':
        # Mengambil input nama dan menghapus spasi di awal/akhir
        nama = request.form.get('nama', '').strip()

    # Merender template HTML dengan data waktu, salam, dan nama
    return render_template('index.html', waktu=waktu_sekarang, nama=nama, salam=salam)

if __name__ == '__main__':
    # Menjalankan aplikasi pada server lokal (localhost) dalam mode debug
    app.run(debug=True)

