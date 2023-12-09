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


## Instalando as dependencias do projeto

```
```


## Ativando o ambiente no VSCode


```shell

poetry shell
```

uvicorn src.server:app --reload


docker run --name postgres-db -p 5432:54321 -e POSTGRES_USER=root -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -d postgres:14

docker rm postgred-db --force