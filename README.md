#  MovieFeed - Django Movie Platform

MovieFeed is a Django-based movie web application where users can register, log in, browse movies, view details, and manage a personal watchlist.

---

##  Features

- User registration and authentication (login / logout)
- Movie listing page
- Movie detail page
- Personal watchlist system
- User-specific sessions
- Bootstrap-based responsive UI
- Protected routes for authenticated users

---

##  Tech Stack

- Python 3
- Django 6
- PostgreSQL
- HTML / CSS
- Bootstrap 5

---

##  Project Structure

Movie_Feed/
├── config/               # Project settings and URLs
├── movies/               # Movie app (models, views, urls)
    ├── templates/movies
        └── movie_detail.html
        └── movie_list.html
        └── watchlist.html
├── users/                # Authentication system
├── templates/            # Global templates
    ├── base.html    
  ├──registration/        # login & register pages
      └── login.html
      └── register.html
├── manage.py
├── templates

---

##  Future Improvements

- Movie rating system
- Comments system
- Search and filter
- API integration (TMDB)
- Deployment (Render / Railway)
