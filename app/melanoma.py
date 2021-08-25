
def app():

    import onnxruntime
    import numpy as np
    import pandas as pd
    from PIL import Image
    from PIL import ImageOps
    import streamlit as st
    import lang.melanoma as lng

    max_age = 90

    genders = (
        lng.male,
        lng.female)

    sites = (
        lng.anterior_torso,
        lng.head_neck,
        lng.lateral_torso,
        lng.lower_extremity,
        lng.oral_genital,
        lng.palms_soles,
        lng.posterior_torso,
        lng.torso,
        lng.upper_extremity,
        lng.nan)

    def pad(im):
        w, h = im.size; m = np.max([w, h])
        hp, hpr = (m - w) // 2, (m - w) % 2
        vp, vpr = (m - h) // 2, (m - h) % 2
        return (hp + hpr, vp + vpr, hp, vp)

    def norm(x):
        mean = np.array([0.485, 0.456, 0.406])
        std = np.array([0.229, 0.224, 0.225])
        return (x - mean) / std

    def load_image(file, size):
        im = Image.open(file)
        im.thumbnail((size, size), Image.ANTIALIAS)
        im = ImageOps.expand(im, pad(im))
        x = np.array(im) / 255.
        x = np.float32(norm(x))
        x = x.transpose(2,0,1)
        return x.reshape((1,) + x.shape)

    def get_meta_features(sex, age, site, sites, max_age):
        age = age / max_age
        sex = {lng.male:1,lng.female:0,lng.nan:-1}[sex]
        m = [sex, age] + [int(s == site) for s in sites]
        m = np.array(m, dtype=np.float32)
        return m.reshape((1,) + m.shape)

    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    def predict(model, sex, age, site, image):
        x = load_image(image, 256)
        meta = get_meta_features(sex, age, site, sites, max_age)
        outs = model.run(None, {'x': x, 'meta': meta})
        y = sigmoid(outs[0])[0][0]
        return int(y > 0.5), y

    st.title(lng.melanoma_diagnosis)

    if 'model' not in st.session_state:
        st.session_state.model = onnxruntime.InferenceSession('models/melanoma.onnx')

    with st.form(key='melanoma_input_form'):
        age = st.slider(lng.age, 0, 90, 25, 5)
        sex = st.radio(lng.gender, genders)
        site = st.radio(lng.site, sites)
        image = st.file_uploader('photo', type='jpg')
        submit = st.form_submit_button(label=lng.check)

    if submit and image is not None:
        im = Image.open(image)
        st.image(im, width=200)
        st.write(predict(st.session_state.model, sex, age, site, image))
