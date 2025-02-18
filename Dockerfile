FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install necessary dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy your script and the .env file to the container
COPY . .

# Command to run your app
CMD ["python", "app.py"]
