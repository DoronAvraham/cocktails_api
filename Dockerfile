# Use an official Python runtime as a base image
FROM python:3.12.0-slim

ENV DB_USER=cocktailsapi \
    DB_HOST=10.26.160.3

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app/

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Specify the command to run on container start
CMD ["python", "main.py"]
