from model.base import Base
from sqlalchemy import Column, Integer, String, DateTime, Float
from datetime import datetime
from typing import Union

class Dados(Base):
    __tablename__ = 'dados'

    id = Column("pk_produto", Integer, primary_key=True)
    nome = Column(String(200), unique=True)
    meta_glicemica_dia = Column(Integer)
    meta_glicemica_noite = Column(Integer)
    fator_sensibilidade = Column(Integer)
    rc_cafe = Column(Integer)
    rc_almoco = Column(Integer)
    rc_lanche = Column(Integer)
    rc_janta = Column(Integer)
    hgt_90 = Column(Integer)
    hgt_70 = Column(Integer)
    glicose = Column(Integer)
    carboidratos = Column(Integer)
    calculo = Column(String(40))
    retorno = Column(Float)
    data = Column(DateTime, default=datetime.now())

    def __init__(self, nome:str, meta_glicemica_dia:int, meta_glicemica_noite:int, fator_sensibilidade:int, rc_cafe:int, rc_almoco:int,
                    rc_lanche:int, rc_janta:int, hgt_90:int, hgt_70:int, glicose:int, carboidratos:int, calculo:str, data:Union[DateTime, None] = None):
        self.nome = nome
        self.meta_glicemica_dia = meta_glicemica_dia
        self.meta_glicemica_noite = meta_glicemica_noite
        self.fator_sensibilidade = fator_sensibilidade
        self.rc_cafe = rc_cafe
        self.rc_almoco = rc_almoco
        self.rc_lanche = rc_lanche
        self.rc_janta = rc_janta
        self.hgt_90 = hgt_90
        self.hgt_70 = hgt_70
        self.glicose = glicose
        self.carboidratos = carboidratos
        self.calculo = calculo
        self.retorno = self.calculando(self.meta_glicemica_dia, self.meta_glicemica_noite, self.fator_sensibilidade, self.rc_cafe, self.rc_almoco,
                                       self.rc_lanche, self.rc_janta, self.hgt_90, self.hgt_70, self.glicose, self.carboidratos, self.calculo)

        """
        Criação de cadastro com dados recebidos
        
        Arguments:
            self.nome: Nome
            meta_glicemica_dia: Meta Glicêmica Dia
            self.meta_glicemica_noite: Meta Glicêmica Noite
            self.fator_sensibilidade: Fator Sensibilidade
            self.rc_cafe: Relação de Carboidratos no Café
            self.rc_almoco: Relação de Carboidratos no Almoço 
            self.rc_lanche: Relação de Carboidratos no Lanche
            self.rc_janta: Relação de Carboidratos no Jantar
            self.hgt_90: HGT 90
            self.hgt_70: HGT 70
            self.glicose: Nível de Glicose Medida
            self.carboidratos: Carboidratos que serão ingeridos
            self.calculo: Escolha do Cálculo
            self.data: Insere a data em que se está sendo utilizado
            self.retorno: Retorna com o resultado do cálculo que foi requisitado
        """

    def calculando(self, meta_glicemica_dia, meta_glicemica_noite, fator_sensibilidade, rc_cafe, rc_almoco, rc_lanche,
                                        rc_janta, hgt_90, hgt_70, glicose, carboidratos, calculo):
        if calculo == 'newCorrecaoDia':
            if glicose > 90:
                return (glicose - meta_glicemica_dia) / fator_sensibilidade
            elif glicose >70:
                return ((glicose - meta_glicemica_dia) / fator_sensibilidade) - hgt_90
            else:
                return ((glicose - meta_glicemica_dia) / fator_sensibilidade) - hgt_70
        elif calculo == 'newCorrecaoNoite':
            if glicose > 90:
                return (glicose - meta_glicemica_noite) / fator_sensibilidade
            elif glicose > 70:
                return ((glicose - meta_glicemica_noite) / fator_sensibilidade) - hgt_90
            else:
                return ((glicose - meta_glicemica_noite) / fator_sensibilidade) - hgt_70
        elif calculo == 'newRcCafe':
            return (carboidratos / rc_cafe)
        elif calculo == 'newRcAlmoco':
            return (carboidratos / rc_almoco)
        elif calculo == 'newRcLanche':
            return (carboidratos / rc_lanche)
        elif calculo == 'newRcJanta':
            return (carboidratos / rc_janta)

        #Formatação para duas casas decimais
        #retorno = round(retorno, 2)

        #Se a glicose estiver muita baixa e o resultado der negativo, retorna 0
        #if retorno < 0:
        #    return 0
        #else:
        #    return retorno
        """
        Realização dos cálculos
        newCorrecaoDia: Cálculo para correção da glicose com base na meta do dia
        newCorrecaoNoite: Cálculo para correção da glicose com base na meta da noite
        newRcCafe: Cálculo de valor para aplicação de glicose com base na quantidade de carboidratos a serem ingeridos no café
        newRcAlmoco: Cálculo de valor para aplicação de glicose com base na quantidade de carboidratos a serem ingeridos no almoço
        newRcLanche: Cálculo de valor para aplicação de glicose com base na quantidade de carboidratos a serem ingeridos no lanche
        newRcJanta: Cálculo de valor para aplicação de glicose com base na quantidade de carboidratos a serem ingeridos no jantar
        """
            