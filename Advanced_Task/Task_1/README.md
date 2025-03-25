🚀 Project Overview
Fielding plays a crucial role in cricket, often influencing the match outcome. This project evaluates the fielding performance of key players in the IPL 2022 Final (RR vs GT) by analyzing key actions like:
✅ Catches
✅ Throws
✅ Run-outs
✅ Stumpings

Using Performance Score Calculation and data visualization, we gain insights into each player's defensive contributions.

📊 Dataset Information
📁 File: fielding_data.csv
🏆 Match: IPL 2022 Final - Rajasthan Royals vs Gujarat Titans

Columns in the Dataset
Column Name	Description
Player Name	Name of the fielder
Pick	Type of pickup (Clean Pick, Catch, Drop, etc.)
Throw	Type of throw (Run Out, Direct Hit, etc.)
Short Desc.	Description of the fielding action
Runs Saved	Runs saved or conceded (+ for saved, - for conceded)
🔥 Key Players Analyzed
🎯 Hardik Pandya
🎯 Shubman Gill
🎯 Rashid Khan

Each player's fielding actions were assessed using a weighted performance score.

🎯 Performance Metrics
We assigned weights to different fielding actions to calculate a Performance Score for each player.

Fielding Action	Weightage
Catch	10
Run-out	12
Stumping	8
Direct Hit	15
Dropped Catch	-5
⚙️ Implementation
1️⃣ Data Cleaning & Processing (Handled missing values & formatted dataset)
2️⃣ Exploratory Data Analysis (EDA) (Plotted trends, distributions)
3️⃣ Performance Scoring (Calculated weighted fielding performance)
4️⃣ Visualization (Bar charts, heatmaps for better insights)

📊 Results & Insights
📌 Key findings from the analysis:
✅ Player X had the highest fielding score of XX points.
✅ Player Y had the most run-saving actions.
✅ Team Z’s fielding made a crucial difference in the match.

Graphs & Visuals 📊:
(Insert plots like bar charts, heatmaps, etc.)

🚀 How to Use
📥 Installation
bash
Copy
Edit
git clone https://github.com/sumitsutharss/Cricket-Fielding-Analysis.git
cd Cricket-Fielding-Analysis
pip install -r requirements.txt
▶️ Running the Analysis
bash
Copy
Edit
python analysis.py
🤝 Contributing
Contributions are welcome! If you'd like to improve this project, follow these steps:
1️⃣ Fork the repo
2️⃣ Create a new branch (feature-branch)
3️⃣ Commit changes
4️⃣ Create a Pull Request

📜 License
This project is open-source under the MIT License.
