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
from .forms import LugForm, FindLugByCityForm
from .models import Lug
from cities_light.models import City


# class LugListView(ListView):
    # model = Lug
    # template_name = 'lugs/home.html'
    # context_object_name = 'lugs'
    # ordering = ['-date_added']
    # paginate_by = 25

def LugListView(request):
    lugs = Lug.objects.all().order_by('-date_added')
    query = request.GET.get('q')
    if query:
        lugs = lugs.filter(name__icontains=query)
        if not lugs:
            messages.warning(request, f'Your search returned no result.')
    context = {'lugs': lugs}
    return render(request, 'lugs/home.html', context)


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

# class LugCreateView(LoginRequiredMixin, CreateView):
#     model = Lug
#     fields = [
#         'name',
#         'city',
#         'description',
#         'cover_image',
#         'website',
#         'contact_person',
#         'contact_info',
#         'donate_link'
#         ]

#     def form_valid(self, form):
#         form.instance.added_by = self.request.user
#         return super().form_valid(form)

# class LugUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Lug
#     fields = [
#         'name',
#         'city',
#         'description',
#         'cover_image',
#         'website',
#         'gettogether_page',
#         'youtube_channel',
#         'twitter',
#         'facebook',
#         'telegram',
#         'contact_person',
#         'contact_info',
#         'donate_link'
#         ]

#     def form_valid(self, form):
#         form.instance.added_by = self.request.user
#         return super().form_valid(form)

#     def test_func(self):
#         lug = self.get_object()
#         if self.request.user == lug.added_by:
#             return True
#         return False



@login_required
def createLug(request):
    user = request.user

    if request.method == 'POST':
        form = LugForm(request.POST, request.FILES)
        if form.is_valid():
            new_lug = form.save(commit=False)
            creator = User.objects.filter(username=user.username).first()
            new_lug.added_by = creator
            new_lug.save()
            creator.profile.lugs.add(new_lug)
            form = LugForm()
            messages.success(request, f'Your new LUG has been successfully created.')
            return redirect('lug-detail', slug=new_lug.slug)
        else:
            form = LugForm(request.POST)
    
    form = LugForm()
    context = {
        'form': form,
        'title': 'Add a new Linux LUG' 
        }
    return render(request, 'lugs/create_lug.html', context)


@login_required
def editLug(request, slug):
    lug = get_object_or_404(Lug, slug=slug)
    user = request.user

    if lug.added_by == user:
        if request.method == 'POST':
            form = LugForm(request.POST, request.FILES, instance=lug)
            if form.is_valid():
                form.save()
                messages.success(request, f'Your changes have been saved.')
                return redirect('lug-detail', slug=lug.slug)
            else:
                form = LugForm(request.POST)
    
        form = LugForm(instance=lug)
        return render(request, 'lugs/edit_lug.html', {'form': form, 'lug': lug, 'title': f'Update LUG {lug.name}'})
    else:
        messages.warning(request, f'You can edit only LUGs you have created')
        return redirect('lug-detail', slug=lug.slug)


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


class LugsByCityListView(ListView): #use try/except
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
def joinLug(request, slug):
    profile = request.user.profile
    lug = get_object_or_404(Lug, slug=slug)
 
    if request.method == 'POST':
        if profile not in lug.profile_set.all():
            profile.lugs.add(lug)
            messages.success(request, f'Your are now a member of this LUG')            
            return redirect('lug-detail', slug=slug)
        else:
            messages.warning(request, f'Your are already a member of this LUG!')
            return redirect('lug-detail', slug=slug)

    return render(request, 'lugs/join_lug.html', {'slug': slug, 'title': f'Join LUG {lug.name}' })


@login_required
def leaveLug(request, slug):
    user = request.user
    profile = user.profile
    lug = get_object_or_404(Lug, slug=slug)

    if request.method == 'POST':
        if profile in lug.profile_set.all():
            if lug.added_by == user:
                messages.warning(request, f'You can NOT leave LUGs you created!')            
                return redirect('lug-detail', slug=slug)
            profile.lugs.remove(lug)
            messages.success(request, f'Your have successfully left this LUG')            
            return redirect('lug-detail', slug=slug)
        else:
            messages.warning(request, f'Your are not a member of this LUG!')
            return redirect('lug-detail', slug=slug)

    return render(request, 'lugs/leave_lug.html', {'slug': slug, 'title': f'Leave LUG {lug.name}'})


def lugMembersView(request, slug):
    lug = get_object_or_404(Lug, slug=slug)
    members = lug.profile_set.all()
    context = {'lug': lug, 'members': members, 'title': f'Members of LUG {lug.name}'}

    return render(request, 'lugs/lug_members_list.html', context)


def findLugByCityView(request):
    title = 'Find Nearby LUGs'
    form = FindLugByCityForm()
    query = request.GET.get('city')
    if query:
        lugs = Lug.objects.filter(city=query)
        form = FindLugByCityForm(request.GET)
        context = {'title': title, 'lugs': lugs, 'form': form}
        if not lugs:
            messages.warning(request, f'No LUGs found in this city.')
        return render(request, 'lugs/find_lugs_in_city.html', context)

    context = {
        'form': form,
        'title': title 
        }
    return render(request, 'lugs/find_lugs_in_city.html', context)

def about(request):
    return render(request, 'lugs/about.html', {'title': 'About Linux LUGs'})
