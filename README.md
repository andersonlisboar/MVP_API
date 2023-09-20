# API para Cálculos de Unidades de Insulina

Este é o FRONT END da entrega do MVP da Sprint 1 da Disciplina **Desenvolvimento Full Stack Básico**

O objetivo é que o usuário insira os dados fornecidos por um médico e tenha como retorno o cálculo com as unidades de insulinas necessárias.

O usuário inserindo os dados passados pelo médico, a API retorna o valor de unidades de insulina necessária.

Estão dispóníveis 5 tipos de cálculos:
    - Correção Dia:  Utilizado para retornar o valor de unidades necessárias para correção da glicose
    - Correção Noite:  Utilizado para retornar o valor de unidades necessárias para correção da glicose
    - RC Café: Relação de Carboidratos no Café - Retorna o valor de unidades a serem realizadas com base na quantidade de carboidratos que serão ingeridos
    - RC Almoço: Relação de Carboidratos no Almoço - Retorna o valor de unidades a serem realizadas com base na quantidade de carboidratos que serão ingeridos
    - RC Lanche: Relação de Carboidratos no Lanche - Retorna o valor de unidades a serem realizadas com base na quantidade de carboidratos que serão ingeridos
    - RC Janta: Relação de Carboidratos na Janta - Retorna o valor de unidades a serem realizadas com base na quantidade de carboidratos que serão ingeridos

---
## Como executar 

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
