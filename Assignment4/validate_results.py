import pandas as pd
import glob
import os

# Paths
input_file = "Assignment4/Data/test_inference_data.csv"  # Use the same input file as your mapreduce script
output_files = glob.glob("output/error_counts/part-*.csv")  # Find all output files

# Load the input data
if not os.path.exists(input_file):
    print(f"Input file {input_file} not found!")
    exit(1)

input_data = pd.read_csv(input_file)

# Filter rows where 'inference_result' is 'wrong'
filtered_data = input_data[input_data['inference_result'] == "wrong"]

# Group by 'producer_id' and count occurrences
expected_counts = filtered_data.groupby('producer_id').size().reset_index(name='count')

# Load and merge the output data
if not output_files:
    print(f"No output files found in 'output/error_counts/'!")
    exit(1)

output_data = pd.concat([pd.read_csv(f) for f in output_files], ignore_index=True)

# Compare the expected and actual results
validation = pd.merge(expected_counts, output_data, on='producer_id', how='outer', suffixes=('_expected', '_actual'))

# Check for mismatches
validation['match'] = validation['count_expected'] == validation['count_actual']
mismatches = validation[~validation['match']]

if mismatches.empty:
    print("Validation successful! All counts match.")
else:
    print("Validation failed. Mismatched counts:")
    print(mismatches)

