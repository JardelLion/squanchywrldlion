from last_result import LastResult
from functions.game_information import GameInformation
from team import Team
from performance import Performance
from ppg import PPG, PPGPoints
from simbol import Simbol
from team_scoring_stats import TeamScoringStast
from total_match_goal_static import TotalMatchGoalStatic
import json

url = 'file:///home/jardel-lion-studio/Documents/games/octuber/18/Alaves%20vs%20Valladolid%20H2H%20stats%20preview%20and%20analysis,%202024-2025.html'
    
last_resutl = LastResult(url)
game = GameInformation(url)
team = Team(url)
ppg = PPG(url)
ppg_points = PPGPoints(url)
performance = Performance(url)
#simbol = Simbol(url)
team_scoring = TeamScoringStast(url)
total_match = TotalMatchGoalStatic(url)

id_game = f"{team.get_home()}{team.get_away()} {game.get_name_league()}{game.get_year()}"
import uuid

# Gerar um UUID único
unique_id = str(uuid.uuid4())
unique_id


data = {
        "id": unique_id,
        "id_game": id_game,
        "date": "falta a data",
        "game": f"{team.get_home()} vs {team.get_away()}",
        "home": team.get_home(),
        "away": team.get_away(), 
        "season": game.get_year(),
        "league": game.get_name_league(),
        "hour_game": "22:00",
        "simbol": {
            "home": 'hom',
            "away": 'awy'
        },
        "last_game":{
            "home": last_resutl.get_home,
            "away": last_resutl.get_away
            },
        "pgg": {
            "home": ppg.get_home_ppg,
            "home_total": ppg.get_home_total_ppg,
            "away": ppg.get_away_ppg,
            "away_total": ppg.get_away_total_ppg,
            "points": {
                "home": {
                    "gp": ppg_points.get_home_point_gp,
                    "w": ppg_points.get_home_point_win,
                    "d": ppg_points.get_home_point_draw,
                    "l": ppg_points.get_home_point_lose,
                    "total": {
                        "gp": ppg_points.get_home_point_gp_total,
                        "w": ppg_points.get_home_point_win_total,
                        "d": ppg_points.get_home_point_draw_total,
                        "l": ppg_points.get_home_point_lose_total
                    }

                },
                "away": {
                   "gp": ppg_points.get_away_point_gp,
                    "w": ppg_points.get_away_point_win,
                    "d": ppg_points.get_away_point_draw,
                    "l": ppg_points.get_away_point_lose,
                    "total": {
                        "gp": ppg_points.get_away_point_gp_total,
                        "w": ppg_points.get_away_point_win_total,
                        "d": ppg_points.get_away_point_draw_total,
                        "l": ppg_points.get_away_point_lose_total
                    }

                }
            }
        },
        "performance": {
            "home": {
                "poins": performance.get_home_points,
                "goal_scored": performance.get_home_scored,
                "goal_conceded": performance.get_home_conceded
            },
            "away": {
                "points": performance.get_away_points,
                "goal_scored": performance.get_away_scored,
                "goal_coneceded": performance.get_away_conceded
            }
        },
        "team_score_stats": {
            "home": {
                "score_average": team_scoring.get_home_scored_average_obj,
                "score_rate": team_scoring.get_home_scoring_rate_obj
            },
            "away": {
                "score_average": team_scoring.get_away_scored_average_obj,
                "score_rate": team_scoring.get_away_scoring_rate_obj
            },
            "bts": team_scoring.get_bts_obj,
            "total_over_1_5": team_scoring.get_total_over_1_5_goals_obj,
            "total_over_2_5": team_scoring.get_total_over_2_5_goals_obj,
            "total_over_3_5": team_scoring.get_total_over_3_5_goals_obj,
            "total_average": team_scoring.get_total_scored_average_obj
        }
        ,
        "total_match_goal": {
            "home": total_match.get_home_obj,
            "away": total_match.get_away_obj
        }
}


# Salvar no arquivo JSON
with open('gamess.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Dados extraídos e salvos no arquivo JSON.")