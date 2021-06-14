import os

print('-' * 60)
#pegando ip ou a host pra ser verificado
ip_ou_host = input("Digite o Ip ou host a ser verficado: ")
print('-' * 60)

os.system('ping -n 6 {}'.format(ip_ou_host))
