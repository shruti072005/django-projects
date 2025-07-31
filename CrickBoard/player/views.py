from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from player.serializers import playerSerializer
from player.models import player
# Create your views here.
class playerinsertview(APIView):
    #insert data
     def post(self, request):
        serializer = playerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"players data saved successfully"},status=201)
        
        return Response(serializer.errors,status=400)

class playerdetailview(APIView):
     
    #get single players data by jr no
     def get(self,request):
        
        jn = request.GET.get('jn')
        if jn:
            try:
                player_obj = player.objects.get(jn=jn)
                serializer = playerSerializer(player_obj)
                return Response(serializer.data, status=200)
            except Exception as e:
                return Response({"error": str(e)}, status=404)
        else:
             return Response({"error": "jercy number is required"}, status=400)
        
    #update single players data by jr no
     def put(self, request):
        jn = request.data.get('jn')
        if jn:
            try:
                player_obj = player.objects.get(jn=jn)
                serializer = playerSerializer(player_obj, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"message": "Player data updated successfully"}, status=200)
                return Response(serializer.errors, status=400)
            except Exception as e:
                return Response({"error": str(e)}, status=404)
        else:
             return Response({"error": "jercy number is required"}, status=400)
        
        #update single players data by jr no
     def patch(self, request):
        jn = request.data.get('jn')
        if jn:
            try:
                player_obj = player.objects.get(jn=jn)
                serializer = playerSerializer(player_obj, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"message": "Player data updated successfully"}, status=200)
                return Response(serializer.errors, status=400)
            except Exception as e:
                return Response({"error": str(e)}, status=404)
        else:
             return Response({"error": "jercy number is required"}, status=400)
        
        #delete single players data by jr no
     def delete(self,request):
        
        jn = request.GET.get('jn')
        if jn:
            try:
                player_obj = player.objects.get(jn=jn)
                player_obj.delete()
                return Response({"message": "Player data deleted successfully"}, status=200)
            except Exception as e:
                return Response({"error": str(e)}, status=404)
        else:
             return Response({"error": "jercy number is required"}, status=400)

class playergetallview(APIView):
    
     def get(self,request):
        print(" GET all players by jn")
        #retrive all players data by jercy no
        players = player.objects.all()
        serializer = playerSerializer(players, many=True)
        return Response(serializer.data, status=200)        
     
class batsmanview(APIView):
    #get all batsman
     def get(self,request):
        print(" GET all batsman")
        batsmen = player.objects.filter(runs__gt=1000)  # Assuming batsmen have more than 1000 runs
        serializer = playerSerializer(batsmen, many=True)
        return Response(serializer.data, status=200)
     
class bowlerview(APIView):
    #get all bowlers
     def get(self,request):
        print(" GET all bowlers")
        bowlers = player.objects.filter(wickets__gt=50)
        serializer = playerSerializer(bowlers, many=True)
        return Response(serializer.data, status=200)

#  Get Players by Team
class PlayersByTeamView(APIView):
     def get(self,request):
        
        teamname= request.GET.get('teamname')
        if teamname:
            try:
                player_obj = player.objects.get(teamname=teamname)
                serializer = playerSerializer(player_obj)
                return Response(serializer.data, status=200)
            except Exception as e:
                return Response({"error": str(e)}, status=404)
        else:
             return Response({"error": "team name is required"}, status=400)
        
#  get players by name
class PlayersByNameView(APIView):
     def get(self, request):

        name = request.GET.get('name')
        if name:
            try:
                player_obj = player.objects.get(name=name)
                serializer = playerSerializer(player_obj)
                return Response(serializer.data, status=200)
            except Exception as e:
                return Response({"error": str(e)}, status=404)
        else:
             return Response({"error": "name is required"}, status=400)
    

#  Team-Wise Aggregated Statistics
# Returns per-team total runs, total wickets, player count.

class TeamStatsView(APIView):
    def get(self, request):
        team_name = request.GET.get('teamname')
        if team_name:
            players = player.objects.filter(teamname=team_name)
            total_runs = sum(player.runs for player in players)
            total_wickets = sum(player.wickets for player in players)
            stats = {
                'teamname': team_name,
                'runs': total_runs,
                'wickets': total_wickets
            }
            return Response(stats, status=200)
        else:
            return Response({"error": "team name is required"}, status=400)

class allteamsview(APIView):
    #get all teams
    def get(self, request):
        teams = player.objects.values_list('teamname', flat=True).distinct()
        return Response(list(teams), status=200)
    
class playerrankview(APIView):
    #get player rank by runs
    def get(self, request):
        jn = request.GET.get('jn')
        if not jn:
            return Response({'error': 'jercy number is required'}, status=400)
        players_qs = player.objects.order_by('-runs')
        rank = 1
        for p in players_qs:
            if str(p.jn) == str(jn):
                return Response({'jn': jn, 'name': p.name, 'rank_by_runs': rank})
            rank += 1
        return Response({'detail': 'Player not found'}, status=404)
    
class playercountview(APIView):
    #get player count by team
    def get(self, request):
        teamname = request.GET.get('teamname')
        if not teamname:
            return Response({'error': 'team name is required'}, status=400)
        count = player.objects.filter(teamname=teamname).count()
        return Response({'teamname': teamname, 'player_count': count}, status=200)
    