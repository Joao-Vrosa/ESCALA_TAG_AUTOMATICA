import sys
import os
import logging
import urllib3

from typing import Any
if sys.platform.startswith("win32"):
    from subprocess import CREATE_NO_WINDOW
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from .controle_log import ControleLog


class ControleDriver:
    """Controla a instalação de driver de navegador."""

    def __init__(self) -> None:
        self.driver: Any = None

    def set_navegador(self, navegador: str, dir_driver: str, dir_log: str) -> None:
        """Funcão para inicializar o carregamento do driver do navegador."""

        log = ControleLog(dir_log, False)

        urllib3.disable_warnings()  # Desativando aviso de SSL não verificado.
        os.environ["WDM_SSL_VERIFY"] = "0"  # Erro de SSL auto assinado, removendo a verificacao.
        logging.getLogger("WDM").setLevel(logging.NOTSET)  # Desabilitando o log do wdm webdriver-manager.
        os.environ["WDM_LOG"] = "0"  # Desabilitando o log do wdm webdriver-manager.
        os.environ["WDM_PRINT_FIRST_LINE"] = "False"  # Desabilitando a insercao de linhas em branco no log do webdriver

        try:
            if navegador == "ERRO":
                log.error("Houve falha ao executar o navegador! NÃO sera inicializado neste processamento.")
            elif navegador == "Chrome":
                # Definindo opcoes para o webdriver para o chrome:
                options = webdriver.ChromeOptions()
                # Desabilitando a captura padrao de bluetooth do navegador:
                options.add_experimental_option("excludeSwitches", ["enable-logging"])
                # Construindo o servico, download e instalacao do driver automaticamente:
                service = ChromeService(log_path=f"{dir_driver}/chromedriver.log")
                if sys.platform.startswith("win32"):
                    service.creation_flags = CREATE_NO_WINDOW  # CREATE_NO_WINDOW desativa a abertura do terminal.
                self.driver = webdriver.Chrome(options=options, service=service)
            elif navegador == "Firefox":
                service = FirefoxService(log_path=f"{dir_driver}/geckodriver.log")
                if sys.platform.startswith("win32"):
                    service.creation_flags = CREATE_NO_WINDOW
                self.driver = webdriver.Firefox(service=service)
            elif navegador == "Edge":
                service = EdgeService(log_path=f"{dir_driver}/edgedriver.log")
                if sys.platform.startswith("win32"):
                    service.creation_flags = CREATE_NO_WINDOW
                self.driver = webdriver.Edge(service=service)
                self.driver.find_element()
        except Exception as erro:
            log.error(erro)
