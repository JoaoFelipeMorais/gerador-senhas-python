import random           # Módulo para gerar valores aleatórios
import string as st     # Módulo string para acessar conjuntos de caracteres (letras, números, pontuação)
import sys              # Módulo sys usado aqui para encerrar o programa em caso de erro
import pyperclip        # Módulo para copiar a senha gerada diretamente para a área de transferência

# Função principal que gera a senha
def gerador_Senha():
    # Solicita ao usuário o número de caracteres desejados para a senha
    n_caracteres = int(input("Quantos caracteres sua senha deve ter? "))

    # Lista que armazenará os conjuntos de caracteres escolhidos
    caracteres_escolhidos = []

    # Dicionário que mapeia os números às categorias de caracteres
    opcoes = {
        "1": st.ascii_lowercase,
        "2": st.ascii_uppercase,
        "3": st.digits,
        "4": st.punctuation
    }

    # Exibe as opções disponíveis ao usuário
    print("[1] letras minusculas\n[2] letras maiusculas\n[3] numeros\n[4] numeros especiais")

    # Solicita ao usuário que digite os tipos de caracteres desejados na senha (ex: 123 para minúsculas, maiúsculas e números)
    escolhas = (input("Quais tipos de caracteres deve conter na senha? (digite os numeros que deseja ex: 123) "))

    # Itera sobre cada caractere digitado pelo usuário (ex: "123" -> '1', '2', '3')
    for digito in escolhas:
        if digito in opcoes:
            # Se o dígito for válido, adiciona o conjunto de caracteres correspondente à lista
            caracteres_escolhidos.append(opcoes[digito])
        else:
            # Se o dígito não for válido, exibe mensagem de erro e encerra o programa
            print("Escolha Invalida, Encerrando o programa.")
            sys.exit()

    # Verifica se ao menos uma categoria de caracteres foi selecionada
    if caracteres_escolhidos:
        # Une todos os conjuntos escolhidos em uma única string com todos os caracteres possíveis
        conjunto_total = "".join(caracteres_escolhidos)

        # Gera a senha com o número de caracteres definidos, escolhendo aleatoriamente do conjunto total
        senha = "".join(random.choices(conjunto_total, k=n_caracteres))

        # Copia a senha gerada para a área de transferência usando pyperclip
        pyperclip.copy(senha)

        # Exibe a senha ao usuário
        print(f"A senha gerada foi: {senha}")
        print("A senha foi copiada automaticamente para a área de transferência.")
    else:
        # Se nenhum tipo de caractere foi escolhido, não é possível gerar a senha
        print("Nenhum tipo de caractere selecionado. Não é possível gerar a senha.")

# Chamada da função para iniciar o processo
gerador_Senha()
