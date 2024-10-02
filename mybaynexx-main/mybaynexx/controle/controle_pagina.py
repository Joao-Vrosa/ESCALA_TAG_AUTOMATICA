from typing import Any
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class ControlePagina:
    """Funções para controle de páginas."""

    def __init__(self, driver: Any) -> None:
        super().__init__()
        self._driver: Any = driver

    def abrir_pagina(self, url: str) -> None:
        """Função para acessar a página de login no navegador."""
        self._driver.get(url)

    def aguardar(self, tempo: str, elemento: tuple) -> None:
        """Função para aguardar um elemente aparecer na tela."""
        WebDriverWait(self.driver, tempo).until(expected_conditions.presence_of_element_located(elemento))
