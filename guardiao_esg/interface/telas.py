"""Tudo que é exibido no terminal fica aqui."""

import os

from sistema.analise import definir_nivel
from sistema.config import LARGURA_BARRA, LARGURA_TELA


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def _linha():
    print("=" * LARGURA_TELA)


def _titulo(texto):
    print()
    _linha()
    print(texto.center(LARGURA_TELA))
    _linha()


def _barra(percentual):
    cheio = round(percentual / 100 * LARGURA_BARRA)
    return "#" * cheio + "." * (LARGURA_BARRA - cheio)


def mostrar_cabecalho():
    _linha()
    print("GUARDIÃO ESG".center(LARGURA_TELA))
    print("Diagnóstico simples para o seu restaurante".center(LARGURA_TELA))
    _linha()


def mostrar_menu():
    print("\n1 - Realizar diagnóstico")
    print("2 - Ver histórico")
    print("0 - Sair")


def mostrar_resultado(pilares, geral):
    _titulo("SEU DIAGNÓSTICO")
    for pilar, percentual in pilares.items():
        print(f"{pilar:<12} [{_barra(percentual)}] {percentual:5.1f}%")
    print("-" * LARGURA_TELA)
    print(f"{'Geral':<12} [{_barra(geral)}] {geral:5.1f}%")


def mostrar_niveis(pilares, geral):
    _titulo("NÍVEL DE MATURIDADE")
    nome, explicacao = definir_nivel(geral)
    print(f"Geral: {nome}")
    print(explicacao)
    print()
    for pilar, percentual in pilares.items():
        nome_pilar, _ = definir_nivel(percentual)
        print(f"{pilar}: {nome_pilar}")


def mostrar_comparacao(pilares, geral, anterior):
    """Compara com o diagnóstico anterior, se existir."""
    if not anterior:
        return
    _titulo(f"EVOLUÇÃO (desde {anterior['data']})")
    linhas = [("Geral", anterior.get("geral"), geral)]
    linhas += [
        (pilar, anterior.get("pilares", {}).get(pilar), atual)
        for pilar, atual in pilares.items()
    ]
    for nome, antes, agora in linhas:
        if antes is None:
            continue
        diferenca = agora - antes
        print(f"{nome:<12} {antes:5.1f}% -> {agora:5.1f}%  ({diferenca:+.1f})")


def mostrar_plano(plano):
    _titulo("PLANO DE AÇÃO")
    if not plano:
        print("Parabéns! Suas respostas mostram boas práticas em todas as áreas.")
        print("Continue acompanhando e refaça o diagnóstico daqui a 3 meses.")
        return

    for item in plano:
        print(f"\nSemana {item['semana']} - {item['pilar']}")
        print(f"  Missão: {item['titulo']}")
        print(f"  Como fazer: {item['como_fazer']}")
        print(f"  Custo: {item['custo']}")
        print(f"  Benefício: {item['beneficio']}")


def mostrar_historico(historico):
    _titulo("HISTÓRICO DE DIAGNÓSTICOS")
    if not historico:
        print("Nenhum diagnóstico salvo ainda.")
        return
    for registro in historico:
        pilares = " | ".join(
            f"{pilar[:3]}: {valor:.0f}%" for pilar, valor in registro["pilares"].items()
        )
        print(f"{registro['data']}  Geral: {registro['geral']:5.1f}%  ({pilares})")
