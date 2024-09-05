README
This is a project built with Django that is a database of movies and their soundtracks.

Models
The following models are used in the project:

Genre: represents the genre of the movie.
Film: represents the movie with its title, description, year of release, and genre.
FilmPhotos: represents the photos of the movie.
SoundTrack: represents the soundtrack of the movie with its title, description, and track link.
API
The project has an API that allows CRUD operations on models.

Installation
To install the project, you need to perform the following steps:

Install the necessary libraries: pip install -r requirements.txt
Create migrations: python manage.py makemigrations
Run migrations: python manage.py migrate

Run
To run the project, you need to run the command: python manage.py runserver

Usage
To use the API, you need to send requests to the following addresses:

GET /api/films/ - get a list of all films
GET /api/films/<id>/ - get information about a specific film
POST /api/films/ - create a new film
PUT /api/films/<id>/ - update information about a specific film
DELETE /api/films/<id>/ - delete a specific film
Similarly, you can use the API to work with genres, film photos, and soundtracks.