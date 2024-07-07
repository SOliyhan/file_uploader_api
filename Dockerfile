# Use a lightweight Python base image
FROM python:3.12.1-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy project code
COPY . .

# Expose the port used by your Django application (usually 8000)
EXPOSE 8000

# Run gunicorn as the main process
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "csv_project.wsgi:application"]
