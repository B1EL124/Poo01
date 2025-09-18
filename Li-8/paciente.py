class Paciente:
    def __init__(self, nome, cpf, tel, nas):
        self.__nome = nome
        self.__cpf = cpf
        self.__tel = tel
        self.__nas = nas
    def __str__(self):
        return f"Nome = {self.__nome}\nCpf = {self.__cpf}\nTelefone = {self.__tel}\nNascimento = {self.__nas}"