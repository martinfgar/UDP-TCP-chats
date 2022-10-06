import socket
import threading
import os

msgFromClient       = "Hello UDP Server"

bytesToSend         = str.encode(msgFromClient)

serverAddressPort   = ("10.10.17.255", 3000)

bufferSize          = 1024

def escuchar(sock):
    while(True):
        try:
            data = sock.recvfrom(bufferSize)
            print(data[0].decode('utf-8')) 
            print('Escriba su mensaje: ')
        except:
            sock.close()
            os._exit(1)
            

def enviar(sock):
    while(True):
        try:
            entrada = input()
            if (entrada == 'salir'):
                raise 
            sock.sendto(entrada.encode('utf-8'),serverAddressPort) 
        except:
            sock.close()
            os._exit(1)

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
print("Escriba 'salir' para cerrar el cliente")
 
th1 = threading.Thread(target=escuchar,args=(UDPClientSocket,))
th2 = threading.Thread(target=enviar, args=(UDPClientSocket,))

th1.start()
th2.start()