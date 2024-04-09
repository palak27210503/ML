import streamlit as st
import joblib
model=joblib.load('penguin')
joblib.dump(model,'penguin')
st.title('Penguin Species')
island=st.number_input('Enter island number',min_value=0,max_value=2,value=1)
if st.button("Predict Species"):
    input=[[island]]
    result=model.predict(input)[0]
    st.write("The recommended penguin species is",result)