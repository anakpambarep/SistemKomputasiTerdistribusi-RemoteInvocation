from flask import Flask, request
import json

app = Flask("Data Mahasiswa")

data_mahasiswa = [
    {
        "nama" : "Novan",
        "nim" : 1515757657575
        
    },
    {
         "nama" : "Erdian",
        "nim" : 67558768686
       
    }
]

@app.route('/mahasiswa', methods=['GET'])

def get_all_mahasiswa():
    json_mahasiswa = json.dumps(data_mahasiswa)
    return json_mahasiswa

@app.route('/mahasiswa', methods=['POST'])

def create_mahasiswa():
   
    nim = request.json['nim']
    nama = request.json['nama']
   
    mahasiswa_baru = {
        "nama" : nama,
        "nim" : nim
        
    }
    
    data_mahasiswa.append(mahasiswa_baru)
   
    return "Add data success"


@app.route('/mahasiswa/<int:id>', methods=['GET'])

def satu_mahasiswa(id):
   
    data_mahasiswa_Satu = json.dumps(data_mahasiswa[id])
    return ("Masukkan data ke daftar" + "\n" + data_mahasiswa_Satu )


@app.route('/mahasiswa/update/<int:id>', methods=['PUT'])

def update_mahasiswa(id):
   
    nama = request.json['nama']
    nim = request.json['nim']
    
   
    mahasiswa_baru = {
        "nama" : nama,
        "nim" : nim
    
    }
 
    data_mahasiswa[id]=mahasiswa_baru
    return "Update data mahasiswa berhasil"


@app.route('/mahasiswa/hapus/<int:id>', methods=['DELETE'])

def hapus_mahasiswa(id):
   
    data_mahasiswa.pop(id)
    json_mahasiswa = json.dumps(data_mahasiswa)
    return ("Hapus data mahasiswa berhasil"+ "\n" +json_mahasiswa, )


@app.route('/mahasiswa/hapus semua', methods=['DELETE'])

def hapus_semuaMahasiswa():
   
    data_mahasiswa.clear()
    json_mahasiswa = json.dumps(data_mahasiswa)
    return ("Hapus semua data mahasiswa berhasil" + "\n" + json_mahasiswa,)


app.run(port=7777)