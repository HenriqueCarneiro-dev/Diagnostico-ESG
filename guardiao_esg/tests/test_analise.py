import pytest

from dados.missoes import missoes
from dados.perguntas import perguntas
from sistema.analise import (
    analisar,
    calcular_nota_geral,
    calcular_percentual,
    definir_nivel,
    gerar_plano_de_acao,
)


def resposta(id_, pilar, pontos):
    return {"id": id_, "pilar": pilar, "pontos": pontos}


def todas_com(pontos):
    return [resposta(p["id"], p["pilar"], pontos) for p in perguntas]


# ---------- percentual ----------

def test_percentual_minimo_e_zero():
    assert calcular_percentual([0, 0, 0]) == 0


def test_percentual_maximo_e_cem():
    assert calcular_percentual([3, 3, 3]) == 100


def test_percentual_intermediario():
    assert calcular_percentual([3, 0]) == pytest.approx(50)


def test_percentual_lista_vazia():
    assert calcular_percentual([]) == 0


# ---------- análise ----------

def test_analisar_agrupa_por_pilar():
    respostas = [
        resposta("a", "Ambiental", 3),
        resposta("b", "Ambiental", 3),
        resposta("c", "Social", 0),
    ]
    resultado = analisar(respostas)
    assert resultado == {"Ambiental": 100, "Social": 0}


def test_analisar_inclui_pilar_novo():
    resultado = analisar([resposta("x", "Novo Pilar", 3)])
    assert resultado == {"Novo Pilar": 100}


def test_nota_geral():
    respostas = [resposta("a", "Ambiental", 3), resposta("b", "Social", 0)]
    assert calcular_nota_geral(respostas) == pytest.approx(50)


# ---------- níveis ----------

@pytest.mark.parametrize("percentual,esperado", [
    (0, "Inicial"),
    (25, "Inicial"),
    (25.1, "Em desenvolvimento"),
    (50, "Em desenvolvimento"),
    (75, "Estruturado"),
    (75.1, "Avançado"),
    (100, "Avançado"),
])
def test_definir_nivel(percentual, esperado):
    nome, explicacao = definir_nivel(percentual)
    assert nome == esperado
    assert explicacao


# ---------- plano de ação ----------

def test_plano_vazio_quando_tudo_bom():
    assert gerar_plano_de_acao(todas_com(3), missoes) == []


def test_plano_vazio_quando_respostas_medianas():
    # 2 pontos (Frequentemente) não precisa de missão
    assert gerar_plano_de_acao(todas_com(2), missoes) == []


def test_plano_respeita_limite_de_missoes():
    plano = gerar_plano_de_acao(todas_com(0), missoes)
    assert len(plano) == 4


def test_plano_e_personalizado():
    respostas = todas_com(3)
    # só a água e o lixo estão ruins
    respostas[0] = resposta("agua", "Ambiental", 0)
    respostas[3] = resposta("residuos", "Ambiental", 1)
    plano = gerar_plano_de_acao(respostas, missoes)
    assert [item["id"] for item in plano] == ["agua", "residuos"]


def test_plano_numera_semanas():
    plano = gerar_plano_de_acao(todas_com(0), missoes)
    assert [item["semana"] for item in plano] == [1, 2, 3, 4]


def test_plano_prioriza_piores_notas():
    respostas = todas_com(3)
    respostas[0] = resposta("agua", "Ambiental", 1)
    respostas[6] = resposta("fornecedores_locais", "Social", 0)
    plano = gerar_plano_de_acao(respostas, missoes)
    assert plano[0]["id"] == "fornecedores_locais"


def test_plano_distribui_entre_pilares_em_caso_de_empate():
    plano = gerar_plano_de_acao(todas_com(0), missoes)
    pilares = {item["pilar"] for item in plano}
    assert len(pilares) > 1


def test_plano_traz_dados_da_missao():
    plano = gerar_plano_de_acao(todas_com(0), missoes)
    for item in plano:
        for campo in ("titulo", "como_fazer", "custo", "beneficio"):
            assert item[campo]
