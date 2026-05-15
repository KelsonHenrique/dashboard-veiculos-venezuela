import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# Configuração da página
st.set_page_config(page_title="Dashboard de Vendas de Veículos", layout="wide", initial_sidebar_state="collapsed")

# CSS Customizado para aparência elegante e o gráfico de barras
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

    /* Ocultar menu do streamlit e rodapé */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Fundo e tipografia premium */
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
        font-family: 'Inter', sans-serif;
    }
    
    .title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #FFFFFF;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        font-size: 1.1rem;
        color: #A0AEC0;
        margin-bottom: 2rem;
    }
    
    /* Container do gráfico customizado */
    .chart-container {
        display: flex;
        flex-direction: column;
        gap: 1.5rem;
        margin-top: 2rem;
    }
    
    /* Linha do veículo */
    .vehicle-row {
        display: flex;
        align-items: center;
        background-color: #1A202C;
        border-radius: 12px;
        padding: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .vehicle-row:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
    }
    
    /* Imagem do carro - Enquadramento aprimorado */
    .vehicle-img {
        width: 180px;
        height: 101px; /* Proporção 16:9 aproximada */
        object-fit: cover;
        object-position: center center;
        border-radius: 8px;
        border: 1px solid #2D3748;
        margin-right: 1.5rem;
        background-color: #1A202C;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    
    /* Detalhes e Barra */
    .vehicle-details {
        flex-grow: 1;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    .vehicle-header {
        display: flex;
        justify-content: space-between;
        margin-bottom: 0.5rem;
    }
    
    .vehicle-name {
        font-size: 1.2rem;
        font-weight: 600;
        color: #E2E8F0;
    }
    
    .vehicle-category {
        font-size: 0.9rem;
        font-weight: 400;
        color: #718096;
        margin-left: 0.5rem;
    }
    
    .vehicle-rank {
        color: #4FD1C5;
        font-weight: 800;
        font-size: 1.3rem;
        margin-right: 0.4rem;
    }
    
    .vehicle-sales {
        font-size: 1.2rem;
        font-weight: 700;
        color: #38B2AC;
    }
    
    /* Barra de progresso customizada (representando o gráfico de barras) */
    .bar-bg {
        width: 100%;
        height: 12px;
        background-color: #2D3748;
        border-radius: 6px;
        overflow: hidden;
    }
    
    .bar-fill {
        height: 100%;
        background: linear-gradient(90deg, #319795 0%, #4FD1C5 100%);
        border-radius: 6px;
        transition: width 1s ease-in-out;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">Performance de Vendas</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Top 10 Veículos - Mercado Venezuela</div>', unsafe_allow_html=True)

# Função para conectar ao Google Sheets e carregar os dados
@st.cache_data(ttl=300) # Cache de 5 minutos para performance
def load_data():
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = Credentials.from_service_account_file("credenciais.json", scopes=scopes)
    client = gspread.authorize(creds)
    
    # Acessar a planilha e aba corretas
    sheet = client.open("TOP10_VEICULOS_VEN").worksheet("Página1")
    
    # Baixar todos os dados e converter para DataFrame
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    
    # Tratamento básico
    df['quantidade'] = pd.to_numeric(df['quantidade'], errors='coerce').fillna(0)
    df = df.sort_values(by='quantidade', ascending=False).head(10).reset_index(drop=True)
    
    return df

try:
    with st.spinner('Conectando ao Google Sheets e baixando dados...'):
        df = load_data()
        
    if df.empty:
        st.warning("A planilha foi lida com sucesso, mas parece estar vazia.")
    else:
        # Lógica para o gráfico de barras clusterizado customizado
        max_vendas = df['quantidade'].max()

        html_content = '<div class="chart-container">'

        for index, row in df.iterrows():
            # Calcula a porcentagem da barra em relação ao valor máximo para manter proporção
            bar_width = (row['quantidade'] / max_vendas) * 100 if max_vendas > 0 else 0
            
            # Tenta pegar a URL da coluna foto. Se estiver vazia, tenta pegar de imagem
            img_url = row.get('foto', '')
            if pd.isna(img_url) or str(img_url).strip() == '':
                img_url = row.get('imagem', '')
                
            categoria_html = f'<span class="vehicle-category">({row.get("Categoria", "")})</span>' if "Categoria" in df.columns else ''
            
            html_content += f"""
<div class="vehicle-row">
    <img src="{img_url}" alt="{row.get('modelo', 'Veículo')}" class="vehicle-img" onerror="this.src='https://via.placeholder.com/180x101.png?text=Sem+Foto'">
    <div class="vehicle-details">
        <div class="vehicle-header">
            <span class="vehicle-name"><span class="vehicle-rank">#{index + 1}</span> {row.get('modelo', 'Modelo Desconhecido')} {categoria_html}</span>
            <span class="vehicle-sales">{int(row['quantidade']):,} uni.</span>
        </div>
        <div class="bar-bg">
            <div class="bar-fill" style="width: {bar_width}%;"></div>
        </div>
    </div>
</div>
"""

        html_content += '</div>'

        # Renderiza o gráfico customizado
        st.markdown(html_content, unsafe_allow_html=True)
        
except FileNotFoundError:
    st.error("⚠️ O arquivo 'credenciais.json' não foi encontrado na pasta. Por favor, certifique-se de que ele está salvo no mesmo diretório do script.")
except Exception as e:
    st.error(f"⚠️ Erro ao se conectar ao Google Sheets: {e}")
    st.info("Verifique se o e-mail da Conta de Serviço foi compartilhado na planilha como Leitor e se o nome da planilha está exatamente igual: 'TOP10_VEICULOS_VEN'")

st.markdown("<br><br>", unsafe_allow_html=True)
st.success("✅ Integração com Google Sheets ativa. Dados sincronizados em tempo real.")
