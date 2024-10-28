
teams = {
    'New York Knicks': [22, 7, 6, 9, 45],
    'Los Angeles Lakers': [23, 14, 5, 4, 55],
    'Chicago Bulls': [21, 10, 6, 5, 50]
}

for team, stats in teams.items():
    print(f"{team.upper()} {' '.join(map(str, stats))}")
