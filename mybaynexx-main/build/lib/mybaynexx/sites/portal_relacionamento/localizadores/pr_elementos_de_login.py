from selenium.webdriver.common.by import By


class PortalRelacionamentosLoginElementos:
    """Elementos HTML da página de login do Jira."""

    def __init__(self) -> None:
        self.usuario_textbox_id: tuple = (By.ID, "username")
        self.senha_textbox_id: tuple = (By.ID, "password")
        self.login_button_id: tuple = (By.ID, "btEnviar")
