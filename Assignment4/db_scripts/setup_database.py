"""
Script to set up the database schema for the inference pipeline.
Creates the 'inference_data' table.
"""

import psycopg2

conn = psycopg2.connect(
    dbname="your_db", user="your_user", password="your_password", host="localhost"
)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE inference_data (
    id SERIAL PRIMARY KEY,
    producer_id VARCHAR(255),
    inference_result BOOLEAN
);
""")
conn.commit()
conn.close()
print("Table created successfully!")

