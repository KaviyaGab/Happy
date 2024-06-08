import streamlit as st
import pandas as pd
st.title('Happy pred')
infoavail = st.number_input("Enter your infoavail")
housecost = st.number_input("Enter your housecost")
schoolquality = st.number_input("Enter schoolquality")
policetrust = st.number_input("Enter your policetrust")
streetquality = st.number_input("Enter your streetquality")
ëvents = st.number_input("Enter your ëvents")

test = pd.DataFrame({'infoavail':infoavail,
                     'housecost':housecost,
                     'schoolquality':schoolquality,
                     'policetrust':policetrust,
                     'streetquality':streetquality,
                     'ëvents':ëvents},index=[0])

if st.button("submit"):
 import pickle
 model = pickle.load(open("C:\\Users\\Dell\\Downloads\\Happy2.pkl",'rb'))
 st.write(model.predict(test))
