from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StringType

# Step 1: Initialize Spark Streaming session
spark = SparkSession.builder \
    .appName("InferenceErrorCountStreaming") \
    .getOrCreate()

# Step 2: Define Kafka settings
kafka_broker = "YOUR_KAFKA_BROKER_IP:9092"  # Replace with the Kafka broker IP
kafka_topic = "test"  # Replace with the Kafka topic name

# Step 3: Read streaming data from Kafka
streaming_data = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_broker) \
    .option("subscribe", kafka_topic) \
    .load()

# Step 4: Parse the incoming JSON data
schema = StructType() \
    .add("producer_id", StringType()) \
    .add("image_id", StringType()) \
    .add("inference_result", StringType())

parsed_data = streaming_data.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# Step 5: Apply transformations (count "wrong" inferences per producer)
result = parsed_data.filter(col("inference_result") == "wrong") \
    .groupBy("producer_id") \
    .count()

# Step 6: Output results to the console
query = result.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

# Step 7: Await termination
query.awaitTermination()


