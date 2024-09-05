README
Это проект, созданный с помощью Django, который представляет собой базу данных фильмов и их саундтреков.

Модели
В проекте используются следующие модели:

Жанр (Genre): представляет собой жанр фильма.
Фильм (Film): представляет собой фильм с его названием, описанием, годом выпуска и жанром.
Фотографии фильма (FilmPhotos): представляет собой фотографии фильма.
Саундтрек (SoundTrack): представляет собой саундтрек фильма с его названием, описанием и ссылкой на трек.
API
В проекте реализовано API, которое позволяет выполнять CRUD-операции над моделями.

Установка
Для установки проекта необходимо выполнить следующие шаги:

Установить необходимые библиотеки: pip install -r requirements.txt
Создать миграции: python manage.py makemigrations
Выполнить миграции: python manage.py migrate

Запуск
Для запуска проекта необходимо выполнить команду: python manage.py runserver

Использование
Для использования API необходимо отправлять запросы на следующие адреса:

GET /api/films/ - получить список всех фильмов
GET /api/films/<id>/ - получить информацию о конкретном фильме
POST /api/films/ - создать новый фильм
PUT /api/films/<id>/ - обновить информацию о конкретном фильме
DELETE /api/films/<id>/ - удалить конкретный фильм
Аналогично можно использовать API для работы с жанрами, фотографиями фильмов и саундтреками.