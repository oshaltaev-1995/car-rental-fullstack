# 1 — Angular build
FROM node:18 AS build-frontend
WORKDIR /app
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ .
RUN npm run build -- --configuration production

# 2 — Python backend + Nginx
FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y nginx && \
    apt-get clean

WORKDIR /app

# Install backend dependencies FIRST
COPY backend/requirements.txt /app/backend/requirements.txt
RUN pip install --no-cache-dir -r /app/backend/requirements.txt

# Now copy backend code (без venv!)
COPY backend /app/backend

# Copy Angular build
COPY --from=build-frontend /app/dist/demo/browser/ /var/www/html/

# Correct nginx path
COPY nginx.conf /etc/nginx/conf.d/default.conf

COPY start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 80
CMD ["/start.sh"]
