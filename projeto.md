# Endpoints da API

POST /api/tarefas/ → **Cria uma nova tarefa.**

GET /api/tarefas/ → **Lista as tarefas do usuário logado.**

GET /api/tarefas/?concluida=true → **Lista apenas as tarefas concluídas do usuário.**

GET /api/tarefas/{id}/ → **Mostra os detalhes da tarefa com o ID especificado.**

PUT /api/tarefas/{id}/ → **Atualiza a tarefa com o ID especificado.**

DELETE /api/tarefas/{id}/ → **Deleta a tarefa com o ID especificado.**