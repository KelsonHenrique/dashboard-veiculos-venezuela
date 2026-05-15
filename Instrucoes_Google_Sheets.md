# Guia de Integração: Google Sheets API e Python

Para que o nosso dashboard consiga puxar os dados da sua planilha automaticamente, precisamos criar uma credencial que funciona como um "usuário robô" (Service Account). Esse robô terá permissão apenas para ler as planilhas que você compartilhar com ele.

Siga o passo a passo abaixo:

## Passo 1: Criar um Projeto no Google Cloud
1. Acesse o [Google Cloud Console](https://console.cloud.google.com/).
2. Faça login com a sua conta Google (pode ser a mesma onde a planilha está salva).
3. No menu superior (ao lado da logo do Google Cloud), clique no **Seletor de Projetos** e depois em **"Novo Projeto"**.
4. Dê um nome ao projeto (ex: `Dashboard-Veiculos`) e clique em **"Criar"**.
5. Certifique-se de selecionar esse projeto recém-criado no menu superior.

## Passo 2: Ativar as APIs Necessárias
O nosso código precisa de duas APIs para ler a planilha corretamente:
1. No menu lateral esquerdo (☰), vá em **APIs e Serviços** > **Biblioteca**.
2. Na barra de pesquisa, digite **"Google Sheets API"**. Clique nela e depois em **"Ativar"**.
3. Volte para a Biblioteca, pesquise por **"Google Drive API"**, clique nela e também clique em **"Ativar"**.

## Passo 3: Criar a Conta de Serviço (O seu "Robô")
1. No menu lateral esquerdo, vá em **APIs e Serviços** > **Credenciais**.
2. No topo da tela, clique em **"+ CRIAR CREDENCIAIS"** e escolha **"Conta de Serviço"** (Service Account).
3. Preencha os detalhes:
   * **Nome da conta de serviço:** `acesso-planilha`
   * O sistema vai gerar um ID de e-mail automaticamente logo abaixo (ex: `acesso-planilha@dashboard-veiculos.iam.gserviceaccount.com`). **Copie esse e-mail e guarde-o (você precisará dele no Passo 5)**.
4. Clique em **"Criar e Continuar"**.
5. Em "Conceder a essa conta de serviço acesso ao projeto", você não precisa selecionar nenhuma função (pode deixar em branco). Clique em **"Continuar"** e depois em **"Concluído"**.

## Passo 4: Gerar a Chave JSON
Agora vamos baixar o arquivo de senha do nosso "robô".
1. Você será redirecionado de volta para a tela de Credenciais.
2. Na parte inferior, na lista de **"Contas de Serviço"**, clique no e-mail que você acabou de criar.
3. Vá até a aba **"CHAVES"** (Keys).
4. Clique em **"Adicionar Chave"** > **"Criar nova chave"**.
5. Escolha o tipo **JSON** e clique em **"Criar"**.
6. Um arquivo `.json` será baixado automaticamente para o seu computador.
7. Mova esse arquivo `.json` para a pasta atual do nosso projeto (`/Users/kelsonelaura/python/paises/venezuela/`) e renomeie-o para algo simples, como `credenciais.json`.

## Passo 5: Compartilhar a Planilha com o Robô
Este é o passo mais importante:
1. Abra a sua planilha com os dados dos veículos no Google Sheets.
2. Clique no botão **"Compartilhar"** (canto superior direito).
3. No campo "Adicionar pessoas e grupos", cole o e-mail da conta de serviço que você copiou no Passo 3 (ex: `acesso-planilha@...iam.gserviceaccount.com`).
4. Desmarque a opção "Notificar pessoas" (pois é um robô, não recebe e-mail).
5. Certifique-se de que a permissão está como **"Leitor"** (Viewer).
6. Clique em **"Compartilhar"**.

## Passo 6: O que preciso que você me envie
Para que eu possa atualizar o código Python (`app.py`), por favor, me confirme quando o arquivo `.json` estiver na pasta do projeto e me passe a seguinte informação:
1. O **nome da sua planilha** (ou parte do link, não precisa ser o link inteiro, apenas a URL base).
2. O nome exato que está na **Aba/Página** da planilha (ex: `Página1`, `Vendas`, etc.).
3. Os nomes exatos das colunas (ex: `Modelo`, `Vendas`, `Foto`).
