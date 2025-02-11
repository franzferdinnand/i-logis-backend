# 🚚 i-Logis Backend  
📦 **A backend for a logistics platform connecting drivers and volunteers for cargo transportation**  

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)  
![Django](https://img.shields.io/badge/Django-5.1.5-green.svg)  
![Docker](https://img.shields.io/badge/Docker-✔️-blue)  
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-✔️-yellow)  
 

🚧 **Project is under active development** 🚧  

## 🚀 Project Overview  
**i-Logis Backend** is the server-side application for a logistics platform that connects drivers and volunteers for cargo transportation. The project uses **Django REST Framework (DRF)** for API development and **PostgreSQL** as the primary database.  

### 📌 Main Features:
- 🔐 **User management system** (registration, login, profile management)  
- 🚚 **Cargo management** (create, update, retrieve)  
- 📍 **Cargo tracking system**  
- 🔔 **Notifications for cargo status updates**  
- 📊 **Analytics and reporting on cargo deliveries**  

## ⚙️ Tech Stack  
- **Language**: Python 3.9+  
- **Framework**: Django 4.0, Django REST Framework  
- **Database**: PostgreSQL  
- **Caching**: Redis  
- **Task Queue**: Celery + RabbitMQ  
- **Authentication**: JWT (SimpleJWT)  
- **Docker containers**  
- **CI/CD**: GitHub Actions  

## 🔧 Installation & Setup  

### Clone the repository  
```bash
git clone https://github.com/franzferdinnand/i-logis-backend.git
cd i-logis-backend
```

### Set up a virtual environment  
```bash
python3 -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
```

### Install dependencies  
```bash
pip install -r requirements.txt
```

### Apply migrations  
```bash
python manage.py migrate
python manage.py createsuperuser  # Create a superuser
python manage.py runserver
```

### Run with Docker  
```bash
docker-compose up --build
```

## 📡 API Endpoints  
**Main API endpoints (ViewSets for Users & Cargos):**  

| Method   | URL                   | Description                 |
|----------|------------------------|-----------------------------|
| `POST`   | `/api/auth/login/`     | User login (JWT)           |
| `POST`   | `/api/auth/register/`  | User registration          |
| `GET`    | `/api/users/`          | Retrieve all users         |
| `GET`    | `/api/users/{id}/`     | Retrieve a specific user   |
| `PATCH`  | `/api/users/{id}/`     | Update user details        |
| `DELETE` | `/api/users/{id}/`     | Delete a user             |
| `GET`    | `/api/cargos/`         | Retrieve all cargo         |
| `POST`   | `/api/cargos/`         | Create a new cargo item    |
| `GET`    | `/api/cargos/{id}/`    | Retrieve cargo details     |
| `PATCH`  | `/api/cargos/{id}/`    | Update cargo status        |
| `DELETE` | `/api/cargos/{id}/`    | Delete a cargo item       |

📌 **API Documentation:**  
```bash
http://localhost:8000/api/docs/
```

## 🛠 Testing  
Run tests before deployment:  
```bash
pytest
```

## 📜 License  
This project is licensed under the **MIT License**.  
