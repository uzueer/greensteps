# ----------------------------
# Dockerfile for Django + MySQL
# ----------------------------
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install system dependencies (for mysqlclient, netcat, etc.)
RUN apt-get update && apt-get install -y \
    gcc \
    pkg-config \
    default-libmysqlclient-dev \
    netcat-traditional \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static automatically during build
RUN python manage.py collectstatic --noinput || true

# Expose Django port
EXPOSE 8000

# Command to run app (with DB wait)
CMD sh -c "echo '⏳ Waiting for database...' && \
    until nc -z db 3306; do echo '🚧 MySQL not ready yet... waiting 3s'; sleep 3; done; \
    echo '✅ MySQL is ready! Running migrations...' && \
    python manage.py migrate && \
    python manage.py collectstatic --noinput && \
    echo '🚀 Starting Gunicorn...' && \
    gunicorn greensteps.wsgi:application --bind 0.0.0.0:8000"
