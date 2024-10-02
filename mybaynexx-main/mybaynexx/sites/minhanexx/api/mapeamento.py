class Mapeamento:
    """
        Registro referente a busca de dados dos relacionamentos bancarios do Minha Nexx através de API.
    """
    url_api = 'https://api.nexxera.com/minhanexx/api/v1/integrations/requests'
    # Dicionário de mapeamento dos nomes
    status = {
        'IN_PROGRESS': 'Em atendimento',
        'RECEIVED': 'Recebido',
        'WAITING_AUTHORIZATION': 'Esperando autorização',
        'WAITING_APPROVAL': 'Aguardando aprovação',
        'CUSTOMER_PENDING': 'Pendente cliente',
        'REJECTED': 'Rejeitado',
        'REQUEST_APPROVED': 'Relacionamento aprovado',
        'ABLE_TO_DEPLOY': 'Pronto para implantar',
        'DEPLOY_COMPLETED': 'Implantação finalizada',
        'DEPLOY_FAILED': 'Falha na implantação',
        'COMPLETED': 'Concluído',
        'CANCELED': 'Cancelado',
        'REQUEST_AUTHORIZATION_FAILED': 'Falha na autorização do relacionamento',
        'INSTITUTION_PENDING': 'Pendente instituição',
        'VAN_PENDING': 'Pendente Van',
        'REVIEWED': 'Revisado',
        'IMPLANTATION': 'Implantação',
        'SCHEDULED': 'Agendado'
    }

    custo = {
        'COMPANY_100': '100% EMPRESA - PRODUCAO',
        'CUSTOMER_100': '100% INSTITUICAO - PRODUCAO',
        'COMPANY_50_CUSTOMER_50': '50% EMPRESA - PRODUCAO',
        'CP_CLIENTE': 'CP CLIENTE',
        'CP_BANCOS': 'CP BANCOS',
        'CP_CONTINGENCIA': 'CP CONTINGENCIA',
        'CP_REDISTRIBUICAO': 'CP REDISTRIBUICAO',
        'USO_INTERNO': 'USO INTERNO'
    }
