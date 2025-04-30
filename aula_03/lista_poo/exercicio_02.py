d = float(input("Distância: "))
h = float(input("Horas: "))
m = float(input("Minutos: "))

class Viagem:
    def __init__ (self):
        self.d = d
        self.h = h
        self.m = m / 60
    def  calc_vm(self):
        return self.d / (self.h + self.m)

vm = Viagem()
print(f"{vm.calc_vm():.2f}")