### CRUD для Yatube - api_final_yatube

Для взаимодействия с ресурсами доступны следующие эндпоинты:
* ```api/v1/posts/``` (GET, POST): получаем список всех постов или создаём новый пост. При указании параметров limit и offset выдача работает с пагинацией.
* ```api/v1/posts/{post_id}/``` (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост по id.
* ```api/v1/groups/``` (GET): получаем список всех групп.
* ```api/v1/groups/{group_id}/``` (GET): получаем информацию о группе по id.
* ```api/v1/posts/{post_id}/comments/``` (GET, POST): получаем список всех комментариев поста с id=post_id или создаём новый, указав id поста, который хотим прокомментировать.
* ```api/v1/posts/{post_id}/comments/{comment_id}/``` (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий по id у поста с id=post_id.
* ```api/v1/follow/``` (GET, POST): GET возвращает все подписки пользователя, сделавшего запрос. Анонимные запросы запрещены. POST подпишет пользователя, от имени которого сделан запрос, на пользователя переданного в теле запроса.
* ```api/v1/jwt/create/``` ( POST): получение JWT-токена.
* ```api/v1/jwt/refresh/``` ( POST): обновление JWT-токена.
* ```api/v1/jwt/verify/``` ( POST): проверка JWT-токена.
### Технологии:
* Python 3.11
* Django 3.2.16
* Django REST framework 3.12.4
* djangorestframework-simplejwt 4.7.2

### Запуск проекта

Клонировать проект c GitHub:

```bash
git clone git@github.com:chrnmaxim/api_final_yatube.git
```

Перейти в папку с проектом:

```bash
cd api_final_yatube
```
Установить виртуальное окружение:
```bash
python -m venv venv
```
Активировать виртуальное окружениe:
```bash
. venv/Scripts/activate
```
Обновить менеджер пакетов pip:
```bash
python -m pip install --upgrade pip
```
Установить зависимости из requirements.txt:
```bash
pip install -r requirements.txt
``` 
Перейти в директорию с файлом manage.py и применить миграции:
```bash
cd yatube_api
python manage.py migrate
``` 
Создать супер пользователя:

```bash
python manage.py createsuperuser
```
Запустить сервер разработки (виртуальное окружение должно быть активно):
```bash
python manage.py runserver 
```
Документация API в формате ReDoc доступна по адресу:
```bash
http://127.0.0.1:8000/redoc/
```
## Примеры запросов
Получить список всех публикаций. При указании параметров limit и offset выдача должна работать с пагинацией:
```bash

http://127.0.0.1:8000/redoc/
```
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
Получение всех комментариев к публикации:
```
GET http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```
```
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```
Получение списка доступных сообществ.
```
GET http://127.0.0.1:8000/api/v1/groups/
```
```
[
  {
    "id": 0,
    "title": "string",
    "slug": "^-$",
    "description": "string"
  }
]
```
Возвращает все подписки пользователя, сделавшего запрос:
```
GET http://127.0.0.1:8000/api/v1/follow/
```
```
[
  {
    "user": "string",
    "following": "string"
  }
]
```
Получение JWT-токена.
```
POST http://127.0.0.1:8000/api/v1/jwt/create/

{
  "username": "string",
  "password": "string"
}
```
```
{
  "refresh": "string",
  "access": "string"
}
```
К доступным эндпоинтам также можно обращаться с помощью [Postman](https://www.postman.com/).