from dados.missoes import missoes
from dados.perguntas import perguntas
from sistema.config import ESCALAS


def test_ids_de_perguntas_sao_unicos():
    ids = [p["id"] for p in perguntas]
    assert len(ids) == len(set(ids))


def test_toda_pergunta_tem_missao():
    for p in perguntas:
        assert p["id"] in missoes, f"Sem missão para a pergunta {p['id']}"


def test_toda_missao_nasce_de_uma_pergunta():
    ids = {p["id"] for p in perguntas}
    for id_missao in missoes:
        assert id_missao in ids, f"Missão {id_missao} sem pergunta"


def test_tipos_de_pergunta_existem_nas_escalas():
    for p in perguntas:
        assert p["tipo"] in ESCALAS


def test_cada_pilar_tem_ao_menos_cinco_perguntas():
    contagem = {}
    for p in perguntas:
        contagem[p["pilar"]] = contagem.get(p["pilar"], 0) + 1
    assert set(contagem) == {"Ambiental", "Social", "Governança"}
    assert all(qtd >= 5 for qtd in contagem.values())


def test_missoes_tem_campos_obrigatorios():
    for id_missao, missao in missoes.items():
        for campo in ("titulo", "como_fazer", "custo", "beneficio"):
            assert missao.get(campo), f"{id_missao} sem {campo}"
