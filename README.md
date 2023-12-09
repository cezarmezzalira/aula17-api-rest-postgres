# Aula 17 - CRUD com PostgreSQL

## Usando o poetry para gerenciar dependencias

```shell
pip install poetry
```

## Configurar o poetry para criar .venv automaticamente

```shell
poetry config virtualenvs.in-project true
```

## Criando um no projeto

```shell
cd projetos
mkdir aula17-api-rest-postgres
code aula17-api-rest-postgres
```

## Instalando as dependências do projeto

```shell
poetry install
```

## Rodando o container docker com o banco de dados

```shell
# Remove 
docker run --name aula17-pg-db -p 5432:54321 -e POSTGRES_USER=root -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=oficina -d postgres:14
```

## Executando o projeto

```shell
poetry run uvicorn src.server:app --reload
```
