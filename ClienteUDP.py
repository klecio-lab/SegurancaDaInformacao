import socket

#criei o objeto de conexão
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Cliente Socket Criado com Sucesso!!!")

host = 'localhost'
porta = 5433
mensagem = 'O pai tá fazendo segurança da informação'

try:
    print('Cliente: ' + mensagem)
    s.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print("Cliente: " + dados)
finally:
    print("Cliente: fechando a Conexão")
    s.close()
