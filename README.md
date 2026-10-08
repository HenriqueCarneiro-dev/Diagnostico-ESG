# Guardião ESG

Diagnóstico simples para donos de restaurantes entenderem seu nível de sustentabilidade e receberem um plano de ação prático, sem termos técnicos.

Este projeto faz parte do ecossistema do [BelmontBeta/projeto-impacta](https://github.com/BelmontBeta/projeto-impacta), uma iniciativa dedicada ao tema ESG com referência a práticas e metodologias inspiradas no mercado, especialmente para o setor alimentício.

## Objetivo

O Guardião ESG ajuda pequenos e médios negócios do ramo alimentício a:

- avaliar seu desempenho em sustentabilidade;
- identificar oportunidades de melhoria em pilares ambientais, sociais e de governança;
- receber um plano de ação objetivo e organizado;
- acompanhar evolução ao longo do tempo.

## Como funciona

1. O usuário responde a 16 perguntas com respostas de 1 a 4.
2. O sistema calcula a nota por pilar: Ambiental, Social e Governança.
3. Cada pilar recebe um nível de maturidade: Inicial, Em desenvolvimento, Estruturado ou Avançado.
4. As respostas com menor desempenho viram missões de melhoria.
5. O resultado é salvo no histórico do diagnóstico para comparação futura.

## Estrutura do projeto

```text
main.py                  Fluxo principal do diagnóstico

dados/perguntas.py       Perguntas e categorias de ESG
dados/missoes.py         Missões de ação sugeridas
sistema/config.py        Regras de pontuação, níveis e escalas
sistema/diagnostico.py   Aplicação do questionário
sistema/analise.py       Cálculo de notas e planos de ação
sistema/historico.py     Armazenamento dos diagnósticos
interface/telas.py       Interface do terminal
tests/                   Testes automatizados
```

## Como rodar

```bash
python main.py
```

Para executar os testes:

```bash
pip install -r requirements-dev.txt
pytest
```

## Link com o Projeto Impacta

Este repositório é um módulo/parte complementar do projeto principal:

- [BelmontBeta/projeto-impacta](https://github.com/BelmontBeta/projeto-impacta)
- Site do projeto: https://projeto-impacta.onrender.com

A integração entre os repositórios reflete a proposta de criar uma solução mais ampla de diagnóstico e apoio à sustentabilidade para o setor alimentício.

## Tecnologias

- Python
- Estrutura modular para diagnósticos e análise
- Interface em terminal
- Sistema de histórico e comparação de resultados

## Contribuição

Contribuições são bem-vindas. Se você quiser melhorar o projeto:

1. faça um fork;
2. crie uma branch para sua alteração;
3. envie o pull request com uma descrição clara.

## Licença

Este projeto segue os termos definidos no repositório principal do projeto Impacta, quando aplicável.

---

Guardião ESG é uma ferramenta de apoio à transformação sustentável, combinando tecnologia, análise de dados e orientação prática para decisões mais conscientes.
