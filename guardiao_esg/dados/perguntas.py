"""Perguntas do diagnóstico.

Cada pergunta tem:
- id: o mesmo id da missão que será sugerida se a nota for baixa;
- pilar: Ambiental, Social ou Governança;
- tipo: "frequencia" (Nunca...Sempre) ou "existencia" (Não tenho...Tenho e acompanho).
"""

perguntas = [
    # ---------------- Ambiental ----------------
    {
        "id": "agua",
        "pilar": "Ambiental",
        "tipo": "frequencia",
        "pergunta": "Você acompanha o consumo de água do restaurante (conta ou hidrômetro)?",
    },
    {
        "id": "desperdicio",
        "pilar": "Ambiental",
        "tipo": "frequencia",
        "pergunta": "Você controla o que sobra ou estraga de comida na cozinha?",
    },
    {
        "id": "energia",
        "pilar": "Ambiental",
        "tipo": "frequencia",
        "pergunta": "Você acompanha o consumo de energia (conta de luz, equipamentos ligados sem necessidade)?",
    },
    {
        "id": "residuos",
        "pilar": "Ambiental",
        "tipo": "frequencia",
        "pergunta": "Você separa o lixo reciclável do lixo comum?",
    },
    {
        "id": "oleo",
        "pilar": "Ambiental",
        "tipo": "frequencia",
        "pergunta": "O óleo de cozinha usado é guardado e entregue para coleta, sem ir para a pia?",
    },
    {
        "id": "embalagens",
        "pilar": "Ambiental",
        "tipo": "existencia",
        "pergunta": "Você pensa na embalagem das entregas para evitar excesso de plástico e material descartável?",
    },

    # ---------------- Social ----------------
    {
        "id": "fornecedores_locais",
        "pilar": "Social",
        "tipo": "frequencia",
        "pergunta": "Você compra de produtores e fornecedores da sua região?",
    },
    {
        "id": "regras_equipe",
        "pilar": "Social",
        "tipo": "existencia",
        "pergunta": "Sua equipe tem regras claras de trabalho (horários, funções, tratamento entre colegas)?",
    },
    {
        "id": "entregadores",
        "pilar": "Social",
        "tipo": "frequencia",
        "pergunta": "Funcionários e entregadores recebem em dia e com condições de trabalho seguras?",
    },
    {
        "id": "reuniao_equipe",
        "pilar": "Social",
        "tipo": "frequencia",
        "pergunta": "Você conversa com a equipe para ouvir sugestões e problemas?",
    },
    {
        "id": "canal_clientes",
        "pilar": "Social",
        "tipo": "existencia",
        "pergunta": "Você tem um canal para ouvir reclamações e elogios dos clientes?",
    },

    # ---------------- Governança ----------------
    {
        "id": "financeiro",
        "pilar": "Governança",
        "tipo": "frequencia",
        "pergunta": "Você registra todas as receitas e despesas do restaurante?",
    },
    {
        "id": "metas",
        "pilar": "Governança",
        "tipo": "existencia",
        "pergunta": "Você tem alguma meta para reduzir desperdício ou gastos (água, energia, comida)?",
    },
    {
        "id": "formalizacao",
        "pilar": "Governança",
        "tipo": "existencia",
        "pergunta": "O negócio está formalizado (CNPJ/MEI, alvará, notas fiscais)?",
    },
    {
        "id": "estoque",
        "pilar": "Governança",
        "tipo": "frequencia",
        "pergunta": "Você controla o estoque e a validade dos ingredientes?",
    },
    {
        "id": "acompanhamento",
        "pilar": "Governança",
        "tipo": "frequencia",
        "pergunta": "Você analisa os resultados do restaurante todo mês (vendas, custos, sobras)?",
    },
]
