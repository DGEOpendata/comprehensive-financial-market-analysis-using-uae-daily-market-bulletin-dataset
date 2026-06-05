python
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
dataset_url = "path_to_dataset/Daily_Bulletins_11.xlsx"
data = pd.read_excel(dataset_url)

# Display the first few rows of the dataset
print("Dataset Preview:")
print(data.head())

# Feature of interest: Market Capitalization Analysis
# Calculate total market capitalization
total_market_cap = data['Market Capitalization (AED)'].sum()
print(f"Total Market Capitalization: {total_market_cap} AED")

# Calculate percentage change for each company
data['Percentage Change'] = data['Closing Price'].pct_change() * 100
print("Percentage Change Computed:")
print(data[['Company Name', 'Percentage Change']].head())

# Visualize sector performance
sectors = data.groupby('Sector')['Sector Performance'].mean()
sectors.plot(kind='bar', title='Average Sector Performance')
plt.ylabel('Performance (%)')
plt.xlabel('Sector')
plt.show()

# Save the processed data for further use
output_file = "processed_market_data.xlsx"
data.to_excel(output_file, index=False)
print(f"Processed data saved to {output_file}")
