<h1 align="center">
  Pandas Script
</h1>

<h4 align="center">Linguagem baseada no <a href="https://pandas.pydata.org/">Pandas</a> e feita com <a href="https://www.python.org/">Python</a>.</h4>

<p align="center">
  <a href="#introdução">Introdução</a> •
  <a href="#funcionalidades">Funcionalidades</a> •
  <a href="#como-usar">Como usar</a> •
  <a href="#exemplo">Exemplo</a> •
  <a href="#documentação">Documentação</a> •
  <a href="#produções-e-ações-semânticas">Produções e Ações Semânticas</a> •
  <a href="#créditos">Créditos</a> •
  <a href="#license">License</a>
</p>

[![screenshot](https://i.imgur.com/nWrDkmN.png)](https://www.youtube.com/watch?v=JWDCLF0NqS8)

## Introdução
O Pandas Script é uma linguagem simples de alto nível que tem como objetivo simplificar e agilizar a visualização e gerenciamento de dados como CSV.

## Funcionalidades

* PS Shell - Shell interativo
  - Faça programas curtos, checagens rápidas ou aprendizado dinâmico.
* Parse de Arquivos
  - Para programas longos e complexo
* Suporte para
  - Inteiros
  - Floats
  - Strings
* Operações com arquivos
  - Leitura
  - Escrita
  - Selecionar
  - Cortar
  - Gerar gráfico simples
* Arquivos online
  - Leitura de arquivos pode ser através de uma URL
* Informações estatísticas - Calcule
  - Média
  - Mediana
  - Desvio Padrão

## Como usar

[Video de apresentação](https://www.youtube.com/watch?v=JWDCLF0NqS8).

Para clonar e rodar essa aplicação, você irá precisar [Git](https://git-scm.com), [Python](https://www.python.org/). Pelo seu terminal:

```bash
# Clone o repositório
git clone https://github.com/cassiofb-dev/pandasscript

# Entre no repositório
cd pandasscript

# Instale as dependências
pip install numpy
pip install pandas

# Rode a aplicação
py main.py
```

## Exemplo
```
covid_data  = LOAD "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
brazil_data = CUT 30 31 covid_data
deaths      = CUT 474 484 brazil_data 1
PLOT deaths "Mortes por COVID"
```

Rodando o exemplo no terminal:
```
py main.py .\example\covid_death.ps
```

Gráfico gerado:
![covid](https://i.imgur.com/455rc7J.png)

Árvore de geração utilizada caso a linha 2 fosse um print no lugar de um asssing:
![arvore](https://i.imgur.com/3q7fWa5.png)

## Documentação

- ``py main.py``
  - Executa o shell
- ``py main.py help``
  - Executa o comando de ajuda
- ``py main.py license``
  - Executa o comando de licensa
- ``py main.py copyright``
  - Executa o comando de copyright
- ``py main.py filePath``
  - Executa o parse de um arquivo

## Produções e Ações Semânticas

Observações:
- Tokens em caixa alta
- Funções completas das ações sintáticas podem ser encontradas no [código de funções](https://github.com/cassiofb-dev/pandasscript/blob/master/lang/PSFunctions.py), elas são utilizadas atráves do módulo ``psf``
- Tokens dos operadores substituido pelos próprios para simplificação da leitura (Ex: "=" ficará no lugar de "ASSIGN")
```bnf
Grammar                                         Action
------------------------                        ---------------------------------
statement : PRINT expr                          print(expr.val)
          | SAVE ID STRING                      psf.save(ID.val, STRING.val)
          | ID = expr                           ID.val = expr.val
          | expr                                ---

expr0     : expr1 + expr2                       expr0.val = expr1.val + expr2.val
          | expr1 - expr2                       expr0.val = expr1.val - expr2.val
          | expr1 * expr2                       expr0.val = expr1.val * expr2.val
          | expr1 / expr2                       expr0.val = expr1.val / expr2.val
          | (expr1)                             expr0.val = expr1.val
          | FLOAT                               expr0.val = float(FLOAT.val)
          | INT                                 expr0.val = int(INT.val)
          | STRING                              expr0.val = string(STRING.val)
          | ID                                  self.ids[ID.val]
          | COLUMNS ID                          expr0.val = psf.columns(self.ids[ID.val])
          | LOAD STRING                         expr0.val = psf.load(STRING.val)
          | CUT INTEGER1 INTEGER2 ID            expr0.val = psf.cut(INTEGER1.val, INTEGER2.val, self.ids[ID.val])
          | CUT INTEGER1 INTEGER2 ID INTEGER3   expr0.val = psf.cut(INTEGER1.val, INTEGER2.val, self.ids[ID.val], INTEGER3.val)
          | MEDIAN expr1                        expr0.val = psf.median(expr1.val)
          | MEAN expr1                          expr0.val = psf.mean(expr1.val)
          | STD expr1                           expr0.val = psf.std(expr1.val)
          | select                              expr0.val = select.val
          | PLOT ID STRING                      psf.plot(self.ids[ID.val], STRING.val)

select    : SELECT STRING STRING FROM expr      psf.select_from(STRING0.val, STRING1.val, expr.val)
          | SELECT STRING FROM expr             psf.select_from(STRING.val, None, expr.val)
          | SELECT FROM expr                    psf.select_from(None, None, expr.val)
```

## Créditos

Essa aplicação utiliza os seguintes projetos de código aberto:

- [Python](https://www.python.org/)
- [Numpy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)
- [SLY](https://github.com/dabeaz/sly)
- [COVID dataset](https://github.com/CSSEGISandData/COVID-19)

Inspiração do README [electron-markdownify](https://github.com/amitmerchant1990/electron-markdownify).

## License

MIT

---

> [Acesse meu site](https://cassiofernando.netlify.app/) &nbsp;&middot;&nbsp;
> GitHub [@cassiofb-dev](https://github.com/cassiofb-dev) &nbsp;&middot;&nbsp;
> Twitter [@cassiofb_dev](https://twitter.com/cassiofb_dev)
