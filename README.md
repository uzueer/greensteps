# 🚀 GreenSteps – 2-Tier Full-Stack Application Deployed on AWS (Django + MySQL + Docker + Nginx)

**GreenSteps** is a containerized **2-Tier Web Application** that promotes sustainability by tracking users’ daily carbon footprint.
It follows a **DevOps-based deployment architecture** using **Docker, Docker Compose, Nginx reverse proxy**, and **AWS EC2** for cloud hosting.

This project demonstrates a complete **DevOps pipeline** — from development and containerization to production deployment on AWS.

---

## 🏗️ Architecture Overview

### 🧩 Application Architecture (2-Tier)

**Tier 1 – Application Layer (Django + Gunicorn):**
- Handles user requests and business logic
- Served through Gunicorn WSGI server inside a Docker container

**Tier 2 – Database Layer (MySQL):**
- Stores user data, categories, activities, and emission factors
- Persistent storage handled by **Docker Volumes**

**Reverse Proxy Layer (Nginx):**
- Serves static files and routes traffic to the Django container
- Exposed via port 80 to the public internet

**Infrastructure Layer:**
- Hosted on **AWS EC2 (Ubuntu 24.04 LTS)**
- Managed with **Docker Compose**
- Communication over **Docker Bridge Network**

---

## 🌍 Live Deployment

🔗 **Live Demo:** [http://13.127.113.33](http://13.127.113.33)
🔑 **Admin Panel:** [http://13.127.113.33/admin](http://13.127.113.33)

---

## 🧠 Project Description

GreenSteps empowers users to take meaningful steps toward sustainability by tracking CO₂ emissions from daily activities such as transportation, electricity, and food consumption.

Users can:
✅ Log eco-related activities
✅ View total CO₂ footprint
✅ Analyze emission patterns
✅ Manage categories and emission factors through the admin panel

---

## 🧩 Tech Stack

| Layer | Technology |
|--------|-------------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Django 5 (Python 3.11) |
| **Database** | MySQL 8 |
| **Server** | Gunicorn + Nginx |
| **Containerization** | Docker & Docker Compose |
| **Hosting** | AWS EC2 (Ubuntu 24.04 LTS) |
| **Persistence** | Docker Volumes |
| **Networking** | Docker Bridge Network |

---

## 🗂️ Project Structure

```

greensteps/
├── greensteps/              # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tracker/                 # Core carbon tracking app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── static/
├── nginx/
│   └── nginx.conf
├── Dockerfile
├── docker-compose.yaml
├── requirements.txt
├── .env.example
└── README.md

````

---

## ⚙️ Environment Variables

Create a `.env` file in the root directory based on the example below:

```bash
DJANGO_SECRET_KEY=your_secret_key_here
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=*

DB_ENGINE=django.db.backends.mysql
DB_NAME=greensteps_db
DB_USER=greensteps_user
DB_PASSWORD=greensteps_pass
DB_HOST=db
DB_PORT=3306
````

> ⚠️ Keep `.env` out of version control — only commit `.env.example`.

---

## 🐳 Docker Deployment Steps (AWS EC2)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/syeduzair/greensteps.git
cd greensteps
cp .env.example .env
```

### 2️⃣ Build & Start Containers

```bash
docker compose up -d --build
```

### 3️⃣ Verify Container Status

```bash
docker ps
```

✅ `greensteps_db` → (healthy)
✅ `web` → Django + Gunicorn
✅ `greensteps_nginx` → Reverse Proxy

### 4️⃣ Initialize Django Setup

```bash
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
docker compose exec web python manage.py collectstatic --noinput
docker compose restart nginx
```

---

## 🧮 Database Schema

| Table                    | Description                          |
| ------------------------ | ------------------------------------ |
| `auth_user`              | Django built-in users                |
| `tracker_category`       | Categories (Transport, Energy, etc.) |
| `tracker_emissionfactor` | CO₂ factors for each activity        |
| `tracker_activity`       | User-logged activity records         |

### Example Data

```sql
INSERT INTO tracker_category (name, icon, color) VALUES
('Transportation', '🚗', '#1E90FF'),
('Electricity', '⚡', '#FFD700'),
('Food', '🍔', '#FF6347'),
('Waste', '🗑️', '#32CD32'),
('Water', '💧', '#00BFFF');

INSERT INTO tracker_emissionfactor (category_id, activity_name, co2_per_unit, unit) VALUES
(1, 'Car travel', 0.271, 'kg/km'),
(1, 'Flight (short haul)', 0.255, 'kg/km'),
(2, 'Power usage', 0.475, 'kg/kWh'),
(3, 'Beef consumption', 27.0, 'kg/kg'),
(3, 'Chicken consumption', 6.9, 'kg/kg'),
(4, 'Plastic waste', 1.5, 'kg/kg'),
(5, 'Water usage', 0.35, 'kg/litre');
```

---

## 🧠 Application Features

✅ User authentication & registration
✅ Track activities by quantity and date
✅ Real-time CO₂ emission calculation
✅ Admin panel for category & emission management
✅ Deployed via Docker Compose with persistent data
✅ Production-ready with Nginx reverse proxy and Gunicorn

---

## 🧰 Common Docker & DevOps Commands

| Command                               | Description                        |
| ------------------------------------- | ---------------------------------- |
| `docker compose up -d --build`        | Build & run all containers         |
| `docker compose down -v`              | Stop & remove containers & volumes |
| `docker compose logs -f`              | Live logs of all services          |
| `docker exec -it web bash`            | Access Django container            |
| `docker volume ls`                    | List Docker volumes                |
| `docker network ls`                   | List Docker networks               |
| `docker stats`                        | Monitor running containers         |
| `docker system prune -a --volumes -f` | Clean unused Docker data           |

---

## 🖼️ Screenshots

### 🌍 Login Page

![Login Page](screenshots/login.png)

### 📊 Dashboard

![Dashboard](screenshots/dashboard.png)

### ➕ Add New Activity

![Add Activity](screenshots/add.png)

### 🧮 Admin Panel

![Admin Panel](screenshots/admin.png)

---

### 🧰 Docker & Deployment Proof

#### 🧱 Containers, Volumes & Networks

![Docker Info](screenshots/docker_info.png)

#### ⚙️ Resource Usage

![Docker Stats](screenshots/docker_stats.png)

#### 🟢 Docker Service Status

![Docker Status](screenshots/docker_status.png)

---




## 👨‍💻 Author

**Syed Uzair**

---

## 💚 Acknowledgment

This project supports **UN Sustainable Development Goal 13: Climate Action**.

> *“The first step to a sustainable future is knowing your impact — GreenSteps helps you take that step.”*

---

## 🛠️ Tags

`#DevOps` `#AWS` `#Docker` `#Nginx` `#Django` `#MySQL` `#Gunicorn` `#CloudDeployment` `#Sustainability`

---

## ⭐ Support the Project

If you liked this project:

* 🌟 Star the repository
* 🍴 Fork & explore
* 💬 Share feedback
* 🚀 Try it live at [http://13.127.113.33](http://13.127.113.33)

---

````

