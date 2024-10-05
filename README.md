 <h3 align="center">REST API для онлайн выставки кошек</h3>


### Используемый стек технологий в проекте:
* Django
* Django REST Framework
* PostgreSQL
* Docker
* и др.

### Для работы необходимо:
* Склонировать репозиторий в локальную директорию:
  ```sh
  git clone https://github.com/Aleksandr140590/test_workmate.git
  ```
* В каталоге infra/ создайте ```.env``` (или используйте .env.example) и задайте значения переменных:
    ```sh
  SECRET_KEY= Секретный ключ
  POSTGRES_DB= Название базы данных
  POSTGRES_USER= Пользователь БД
  POSTGRES_PASSWORD= Пароль пользователя БД
  POSTGRES_HOST=postgres
  POSTGRES_PORT=5432
  DJANGO_SUPERUSER_PASSWORD= Пароль для суперюзера
  DJANGO_SUPERUSER_USERNAME= Ник для суперюзера
  DJANGO_SUPERUSER_EMAIL= Email для суперюзера
  DJANGO_SUPERUSER_NAME= Имя для суперюзера
  DJANGO_SUPERUSER_SURNAME= Фамилия для суперюзера
  DEBUG_STATUS=
    ```
* Запуск сервера из каталога infra/:
    ```sh
    docker compose up -d
    ```
* Тестовые данные будут загружены автоматически
    ```
* Seagger:
  ```
  http://localhost/api/v1/schema/
  ```
