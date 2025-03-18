## __📞Lead Management System__
![Django](https://img.shields.io/badge/Django-4.2-darkgreen?style=for-the-badge) ![Python](https://img.shields.io/badge/Python-3.12.9-blue?style=for-the-badge)
## Description project
Lead Management System is a CRM system for managing potential clients and agents, 
which includes lead creation, agent management, sending messages via Celery, 
password reset system, client categorization and full CRUD functionality. 
Docker Images with containers (Redis, PostgreSQL, Nginx, Web, Celery) and deployment on RailWay.

🚀Deploy on Railway
The project is deployed on Railway. To check the operation of the site, go to the link: 🔗[Lead Management](https://lead-crm.up.railway.app/)


## 🚀 Functional
✔️ CRUD for lead , agent , category ✔️ Assign a lead to an agent ✔️ Send a message to a lead via Celery ✔️ Register and manage agents ✔️ Assign leads to agents ✔️ Reset password via email ✔️ Group customers by category ✔️ Filter leads by category ✔️ Docker & Docker Compose ✔️ Deploy on Railway



## 🛠️ Technologies
- **Django**
- **PostgreSQL**
- **Celery + Redis**
- **Celery**
- **Nginx**
- **Docker & Docker Compose**
- **Railway.app**

## 📋 Prerequisites
Ensure you have the following installed:
- **Docker**
- **Docker Compose**
- **Railway CLI (optional, for deployment)**

## 📦 Installation and local launch
1️⃣ Cloning the repository
```bash
git clone https://github.com/AMuhailo/Django-CRM-Lead-Management.git
cd Django-CRM-Lead-Management.git
```

2️⃣ Virtual environment
```bash
python -m venv venv
source venv/bin/activate    # for macOS and Linux
venv/Scripts/activate       # for Windows
```

3️⃣ Installing dependencies
```bash
pip install -r requirements.txt
```

4️⃣ Setting Environment Variables
To run locally, you need to create an .env file in the root folder:
```bash
ENVIRONMENT=local
SECRET_KEY=your-secret-key
DATABASE_URL=your-database-url
REDIS_URL=your-redis-url
```
⚠️ Don`t upload .env to GitHub!
It needs to be added to .gitignore.

5️⃣ Starting the server (without Docker)
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
The site is now available at http://127.0.0.1:8000.

## ⚡Launching Celery
To allow Celery to run tasks in the background, start it like this (without Docker):
```bash
celery -A myshop worker --loglevel=info
```

6️⃣ Build and run the project with Docker Compose:
```bash
docker-compose up --build
```

## 🐋 Docker Containers
The project uses the following containers:
- **web**: Django application
- **db**: PostgreSQL database
- **redis**: Redis server for Celery tasks
- **celery**: Celery worker for background tasks
- **nginx**: Reverse proxy for serving static files and routing traffic


## 🔗 Useful commands
💾 Creating a database backup
```bash
python manage.py dumpdata --indent=2 --output=lead/fixtures/data_json.json
```

♻️ Database recovery
```bash
python manage.py loaddata data_json.json
```

## 📩 Contacts
If you have any questions, suggestions, problems with the project, ideas or proposals - please contact
📧 Email: amuhailo25@gmail.com
👨‍💻 GitHub: AMuhailo
