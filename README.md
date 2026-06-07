# FitPlanner - Sistema de Planejamento Fitness

## Autores

- João Pedro de Queiroz Nogueira
- Nelson Meira de Lima

## Sobre o Projeto

O **FitPlanner** é um sistema simples desenvolvido em Python com o objetivo de ajudar usuários a organizarem sua rotina fitness.

O sistema permite cadastrar planos de treino, exercícios e metas pessoais, facilitando o controle da rotina de academia e o acompanhamento dos objetivos do usuário.

A aplicação funciona pelo terminal e salva os dados em arquivos `.txt`, garantindo que as informações continuem disponíveis mesmo após fechar o programa.

## Funcionalidades

### Planos de Treino

O usuário pode realizar as seguintes ações:

- Cadastrar planos de treino;
- Visualizar treinos cadastrados;
- Editar informações de um treino;
- Excluir treinos.

Cada plano de treino possui:

- Nome do treino;
- Tipo;
- Data;
- Duração;
- Objetivo.

### Exercícios

O sistema permite cadastrar exercícios relacionados a um plano de treino.

Cada exercício possui:

- Nome;
- Quantidade de séries;
- Repetições;
- Observação, tempo ou distância.

Também é possível visualizar os exercícios cadastrados em cada treino.

### Metas

O usuário pode cadastrar metas fitness, como:

- Perder peso;
- Ganhar massa muscular;
- Melhorar o condicionamento físico.

Cada meta possui:

- Descrição;
- Tipo;
- Prazo;
- Status.

Também é possível marcar uma meta como concluída.

### Armazenamento de Dados

Os dados são salvos em arquivos `.txt`:

- `treinos.txt`
- `exercicios.txt`
- `metas.txt`

Esses arquivos são criados automaticamente conforme o sistema é utilizado.

## Tecnologias Utilizadas

- Python
- Terminal / Linha de comando
- Arquivos `.txt`

## Como Executar

Para executar o projeto, é necessário ter o Python instalado no computador.

Depois, abra o terminal na pasta do projeto e execute:

```bash
python fitplanner.py
