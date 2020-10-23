import hashlib

# variavel que guarda o que separa o login da hash de senha
separator = ";"

# noma do arquivo
file_users = "users2.txt"

# salt
salt = ''

# funcao que gera o hash em MD5
def func_md5(passwd):
    return hashlib.md5(passwd.encode()).hexdigest()

# ITEM1
def item3():
    op = int(input('Digite 1 se quer cadastrar e 2 caso quera logar: '))
    # if op == 1 -> cadastro
    if op == 1:
        print('-----Cadastro-----')
        print('Login e senha devem ter 4 digitos')
        login = input('login: ')
        passwd = input('senha: ')
        conf_passws = input('confirme a senha: ')

        # definindo o salt
        salt = login[len(login)-2:len(login)]

        if conf_passws == passwd: 
            # funcao MD5
            pass_md5 = func_md5(salt+passwd)
            data = login+separator+pass_md5

            # escrever em arquivo login;pass_md5
            with open(file_users, 'a') as f:
                f.write(data+"\n")
        else :
            print('Senha diferente da digitada. Encerrando sessao...')

    # if op == 2 -> login
    elif op == 2:
        print('-----Login-----')
        flag = False
        login = input('login: ')
        passwd = input('senha: ')
        # pegando o salt
        salt = login[len(login)-2:len(login)]
        with open(file_users, 'r') as f:
            lines = f.readlines()

            # loop para cada linha do arquivo
            for line in lines:
                # separando o login da hash
                # line_data[0] = login
                # line_data[1] = hash+\n
                line_data = line.split(separator)
                
                # caso login for correto
                if line_data[0] == login and line_data[1][:-1] == func_md5(salt+passwd):
                    # pegar o hash
                    print("LOGIN EFETUADO!")
                    flag = True
                    break

            # flag para printar caso o login ou senha estejam errados
            if not flag:
                print("Login ou senha incorretos")

    else:
        print(f"Operacao {op} nao reconhecida, encerrando o programa")

def main():
    item3()

if __name__ == '__main__':
    main()
