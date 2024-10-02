from selenium.webdriver.common.by import By


class LocalizadoresPadroes:
    """ Base de localizadores minha nexx padroes """
    acessar_como_usuario: tuple = (By.XPATH, "(//span[normalize-space()='Entrar'])[1]")
    acessar_como_colaborador: tuple = (By.ID, 'corporateLogin')  # 1 - Icone para abrir tela de login inicial.
    text_box_username: tuple = (By.XPATH, '//*[@id="username"]')  # 2 - Campo input para ser inserido o usuario.
    text_box_password: tuple = (By.XPATH, '//*[@id="password"]')  # 3 - Campo input para ser inserido a senha do usuario.
    icone_perfil: tuple = (By.XPATH, "(//mat-icon[normalize-space()='person'])[1]")  # 4 - Elemento como alvo para aguarda o campo aparecer na tela incial após login.
    botao_sair: tuple = (By.ID, "//span[normalize-space()='Sair']")  # 5 - Botao de logout para sair do Minha Nexx.
    clica_em_relacionamento: tuple = (By.XPATH, '//*[@id="Path_4381"]')  # 6 - Icone na tela principal Minha Nexx para abrir o relacionamento.
    clica_em_codigo: tuple = (By.XPATH, '//*[@id="mat-select-0"]/div/div[1]')  # 7 - Campo "Código" na aba relacionamentos onde tem a informação coluna código para abrir mais filtros.
    clica_em_mais_filtros: tuple = (By.XPATH, '//*[@id="mat-option-34"]/span')  # 8 - Campo "Mais filtros" na aba relacionamentos onde tem a informação coluna código para abrir mais filtros.
    lista_de_status = tuple = (By.XPATH, '//*[@id="mat-dialog-0"]/pr-form-more-filters/form/mat-dialog-content/div/div[2]/mat-form-field[2]/div/div[1]/div')  # 9 - Lista de "Status" para selecionar os status que um relacionamento pode esta.
    # Lista dos "Status" de um código na opção filtros.
    filtro_recebido = tuple = (By.XPATH, '//*[@id="mat-option-42"]/mat-pseudo-checkbox')  # Recebido.
    filtro_atendimento = tuple = (By.XPATH, '//*[@id="mat-option-43"]/mat-pseudo-checkbox')  # Em atendimento.
    filtro_esperando_autorizacao = tuple = (By.XPATH, '//*[@id="mat-option-44"]/mat-pseudo-checkbox')  # Esperando autorização.
    filtro_aguardando_aprovacao = tuple = (By.XPATH, '//*[@id="mat-option-45"]/mat-pseudo-checkbox')  # Aguardando aprovação.
    filtro_pendente_instituicao = tuple = (By.XPATH, '//*[@id="mat-option-46"]/mat-pseudo-checkbox')  # Pendente instituição.
    filtro_pendente_cliente = tuple = (By.XPATH, '//*[@id="mat-option-47"]/mat-pseudo-checkbox')  # Pendente cliente.
    filtro_pendente_van = tuple = (By.XPATH, '//*[@id="mat-option-48"]/mat-pseudo-checkbox')  # Pendente Van.
    filtro_revisado = tuple = (By.XPATH, '//*[@id="mat-option-49"]/mat-pseudo-checkbox')  # Revisado.
    filtro_rejeitado = tuple = (By.XPATH, '//*[@id="mat-option-50"]/mat-pseudo-checkbox')  # Rejeitado.
    filtro_implantacao = tuple = (By.XPATH, '//*[@id="mat-option-51"]/mat-pseudo-checkbox')  # Implantação.
    filtro_relacionamento_aprovado = tuple = (By.XPATH, '//*[@id="mat-option-52"]/mat-pseudo-checkbox')  # Relacionamento aprovado.
    filtro_falha_na_autorizacao_do_relacionamento = tuple = (By.XPATH, '//*[@id="mat-option-53"]/mat-pseudo-checkbox')  # Falha na autorização do relacionamento.
    filtro_pronto_para_implantar = tuple = (By.XPATH, '//*[@id="mat-option-54"]/mat-pseudo-checkbox')  # Pronto para implantar.
    filtro_implantacao_finalizada = tuple = (By.XPATH, '//*[@id="mat-option-55"]/mat-pseudo-checkbox')  # Implantação finalizada.
    filtro_falha_na_implatacao = tuple = (By.XPATH, '//*[@id="mat-option-56"]/mat-pseudo-checkbox')  # Falha na implantação.
    filtro_agendado = tuple = (By.XPATH, '//*[@id="mat-option-57"]/mat-pseudo-checkbox')  # Agendado.
    filtro_click_responsaveis = tuple = (By.XPATH, "(//div[@class='mat-select-arrow'])[8]")  # Filtro localizado e utilizado para a funcionalidae click para poder escrever o nome do responsavel abaixo.
    filtro_input_responsaveis = tuple = (By.XPATH, "//div[@class='cdk-overlay-pane cdk-overlay-pane-select-search']//div//div//mat-option[1]//span//div//input")  # Filtro para inserir o nome do responsavel para realizar a busca dos codigos linkadas a ele.
    salvar_filtros = tuple = (By.XPATH, "(//button[@type='button'])[49]")  # Botao localizado na tela Filtros para salvar a aplicar os filtros selecionados.
    aplicar_filtros = tuple = (By.XPATH, "(//button[@type='submit'])[2]")  # Botao localizado na tela Filtros para aplicar os filtros selecionados.
    # Lista dos "Status" de um código na opção filtros.
    botao_editar = tuple = (By.XPATH, "//table[@class='mat-table']//tbody//tr[1]//td//button[@class='mat-menu-trigger mat-icon-button mat-button-base' and @aria-label='more actions' ]")  # Botao para editar o convenio listado na tela de relacionamento.
    icone_carregamento = tuple = (By.XPATH, "//div//mat-icon[@class='mat-icon notranslate material-icons mat-icon-no-color' and @aria-hidden='true'][normalize-space()='refresh']")  # Icone de carregamento de pagina
    todos_os_codigo = tuple = (By.XPATH, "//div//td[@class='mat-cell cdk-column-code mat-column-code ng-tns-c26-10 ng-star-inserted']")  # Seleciona todos os codigos que estao aparecendo na tela de relacionamento apos aplicar os filtros.
    tela_inicial_consulta = tuple = (By.XPATH, "//span[@class='mat-body-1 ng-tns-c12-1 ng-star-inserted'][.='Nenhum dado carregado']")  # Tela inicial de consultas relacionamentos
    campo_pesquisar = tuple = (By.XPATH, "(//input[@id='mat-input-1'])[1]")  # Campo para pesquisar os dados do relacionamento na tela de relacionamento, ex: convenio, CNPJ etc...
    botao_editar1 = tuple = (By.XPATH, "(//button[normalize-space()='Editar'])[1]")  # Opção para editar o relacionamento dentro dos 3 pontinhos "..."
    # Lista de opções dentro do template - Pagamento a Fornecedores, Bradesco e BB.
    elemento_template = tuple = (By.XPATH, "(//div[@class='mat-chip-list-wrapper']//input[@id='mat-chip-list-input-0'])[1]")  # Aguardar o elemento do template carregar na tela, obs: Não validado no mapeamento.
    campo_emails_secundarios = tuple = (By.XPATH, "(//div[@class='mat-form-field-infix'])[15]")  # Opção para visualisar o campo dentro do template.
    campo_dominio = tuple = (By.XPATH, "(//input[@id='customer_domain'])[1]")  # Campo para informar o dominio dentro do template.
    container_template = tuple = (By.XPATH, "(//div[@class='modal-content-container'])[1]")  # Campo com todos os elementos e input dentro do template.
    campo_id_caixa_postal = tuple = (By.XPATH, "(//input[@id='id_caixa_postal'])[1]")  # Campo para informar o numero da caixa postal do cliente no manager.
    campo_observacoes = tuple = (By.XPATH, "(//textarea[@id='comments'])[1]")  # Campo referente a Observações dentro do template ao editar o convênio.
    campo_apelido = tuple = (By.XPATH, "(//input[@id='apelido'])[1]")  # Campo para informar o apelido no template.
    campo_grupo_pe = tuple = (By.XPATH, "(//input[@id='identificador_grupo'])[1]")  # Campo para informar o grupo/sigla do cliente no Portal de Pagamento.
    campo_tipo_inscricao = tuple = (By.XPATH, "(//input[@id='identificador_do_tipo_de_inscricao_pagador'])[1]")  # Campo para informar o tipo de inscrição do pagador, 1 = CPF 2 = CNPJ no template.
    campo_caixa_postal_banco = tuple = (By.XPATH, "(//input[@id='caixa_postal_banco'])[1]")  # Campo para informar a caixa postal banco do cliente no template para ser cadastrado no Portal de Pagamento.
    campo_caixa_postal_cliente = tuple = (By.XPATH, "(//input[@id='caixa_postal_cliente'])[1]")  # Campo para informar a caixa postal cliente no template para ser cadastrado no portal de pagamento.
    campo_status_codigo = tuple = (By.XPATH, "/html[1]/body[1]/div[3]/div[2]/div[1]/mat-dialog-container[1]/pr-form-relationship[1]/mat-dialog-content[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/div[4]/mat-form-field[1]/div[1]/div[1]/div[1]")  # Campo para selecionar o status do codigo
    campo_status_pronto_para_implantar = tuple = (By.XPATH, "(//span[contains(text(),'Pronto para implantar')])[1]")  # Campo para selecionar o status do codigo "Pronto para implantar"
    campo_status_em_atendimento = tuple = (By.XPATH, "(//span[contains(text(),'Em atendimento')])[1]")  # Campo para selecionar o status do codigo "Em atendimento"
    campo_status_concluido = tuple = (By.XPATH, "//span[contains(text(),'Concluído')]")  # Campo para selecionar o status do codigo "Concluido"
    titulo_editar_cadastro = tuple = (By.XPATH, "//h6[contains(normalize-space(),'Editar cadastro')]")  # Titulo editar cadastro dentro do template.
    titulo_relacionamento = tuple = (By.XPATH, "//div[@class='mat-tab-label-content'][text()='RELACIONAMENTO']")
    campo_nome_empresa = tuple = (By.XPATH, "//form//mat-form-field[2]//div[1]//div[@class='mat-form-field-flex']//div//input[@id='customer_name']")  # Campo para escrever o nome da empresa dentro do formulario/template após editar o codigo.
    campo_dsname_remessa = tuple = (By.XPATH, "(//input[@id='dsn_rem'])[1]")  # Campo para escrever o dsname de remessa no template.
    campo_dsname_retorno = tuple = (By.XPATH, "(//input[@id='dsn_ret'])[1]")  # Campo para escrever o dsname de retorno no template.
    botao_salvar = tuple = (By.XPATH, "(//button[@class='big-button mt-40 mb-55 mat-flat-button mat-button-base mat-accent'])[1]")  # Campo para salvar o template editado.
    campo_dv_agencia = tuple = (By.XPATH, "(//input[@id='dv_agencia'])[1]")  # Campo para colocar o dv da agência dentro do template.
    botao_auto_implantar = tuple = (By.XPATH, "(//button[normalize-space()='Auto implantar'])[1]")  # Botao para auto implantar o codigo filtrado na tela de relacionamento
