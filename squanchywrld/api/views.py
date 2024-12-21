from rest_framework import viewsets
from .models import Game
from .serializers import GameSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer



from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Game, Performance, Moment, TeamScoreStats
from .serializers import GameSerializer

@api_view(['POST'])
def create_game(request):
    if request.method == 'POST':
        serializer = GameSerializer(data=request.data)
        
        if serializer.is_valid():
            # Salvar o jogo principal
            game = serializer.save()
            
            # Salvar performances associadas ao jogo
            performances_data = request.data.get('performances', [])
            for performance_data in performances_data:
                Performance.objects.create(game=game, **performance_data)
            
            # Salvar momentos associados ao jogo
            moments_data = request.data.get('moments', [])
            for moment_data in moments_data:
                Moment.objects.create(game=game, **moment_data)
            
            # Salvar estatísticas da pontuação da equipe associadas ao jogo
            team_score_stats_data = request.data.get('team_score_stats', {})
            TeamScoreStats.objects.create(game=game, **team_score_stats_data)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
