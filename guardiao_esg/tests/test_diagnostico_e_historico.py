from dados.perguntas import perguntas
from sistema.diagnostico import realizar_diagnostico
from sistema.historico import (
    carregar_historico,
    salvar_diagnostico,
    ultimo_diagnostico,
)


def entrada_simulada(valores):
    fila = iter(valores)
    return lambda _texto: next(fila)


def silencio(*_args, **_kwargs):
    pass


# ---------- questionário ----------

def test_faz_todas_as_perguntas():
    respostas = realizar_diagnostico(
        perguntas,
        entrada=entrada_simulada(["4"] * len(perguntas)),
        saida=silencio,
    )
    assert len(respostas) == len(perguntas)


def test_converte_opcao_em_pontos():
    respostas = realizar_diagnostico(
        perguntas[:2],
        entrada=entrada_simulada(["1", "4"]),
        saida=silencio,
    )
    assert [r["pontos"] for r in respostas] == [0, 3]


def test_repete_a_pergunta_se_resposta_invalida():
    respostas = realizar_diagnostico(
        perguntas[:1],
        entrada=entrada_simulada(["abc", "9", "0", "", "2"]),
        saida=silencio,
    )
    assert len(respostas) == 1
    assert respostas[0]["pontos"] == 1


def test_resposta_guarda_id_e_pilar():
    respostas = realizar_diagnostico(
        perguntas[:1], entrada=entrada_simulada(["3"]), saida=silencio
    )
    assert respostas[0]["id"] == perguntas[0]["id"]
    assert respostas[0]["pilar"] == perguntas[0]["pilar"]


# ---------- histórico ----------

def test_historico_vazio_sem_arquivo(tmp_path):
    assert carregar_historico(tmp_path / "nao_existe.json") == []
    assert ultimo_diagnostico(tmp_path / "nao_existe.json") is None


def test_salvar_e_carregar(tmp_path):
    arquivo = tmp_path / "hist.json"
    plano = [{"id": "agua"}, {"id": "residuos"}]
    salvar_diagnostico({"Ambiental": 40.04}, 40.04, plano, arquivo, data="2026-10-07 10:00")

    historico = carregar_historico(arquivo)
    assert len(historico) == 1
    assert historico[0]["data"] == "2026-10-07 10:00"
    assert historico[0]["geral"] == 40.0
    assert historico[0]["pilares"] == {"Ambiental": 40.0}
    assert historico[0]["missoes"] == ["agua", "residuos"]


def test_historico_acumula_e_ultimo_e_o_mais_recente(tmp_path):
    arquivo = tmp_path / "hist.json"
    salvar_diagnostico({"Ambiental": 10}, 10, [], arquivo, data="2026-01-01 08:00")
    salvar_diagnostico({"Ambiental": 60}, 60, [], arquivo, data="2026-04-01 08:00")

    assert len(carregar_historico(arquivo)) == 2
    assert ultimo_diagnostico(arquivo)["geral"] == 60


def test_arquivo_corrompido_nao_quebra(tmp_path):
    arquivo = tmp_path / "hist.json"
    arquivo.write_text("isso nao e json", encoding="utf-8")
    assert carregar_historico(arquivo) == []
