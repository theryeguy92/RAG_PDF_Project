CREATE TABLE inference_data (
    id SERIAL PRIMARY KEY,
    producer_id VARCHAR(255),
    inference_result BOOLEAN
);
