import socket
import sys

def main():
    try:
        #criando conexão com a placa de rede do computador
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    except socket.error as e:
        print("A conexão falhou!!!")
        print("Erro: {}".format(e))
        sys.exit()

    print("Socket Criado com sucesso")
    HostAlvo = input("Digite o Host ou IP a ser conectado: ")
    portaAlvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((HostAlvo, int(portaAlvo)))
        print('Cliente TCP conectado com Sucesso no Host ' + HostAlvo + ' e na porta alvo: ' + portaAlvo)
        s.shutdown(2)
    except socket.error as e:
        print("Não foi possivel conectar no host: " + HostAlvo + " e na porta: " + portaAlvo)
        print("Erro: {}".format(e))
        sys.exit()

if __name__ == "__main__":
    main()
        
