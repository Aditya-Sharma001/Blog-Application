# Blog Application

A simple blog application built using Django with Class-Based Views (CBVs), including features like user signup, login, logout, creating and viewing blogs, commenting on blogs, liking comments, searching blogs by title and content, and sharing blogs via email.

## Features

- **User Authentication**: 
  - User Signup
  - User Login
  - User Logout
- **Blog Functionality**: 
  - Create and View Blogs
  - Add Comments to Blogs
  - Like Comments
  - Share Blogs via Email
- **Search Functionality**:
  - Search Blogs by Title or Content
  - Filter Blogs by Tags
- **Pagination**: 
  - Pagination for the blog list (5 blogs per page)

## Technologies Used

- **Python 3.x**
- **Django 3.x**
- **PostgreSQL** (For full-text search and trigram similarity)
- **SMTP (Gmail)** for Email functionality
- **Python-Decouple** (For secure environment variable management)

## Installation and Setup

### Prerequisites

1. **Python** - Make sure Python is installed.
2. **PostgreSQL** - Ensure that PostgreSQL is installed and running.
3. **Virtual Environment** - It’s recommended to use a virtual environment to manage dependencies.

### 1. Clone the Repository

```bash
git clone https://github.com/Aditya-Sharma001/Blog-Application.git
cd blog-application

Set Up Virtual Environment
mkvirtualenv blogs

pip install -r requirements.txt

CREATE DATABASE blogs;
GRANT ALL PRIVILEGES ON DATABASE blogs TO <db_user>;

Configure Environment Variables - Create a .env file in the project’s root directory to securely store sensitive information such as email credentials and db credentials

EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER='your_email@gmail.com'
EMAIL_HOST_PASSWORD='your_email_password'
DEFAULT_FROM_EMAIL='your_email@gmail.com'
SECRET_KEY='your-django-secret-key'
DEBUG=True
ALLOWED_HOSTS='localhost,127.0.0.1'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog',
        'USER': 'write_your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


Run Database Migrations
python manage.py makemigrations
python manage.py migrate

Create a Superuser
python manage.py createsuperuser

Run the Development Server
python manage.py runserver


Usage
Home Page:
Visitors can sign up or log in.
Blog List:
Authenticated users can see a list of all blogs, with pagination (5 blogs per page).
Blog Detail:
Users can view blog details, post comments, like comments, and share the blog via email.
Search:
Users can search blogs by title or content, and filter by tags.


Security Best Practices
Environment Variables: Sensitive information such as email credentials should be stored in environment variables, and never hard-coded into the project.
.gitignore: Ensure that the .env file is included in the .gitignore file to avoid pushing sensitive information to version control.



If you have any questions, feel free to reach out:

Email: me.adityasharma12@gmail.com
