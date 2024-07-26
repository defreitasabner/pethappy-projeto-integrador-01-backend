FROM python:3.11-slim-bullseye
WORKDIR /api
COPY ../api /api/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt