# Учебный проект todo list
В основе проекта лежат небольшие проекты, сделанные в рамках обучения.
Поэтому на данном этапе всё ещё можно встретить закомментированные куски кода,
которые постепенно будут удаляться.

Также, в docker-compose не запускается фронтовая часть. Будет прикручена в следующем этапе,
в процессе переписывания кода на фронте.

Backend:
- python 3.9
- flask
- mongodb
- redis

Api tests:
- python
- requests
- pytest

Frontend:
- react
- redux
- router

## Перед сборкой dev сборки
1. Выбрать ветку dev
2. Добавить файл .dev.env  в директорию backend

В файле .dev.env необходимо указать значения переменных:
- REDIS_URI
- DATABASE_URI
- SECRET_KEY
- SECRET_KEY_FOR_ADMIN

Пример:

`REDIS_URI='redis://localhost:6379/0'`

`DATABASE_URI='mongodb://mongodb:27017/DevTodoDB'`

`SECRET_KEY='a02c3cf84bc4a66b8a9a13dba5f4516b'`

`SECRET_KEY_FOR_ADMIN= "9cc3a144772b168ca171cea9599fa73f"`

## Cборка и запуск dev версии

1. Выбрать ветку dev
2. В консоли команда: `sudo docker-compose up -d --build`

### Запуск api тестов внутри контейнера

`sudo docker-compose exec -T tests/test_api/tests pytest -vs`

### Остановка докера после прогона тестов

Удалить докер контейнеры: `sudo docker-compose down`

### Удаление всех докер образов

`sudo docker rmi $(sudo docker images -a -q)`