from app import app
from flask import render_template, request
import requests
import pprint as p
from pprint import pformat

#routes
@app.route("/", methods=['GET', 'POST']) #decorator, da uma funcionalidade à linha debaixo
def homepage():
    dados = None
    erro = None

    if request.method == 'POST':
        token_api = "wVZTGB3AhR2rjfZBQptFy9"
        link_api = "https://brapi.dev/api/quote/"
        parametros = {'token' : token_api}
        sigla_acao = request.form.get('acao_bolsa')

        try:
            resposta = requests.get(link_api + sigla_acao, params=parametros)
            resposta.raise_for_status()
            dados = resposta.json()['results'][0]
            
        except Exception as e:
            erro = "Erro ao buscar a ação"

    return render_template("homepage.html", dados=dados, erro=erro)

# @app.route('/resultado', methods=['POST']) #decorator, da uma funcionalidade à linha debaixo
# def resultado():
#     token_api = "wVZTGB3AhR2rjfZBQptFy9"
#     link_api = "https://brapi.dev/api/quote/"
#     sigla_acao = request.form.get('acao_bolsa')
#     parametros = {
#         'token': token_api
#     }
#     link_api = link_api + sigla_acao
#     resposta = requests.get(link_api, params=parametros)
#     data_response = pformat(resposta.json())
#     print(resposta.status_code)
#     return f"{data_response}"