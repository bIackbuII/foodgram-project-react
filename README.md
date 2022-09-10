# Foodgram - Продуктовый помощник

Foodgram - сервис для публикации рецептов.  
Пользователи могут создавать свои рецепты, читать рецепты других пользователей, подписываться на интересных авторов, добавлять лучшие рецепты в избранное, а также создавать список покупок и скачивать его в pdf формате.

## Установка
#### 1. Клонируем репозиторий:

- `git clone https://github.com/bIackbuII/foodgram-project-react.git`

#### 2. Запускаем Docker

#### 3. Открываем терминал

#### 4. Переходим в директорию `infra` склонированного репозитория

#### 5. Выполняем команду для сборки и запуска контейнеров:

- `docker-compose up -d`

#### 6. Переходим в консоль контейнера с веб-приложением (дальнейшие команды будут применятся из консоли контейнера)

- `docker exec -it <CONTAINER_ID> bash`

#### 7. Выполняем миграции:

- `python manage.py migrate`

#### 8. Создаем суперпользователя:

- `python manage.py createsuperuser`

#### 9. Загружаем тестовые данные в базу данных

- `python manage.py load_ingrs`
- `python manage.py load_tags`

# Развернутый проект
Проект доступен по ссылке - http://chernovol.ddns.net/

## Тестовые пользователи
Email: `admin@gmail.com`

Пароль: `minda12345`

---

Email: `magamed_orel@gmail.com`

Пароль: `verystrongpassword`

---

Email: `nesterova-marina@gmail.com`

Пароль: `verystrongpassword`

---

Email: `chernovol.el@gmail.com`

Пароль: `verystrongpassword`
