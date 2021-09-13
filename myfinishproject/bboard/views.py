from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Bb
from .models import Rubric
from django.views.generic.edit import CreateView
from .forms import BbForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages




def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()

    context = {'bbs': bbs, 'rubrics': rubrics,}
    paginator = Paginator(bbs, 3)  # По 3 статьи на каждой странице.
    page = request.GET.get('page')
    try:
        bbs = paginator.page(page)
    except PageNotAnInteger:

        bbs = paginator.page(1)
    except EmptyPage:
         # Если номер страницы больше, чем общее количество страниц, возвращаем последнюю.
        bbs = paginator.page(paginator.num_pages)


    return render(request, 'bboard/index.html',{'page': page, 'bbs': bbs, 'rubrics': rubrics})


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()


    current_rubric = Rubric.objects.get(pk=rubric_id)


    paginator = Paginator(bbs, 3)  # По 3 статьи на каждой странице.
    page = request.GET.get('page')
    page = request.GET.get('page')
    try:
        bbs = paginator.page(page)
    except PageNotAnInteger:

        bbs = paginator.page(1)
    except EmptyPage:
        # Если номер страницы больше, чем общее количество страниц, возвращаем последнюю.
        bbs = paginator.page(paginator.num_pages)
    return render(request, 'bboard/by_rubric.html',{'page': page, 'bbs': bbs, 'rubrics': rubrics,'current_rubric':current_rubric})


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


