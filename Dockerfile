FROM python:3.9.22-alpine3.21
LABEL maintainer="https://github.com/priyanshu69code"

ENV PYTHONUNBUFFERED 1

# Install GDAL dependencies and other required packages
RUN apk update && \
    apk add --no-cache \
    postgresql-client \
    build-base \
    postgresql-dev \
    musl-dev \
    linux-headers \
    gdal-dev \
    && python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt && \
    apk del build-base postgresql-dev musl-dev linux-headers gdal-dev

# Copy application code after installing dependencies
COPY ./planzo /planzo
COPY ./scripts /scripts

WORKDIR /planzo
EXPOSE 8000

USER root

# Set up permissions for the app user
RUN addgroup -S app && adduser -S -H -G app app && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R app:app /vol && \
    chmod -R 775 /vol && \
    chmod -R +x /scripts

# Switch to 'app' user after setting up permissions
ENV PATH="/scripts:/py/bin:$PATH"
USER app

CMD ["run.sh"]
