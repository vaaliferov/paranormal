
def app():

    import streamlit as st
    import lang.about as lng
    st.markdown(lng.description)
    st.image('pics/logo.jpg')
