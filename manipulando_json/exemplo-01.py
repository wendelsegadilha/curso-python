import json
from typing import TypedDict

class Pessoa(TypedDict):
    nome: str
    sobrenome: str
    idade: int
    casado: bool
    profissao: str
    linguagens_trabalho: list[str]
    salario: float

string_json = """
{
    "nome": "Wendel",
    "sobrenome": "Segadilha",
    "idade": 28,
    "casado": true,
    "profissao": "desenvolvedor",
    "linguagens_trabalho": ["Java", "Python", "Javascript"],
    "salario": 2500.00

}
"""

pessoa: Pessoa = json.loads(string_json)
print(pessoa)