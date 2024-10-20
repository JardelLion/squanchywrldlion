# Exemplo de process_and_save_data que espera uma lista de jogos
from api.models import Game
from api.models import Goal

def process_and_save_data(game_data):
    for game_info in game_data:
        try:
            # Verifique se os campos essenciais existem
            if 'game' not in game_info or 'moments' not in game_info:
                print(f"Dados faltando em: {game_info}")
                continue

            # Extraia informações do jogo
            home_team, away_team = game_info['game'].split(' - ')
            result = game_info['result']



            # Verifique se o jogo já existe
            if Game.objects.filter(date=convert_date(game_info['data']), home_team=home_team.strip(), away_team=away_team.strip()).exists():
                #print(f"O jogo {home_team} vs {away_team} já existe no banco de dados.")
                continue

            # Crie e salve o jogo
            
            game = Game.objects.create(
                date= convert_date(game_info['data']),
                home_team=home_team.strip(),
                away_team=away_team.strip(),
                result=result
            )



            # Salve os momentos (gols)
            for moment in game_info['moments']:
                Goal.objects.create(
                    game=game,
                    time=moment['time'],
                    goal=moment['goal'],
                    who_scored=moment['who_scored']
                )

        except Exception as e:
            print(f"Erro ao processar o jogo {game_info['game']}: {e}")


from datetime import datetime

def convert_date(date_str):
    try:
        # Tenta analisar a data no formato atual
        return datetime.strptime(date_str, "%d %b").replace(year=datetime.now().year).date()
    except ValueError:
        print(f"Erro ao converter a data: {date_str}")
        return None
