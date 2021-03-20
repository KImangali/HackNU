import streamlit as st
import pandas as pd

st.title('HackNU')
st.markdown('Hello World')


df = pd.read_csv('data.csv') 
animal = st.sidebar.selectbox('Choose animal',('Numenius arquata', 'Somateria fischeri', 'Clangula hyemalis', 'Anas platyrhynchos'))
st.header(animal)

print(df.info())
st.map(df[df['animal_type'] == animal][['latitude', 'longitude']])