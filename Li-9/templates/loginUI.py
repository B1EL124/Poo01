import streamlit as st
from views import View

class LoginUI:
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        nome = ""
        privilegio = ""
        if st.button("Entrar"):
            c = View.cliente_autenticar(nome, email, senha, privilegio)
            p = View.profissional_autenticar(nome, email, senha)
            if c == None and p == None:
                st.write("E-mail ou senha inválidos")
            else:
                if not c == None:
                    st.session_state["usuario_id"] = c["id"]
                    st.session_state["usuario_email"] = c["email"]
                    st.session_state["usuario_tipo"] = "cliente"
                    st.session_state["usuario_nome"] = c["nome"]
                    st.session_state["usuario_privilegio"] = c["privilegio"]
                else:
                    st.session_state["usuario_id"] = p["id"]
                    st.session_state["usuario_email"] = p["email"]
                    st.session_state["usuario_tipo"] = "profissional"
                    st.session_state["usuario_nome"] = p["nome"]
                st.rerun()