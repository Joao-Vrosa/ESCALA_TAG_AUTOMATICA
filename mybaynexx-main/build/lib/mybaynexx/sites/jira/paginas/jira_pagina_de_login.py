from typing import Any
from ..localizadores.jira_elementos_de_login import JiraLoginElementos


class JiraPaginaLogin(JiraLoginElementos):
    """Funções da página de Login do Jira."""

    def __init__(self, driver: Any) -> None:
        super().__init__()
        self._driver: Any = driver

    def abrir_pagina(self, url: str) -> None:
        """Função para acessar a página de login no navegador."""
        self._driver.get(url)

    def logar(self, username: str, password: str) -> None:
        """Função para fazer o login na página."""
        self._driver.find_element(*self.usuario_textbox_id).send_keys(username)
        self._driver.find_element(*self.senha_textbox_id).send_keys(password)
        self._driver.find_element(*self.login_button_id).click()
