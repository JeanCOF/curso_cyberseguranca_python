###Estudo de Caso: Gerador de Senhas em Python

#Neste estudo de caso, vamos explorar o código de um gerador de senhas em
#Python, analisando sua estrutura, funcionamento e possíveis melhorias. O
#objetivo é entender como o código gera senhas de diferentes tipos e como
#podemos aprimorar a usabilidade e a segurança.

#1. Objetivo do Código
#O código apresentado cria um gerador de senhas que permite ao usuário
#escolher entre cinco tipos de senhas:
#Letras minúsculas
#Letras maiúsculas
#Caracteres especiais
#Dígitos
#Todos os tipos (recomendado)

#2. Estrutura do Código
#O código está dividido em várias seções:
#Importação de Módulos: O módulo random é utilizado para selecionar
#caracteres aleatórios, enquanto string fornece conjuntos de caracteres prontos
#(letras, dígitos, etc.).
#Menu Interativo: O usuário é apresentado a um menu para escolher o tipo de
#senha e o tamanho desejado.
#Funções de Geração de Senha:
#Cada função corresponde a um tipo de senha e utiliza a função
#random.choice() para selecionar caracteres aleatórios.
#Lógica de Seleção: Um bloco condicional (if-elif) determina qual função de
#geração de senha será chamada com base na entrada do usuário.

#3. Funcionamento
#Quando o usuário escolhe um tipo de senha e um tamanho, o código executa a
#função correspondente e imprime a senha gerada. A geração é feita utilizando
#um loop que concatena caracteres escolhidos aleatoriamente.

#4. Análise e Melhoria
#Embora o código funcione bem, existem algumas áreas onde podemos
#melhorá-lo:

#4.1 Validação de Entrada
#Atualmente, o código não valida se a entrada do usuário para o tipo de senha e
#tamanho é um número válido. Podemos adicionar verificações para garantir
#que as entradas sejam inteiras e dentro de um intervalo razoável.

#4.2 Melhorias na Usabilidade
#Podemos usar um loop para permitir que o usuário gere várias senhas sem
#reiniciar o programa, além de oferecer a opção de copiar a senha gerada para
#a área de transferência.

#4.3 Aumento da Segurança
#Podemos implementar um recurso que garante que a senha gerada tenha pelo
#menos um caractere de cada tipo (se o usuário escolher a opção "Todos os
#anteriores"), aumentando a segurança da senha.

#4.4 Modularidade
#Embora o código seja relativamente modular, podemos agrupar a lógica de
#geração em uma única função que aceita parâmetros, tornando o código mais
#limpo e fácil de manter.

#5. Comente todas as funções
#Comentários em programação é documentação.

#6. Apresente o código em grupos.

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