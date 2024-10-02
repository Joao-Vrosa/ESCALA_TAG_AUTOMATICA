import psycopg2
import oracledb as odb
import mysql.connector
import logging


class ControleDB:
    """ 
    Classe de controle para efetuar consultas em bases de dados:
     - Postgres
     - MySQL
     - Oracle
    """

    def __init__(self, log: logging) -> None:
        self.log = log
        

    def mysql_consulta_colunas(self, sql: str, config: dict) -> list | str:
        """ Funcao para realizar consultas MySQL local """

        vcon = None
        try:
            vcon = mysql.connector.connect(**config)
            cursor_vcon = vcon.cursor()
            cursor_vcon.execute(sql)
            retorno = cursor_vcon.fetchall()
            cursor_vcon.close()
            vcon.close()
            return retorno
        except Exception as erro:
            self.log.error(erro)
            return "ERRO"


    def mysql_consulta_coluna_unica(self, sql: str, config: dict) -> str:
        """ Funcao para realizar consultas MySQL local """

        vcon = None
        try:
            vcon = mysql.connector.connect(**config)
            cursor_vcon = vcon.cursor()
            cursor_vcon.execute(sql)
            for coluna in cursor_vcon.fetchall():
                cursor_vcon.close()
                vcon.close()
                return coluna[0]
        except Exception as erro:
            self.log.error(erro)
            return "ERRO"


    def mysql_consulta_status_conexao(self, config: dict) -> str:
        """ Funcao para realizar consultas MySQL local """

        vcon = None
        try:
            vcon = mysql.connector.connect(**config)
            cursor_vcon = vcon.cursor()
            vcon.close()
            cursor_vcon.close()
            return "OK"
        except Exception as erro:
            self.log.error(erro)
            return "ERRO"


    def mysql_atualizar_registros(self, sql: str, config: dict) -> str:
        """ Funcao para realizar atualizacoes MySQL local """

        vcon = None
        try:
            vcon = mysql.connector.connect(**config)
            cursor_vcon = vcon.cursor()
            cursor_vcon.execute(sql)
            vcon.commit()
            return "OK"
        except Exception as erro:
            self.log.error(erro)
            return "ERRO"

    def postgres_consulta_colunas_skyline_manager_cef(self, sql: str, config: dict) -> str | None | list:
        """ Funcao para realizar consultas no db Skyline Manager CEF e retornar todos os registros em lista """

        vcon = None
        try:
            vcon = psycopg2.connect(**config)
            cursor_vcon = vcon.cursor()
            cursor_vcon.execute(sql)
            retorno = cursor_vcon.fetchall()
            cursor_vcon.close()
            vcon.close()
            if retorno is None:
                return None
            elif len(retorno) == 0:
                return None
            else:
                return retorno
        except Exception as erro:
            self.log.error(erro)
            return "ERRO"

    def postgres_consulta_coluna_unica_skyline_manager_cef(self, sql: str, config: dict) -> None | str:
        """ Funcao para realizar consultas no db Skyline Manager CEF para coluna unica """

        vcon = None
        try:
            vcon = psycopg2.connect(**config)
            cursor_vcon = vcon.cursor()
            cursor_vcon.execute(sql)
            retorno = cursor_vcon.fetchone()
            cursor_vcon.close()
            vcon.close()
            if retorno is None:
                return None
            else:
                for col in retorno:
                    return col
        except Exception as erro:
            self.log.error(erro)
            return "ERRO"

    def postgres_consulta_coluna_unica_skyline_manager(self, sql: str, config: dict) -> str | None:
        """ Funcao para realizar consultas no db Skyline Manager para coluna unica """

        vcon = None
        try:
            vcon = psycopg2.connect(**config)
            cursor_vcon = vcon.cursor()
            cursor_vcon.execute(sql)
            retorno = cursor_vcon.fetchone()
            cursor_vcon.close()
            vcon.close()
            if retorno is None:
                return None
            else:
                for coluna in retorno:
                    return coluna        
        except Exception as erro:
            self.log.error(erro)
            return "ERRO"

    def oracle_consulta_coluna_unica(self, sql: str, config: odb, client: str) -> None | str:
        """ Funcao generica para realizar consultas no db Oracle para coluna unica (no modo Thick) """

        odb.init_oracle_client(lib_dir=client) # Inicializando o modo Thick
        vcon = None
        try:
            vcon = odb.connect(params=config)
            cursor_vcon = vcon.cursor()
            cursor_vcon.execute(sql)
            retorno = cursor_vcon.fetchone()
            cursor_vcon.close()
            vcon.close()
            if retorno is None:
                return None
            else:
                for coluna in retorno:
                    return coluna
        except Exception as erro:
            self.log.error(erro)
            return "ERRO"

    def oracle_consulta_colunas(self, sql: str, config: odb, client: str) -> None | str | list:
        """ Funcao generica para realizar consultas no db Oracle (no modo Thick) """

        odb.init_oracle_client(lib_dir=client)  # Inicializando o modo Thick
        vcon = None
        try:
            vcon = odb.connect(params=config)
            cursor_vcon = vcon.cursor()
            cursor_vcon.execute(sql)
            retorno = cursor_vcon.fetchall()
            cursor_vcon.close()
            vcon.close()
            if retorno is None:
                return None
            elif len(retorno) == 0:
                return None
            else:
                return retorno
        except Exception as erro:
            self.log.error(erro)
            return "ERRO"
