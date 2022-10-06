import socket

 

localIP     = "10.10.17.191"

localPort   = 3000

bufferSize  = 1024

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

 

print("UDP server up and listening")

# Diccionario con las tuplas de direcciones, a los cuales se les envia los mensajes de los clientes
addresses = {}

# Listen for incoming datagrams

while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]
    addresses[address] = address
    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)

    # Sending message to clients
    for x in addresses:
        UDPServerSocket.sendto(clientMsg.encode('utf-8'), x)

    
    