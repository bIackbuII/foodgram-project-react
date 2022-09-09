FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

# RUN python3 manage.py migrate

# RUN python3 manage.py load_ingr

CMD ["gunicorn", "backend.wsgi:application", "--bind", "0:8000" ]