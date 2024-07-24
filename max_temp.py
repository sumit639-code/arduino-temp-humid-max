import pandas as pd

# Read the input CSV file
input_file = 'sensor_readings.csv'  # Replace with your input file path
output_file = 'max_temperature_per_day.csv'  # Replace with your desired output file path

# Load the data into a DataFrame
df = pd.read_csv(input_file)

# Ensure the date column is in datetime format
df['date'] = pd.to_datetime(df['Date'])

if 'Temperature (C)' in df.columns:
    # Group by date and find the maximum temperature for each day
    max_temp_per_day = df.groupby(df['date'].dt.date)['Temperature (C)'].max().reset_index()

    # Rename the columns for clarity
    max_temp_per_day.columns = ['date', 'max_temperature']

    # Write the result to a new CSV file
    max_temp_per_day.to_csv(output_file, index=False)

    print(f"Max temperatures per day have been written to {output_file}")
else:
    print("Error: 'temperature' column not found in the CSV file.")