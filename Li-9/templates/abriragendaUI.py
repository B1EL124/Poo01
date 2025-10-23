from views import View
import streamlit as st
from datetime import datetime,timedelta

class AbrirAgendaUI:
    def main():
            st.header("Abrir Minha Agenda")
            
            datar = st.text_input("Informe a data no formato dd/mm/aaaa", datetime.now().strftime("%d/%m/%Y"))
            hora_ini = st.text_input("Informe o horário incial no formato HH:MM", "09:00")
            hora_fim = st.text_input("Informe o horário final no formato HH:MM", "12:00")
            intervalo = st.text_input("Informe o intervalo entre os horários (min)", "30")

            if st.button("Abrir Agenda"):
                try:
                    data = datetime.strptime(datar, "%d/%m/%Y").date()
                    hora_in = datetime.strptime(hora_ini, "%H:%M").time()
                    hora_fi = datetime.strptime(hora_fim, "%H:%M").time()
                    intervalo_min = int(intervalo)

                    inicio = datetime.combine(data, hora_in)
                    fim = datetime.combine(data, hora_fi)
                    delta = timedelta(minutes = intervalo_min)

                    id_profissional = st.session_state["usuario_id"]

                    while inicio <= fim:
                        View.horario_inserir(inicio, False, None, None, id_profissional)
                        inicio += delta

                    st.success("Agenda aberta com sucesso!")
                except Exception as e:
                    st.error(f"Erro ao abrir agenda: {e}")