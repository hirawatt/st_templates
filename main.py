import streamlit as st
from streamlit import caching
import streamlit.components.v1 as components

# streamlit
st.set_page_config(page_title='App', page_icon=':moneybag:', layout='wide', initial_sidebar_state='expanded')
st.sidebar.title(':shark:' + ' Dashboard')
@st.cache(suppress_st_warning=True)
def footer():
    with st.sidebar.expander("Credits"):
        st.success('Created by VH')
        components.html(
        """
        <script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="hirawat" data-color="#FFDD00" data-emoji="☕"  data-font="Poppins" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>
        """,
        height=100
        )

# credentials
api_key = st.secrets['api_key']
api_secret = st.secrets['api_secret']

# Widget

def main():
    st.write("Code Begins")
    footer()

if __name__ == '__main__':
    main()
