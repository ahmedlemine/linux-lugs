from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
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
    ordering = ['-date_added']
    paginate_by = 10

class LugsByUserListView(ListView):
    model = Lug
    template_name = 'lugs/lugs_by_user.html'
    context_object_name = 'lugs'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Lug.objects.filter(added_by=user).order_by('-date_added')

class LugDetailView(DetailView):
    model = Lug

class LugCreateView(LoginRequiredMixin, CreateView):
    # TODO limit user's LUG to 3
    model = Lug
    fields = [
        'name',
        'country',
        'province',
        'city',
        'description',
        'cover_image',
        'website',
        'contact_person',
        'contact_info',
        'donate_link'
        ]

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)

class LugUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Lug
    fields = [
        'name',
        'country',
        'province',
        'city',
        'description',
        'cover_image',
        'website',
        'contact_person',
        'contact_info',
        'donate_link'
        ]

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        lug = self.get_object()
        if self.request.user == lug.added_by:
            return True
        return False

class LugDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Lug
    success_url = '/'
    #TODO add a deletion success message
    def test_func(self):
        lug = self.get_object()
        if self.request.user == lug.added_by:
            return True
        return False


class MyLugsListView(LoginRequiredMixin, ListView): 
    model = Lug
    template_name = 'lugs/my_lugs.html'
    context_object_name = 'lugs'
    paginate_by = 10

    def get_queryset(self):
        current_user = self.request.user
        return Lug.objects.filter(added_by=current_user).order_by('-date_added')


class LugsByCityListView(ListView):
    # TODO : look for city in a list of world cities, if not return error
    # fix space issue in city name
    model = Lug
    template_name = 'lugs/lugs_by_city.html'
    context_object_name = 'lugs'
    paginate_by = 10

    def get_queryset(self):
        # lug_city = get_object_or_404(Lug, city=self.kwargs.get('city'))
        # lug_city = Lug.objects.filter(city=self.kwargs.get('city').first()
        lugs = Lug.objects.filter(city=self.kwargs['lug_city']).order_by('-date_added')

        return lugs

class LugsByCountryListView(ListView):
    # TODO : look for city in a list of world countries, if not return error
    # fix space and casing issue in country name
    model = Lug
    template_name = 'lugs/lugs_by_country.html'
    context_object_name = 'lugs'
    paginate_by = 10

    def get_queryset(self):
        # lug_country = Lug country=self.kwargs.get('country'))
        lugs = Lug.objects.filter(country=self.kwargs['country']).order_by('-date_added')
        # lugs = Lug.objects.filter(country=lug_country).order_by('-date_added')
        return lugs

def about(request):
    return render(request, 'lugs/about.html', {'title': 'About Linux LUGs'})