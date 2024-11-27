#### Writing this Python Code to read the 180 file and concating
import os
import glob
import pandas as pd

# Define the path to the Downloads folder
downloads_folder = os.path.expanduser('~/Downloads')
print(downloads_folder)

# Create a pattern to match files starting with 'driver_details_2W'
pattern = os.path.join(downloads_folder, 'driver_details_2W*.csv')
print(pattern)

# Use glob to find all matching CSV files
files = glob.glob(pattern)

# Initialize an empty list to hold the DataFrames
dataframes = []

# Read each file and append the DataFrame to the list
for file in files:
    df = pd.read_csv(file)
    print(df.head(1))
    dataframes.append(df)

# Concatenate all DataFrames into a single DataFrame
combined_df = pd.concat(dataframes, ignore_index=True)

# Optionally, save the combined DataFrame to a new CSV file
# combined_df.to_csv(os.path.join(downloads_folder, 'combined_driver_details.csv'), index=False)

print("Concatenation complete. Combined DataFrame shape:", combined_df.shape)