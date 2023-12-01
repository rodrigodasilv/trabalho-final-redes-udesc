import socket
import threading
import select


def gerenciadorConexao(socketClient, ipClient, portaClient):
    # Printa na tela e salva em arquivo as conexoes
    print(f'IP cliente: {ipClient} Porta cliente:{portaClient}\n')
    logs = open('logs.txt', 'a')
    logs.write(f'IP cliente: {ipClient} Porta cliente:{portaClient}\n')
    logs.close()
    #Espera ate o cliente requisitar algo
    ready, _, _ = select.select([socketClient], [], [], 1)
    if ready:
        request = socketClient.recv(1024).decode('utf-8')
    if request == 'html':  # Cliente solicitou html
        f = open('index.html', 'w')
        #Monta página HTML
        f.write(f"""<!DOCTYPE html>
                <html lang='pt-br'>
                <head>
                <meta charset='UTF-8'>
                <title>O que eh um servidor http?</title>
                </head>
                <body>
                    <p>Porta utilizada : {portaClient}</p>
                    <p>IP do Cliente : {ipClient}</p>
                    <p>Um servidor HTTP eh como um amigo magico que traz o que voce pede na internet.</p>
                    <img src='servidor.png' alt='Imagem de um servidor'>
                </body>
                </html>""")
        f.close()
        f = open('index.html', 'rb')
        #Envia página HTML
        socketClient.sendall(f.read())
        f.close()
    #Espera o cliente requisitar a imagem
    ready, _, _ = select.select([socketClient], [], [], 2)  
    if ready:
        request = socketClient.recv(1024).decode('utf-8')
    if request == 'png':  # Cliente solicitou png
        png = open('servidor.png', 'rb')
        #Envia imagem
        socketClient.sendall(png.read())
        png.close()
    #Espera o cliente desconectar
    ready, _, _ = select.select([socketClient], [], [], 1)
    if ready:
        request = socketClient.recv(1024).decode('utf-8')
    if request == 'disconnect':  # Cliente solicitou desconexão
        socketClient.shutdown(socket.SHUT_WR)
    socketClient.close()


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria um socket
ipServer = socket.gethostname()  # IP do Servidor
portaServer = 9000  # Porta do servidor.
sock.bind((ipServer, portaServer))  # Faz o bind para o socket
sock.listen()  # Espera o client.
while True:
    conexao, (ipClient, portaClient) = sock.accept()  # Conecta com o cliente.
    #Realiza tratamento do cliente em outra area de memoria
    threadGerenciadorConexao = threading.Thread(target=gerenciadorConexao, args=(conexao, ipClient, portaClient))
    threadGerenciadorConexao.start()
