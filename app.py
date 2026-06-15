import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("Fake News Detector for Students")

news = st.text_area("Enter News Article")

if st.button("Check News"):

    transformed = vectorizer.transform([news])

    prediction = model.predict(transformed)

    if prediction[0] == 1:
        st.success("Real News")
    else:
        st.error("Fake News")