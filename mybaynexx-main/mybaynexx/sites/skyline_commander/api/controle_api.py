import requests


class ControleAPICommander:
    """ Classe para geracao de Token e Cookies de sessão da API do Skyline Commander/CEF. """

    # Variaveis para acesso a API Skyline Commander:
    dominio: str = 'https://webedi.nexxera.io'
    skyline_login: str = f'{dominio}/skyline-web-gateway/skyadmin/login'
    skyline_consultar_criar: str = f'{dominio}/skyline-web-gateway/skyadmin/users/'
    url_teste_sessao_ativa: str = f'{dominio}/skyline-web-gateway/checkauth'

    # Variaveis para acesso a API Skyline Commander CEF:
    cef_dominio: str = 'https://webedicaixa.nexxera.io'
    cef_skyline_login: str = f'{cef_dominio}/skyline-web-gateway/skyadmin/login'
    cef_skyline_consultar_criar: str = f'{cef_dominio}/skyline-web-gateway/skyadmin/users/'
    cef_teste_sessao_ativa: str = f'{cef_dominio}/skyline-web-gateway/checkauth'

    custo_percentuais: dict = {'0': '100% EMPRESA - PRODUCAO',
                               '1': '100% INSTITUICAO - PRODUCAO',
                               '2': '50% EMPRESA - PRODUCAO',
                               '3': 'CP CLIENTE',
                               '4': 'CP BANCOS',
                               '5': 'CP CONTINGENCIA',
                               '6': 'CP REDISTRIBUICAO',
                               '7': '100% NEXXERA',
                               '8': 'USO INTERNO'
                               }

    chave_custo_a_ignorar_demais_campos_billing: list = ['3',
                                                         '4',
                                                         '5',
                                                         '6',
                                                         '8'
                                                         ]  # custo_percentuais

    faturamento_descricao: dict = {'0': 'FATURAVEL',
                                   '1': 'NAO FATURAVEL',
                                   '2': 'FATURAVEL CANCELADO',
                                   '3': 'NAO FATURAVEL CANCELADO'
                                   }

    aba_billing: dict = {1: 'Grupo',
                         2: 'Razao Social',
                         3: 'CNPJ',
                         4: 'Custo',
                         5: 'Faturamento',
                         6: 'Banco',
                         7: 'Produto',
                         8: 'Status',
                         9: 'Contrato de Faturamento'
                         }

    aba_billing_vazio: dict = {1: 'Grupo',
                               2: 'Razao Social',
                               3: 'CNPJ',
                               4: 'Custo',
                               5: 'Faturamento'
                               }

    aba_properties: dict = {'descr': 'Descricao',
                            'coment': 'Comentario',
                            'keywords': 'Palavra chave',
                            'grupo': 'Grupo',
                            'auth': 'Habilitado para comunicar',
                            'cleanmailers': 'Limpar Mailers',
                            'tpprotocolo': 'Protocolar arquivos',
                            'forcechangepwd': 'Expirar senha',
                            'tipo': 'Caixa robô',
                            'ToUseFurtherProcessingOfReceivedFiles': 'Pós-processamento de arquivos',
                            'script': 'Script',
                            'masks': 'Renomeamento',
                            'ips': 'IPs',
                            'email': 'E-mails'
                            }

    aba_properties_vazio: dict = {'descr': 'Descricao',
                                  'coment': 'Comentario',
                                  'keywords': 'Palavras chaves',
                                  'grupo': 'Grupo'
                                  }

    @classmethod
    def login(cls, usuario: str, senha: str, url: str) -> requests.Session:
        """ Metodo para realizar login no Portal do Skyline Commander/CEF via API. """

        headers: dict = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json'}
        data: dict = {'username': usuario, 'password': senha}
        return requests.post(url, headers=headers, data=data)        

    @classmethod
    def gera_token_cookie(cls, login: requests.Session) -> tuple:
        """ Metodo para realizar a autenticação na API do Portal Skyline Commander/CEF. """

        login = login

        if login.status_code == requests.codes.ok:
            x_csrf_token = login.json()
            token: str = x_csrf_token['x-csrf_token']
            cookies: dict = {'session': login.cookies['session']}
            return login, token, cookies
        else:
            return login, None, None

    @classmethod
    def cadastrar(cls,
                  token: requests.Session,
                  cookies: requests.Session,
                  cxp_est: str,
                  url: str,
                  grupo: str = None,
                  razao: str = None,
                  comentario: str = None,
                  faturamento: str = None,
                  comunicar: str = None
                  ) -> str:
        """ Metodo para realizar o cadastro da Caixa Postal """

        headers = {'Content-Type': 'application/x-www-form-urlencoded',
                   'Accept': 'application/json',
                   'X-CSRFToken': token
                   }
        data = {'name': cxp_est,
                'forceadd': 'true'
                }
        if razao is not None:
            data.update({'description': razao})
        if comentario is not None:
            data.update({'coment': comentario})
        if faturamento is not None:
            data.update({'keywords': faturamento})
        if grupo is not None:
            data.update({'group': grupo})
        if comunicar is not None:
            data.update({'auth': comunicar})
        retorno = requests.post(url, cookies=cookies, headers=headers, data=data)
        if retorno.status_code == requests.codes.ok:
            return 'CADASTRADA'

        elif retorno.status_code == requests.codes.unauthorized:
            return 'NAO_AUTORIZADA'

        else:
            return 'CADASTRO_ERRO'
    # cadastrar

    @classmethod
    def billing(cls,
                token: requests.Session,
                cookies: requests.Session,
                cxp_est: str,
                url: str,
                grupo: str = None,
                razao: str = None,
                pfpj: str = None,
                cod_custo: int = None,
                cod_faturamento: int = None,
                banco: str = None,
                produto: str = None,
                status: str = None,
                contrato_faturamento: str = None
                ) -> str:
        """ Metodo para realizar a definicao das informacoes basicas da Aba Billing Properties da Caixa Postal """

        headers = {'Accept': 'application/json',
                   'X-CSRFToken': token
                   }
        data = {}
        if grupo is not None:
            data.update({'1': grupo})
        if razao is not None:
            data.update({'2': razao})
        if pfpj is not None:
            data.update({'3': pfpj})
        if cod_custo is not None:
            data.update({'4': cod_custo})
        if cod_faturamento is not None:
            data.update({'5': cod_faturamento})
        if banco is not None:
            data.update({'6': banco})
        if produto is not None:
            data.update({'7': produto})
        if status is not None:
            data.update({'8': status})
        if contrato_faturamento is not None:
            data.update({'9': contrato_faturamento})
        retorno = requests.put(f'{url}/{cxp_est}/billing_properties', cookies=cookies, headers=headers, json=data)
        if retorno.status_code == requests.codes.ok:
            return 'BILLING_OK'

        elif retorno.status_code == requests.codes.unauthorized:
            return 'NAO_AUTORIZADA'

        else:
            return 'BILLING_ERRO'
    # billing

    @classmethod
    def propriedades(cls,
                     token: requests.Session,
                     cookies: requests.Session,
                     cxp_est: str,
                     url: str,
                     grupo: str = None,
                     razao: str = None,
                     comentario: str = None,
                     faturamento: str = None,
                     comunicar: str = None,
                     limpa_mailers: str = None,
                     protocolar_arq: str = None,
                     expirar_senha: str = None,
                     caixa_robo: str = None,
                     pos_proces_arq: str = None,
                     script: str = None,
                     renomeamento: str = None,
                     ips: str = None,
                     emails: str = None
                     ) -> str:
        """ Metodo para realizar a definicao das informacoes basicas da Aba Properties da Caixa Postal """

        headers = {'Content-Type': 'application/x-www-form-urlencoded',
                   'Accept': 'application/json',
                   'X-CSRFToken': token
                   }
        data = []
        if razao is not None:
            data.append(f'description={razao}')
        if comentario is not None:
            data.append(f'coment={comentario}')
        if faturamento is not None:
            data.append(f'keywords={faturamento}')
        if grupo is not None:
            data.append(f'group={grupo}')
        if comunicar is not None:
            data.append(f'auth={comunicar}')
        if limpa_mailers is not None:
            data.append(f'cleanmailers={limpa_mailers}')
        if protocolar_arq is not None:
            data.append(f'tpprotocol={protocolar_arq}')
        if expirar_senha is not None:
            data.append(f'forcechangepwd={expirar_senha}')
        if caixa_robo is not None:
            data.append(f'tipo={caixa_robo}')
        if pos_proces_arq is not None:
            data.append(f'processing={pos_proces_arq}')
        if script is not None:
            data.append(f'script={script}')
        if renomeamento is not None:
            data.append(f'masks={renomeamento}')
        if ips is not None:
            data.append(f'ips={ips}')
        if emails is not None:
            data.append(f'email={emails}')
        retorno = requests.put(f'{url}/{cxp_est}/properties', cookies=cookies, headers=headers, data='&'.join(data))
        if retorno.status_code == requests.codes.ok:
            return 'PROPRIEDADES_OK'

        elif retorno.status_code == requests.codes.unauthorized:
            return 'NAO_AUTORIZADA'

        else:
            return 'PROPRIEDADES_ERRO'
    # propriedades

    @classmethod
    def senha(cls,
              token: requests.Session,
              cookies: requests.Session,
              cxp_est: str,
              senha: str,
              url: str
              ) -> str:
        """ Metodo para realizar a definicao da senha da Caixa Postal ou Estacao de Log """

        headers = {'Content-Type': 'application/x-www-form-urlencoded',
                   'Accept': 'application/json',
                   'X-CSRFToken': token
                   }
        data = {'password': senha
                }
        retorno = requests.put(f'{url}/{cxp_est}/password', cookies=cookies, headers=headers, data=data)
        if retorno.status_code == requests.codes.ok:
            return 'SENHA_OK'

        elif retorno.status_code == requests.codes.unauthorized:
            return 'NAO_AUTORIZADA'

        else:
            return 'SENHA_ERRO'
    # senha

    @classmethod
    def consultar_cxp_est(cls,
                          token: requests.Session,
                          cookies: requests.Session,
                          cxp_est: str,
                          url: str
                          ) -> str:
        """ Metodo para consultar a existencia do cadastro da Caixa Postal ou Estacao de Log """

        headers = {'Accept': 'application/json',
                   'X-CSRFToken': token
                   }
        retorno = requests.get(f'{url}/{cxp_est}/properties', cookies=cookies, headers=headers)
        if retorno.status_code == requests.codes.ok:
            return 'ENCONTRADA'

        elif retorno.status_code == requests.codes.not_found:
            return 'NAO_ENCONTRADA'

        elif retorno.status_code == requests.codes.unauthorized:
            return 'NAO_AUTORIZADA'

        else:
            return 'RETORNO_NAO_IDENTIFICADO'
    # consultar_cxp_est

    @classmethod
    def consultar(cls,
                  token: requests.Session,
                  cookies: requests.Session,
                  url: str,
                  filtro: str = None,
                  limite: int = None,
                  pagina: int = None
                  ) -> str:
        """ Metodo para consultar todos os cadastros de Caixa Postal e Estacao de Log com ou sem filtro """

        headers = {'Accept': 'application/json',
                   'X-CSRFToken': token
                   }
        params = {}
        if filtro is not None:
            params.update({'filter': filtro})
        if limite is not None:
            params.update({'per_page': limite})
        if pagina is not None:
            if pagina > 1:
                params.update({'page': pagina})
        retorno = requests.get(url, cookies=cookies, headers=headers, params=params)
        if retorno.status_code == requests.codes.ok:
            return retorno.json()

        elif retorno.status_code == requests.codes.unauthorized:
            return 'NAO_AUTORIZADA'

        else:
            return 'CONSULTA_ERRO'
    # consultar

    @classmethod
    def consultar_abas(cls,
                       token: requests.Session,
                       cookies: requests.Session,
                       cxp_est: str,
                       aba: str,
                       url: str
                       ) -> str:
        """ Metodo para consultar os registros das Abas do cadastro """

        headers = {'Accept': 'application/json',
                   'X-CSRFToken': token
                   }
        retorno = requests.get(f'{url}/{cxp_est}/{aba}', cookies=cookies, headers=headers)
        if retorno.status_code == requests.codes.ok:
            return retorno.json()

        elif retorno.status_code == requests.codes.unauthorized:
            return 'NAO_AUTORIZADA'

        else:
            return 'CONSULTA_ERRO'
    # consultar_abas
