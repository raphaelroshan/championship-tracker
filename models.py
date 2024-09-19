from flask import flash

# store team details for retrieval and ranking, can be regenerated from the txt files to simulate persistent storage
team_details = {} # teamName. : {reg_date, group_number, matches_played, outcomes : {wins, losses, draws}}, json storage

def update_registration(team_name, reg_date, group_number):
    # Check if team already exists in team_details
    if team_name in team_details:
        # Update existing team's details
        team_details[team_name]['reg_date'] = reg_date
        team_details[team_name]['group_number'] = group_number
        flash(f"{team_name} updated.", "success")
    else:
        # Register new team
        team_details[team_name] = {
            'reg_date': reg_date,
            'group_number': group_number,
            'matches_played': 0,
            'outcomes': {
                'wins': 0,
                'losses': 0,
                'draws': 0
            },
            'total_points': 0,
            'alternate_points': 0
        }
        flash(f"New {team_name} registered.", "success")
    return


def update_results(team_a_name, team_b_name, team_a_goals, team_b_goals):
    if team_a_name not in team_details and team_b_name not in team_details:
        flash(f"Both {team_a_name} and {team_b_name} are not registered. Please register both teams first.", "error")
        return

    if team_a_name not in team_details:
        flash(f"{team_a_name} is not registered. Please register {team_a_name} first.", "error")
        return
    
    if team_b_name not in team_details:
        flash(f"{team_b_name} is not registered. Please register {team_b_name} first.", "error")
        return

    # Retrieve team details
    team_a = team_details.get(team_a_name)
    team_b = team_details.get(team_b_name)

    # Update matches played
    team_a['matches_played'] += 1
    team_b['matches_played'] += 1

    # Calculate outcomes and points
    if team_a_goals > team_b_goals:
        # Team A wins
        team_a['outcomes']['wins'] += 1
        team_b['outcomes']['losses'] += 1
        team_a['total_points'] += 3
        team_a['alternate_points'] += 5
        team_b['alternate_points'] += 1

    elif team_a_goals < team_b_goals:
        # Team B wins
        team_b['outcomes']['wins'] += 1
        team_a['outcomes']['losses'] += 1
        team_b['total_points'] += 3
        team_b['alternate_points'] += 5
        team_a['alternate_points'] += 1

    else:
        # Draw
        team_a['outcomes']['draws'] += 1
        team_b['outcomes']['draws'] += 1
        team_a['total_points'] += 1
        team_b['total_points'] += 1
        team_a['alternate_points'] += 3
        team_b['alternate_points'] += 3
    flash(f"The match between {team_a_name} and {team_b_name} has been recorded with score {team_a_goals} - {team_b_goals}.", "success")
    return

def clear_data():
    team_details.clear()
    return

def search(team_name):
    return team_details.get(team_name)

def calculate_rankings():
    return sorted(team_details.items(), key=lambda x: (x[1]['total_points'], x[1]['alternate_points']), reverse=True)