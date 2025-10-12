# 🍕 Pizzaria App Pro

![Status](https://img.shields.io/badge/status-Finalizado-green)

> Projeto desenvolvido para a matéria de Sistemas Web, com o objetivo de criar um sistema completo de gerenciamento para uma pizzaria, incluindo backend e frontend.

### 📖 Tabela de Conteúdos
- [Descrição do Projeto](#-descrição-do-projeto)
- [Funcionalidades](#-funcionalidades)
- [Pré-requisitos](#-pré-requisitos)
- [Como Rodar a Aplicação](#-como-rodar-a-aplicação)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Autores](#-autores)

---

### 📝 Descrição do Projeto
<p align="justify">
  Aqui você descreve com mais detalhes o que o projeto faz. Qual o objetivo? Qual problema ele resolve? Fale sobre o sistema de pedidos, o gerenciamento de clientes, o cardápio, etc.
</p>

---

### ✨ Funcionalidades e Serviços AWS utilizados
- [x] Cadastro de Usuário
- [x] Login de Usuário
- [x] Listagem de Produtos (Pizzas)
- [x] Criação de Pedidos
- [x] Gerenciamento de Categorias
- [x] API Gateway: Expõe os endpoints HTTP
- [x] AWS Lambda: Executa funções serverless (addOrder, setAsDelivered, notifyOwner)
- [x] DynamoDB: Armazena dados dos pedidos e tokens
- [x] SNS (Simple Notification Service): Envia notificações quando um pedido muda de status
- [x] SQS (Simple Queue Service): 

---

### 🔧 Pré-requisitos
Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
* [Git](https://git-scm.com)
* [Node.js](https://nodejs.org/en/)
* [NPM](https://www.npmjs.com) ou [Yarn](https://yarnpkg.com)

---

### 🚀 Como Rodar a Aplicação

```bash
# Clone este repositório
$ git clone [https://github.com/Lorentralhe/ProjetoSW---Lorenzo-Bruno-Igor.git](https://github.com/Lorentralhe/ProjetoSW---Lorenzo-Bruno-Igor.git)

# Acesse a pasta do projeto
$ cd ProjetoSW---Lorenzo-Bruno-Igor/pizzaria-app-pro

# Instale as dependências do Backend
$ cd backend
$ npm install

# Rode o servidor do Backend
$ npm run dev

# Abra outro terminal na pasta do projeto
# Instale as dependências do Frontend
$ cd frontend
$ npm install

# Rode a aplicação Frontend
$ npm run dev
