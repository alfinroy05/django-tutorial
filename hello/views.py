from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def printhello(request):
    m={'movie':[{'title':'bromance','released':'yes','rating':'good'},
                 {'title':'daveed','released':'yes','rating':'good'}]}
    return render(request,'printhello.html',m)