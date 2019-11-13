from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
                                  )
from .models import Lug


class LugListView(ListView):
    model = Lug
    template_name = 'lugs/home.html'
    context_object_name = 'lugs'
    ordering = ['-date_added']
    paginate_by = 25

class LugsByUserListView(ListView):
    model = Lug
    template_name = 'lugs/lugs_by_user.html'
    context_object_name = 'lugs'
    paginate_by = 25

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Lug.objects.filter(added_by=user).order_by('-date_added')

class LugDetailView(DetailView):
    model = Lug
    context_object_name = 'lug'

class LugCreateView(LoginRequiredMixin, CreateView):
    # TODO limit user's LUG to 3
    model = Lug
    fields = [
        'name',
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
        'city',
        'description',
        'cover_image',
        'website',
        'gettogether_page',
        'youtube_channel',
        'twitter',
        'facebook',
        'telegram',
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

    def test_func(self):
        lug = self.get_object()
        if self.request.user == lug.added_by:
            return True
        return False


class MyLugsListView(LoginRequiredMixin, ListView): 
    model = Lug
    template_name = 'lugs/my_lugs.html'
    context_object_name = 'lugs'
    paginate_by = 25

    def get_queryset(self):
        current_user = self.request.user
        return Lug.objects.filter(added_by=current_user).order_by('-date_added')


class LugsByCityListView(ListView):
    model = Lug
    template_name = 'lugs/lugs_by_city.html'
    context_object_name = 'lugs'
    paginate_by = 25

    def get_queryset(self):
        city_id = self.kwargs.get('city_id')
        # city = get_object_or_404(Lug, city_id=self.kwargs.get('city_id'))
        lugs = Lug.objects.filter(city_id=city_id).order_by('-date_added')
        return lugs


@login_required
def joinLug(request, slug, method=['POST', 'GET']):
    user = request.user.profile
    lug = get_object_or_404(Lug, slug=slug)
    # in_lug = is_in_lug(user, lug)
    # lug = Lug.objects.get(slug=slug)    
    if request.method == 'POST':
        if user not in lug.profile_set.all():
        # if not in_lug:
            user.lugs.add(lug)
            messages.success(request, f'Your are now a member of this LUG')            
            return redirect('lug-detail', slug=slug)
        else:
            messages.warning(request, f'Your are already a member of this LUG!')
            return redirect('lug-detail', slug=slug)

    return render(request, 'lugs/join_lug.html', {'slug': slug})


@login_required
def leaveLug(request, slug, method=['POST', 'GET']):
    user = request.user.profile
    lug = get_object_or_404(Lug, slug=slug)
    # in_lug = is_in_lug(user, lug)
    if request.method == 'POST':
        if user in lug.profile_set.all():
        # if in_lug:
            user.lugs.remove(lug)
            messages.success(request, f'Your have successfully left this LUG')            
            return redirect('lug-detail', slug=slug)
        else:
            messages.warning(request, f'Your are not a member of this LUG!')
            return redirect('lug-detail', slug=slug)

    return render(request, 'lugs/leave_lug.html', {'slug': slug})


def lugMembersView(request, slug):
    lug = get_object_or_404(Lug, slug=slug)
    members = lug.profile_set.all()

    return render(request, 'lugs/lug_members_list.html', {'lug': lug, 'members': members})

def about(request):
    return render(request, 'lugs/about.html', {'title': 'About Linux LUGs'})