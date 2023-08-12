from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Bug
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # If you wish to use token-based auth, generate a token here and return it
            return JsonResponse({'success': True, 'message': 'Usuário logado com sucesso!'})
        else:
            return JsonResponse({'success': False, 'message': 'Credenciais inválidas.'}, status=401)
    
    return JsonResponse({'success': False, 'message': 'Método não permitido.'}, status=405)

@csrf_exempt
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'success': True, 'message': 'Usuário deslogado com sucesso!'})
    
    return JsonResponse({'success': False, 'message': 'Método não permitido.'}, status=405)

@login_required
@csrf_exempt
def report_bug(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        bug = Bug(
            title=data['title'],
            description=data['description'],
            status=data['status'],
            priority=data['priority'],
            category=data['category_id']
        )
        bug.save()

        return JsonResponse({'success': True, 'message': 'Bug reportado com sucesso!'})

    return JsonResponse({'success': False, 'message': 'Método não permitido.'}, status=405)

