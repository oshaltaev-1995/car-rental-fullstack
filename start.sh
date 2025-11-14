#!/bin/sh
set -e

echo "Starting Gunicorn..."
gunicorn -w 4 -b 0.0.0.0:5000 app:app --chdir /app/backend &

echo "Starting Nginx..."
nginx -g "daemon off;"
