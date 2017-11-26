from TelevisaoClass import Televisao

t1 = Televisao(1, 50)
print(t1.canal)

t1.aumenta_canal()
print(t1.canal)

t1.muda_canal(10)

tv_sala = Televisao(2, 10)
tv_sala.ligada = True
tv_sala.canal = 4

print(tv_sala.canal)
print(tv_sala.ligada)
