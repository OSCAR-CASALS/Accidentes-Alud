import streamlit as st
import pandas as pd
from src.functions import create_map
import folium

# Page title
st.set_page_config(page_title="Accidentes Alud")

# Tile
st.title("Accidentes Alud")

# Loading data
#data_load_state = st.text('Loading data...')

DF = pd.read_csv('data/Alud_accidents.csv', sep = ',')
DF.drop(columns=DF.columns[0], axis=1, inplace=True)
DF.drop(columns="Mida", axis=1, inplace=True)
DF.dropna(subset=["lat", "long"], inplace=True)

DF.rename(columns={'Grau_Perill' : 'Grado de Peligro', 'Arrossegats' : 'Arrastrados', 'Ferits' : 'Heridos', 'Morts' : 'Muertos'}, inplace=True)

#data_load_state.text('Loading data...done!')

#######################################################
# Map
#######################################################

ColorBy = st.selectbox("Colorea por:", ['Grado de Peligro',
                              'Arrastrados', 
                              'Heridos', 
                              'Muertos'], index=0)

st.subheader("Mapa Aludes")
m = create_map(DF, ColorBy)
st.components.v1.html(folium.Figure().add_child(m).render(), height=500)

#st.subheader('Raw data')
#st.write(DF)