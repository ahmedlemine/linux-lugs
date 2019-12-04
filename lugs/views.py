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
from .forms import LugForm,PostForm, FindLugByCityForm
from .models import Lug, Post
from users.models import Profile
from cities_light.models import City


def lugListView(request):
    lugs = Lug.objects.all().order_by('-date_added')
    latest_lugs = lugs[:5]

    context = {'lugs': lugs, 'latest_lugs': latest_lugs}
    return render(request, 'lugs/home.html', context)


class LugsByUserListView(ListView):
    model = Lug
    template_name = 'lugs/lugs_by_user.html'
    context_object_name = 'lugs'
    paginate_by = 25

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Lug.objects.filter(added_by=user).order_by('-date_added')


def lugDetailView(request, slug):
    lug = get_object_or_404(Lug, slug=slug)
    similar_lugs = Lug.objects.filter(city=lug.city)[:3]

    context = {
            'lug': lug,
            'title': f'About LUG: {lug.name}',
            'similar_lugs': similar_lugs,
            }
    return render(request, 'lugs/lug_detail.html', context)


def searchLUGsView(request):
    lugs = ''
    query = request.GET.get('q')
    if query:
        lugs = Lug.objects.filter(name__icontains=query)
        
        if not lugs:
            messages.warning(request, f'Your search \"{query}\" returned no results.')
    context = {
        'lugs': lugs,
        'query': query,
        'title': 'search LUGs'
        }
    return render(request, 'lugs/search_lugs.html', context)

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
        context = {
            'form': form,
            'lug': lug,
            'title': f'Update LUG: {lug.name}'
            }
        return render(request, 'lugs/edit_lug.html', context)
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

'''
        LUG POSTS
'''
def lugPostsListView(request, slug):
    lug = get_object_or_404(Lug, slug=slug)
    posts = Post.objects.filter(lug=lug).order_by('-date_added')
    context = {'lug': lug, 'posts': posts}
    return render(request, 'lugs/lug_posts.html', context)

def lugPostDetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    return render(request, 'lugs/post_detail.html', {'post': post, 'title': f'Post Detail {post.title}'})

@login_required
def createPost(request, slug):
    lug = get_object_or_404(Lug, slug=slug)
    user = request.user

    if lug.added_by == user:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                new_post = form.save(commit=False)
                new_post.lug = lug
                poster = User.objects.filter(username=user.username).first()
                new_post.posted_by = poster
                form.save()
                messages.success(request, f'Your post has been created')
                return redirect('lug-detail', slug=lug.slug)
            else:
                form = PostForm(request.POST)
    
        form = PostForm()
        return render(request, 'lugs/post_create.html', {'form': form, 'lug': lug, 'title': f'Create a Post for LUG {lug.name}'})
    else:
        messages.warning(request, f'You are not allowed to post to this LUG')
        return redirect('lug-detail', slug=lug.slug)

@login_required
def editPost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    if post.posted_by == user:
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                messages.success(request, f'Post updated.')
                return redirect('post-detail', pk=pk)
            else:
                form = PostForm(request.POST)
    
        form = PostForm(instance=post)
        return render(request, 'lugs/post_edit.html', {'form': form, 'post': post, 'title': f'Update Post {post.title}'})
    else:
        messages.warning(request, f'You can edit only LUGs you have created')
        return redirect('lug-posts', slug=post.lug.slug)

def deletePost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    if post.posted_by == user or post.lug.added_by == user:
        if request.method == 'POST':
            post.delete()
            messages.success(request, f'Post deleted!')
            return redirect('lug-posts', slug=post.lug.slug)

        return render(request, 'lugs/post_delete.html', {'post': post, 'title': f'Delete Post {post.title}'})
    else:
        messages.warning(request, f'You are not allowed to delete this post!')
        return redirect('lug-posts', slug=post.lug.slug)

def about(request):
    return render(request, 'lugs/about.html', {'title': 'About Linux LUGs'})
