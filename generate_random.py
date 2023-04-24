import random
import pandas as pd
num_records = 100

# Define the range for random values
min_value = 60
max_value = 100

# Create a list of dates for the records
dates = pd.date_range('2022-01-01', periods=num_records, freq='D')

# Generate random values for blood pressure, heart rate, and temperature
blood_pressure = [random.randint(min_value, max_value)
                  for i in range(num_records)]
heart_rate = [random.randint(min_value, max_value) for i in range(num_records)]
temperature = [random.uniform(97.0, 99.0) for i in range(num_records)]

# Create a dictionary with the generated data
data = {'Date': dates,
        'Blood Pressure': blood_pressure,
        'Heart Rate': heart_rate,
        'Temperature': temperature}

# Create a pandas DataFrame from the dictionary
df = pd.DataFrame(data)

# Print the generated data
print(df.head())
