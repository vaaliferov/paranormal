def app():
    
    import os
    import pickle
    import numpy as np
    import pandas as pd
    import streamlit as st
    import lang.diabetes as lng

    st.title(lng.diabetes_diagnosis)

    with st.form(key='input_form'):
        
        fields = (
            st.slider(lng.age, 1, 100, 25, 1),
            st.radio(lng.gender, (lng.male, lng.female)),
            st.checkbox(lng.polyuria),
            st.checkbox(lng.polydipsia),
            st.checkbox(lng.sudden_weight_loss),
            st.checkbox(lng.weakness),
            st.checkbox(lng.polyphagia),
            st.checkbox(lng.genital_thrush),
            st.checkbox(lng.visual_blurring),
            st.checkbox(lng.itching),
            st.checkbox(lng.irritability),
            st.checkbox(lng.delayed_healing),
            st.checkbox(lng.partial_paresis),
            st.checkbox(lng.muscle_stiffness),
            st.checkbox(lng.alopecia),
            st.checkbox(lng.obesity))
     
        submit = st.form_submit_button(label=lng.check)

    if submit:
        data = pd.DataFrame([fields])
        data.replace({lng.male: 1, lng.female: 0}, inplace=True)
        data.replace({True: 1, False: 0}, inplace=True)
        app_path = os.path.dirname(__file__)
        model_path = os.path.join(app_path, 'models', 'diabetes.pkl')
        model = pickle.load(open(model_path,'rb'))
        probas = model.predict_proba(data)[:,1]
        predicted = model.predict(data)
        e = '⚠️' if predicted[0] else '✅'
        p = lng.high_prob if predicted[0] else lng.low_prob
        st.markdown(f'{p} ({probas[0]:.4f}) {e}')
