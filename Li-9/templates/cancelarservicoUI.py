import streamlit as st
from views import View


class CancelarServiciUI:
    def main():
        st.header("Cancelar Serviço")

        if "usuario_id" not in st.session_state:
            st.error("Nenhum cliente logado.")
            return
        
        id_cliente = st.session_state["usuario_id"]

        horarios = View.horario_filtrar_cliente(id_cliente)

        if len(horarios) == 0:
           st.info("Nenhum serviço a")
