import sys
import os
from function import *
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
#bagian check semua depedensi sudah terinstall

app = Flask(__name__)
app.secret_key = "ini cuma testing"

UPLOAD_FOLDER = os.path.join(os.getcwd(), "upload")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if check() != 0:
    print("Mematikan aplikasi ada yang error")
    sys.exit(1)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/cmd", methods=['POST'])
def command():
    if request.method == 'POST':
        if 'seeService' in request.form:
            return f"{listService()}"

    return "notFound", 400
            

@app.route("/ups", methods=['POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "Error: Tidak ada bagian file di form HTML"

        f = request.files['file']

        if f.filename == '':
            return "Error: Kamu belum memilih file!"

        filename = secure_filename(f.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        f.save(file_path)
        return f"File '{filename}' berhasil diupload dengan aman!"

if __name__ == "__main__":
    app.run(debug="True", port="5000")
