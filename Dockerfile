# Use the official Python image.
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app directory into the container
COPY ./app /app

# Expose port 80 for the Flask app
EXPOSE 80

# Define environment variable for Flask
ENV FLASK_APP=app.py

# Run the Flask app on port 80
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=80"]
