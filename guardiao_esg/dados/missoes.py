"""Missões do plano de ação.

Cada missão tem o mesmo id da pergunta que a origina.
Todas são de baixo custo e não exigem consultoria.
"""

missoes = {
    # ---------------- Ambiental ----------------
    "agua": {
        "titulo": "Acompanhar o consumo de água",
        "como_fazer": "Toda segunda-feira, anote a leitura do hidrômetro (ou o valor da conta) em um caderno ou planilha.",
        "custo": "Zero",
        "beneficio": "Descobrir vazamentos e desperdícios, reduzindo a conta.",
    },
    "desperdicio": {
        "titulo": "Pesar o desperdício de comida por 7 dias",
        "como_fazer": "Deixe uma balança e um balde de descarte na cozinha. Anote ao fim do dia o peso e o motivo (sobra, validade, erro).",
        "custo": "Zero a baixo (balança simples)",
        "beneficio": "Enxergar onde o dinheiro está indo para o lixo e ajustar compras e porções.",
    },
    "energia": {
        "titulo": "Fazer a ronda da energia",
        "como_fazer": "Ao fechar, confira luzes, ar-condicionado e equipamentos ligados sem uso. Anote o valor da conta de luz todo mês.",
        "custo": "Zero",
        "beneficio": "Cortar gasto fixo sem mexer na qualidade do serviço.",
    },
    "residuos": {
        "titulo": "Separar o lixo em dois recipientes",
        "como_fazer": "Coloque uma lixeira para recicláveis (papel, plástico, vidro, metal) e outra para o resto. Combine com a equipe quem leva para a coleta.",
        "custo": "Baixo (uma lixeira extra)",
        "beneficio": "Menos lixo comum e uma rotina de limpeza mais organizada.",
    },
    "oleo": {
        "titulo": "Guardar o óleo usado para coleta",
        "como_fazer": "Armazene o óleo frio em garrafa PET e procure um ponto de coleta ou cooperativa da sua cidade que recolha.",
        "custo": "Zero",
        "beneficio": "Evita entupimento e poluição, e pode render parceria de coleta.",
    },
    "embalagens": {
        "titulo": "Revisar as embalagens das entregas",
        "como_fazer": "Liste o que vai em cada pedido (talheres, sachês, sacolas). Pergunte ao cliente se quer talheres e retire o que for excesso.",
        "custo": "Zero (pode até economizar)",
        "beneficio": "Menos custo com descartáveis e mais valor para clientes preocupados com o meio ambiente.",
    },

    # ---------------- Social ----------------
    "fornecedores_locais": {
        "titulo": "Testar um fornecedor local",
        "como_fazer": "Escolha 1 ou 2 itens do cardápio (hortaliças, ovos, pães) e peça orçamento a produtores da região.",
        "custo": "Zero",
        "beneficio": "Ingredientes mais frescos, menos transporte e fortalecimento da comunidade.",
    },
    "regras_equipe": {
        "titulo": "Escrever regras básicas de trabalho",
        "como_fazer": "Em uma folha, anote horários, funções, regras de higiene e de convivência. Converse com a equipe e deixe afixado na cozinha.",
        "custo": "Zero",
        "beneficio": "Menos conflitos e uma equipe que sabe o que se espera dela.",
    },
    "entregadores": {
        "titulo": "Conferir pagamento e segurança da equipe",
        "como_fazer": "Defina datas fixas de pagamento e pergunte a entregadores e funcionários o que falta (equipamento de proteção, local de descanso).",
        "custo": "Baixo",
        "beneficio": "Equipe mais estável, menos rotatividade e menor risco de problemas trabalhistas.",
    },
    "reuniao_equipe": {
        "titulo": "Fazer uma conversa mensal de 15 minutos",
        "como_fazer": "Reserve 15 minutos no mesmo dia todo mês. Pergunte: o que está funcionando, o que atrapalha e uma ideia de melhoria.",
        "custo": "Zero",
        "beneficio": "Ideias que reduzem erros e desperdício, e uma equipe mais engajada.",
    },
    "canal_clientes": {
        "titulo": "Abrir um canal simples de feedback",
        "como_fazer": "Coloque um QR code ou um número de WhatsApp na embalagem para reclamações e elogios. Responda em até 2 dias.",
        "custo": "Zero",
        "beneficio": "Resolver problemas antes de virarem má avaliação e saber o que os clientes valorizam.",
    },

    # ---------------- Governança ----------------
    "financeiro": {
        "titulo": "Registrar receitas e despesas",
        "como_fazer": "Use uma planilha ou caderno e anote tudo que entra e sai, no mesmo dia. Separe a conta pessoal da conta do restaurante.",
        "custo": "Zero",
        "beneficio": "Saber de verdade se o negócio dá lucro e onde cortar custos.",
    },
    "metas": {
        "titulo": "Definir uma meta simples e medível",
        "como_fazer": "Escolha uma meta para os próximos 3 meses, como reduzir o desperdício de comida em 10%, e anote o ponto de partida.",
        "custo": "Zero",
        "beneficio": "Dá direção ao esforço e permite comemorar resultados reais.",
    },
    "formalizacao": {
        "titulo": "Regularizar a documentação do negócio",
        "como_fazer": "Verifique CNPJ/MEI, alvará e licença sanitária. O Sebrae e a prefeitura orientam gratuitamente. Emita nota fiscal nas vendas.",
        "custo": "Baixo (taxas oficiais)",
        "beneficio": "Evita multas, abre acesso a crédito e passa confiança para clientes e parceiros.",
    },
    "estoque": {
        "titulo": "Criar um controle de estoque e validade",
        "como_fazer": "Etiquete os itens com a data de abertura e validade, use a regra 'o que vence primeiro sai primeiro' e faça uma contagem semanal.",
        "custo": "Baixo (etiquetas e caneta)",
        "beneficio": "Menos comida jogada fora e compras mais certeiras.",
    },
    "acompanhamento": {
        "titulo": "Revisar os resultados todo mês",
        "como_fazer": "No primeiro dia útil, olhe vendas, custos e sobras do mês anterior e compare com o mês retrasado. Anote uma decisão.",
        "custo": "Zero",
        "beneficio": "Decisões com base em dados, e não só na intuição.",
    },
}
