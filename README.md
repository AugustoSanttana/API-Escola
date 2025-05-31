# 📘 API da Escola

## Descrição
Esta API é responsável por gerenciar informações relacionadas a turmas e professores. Ela fornece endpoints para listar, buscar e validar entidades educacionais, servindo como base para outros microsserviços, como o de reservas de salas.

## Como executar

### Pré-requisitos
- Docker
- Docker Compose

### Passos para execução
1. Clone o repositório:
   ```bash
   git clone https://github.com/AugustoSanttana/API-Escola.git
   cd API-Escola/api
Execute o Docker Compose:

bash
Copiar
Editar
docker-compose up --build
Acesse a API em: http://localhost:8000

Endpoints principais
GET /turmas
Lista todas as turmas cadastradas.

GET /turmas/<id>
Retorna os detalhes de uma turma específica.

GET /professores
Lista todos os professores cadastrados.

GET /professores/<id>
Retorna os detalhes de um professor específico.

Tecnologias utilizadas
Python 3.12

Flask

PostgreSQL

SQLAlchemy

Docker

Integração com outros microsserviços
Esta API serve como fonte de dados para outros serviços, como o de reservas de salas, que consomem seus endpoints para validar a existência de turmas e professores antes de realizar operações relacionadas.

Estrutura do projeto
arduino
Copiar
Editar
api/
├── app.py
├── config/
│   └── __init__.py
├── controllers/
│   ├── professores_controller.py
│   └── turmas_controller.py
├── models/
│   ├── professor_model.py
│   └── turma_model.py
├── services/
│   ├── professor_service.py
│   └── turma_service.py
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
