from datetime import datetime
from models.horario import Horario, HorarioDAO
from models.cliente import Cliente, ClienteDAO
from models.profissional import Profissional, ProfissionalDAO
from models.servico import Servico, ServicoDAO

class View:
    def cliente_criar_admin():
        for c in View.cliente_listar():
            if c.get_email() == "admin":
                return c.get_id()
        View.cliente_inserir("admin", "admin", "fone", "1234", "1", isadmin=True)

    def cliente_autenticar(nome, email, senha, privilegio):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "email": c.get_email(), "nome": c.get_nome(), "privilegio": c.get_privilegio()}
        return None

    def cliente_listar():
        r = ClienteDAO.listar()
        r.sort(key = lambda obj : obj.get_nome())
        return r
    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)
    
    def cliente_inserir(nome, email, fone, senha, privilegio, isadmin=False):
        if not isadmin:
            if email == "admin":
                raise ValueError("Inválido")
        for c in View.cliente_listar() + View.profissional_listar():
            if c.get_email() == email:
                raise ValueError("Email já usado")
        
        cliente = Cliente(0, nome, email, fone, senha, privilegio)
        ClienteDAO.inserir(cliente)
        
    def cliente_atualizar(id, nome, email, fone, senha, privilegio, isadmin=False):
        if not isadmin:
            if email == "admin":
                raise ValueError("Invalido")
        for c in View.cliente_listar() + View.profissional_listar():
            if c.get_email() == email:
                raise ValueError("Email já usado")
            
        cliente = Cliente(id, nome, email, fone, senha, privilegio)
        ClienteDAO.atualizar(cliente)

    def cliente_atualizar(id, nome, email, fone, senha, privilegio, isadmin=True):
        if not isadmin:
            if email == "admin":
                raise ValueError("Invalido")
        for c in View.cliente_listar() + View.profissional_listar():
            if c.get_email().lower() == email.lower() and c.get_id() != id:
                raise ValueError("Email já usado")
            
        cliente = Cliente(id, nome, email, fone, senha, privilegio)
        ClienteDAO.atualizar(cliente)

    def cliente_excluir(id):
        for h in View.horario_listar():
            if h.get_id_cliente() == id:
                raise ValueError("Não é possível remover clientes com horários marcados")

        cliente = Cliente(id, "_", "_", "_", "_", "_")
        ClienteDAO.excluir(cliente)

    def servico_listar():
        r = ServicoDAO.listar()
        r.sort(key = lambda obj : obj.get_descricao())
        return r
    
    def servico_listar_id(id):
        return ServicoDAO.listar_id(id)
    
    def servico_inserir(descricao, valor):
        for obj in View.servico_listar():
            if obj.get_descricao() == descricao:
                raise ValueError("Serviço já cadastrado")
        c = Servico(0, descricao, valor)
        ServicoDAO.inserir(c)

    def servico_atualizar(id, descricao, valor):
        for obj in View.servico_listar():
            if obj.get_id() != id and obj.get_descricao() == descricao:
                raise ValueError("Descriçao já cadastrada em outro serviço")
        c = Servico(id, descricao, valor)
        ServicoDAO.atualizar(c)

    def servico_excluir(id):
        for obj in View.horario_listar():
            if obj.get_id_servico() == id:
                raise ValueError("Serviço já agendado: não é possível excluir")
            
        c = Servico(id, "sem descrição", 0)
        ServicoDAO.excluir(c)
    
    def profissional_autenticar(nome, email, senha):
        for p in View.profissional_listar():
            if p.get_email() == email and p.get_senha() == senha:
                return{"id": p.get_id(), "email": p.get_email(), "nome": p.get_nome()}
        return None

    def profissional_listar():
        r = ProfissionalDAO.listar()
        r.sort(key = lambda obj : obj.get_nome())
        return r
    def profissional_listar_id(id):
        return ProfissionalDAO.listar_id(id)
    def profissional_inserir(nome, especialidade, conselho, email, senha):
        if email == "admin":
            raise ValueError
        for c in View.cliente_listar() + View.profissional_listar():
            if c.get_email() == email:
                raise ValueError("Email já usado")
        profissional = Profissional(0, nome, especialidade, conselho, email, senha)
        ProfissionalDAO.inserir(profissional)

    def profissional_atualizar(id, nome, especialidade, conselho, email, senha):
        if email == "admin":
            raise ValueError
        for c in View.cliente_listar() + View.profissional_listar():
            if c.get_email() == email and c.get_id() != id:
                raise ValueError("Email já usado")
        profissional = Profissional(id, nome, especialidade, conselho, email, senha)
        ProfissionalDAO.atualizar(profissional)

    def profissional_excluir(id):
        for h in View.horario_listar():
            if h.get_id_profissional() == id:
                raise ValueError("Não é possível remover profissionais com horários agendados")

        profissional = Profissional(id, "_", "_", "_", "_", "_")
        ProfissionalDAO.excluir(profissional)

    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        for obj in View.horario_listar():
            if obj.get_data() == data and obj.get_id_profissional() == id_profissional:
                raise ValueError("Serviço já agendado com esse profissional para essa hora")
        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        HorarioDAO.inserir(c)

    def horario_listar_id(id_hoario):
        return HorarioDAO.listar_id(id_hoario)

    def horario_listar():
        r = HorarioDAO.listar()
        r.sort(key = lambda obj : obj.get_data())
        return r

    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
        for obj in View.horario_listar():
            if obj.get_data() == data and obj.get_id_profissional() == id_profissional and not obj.get_id() == id:
                raise ValueError("Serviço já agendado com esse profissional para essa hora")
            
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        HorarioDAO.atualizar(c)

    def horario_filtrar_cliente(id_cliente):
        r = []
        agora = datetime.now()
        for h in View.horario_listar():
            if h.get_data() >= agora and h.get_id_cliente() == id_cliente:
                r.append(h)
        r.sort(key = lambda h : h.get_data())
        return r

    def horario_filtrar_profissional(id_profissional):
        r = []
        agora = datetime.now()
        for h in View.horario_listar():
            print(h.get_data(), type(h.get_data()), agora)
            if h.get_data() >= agora and h.get_confirmado() == False and h.get_id_profissional() == id_profissional:
                r.append(h)
        r.sort(key = lambda h : h.get_data())
        return r

    def horario_agendar_horario(id_profissional):
        r = []
        agora = datetime.now()
        for h in View.horario_listar():
            if h.get_data() >= agora and h.get_confirmado() == False and h.get_id_cliente() == None and h.get_id_profissional() == id_profissional:
                r.append(h)
        r.sort(key = lambda h : h.get_data())
        return r

    def horario_excluir(id):
        obj = View.horario_listar_id(id)
        if obj.get_confirmado() == True:
            raise ValueError("Horário já está agendado")
        
        c = Horario(id, None)
        HorarioDAO.excluir(c)