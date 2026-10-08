"""Regras do diagnóstico em um só lugar.

Para ajustar a pontuação, os níveis ou o tamanho do plano de ação,
basta mexer neste arquivo.
"""

# Cada resposta vale de 0 a 3 pontos.
PONTOS_MAXIMO = 3

# Respostas com 0 ou 1 ponto viram missão no plano de ação.
LIMITE_RESPOSTA_BAIXA = 1

# Quantidade máxima de missões (uma por semana).
MAX_MISSOES = 4

# Largura das linhas decorativas e das barras no terminal.
LARGURA_TELA = 50
LARGURA_BARRA = 20

# Opções de resposta, na ordem dos pontos (0, 1, 2, 3).
ESCALAS = {
    "frequencia": ["Nunca", "Às vezes", "Frequentemente", "Sempre"],
    "existencia": [
        "Não tenho",
        "Estou começando",
        "Tenho, mas não acompanho",
        "Tenho e acompanho",
    ],
}

# (limite máximo em %, nome do nível, explicação curta)
NIVEIS = [
    (25, "Inicial",
     "Você está no começo. Pequenos passos já vão fazer diferença."),
    (50, "Em desenvolvimento",
     "Você já tem boas práticas, mas muitas ainda sem registro ou rotina."),
    (75, "Estruturado",
     "Suas práticas estão organizadas. Falta acompanhar os resultados."),
    (100, "Avançado",
     "Você mantém boas práticas e acompanha os resultados. Continue assim!"),
]
