from django.shortcuts import render


def homeDash(request):
    context = {}
    return render(request, 'dashboard/dashboard.html', context)
