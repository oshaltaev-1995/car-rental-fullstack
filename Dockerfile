# Build Angular frontend
FROM node:18 AS build-frontend
WORKDIR /app
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ .
RUN npm run build -- --configuration production

# Python + Nginx base image
FROM python:3.11-slim

# Install nginx
RUN apt-get update && apt-get install -y nginx && apt-get clean

WORKDIR /app

# Install Python dependencies
COPY backend/requirements.txt /app/backend/requirements.txt
RUN pip install --no-cache-dir -r /app/backend/requirements.txt

# Copy backend
COPY backend /app/backend

# Copy Angular built files
COPY --from=build-frontend /app/dist/demo/browser/ /var/www/html/

# Nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Start script
COPY start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 80

CMD ["/start.sh"]
