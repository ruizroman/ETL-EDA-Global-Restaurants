import streamlit as st
import utils
import pandas as pd
import inflection
from millify import prettify

import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static


#==============================================
# Configs
#==============================================
st.set_page_config(
    page_title="Fome Zero - Ciência de Dados",
    page_icon="🍽️",
    layout="wide",  # Layout amplo para usar mais espaço horizontal
    initial_sidebar_state="auto"  # Barra lateral inicialmente recolhida (pode ser "auto" ou "expanded")
)


#==============================================
# Functions
#==============================================



def world_unique_restaurants(df):
    return df['restaurant_id'].nunique()

def registered_countries(df):
    return df['country_code'].nunique()

def registered_cities(df):
    return df['city'].nunique()

def total_votes(df):
    return df['votes'].sum()

def total_cuisines(df):
    return df['cuisines'].nunique()

def mapa(df):
    cols = ['city', 'cuisines', 'restaurant_name', 'latitude', 'longitude']
    dfaux = df[cols]

    map = folium.Map([-15.7829277,-47.8769482],zoom_start=2.5)

    # Crie um objeto MarkerCluster
    marker_cluster = MarkerCluster().add_to(map)



    # folium.Marker ( [latitude, longitude ) ]
    for i, row in dfaux.iterrows():
        popup_text = f"Cidade: <b>{row.city}</b><br>Cozinha: <b>{row.cuisines}</b><br>Restaurante: <b>{row.restaurant_name}</b>"    
        folium.Marker(
            location=[row.latitude, row.longitude],
            popup=folium.Popup(folium.Html(popup_text, script=True), parse_html=True),
            icon=None
        ).add_to( marker_cluster )
    return map



# Data Extraction and Transformation
df_raw = pd.read_csv( 'data/zomato.csv' )
clean_df = utils.clean_code(df_raw)

#==============================================
# Sidebar
#==============================================

# Logo
#-------------------------------
st.sidebar.image( 'logo1.png' )
st.sidebar.write('<div style="text-align: center; font-size: 20px;">Conectando Culturas</div>', unsafe_allow_html=True)
st.sidebar.write('<div style="text-align: center; font-size: 20px;">Compartilhando Sabores</div>', unsafe_allow_html=True)

# Middle
#-------------------------------
st.sidebar.divider()

countries = st.sidebar.multiselect( ' **Selecione os países que deseja visualizar:** ', options=clean_df.country.unique(), default=clean_df.country.unique() )

df = clean_df.query('country in @countries')

# Bottom
#-------------------------------
st.sidebar.divider()
st.sidebar.write('<div style="text-align: right">Powered by RuizRoman</div>', unsafe_allow_html=True)

#=============== Sidebar End ==================
#==============================================


#==============================================
# Main Page
#==============================================


st.divider()

st.markdown('<h2 style="text-align: center">Conheça a culinária no mundo com o Fome Zero!  </h2>', unsafe_allow_html=True)
with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric( label= ':department_store: Restaurantes', value=prettify( world_unique_restaurants(df) ) )
    with col2:
        st.metric( label= ':earth_asia: Países', value=registered_countries(df) )
    with col3:
        st.metric( label= ':city_sunrise: Cidades', value=registered_cities(df) )
    with col4:
        st.metric( label= ':star: Avaliações', value=prettify( total_votes(df) ) )
    with col5:
        st.metric( label= ':spaghetti: Tipos de Culinária', value=total_cuisines(df) )
    
st.markdown( '---' )

with st.container():
    folium_static( mapa(df), width=1600, height=600 )


    
# Centralizando os elementos metric
css='''
[data-testid="metric-container"] {
    width: fit-content;
    margin: auto;
}

[data-testid="metric-container"] > div {
    width: fit-content;
    margin: auto;
}

[data-testid="metric-container"] label {
    width: fit-content;
    margin: auto;
}
'''
st.markdown(f'<style>{css}</style>',unsafe_allow_html=True)