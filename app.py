from flask_openapi3 import Info, OpenAPI, Tag
from flask_cors import CORS
from flask import redirect
from schemas.dados import DadosViewSchema, DadosSchema, apresenta_dado, ListagemDadosSchema, apresenta_dados, DadosBuscaSchema, DadosDelSchema
from schemas.error import ErrorSchema
from model.dados import Dados
from model.__init__ import Session
from logger import logger
from sqlalchemy.exc import IntegrityError
from urllib.parse import unquote


info = Info(title="Cálculos de Insulina", version="1.0")
app = OpenAPI(__name__, info=info)
CORS(app)

#TAGS
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
dados_tag = Tag(name="Dados", description="Adição, visualização e remoção de Dados de Diabetes Cadastrados à base de dados")

@app.get('/', tags=[dados_tag])
def home():
    """
    Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.post('/dado', tags=[dados_tag], responses={"200":DadosViewSchema, "409":ErrorSchema, "400": ErrorSchema})
def add_dado(form: DadosSchema):
    """
    Adiciona um novo Dado à base de dados
    Retorna uma representação dos dados.
    """
    dados = Dados(
        nome = form.nome,
        meta_glicemica_dia = form.meta_glicemica_dia,
        meta_glicemica_noite = form.meta_glicemica_noite,
        fator_sensibilidade = form.fator_sensibilidade,
        rc_cafe = form.rc_cafe,
        rc_almoco = form.rc_almoco,
        rc_lanche = form.rc_lanche,
        rc_janta = form.rc_janta,
        hgt_90 = form.hgt_90,
        hgt_70 = form.hgt_70,
        glicose = form.glicose,
        carboidratos = form.carboidratos,
        calculo = form.calculo,
    )

    logger.debug(f"Adicionando dados de '{dados.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando produto
        session.add(dados)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado produto de nome: '{dados.nome}'")
        return apresenta_dado(dados), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Não foi possível salvar na base :/"
        logger.warning(f"Erro ao adicionar dados na base '{dados.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar seus dados :/"
        logger.warning(f"Erro ao adicionar os dados '{dados.nome}', {error_msg}")
        return {"mesage": error_msg}, 400

@app.get('/dados', tags=[dados_tag], responses={"200": ListagemDadosSchema, "404": ErrorSchema})
def get_dados():
    """Faz a busca por todos os Dados cadastrados

    Retorna uma representação da listagem cadastrada.
    """
    logger.debug(f"Coletando dados ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    dados = session.query(Dados).all()
    if not dados:
        # se não há produtos cadastrados
        return {"dados": []}, 200
    else:
        logger.debug(f"%d dados encontrados" % len(dados))
        # retorna a representação de produto
        print(dados)
        return apresenta_dados(dados), 200
    
@app.get('/dado', tags=[dados_tag], responses={"200":DadosViewSchema, "404": ErrorSchema})
def get_dado(query: DadosBuscaSchema):
    """
    Faz a busca por um Dado a partir do id do dado

    Retorna uma representação dos dados.
    """
    dado_id = query.id
    logger.debug(f"Coletando dados sobre #{dado_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    dado = session.query(Dados).filter(Dados.id == dado_id)

    if not dado:
        # se o produto não foi encontrado
        error_msg = "Produto não encontrado na base :/"
        logger.warning(f"Erro ao buscar produto '{dado_id}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Produto econtrado: '{dado.nome}'")
        # retorna a representação de produto
        return apresenta_dado(dado), 200
    

@app.delete('/dado', tags=[dados_tag], responses={"200": DadosDelSchema, "404": ErrorSchema})
def del_dado(query: DadosBuscaSchema):
    """Deleta um Dado a partir do nome de dado informado

    Retorna uma mensagem de confirmação da remoção.
    """
    dado_nome = unquote(unquote(query.nome))
    print(dado_nome)
    logger.debug(f"Deletando dados do produto #{dado_nome}")
    session = Session()
    count = session.query(Dados).filter(Dados.nome == dado_nome).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado produto #{dado_nome}")
        return {"mesage": "Dado removido", "id": dado_nome}
    else:
        # se o produto não foi encontrado
        error_msg = "Produto não encontrado na base :/"
        logger.warning(f"Erro ao deletar produto #'{dado_nome}', {error_msg}")
        return {"mesage": error_msg}, 404