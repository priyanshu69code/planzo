# Stage 1: Builder
FROM python:3.13-slim as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install pipenv
RUN pip install --upgrade pip && \
    pip install pipenv

# Copy Pipfile files
COPY Pipfile Pipfile.lock /app/

# Install dependencies
RUN pipenv install --deploy --system

# Stage 2: Runtime
FROM python:3.13-slim

# Create a non-root user
RUN groupadd -r django && useradd -r -g django django

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV HOME=/home/django
ENV APP_HOME=/home/django/web

# Create directory structure
RUN mkdir -p $APP_HOME/staticfiles $APP_HOME/mediafiles

# Install runtime dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends libpq5 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy installed packages from builder stage
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Set work directory
WORKDIR $APP_HOME

# Copy project files
COPY . $APP_HOME

# Adjust ownership to non-root user
RUN chown -R django:django $HOME

# Switch to non-root user
USER django

# Run entrypoint script
ENTRYPOINT ["/home/django/web/entrypoint.prod.sh"]
