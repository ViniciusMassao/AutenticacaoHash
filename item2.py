import itertools, string
import hashlib
import time

# variavel que guarda o que separa o login da hash de senha
separator = ";"

# noma do arquivo
file_users = "users.txt"

# funcao que gera o hash em MD5
def func_md5(passwd):
    return hashlib.md5(passwd.encode()).hexdigest()


# funcao de forca bruta para encontrar a senha de quatro digitos
def brute_force(hash_passwd):
    # chrs tem chars que conseguem ser printados, conteudo de chrs na linha abaixo...
    # 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    chrs = string.printable.replace(' \t\n\r\x0b\x0c', '')

    # loop que tenta todas as combinacoes de characteres que tem em chrs
    # cada loop pega um character, resultado em 4 digitos que ele testa
    # todas as combinacoes possiveis
    for c1 in chrs:
        for c2 in chrs:
            for c3 in chrs:
                for c4 in chrs:
                    tentativa = c1+c2+c3+c4
                    # se encontrar a senha deve retornar a senha sem hash
                    if hash_passwd == func_md5(tentativa):
                        return tentativa
    # caso nao consiga encontrar a senha retorna -1
    return -1


# ITEM2
def item2():
    with open(file_users, 'r') as f:
        lines = f.readlines()
        # loop para cada linha do arquivo
        start = time.time()
        for line in lines:
            line_data = line.split(separator)
            
            # chamando a funcao de forca bruta
            passwd_brute_force = brute_force(line_data[1][:-1])
            
            # caso o retorna da funcao de forca bruta seja diferente de -1 entao
            # encontrou a senha
            if passwd_brute_force != -1:
                print(f'Login: {line_data[0]} - Senha: {passwd_brute_force}')
            else:
                print('Nao foi possivel encontrar a senha')         
        end = time.time()
        print(f'Tempo Forca Bruta: {end-start}')
		
def main():
    item2()

if __name__ == '__main__':
    main()