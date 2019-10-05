from django.shortcuts import render
from .forms import HashForm
from hash.models import Hash
import hashlib

# Create your views here.


def home(request):
    if request.method == "POST":
        form = HashForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            try:
                hash = Hash.objects.get(name=name)
                form = HashForm()
                return render(request, 'home.html', {'form': form, 'hash': hash})
            except Hash.DoesNotExist:
                hash = Hash()
                hash.name = name
                hash.encoding = hashlib.sha256(
                    name.encode('utf-8')).hexdigest()
                hash.save()
                form = HashForm()
                return render(request, 'home.html', {'form': form, 'hash': hash})
        else:
            note = "Not Available. Wrong text entered. Try Again"
            return render(request, 'home.html', {'form': form, 'note': note})

    else:
        form = HashForm()
        return render(request, 'home.html', {'form': form})
