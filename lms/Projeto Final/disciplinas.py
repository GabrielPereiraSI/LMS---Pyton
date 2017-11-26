
class Disciplina:

    def __init__(self):
        self.nome = 'programação'
        self.carga_horaria = None
        self.teoria = None
        self.pratica = None
        self.ementa = 'aprender sobre batatas'
        self.competencias = 'desenvolvimento de aplicacões'
        self.habilidades = 'almento de skill'
        self.conteudo = 'batatas'
        self.bibliografia_basica = 'batatinhas'
        self.bibliografia_complementar = 'batatas das batatinhas'

    def altera_nome(self, nome):
        if type(nome) == str:
            self.nome = nome
            return True
        return False

    def retorna_nome(self):
        return self.nome