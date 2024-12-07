from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.master("local[*]").appName("Test").getOrCreate()

# Verify Spark context is available
print(f"Spark version: {spark.version}")
