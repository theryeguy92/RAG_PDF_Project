from kafka import KafkaConsumer
from pymongo import MongoClient
import json

KAFKA_TOPIC = "pdf_uploads"
KAFKA_SERVER = "vm2:9092"

mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["pdf_database"]
collection = db["pdf_collection"]

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_SERVER,
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='database_consumer'
)

for message in consumer:
    data = eval(message.value.decode('utf-8'))
    file_path = data['file_path']
    file_name = data['file_name']
    
    # Placeholder for actual PDF text extraction
    extracted_text = f"Text content of {file_name}"
    collection.insert_one({"file_name": file_name, "content": extracted_text})

    print(f"Saved {file_name} to MongoDB")
