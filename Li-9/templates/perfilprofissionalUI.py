import streamlit as st
from views import View
import time
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
            id = op.get_id()
            View.profissional_atualizar(id, nome, especialidade, conselho, email, senha)
            st.success("Profissional atualizado com sucesso")
    # def abrir_agenda():
    #     st.header("Abrir Minha Agenda")
    #     data = st.text_input("Informe a data no formato dd/mm/aaaa", op.get_data())
    #     hora_ini = st.text_input("Informe o horário incial no formato HH:MM", op.get_hora_ini())
    #     hora_fim = st.text_input("Informe o horário final no formato HH:MM", op.get_hora_fim())
    #     intervalo = st.text_input("Informe o intervalo entre os horários (min)", op.get_intervalo())