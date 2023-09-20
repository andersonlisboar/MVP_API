from pydantic import BaseModel
from typing import List
from model.dados import Dados


class DadosSchema(BaseModel):
    """
    Define a apresentação dos dados inseridos
    """
    nome: str = "Helena"
    meta_glicemica_dia: int = 100
    meta_glicemica_noite: int = 120
    fator_sensibilidade: int = 80
    rc_cafe: int = 15
    rc_almoco: int = 18 
    rc_lanche: int = 15
    rc_janta: int = 25
    hgt_90: int = 1
    hgt_70: int = 2
    glicose: int = 100
    carboidratos: int = 100
    calculo: str = "correcao_dia"
    #retorno: float = 1.0

class DadosBuscaSchema(BaseModel):
    """ 
    Define como deve ser a estrutura que representa a busca. Que será feita apenas com base no nome do dado cadastrado.
    """
    nome: str = "Helena"
    
class ListagemDadosSchema(BaseModel):
    """
    Define como uma listagem de produtos será retornada.
    """
    dados:List[DadosSchema]

def apresenta_dados(dados: List[Dados]):
    """
    Retorna uma representação do dado cadastrado seguindo o schema definido em DadoViewSchema.
    """
    result = []
    for dado in dados:
        result.append({
            "nome": dado.nome,
            "meta_glicemica_dia": dado.meta_glicemica_dia,
            "meta_glicemica_noite": dado.meta_glicemica_noite,
            "fator_sensibilidade": dado.fator_sensibilidade,
            "rc_cafe": dado.rc_cafe,
            "rc_almoco": dado.rc_almoco,
            "rc_lanche": dado.rc_lanche,
            "rc_janta": dado.rc_janta,
            "hgt_90": dado.hgt_90,
            "hgt_70": dado.hgt_70,
            "glicose": dado.glicose,
            "carboidratos": dado.carboidratos,
            "calculo": dado.calculo,
            "retorno": dado.retorno,
        })
    return {"dados": result}

class DadosViewSchema(BaseModel):
    """
    Define como um dado será retornado.
    """
    nome: str = "Helena"
    meta_glicemica_dia: int = 100
    meta_glicemica_noite: int = 120
    fator_sensibilidade: int = 80
    rc_cafe: int = 15
    rc_almoco: int = 18 
    rc_lanche: int = 15
    rc_janta: int = 25
    hgt_90: int = 1
    hgt_70: int = 2
    glicose: int = 100
    carboidratos: int = 100
    calculo: str = "correcao_dia"
    retorno: float = 1.0

class DadosDelSchema(BaseModel):
    """
    Define como deve ser a estrutura do dado retornado após uma requisição de remoção.
    """
    mesage: str
    nome: str

def apresenta_dado(dado: Dados):
    """
    Retorna uma representação do produto seguindo o schema definido em DadoViewSchema.
    """
    return {
        "nome": dado.nome,
        "meta_glicemica_dia": dado.meta_glicemica_dia,
        "meta_glicemica_noite": dado.meta_glicemica_noite,
        "fator_sensibilidade": dado.fator_sensibilidade,
        "rc_cafe": dado.rc_cafe,
        "rc_almoco": dado.rc_almoco,
        "rc_lanche": dado.rc_lanche,
        "rc_janta": dado.rc_janta,
        "hgt_90": dado.hgt_90,
        "hgt_70": dado.hgt_70,
        "glicose": dado.glicose,
        "carboidratos": dado.carboidratos,
        "calculo": dado.calculo,
        "retorno": dado.retorno,
    }