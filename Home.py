import streamlit as st


#==============================================
# Configs
#==============================================
# page colors



st.set_page_config(
    page_title="Fome Zero - Ciência de Dados",
    page_icon="🍽️",
    layout="wide",  # Layout amplo para usar mais espaço horizontal
    initial_sidebar_state="auto"  # Barra lateral inicialmente recolhida (pode ser "auto" ou "expanded")
)

#=============== Configs End ==================
#==============================================

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
st.sidebar.markdown( '---' )


# Bottom
#-------------------------------
st.sidebar.markdown( '---' )
st.sidebar.write('<div style="text-align: right">Powered by RuizRoman</div>', unsafe_allow_html=True)

#=============== Sidebar End ==================
#==============================================


#==============================================
# Main Page
#==============================================

# Título da Página
st.title("Projeto de Ciência de Dados")
st.title("Marketplace - Fome Zero")

# Introdução
st.write("🚀 **Bem-vindo ao Projeto de Ciência de Dados da Fome Zero!** 🍽️")

# Contexto do Problema de Negócio
st.write("**Contexto do Problema de Negócio**")
st.write("Aqui, você é o Cientista de Dados da Fome Zero, o principal marketplace de restaurantes que une famintos e restaurantes locais. Nossa missão é desvendar os segredos escondidos nos dados para orientar as decisões estratégicas e o crescimento da empresa.")

st.write("✨ **O que a Fome Zero faz?**")
st.write("A Fome Zero reúne uma riqueza de informações sobre os restaurantes em sua plataforma. Isso inclui detalhes como endereço, tipo de culinária, disponibilidade de reservas, entregas e avaliações dos clientes. Agora, é sua missão transformar esses dados em conhecimento para responder às perguntas-chave do CEO e impulsionar a empresa.")

# Desafio e Objetivos
st.write("**Desafio e Objetivos**")
st.write("Neste projeto, você será o detetive de dados, respondendo perguntas de negócios críticas e criando visualizações interativas para apresentar suas descobertas. Suas ações moldarão as decisões da Fome Zero, desde a escolha de restaurantes parceiros até a melhoria da experiência do cliente.")

# Aventura de Análise de Dados
st.write("**Aventura de Análise de Dados**")
st.write("Prepare-se para uma emocionante jornada de exploração de dados! Neste painel, você encontrará respostas para as perguntas-chave da Fome Zero, acompanhadas de visualizações interativas que tornarão os dados complexos em insights claros e acionáveis.")

st.write("Estamos ansiosos para compartilhar nossas descobertas com o CEO e ajudar a Fome Zero a se destacar ainda mais no mercado de restaurantes. Vamos começar!")

# Dicas e Guias
st.write("**Dicas e Guias**")
st.write("🔍 **Navegação Fácil**: Use o menu à esquerda para explorar diferentes seções e encontrar respostas para as perguntas de negócios.")
st.write("📧 **Precisa de Ajuda?**: Se tiver dúvidas ou precisar de orientação, não hesite em entrar em contato com nossa equipe de Ciência de Dados.")

# Rodapé
st.write("© 2023 Fome Zero - Todos os direitos reservados")
