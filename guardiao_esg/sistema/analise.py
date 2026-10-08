"""Cálculo das notas, níveis de maturidade e plano de ação."""

from sistema.config import (
    LIMITE_RESPOSTA_BAIXA,
    MAX_MISSOES,
    NIVEIS,
    PONTOS_MAXIMO,
)


def calcular_percentual(pontos):
    """Converte uma lista de pontos (0 a 3) em percentual de 0 a 100.

    Quem responde o mínimo em tudo fica com 0% e quem responde o máximo
    em tudo fica com 100%.
    """
    if not pontos:
        return 0.0
    return sum(pontos) / (len(pontos) * PONTOS_MAXIMO) * 100


def analisar(respostas):
    """Devolve o percentual de cada pilar, ex.: {"Ambiental": 58.3, ...}.

    Os pilares são lidos das próprias respostas, então um pilar novo
    criado em perguntas.py é incluído automaticamente.
    """
    pontos_por_pilar = {}
    for resposta in respostas:
        pontos_por_pilar.setdefault(resposta["pilar"], []).append(resposta["pontos"])

    return {
        pilar: calcular_percentual(pontos)
        for pilar, pontos in pontos_por_pilar.items()
    }


def calcular_nota_geral(respostas):
    """Percentual geral, considerando todas as respostas."""
    return calcular_percentual([r["pontos"] for r in respostas])


def definir_nivel(percentual):
    """Devolve (nome do nível, explicação curta) para um percentual."""
    for limite, nome, explicacao in NIVEIS:
        if percentual <= limite:
            return nome, explicacao
    # Percentual acima de 100 (não deveria ocorrer): último nível.
    return NIVEIS[-1][1], NIVEIS[-1][2]


def gerar_plano_de_acao(respostas, missoes, max_missoes=MAX_MISSOES):
    """Monta o plano a partir das respostas fracas.

    - Só entram respostas com nota baixa (0 ou 1 ponto).
    - As piores notas vêm primeiro.
    - Em caso de empate, prefere pilares ainda pouco representados,
      para o plano não ficar concentrado em um único pilar.
    - Cada missão é uma semana: Semana 1, Semana 2, ...
    Se estiver tudo bem, devolve uma lista vazia.
    """
    candidatas = [
        (posicao, r)
        for posicao, r in enumerate(respostas)
        if r["pontos"] <= LIMITE_RESPOSTA_BAIXA and r["id"] in missoes
    ]
    escolhidas_por_pilar = {}
    plano = []

    while candidatas and len(plano) < max_missoes:
        posicao, resposta = min(
            candidatas,
            key=lambda c: (
                c[1]["pontos"],
                escolhidas_por_pilar.get(c[1]["pilar"], 0),
                c[0],
            ),
        )
        candidatas.remove((posicao, resposta))
        escolhidas_por_pilar[resposta["pilar"]] = (
            escolhidas_por_pilar.get(resposta["pilar"], 0) + 1
        )

        plano.append({
            "semana": len(plano) + 1,
            "id": resposta["id"],
            "pilar": resposta["pilar"],
            **missoes[resposta["id"]],
        })

    return plano
