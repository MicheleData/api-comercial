
from flask import Flask
import pandas as pd

df_cliente = pd.read_excel("Cadastro Clientes.xlsx")
df_lojas = pd.read_excel("Cadastro Lojas.xlsx")
df_localidades = pd.read_excel("Cadastro Localidades.xlsx")
df_produtos = pd.read_excel("Cadastro Produtos.xlsx")
df_vendas_2020 = pd.read_excel("Base Vendas - 2020.xlsx")
df_vendas_2021 = pd.read_excel("Base Vendas - 2021.xlsx")
df_vendas_2022 = pd.read_excel("Base Vendas - 2022.xlsx")
df_devolucoes = pd.read_excel("Base Devoluções.xlsx")
df_imagens = pd.read_excel("Imagens.xlsx")

app = Flask(__name__)

@app.route("/")
def cliente():
    dic_df_cliente = df_cliente.to_dict()
    return dic_df_cliente

@app.route("/lojas")
def loja():
    dic_df_lojas = df_lojas.to_dict()
    return dic_df_lojas

@app.route("/localidades")
def localidade():
    dic_df_localidades = df_localidades.to_dict()
    return dic_df_localidades

@app.route("/produtos")
def produto():
    dic_df_produtos = df_produtos.to_dict()
    return dic_df_produtos

@app.route("/vendas2020")
def venda_2020():
    dic_df_vendas_2020 = df_vendas_2020.to_dict()
    return dic_df_vendas_2020

@app.route("/vendas2021")
def venda_2021():
    dic_df_vendas_2021 = df_vendas_2021.to_dict()
    return dic_df_vendas_2021

@app.route("/vendas2022")
def venda_2022():
    dic_df_vendas_2022 = df_vendas_2022.to_dict()
    return dic_df_vendas_2022

@app.route("/devolucoes")
def devolucao():
    dic_df_devolucoes = df_devolucoes.to_dict()
    return dic_df_devolucoes

@app.route("/imagens")
def imagem():
    dic_df_imagem = df_imagens.to_dict()
    return dic_df_imagem


if __name__ == '__main__':
    app.run()

