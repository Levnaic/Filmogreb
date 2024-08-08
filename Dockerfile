# Use the official Python image as a base
FROM python:3-alpine3.12

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable to tell Flask we are in production
ENV FLASK_ENV=production

# Run app.py when the container launches
CMD ["python", "app.py"]