"""
Given the following inputs:
- <game_data> is a list of dictionaries, with each dictionary representing a player's shot attempts in a game. The list can be empty, but any dictionary in the list will include the following keys: gameID, playerID, gameDate, fieldGoal2Attempted, fieldGoal2Made, fieldGoal3Attempted, fieldGoal3Made, freeThrowAttempted, freeThrowMade. All values in this dictionary are ints, except for gameDate which is of type str in the format 'MM/DD/YYYY'
- <true_shooting_cutoff> is the minimum True Shooting percentage value for a player to qualify in a game. It will be an int value >= 0.
- <player_count> is the number of players that need to meet the <true_shooting_cutoff> in order for a gameID to qualify. It will be an int value >= 0.

Implement find_qualified_games to return a list of unique qualified gameIDs in which at least <player_count> players have a True Shooting percentage >= <true_shooting_cutoff>, ordered from most to least recent game.
"""
def calculate_true_shooting_percentage(player:dict) -> float:
	fieldGoal2_attempted = player['fieldGoal2Attempted']
	fieldGoal2_made = player ['fieldGoal2Made']
	fieldGoal3_attempted = player ['fieldGoal3Attempted']
	fieldGoal3_made =  player['fieldGoal3Made']
	freeThrow_attempted = player['freeThrowAttempted']
	freeThrow_made = player['freeThrowMade']


	points = 

def find_qualified_games(game_data: list[dict], true_shooting_cutoff: int, player_count: int) -> list[int]:
	
	pass