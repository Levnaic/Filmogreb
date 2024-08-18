# Use the official Python image as a base
FROM python:3-alpine3.12

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Install Nginx
RUN apk update && apk add nginx

# Copy Nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Remove the default Nginx server definition and use ours
RUN rm /etc/nginx/conf.d/default.conf

# Expose ports for Flask and Nginx
EXPOSE 5000 80

# Define environment variable to tell Flask we are in production
ENV FLASK_ENV=production

# Start both Nginx and Flask using a supervisor or a script
CMD ["sh", "-c", "python app.py & nginx -g 'daemon off;'"]
