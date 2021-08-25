
import streamlit as st
import lang.app as lng
import about, diabetes, melanoma

apps = (
    (lng.about_us, about.app),
    (lng.diabetes, diabetes.app), 
    (lng.melanoma, melanoma.app))

st.sidebar.radio(lng.diagnosis, apps, 0, lambda app: app[0])[1]()
