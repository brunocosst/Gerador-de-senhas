
# Gerador de Senhas em Python

import secrets
import string

# Define as cores utilizadas no terminal
verde = "\033[32m"
azul = "\033[34m"
amarelo = "\033[33m"
vermelho = "\033[31m"
reset = "\033[0m"

# Exibe o título do programa
print(azul + "=" * 40 + reset)
print(azul + "       GERADOR DE SENHAS" + reset)
print(azul + "=" * 40 + reset)

# Define os caracteres que podem aparecer na senha
caracteres = string.ascii_letters + string.digits + string.punctuation

# Solicita o tamanho da senha
tamanho = int(input("\nQuantos caracteres deseja na senha? "))

# Verifica se o tamanho da senha é válido
if tamanho < 8:
    print(vermelho + "\nErro! A senha deve ter pelo menos 8 caracteres." + reset)
else:
    # Gera uma senha aleatória
    senha = "".join(secrets.choice(caracteres) for i in range(tamanho))

    # Exibe a senha gerada
    print(amarelo + "\nGerando senha..." + reset)
    print(verde + "\nSua senha é: {}".format(senha) + reset)

print(azul + "\n" + "=" * 40 + reset)


#string.ascii_letters contém as letras maiúsculas e minúsculas do alfabeto.

#string.digits contém os números de 0 a 9.

#string.punctuation contém caracteres especiais, como !, @, # e $.

#secrets.choice(caracteres) escolhe um caractere aleatório de forma segura.