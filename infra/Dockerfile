FROM python:3.11-bullseye
WORKDIR /api
COPY ../api /api/
COPY /infra/dev-entrypoint.sh /api/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x /api/dev-entrypoint.sh