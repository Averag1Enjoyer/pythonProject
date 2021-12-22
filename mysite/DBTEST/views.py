from django.shortcuts import render,redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView , UpdateView , DeleteView

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'DBTEST/create.html'
    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'DBTEST/news-delete.html'


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'DBTEST/details_view.html'
    context_object_name = 'article'


def news_home(request):
    news = Articles.objects.order_by('date')
    return render(request,'DBTEST/news_home.html',{'news': news})

def create(request):
    return render(request,'DBTEST/create.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Форма не вірна"


    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request,'DBTEST/create.html',data)

