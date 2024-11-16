from kafka import KafkaConsumer
from kafka import KafkaProducer
from transformers import pipeline

KAFKA_QUERY_TOPIC = "user_queries"
KAFKA_RESPONSE_TOPIC = "bot_responses"
KAFKA_SERVER = "vm2:9092"

consumer = KafkaConsumer(
    KAFKA_QUERY_TOPIC,
    bootstrap_servers=KAFKA_SERVER,
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='chatbot'
)

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

for message in consumer:
    query_data = eval(message.value.decode('utf-8'))
    question = query_data['question']
    context = query_data['context']  # Retrieved from the database in VM4
    
    answer = qa_pipeline(question=question, context=context)
    response = {"answer": answer['answer']}
    
    producer.send(KAFKA_RESPONSE_TOPIC, value=str(response).encode('utf-8'))
