# Flask Random User API

Esta é uma aplicação simples em Flask que serve uma API intermediária para obter dados de usuários aleatórios a partir da API pública randomuser.me.

# Funcionalidade
Quando acessada a rota / via método GET, a aplicação faz uma requisição para https://randomuser.me/api e retorna os dados JSON do usuário aleatório.

# Requisitos
Docker instalado na máquina.

-- Projeto de estudo.

# Comunicação Direta entre Containers PostgreSQL com Docker

Este projeto é uma demonstração de como configurar dois containers PostgreSQL para se comunicarem diretamente através de uma rede Docker.

### Conceitos Demonstrados

* **Rede Docker Bridge**: Criação de uma rede virtual customizada para isolar e permitir a comunicação entre containers.
* **Comunicação via Nome do Container**: Uso do nome do container (`db_source`) como hostname para a conexão de rede interna do Docker.
* **PostgreSQL Foreign Data Wrapper (`postgres_fdw`)**: Configuração de um banco de dados para atuar como um cliente de outro, permitindo consultas entre bancos.
* **Orquestração Manual**: Lançamento e configuração de containers usando comandos `docker run` e `docker exec`.
