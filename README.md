# Dashboard de Vendas de Veículos (Venezuela) 🚗📊

Este projeto consiste em um dashboard analítico focado no acompanhamento de vendas de veículos do mercado venezuelano. Ele consome dados **em tempo real** de uma planilha do Google Sheets através de integração via API e apresenta as informações de forma visualmente elegante, focando na usabilidade executiva.

## 🌟 Funcionalidades Principais
* **Integração em Tempo Real:** Conexão direta com Google Sheets (`gspread`), permitindo que as equipes de negócios atualizem a planilha e os dados reflitam instantaneamente no painel.
* **Ranking Dinâmico:** Processamento do Top 10 veículos mais vendidos, calculando automaticamente as proporções das barras.
* **UI/UX Premium:** Design construído com CSS customizado e Flexbox injetado no Streamlit, garantindo que as fotos dos veículos fiquem perfeitamente alinhadas ao gráfico de barras horizontais.
* **Tratamento de Exceções:** Sistema robusto para caso imagens não sejam encontradas, inserindo *placeholders* visuais para não quebrar a arquitetura do painel.

## 💻 Tecnologias Utilizadas
* **[Python 3](https://www.python.org/)**: Linguagem principal do projeto.
* **[Streamlit](https://streamlit.io/)**: Framework ágil para a criação da interface do dashboard.
* **[Pandas](https://pandas.pydata.org/)**: Motor de limpeza, ordenação e estruturação dos dados.
* **[Google Sheets API](https://developers.google.com/sheets/api) / [gspread](https://docs.gspread.org/)**: Para ingestão e autenticação (Service Account) dos dados hospedados na nuvem da Google.

## 🚀 Como executar o projeto localmente

### 1. Clonar o repositório
```bash
git clone https://github.com/KelsonHenrique/dashboard-veiculos-venezuela.git
cd dashboard-veiculos-venezuela
```

### 2. Configurar o Ambiente Virtual
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar Autenticação do Google
Para que o dashboard funcione, é necessário gerar uma chave de Conta de Serviço (Service Account) no Google Cloud Console com permissões para o **Google Sheets API** e **Google Drive API**.
* Baixe o arquivo JSON da sua conta de serviço.
* Renomeie-o para `credenciais.json` e coloque-o na raiz deste projeto.
* **Nota:** Este arquivo já está no `.gitignore` por questões de segurança e nunca deve ser commitado no repositório público.
* Compartilhe a planilha alvo com o e-mail gerado pela sua Conta de Serviço.

### 5. Executar a Aplicação
```bash
streamlit run app.py
```
O dashboard estará disponível no seu navegador no endereço: `http://localhost:8501`.

---
*Desenvolvido em parceria com ferramentas de Analytics Engineering orientadas por Inteligência Artificial.*
