import http.client
import json

ip_server = "127.0.0.1"
port_server = 7777

def get_mahasiswa():
    conn = http.client.HTTPConnection(ip_server, port=port_server)
   
    conn.request("GET", "/mahasiswa")
    data = conn.getresponse().read()
    data = data.decode('ascii')
    print(data)


def add_mahasiswa():
    conn = http.client.HTTPConnection(ip_server, port=port_server)
    header = {"Content-Type" : "application/json"}
    mhs = {
        "nim" : 87697987987,
        "nama" : "Sahlan",
    }

    json_mhs = json.dumps(mhs)
    conn.request("POST", "/mahasiswa", json_mhs, header)
    data = conn.getresponse().read()
    data = data.decode('ascii')
    print(data)

def update_mahasiswa():
    conn = http.client.HTTPConnection(ip_server, port=port_server)
    header = {"Content-Type" : "application/json"}
    mhs = {
        "nim" : 97980808998,
        "nama" : "CB",
    }
    json_mhs = json.dumps(mhs)
    conn.request("PUT", "/mahasiswa/update/2", json_mhs, header)
    data = conn.getresponse().read()
    data = data.decode('ascii')
    print(data)


def satu_mahasiswa():
    conn = http.client.HTTPConnection(ip_server, port=port_server)
    conn.request("GET", "/mahasiswa/0")
    data = conn.getresponse().read()
    data = data.decode('ascii')
    print(data)

def hapus_mahasiswa():
    conn = http.client.HTTPConnection(ip_server, port=port_server)
    conn.request("DELETE", "/mahasiswa/delete/2")
    data = conn.getresponse().read()
    data = data.decode('ascii')
    print(data)


def hapus_semuaMahasiswa():
    conn = http.client.HTTPConnection(ip_server, port=port_server)
    conn.request("DELETE", "/mahasiswa/deleteAll")
    data = conn.getresponse().read()
    data = data.decode('ascii')
    print(data)

#Untuk memanggil fungsi :

get_mahasiswa()
#add_mahasiswa()
#update_mahasiswa()
#satu_mahasiswa()
#hapus_mahasiswa()
#hapus_semuaMahasiswa()
