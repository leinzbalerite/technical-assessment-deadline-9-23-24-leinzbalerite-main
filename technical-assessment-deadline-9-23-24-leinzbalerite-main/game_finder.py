"""
Given the following inputs:
- <game_data> is a list of dictionaries, with each dictionary representing a player's shot attempts in a game. The list can be empty, but any dictionary in the list will include the following keys: gameID, playerID, gameDate, fieldGoal2Attempted, fieldGoal2Made, fieldGoal3Attempted, fieldGoal3Made, freeThrowAttempted, freeThrowMade. All values in this dictionary are ints, except for gameDate which is of type str in the format 'MM/DD/YYYY'
- <true_shooting_cutoff> is the minimum True Shooting percentage value for a player to qualify in a game. It will be an int value >= 0.
- <player_count> is the number of players that need to meet the <true_shooting_cutoff> in order for a gameID to qualify. It will be an int value >= 0.

Implement find_qualified_games to return a list of unique qualified gameIDs in which at least <player_count> players have a True Shooting percentage >= <true_shooting_cutoff>, ordered from most to least recent game.
"""
from datetime import datetime
# Function calculates the truse shooting percentage for a player
def calculate_true_shooting_percentage(player: dict) -> float:
    fieldGoal2_attempted = player['fieldGoal2Attempted']
    fieldGoal2_made = player['fieldGoal2Made']
    fieldGoal3_attempted = player['fieldGoal3Attempted']
    fieldGoal3_made = player['fieldGoal3Made']
    freeThrow_attempted = player['freeThrowAttempted']
    freeThrow_made = player['freeThrowMade']

    # Calculates total points scored
    points = 2 * fieldGoal2_made + 3 * fieldGoal3_made + freeThrow_made

    # Calculate the total number of field goals attempted
    total_fieldGoal_attempted = fieldGoal2_attempted + fieldGoal3_attempted

    # Calculate true shooting percentage
    if total_fieldGoal_attempted + (0.44 * freeThrow_attempted) == 0:
        return 0.0  # Avoid dividing by zero error
    trueShooting_percentage = points / (2 * (total_fieldGoal_attempted + 0.44 * freeThrow_attempted))
    return trueShooting_percentage * 100  # Convert into a percentage

# Function to find qualified games based on their true shooting percentage and min number of players that must qualify
def find_qualified_games(game_data: list[dict], true_shooting_cutoff: int, player_count: int) -> list[int]:
    # Dictionary to store the number of qualified players and gameDate for each gameID
    qualified_games = {}
     # Iterate through each player's game data
    for player in game_data:
        game_id = player['gameID']
        trueShooting_percentage = calculate_true_shooting_percentage(player)
		# Check if each player's true shooting percentage meets or exceeds the shooting cutoff
        if trueShooting_percentage >= true_shooting_cutoff:
            # If the gameID is not in qualified_games, initialize it
            if game_id not in qualified_games:
                qualified_games[game_id] = {
                    'count': 0,
                    'gameDate': player['gameDate'] # Store the game date 
                }
            # add to the count of qualified players for this game
            qualified_games[game_id]['count'] += 1

    # Filter games where the number of qualified players is >= player_count
    result = [
        (game_id, game_info['gameDate']) # Keep track of both game_id and gameDate for sorting
        for game_id, game_info in qualified_games.items() # Iterate over all games
        if game_info['count'] >= player_count # Only keep games that meet the criteria
    ]

    # Sort the result by date in descending order (most recent first)
    result.sort(key=lambda x: datetime.strptime(x[1], '%m/%d/%Y'), reverse=True)

    # Return the list of gameIDs from the sorted result
    return [game_id for game_id, _ in result]
