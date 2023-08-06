from django.shortcuts import render, redirect
from .models import Bug

def report_bug(request):
    if request.method == 'POST':
        bug = Bug(
            title=request.POST['title'],
            description=request.POST['description'],
            status=request.POST['status'],
            priority=request.POST['priority'],
            category=request.POST['category']
        )
        bug.save()
        return redirect('home')
    return render(request, 'bugs/report_bug.html')

