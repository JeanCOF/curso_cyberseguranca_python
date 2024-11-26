
import string
import random

def gera_senha() -> None:
    while True:  
        print("Bem-vindo ao gerador de Senhas")
        i = input("Digite '1' para iniciar ou '0' para encerrar: ")

        if i == '0':  # Encerra o programa
            print("Encerrando o gerador de senhas.")
            break
        
        if i == '1':  # Inicia a geração de senha
            print("========== Gerador de Senha ==========")
            print("Tipos:\n"
                  "1) Letras minúsculas\n"
                  "2) Letras maiúsculas\n"
                  "3) Caracteres especiais\n"
                  "4) Dígitos\n"
                  "5) Todos os anteriores (recomendado)\n ")

            valido = False
            while not valido:  
                tipo_de_senha = int(input("Digite o tipo de senha escolhido: "))
                if tipo_de_senha in [1, 2, 3, 4, 5]: #valida se o tipo de senha é valido
                    tamanho_da_senha = int(input("Digite o tamanho desejado para a senha: "))
                    if tamanho_da_senha >= 4:
                        valido = True
                    else:
                        print("Digite um tamanho de senha válido (mínimo de 4 caracteres)")
                else:
                    print("Digite um tipo de senha válido")

            # Gerando a senha com base na escolha do usuário
            if tipo_de_senha == 1:
                caracteres = string.ascii_lowercase # Letras minusculas
            elif tipo_de_senha == 2:
                caracteres = string.ascii_uppercase # Letras maiusculas
            elif tipo_de_senha == 3:
                caracteres = string.punctuation  # Caracteres especiais
            elif tipo_de_senha == 4:
                caracteres = string.digits  # Dígitos
            elif tipo_de_senha == 5:
                caracteres = string.ascii_letters + string.digits + string.punctuation  # Todos

            senha = "".join(random.choice(caracteres) for _ in range(tamanho_da_senha))

            print(f"============== Senha Gerada ==============")
            print(f"Copie sua senha: {senha}")
        else:
            print("Opção inválida, digite '1' para iniciar ou '0' para encerrar.")

# Chamada da função sem argumentos
gera_senha()