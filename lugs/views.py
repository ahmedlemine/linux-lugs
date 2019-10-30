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
    # TODO add a test_func to limit user's LUG to 3
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
        'website',
        'contact_person',
        'contact_info',
        'donate_link',
        'cover_image'
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
        # user = get_object_or_404(User, username=self.kwargs.get('username'))
        current_user = self.request.user
        return Lug.objects.filter(added_by=current_user).order_by('-date_added')


def about(request):
    return render(request, 'lugs/about.html', {'title': 'About Linux LUGs'})