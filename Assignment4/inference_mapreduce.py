import sys
from pyspark.sql import SparkSession

# Step 1: Initialize Spark session
spark = SparkSession.builder \
    .appName("InferenceErrorCount") \
    .getOrCreate()

# Step 2: Get input file from command-line arguments
if len(sys.argv) != 2:
    print("Usage: python inference_mapreduce.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]

# Load data
data = spark.read.csv(input_file, header=True, inferSchema=True)

# Step 3: MapReduce to count errors per producer
result = data.filter(data["inference_result"] == "wrong") \
             .groupby("producer_id") \
             .count()

# Step 4: Save results
result.write.csv("output/error_counts", header=True, mode="overwrite")


print("MapReduce completed. Results saved to 'output/error_counts'.")

# Step 5: Stop Spark session
spark.stop()

