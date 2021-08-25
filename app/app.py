
import streamlit as st
import lang.app as lng
import about, diabetes, melanoma

apps = (
    (lng.about_us, about.app),
    (lng.diabetes, diabetes.app), 
    (lng.melanoma, melanoma.app))


# st.sidebar.image('pics/paranormal.jpg')
st.sidebar.markdown('### 👻 Paranormal \n 🤳 Self-Screening')
st.sidebar.radio('', apps, 0, lambda app: app[0])[1]()
