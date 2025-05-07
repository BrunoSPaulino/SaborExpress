import os
import sys

restaurantes = [{"Nome":"Praça", "Categoria": "Japonesa", "Ativo":False}, 
                {"Nome":"Subway", "Categoria": "Americana", "Ativo":False},
                {"Nome":"Pizzaria da Bela", "Categoria": "Italiana", "Ativo":True}
]

def exibir_nome_do_programa():
    print("🆂 🅰 🅱 🅾 🆁   🅴 🆇 🅿 🆁 🅴 🆂 🆂\n")

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alterar estado do restaurante")
    print("4. Sair")

def finalizar_app():
    exibir_subtitulo("Finalizando o app...")

def voltar_ao_menu_principal():
    input("Digite uma tecla para voltar ao menu principal. \n")
    main()

def opcao_invalida():
    print("Opção inválida. Tente novamente. \n")
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system("cls")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    """
    Esta função é responsável por cadastrar um novo restaurante.
    
    Inputs:
    - nome_do_restaurante (str): O nome do novo restaurante.
    - categoria (str): A categoria do novo restaurante.

    Outputs:
    - Adiciona o novo restaurante ao array de restaurantes.
    """
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite a categoria do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {"Nome":nome_do_restaurante, "Categoria": categoria, "Ativo":False}
    restaurantes.append(dados_do_restaurante)
    print(f"Restaurante '{nome_do_restaurante}' cadastrado com sucesso!\n")
    voltar_ao_menu_principal()
pass

def listar_restaurantes():
    exibir_subtitulo("Listando restaurantes")
    print("Nome do restaurante".ljust(22) + " | Categoria".ljust(23) + " | Status\n")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["Nome"]
        categoria_restaurante = restaurante["Categoria"]
        ativo = "Ativo" if restaurante["Ativo"] else "Inativo"
        print(f"* {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}\n")
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo("Alterando estado dos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    for restaurante in restaurantes:
        if restaurante["Nome"] == nome_do_restaurante:
            restaurante["Ativo"] = not restaurante["Ativo"]
            status = "Ativo" if restaurante["Ativo"] else "Inativo"
            print(f"Restaurante '{nome_do_restaurante}' alterado com sucesso! Status: {status}\n")
            voltar_ao_menu_principal()
            return
    print(f"Restaurante '{nome_do_restaurante}' não encontrado.\n")
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("\nEscolha uma opção: "))
        # print(f"Você escolheu a opção {opcao_escolhida}")
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()
        
def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()