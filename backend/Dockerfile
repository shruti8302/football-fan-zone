# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable for Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Copy the rest of the backend code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Run the seed script to populate the database, then start the Flask app
CMD ["sh", "-c", "python seed.py && flask run --host=0.0.0.0 --port=5000"]
