# Use Python 3.9 image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory in the container
COPY . /app

# Flask
RUN pip install flask

# Expose port 5000 for the Flask app
EXPOSE 5000

# Run Flask
CMD ["python", "ml_models_vm3.py"]