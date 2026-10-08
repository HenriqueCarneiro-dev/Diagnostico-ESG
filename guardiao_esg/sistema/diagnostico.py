"""Aplicação do questionário."""

from sistema.config import ESCALAS


def realizar_diagnostico(perguntas, entrada=input, saida=print):
    """Faz todas as perguntas e devolve a lista de respostas.

    Cada resposta é um dicionário: {"id", "pilar", "pontos"} com pontos de 0 a 3.
    Os parâmetros `entrada` e `saida` existem para facilitar os testes.
    """
    respostas = []
    total = len(perguntas)

    for numero, item in enumerate(perguntas, start=1):
        opcoes = ESCALAS[item["tipo"]]

        saida(f"\n[{numero}/{total}] {item['pilar']}")
        saida(item["pergunta"])
        for indice, texto in enumerate(opcoes, start=1):
            saida(f"  {indice} - {texto}")

        while True:
            digitado = entrada("Sua resposta: ").strip()

            if not digitado.isdigit():
                saida("Digite apenas números.")
                continue

            escolha = int(digitado)
            if not 1 <= escolha <= len(opcoes):
                saida(f"Digite uma opção entre 1 e {len(opcoes)}.")
                continue

            respostas.append({
                "id": item["id"],
                "pilar": item["pilar"],
                "pontos": escolha - 1,  # 1..4 vira 0..3
            })
            break

    return respostas
