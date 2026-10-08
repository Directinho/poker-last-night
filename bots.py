
import random
from data import datas as bots
from cartas import cartas 
from jogo import nivel_bots, nivel_jogo, nivel_random
from checker import *
import sys
import os
import heapq


# bot_escolha = ["Cobriu", "Apostou", "Fugiu"]
#nivel_bots = 0
#nivel_jogo = 0
# nivel_random = 0


def checar_nivel():
    print(f"Nivel do Bot: {nivel_bots}")
    print(f"Nivel do Jogo: {nivel_jogo}")
    print(f"Nivel do Random: {nivel_random}")

def gerar_bots():
    global bot1, bot2, bot3, bot4
    bot1, bot2, bot3, bot4 = random.sample(bots["bots"], 4)

    #print(bot1["nome"], bot1["icone"])  
    #print(bot2["nome"], bot2["icone"])  
    #print(bot3["nome"], bot3["icone"])  
   # print(bot4["nome"], bot4["icone"])

def reset_cartas():
    global bot1_c1, bot1_c2, bot2_c1, bot2_c2, bot3_c1, bot3_c2, bot4_c1, bot4_c2
    bot_baralho = (
    cartas["espadas"] +
    cartas["paus"] +
    cartas["copas"] +
    cartas["ouros"]
        )
    bot1_c1, bot1_c2 = random.sample(bot_baralho, 2)
    bot2_c1, bot2_c2 = random.sample(bot_baralho, 2)
    bot3_c1, bot3_c2 = random.sample(bot_baralho, 2)
    bot4_c1, bot4_c2 = random.sample(bot_baralho, 2)

def revelar_cartas():
    print(bot1["nome"],"|", bot1["icone"])   # Nome Bot
    print(bot1_c1["nome"], "|", bot1_c2["nome"])
    print(bot2["nome"], "|", bot2["icone"])  # Nome bot
    print(bot2_c2["nome"], "|", bot2_c2["nome"])
    print(bot3["nome"], "|", bot3["icone"])   # NOme bot
    print(bot3_c2["nome"], "|", bot3_c2["nome"])
    print(bot4["nome"], "|", bot4["icone"]) #nome bot
    print(bot4_c1["nome"], "|", bot4_c2["nome"])
def revelar_bots():
    print(bot1["nome"], bot1["icone"])  
    print(bot2["nome"], bot2["icone"])  
    print(bot3["nome"], bot3["icone"])  
    print(bot4["nome"], bot4["icone"])
def mesa():
    print("-------------------------------------")
    print(bot1["icone"],bot1["nome"], "-")
    print(bot2["icone"],bot2["nome"], "-")
    print(bot3["icone"],bot3["nome"], "-")

# BOT IA
class ia:
    def bot_ia(self, id, mao, nivel_bots, nivel_random):
        self.id = id
        self.mao =  mao
        self.nivel = nivel_bots
        self.random = nivel_random
        

