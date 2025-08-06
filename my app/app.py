from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def halaman_utama():
    # Kirim data dari Python ke HTML
    nama = "Siti Azizah"
    pesan = "Selamat datang di website sederhana!"
    return render_template('index.html', nama=nama, pesan=pesan)

if __name__ == '__main__':
    app.run(debug=True)
