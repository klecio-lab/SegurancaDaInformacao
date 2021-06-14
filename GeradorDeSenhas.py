import random, string

tamanho = int(input("DIGITE O TAMANHO DA SENHA A SER GERADA"))

chars = string.ascii_letters + string.digits + '!@#$%*()-=,.;:/?'

#print(chars)
rnd = random.SystemRandom() #os.urandom

print(''.join(rnd.choice(chars) for i in range(tamanho)))
