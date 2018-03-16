# Import library xmlrpc
import xmlrpc.client

# Inisiasi proxy ke server
proxy = xmlrpc.client.ServerProxy("http://localhost:7778/")

penjumlahan = proxy.penjumlahan(20,10)
pengurangan = proxy.pengurangan(20,10)
perkalian = proxy.perkalian(20,10)
pembagian = proxy.pembagian(20,10)
prima1 = proxy.isPrima(22)
prima2 = proxy.isPrima(17)

print("Hasil Penjumalahan : ", penjumlahan)
print("Hasil Pengurangan : ", pengurangan)
print("Hasil Perkalian : ", perkalian)
print("Hasil Pembagian : ", pembagian)
print("Is Prima : ", prima1)
print("Is Prima : ", prima2)