import pandas as pd
import inflection


def clean_code(df):

    # Removendo Colunas com apenas 1 valor unico.
    drop_col = [ col for col in df.nunique().index if df.nunique()[col] == 1 ]
    df = df.drop( drop_col, axis=1 )
    
    # Remove linhas com valores faltantes
    df = df.dropna( how='any', axis= 0 )
    
    # Renomear as colunas do DataFrame
    def rename_columns(dataframe):
        df = dataframe.copy()
        title = lambda x: inflection.titleize(x)
        snakecase = lambda x: inflection.underscore(x)
        spaces = lambda x: x.replace(" ", "")
        cols_old = list(df.columns)
        cols_old = list(map(title, cols_old))
        cols_old = list(map(spaces, cols_old))
        cols_new = list(map(snakecase, cols_old))
        df.columns = cols_new
        return df
    
    # Renomeia as colunas
    df = rename_columns( df )
    
    # Preenchimento do nome dos países
    COUNTRIES = {
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zeland",
    162: "Philippines",
    166: "Qatar",
    184: "Singapure",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "United Arab Emirates",
    215: "England",
    216: "United States of America",
    }
    def country_name(country_id):
        return COUNTRIES[country_id]
    
    
    
    # cria coluna com nome do país
    df.insert( 3, 'country', df['country_code'].apply( country_name ) )
    
    # Criação do Tipo de Categoria de Comida
    
    def create_price_type(price_range):
        if price_range == 1:
            return "cheap"
        elif price_range == 2:
            return "normal"
        elif price_range == 3:
            return "expensive"
        else:
            return "gourmet"
    
    # cria coluna com categoria de preço
    df.insert( 17 , 'price_type', df['price_range'].apply( create_price_type ) )
    
    # Criação do nome das Cores
    COLORS = {
    "3F7E00": "darkgreen",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "orange",
    "FFBA00": "red",
    "CBCBC8": "darkred",
    "FF7800": "darkred",
    }
    
    def color_name(color_code):
        return COLORS[color_code]
    
    #cria coluna com nome da cores
    df.insert( 19 , 'color', df['rating_color'].apply( color_name ) )
    
    
    # categoriza restaurantes por apenas 1 tipo de cozinha
    df["cuisines"] = df.loc[:, "cuisines"].apply(lambda x: x.split(",")[0])
    
    
    # Remove linhas duplicadas
    df.drop_duplicates(keep='first', inplace=True)
    
    
    # Remove linhas com valores zerados
    df.drop( df[ df['average_cost_for_two'] == 0 ].index , axis=0, inplace=True )
    df.drop( df[ df['votes'] == 0 ].index , axis=0, inplace=True )
    
    # Remove 1 linha com valor inconsistente 
    df.drop( df[ df.average_cost_for_two == df.average_cost_for_two.max() ].index, inplace=True )
    
    return df

