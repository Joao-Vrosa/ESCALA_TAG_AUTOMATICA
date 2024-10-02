from selenium.webdriver.common.by import By


class MinhaNexxLoginElementos:
    """Elementos HTML da página de login do MinhaNexx."""

    acessar_como_colaborador: tuple = (By.ID, 'corporateLogin')  # 1 - Icone para abrir tela de login inicial.
    text_box_username: tuple = (By.XPATH, '//*[@id="username"]')  # 2 - Campo input para ser inserido o usuario.
    text_box_password: tuple = (By.XPATH, '//*[@id="password"]')  # 3 - Campo input para ser inserido a senha do usuario.
    icone_perfil: tuple = (By.XPATH, "(//mat-icon[normalize-space()='person'])[1]")  # 4 - Elemento como alvo para aguarda o campo aparecer na tela incial após login.

class MinhaNexxLogoutElementos:
    """Elementos HTML da página de logout do MinhaNexx."""

    botao_sair: tuple = (By.ID, "//span[normalize-space()='Sair']")  # 5 - Botao de logout para sair do Minha Nexx.
