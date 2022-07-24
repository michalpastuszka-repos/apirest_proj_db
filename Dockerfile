FROM python:3.9.7-slim


WORKDIR /app

COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
HEALTHCHECK --interval=1m --timeout=3s \
    CMD curl -f http://localhost:5000/docs || exit 1
COPY . .