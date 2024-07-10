# user-service

Aplicação que encapsula dos dados de usuário.

Depende que um banco postgresql esteja rodando na porta 5432 com um db chamado users_db:
O schema do banco de dados deve ser o seguinte:

```sql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  name TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE
);

```

## Rodando aplicação com suas dependências
Veja https://github.com/Joaoasbittencourt/microservices-user-manager


## Como rodar aplicação sem dependências
 1. Certifique-se de que todas as aplicações dependências estão rodando
 2. Certifique-se de ter docker instalado
 3. docker build . -t users-service
 4. docker run -p 5000:5000 users-service
