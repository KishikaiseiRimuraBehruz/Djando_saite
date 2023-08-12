from django.shortcuts import render, redirect
from .models import Creators
from .models import New
from .forms import NewForm
from django.views.generic import DetailView, UpdateView, DeleteView
# Create your views here.
def creators(request):
    creat = Creators.objects.order_by('date')#[:1]

    context = {'creat': creat}

    return render(request, 'souce/souce.html', context)
class NewsDetailView(DetailView):
    model = New
    template_name = 'souce/details_view.html'
    context_object_name = 'article'

class NewsDeleteView(DeleteView):
    model = New
    success_url = '/creators/'
    template_name = 'souce/news-delete.html'


class NewsUpdatelView(UpdateView):
    model = New
    template_name = 'souce/create.html'

    form_class = NewForm


def new(request):

    new = New.objects.order_by('date')

    context = {'new': new}

    return render(request, 'souce/new.html', context)

def create(request):
    error = ''
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'У вас не вышла добовить'



    form = NewForm()

    context = {
        'form': form,
        'error': error
    }

    return render(request, 'souce/create.html', context)