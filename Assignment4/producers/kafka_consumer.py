from kafka import KafkaConsumer
import psycopg2
import json

# Connect to the database
conn = psycopg2.connect(
    dbname="your_db",
    user="your_user",
    password="your_password",
    host="localhost"
)
cursor = conn.cursor()

# Kafka Consumer
consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='consumer-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Consume messages and insert into database
for message in consumer:
    data = message.value
    producer_id = data.get('producer_id')
    inference_result = data.get('inference_result')

    # Insert data into the table
    cursor.execute(
        """
        INSERT INTO inference_data (producer_id, inference_result)
        VALUES (%s, %s)
        """,
        (producer_id, inference_result)
    )
    conn.commit()

    print(f"Inserted message: {data}")

cursor.close()
conn.close()
