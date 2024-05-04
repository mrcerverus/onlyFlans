from django.shortcuts import redirect, render
from web.models import Flan
from .forms import ContactForm

# Create your views here.
def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request,'index.html', {'flanes':flanes_publicos})

def about(request):
    return render(request, 'about.html', {})

def welcome(request):
    flanes_publicos = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'flanes':flanes_publicos})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto_exitoso')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})

def contact_view_exito(request):
    return render(request, 'contacto_exitoso.html', {})