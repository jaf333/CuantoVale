# En juego/views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Jugador
import random

def juego(request):
    jugadores = list(Jugador.objects.all())
    jugador_izquierda = random.choice(jugadores)
    jugador_derecha = random.choice([j for j in jugadores if j != jugador_izquierda])
    return render(request, 'juego.html', {
        'jugador_izquierda': jugador_izquierda,
        'jugador_derecha': jugador_derecha
    })

def verificar_respuesta(request):
    if request.method == 'POST':
        jugador_izquierda_id = request.POST.get('jugador_izquierda_id')
        jugador_derecha_id = request.POST.get('jugador_derecha_id')
        respuesta = request.POST.get('respuesta')

        jugador_izquierda = Jugador.objects.get(id=jugador_izquierda_id)
        jugador_derecha = Jugador.objects.get(id=jugador_derecha_id)

        if respuesta == 'superior' and jugador_derecha.valor_mercado > jugador_izquierda.valor_mercado:
            return JsonResponse({'resultado': 'correcto'})
        elif respuesta == 'inferior' and jugador_derecha.valor_mercado < jugador_izquierda.valor_mercado:
            return JsonResponse({'resultado': 'correcto'})
        elif respuesta == 'igual' and jugador_derecha.valor_mercado == jugador_izquierda.valor_mercado:
            return JsonResponse({'resultado': 'correcto'})
        else:
            return JsonResponse({'resultado': 'incorrecto'})

    return redirect('juego')
