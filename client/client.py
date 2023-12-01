import socket
import select

ipServer = '192.168.0.105'
portaServer = 9000

socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
socketClient.connect((ipServer, portaServer)) #Conecta no servidor

socketClient.send('html'.encode('utf-8')) #Solicita o arquivo html
response = b''
html = open('index.html', 'wb')
response = socketClient.recv(1024)
while response:
    html.write(response)
    ready, _, _ = select.select([socketClient], [], [], 1)  # Use 1 segundo de timeout
    if not ready:
        break
    response = socketClient.recv(1024)

html.close()

response = b''
ready = b''
socketClient.send('png'.encode('utf-8')) #Solicita o arquivo png
png = open('servidor.png', 'wb')
ready, _, _ = select.select([socketClient], [], [], 1)  # Use 1 segundo de timeout
if ready:
    response = socketClient.recv(1024)
while response:
    png.write(response)
    ready, _, _ = select.select([socketClient], [], [], 1)  # Use 1 segundo de timeout
    if not ready:
        break
    response = socketClient.recv(1024)
png.close()

socketClient.send('disconnect'.encode('utf-8')) #Solicita a desconexão
socketClient.close()