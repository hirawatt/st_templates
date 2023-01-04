import streamlit as st
import streamlit.components.v1 as components

# credentials
page_title = st.secrets['initialize']['page_title']
website = st.secrets['credits']['website']
name = st.secrets['credits']['name']
buymeacoffee = st.secrets['credits']['buymeacoffee']
api_key = st.secrets['api_key']
api_secret = st.secrets['api_secret']

# streamlit
st.set_page_config(
    page_title='{}'.format(page_title),
    page_icon=':moneybag:',
    layout='wide',
    initial_sidebar_state='expanded'
)
st.title(':shark:' + ' Dashboard')
st.sidebar.title(':smile' + ' Sidebar')

# footer & credits section
@st.cache(suppress_st_warning=True)
def footer():
    st.markdown('<div style="text-align: center">Made with ❤️ by <a href="{}">{}</a></div>'.format(website, name), unsafe_allow_html=True)
    with st.sidebar.expander("Credits", expanded=True):
        components.html(
            '{}'.format(buymeacoffee),
            height=80
        )



# widget

def main():
    st.write("Code Begins")
    footer()

if __name__ == '__main__':
    main()
