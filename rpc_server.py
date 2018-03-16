# Import library xmlrpc
import xmlrpc.server

# Inisiasi server
server = xmlrpc.server.SimpleXMLRPCServer( ("0.0.0.0", 7778) )


def penjumlahan(a,b):
    return (a+b)

def pengurangan(a,b):
    return (a-b)

def perkalian(a,b):
    return (a*b)

def pembagian(a,b):
    return (a/b)

def isPrima(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):  
        if n%i==0:
            return False
    return True


server.register_function(penjumlahan, "penjumlahan")
server.register_function(pengurangan, "pengurangan")
server.register_function(perkalian, "perkalian")
server.register_function(pembagian, "pembagian")
server.register_function(isPrima, "Prima")

server.serve_forever()