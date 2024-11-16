from flask import Flask, request, jsonify
from kafka import KafkaProducer
import os

# Set the Flask
app = Flask(__name__)
KAFKA_TOPIC = "pdf_uploads"
KAFKA_SERVER = "vm2:9092"

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

@app.rout('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # Save file locally
    file_path = os.path.join('/uploads', file.filename)
    file.save(file_path)

    # Send message to Kafka
    message = {"file_path": file_path, "file_name": file.filename}
    producer.send(KAFKA_TOPIC, value=str(message).encode('utf-8'))

    return jsonify({"message": "File uploaded and sent to Kafka"}), 200

if __name__ == "__main__":
    os.makedirs('/uploads', exist_ok=True)
    app.run(host="0.0.0.0", port=5000)


