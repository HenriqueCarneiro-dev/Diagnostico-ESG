import sys

from dados.missoes import missoes
from dados.perguntas import perguntas
from interface.telas import (
    limpar_tela,
    mostrar_cabecalho,
    mostrar_comparacao,
    mostrar_historico,
    mostrar_menu,
    mostrar_niveis,
    mostrar_plano,
    mostrar_resultado,
)
from sistema.analise import (
    analisar,
    calcular_nota_geral,
    gerar_plano_de_acao,
)
from sistema.diagnostico import realizar_diagnostico
from sistema.historico import (
    carregar_historico,
    salvar_diagnostico,
    ultimo_diagnostico,
)


def executar_diagnostico():
    limpar_tela()
    mostrar_cabecalho()
    print("\nResponda com o número da opção. Não existe resposta certa ou errada.")

    respostas = realizar_diagnostico(perguntas)
    pilares = analisar(respostas)
    geral = calcular_nota_geral(respostas)
    plano = gerar_plano_de_acao(respostas, missoes)
    anterior = ultimo_diagnostico()

    limpar_tela()
    mostrar_resultado(pilares, geral)
    mostrar_niveis(pilares, geral)
    mostrar_comparacao(pilares, geral, anterior)
    mostrar_plano(plano)

    salvar_diagnostico(pilares, geral, plano)
    print("\nDiagnóstico salvo no histórico.")
    input("\nPressione Enter para voltar ao menu...")


def ver_historico():
    limpar_tela()
    mostrar_historico(carregar_historico())
    input("\nPressione Enter para voltar ao menu...")


def main():
    # Evita erro de acentuação em terminais Windows antigos.
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass

    aviso = ""
    while True:
        limpar_tela()
        mostrar_cabecalho()
        mostrar_menu()
        if aviso:
            print(f"\n{aviso}")
        escolha = input("\nEscolha: ").strip()
        aviso = ""

        if escolha == "0":
            print("Até logo!")
            break
        elif escolha == "1":
            executar_diagnostico()
        elif escolha == "2":
            ver_historico()
        else:
            aviso = "Opção inválida. Digite 1, 2 ou 0."


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nEncerrado.")
