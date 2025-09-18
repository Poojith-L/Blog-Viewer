# 📖 Blog Viewer

Blog Viewer is a **Django web application** where users can explore blogs authored by different writers.  
Registered authors can securely **create, update, and manage blogs**, while administrators can manage users and permissions through the **Django Admin Dashboard**.  
The application is backed by **PostgreSQL** and includes a prototype for **email notifications** using Celery, Redis, and aiosmtpd.  
It follows clean, modular design with mixins for authentication and a scalable architecture.

---

## 🚀 Features
- Browse blogs posted by various authors.
- User **signup/login** with authentication mixins.
- Create, update, and view blog posts.
- **Django Admin** for managing users, permissions, and blog filtering.
- PostgreSQL database integration for reliability and scalability.
- Prototype for **async email notifications** with Celery + Redis.

---

## 🛠️ Tech Stack
- **Backend:** Django (Python)
- **Database:** PostgreSQL
- **Task Queue:** Celery, Redis
- **Email Prototype:** aiosmtpd
- **Authentication:** Django Auth + Mixins
- **Frontend:** HTML, CSS (custom styling)

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/blog-viewer.git
   cd blog-viewer

2. **Create virtual environment & install dependencies**
   ```base
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate

3. **Configure PostgreSQL**
   - Update settings.py with your PostgreSQL credentials:
   ```python
   DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'websitedb',
            'USER': 'youruser',
            'PASSWORD': 'yourpassword',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

4. **Run migrations**
   ```bash
   python manage.py migrate

5. **Create superuser**
   ```bash
   python manage.py createsuperuser

6. **Run development server**
   ```bash
   python manage.py runserver

## 📬 Future Improvements
- Implement full email notification system for new users.
- Add rich text editor for blog posts.
- Improve UI with Bootstrap/Tailwind integration.
- Deploy to cloud (Heroku/Netlify/AWS).
