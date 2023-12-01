# Passo-a-passo para execução do programa

## Servidor

Para executar o servidor, abrir um terminal na pasta "server" e digitar o comando "python .\server.py"

## Cliente

Para executar o cliente, alterar o valor da variável "ipServer" no arquivo "client.py" para o IP do servidor. Posteriormente abrir um terminal na pasta "client" e digitar o comando "python .\client.py"

### Funcionamento do programa

O programa funciona através de uma conexão TCP e o servidor pode responder os seguintes comandos do cliente:

1. html : retorna o arquivo index.html
2. png : retorna o arquivo servidor.png
3. disconnect : finaliza a conexão com o cliente

Para cada cliente, o servidor cria uma Thread, onde altera o arquivo index.html para conter o IP e a porta do cliente e posteriormente o envia. Além disso, envia a imagem e permite a desconexão. O servidor também mantém um arquivo "logs.txt" com o IP e porta de cada cliente que conectou, além de listar na tela quando a conexão ocorre. 
