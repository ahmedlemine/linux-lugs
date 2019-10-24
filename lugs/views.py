from django.shortcuts import render
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView
                                  )
from .models import Lug


# def home(request):
#     context = {
#         'lugs': Lug.objects.all()
#     }
#     return render(request, 'lugs/home.html', context)

class LugListView(ListView):
    model = Lug
    template_name = 'lugs/home.html'
    context_object_name = 'lugs'
    oerdering = ['-date_added']

class LugDetailView(DetailView):
    model = Lug

class LugCreateView(CreateView):
    model = Lug
    fields = ['name', 'country', 'province', 'city', 'description', 'website', 'contact_person', 'contact_info', 'donate_link']

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request, 'lugs/about.html', {'title': 'About'})