import threading
import socket
import os

def escuchar(socket):
    while(True):
        data = socket.recv(1024)
        print(data.decode('utf-8')) 
def enviar(socket):
    while(True):
        entrada = input()
        socket.sendall(entrada.encode('utf-8'))
        if (entrada == 'quit' or entrada == 'shutdown'):
            print('closing socket')
            socket.close()
            os._exit(1)
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('10.10.17.168', 1234)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)


    
th1 = threading.Thread( target=escuchar, args=(sock, ) )
th2 = threading.Thread( target= enviar, args=(sock, ) )
th1.start()
th2.start()

