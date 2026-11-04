# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST para gerenciar livros usando FastAPI. Você praticará rotas HTTP, parâmetros de caminho, validação de dados e respostas com códigos de status apropriados.

## 📝 Tasks

### 🛠️ Criar rotas para consultar livros

#### Descrição
Complete as rotas de leitura no código inicial para que clientes possam listar os livros cadastrados e consultar um livro pelo seu identificador.

#### Requisitos
A API concluída deve:

- Responder a `GET /books` com a lista de livros disponíveis.
- Responder a `GET /books/{book_id}` com os dados do livro correspondente.
- Retornar o status HTTP `404` quando o identificador solicitado não existir.
- Expor a documentação interativa do FastAPI em `/docs`.

### 🛠️ Criar livros com validação

#### Descrição
Implemente a rota para cadastrar livros. Use os modelos Pydantic fornecidos para validar os dados recebidos e gerar um identificador para cada novo registro.

#### Requisitos
A API concluída deve:

- Aceitar `POST /books` com título, autor e ano de publicação.
- Rejeitar dados que não correspondam aos campos e tipos definidos no modelo de entrada.
- Adicionar o livro à coleção em memória e devolver o registro criado com status HTTP `201`.

### 🛠️ Atualizar e remover livros

#### Descrição
Complete as rotas de atualização e remoção para que clientes possam gerenciar os livros existentes pelo identificador.

#### Requisitos
A API concluída deve:

- Aceitar `PUT /books/{book_id}` para atualizar título, autor e ano de publicação de um livro existente.
- Aceitar `DELETE /books/{book_id}` para remover um livro existente e responder com status HTTP `204`.
- Retornar o status HTTP `404` ao tentar atualizar ou remover um identificador inexistente.
- Manter as alterações disponíveis enquanto a aplicação estiver em execução.

Para executar a API, instale as dependências com `python -m pip install fastapi uvicorn` e inicie o servidor com `python -m uvicorn starter-code:app --reload`. A documentação interativa ficará disponível em `http://127.0.0.1:8000/docs`.
