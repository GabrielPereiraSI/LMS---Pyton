from periodo import Periodo
from disciplinas import Disciplina

class Periodo_disciplina():
    def __init__(self, sigla, ano, semestre,numero,nome):
        self.sigla_grade = sigla
        self.ano_grade = ano
        self.semestre_grade = semestre
        self.numero_periodo = numero
        self.nome_disciplina = nome