# Plano de Ação: Dashboard Analítico de Veículos

## 1. Configuração da Integração (Google Sheets)
*   **Google Cloud Console:** Acessar o Google Cloud, criar um projeto e habilitar a **Google Sheets API** e a **Google Drive API**.
*   **Autenticação e Credenciais:** Gerar uma Conta de Serviço (Service Account) e baixar o arquivo JSON contendo as chaves de acesso.
*   **Permissões:** Compartilhar a planilha de dados do Google Sheets com o e-mail da Service Account (nível de acesso: Leitor).
*   **Hospedagem das Imagens:** Assegurar que as URLs contendo as fotos dos modelos dos veículos sejam acessíveis publicamente para o renderizador web.

## 2. Engenharia e Processamento de Dados (Python)
*   **Extração de Dados:** Desenvolver um script Python utilizando a biblioteca `gspread` em conjunto com `google-auth` para estabelecer uma conexão segura e realizar o download dos dados em tempo real.
*   **Tratamento e Modelagem:** Utilizar a biblioteca `pandas` para estruturar os dados. Faremos agregações de quantidade vendida por modelo e garantiremos que o *dataframe* final possua uma coluna dedicada com a URL exata da foto do veículo correspondente.

## 3. Desenvolvimento do Dashboard Profissional
*   **Framework Principal:** Adotar o **Streamlit**, framework líder no mercado Python para o desenvolvimento ágil de interfaces analíticas com design moderno.
*   **Visualização Customizada (Gráfico de Barras com Fotos):**
    *   Como a exibição de fotos vinculadas ao eixo Y de gráficos de barras não é suportada nativamente de forma elegante pela maioria das bibliotecas puras de visualização, aplicaremos uma abordagem híbrida avançada.
    *   Faremos a **Injeção Dinâmica de HTML e CSS customizados** através da função `st.markdown(unsafe_allow_html=True)`. Isso nos permite construir elementos visuais onde a imagem do veículo fica perfeitamente alinhada ao lado de uma barra de progresso customizada (que representará as vendas), garantindo responsividade e aspecto premium.
*   **Design de Interface (Aesthetics):** Focaremos em uma interface premium e minimalista. Utilizaremos paletas de cores modernas, tipografia nítida (ex: Roboto/Inter via importação CSS) e micro-interações no *hover* (passar o mouse) das barras.

## 4. Implantação e Deploy
*   **Controle de Versão:** Versionar a aplicação com Git e armazenar o repositório no GitHub.
*   **Hospedagem:** Fazer o deploy da aplicação no **Streamlit Community Cloud** (ou Azure Web App).
*   **Segurança:** Configurar o arquivo JSON da conta de serviço de forma segura usando o gerenciador de *Secrets* (variáveis de ambiente) do provedor de hospedagem, evitando vazamentos.

---

# Architecture Decision Record (ADR)

## Título: Adoção do Stack Streamlit, Pandas e HTML/CSS Dinâmico para Dashboard de Veículos
**Data:** 14 de Maio de 2026
**Status:** Proposto
**Contexto:**
Existe a necessidade estratégica de visualizar o desempenho das vendas de veículos (por modelo) em um dashboard de dados profissionais. Os dados brutos operacionais residem em uma planilha no Google Sheets e devem ser consumidos e atualizados através de uma conexão via API. O grande diferencial visual solicitado é a exibição de um gráfico de barras clusterizado onde a foto exata de cada modelo do veículo apareça justaposta ou adjacente à sua respectiva barra, exigindo um alto nível de flexibilidade em visualização de dados. A linguagem mandatória do projeto é Python.

**Decisão:**
A arquitetura tecnológica definida será baseada 100% no ecossistema Python, distribuída da seguinte forma:
1.  **Ingestão de Dados:** `Google Sheets API` com a biblioteca `gspread` para estabelecer a conexão servidor a servidor (Service Account).
2.  **Processamento:** `pandas` para a criação do motor de engenharia, encarregado de limpar, transformar e agregar o volume de vendas por veículo.
3.  **Frontend e Camada de Apresentação:** `Streamlit`. Devido à sua velocidade de desenvolvimento e integração fluida.
4.  **Renderização do Gráfico Específico:** Para suprir o requisito rigoroso de colocar fotos dos modelos estritamente ao lado das barras, substituiremos as bibliotecas clássicas de plotagem (como Matplotlib ou Seaborn, que possuem suporte ruim para imagens nos eixos) pela **Geração Dinâmica de Componentes HTML/CSS** diretamente do Python. O motor processará o dataframe e formatará divs flexbox que comportam a imagem do carro e o volume (barra estilizada por CSS), injetando no Streamlit.

**Consequências:**
*   **Positivas:** 
    *   Entrega extremamente rápida de protótipo de dados para produção.
    *   O design não será estrangulado pelas restrições de bibliotecas de gráficos padrão. O uso de CSS customizado garante a "elegância e o nível profissional" exigidos.
    *   Leveza de integração, já que a fonte primária é gerenciada sem servidor de banco de dados extra (Google Sheets atua como banco temporário e fácil para o time de negócios operar).
*   **Riscos e Trade-offs:** 
    *   Gerar HTML a partir de strings no Python pode deixar o código menos legível e dificultar uma manutenção futura se o usuário quiser transformar esse gráfico em algo tridimensional ou com filtros de *drill-down* muito avançados.
    *   As imagens listadas na planilha devem ser preferencialmente armazenadas em CDN ou Drive Público de rápido carregamento, senão a interface pode apresentar lentidão.

**Alternativas Consideradas:**
*   **Plotly nativo no Streamlit:** Avaliamos a funcionalidade `layout.images` do Plotly, porém o posicionamento responsivo nos eixos (para alinhar com cada barra caso os dados cresçam dinamicamente) é frágil e sujeito a quebras em telas de diferentes resoluções.
*   **Power BI/Tableau:** Descartados por desviarem da diretriz de construir o fluxo em linguagem Python e pelas complexidades nativas dessas ferramentas em alinhar dinamicamente recursos web baseados em URLs diretas e dinâmicas nos eixos principais dos visuais.
