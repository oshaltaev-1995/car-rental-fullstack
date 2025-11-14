# 1. Build Angular
FROM node:18 AS build-frontend
WORKDIR /app
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ .
RUN npm run build -- --configuration production

# 2. Backend + Nginx
FROM python:3.11-slim

RUN apt-get update && apt-get install -y nginx && apt-get clean

WORKDIR /app

# Install dependencies
COPY backend/requirements.txt ./backend/requirements.txt
RUN pip install --no-cache-dir -r backend/requirements.txt

# Copy backend
COPY backend/ ./backend/

# Copy Angular build
COPY --from=build-frontend /app/dist/demo/browser/ /var/www/html/

# REPLACE default nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy startup script
COPY start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 80

CMD ["/start.sh"]
