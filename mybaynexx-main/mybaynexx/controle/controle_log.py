from os import mkdir
from time import strftime
from os.path import join, isdir
from logging import Logger, Formatter, FileHandler, StreamHandler, CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET
from locale import setlocale, LC_ALL
from json import dumps
from requests import post


class ControleLog(Logger):
    """Controla as configurações do arquivo de log."""

    def __init__(self, directory: str, console: bool = False, name: str = "log", level: int = NOTSET) -> None:
        setlocale(LC_ALL, 'pt_BR.utf-8')

        if not isdir(directory):
            mkdir(directory)

        Logger.__init__(self, name, level)
        log_format = Formatter("L%(lineno)03d ** %(asctime)s-%(msecs)03d %(levelname)s: %(message)s",
                               datefmt="%d/%m/%Y %H:%M:%S")  # Padrão das mensagens.
        arq_log = FileHandler(join(directory, strftime("%Y-%m-%d") + ".log"))
        arq_log.setFormatter(log_format)
        self.addHandler(arq_log)

        if console:
            console = StreamHandler()
            console.setFormatter(log_format)
            self.addHandler(console)

    def header(self):
        """
        Adiciona uma linha de cabeçalho no arquivo de log.
        Sempre usar no início do processo.
        """

        self.info("-------------------------------------- PROCESSO INICIADO --------------------------------------")

    def footer(self):
        """
        Adiciona uma linha de rodapé no arquivo de log.
        Sempre usar no final do processo.
        """

        self.info("-----------------------------------------------------------------------------------------------")
        self.info("------------------------------------- PROCESSO FINALIZADO -------------------------------------\n")

    def ruler(self):
        """
        Adiciona uma linha tracejada no arquivo de log.
        Pode ser utilizada em qualquer momento, serve para separar o log em seções.
        """

        self.info("-----------------------------------------------------------------------------------------------")

    @classmethod
    def google_chat(cls, key: str, msg: str):
        """
        Google Chat
        Documentacao: https://developers.google.com/workspace/chat/quickstart/webhooks?hl=pt-br
        Envia mensagens via Google Chat
        """

        url = key
        app_message = {"text": msg}
        message_headers = {"Content-Type": "application/json; charset=UTF-8"}

        response = post(
            url=url,
            headers=message_headers,
            data=dumps(app_message)
        )

        return response.status_code

    CRT = CRITICAL
    ERR = ERROR
    WRN = WARNING
    INF = INFO
    DBG = DEBUG
