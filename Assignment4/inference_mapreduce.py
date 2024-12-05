from pyspark.sql import SparkSession

# Step 1: Initialize Spark session
spark = SparkSession.builder \
    .appName("InferenceErrorCount") \
    .getOrCreate()

# Step 2: Load data
# Replace 'data/inference_data.csv' with your actual file path or database connection
data = spark.read.csv("Assignment4/Data/inference_data.csv", header=True, inferSchema=True)

# Step 3: MapReduce to count errors per producer
# Filtering for rows where 'inference_result' is 'wrong'
result = data.filter(data["inference_result"] == "wrong") \
             .groupby("producer_id") \
             .count()

# Step 4: Save results
# Save to output folder
result.write.mode("overwrite").csv("Assignment4/output/error_counts", header=True)

print("MapReduce completed. Results saved to 'output/error_counts'.")

# Step 5: Stop Spark session
spark.stop()
