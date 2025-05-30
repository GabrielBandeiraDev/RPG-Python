# StockMaster API: Sistema de Gerenciamento de Estoque e Vendas

![StockFlow](https://i.imgur.com/JK7w3P9.png)

## Descrição

O StockMaster é um sistema completo de gerenciamento de estoque e vendas desenvolvido com FastAPI e Python. Este projeto foi criado como uma solução para o desafio do instituto IBBI , voltado para o treinamento de Conhecimentos de Gabriel B. - Dev . PL 

- O sistema oferece:

- Autenticação segura via JWT
- CRUD completo para produtos
- Registro de vendas com cálculo automático de valores
- Dashboard analítico em tempo real
- Histórico completo de alterações
- WebSocket para atualizações instantâneas
- Cache com Redis para alta performance
- Sincronização entre estoque principal e dashboard

## Tecnologias Utilizadas

- **FastAPI**: Framework moderno e rápido para construção de APIs
- **SQLAlchemy**: ORM poderoso para interação com banco de dados
- **Redis**: Sistema de cache para melhorar performance
- **JWT**: Autenticação segura com JSON Web Tokens
- **WebSocket**: Comunicação em tempo real entre servidor e clientes
- **PostgreSQL/SQLite**: Bancos de dados suportados
- **Pydantic**: Validação de dados eficiente

## Instalação

Para instalar e executar o StockFlow API, siga estas etapas:

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/stockflow-api.git
```

2. Entre no diretório do projeto:
```bash
cd stockMaster-api
```

3. Crie e ative um ambiente virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

5. Configure as variáveis de ambiente (crie um arquivo `.env`):
```ini
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
SECRET_KEY=sua_chave_secreta_aqui
```

6. Execute o servidor:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

O servidor estará disponível em `http://localhost:8000` e a documentação interativa (Swagger UI) em `http://localhost:8000/docs`.

## Uso

### Autenticação

1. Primeiro, faça login para obter seu token:
```bash
curl -X POST "http://localhost:8000/auth/login" \
-H "Content-Type: application/json" \
-d '{"username": "user@example.com", "password": "secret"}'
```

2. Use o token retornado nas requisições subsequentes:
```bash
curl -X GET "http://localhost:8000/products/" \
-H "Authorization: Bearer <seu_token_aqui>"
```

### Endpoints Principais

- **Produtos**:
  - `GET /products/` - Lista todos os produtos
  - `POST /products/` - Cria um novo produto
  - `PUT /products/{id}` - Atualiza um produto
  - `DELETE /products/{id}` - Remove um produto

- **Vendas**:
  - `POST /products/purchase/` - Registra uma nova venda
  - `GET /sales-history/` - Histórico de vendas

- **Dashboard**:
  - `GET /dashboard/products/` - Produtos para o dashboard
  - `GET /top-products/` - Produtos mais vendidos
  - `GET /sales-by-category/` - Vendas por categoria

- **Configuração**:
  - `POST /update_dollar_rate/` - Atualiza taxa de câmbio

## Exemplo de Requisição

Criar um novo produto:
```bash
curl -X POST "http://localhost:8000/products/" \
-H "Authorization: Bearer <seu_token_aqui>" \
-H "Content-Type: application/json" \
-d '{
    "description": "Notebook Dell Inspiron",
    "image_url": "https://example.com/notebook.jpg",
    "quantity": 15,
    "suggested_quantity": 10,
    "price": 4500.00,
    "categories": ["Eletrônicos", "Informática"]
}'
```

## Preto no Branco para DEVS (Analisar o Código)

-Logo após o DEV clonar o repositório , deve fazer o pip dos requeriments.txt logo após isso ele irá :
-Terminal : CD Backend , (Uvicorn main:app --reload )
-Terminal 2 : CD src/ , (Npm run dev )
-Logo após isso o Dev abre o LocalHost na "/" 
-Login (user@example.com)/(senha : secret)

-como acessar rotas ?

-Rotas de produto  - /produtos , /cadastro , /dashboard.


## Video no Youtube 

Para dúvidas ou sugestões, entre em contato:

- Eu deixei um Video no youtube, e uma documentação em PDF do meu codigo completo de forma bem explicada!
- PDF :
- Video : 
