from typing import Any
from  ..localizadores.pr_elementos_de_login import PortalRelacionamentosLoginElementos


class PortalRelacionamentosPaginaLogin(PortalRelacionamentosLoginElementos):
    """Funções da página do Portal de Relacionamentos."""

    def __init__(self, driver: Any) -> None:
        super().__init__()
        self._driver: Any = driver

    def logar(self, username: str, password: str) -> None:
        """Função para fazer o login na página."""
        self._driver.find_element(*self.usuario_textbox_id).send_keys(username)
        self._driver.find_element(*self.senha_textbox_id).send_keys(password)
        self._driver.find_element(*self.login_button_id).click()
