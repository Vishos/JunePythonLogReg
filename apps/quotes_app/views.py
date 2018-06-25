from django.shortcuts import render
from ..login_app.models import User
# Create your views here.
def index(request):
    context = {
        'user' : User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'quotes_app/index.html', context)