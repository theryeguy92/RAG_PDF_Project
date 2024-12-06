from kafka import KafkaProducer
import json
import time

# Kafka Configuration
KAFKA_BROKER = "localhost:9092"  # Replace with your Kafka broker address
TOPIC_NAME = "inference_results"  # Define the topic name

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Simulate sending inference results
for i in range(10):
    message = {
        "producer_id": f"producer_{i % 3 + 1}",  # Rotate between producer IDs
        "inference_result": "wrong" if i % 2 == 0 else "correct",
        "timestamp": time.time()
    }
    producer.send(TOPIC_NAME, value=message)
    print(f"Sent: {message}")
    time.sleep(1)  # Simulate some delay between messages

producer.flush()
producer.close()
