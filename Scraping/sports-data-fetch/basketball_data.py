import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

url = "https://www.basketball-reference.com/teams/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', id='teams_active')
data = []

if table:
    rows = table.find_all('tr')
    for row in rows[1:]:  # Skip the header row
        columns = row.find_all(['th', 'td'])
        if columns:
            row_data = [column.text for column in columns]
            data.append(row_data)

columns = [
    "Franchise", "League", "From", "To", "Years", "Games Played",
    "Wins", "Losses", "Win/Loss %", "Playoffs", "Division", "Conference", "Championships"
]

team_data = []
for row in data:
    team = dict(zip(columns, row))
    team_data.append(team)

# Save as JSON
json_data = json.dumps(team_data, indent=4)
try:
    with open("basketball_teams.json", "w") as json_file:
        json_file.write(json_data)
    print("JSON file 'basketball_teams.json' created successfully.")
except Exception as e:
    print("An error occurred while saving the JSON file:", e)

# Save as CSV using pandas
df = pd.DataFrame(data, columns=columns)
try:
    df.to_csv("basketball_teams.csv", index=False)
    print("CSV file 'basketball_teams.csv' created successfully.")
except Exception as e:
    print("An error occurred while saving the CSV file:", e)
