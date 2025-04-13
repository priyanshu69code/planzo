FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/planzo

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY Pipfile Pipfile.lock /app/
RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --system --deploy

COPY . /app/

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
