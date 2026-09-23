import os
import sys
import random
from data import datas as bots
nivel_bots = 0
nivel_jogo = 0
nivel_random = 0
coins = 1000
cheats = False
jogando = False
bot = bots


if len(sys.argv) > 1:
    jogador = sys.argv[1]
else:
    jogador = "Player"

def gerar_bots():
    print("Teste")
    bot1, bot2, bot3, bot4 = random.sample(bots["bots"], 4)

    print(bot1["nome"], bot1["icone"])  
    print(bot2["nome"], bot2["icone"])  
    print(bot3["nome"], bot3["icone"])  
    print(bot4["nome"], bot4["icone"])

def ligar_cheats():
    cheats = True
    print("CHEATS ATIVADO\n/adicionar {Número de LNCoins}- Adiciona LNCoins\n/remove_bot_{Nome do Bot} - Remove um dos bots\n/adicionar_bot - Adiciona um Bot\n\nPara mostrar os cheats novamente digite 'ch'")
def jogo():
    gerar_bots()


def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def ajuda():
    limpar()
    print("-------------------------------------")
    print("MENU DE AJUDA")
    print("1 - Sobre Poker")
    print("2 - Como funciona")
    print("-------------------------------------")
    print()
def facil():
    nivel_bots = 2
    nivel_jogo = 2
    nivel_random = 2
    coins = 50000
    limpar()
    print("-------------------------------------")
    print("👶 Modo Selecionado: Fácil👶 ")
    print(f"\nConfigurações do Multiplicador\n- Nível dos Bots: {nivel_bots}\n- Nível de Jogo: {nivel_jogo}\n -Nível de Random: {nivel_random}\n🪙LN Coins: {coins}\n")
    print("Digite qualquer coisa para começar o jogo\nDigite sair para voltar ao jogo")
    print("-------------------------------------")

    controle = input("\nDeseja iniciar o jogo: ")

    if controle == "sair".lower():
        jogo_configuracoes()
    else:
        jogo()

def normal():

    limpar()
    print("-------------------------------------")
    print(" Modo Selecionado: Normal ")
    print(f"\nConfigurações do Multiplicador\n- Nível dos Bots: {nivel_bots}\n- Nível de Jogo: {nivel_jogo}\n -Nível de Random: {nivel_random}\n🪙LN Coins: {coins}\n(Não será aplicado o multiplicador)\n")
    print("Digite qualquer coisa para começar o jogo\nDigite sair para voltar ao jogo")
    print("-------------------------------------")

    controle = input("\nDeseja iniciar o jogo: ")

    if controle == "sair".lower():
        jogo_configuracoes()
    else:
        jogo()
def dificil():
    nivel_bots = 4
    nivel_jogo = 4
    nivel_random = 4
    coins = 500
    limpar()
    print("-------------------------------------")
    print("💀Modo Selecionado: Dificil💀")
    print(f"\nConfigurações do Multiplicador\n- Nível dos Bots: {nivel_bots}\n- Nível de Jogo: {nivel_jogo}\n-Nível de Random: {nivel_random}\n🪙LN Coins: {coins}\n")
    print("Digite qualquer coisa para começar o jogo\nDigite sair para voltar ao jogo")
    print("-------------------------------------")
    controle = input("\nDeseja iniciar o jogo: ")
    if controle == "sair".lower():
        jogo_configuracoes()
    else:
        jogo()

def jogo_configuracoes():
    while True:
        limpar()
        print(f"Bem Vindo, {jogador}")
        print("Configurações de Jogo\n\n👶 1 - Modo Fácil\n🃏 2 - Modo Normal\n👹 3 - Modo Dificil\n\n")
        print("digite 'ajuda' se tiver com dúvidas\ndigite 'menu' para voltar\ndigite 'sair' para fechar Jogo\n")
        opcao = input("Insira a opção desejada: ")
        if opcao == "1":
            facil()
            break
        elif opcao == "2":
            normal()
            break
        elif opcao =="3":   
            dificil()
            break
        elif opcao == "ajuda".lower():
            ajuda()
            break
        elif opcao == "menu".lower():
            print("Menu")
            break
        elif opcao == "sair".lower():
            os.system('cls')
            print("Fechando Programa...")
            break
        else:
            print("Opção Invalida")

    
def main():
    jogo_configuracoes()
main()