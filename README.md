<h1 align="center">
  Pandas Script
</h1>

<h4 align="center">Linguagem baseada no <a href="https://pandas.pydata.org/">Pandas</a> e feita com <a href="https://www.python.org/">Python</a>.</h4>

<p align="center">
  <a href="#introdução">Introdução</a> •
  <a href="#funcionalidades">Funcionalidades</a> •
  <a href="#como-usar">Como usar</a> •
  <a href="#exemplo">Exemplo</a> •
  <a href="#créditos">Créditos</a> •
  <a href="#license">License</a>
</p>

![screenshot](https://i.imgur.com/nWrDkmN.png)

## Introdução
O Pandas Script é uma linguagem simples de auto nível que tem como objetivo simplificar e agilizar a visualização e gerenciamento de dados como CSV.

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

Gráfico gerado:
![covid](https://i.imgur.com/455rc7J.png)

Árvore de geração utilizada caso a linha 2 fosse um print no lugar de um asssing:
![arvore](https://i.imgur.com/dRctMRa.png)

## Créditos

Essa aplicação utiliza os seguintes projetos de código aberto:

- [Python](https://www.python.org/)
- [Numpy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)
- [SLY](https://github.com/dabeaz/sly)

Inspiração do README [electron-markdownify](https://github.com/amitmerchant1990/electron-markdownify).

## License

MIT

---

> [Acesse meu site](https://cassiofernando.netlify.app/) &nbsp;&middot;&nbsp;
> GitHub [@cassiofb-dev](https://github.com/cassiofb-dev) &nbsp;&middot;&nbsp;
> Twitter [@cassiofb_dev](https://twitter.com/cassiofb_dev)
