class Circulo:
    def __init__(self):
        self.r = R
        self.pi = 3.14
    def calc_area(self):
        return self.pi * (self.r ** 2)
    def calc_circ(self):
        return 2 * self.pi * self.r
R = float(input())
b = Circulo()
print(b.calc_area())
print(b.calc_circ())