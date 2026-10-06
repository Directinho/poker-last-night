import os
import sys
import random
from cartas import cartas 
from data import datas as bots
from bots import gerar_bots, reset_cartas, revelar_cartas, revelar_bots
nivel_bots = 0
nivel_jogo = 0
nivel_random = 0
coins = 1000
cheats = False
jogando = False
reset = False
vez = 0
bot = bots
player_c1 = "" #Primeira carta do jogador
player_c2 = "" #Segunda carta do jogador

if len(sys.argv) > 1:
    jogador = sys.argv[1]
else:
    jogador = "Player"

def retorno():
    input("Clique em qualquer tecla: ")
    jogo_configuracoes(jogador)

def jogador_cartas():
    global player_c1, player_c2, player

    baralho = (
        cartas["espadas"] +
        cartas["paus"] +
        cartas["copas"] +
        cartas["ouros"]
    )

    player_c1, player_c2 = random.sample(baralho, 2)


def checar_bots():
    gerar_bots()
    revelar_bots()
    retorno()
def dev_mode():
    print("MODO DESENVOLVEDOR SELECIONADO\n1- Checar Cartas geradas\n2 -Checar Bots gerados\n3- Sair do Modo Desenvolvedor")

    dev_entrada = int(input("Insira o comando de desenvolvedor:\n>"))
    while True:
        if dev_entrada == 1:
            reset_cartas()
            revelar_cartas()
            retorno()
            break
        elif dev_entrada == 2:
            checar_bots()
            break
        elif dev_entrada == 3:
            jogo_configuracoes()
        else:
            print("Erro no Console de Desenvolvedor")
            
def jogador_passa():
    pass
def jogador_cobrar():
    pass
def jogador_aposta():
    pass
def erro_opcao():
    print("Opção não existente")
def jogador_fugir():
    pass
def jogo():
    reset = False
    if reset == False:
        while True:
            opcoes_jogo()

def menu():
    print("---------")
    print("MENU DE AJUDA\n1-Passa a Vez\n2- Cobra na partida\n3- Aposta\n4- Mostrar menu de ajuda\n5- Fugir da rodada ")
    print("---------")
def opcoes_jogo():
    jogador_cartas()
    
    while True:
        print("Suas Cartas\n", player_c1["icone"], " ", player_c1["nome"], "e", player_c2["icone"], " ", player_c2["nome"])

        opcao_jogador = int(input("Insira a sua opção:  "))
        if opcao_jogador == 1: # Passar
            jogador_passa()
        elif opcao_jogador == 2:
            jogador_cobrar()
        elif opcao_jogador == 3:
            jogador_aposta()
        elif opcao_jogador == 4:
            menu()
        elif opcao_jogador == 5:
            jogador_fugir()
        else:
            erro_opcao()
def iniciar_jogo():
    reset = True
    if reset == True:
        gerar_bots()
        reset_cartas() # Reseta as cartas dos bots
        opcoes_jogo()
        jogo()

def ligar_cheats():
    cheats = True
    print("CHEATS ATIVADO\n/adicionar {Número de LNCoins}- Adiciona LNCoins\n/remove_bot_{Nome do Bot} - Remove um dos bots\n/adicionar_bot - Adiciona um Bot\n\nPara mostrar os cheats novamente digite 'ch'")

    


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
    elif controle == "iniciar".lower():
        iniciar_jogo()
    elif controle == "devv".lower():
        dev_mode()
    else:
        iniciar_jogo()

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
        iniciar_jogo()
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
        iniciar_jogo()

def jogo_configuracoes(jogador):
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

    
#def iniciar():
 #   jogo_configuracoes(jogador)
#iniciar()
if __name__ == '__main__':
    jogo_configuracoes(jogador)

