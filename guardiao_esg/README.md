# Guardião ESG

Diagnóstico simples (no terminal) para donos de restaurante entenderem seu nível de
sustentabilidade e receberem um plano de ação prático, sem termos técnicos.

## Como rodar

```bash
python main.py
```

Para rodar os testes:

```bash
pip install -r requirements-dev.txt
pytest
```

## Estrutura

```
main.py                  fluxo do menu
dados/perguntas.py       perguntas (cada uma com id, pilar e tipo de escala)
dados/missoes.py         missões (mesmo id da pergunta de origem)
sistema/config.py        regras: pontuação, níveis, escalas, tamanho do plano
sistema/diagnostico.py   aplica o questionário
sistema/analise.py       notas, níveis e plano de ação
sistema/historico.py     salva/lê diagnósticos em historico.json
interface/telas.py       tudo que aparece na tela
tests/                   testes automatizados
```

## Como funciona

1. O usuário responde 16 perguntas (opções de 1 a 4, que valem de 0 a 3 pontos).
2. O sistema calcula a nota de cada pilar (Ambiental, Social, Governança) e a nota geral.
3. Cada nota vira um nível: Inicial, Em desenvolvimento, Estruturado ou Avançado.
4. Respostas com 0 ou 1 ponto viram missões (até 4, uma por semana), começando
   pelas notas mais baixas e variando os pilares.
5. O resultado é salvo em `historico.json` e comparado com o diagnóstico anterior.

## Como personalizar

- **Nova pergunta:** adicione em `dados/perguntas.py` e crie uma missão com o mesmo `id`
  em `dados/missoes.py`. Os testes avisam se faltar uma das duas.
- **Níveis, pontuação, tamanho do plano:** `sistema/config.py`.
