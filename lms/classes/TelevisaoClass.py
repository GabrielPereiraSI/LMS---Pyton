class Televisao:

    def __init__(self, cmin, cmax, inicio):
        self.ligada = False
        self.canal = inicio
        self.cmin = cmin
        self.cmax = cmax

    def muda_canal(self, c):
        self.canal = c

    def aumenta_canal(self):
        if self.canal == self.cmax:
            self.canal = self.cmin
        else:
            self.canal += 1

    def dimunui_canal(self):
        if self.canal == self.cmin:
            self.canal = self.cmax
        else:
            self.canal -= 1
