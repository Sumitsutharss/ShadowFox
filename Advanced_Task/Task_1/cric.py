# Cricket Fielding Analysis - ShadowFox Internship Task (RR vs GT IPL 2022 Final, 20 Overs)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "fielding_data.csv"
try:
    df = pd.read_csv(file_path)
    print("Fielding dataset loaded successfully:")
    print(df.head())
except FileNotFoundError:
    print("Error: 'fielding_data.csv' not found.")
    exit()

# Select three players for analysis
players = ["Hardik Pandya", "Shubman Gill", "Rashid Khan"]
df = df[df["Player Name"].isin(players)]
print(f"\nAnalyzing players: {players}")

# Define weights for performance metrics
weights = {
    "CP": 1,   # Clean Pick
    "GT": 1,   # Good Throw
    "C": 3,    # Catch
    "DC": -3,  # Dropped Catch
    "ST": 3,   # Stumping
    "RO": 3,   # Run Out
    "MRO": -2, # Missed Run Out
    "DH": 2,   # Direct Hit
}

# Calculate performance score
def calculate_performance(row):
    cp = 1 if row["Pick"] == "Clean Pick" else 0
    gt = 1 if row["Throw"] == "Good Throw" or row["Pick"] == "Good Throw" else 0
    c = 3 if row["Pick"] == "Catch" or "Catch" in row["Short Description"] else 0
    dc = -3 if row["Pick"] == "Drop Catch" else 0
    st = 3 if row["Throw"] == "Stumping" else 0
    ro = 3 if row["Throw"] == "Run Out" else 0
    mro = -2 if row["Throw"] == "Missed Run Out" else 0
    dh = 2 if row["Throw"] == "Direct Hit" or "Direct Hit" in row["Short Description"] else 0
    rs = row["Runs"]
    
    ps = (cp * weights["CP"]) + (gt * weights["GT"]) + (c * weights["C"]) + \
         (dc * weights["DC"]) + (st * weights["ST"]) + (ro * weights["RO"]) + \
         (mro * weights["MRO"]) + (dh * weights["DH"]) + rs
    return ps

# Apply performance score
df["Performance Score"] = df.apply(calculate_performance, axis=1)

# Aggregate scores per player
player_scores = df.groupby("Player Name")["Performance Score"].sum().reset_index()

# Save to Excel
try:
    df.to_excel("fielding_data_with_scores.xlsx", index=False)
    player_scores.to_excel("player_performance_scores.xlsx", index=False)
    print("\nData saved to 'fielding_data_with_scores.xlsx' and 'player_performance_scores.xlsx'")
except Exception as e:
    print(f"Error saving Excel files: {e}")

# Graph 1: Bar Chart of Player Performance Scores
plt.figure(figsize=(8, 5))
sns.barplot(x="Player Name", y="Performance Score", data=player_scores, palette="viridis")
plt.title("Fielding Performance Scores (RR vs GT IPL 2022 Final)")
plt.xlabel("Player Name")
plt.ylabel("Performance Score")
plt.tight_layout()
plt.show()

# Graph 2: Pie Chart of Fielding Actions
fielding_actions = {
    "Clean Pick": df["Pick"].value_counts().get("Clean Pick", 0),
    "Good Throw": df["Pick"].value_counts().get("Good Throw", 0) + df["Throw"].value_counts().get("Good Throw", 0),
    "Catch": df["Pick"].value_counts().get("Catch", 0),
    "Drop Catch": df["Pick"].value_counts().get("Drop Catch", 0),
    "Stumping": df["Throw"].value_counts().get("Stumping", 0),
    "Run Out": df["Throw"].value_counts().get("Run Out", 0),
    "Missed Run Out": df["Throw"].value_counts().get("Missed Run Out", 0),
    "Direct Hit": df["Throw"].value_counts().get("Direct Hit", 0),
    "Fumble": df["Pick"].value_counts().get("Fumble", 0)
}

action_counts = {k: v for k, v in fielding_actions.items() if v > 0}
plt.figure(figsize=(8, 8))
plt.pie(action_counts.values(), labels=action_counts.keys(), autopct='%1.1f%%', colors=sns.color_palette("pastel"), startangle=90)
plt.title("Proportion of Fielding Actions (RR vs GT IPL 2022 Final)")
plt.tight_layout()
plt.show()

# Analysis Report
print("\n=== Fielding Analysis Report (RR vs GT IPL 2022 Final) ===")
print("Top Fielders Based on Performance Score:")
print(player_scores.sort_values(by="Performance Score", ascending=False).to_string(index=False))

print("\nKey Observations:")
for player in players:
    player_data = df[df["Player Name"] == player]
    total_score = player_scores[player_scores["Player Name"] == player]["Performance Score"].values[0]
    runs = player_data["Runs"].sum()
    print(f"\n{player}:")
    print(f"  Total Performance Score: {total_score}")
    print(f"  Runs Saved/Conceded: {runs}")
    print(f"  Actions:\n{player_data[['Short Description', 'Pick', 'Throw', 'Runs']].to_string(index=False)}")
    if total_score > 10:
        print("  Strength: High-impact fielder with significant contributions.")
    elif total_score < 0:
        print("  Improvement: Reduce errors (e.g., fumbles, missed run outs).")
    else:
        print("  Observation: Consistent but room for more impactful plays.")

print("\nSuggestions for Team Improvement:")
print("- Enhance catching practice to minimize dropped catches.")
print("- Improve throw accuracy to convert more run-out opportunities.")
print("- Position high-scorers like Rashid Khan in critical fielding zones.")

print("\nAnalysis Completed! Check Excel files and visualizations.")
