class guardar():
    pass
    # import requests # type: ignore
    # import pprint as pretty

    # # api_key = "379133b8555c4644ae3155614250107"
    # # link_api = "http://api.weatherapi.com/v1/current.json"

    # # q_cidade = input("Digite o nome da cidade que você quer saber a temperatura: ")

    # # parametros = {
    # #     "key": api_key,
    # #     "q": q_cidade,
    # #     "lang": "pt"
    # # }

    # # resposta = requests.get(link_api, params= parametros)
    # # print(resposta.status_code)

    # # if resposta.status_code == 200:
    # #     data_required = resposta.json()

    # # pprint.pprint(data_required["current"]["temp_c"])
    # # pprint.pprint(data_required["location"]["region"])

    # api_key = "6ac0f131f43539888bcf37810a07e580"
    # link_api = "https://api.exchangerate.host/live"

    # moeda = input("Digite a sigla da moeda que quer saber os valores:  ")
    # conversao = input("Digite a sigla da moeda na qual quer converter: ")

    # moedafinal = moeda + conversao

    # # print(moedafinal)

    # parametros = {
    #     "access_key": api_key,
    #     "timestamp": 1430401802,
    #     "source": moeda
    # }

    # resposta = requests.get(link_api, params= parametros)

    # if resposta.status_code == 200:
    #     dados_json = resposta.json()

    # # print(resposta.status_code)
    # # print(resposta.json())
    # pretty.pprint(dados_json["quotes"][moedafinal])

import requests
import pprint as p

token_api = "wVZTGB3AhR2rjfZBQptFy9"
link_api = "https://brapi.dev/api/quote/"

acao_buscada = input("Digite a sigla da ação que deseja receber informações: ")

link_api = link_api + acao_buscada

parametros = {
    "token": token_api
}

resposta = requests.get(link_api, params=parametros)

# print(resposta.status_code)
p.pprint(resposta.json())

jsonResponse = resposta.json()['results'][0]

# priceMarket = 
# earningPerShare = 
if resposta.status_code == 200:
    priceToProfit = jsonResponse['priceEarnings']
    print(jsonResponse.get('roe', 'Não informado'))
    print(priceToProfit)
else:
    print(resposta.status_code)
