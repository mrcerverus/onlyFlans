from django.shortcuts import redirect, render, get_object_or_404
from web.models import Flan
from .forms import ContactForm, CustomUserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request,'index.html', {'flanes':flanes_publicos})

def about(request):
    return render(request, 'about.html', {})

@login_required
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

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    next_page = '/'

def flan_details(request, flan_id):
    flan = get_object_or_404(Flan,pk=flan_id)
    return render(request, 'flan_detail.html', {'flan': flan})

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('indice')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)