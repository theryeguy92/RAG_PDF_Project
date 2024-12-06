import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Step 1: Initialize Spark session
spark = SparkSession.builder \
    .appName("InferenceErrorCount") \
    .getOrCreate()

# Step 2: Get input file from command-line arguments (for batch processing)
if len(sys.argv) != 2:
    print("Usage: python inference_mapreduce.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]

# Step 3: Load data (you can replace this with database connection logic)
data = spark.read.csv(input_file, header=True, inferSchema=True)

# Step 4: Apply MapReduce to count "wrong" inferences per producer
result = data.filter(col("inference_result") == "wrong") \
    .groupBy("producer_id") \
    .count()

# Step 5: Save results
result.write.csv("output/error_counts", header=True, mode="overwrite")

# Step 6: Stop Spark session
spark.stop()

print("MapReduce completed. Results saved to 'output/error_counts'.")


