from mybaynexx.controle.controle_log import ControleLog as chat  # Biblioteca para encaminhar mensagem no Google Chat 


url_chat = ''


class Tag:
    def __init__(self, planilha):
        self.tag_imp = ''
        self.tag_quarentena = ''
        self.planilha = planilha
        

    def tag_segunda(self):
        self.dia_semana = 'SEGUNDA-FEIRA'
        
        self.tag_imp_08 = self.planilha.iloc[1, 2]
        self.tag_imp_09 = self.planilha.iloc[2, 2]
        self.tag_imp_10 = self.planilha.iloc[3, 2]
        self.tag_imp_11 = self.planilha.iloc[4, 2]
        self.tag_imp_12 = self.planilha.iloc[5, 2]
        self.tag_imp_13 = self.planilha.iloc[6, 2]
        self.tag_imp_14 = self.planilha.iloc[7, 2]
        self.tag_imp_15 = self.planilha.iloc[8, 2]
        self.tag_imp_16 = self.planilha.iloc[9, 2]
        self.tag_imp_17 = self.planilha.iloc[10, 2]
        
        self.tag_quarentena_08 = self.planilha.iloc[1, 3]
        self.tag_quarentena_09 = self.planilha.iloc[2, 3]
        self.tag_quarentena_10 = self.planilha.iloc[3, 3]
        self.tag_quarentena_11 = self.planilha.iloc[4, 3]
        self.tag_quarentena_12 = self.planilha.iloc[5, 3]
        self.tag_quarentena_13 = self.planilha.iloc[6, 3]
        self.tag_quarentena_14 = self.planilha.iloc[7, 3]
        self.tag_quarentena_15 = self.planilha.iloc[8, 3]
        self.tag_quarentena_16 = self.planilha.iloc[9, 3]
        self.tag_quarentena_17 = self.planilha.iloc[10, 3]
        
        self.mensagem(self.dia_semana, self.tag_imp_08, self.tag_imp_09, self.tag_imp_10, self.tag_imp_11, self.tag_imp_12, self.tag_imp_13, self.tag_imp_14, self.tag_imp_15, self.tag_imp_16, self.tag_imp_17, self.tag_quarentena_08, self.tag_quarentena_09, self.tag_quarentena_10, self.tag_quarentena_11, self.tag_quarentena_12, self.tag_quarentena_13, self.tag_quarentena_14, self.tag_quarentena_15, self.tag_quarentena_16, self.tag_quarentena_17)

    
    
    def tag_terca(self):
        self.dia_semana = 'TERÇA-FEIRA'
        
        self.tag_imp_08 = ''
        self.tag_imp_09 = ''
        self.tag_imp_10 = ''
        self.tag_imp_11 = ''
        self.tag_imp_12 = ''
        self.tag_imp_13 = ''
        self.tag_imp_14 = ''
        self.tag_imp_15 = ''
        self.tag_imp_16 = ''
        self.tag_imp_17 = ''
        
        self.tag_quarentena_08 = ''
        self.tag_quarentena_09 = ''
        self.tag_quarentena_10 = ''
        self.tag_quarentena_11 = ''
        self.tag_quarentena_12 = ''
        self.tag_quarentena_13 = ''
        self.tag_quarentena_14 = ''
        self.tag_quarentena_15 = ''
        self.tag_quarentena_16 = ''
        self.tag_quarentena_17 = ''
        
        self.mensagem(self.dia_semana, self.tag_imp_08, self.tag_imp_09, self.tag_imp_10, self.tag_imp_11, self.tag_imp_12, self.tag_imp_13, self.tag_imp_14, self.tag_imp_15, self.tag_imp_16, self.tag_imp_17, self.tag_quarentena_08, self.tag_quarentena_09, self.tag_quarentena_10, self.tag_quarentena_11, self.tag_quarentena_12, self.tag_quarentena_13, self.tag_quarentena_14, self.tag_quarentena_15, self.tag_quarentena_16, self.tag_quarentena_17)


    def tag_quarta(self):
        self.dia_semana = 'QUARTA-FEIRA'
        
        self.tag_imp_08 = ''
        self.tag_imp_09 = ''
        self.tag_imp_10 = ''
        self.tag_imp_11 = ''
        self.tag_imp_12 = ''
        self.tag_imp_13 = ''
        self.tag_imp_14 = ''
        self.tag_imp_15 = ''
        self.tag_imp_16 = ''
        self.tag_imp_17 = ''
        
        self.tag_quarentena_08 = ''
        self.tag_quarentena_09 = ''
        self.tag_quarentena_10 = ''
        self.tag_quarentena_11 = ''
        self.tag_quarentena_12 = ''
        self.tag_quarentena_13 = ''
        self.tag_quarentena_14 = ''
        self.tag_quarentena_15 = ''
        self.tag_quarentena_16 = ''
        self.tag_quarentena_17 = ''
        
        self.mensagem(self.dia_semana, self.tag_imp_08, self.tag_imp_09, self.tag_imp_10, self.tag_imp_11, self.tag_imp_12, self.tag_imp_13, self.tag_imp_14, self.tag_imp_15, self.tag_imp_16, self.tag_imp_17, self.tag_quarentena_08, self.tag_quarentena_09, self.tag_quarentena_10, self.tag_quarentena_11, self.tag_quarentena_12, self.tag_quarentena_13, self.tag_quarentena_14, self.tag_quarentena_15, self.tag_quarentena_16, self.tag_quarentena_17)


    def tag_quinta(self):
        self.dia_semana = 'QUINTA-FEIRA'
        
        self.tag_imp_08 = ''
        self.tag_imp_09 = ''
        self.tag_imp_10 = ''
        self.tag_imp_11 = ''
        self.tag_imp_12 = ''
        self.tag_imp_13 = ''
        self.tag_imp_14 = ''
        self.tag_imp_15 = ''
        self.tag_imp_16 = ''
        self.tag_imp_17 = ''
        
        self.tag_quarentena_08 = ''
        self.tag_quarentena_09 = ''
        self.tag_quarentena_10 = ''
        self.tag_quarentena_11 = ''
        self.tag_quarentena_12 = ''
        self.tag_quarentena_13 = ''
        self.tag_quarentena_14 = ''
        self.tag_quarentena_15 = ''
        self.tag_quarentena_16 = ''
        self.tag_quarentena_17 = ''

        self.mensagem(self.dia_semana, self.tag_imp_08, self.tag_imp_09, self.tag_imp_10, self.tag_imp_11, self.tag_imp_12, self.tag_imp_13, self.tag_imp_14, self.tag_imp_15, self.tag_imp_16, self.tag_imp_17, self.tag_quarentena_08, self.tag_quarentena_09, self.tag_quarentena_10, self.tag_quarentena_11, self.tag_quarentena_12, self.tag_quarentena_13, self.tag_quarentena_14, self.tag_quarentena_15, self.tag_quarentena_16, self.tag_quarentena_17)

    
    def tag_sexta(self):
        self.dia_semana = 'SEXTA-FEIRA'        
        
        self.tag_imp_08 = ''
        self.tag_imp_09 = ''
        self.tag_imp_10 = ''
        self.tag_imp_11 = ''
        self.tag_imp_12 = ''
        self.tag_imp_13 = ''
        self.tag_imp_14 = ''
        self.tag_imp_15 = ''
        self.tag_imp_16 = ''
        self.tag_imp_17 = ''
        
        self.tag_quarentena_08 = ''
        self.tag_quarentena_09 = ''
        self.tag_quarentena_10 = ''
        self.tag_quarentena_11 = ''
        self.tag_quarentena_12 = ''
        self.tag_quarentena_13 = ''
        self.tag_quarentena_14 = ''
        self.tag_quarentena_15 = ''
        self.tag_quarentena_16 = ''
        self.tag_quarentena_17 = ''
        
        self.mensagem(self.dia_semana, self.tag_imp_08, self.tag_imp_09, self.tag_imp_10, self.tag_imp_11, self.tag_imp_12, self.tag_imp_13, self.tag_imp_14, self.tag_imp_15, self.tag_imp_16, self.tag_imp_17, self.tag_quarentena_08, self.tag_quarentena_09, self.tag_quarentena_10, self.tag_quarentena_11, self.tag_quarentena_12, self.tag_quarentena_13, self.tag_quarentena_14, self.tag_quarentena_15, self.tag_quarentena_16, self.tag_quarentena_17)


    def mensagem(self, dia_semana, tag_imp_08, tag_imp_09, tag_imp_10, tag_imp_11, tag_imp_12, tag_imp_13, tag_imp_14, tag_imp_15, tag_imp_16, tag_imp_17, tag_quarentena_08, tag_quarentena_09, tag_quarentena_10, tag_quarentena_11, tag_quarentena_12, tag_quarentena_13, tag_quarentena_14, tag_quarentena_15, tag_quarentena_16, tag_quarentena_17):
        
        msg = f'''
        .......................{dia_semana}
        
        INICIO...TERMINO......................IMPLANTAÇÃO...................QUARENTENA
        
        08:00....09:00..................{tag_imp_08}{"." * (30 - len(tag_imp_08))}{tag_quarentena_08}
        09:00....10:00..................{tag_imp_09}{"." * (30 - len(tag_imp_09))}{tag_quarentena_09}
        10:00....11:00..................{tag_imp_10}{"." * (30 - len(tag_imp_10))}{tag_quarentena_10}
        11:00....12:00..................{tag_imp_11}{"." * (30 - len(tag_imp_11))}{tag_quarentena_11}
        12:00....13:00..................{tag_imp_12}{"." * (30 - len(tag_imp_12))}{tag_quarentena_12}
        13:00....14:00..................{tag_imp_13}{"." * (30 - len(tag_imp_13))}{tag_quarentena_13}
        14:00....15:00..................{tag_imp_14}{"." * (30 - len(tag_imp_14))}{tag_quarentena_14}
        15:00....16:00..................{tag_imp_15}{"." * (30 - len(tag_imp_15))}{tag_quarentena_15}
        16:00....17:00..................{tag_imp_16}{"." * (30 - len(tag_imp_16))}{tag_quarentena_16}
        17:00....18:00..................{tag_imp_17}{"." * (30 - len(tag_imp_17))}{tag_quarentena_17}
        '''
        
        print(msg)
