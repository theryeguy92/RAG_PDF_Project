# Use Python 3.9 image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Capy the current directory contents into the container
COPY . /app

# Install necessary dependencies
RUN pip install kafka-python

# Command to run Flask app
CMD ["python", "iot_producer.py"]