from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='129.114.25.163:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Simulate data from 5G devices
data = [
    {"producer_id": "5G_Producer_1", "image_id": "img_101", "inference_result": "wrong"},
    {"producer_id": "5G_Producer_2", "image_id": "img_102", "inference_result": "correct"},
]

for record in data:
    producer.send('test', record)
    print(f"Sent: {record}")
    time.sleep(1)
