import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
csv_file = 'sensor_readings.csv'  # Update with your actual file path
data = pd.read_csv(csv_file)
# data.columns = data.columns.str.strip()
print(data['Temperature (C)'])
# Convert the 'timestamp' column to datetime
data['timestamp'] = pd.to_datetime(data['Date'])
data['Temperature (C)'] = data['Temperature (C)'].str.replace('C', '').astype(float)
# Extract the date from the timestamp
data['date'] = data['timestamp'].dt.date

# Group the data by date and calculate the average temperature for each day
average_daily_temperature = data.groupby('date')['Temperature (C)'].mean()

# Print the average daily temperatures
print(average_daily_temperature)

# Plot the average daily temperatures
plt.figure(figsize=(10, 5))
plt.plot(average_daily_temperature.index, average_daily_temperature.values, label='Average Temperature (°C)', color='b', marker='o')
plt.xlabel('Date')
plt.ylabel('Average Temperature (°C)')
plt.title('Average Daily Temperature')
plt.xticks(rotation=45)  # Rotate date labels for better readability
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()






















