import sys  # Biblioteca para recursos de identificacao de sistema operacional
import json  # Biblioteca para tratar arquivos json
import requests  # Biblioteca para trabalhar com api
import time  # Biblioteca para tratar datas e horarios.
import os  # Biblioteca para interagir com o sitema operacional
import urllib3  # Biblioteca para desativar verificacao de ssl nao verificado googleapis
import pandas as pd
from urllib.parse import urlencode, urlparse, parse_qs
from selenium import webdriver  # Importando WebDriver do Selenium
from selenium.webdriver.chrome.service import Service as ChromeService  # Importando o servico webdriver do selenium e definando o nome para o servico no chrome
from selenium.webdriver.firefox.service import Service as FirefoxService  # Importando o servico webdriver do selenium e definando o nome para o servico no firefox
from selenium.webdriver.edge.service import Service as EdgeService  # Importando o servico webdriver do selenium e definando o nome para o servico no firefox
from selenium.webdriver.common.by import By  # Recurso do Selenium Find POR
from selenium.webdriver.common.keys import Keys  # Recurso do Selenium uso de padroes de teclas ex Enter
from selenium.webdriver.common.action_chains import ActionChains  # Recursos do Selenium para acoes do mouse
from selenium.webdriver.support import expected_conditions as EC  # Recurso do Selenium como EC
from selenium.webdriver.support.ui import WebDriverWait  # Recurso do Selenium Usar para aguardar elementos aparecerem
from selenium.webdriver.support.select import Select  # Recursos do Selenium Selecao de Menus
from selenium.common.exceptions import *  # Recursos do Selenium Excecoes


