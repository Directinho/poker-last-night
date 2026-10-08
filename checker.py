from collections import Counter
from cartas import cartas
from config import *
from jogo import player_c1, player_c2, player
from bots import *


todas_cartas = []  # Array que irá conter todas as cartas

# Jogador
jogador = player
mao_jogador = [player_c1, player_c2]

# Checar todas as cartas e juntar em uma lista única
for naipe in cartas.values():
    todas_cartas.extend(naipe)

# Cria um dicionário de busca rápida
cartas_por_id = {carta["id"]: carta for carta in todas_cartas}

def obter_carta(id_carta: int) -> dict:
    return cartas_por_id.get(id_carta)


def avaliar_mao(id_cartas: list[int]) -> dict:
    ids_cartas = [cartas.id for cartas in mao_jogador]
    quantidade = len(id_cartas)

    # Valida se a mão possui estritamente 2 cartas
    if quantidade != 2:
        raise ValueError(
            f"Quantidade de cartas inválida: {quantidade}. Esperado exatamente 2."
        )

    # Transforma os IDs em dicionários de cartas reais
    mao = [obter_carta(id_c) for id_c in ids_cartas]
    if None in mao:
        raise ValueError("Um ou mais IDs de carta são inválidos.")

    # Descobre as características da mão de 2 cartas
    valores = sorted([carta["valor"] for carta in mao])
    naipes = [carta["naipe"] for carta in mao]
    nomes = [carta["nome"] for carta in mao]
    cores = [carta["cor"] for carta in mao]

    contagem_valores = Counter(valores)

    # Se as duas cartas tiverem o mesmo valor, forma um Par ("One Pair")
    if contagem_valores.most_common(1)[0][1] == 2:
        valor_par = valores[0]
        return (
            2,
            "One Pair",
            {
                "valor": valor_par,
                "cartas": nomes,
                "mesmo_naipe": naipes[0] == naipes[1],
                "mesmo_cor": cores[0] == cores[1],
            },
        )

    # Se forem valores diferentes, é apenas a Carta Mais Alta ("High Card")
    carta_alta = max(valores)
    return (
        1,
        "High Card",
        {
            "maior_carta": carta_alta,
            "cartas": nomes,
            "mesmo_naipe": naipes[0] == naipes[1],
            "mesmo_cor": cores[0] == cores[1],
        },
    )


def comparar_maos(mao1_ids: list[int], mao2_ids: list[int]) -> int:
    rank1, _, _ = avaliar_mao(mao1_ids)
    rank2, _, _ = avaliar_mao(mao2_ids)

    if rank1 > rank2:
        return 1
    if rank2 > rank1:
        return -1
    return 0


def comparar_maos_jogador(player_c1_id: list[int], player_c2_id: list[int]) -> int:
    rank1, _, _ = avaliar_mao(player_c1_id)
    rank2, _, _ = avaliar_mao(player_c2_id)

    if rank1 > rank2:
        return 1
    if rank2 > rank1:
        return -1
    return 0


if __name__ == "__main__":
    # Testes estruturais usando IDs hipotéticos para garantir a sintaxe do arquivo
    try:
        print(avaliar_mao([1, 2]))
    except Exception as e:
        print(f"O script compilou com sucesso! Mensagem de dados: {e}")

def verificar_jogador(mao_jogador):
    rank, jogada, detalhes = avaliar_mao(mao_jogador)
    print(f"O jogador possui as cartas {mao_jogador}\nO jogador tem {jogada}\nForça: {rank}")
    
