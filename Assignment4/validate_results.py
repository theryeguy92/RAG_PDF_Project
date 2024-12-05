import pandas as pd
import os

# Paths
input_file = "Assignment4/Data/inference_data.csv"
output_file = "Assignment4/output/error_counts/part-00000-a1ae0f0f-951c-4940-8ef3-7205073ac44f-c000.csv"

# Load the input data
if not os.path.exists(input_file):
    print(f"Input file {input_file} not found!")
    exit(1)

input_data = pd.read_csv(input_file)

# Filter rows where 'inference_result' is 'wrong'
filtered_data = input_data[input_data['inference_result'] == "wrong"]

# Group by 'producer_id' and count occurrences
expected_counts = filtered_data.groupby('producer_id').size().reset_index(name='count')

# Load the output data
if not os.path.exists(output_file):
    print(f"Output file {output_file} not found!")
    exit(1)

output_data = pd.read_csv(output_file)

# Compare the expected and actual results
validation = pd.merge(expected_counts, output_data, on='producer_id', suffixes=('_expected', '_actual'))

# Check for mismatches
mismatches = validation[validation['count_expected'] != validation['count_actual']]

if mismatches.empty:
    print("Validation successful! All counts match.")
else:
    print("Validation failed. Mismatched counts:")
    print(mismatches)
