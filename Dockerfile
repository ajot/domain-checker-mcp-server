FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose the port that the app will run on
EXPOSE 8080

# Command to run the application
CMD gunicorn --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8080 "domain-checker:mcp.app" 