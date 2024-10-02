from app import Tag  # Importando classe principal
import pandas as pd  # Pandas para analise dos dados da planilha
from datetime import datetime  # Usada para verificasr o dia da semana


def main():
    planilha = pd.read_excel('G:\\Meu Drive\\Python\\ESCALA_TAG\\TESTE_TAG.xlsx')
    
    dia_atual = datetime.now()
    dia_semana = dia_atual.weekday()
    
    chamada = Tag(planilha)
    
    match dia_semana:
        case 0:
            chamada.tag_segunda()
        case 1:
            chamada.tag_terca()
        case 2:
            chamada.tag_quarta()
        case 3:
            chamada.tag_quinta()
        case 4:
            chamada.tag_sexta()
        case _:
            pass



if __name__ == '__main__':
    main()
