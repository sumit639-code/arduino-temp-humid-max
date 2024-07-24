import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
csv_file = 'sensor_readings.csv'  # Update with your actual file path
data = pd.read_csv(csv_file)

# Convert the 'timestamp' column to datetime
data['timestamp'] = pd.to_datetime(data['Date'])
data['Temperature (C)'] = data['Temperature (C)'].str.replace('C', '').astype(float)
data['Humidity (%)'] = data['Humidity (%)'].str.replace('%', '').astype(float)
# Extract the date from the timestamp (optional, if you want to analyze by date)
data['date'] = data['timestamp'].dt.date

# Plot the relationship between temperature and humidity
plt.figure(figsize=(10, 5))
sns.scatterplot(x=data['Humidity (%)'], y=data['Temperature (C)'], hue=data['date'], palette='coolwarm', alpha=0.7)
plt.xlabel('Humidity (%)')
plt.ylabel('Temperature (°C)')
plt.title('Effect of Humidity on Temperature')
plt.legend(title='Date', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()

# Calculate and print the correlation coefficient
correlation = data['Temperature (C)'].corr(data['Humidity (%)'])
print(f"Correlation between temperature and humidity: {correlation:.2f}")