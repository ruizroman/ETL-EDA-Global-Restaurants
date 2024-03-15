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
    


def cities_by_country(df):
    dfaux = df.groupby('country').city.nunique().sort_values(ascending=False).reset_index()
    fig = px.bar(dfaux, x='country', y='city')
    
    # Personalizando Gráfico
    fig = customize_chart(fig, 
                          title_text='Número de Cidades Registradas',
                          x_axis_title=None,
                          y_axis_title='Cidades')
    
    # Personalizando Traces
    fig.update_traces(marker_color='gold',
                      text=dfaux['city'],
                      textposition='inside',
                      insidetextfont=dict(size=18, family='arial black'),
                      textangle=0,
                      hovertemplate='<b>País:</b> %{x}</b><br>' + '<b>Cidades:</b> %{y}'
                     )
    
    return fig


def restaurants_by_country(df):
    dfaux = df.groupby('country').restaurant_id.nunique().sort_values(ascending=False).reset_index()
    fig = px.bar(dfaux, x='country', y='restaurant_id')
    
    # Personalizando Gráfico
    fig = customize_chart(fig, 
                          title_text='Número de Restaurantes Registrados',
                          x_axis_title=None,
                          y_axis_title='Restaurantes')
    
    # Personalizando Traces
    fig.update_traces(marker_color='gold',
                      text=dfaux['restaurant_id'],
                      textposition='inside',
                      insidetextfont=dict(size=18, family='arial black'),
                      textangle=0,
                      hovertemplate='<b>País:</b> %{x}</b><br>' + '<b>Restaurantes:</b> %{y}'
                     )
    
    return fig


def mean_votes_by_country(df):
    dfaux = df.groupby( 'country' ).votes.mean().astype(int).sort_values(ascending=False).reset_index()
    fig = px.bar(dfaux.head(), x='country', y='votes')
    
    # Personalizando Gráfico
    fig = customize_chart(fig, 
                          title_text='Top 5 - Quantidade Média de Avaliações',
                          x_axis_title=None,
                          y_axis_title='Avaliações')
    
    # Personalizando Traces
    fig.update_traces(marker_color='gold',
                      text=dfaux['votes'],
                      textposition='inside',
                      insidetextfont=dict(size=18, family='arial black'),
                      textangle=0,
                      hovertemplate='<b>País:</b> %{x}</b><br>' + '<b>Avaliações:</b> %{y}'
                     )

    
    return fig

def cuisines_by_country(df):
    dfaux = df.groupby( 'country' ).cuisines.nunique().sort_values(ascending=False).reset_index()
    fig = px.bar(dfaux.head(), x='country', y='cuisines')
    
    # Personalizando Gráfico
    fig = customize_chart(fig, 
                          title_text='Top 5 - Diversidade de Cozinhas',
                          x_axis_title=None,
                          y_axis_title='Cozinhas')
    
    # Personalizando Traces
    fig.update_traces(marker_color='gold',
                      text=dfaux['cuisines'],
                      textposition='inside',
                      insidetextfont=dict(size=18, family='arial black'),
                      textangle=0,
                      hovertemplate='<b>País:</b> %{x}</b><br>' + '<b>Cozinhas:</b> %{y}'
                     )


    
    
    return fig




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


st.markdown('<h2 style="text-align: center; font-family: Arial Black;">Visão Mundial </h2>', unsafe_allow_html=True)
st.divider()

with st.container():
    st.plotly_chart(cities_by_country(df), use_container_width=True)

    
st.divider()
with st.container():
    st.plotly_chart(restaurants_by_country(df), use_container_width=True)


    
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(mean_votes_by_country(df), use_container_width=True, height=500) 
    with col2:
        st.plotly_chart(cuisines_by_country(df), use_container_width=True, height=500) 

