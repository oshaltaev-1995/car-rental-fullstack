# 1. Build Angular
FROM node:18 AS build-frontend
WORKDIR /app
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ .
RUN npm run build -- --configuration production

# 2. Python backend
FROM python:3.11-slim

WORKDIR /app

# Install backend deps
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend
COPY backend ./backend

# Copy frontend build
COPY --from=build-frontend /app/dist/demo/browser ./frontend

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "backend.app:app"]
