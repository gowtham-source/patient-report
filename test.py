import pandas as pd
import numpy as np

# Define number of days
num_days = 30

# Define list of medications
medications = ['Medication A', 'Medication B',
               'Medication C', 'Medication D', 'Medication E']

# Define dosage dataframe
dosage_df = pd.DataFrame(np.random.randint(0, 3, size=(
    num_days, len(medications))), columns=medications)

# Define time dataframe
time_df = pd.DataFrame({'hour': np.random.randint(
    0, 24, size=num_days), 'minute': np.random.randint(0, 60, size=num_days)})

# Combine dosage and time dataframes
df = pd.concat([dosage_df, time_df], axis=1)

# Define date range
date_rng = pd.date_range(start='1/1/2023', end='1/30/2023', freq='D')

# Convert date range to dataframe
date_df = pd.DataFrame(date_rng, columns=['date'])

# Merge date dataframe with existing dataframe
df = pd.merge(date_df, df, left_index=True, right_index=True)

df.to_csv('medication.csv', index=False)
