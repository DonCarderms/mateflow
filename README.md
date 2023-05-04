# Gerenciamento de Materiais

Este projeto consiste em um sistema de gerenciamento de materiais que permite aos usuários cadastrar, visualizar, atualizar e remover informações sobre materiais. Além disso, os usuários podem se cadastrar e interagir com os materiais através de comentários.

## Tecnologias Utilizadas

A aplicação foi desenvolvida utilizando as seguintes tecnologias:

- Backend:

  - Linguagem Python
  - Framework Django para criação dos modelos
  - Django Rest Framework para criação da API

- Frontend:
  - Linguagem TypeScript
  - Framework React 
  - React Router para roteamento das URLs
  - React Query para requisições

## Como Executar o Projeto

1. Clone o repositório em sua máquina local:
   git clone `https://github.com/DonCarderms/Gestao-de-materiais.git`

2. Instale as dependências do backend:
   cd backend/
   pip install -r requirements.txt

3. Execute as migrações do banco de dados:
   python manage.py migrate

4. Inicie o servidor backend:
   python manage.py runserver

5. Instale as dependências do frontend:
   cd nome-do-repositorio/frontend
   npm install

6. Inicie o servidor frontend:
   npm start

A aplicação estará executando na porta 3000 por padrão.

## Funcionalidades

A aplicação possui as seguintes funcionalidades:

- Visualização da lista de materiais cadastrados: `http://localhost:3000/materiais`
- Cadastro de um novo material: `http://localhost:3000/materiais/novo`
- Visualização das informações de um material específico: `http://localhost:3000/materiais/:id`
- Atualização das informações de um material específico: `http://localhost:3000/materiais/:id/editar`
- Remoção de um material específico: `http://localhost:3000/materiais/:id/remover`
- Visualização da lista de usuários cadastrados: `http://localhost:3000/usuarios`
- Cadastro de um novo usuário: `http://localhost:3000/usuarios/novo`
- Visualização das informações de um usuário específico: `http://localhost:3000/usuarios/:id`
- Atualização das informações de um usuário específico: `http://localhost:3000/usuarios/:id/editar`
- Remoção de um usuário específico: `http://localhost:3000/usuarios/:id/remover`
- Visualização da lista de comentários cadastrados em um material específico: `http://localhost:3000/materiais/:id/comentarios`
- Cadastro de um novo comentário em um material específico: `http://localhost:3000/materiais/:id/comentarios/novo`
- Visualização das informações de um comentário específico em um material específico: `http://localhost:3000/materiais/:id/comentarios/:id_comentario`
- Atualização das informações de um comentário específico em um material específico: `http://localhost:3000/materiais/:id/comentarios/:id_comentario/editar`
- Remoção de um comentário específico
