from django.http import HttpResponse 
from django.http import JsonResponse

from django.template import loader
from django.shortcuts import render
from .models import Highscore
import json

def highscores(request):
  allhighscores = Highscore.objects.all().values()
  template = loader.get_template('hs.html')
  context = {
    'allhighscores': allhighscores,
  }
  return HttpResponse(template.render(context, request))

def fullscreen(request):
  template = loader.get_template('game.html')
  return HttpResponse(template.render())

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())

def htp(request):
  template = loader.get_template('htp.html')
  return HttpResponse(template.render())

def game(request):
    return render(request, "game.html")

def check_highscore(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        score = data.get('score', 0)
        time = data.get('time', 0)

        # Get current highest score
        top = Highscore.objects.order_by('-score', 'time').first()
        current_high = top.score if top else 0

        # Determine if this is a new highscore
        new_highscore = score > current_high

        return JsonResponse({'new_highscore': new_highscore, 'current_high': current_high})

def save_highscore(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        score = data.get('score', 0)
        time = data.get('time', 0)
        name = data.get('name', 'Anonymous')

        Highscore.objects.create(score=score, time=time, name=name)

        return JsonResponse({'saved': True})