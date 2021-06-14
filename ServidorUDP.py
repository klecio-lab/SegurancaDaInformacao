import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket Criado com Sucesso")

host = '192.168.1.105'
port = 5432

s.bind((host, port))
mensagem = '\nServidor: Boa kleciooo'

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print('Servidor enviando mensagem...')
        s.sendto(dados + mensagem.encode(), end)
