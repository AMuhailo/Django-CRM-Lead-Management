## __ 📞Lead Management System __
![Django](https://img.shields.io/badge/Django-4.2-green?style=for-the-badge) ![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge)
## Description project
Lead Management System is a CRM system for managing leads and agents, 
which includes lead creation functionality, agent management, 
sending messages via Celery, a password reset system, customer 
categorization, and full CRUD functionality.

🚀Deploy on Railway
The project has not yet been launched on Railway but will be launched.

## 🚀 Functional
✔️ CRUD for lead , agent , category ✔️ Assign a lead to an agent  ✔️ Send a message to a lead via Celery  ✔️ Register and manage agents ✔️ Assign leads to agents ✔️ Reset password via email ✔️ Group customers by category ✔️ Filter leads by category

## 🛠️ Technologies
- **Django**
- **PostgreSQL**
- **Celery + Redis**
- **Celery**

## 📦 Installation and local launch

1️⃣ Cloning the repository
```bash
git clone https://github.com/AMuhailo/Django-CRM-Lead-Management.git
cd Django-CRM-Lead-Management.git
```

2️⃣ Virtual environment
```bash
python -m venv venv
source venv/bin/activate # for macOS and Linux
venv\Scripts\activate # for Windows
```

3️⃣ Installing dependencies
```bash
pip install -r requirements.txt
```

4️⃣ Setting Environment Variables
To run locally, you need to create an .env file in the root folder:
```bash
ENVIRONMENT=development
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/lead_db
REDIS_URL=redis://localhost:6379/0
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-password
```
⚠️ Don`t upload .env to GitHub!
It needs to be added to .gitignore.

5️⃣ Starting the server
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
The site is now available at http://127.0.0.1:8000.

## ⚡Launching Celery
To allow Celery to run tasks in the background, start it like this:
```bash
celery -A myshop worker --loglevel=info
```

## 🔗 Useful commands
💾 Creating a database backup
```bash
python manage.py dumpdata --indent=2 --output=shop/fixtures/db_backup.json
```

♻️ Database recovery
```bash
python manage.py loaddata db_backup.json
```

## 📩 Contacts
If you have any questions, suggestions, problems with the project, ideas or proposals - please contact
📧 Email: amuhailo25@gmail.com
👨‍💻 GitHub: AMuhailo