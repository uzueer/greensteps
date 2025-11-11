GreenSteps - Carbon Footprint Tracker

A full-stack **two-tier web application** designed to help users **track, visualize, and analyze** their personal carbon emissions.
GreenSteps promotes sustainable living by providing **data-driven insights** into daily activities’ environmental impact.

---

## 🛠️ Tech Stack

* **Backend**: Django 5.2.8 (Python)
* **Database**: MySQL (MariaDB)
* **Frontend**: Django Templates, HTML5, CSS3, JavaScript
* **Visualization**: Chart.js
* **Web Server**: Nginx (Reverse Proxy)
* **Containerization**: Docker, Docker Compose
* **Deployment Environment**: AWS EC2 (Ubuntu 22.04)
* **Networking**: Docker Bridge Network with persistent Volumes

---

## ⚙️ Features

### 👤 User Management

* Registration, login/logout, and authentication
* Personal user dashboards

### 🌍 Carbon Tracking

* Track across multiple categories:

  * 🚗 Transportation
  * ⚡ Energy
  * 🍔 Food
  * 🗑️ Waste
* Each activity uses real CO₂ emission factors
* Calculates total emissions in real time

### 📊 Analytics Dashboard

* Interactive visualizations with Chart.js
* Emission breakdown by category and time
* Daily emission trends and sustainability insights

### 🧰 Admin Panel

* Manage users, categories, and emission factors
* Add or modify new activity types
* Full control via Django’s built-in admin interface

---

## 🗄️ Database Schema

### Models

1. **Category** – Activity categories with icons and colors
2. **EmissionFactor** – CO₂ emission rate per activity
3. **Activity** – User-logged activities and calculated emissions

---

## 🚀 Deployment Guide (Docker + Nginx + AWS EC2)

### 🧱 1. Prerequisites

Ensure the following are installed on your system (EC2 instance recommended):

```bash
sudo apt update && sudo apt install docker.io docker-compose -y
```

Create a directory for your app:

```bash
mkdir ~/greensteps && cd ~/greensteps
```

Clone your repository:

```bash
git clone https://github.com/uzueer/GreenSteps.git
cd GreenSteps
```

---

### 🐳 2. Docker Setup


#### docker-compose.yml

```

---

### ⚡ 3. Build and Run Containers

```bash
sudo docker-compose build
sudo docker-compose up -d
```

View logs:

```bash
sudo docker-compose logs -f
```

Access the app:

```
http://<your-ec2-public-ip>
```

---

### ☁️ 4. Deploy on AWS EC2

1. **Launch EC2 instance**

   * Ubuntu 22.04 LTS
   * Instance type: t2.micro or higher
   * Open inbound ports **80** (HTTP) and **22** (SSH)

2. **SSH into EC2**

   ```bash
   ssh -i your-key.pem ubuntu@<your-ec2-ip>
   ```

3. **Install Docker and Docker Compose**
   (as shown above)

4. **Clone and deploy**

   ```bash
   git clone https://github.com/uzueer/GreenSteps.git
   cd GreenSteps
   sudo docker-compose up -d
   ```

5. Visit your app:

   ```
   http://<ec2-public-ip>
   ```

---

## 🧠 Development Setup (Local)

If you prefer local development:

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start local server
python manage.py runserver
```

---

## 🔍 Key Features Explained

### 💨 Real-Time Emission Calculation

* Uses pre-loaded CO₂ emission factors per activity
* Formula:

  ```
  Total CO₂ = Quantity × CO₂ per Unit
  ```

### ⚡ Dynamic Form Loading (AJAX)

* Automatically loads emission factors for selected category
* Displays correct unit and calculates live estimates

### 📱 Responsive Design

* Mobile-first layout with adaptive grid and flexible design

---

## 🧾 Sample Emission Factors

| Activity       | CO₂ Emission | Unit    |
| -------------- | ------------ | ------- |
| Car (Gasoline) | 0.2392 kg    | per km  |
| Electricity    | 0.4330 kg    | per kWh |
| Beef           | 27.0 kg      | per kg  |
| Bus Travel     | 0.1043 kg    | per km  |

---

## 🧭 Future Enhancements

* 🌐 Public API for third-party integrations
* 📈 Export reports (CSV/PDF)
* ♻️ Carbon offset recommendations
* 📱 Mobile App (Flutter)
* 🔒 JWT-based API authentication

---

## 🪪 License

This project is created for **educational purposes** under an open-source license.
Feel free to fork and enhance with attribution.

---

## 👨‍💻 Author

**Syed Uzair**
GreenSteps | A Carbon Footprint Tracker 🌍
Built with ❤️ using **Django, MySQL, Docker, and AWS**


