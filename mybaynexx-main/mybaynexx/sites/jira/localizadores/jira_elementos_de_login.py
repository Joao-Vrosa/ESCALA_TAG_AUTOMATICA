from selenium.webdriver.common.by import By


class JiraLoginElementos:
    """Elementos HTML da página de login do Jira."""

    def __init__(self) -> None:
        self.usuario_textbox_id: tuple = (By.ID, "login-form-username")
        self.senha_textbox_id: tuple = (By.ID, "login-form-password")
        self.login_button_id: tuple = (By.ID, "login")
