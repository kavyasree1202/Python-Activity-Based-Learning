
# Sports Tournament Ranking System

teams = {}

# Number of teams
n = int(input("Enter number of teams: "))

# Initialize team statistics
for i in range(n):
    name = input(f"Enter team {i + 1} name: ")
    teams[name] = {
        "played": 0,
        "won": 0,
        "drawn": 0,
        "lost": 0,
        "scored": 0,
        "conceded": 0,
        "points": 0
    }

# Number of matches
matches = int(input("Enter number of matches: "))

# Process match results
for i in range(matches):
    print(f"\nMatch {i + 1}")

    team1 = input("Enter first team: ")
    team2 = input("Enter second team: ")

    if team1 not in teams or team2 not in teams or team1 == team2:
        print("Invalid team names! Match ignored.")
        continue

    score1 = int(input(f"Enter {team1} score: "))
    score2 = int(input(f"Enter {team2} score: "))

    if score1 < 0 or score2 < 0:
        print("Invalid scores! Match ignored.")
        continue

    t1 = teams[team1]
    t2 = teams[team2]

    t1["played"] += 1
    t2["played"] += 1

    t1["scored"] += score1
    t1["conceded"] += score2

    t2["scored"] += score2
    t2["conceded"] += score1

    if score1 > score2:
        t1["won"] += 1
        t2["lost"] += 1
        t1["points"] += 3

    elif score2 > score1:
        t2["won"] += 1
        t1["lost"] += 1
        t2["points"] += 3

    else:
        t1["drawn"] += 1
        t2["drawn"] += 1
        t1["points"] += 1
        t2["points"] += 1

# Calculate goal difference
for name in teams:
    teams[name]["difference"] = (
        teams[name]["scored"] - teams[name]["conceded"]
    )

# Ranking policy:
# 1. Total points (descending)
# 2. Goal difference (descending)
# 3. Goals scored (descending)
# 4. Team name (alphabetical)

ranking = sorted(
    teams.items(),
    key=lambda item: (
        -item[1]["points"],
        -item[1]["difference"],
        -item[1]["scored"],
        item[0].lower()
    )
)

# Display final standings
print("\n========== TOURNAMENT RANKINGS ==========")
print(
    f"{'Rank':<6}{'Team':<15}{'P':<5}{'W':<5}"
    f"{'D':<5}{'L':<5}{'GF':<6}{'GA':<6}"
    f"{'GD':<6}{'Pts':<5}"
)

for rank, (name, stats) in enumerate(ranking, start=1):
    print(
        f"{rank:<6}{name:<15}{stats['played']:<5}"
        f"{stats['won']:<5}{stats['drawn']:<5}"
        f"{stats['lost']:<5}{stats['scored']:<6}"
        f"{stats['conceded']:<6}"
        f"{stats['difference']:<6}{stats['points']:<5}"
    )

print("\nRanking completed successfully!")

