import streamlit as st
from views import View
import time
from datetime import datetime
class PerfilProfissionalUI:
    def main():
        st.header("Meus Dados")
        op = View.profissional_listar_id(st.session_state["usuario_id"])
        nome = st.text_input("Informe o novo nome", op.get_nome())
        especialidade = st.text_input("Informe a nova especialidade", op.get_especialidade())
        conselho = st.text_input("Informe o novo conselho", op.get_conselho())
        email = st.text_input("Informe o novo e-mail", op.get_email())
        senha = st.text_input("Informe a nova senha", op.get_senha(), type="password")
        if st.button("Atualizar"):
            try:
                id = op.get_id()
                View.profissional_atualizar(id, nome, especialidade, conselho, email, senha)
                st.success("Profissional atualizado com sucesso")
            except ValueError as erro:
                st.error(erro)

    # def main():
    #     st.header("Agendar Serviço")
    #     profs = View.profissional_listar()
    #     if len(profs) == 0:
    #       st.write("Nenhum profissional cadastrado") 
    #     else:
    #         profissional = st.selectbox("Informe o profissional", profs) 
    #         horarios = View.horario_agendar_horario(profissional.get_id())
    #         if len(horarios) == 0: st.write("Nenhum horário disponível")
    #         else:
    #             horario = st.selectbox("Informe o horário", horarios)
    #             servico = st.selectbox("Informe o serviço", servicos)
    #             if st.button("Agendar"):
    #                 View.horario_atualizar(horario.get_id(), horario.get_data(), False, st.session_state["usuario_id"], servico.get_id(), profissional.get_id())
    #                 st.success("Horário agendado com sucesso")
    #                 time.sleep(2)
    #                 st.rerun()