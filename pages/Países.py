import streamlit as st
import utils
import pandas as pd
import inflection
from millify import prettify

import plotly.express as px
import plotly.graph_objects as go



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
def customize_chart(fig, title_text=None, x_axis_title=None, y_axis_title=None):
    
    # Personalizando o Layout
    fig.update_layout(title={
        'text': title_text,
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
                      title_font_size=25,
                      title_font_family='Trebuchet MS'
                     )
    
    # Personalizando Eixo X
    fig.update_xaxes(showgrid=False,
                     ticks='outside',
                     title_text=x_axis_title,
                     title_font_family='Trebuchet MS',
                     title_font_size=20,
                     tickfont_size=20
                    )
    
    # Personalizando Eixo Y
    fig.update_yaxes(showgrid=False,
                     ticks='outside',
                     title_text=y_axis_title,
                     title_font_family='Trebuchet MS',
                     title_font_size=20,
                     tickfont_size=20
                    )
    
    
    
    return fig
    


def valor_medio_prato_para_dois(df):
    return f"$ { int(df.groupby( ['currency'] ).average_cost_for_two.mean().iloc[0]) }"

def quantidade_tipos_de_cozinha(df):
    return df.cuisines.nunique()

def quantidade_cidades_registradas(df):
    return df['city'].nunique()

def quantidade_restaurantes_registrados(df):
    return df['restaurant_id'].nunique()

def melhor_restaurante(df, rank=0):
    dfaux = df[ ['restaurant_id', 'restaurant_name', 'cuisines', 'aggregate_rating'] ].sort_values(by=['aggregate_rating', 'restaurant_id'], ascending=[False, True])
    restaurant_name= dfaux.restaurant_name.iloc[rank]
    restaurant_rating= dfaux.aggregate_rating.iloc[rank]
    return [restaurant_name, restaurant_rating]


def pior_restaurante(df, rank=0):
    dfaux = df[ ['restaurant_id', 'restaurant_name', 'cuisines', 'aggregate_rating'] ].sort_values(by=['aggregate_rating', 'restaurant_id'], ascending=[True, True])
    restaurant_name= dfaux.restaurant_name.iloc[rank]
    restaurant_rating= dfaux.aggregate_rating.iloc[rank]
    return [restaurant_name, restaurant_rating]




# Data Extraction and Transformation
df_raw = pd.read_csv( 'data/zomato.csv' )
clean_df = utils.clean_code(df_raw)

#==============================================
# Sidebar
#==============================================
st.markdown(
    """
    <style>
    /* CSS to change selectbox font size */
    .sidebar .stSelectbox select {
        font-size: 50px !important; /* Adjust the font size as needed */
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Logo
#-------------------------------
st.sidebar.image( 'logo1.png' )
st.sidebar.write('<div style="text-align: center; font-size: 20px;">Conectando Culturas</div>', unsafe_allow_html=True)
st.sidebar.write('<div style="text-align: center; font-size: 20px;">Compartilhando Sabores</div>', unsafe_allow_html=True)

st.sidebar.markdown(
    """
    <style>
    /* CSS to change font size */
    .sidebar-content {
        font-size: 20px; /* Adjust the font size as needed */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Middle
#-------------------------------
st.sidebar.divider()

st.sidebar.write('<div style="text-align: center; font-size: 20px;">Selecione o país que deseja visualizar</div>', unsafe_allow_html=True)
countries = st.sidebar.selectbox( ' **Selecione o país que deseja visualizar:** ', options=clean_df.country.unique(), index=1, label_visibility='hidden')
df = clean_df.query('country in @countries')

st.sidebar.write('<div style="text-align: center; font-size: 20px;">Selecione o tipo de Cozinha</div>', unsafe_allow_html=True)
cuisines = st.sidebar.selectbox( ' **Selecione o tipo de cozinha:** ', options=df.cuisines.unique(), index=1, label_visibility='hidden')
df1 = df.query('cuisines in @cuisines')

# Bottom
#-------------------------------
st.sidebar.divider()
st.sidebar.write('<div style="text-align: right">Powered by RuizRoman</div>', unsafe_allow_html=True)

#=============== Sidebar End ==================
#==============================================


#==============================================
# Main Page
#==============================================

with st.container():
    st.markdown('<h3 style="text-align: center; color:gold ; font-family: Arial Black;">Dados Gerais do País </h3><br><br>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)

    col1.metric( label='Preço Médio de Pratos Para 2', value=( valor_medio_prato_para_dois(df)), label_visibility="visible" )
    col2.metric( label='Tipos de Cozinhas', value=quantidade_tipos_de_cozinha(df), label_visibility="visible" )
    col3.metric( label='Quantidade de Cidades', value= quantidade_cidades_registradas(df), label_visibility="visible" )
    col4.metric( label='Quantidade de Restaurantes', value= quantidade_restaurantes_registrados(df), label_visibility="visible" )
    

    
st.divider()
with st.container():
    st.markdown('<h3 style="text-align: center; color:gold ; font-family: Arial Black;">Melhores Restaurantes <br></h3>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    #Coluna 1
    col1.markdown('<h3 style="text-align: center ; color:gold ; font-family: Arial Black;">🥇 <br></h3>', unsafe_allow_html=True)
    col1.metric( label=melhor_restaurante(df1)[0], value=melhor_restaurante(df1)[1], label_visibility="visible" )
    
    #Coluna 2
    col2.markdown('<h3 style="text-align: center ; color:silver ; font-family: Arial Black;">🥈 <br></h3>', unsafe_allow_html=True)
    try:
        col2.metric( label=melhor_restaurante(df1, rank=1)[0], value=melhor_restaurante(df1, rank=1)[1], label_visibility="visible"  )
    except:
        col2.write("---")
    
    #Coluna 3     
    col3.markdown('<h3 style="text-align: center ; color:darkorange ; font-family: Arial Black;">🥉 <br></h3>', unsafe_allow_html=True)
    try:
        col3.metric( label=melhor_restaurante(df1, rank=2)[0], value=melhor_restaurante(df1, rank=2)[1], label_visibility="visible"  )
    except:
        col3.write("---")
        
    st.divider()

with st.container():
    st.markdown('<h3 style="text-align: center; color:gold ; font-family: Arial Black;">Piores Restaurantes <br><br></h3>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    #Coluna 1
    col1.markdown('<h3 style="text-align: center ; color:gold ; font-family: Arial Black;">⛔⛔⛔ <br></h3>', unsafe_allow_html=True)
    col1.metric( label=pior_restaurante(df1)[0], value=pior_restaurante(df1)[1], label_visibility="visible" )
    
    #Coluna 2
    col2.markdown('<h3 style="text-align: center ; color:silver ; font-family: Arial Black;">⛔⛔ <br></h3>', unsafe_allow_html=True)
    try:
        col2.metric( label=pior_restaurante(df1, rank=1)[0], value=pior_restaurante(df1, rank=1)[1], label_visibility="visible"  )
    except:
        col2.write("---")
    
    #Coluna 3     
    col3.markdown('<h3 style="text-align: center ; color:red ; font-family: Arial Black;">⛔ <br></h3>', unsafe_allow_html=True)
    try:
        col3.metric( label=pior_restaurante(df1, rank=2)[0], value=pior_restaurante(df1, rank=2)[1], label_visibility="visible"  )
    except:
        col3.write("---")
        
    st.divider()

        
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