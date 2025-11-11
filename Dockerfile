#base image
FROM python:3.11-slim

#enev setup
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#dir setup
WORKDIR /app

#dependencies
RUN apt-get update && apt-get install -y \
    libmariadb-dev \
    libmariadb-dev-compat \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


COPY . /app/

#run file
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "greensteps.wsgi:application", "--bind", "0.0.0.0:8000"]
