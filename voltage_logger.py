import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Simulate 50 voltage measurements
np.random.seed(42)
voltages = 5 + 0.2 * np.random.randn(50)  # around 5V, with some noise

# Create a DataFrame
df = pd.DataFrame({'Measurement #': range(1, 51), 'Voltage (V)': voltages})

# Save to Excel
df.to_excel('voltage_readings.xlsx', index=False)
print("Excel file 'voltage_readings.xlsx' saved.")

# Plot the readings
plt.plot(df['Measurement #'], df['Voltage (V)'], marker='o')
plt.title('Voltage Readings Over Time')
plt.xlabel('Measurement #')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.tight_layout()
plt.savefig('voltage_plot.png')
plt.show()
print("Voltage plot saved as 'voltage_plot.png'.")
