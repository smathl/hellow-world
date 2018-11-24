from django.http impport HttpResponse
rfom shortcut import redirect

def index(request):
	return HttpResponse('index')

def login(request):
	return redirct('index')
