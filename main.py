import os
import subprocess
import sys

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def opcao_invalida():
    print('Opção Inválida\n')
    input('\nDigite Enter para voltar ao menu: ')

def comecar_jogo(jogador):
    try:
        subprocess.run([sys.executable, "jogo.py"])
    except Exception as e:
        print(f"Erro ao abrir o jogo: {e}")
        input('\nDigite Enter para voltar ao menu: ')

def creditos():
    print("\nDesenvolvido por DirectDev")
    print("🐈 Github: https://github.com/Directinho\n")
    input('\nDigite Enter para voltar ao menu: ')

def iniciar():
    limpar_tela()
    print("Insira seu Nome (Se deixar vazio: Player)")
    print("Digite 'sair' para voltar ao Menu\n")
    
    nome = input("Insira o Nome do Jogador: ").strip()
    
    if nome.lower() == "sair":
        return   
    
    if nome == "":
        nome = "Player"
    
    comecar_jogo(nome)

def exibir():
    print("Bem Vindo ao Poker Last Night")
    print("Um jogo de Poker feito em python\n")
    print("1 - Iniciar Jogo")
    print("2 - Créditos")
    print("3 - Sair")

def main():
    limpar_tela()
    exibir()
    while True:
        try:
            opcao = int(input('\nInsira uma opção: '))
            
            if opcao == 1:
                iniciar()
                break
            elif opcao == 2:
                limpar_tela()
                creditos()
            elif opcao == 3:
                limpar_tela()
                print("Fechando o programa...")
            else:
                opcao_invalida()
                
        except ValueError:
            opcao_invalida()

if __name__ == '__main__':
    main()