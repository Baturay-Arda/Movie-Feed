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
├── users/                # Authentication system
├── templates/            # Global templates
│   ├── registration/     # login & register pages
│   └── movies/           # movie pages
├── manage.py

---

##  Installation

### 1. Clone the repository
git clone https://github.com/yourusername/moviefeed.git
cd moviefeed

---

### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

---

### 3. Install dependencies
pip install -r requirements.txt

---

### 4. Setup database (PostgreSQL)
Update database credentials in settings.py or .env file.

---

### 5. Run migrations
python manage.py makemigrations
python manage.py migrate

---

### 6. Create superuser (optional)
python manage.py createsuperuser

---

### 7. Run server
python manage.py runserver

---

##  Authentication Flow

Register → Login → Movies → Movie Detail → Watchlist → Logout

---

##  Future Improvements

- Movie rating system
- Comments system
- Search and filter
- API integration (TMDB)
- Deployment (Render / Railway)

---

##  Author

Developed by Baturay

---

##  License

This project is for educational purposes.
