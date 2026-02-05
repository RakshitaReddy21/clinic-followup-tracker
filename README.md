# Clinic Follow-up Tracker (Lite)

A Django-based application to manage clinic patient follow-ups with secure clinic-level access, public follow-up links, and CSV import support.

---

**********************Tech Stack*************************
- Python 
- Django 
- MySQL
- Django ORM (no DRF or Celery)

---

************************Project Setup**************************

1. Clone Repository
```bash
git clone <your-repo-url>
cd Clinic_Followup_Tracker/clinic_tracker

2. Create & Activate Virtual Environment
python -m venv clinic_env
source clinic_env/bin/activate

3. Install Dependencies
pip install -r requirements.txt

Database Setup (MySQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'clinic_db',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

Migrations
python manage.py makemigrations
python manage.py migrate

Create Superuser
python manage.py createsuperuser


Initial Data Setup

	Login to Django Admin at:
	http://127.0.0.1:8000/admin/
	Create a Clinic
	Create a User
	Create a UserProfile and assign the user to the clinic

Run Server
python manage.py runserver


***************Access*****************
Dashboard: http://127.0.0.1:8000/
Admin Panel: http://127.0.0.1:8000/admin/

CSV Import (Pure Python)
Import follow-ups using a CSV file:
python manage.py import_followups --csv sample.csv --username <username>


********Running Tests******
python manage.py test
Tests Included::
	Unique generation of clinic_code
	Unique generation of public_token
	Dashboard requires authentication
	Cross-clinic data access is blocked
	Public follow-up page creates a PublicViewLog



*********Admin Features***********
	All models registered in Django admin
	Useful list displays
	Auto-generated fields are read-only
	Secure clinic-level data separation
	
	
	
	
