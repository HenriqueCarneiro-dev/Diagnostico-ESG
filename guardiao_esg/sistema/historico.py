"""Salva e lê os diagnósticos anteriores em um arquivo JSON."""

import json
from datetime import datetime
from pathlib import Path

CAMINHO_PADRAO = Path(__file__).resolve().parent.parent / "historico.json"


def carregar_historico(caminho=CAMINHO_PADRAO):
    """Lista de diagnósticos salvos (do mais antigo ao mais recente).

    Se o arquivo não existir ou estiver corrompido, devolve lista vazia.
    """
    caminho = Path(caminho)
    if not caminho.exists():
        return []
    try:
        with caminho.open(encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    except (json.JSONDecodeError, OSError):
        return []
    return dados if isinstance(dados, list) else []


def ultimo_diagnostico(caminho=CAMINHO_PADRAO):
    historico = carregar_historico(caminho)
    return historico[-1] if historico else None


def salvar_diagnostico(pilares, geral, plano, caminho=CAMINHO_PADRAO, data=None):
    """Acrescenta um diagnóstico ao histórico e devolve o registro salvo."""
    registro = {
        "data": data or datetime.now().strftime("%Y-%m-%d %H:%M"),
        "geral": round(geral, 1),
        "pilares": {pilar: round(valor, 1) for pilar, valor in pilares.items()},
        "missoes": [item["id"] for item in plano],
    }

    historico = carregar_historico(caminho)
    historico.append(registro)

    caminho = Path(caminho)
    with caminho.open("w", encoding="utf-8") as arquivo:
        json.dump(historico, arquivo, ensure_ascii=False, indent=2)

    return registro