class ConsultarAlterar:
    """ Api criada para realizar algumas etapas usando API do Minha Nexx """

    redirect_uri = 'https://portal-relacionamento-prd.nexxera.io/static/drf-yasg/swagger-ui-dist/oauth2-redirect.49cb7cc0bfe0.html'
    authorization_base_url = 'https://nix-sso.nexxera.com/auth/realms/PortalRelacionamento/protocol/openid-connect/auth'
    token_url = 'https://nix-sso.nexxera.com/auth/realms/PortalRelacionamento/protocol/openid-connect/token'
    token_van = '92837b28-87b1-441c-9650-60953951e86b'  # Token Van Nexxera Fixo
    url_base = 'https://portal-relacionamento-prd.nexxera.io/api/v1'  # URL API

    def __init__(self,
                 usuario: str,
                 senha: str):

        # Configurações da aplicação
        self.client_id = 'portal-relacionamento-core'
        self.client_secret = 'ec7186bb-44c6-4efc-8ef1-5fa1470ebcc7'
        self.usuario = usuario
        self.senha = senha

    def autentica_captura_token(self) -> str:
        """ Api para realizar a captura do token para poder autenticar nas outras urls referente ao minha nexx """

        # Passo 1: Obter a URL de autorização
        params = {'response_type': 'code',
                  'client_id': self.client_id,
                  'redirect_uri': self.redirect_uri,
                  'scope': 'openid',
                  'state': 'random_state_string'
                  }

        authorization_url = f"{self.authorization_base_url}?{urlencode(params)}"

        # Configuração do Selenium
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Definindo opcoes para rodar a automação web em segundo plano.
        options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Desabilitando a captura padrao de bluetooth do navegador
        driver = webdriver.Chrome(options=options)  # Passando o webdriver para a classe servico e inicializando e realizando o download automatico chrome

        # Abrir o navegador e visitar a URL de autorização
        driver.get(authorization_url)
        driver.maximize_window()  # Definindo para abrir no formato maximizado

        # Preencher o formulário de login
        tentativa = 0
        falha = True
        while tentativa <= 5:
            try:
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='username'])[1]")))
                driver.find_element(By.XPATH, "(//a[@id='zocial-keycloak-oidc'])[1]").click()
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='username'])[1]")))
                time.sleep(2)
                driver.find_element(By.XPATH, "(//input[@id='username'])[1]").send_keys(self.usuario)  # Inserindo nome de usuario no portal
                time.sleep(2)
                driver.find_element(By.XPATH, "(//input[@id='password'])[1]").send_keys(self.senha, Keys.ENTER)  # Inserindo senha do usuario no portal
                time.sleep(2)
                tentativa = 6
                falha = False
            except Exception:
                driver.refresh()
                tentativa += 1

        if falha is False:
            # Capturar a URL de redirecionamento
            redirected_url = driver.current_url

            # Extrair o código de autorização da URL de redirecionamento
            redirect_response_params = parse_qs(urlparse(redirected_url).query)
            authorization_code = redirect_response_params.get('code')[0]

            # Passo 3: Trocar o código de autorização pelo token de acesso
            token_data = {'grant_type': 'authorization_code',
                          'code': authorization_code,
                          'redirect_uri': self.redirect_uri,
                          'client_id': self.client_id,
                          'client_secret': self.client_secret
                          }

            response = requests.post(self.token_url, data=token_data)
            if response.status_code == requests.codes.ok:
                token = response.json()
                return token['access_token']

            else:
                return 'ERRO1'
        else:
            return 'ERRO2'

    def key_usuario(self,
                    token_api: str,
                    usuario: str
                    ) -> str:
        """GET"""

        url = f"{self.url_base}/users?email={usuario}%40nexxera.com"

        payload = {}
        headers = {'Content-Type': 'application/json',
                   'authorization': f'Bearer {token_api}'
                   }

        response = requests.get(url, headers=headers, data=payload)
        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            return 'ERRO'

    def tag_relacionamento(self,
                               token_api: str,
                               key_relacionamento: str,
                               token_usuario: str
                               ) -> str:
        """PUT"""

        url = f"{self.url_base}/companies/{self.token_van}/requests/{key_relacionamento}/assign"

        payload = {"user_key": token_usuario}
        headers = {'Content-Type': 'application/json',
                   'authorization': f'Bearer {token_api}'
                   }

        response = requests.put(url, headers=headers, data=json.dumps(payload))
        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            return 'ERRO'

    def captura_relacionamento(self,
                               token_api: str,
                               codigo_relacionamento: str
                               ) -> dict:
        """GET"""

        url = f"{self.url_base}/companies/{self.token_van}/requests?code={codigo_relacionamento}"

        payload = {}
        headers = {'Content-Type': 'application/json',
                   'authorization': f'Bearer {token_api}'
                   }

        response = requests.get(url, headers=headers, data=payload)
        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            return 'ERRO'

    def captura_key_relacionamento(self,
                               token_api: str,
                               codigo_relacionamento: str
                               ) -> dict:
        """
        GET API retorna a key do relacionamento.
        Se mais de 1 relacionamento com o mesmo codigo então retorna "ERRO".
        Se status_code diferente de "OK" então retorna "ERRO".
        """

        url = f"{self.url_base}/companies/{self.token_van}/requests?code={codigo_relacionamento}"
        payload = {}
        headers = {'Content-Type': 'application/json',
                   'authorization': f'Bearer {token_api}'
                   }

        response = requests.get(url, headers=headers, data=payload)
        if response.status_code == requests.codes.ok:
            key_relacionamento = response.json()
            if key_relacionamento['count'] == 1:
                return key_relacionamento['results'][0]['key']
            else:
                return "ERRO"
        else:
            return "ERRO"

    def captura_status_relacionamento(self,
                               token_api: str,
                               codigo_relacionamento: str
                               ) -> dict:
        """
        GET API retorna o status do relacionamento.
        Se mais de 1 relacionamento com o mesmo codigo então retorna "ERRO".
        Se status_code diferente de "OK" então retorna "ERRO".
        """

        url = f"{self.url_base}/companies/{self.token_van}/requests?code={codigo_relacionamento}"

        payload = {}
        headers = {'Content-Type': 'application/json',
                   'authorization': f'Bearer {token_api}'
                   }

        response = requests.get(url, headers=headers, data=payload)
        if response.status_code == requests.codes.ok:
            key_relacionamento = response.json()
            if key_relacionamento['count'] == 1:
                return key_relacionamento['results'][0]['status']
            else:
                return "ERRO"
        else:
            return "ERRO"

    def altera_status_relacionamento(self,
                                     token_api: str,
                                     key_relacionamento: str,
                                     status: str
                                     ) -> str:
        """
        PUT Altera status do relacionamento, se realizado então retorna "OK" senão "ERRO".
        """

        url = f"{self.url_base}/companies/{self.token_van}/requests/{key_relacionamento}/statuses/{status}"

        payload = {}
        headers = {'accept': 'application/json',
                   'authorization': f'Bearer {token_api}'
                   }

        response = requests.put(url, headers=headers, data=payload)

        if response.status_code == 204:
            return "OK"
        else:
            return response.json()

    def captura_relacionamento(self,
                               token_api: str,
                               codigo_relacionamento: str
                               ) -> dict:
        """GET"""

        url = f"{self.url_base}/companies/{self.token_van}/requests?code={codigo_relacionamento}"

        payload = {}
        headers = {'Content-Type': 'application/json',
                   'authorization': f'Bearer {token_api}'
                   }

        response = requests.get(url, headers=headers, data=payload)
        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            return 'ERRO'

    def altera_relacionamento_extrato(self,
                                      token_api: str,
                                      key_relacionamento: str,
                                      relacionamento: dict,
                                      contato: str,
                                      telefone: str,
                                      agencia: str,
                                      id_caixa_postal: str,
                                      nome_da_pasta_retorno_commander: str
                                      ) -> dict:
        """GET"""

        url = f"{self.url_base}/companies/{self.token_van}/requests/{key_relacionamento}"

        payload = {
                   "customer_document":relacionamento['results'][0]['customer_document'],  # Este campo é obrigatório.
                   "customer_name":relacionamento['results'][0]['customer_name'],  # Este campo é obrigatório.
                   "customer_contact":contato,  # Este campo é obrigatório.
                   "customer_phone":telefone,  # Este campo é obrigatório.
                   "customer_email":relacionamento['results'][0]['customer_email'],  # Este campo é obrigatório.
                   "customer_domain":relacionamento['results'][0]['customer_domain'],
                   "institution_user_name":"operacoes contas",  # Este campo é obrigatório.
                   # "institution_user_phone":"(11) 2968-0779",  # Este campo é obrigatório.
                   "agreement_number":relacionamento['results'][0]['agreement_number'],
                   # "institution_user_email":relacionamento['results'][0]['institution_user_email'],  # Este campo é obrigatório.
                   "agreement_branch_number":agencia,  # Este campo é obrigatório.
                   "agreement_account_number":relacionamento['results'][0]['agreement_account_number'],  # Este campo é obrigatório.
                   # "agreement_check_digit_number":"8",  # Este campo é obrigatório.
                   # "environment":relacionamento['results'][0]['environment'], # Este campo é obrigatório.
                   "cost":relacionamento['results'][0]['cost'],
                   "dsn_ret":relacionamento['results'][0]['dsn_ret'],  # Este campo é obrigatório.
                   "comments":relacionamento['results'][0]['comments'],
                   "environment":"PRODUCTION",
                   "additional":{
                       "id_caixa_postal": id_caixa_postal,
                       # "apelido":"teste04",
                       # "custo_do_trafego":"0",  # Este campo é obrigatório.
                       # "faturamento":"0",
                       "nome_da_pasta_retorno_commander": nome_da_pasta_retorno_commander,
                       # "nome_do_grupo":"anderson1231",
                       "posto": relacionamento['results'][0]['additional']['posto']
                   },
                   # "editable":True,
                   # "import_csv_file":None,
                   # "register_user":False
                   }

        headers = {'Content-Type': 'application/json',
                   'authorization': f'Bearer {token_api}'
                   }

        response = requests.put(url, headers=headers, json=payload)
        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            return response.status_code, response.json()

    def altera_relacionamento_cobranca(self,
                                      token_api: str,
                                      key_relacionamento: str,
                                      relacionamento: dict,
                                      contato: str,
                                      telefone: str,
                                      agencia: str,
                                      id_caixa_postal: str,
                                      nome_da_pasta_retorno_commander: str
                                      ) -> dict:
        """GET"""

        url = f"{self.url_base}/companies/{self.token_van}/requests/{key_relacionamento}"

        payload = {"customer_document":relacionamento['results'][0]['customer_document'],  # Este campo é obrigatório.
                   "customer_name":relacionamento['results'][0]['customer_name'],  # Este campo é obrigatório.
                   "customer_contact":contato,  # Este campo é obrigatório.
                   "customer_phone":telefone,  # Este campo é obrigatório.
                   "customer_email":relacionamento['results'][0]['customer_email'],  # Este campo é obrigatório.
                   "customer_domain":relacionamento['results'][0]['customer_domain'],
                   "institution_user_name":"PJTECH",  # Este campo é obrigatório.
                   "institution_user_phone":'5133588000',  # Este campo é obrigatório.
                   "agreement_number":relacionamento['results'][0]['agreement_number'],
                   "institution_user_email":['pjtech@sicredi.com.br'],  # Este campo é obrigatório.
                   "agreement_branch_number":agencia,  # Este campo é obrigatório.
                   "agreement_account_number":relacionamento['results'][0]['agreement_account_number'],  # Este campo é obrigatório.
                   "cost":relacionamento['results'][0]['cost'],
                   "dsn_rem": relacionamento['results'][0]['dsn_rem'], # Este campo é obrigatório.
                   "dsn_ret":relacionamento['results'][0]['dsn_ret'],  # Este campo é obrigatório.
                   "comments":relacionamento['results'][0]['comments'],
                   "environment":"PRODUCTION",
                   "additional":{
                       "id_caixa_postal": id_caixa_postal,
                       "nome_da_pasta_retorno_commander": nome_da_pasta_retorno_commander,
                       "posto": relacionamento['results'][0]['additional']['posto'],
                       "layout": relacionamento['results'][0]['additional']['layout'],
                   },
                   }

        headers = {'Content-Type': 'application/json',
                   'authorization': f'Bearer {token_api}'
                   }

        response = requests.put(url, headers=headers, json=payload)
        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            return response.status_code, response.json()

    def captura_relacionamento_integracao(self,
                                          token_api: str,
                                          token_api_integracao: str,
                                          key_relacionamento: str
                                          ) -> dict:
        """GET"""

        url = f"{self.url_base}/integrations/requests/{key_relacionamento}"

        payload = {}
        headers = {'accept': 'application/json',
                   'service-token': f'{token_api_integracao}',
                   'authorization': f'Bearer {token_api}'
                   }

        response = requests.get(url, headers=headers, data=payload)
        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            return 'ERRO'
