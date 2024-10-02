import requests  # Importa a biblioteca requests para fazer solicitações HTTP.


class ConsultaRegistros:
    """ Possui metodos para consultas de registros e ou relacionamentos do Portal MinhaNexx """

    def valida_token(self, token, url) -> str:
        """ Metodo para validar o Token informado no app AlloKate a fim de identificar a que Banco o mesmo pertence """

        # Define os parametros da solicitacao
        params = {
            'limit': '1',  # Retorna apenas 1 resultado
        }

        # Define os cabecalhos da solicitacao incluindo o token de servico
        headers = {
            'service-token': token,
            'Content-Type': 'application/json',
        }

        # Realiza uma solicitacao GET a API do MinhaNexx com os parametros e cabecalhos especificados
        response = requests.get(url, headers=headers, params=params)

        # Verifica se a solicitacao foi bem-sucedida
        if response.status_code == 200:
            dic_requisicao = response.json()  # Converte a resposta JSON em um dicionario Python
            if dic_requisicao['count'] == 0:
                return 'Nada Encontrado'
            return dic_requisicao['results'][0]['institution']['name']  # Retorna o nome do Banco identificado no primeiro indice do resultado

        elif response.status_code == 403:
            return 'Invalido'  # Erro token invalido

        else:
            return None  # Retorna None devido a outros motivos
