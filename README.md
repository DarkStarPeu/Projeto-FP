# FitPlanner - Sistema de Planejamento Fitness

## Autores

- João Pedro de Queiroz Nogueira
- Nelson Meira de Lima

## Descrição do Projeto

O **FitPlanner** é um sistema de planejamento fitness desenvolvido em Python, com funcionamento pelo terminal.

O objetivo do projeto é ajudar usuários a organizarem melhor sua rotina de treinos, exercícios, metas e evolução pessoal. O sistema permite cadastrar planos de treino, registrar exercícios, acompanhar metas, visualizar evolução e receber sugestões simples relacionadas à rotina fitness.

A aplicação utiliza arquivos `.txt` para armazenar os dados, permitindo que as informações cadastradas continuem salvas mesmo após o encerramento do programa.

## Problema

Marina começou a frequentar academia e decidiu ter uma vida mais saudável, mas encontrou dificuldade para acompanhar sua rotina fitness, controlar exercícios realizados, registrar metas e manter disciplina.

Pensando nisso, o FitPlanner foi criado para auxiliar Marina e outros usuários no controle de treinos, metas e evolução física de forma simples e prática.

## Funcionalidades do Sistema

### 1. CRUD de Planos de Treino

O sistema permite que o usuário gerencie seus planos de treino.

É possível:

- Cadastrar um novo treino
- Visualizar os treinos cadastrado
- Editar informações de um treino
- Excluir um treino

Cada plano de treino possui as seguintes informações:

- Nome do treino
- Tipo do treino
- Data
- Duração
- Objetivo

Exemplos de tipos de treino:

- Musculação
- Cardio
- Funcional
- Corrida

---

### 2. Cadastro de Exercícios

O usuário pode cadastrar exercícios relacionados a um plano de treino já existente.

Cada exercício possui:

- Nome do exercício
- Quantidade de séries
- Quantidade de repetições
- Tempo, distância ou observação

Exemplos de exercícios:

- Agachamento
- Supino
- Corrida
- Abdominal
- Flexão

Também é possível visualizar os exercícios cadastrados em cada treino.

---

### 3. Controle de Metas

O sistema permite cadastrar metas fitness para acompanhar os objetivos do usuário.

Cada meta possui:

- Descrição
- Tipo da meta
- Prazo
- Status

Exemplos de metas:

- Perder peso
- Ganhar massa muscular
- Melhorar o condicionamento físico
- Treinar mais vezes por semana

O usuário também pode marcar uma meta como concluída.

---

### 4. Acompanhamento de Evolução

O sistema pode exibir informações sobre a evolução do usuário com base nos dados cadastrados.

Exemplos de informações exibidas:

- Quantidade de treinos cadastrados
- Quantidade de exercícios registrados
- Quantidade de metas concluídas
- Quantidade de metas em andamento
- Progresso geral do usuário

Essa funcionalidade ajuda o usuário a ter uma visão geral da sua rotina fitness.

---

### 5. Armazenamento de Dados

Todos os dados do sistema são armazenados em arquivos `.txt`.

Arquivos utilizados:

```text
treinos.txt
exercicios.txt
metas.txt
