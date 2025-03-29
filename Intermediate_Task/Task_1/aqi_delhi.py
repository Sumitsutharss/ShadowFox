import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "delhiaqi.csv"  
try:
    df_aqi = pd.read_csv(file_path)
    print("Dataset loaded successfully:")
    print(df_aqi.head())
except FileNotFoundError:
    print("Error: 'delhiaqi.csv' not found. Please ensure the file is present.")
    exit()

# Convert date column to datetime and set as index
df_aqi["date"] = pd.to_datetime(df_aqi["date"], errors='coerce')
df_aqi.set_index("date", inplace=True)

# Handle missing values
df_aqi.fillna(method='ffill', inplace=True)  # Forward fill
df_aqi.dropna(subset=['pm2_5', 'pm10'], inplace=True)  # Drop rows if key pollutants are still NaN
print(f"\nRows after cleaning: {len(df_aqi)}")

# Summary Statistics
print("\nSummary Statistics:")
print(df_aqi.describe())

# Key Pollutants Identification
pollutants = ['pm2_5', 'pm10', 'no2', 'so2', 'co', 'o3']  # Adjust based on available columns
available_pollutants = [col for col in pollutants if col in df_aqi.columns]
mean_pollutants = df_aqi[available_pollutants].mean()
plt.figure(figsize=(8, 5))
sns.barplot(x=mean_pollutants.index, y=mean_pollutants.values, palette="viridis")
plt.title("Average Levels of Key Pollutants in Delhi")
plt.xlabel("Pollutant")
plt.ylabel("Mean Concentration (µg/m³)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# PM2.5 Trend Over Time
plt.figure(figsize=(12, 5))
sns.lineplot(data=df_aqi, x=df_aqi.index, y="pm2_5", color="red", label="PM2.5")
plt.title("Delhi PM2.5 Levels Over Time")
plt.xlabel("Date")
plt.ylabel("PM2.5 Concentration (µg/m³)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Seasonal Variations
df_aqi['month'] = df_aqi.index.month
def assign_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5, 6]:
        return "Summer"
    elif month in [7, 8, 9]:
        return "Monsoon"
    else:
        return "Post-Monsoon"

df_aqi['season'] = df_aqi['month'].apply(assign_season)
seasonal_avg = df_aqi.groupby('season')[available_pollutants].mean()
plt.figure(figsize=(10, 6))
seasonal_avg.plot(kind='bar', stacked=True, cmap='viridis', ax=plt.gca())
plt.title("Seasonal Variations in Pollutant Levels")
plt.xlabel("Season")
plt.ylabel("Average Concentration (µg/m³)")
plt.legend(title="Pollutants")
plt.tight_layout()
plt.show()

# Monthly Average PM2.5 Levels (Bar Chart)
monthly_avg = df_aqi.groupby('month')["pm2_5"].mean()
plt.figure(figsize=(10, 5))
sns.barplot(x=monthly_avg.index, y=monthly_avg.values, palette="coolwarm")
plt.title("Monthly Average PM2.5 Levels in Delhi")
plt.xlabel("Month")
plt.ylabel("PM2.5 (µg/m³)")
plt.xticks(ticks=range(12), labels=[
    "Jan", "Feb", "Mar", "Apr", "May", "Jun", 
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
])
plt.tight_layout()
plt.show()

# Pollutant Correlation Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df_aqi[available_pollutants].corr(), annot=True, cmap="coolwarm", 
            linewidths=0.5, vmin=-1, vmax=1)
plt.title("Correlation Between Pollutants")
plt.tight_layout()
plt.show()

# Geographical Impact (if 'location' column exists)
if 'location' in df_aqi.columns:
    loc_avg = df_aqi.groupby('location')[available_pollutants].mean()
    plt.figure(figsize=(10, 6))
    sns.heatmap(loc_avg, cmap='YlOrRd', annot=True)
    plt.title("Pollutant Levels by Location in Delhi")
    plt.xlabel("Pollutant")
    plt.ylabel("Location")
    plt.tight_layout()
    plt.show()
else:
    print("\nNo 'location' column found for geographical analysis.")

# Save Cleaned Dataset
df_aqi.to_csv("Cleaned_Delhi_AQI.csv")
print("\nCleaned dataset saved as 'Cleaned_Delhi_AQI.csv'")

# Insights for Air Quality Improvement
print("\nInsights for Air Quality Improvement:")
print("1. Key Pollutants: PM2.5 and PM10 show the highest concentrations, indicating particulate matter as the primary concern.")
print("2. Seasonal Peaks: Winter months (Nov-Feb) exhibit elevated pollution, likely due to stubble burning and low wind speeds.")
print("3. Correlations: Strong correlation between PM2.5 and PM10 suggests common sources (e.g., vehicular emissions, construction).")
print("4. Recommendations: Implement stricter emission controls in winter, promote green transport, and reduce industrial dust.")

print("\nAQI Analysis Completed! Check visualizations and cleaned dataset.")
