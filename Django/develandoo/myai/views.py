from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Document
from .forms import DocumentForm

from .machine_learning.core import DataAnalayzer
ai = DataAnalayzer()

def home(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save()
            ai.make_predictions(pk=doc.id)
            return redirect('info')
    else:
        form = DocumentForm()
    return render(request, 'home.html', {'form': form})


def info(request):
    documents = Document.objects.all()
    return render(request, 'info.html', { 'documents': documents })
