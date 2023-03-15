# PROJECT RESTAURANT ORDERS PYTHON 🖱️

# 🍔🍕🍟

## 📃Descrição

O Restaurant Orders é um projeto desenvolvido para ajudar a gerência da lanchonete Pão na Chapa a aumentar suas vendas e melhorar sua gestão interna. O sistema de faturamento da lanchonete salva o nome da pessoa, o pedido realizado e o dia da semana do atendimento, e o objetivo do projeto é gerar relatórios com informações sobre os pedidos e as pessoas clientes que frequentam a lanchonete. Esses dados irão auxiliar o trabalho de uma agência de marketing com o objetivo de alavancar as vendas e o número de pessoas clientes.

## ⚙️Funcionalidades

O projeto possui as seguintes funcionalidades:

-   Geração de relatórios com informações sobre pedidos e clientes;
-   Controle de estoque de ingredientes para garantir que o menu digital do restaurante sempre ofereça produtos disponíveis em estoque.

## 💻Tecnologias utilizadas
<div align="left">

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="50" width="62" alt="python logo" />

</div>

## 📑 Instruções
Clone o repositório usando o comando:

    git clone git@github.com:Ytellon/project-restaurant-orders.git
Crie o ambiente virtual para o projeto

    python3 -m venv .venv && source .venv/bin/activate
Instale as dependências

    python3 -m pip install -r dev-requirements.txt

<details>
  <summary><h3>🧱 Estrutura do Projeto</h3></summary><br />

  ```
  
  ├── data
  │   ├──🔸 orders_1.csv
  │   └──🔸 orders_2.csv
  ├── src
  │   ├──🔹 analyze_log.py
  │   ├──🔹 inventory_control.py
  │   ├──🔹 main.py
  │   └──🔹 track_orders.py
  ├──tests
  │   ├──🔸 test_analyze_log.py
  │   ├──🔸 test_inventory_control.py
  │   └──🔸 test_track_orders.py
  ├──🔸 dev-requirements.txt
  ├──🔸 pyproject.toml
  ├──🔹 README.md
  ├──🔸 requirements.txt
  ├──🔸 setup.cfg
  ├──🔸 setup.py
  └──🔸 trybe.yml
Legenda:
  🔸 Arquivos desenvolvidos pela Trybe.
  🔹 Arquivos desenvolvidos por mim.
```
</details>


## Campanha de publicidade 
#### O sistema gera um arquivo txt no caminho `data/mkt_campaign.txt` com as seguintes informações:

-   Qual o prato mais pedido por 'maria'?
-   Quantas vezes 'arnaldo' pediu 'hambúrguer'?
-   Que pratos 'joão' nunca pediu?
-   Em que dias o 'joão' nunca foi a lanchonete?

Para executá-lo, use o comando `python3 -m src.analyze_log`

## Análise Contínua
#### Sistema que permite, a qualquer momento, a extração de informações:

-   Prato favorito por cliente
-   Pratos nunca encomendados por cada cliente
-   Dias nunca visitados por cada cliente
-   Dia mais movimentado
-   Dia menos movimentado

Para executá-lo, use o comando `python3 -m src.track_orders`
