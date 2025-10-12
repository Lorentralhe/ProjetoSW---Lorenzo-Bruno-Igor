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

```
🛠️ Tecnologias Utilizadas
As seguintes ferramentas foram usadas na construção do projeto:

Backend (Serverless)
<p>
<a href="https://nodejs.org/en/" target="_blank">
<img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" alt="Node.js"/>
</a>
<a href="https://aws.amazon.com/lambda/" target="_blank">
<img src="https://img.shields.io/badge/AWS_Lambda-FF9900?style=for-the-badge&logo=aws-lambda&logoColor=white" alt="AWS Lambda"/>
</a>
<a href="https://aws.amazon.com/api-gateway/" target="_blank">
<img src="https://img.shields.io/badge/API_Gateway-FF4F8B?style=for-the-badge&logo=amazon-api-gateway&logoColor=white" alt="Amazon API Gateway"/>
</a>
<a href="https://aws.amazon.com/dynamodb/" target="_blank">
<img src="https://img.shields.io/badge/Amazon_DynamoDB-4053D6?style=for-the-badge&logo=amazon-dynamodb&logoColor=white" alt="Amazon DynamoDB"/>
</a>
<a href="https://www.serverless.com/" target="_blank">
<img src="https://img.shields.io/badge/Serverless-FD5750?style=for-the-badge&logo=serverless&logoColor=white" alt="Serverless Framework"/>
</a>
</p>


```
  

### 👥 Autores  
Este projeto foi desenvolvido por:

<table>
<tr>
<td align="center">
<a href="https://github.com/Lorentralhe">
<sub><b>Lorenzo</b></sub>
</a>
</td>
<td align="center">
<a href="https://github.com/brunobui/">
<sub><b>Bruno</b></sub>
</a>
</td>
<td align="center">
<a href="https://github.com/Igorrangelsouza">
<sub><b>Igor</b></sub>
</a>
</td>
</tr>
</table>
