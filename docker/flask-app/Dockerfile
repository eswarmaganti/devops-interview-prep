# Selecting the base image
FROM python:3.12-slim

# Define Environment Variables
ENV USER=dev

# Set working directory
WORKDIR /app

# Install System Dependencies if needed
RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
  && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt file
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Create a non-root user
RUN useradd -m $USER 
USER $USER

# port details
EXPOSE 8000

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]