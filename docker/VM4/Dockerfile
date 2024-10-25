# Use Python 3.9 image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install necessary dependencies
RUN pip install kafka-python pymongo

# Command to run the consumer script
CMD ["python", "db_consumer_vm4.py"]
