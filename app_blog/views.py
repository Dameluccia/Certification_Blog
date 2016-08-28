from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth.decorators import permission_required,login_required
from .models import Post, User
from .forms import PostForm, UserForm

# Create your views here.
def post_list(request):
    queryset_list =Post.objects.filter(draft=False).filter(publish__lte=timezone.now()).order_by("-timestamp")
    # all().order_by("-timestamp","-updated")
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_list, 9) # Show 5 articles per page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
    "object_list" : queryset,
    "title" : "Articles",
    }
    return render(request, 'list.html',context)

@permission_required('app_blog.Can_delete_permission')
def draft_list(request):
    queryset_list =Post.objects.filter(Q(draft=True) | Q(publish__gt=timezone.now())).order_by("-timestamp")
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query)
        ).distinct()
    # all().order_by("-timestamp","-updated")
    paginator = Paginator(queryset_list, 9) # Show 5 articles per page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
    "object_list" : queryset,
    "title" : "Articles",
    }
    return render(request, 'draft_list.html',context)

@permission_required('app_blog.Can_delete_permission')
def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if not instance.publish:
            instance.publish = timezone.now()
        instance.save()
        return redirect(instance.get_absolute_url())
    context = {
    "form" : form
    }
    return render(request, 'post_form.html', context)


def post_detail(request, slug):
    instance = get_object_or_404(Post, slug=slug)
    context = {
    "title" : instance.title,
    "instance": instance,
    }
    return render(request, 'detail.html',context)

@permission_required('app_blog.Can_delete_permission')
def draft_detail(request, slug):
    instance = get_object_or_404(Post, slug=slug)
    context = {
    "title" : instance.title,
    "instance": instance,
    }
    return render(request, 'draft_detail.html',context)


@permission_required('app_blog.Can_delete_permission')
def post_update(request, slug):
        instance = get_object_or_404(Post, slug=slug)
        form = PostForm(request.POST or None, request.FILES or None ,instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect(instance.get_absolute_url())

        context = {
        "title" : instance.title,
        "instance": instance,
        "form" : form
        }
        return render(request, 'post_form.html',context)

@permission_required('app_blog.Can_delete_permission')
def post_delete(request, slug):
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    return redirect('list')

@login_required
def user_profile(request, id):
    instance = get_object_or_404(User, id=id)
    context = {
    "instance" : instance
    }
    return render(request,'profile.html',context)

@login_required
def user_update(request, id):
    instance = get_object_or_404(User, id=id)

    form = UserForm(request.POST or None,instance=instance)
    if request.user.id == instance.id :

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect(reverse('profile', args=[request.user.id]))
        context = {
        "form" : form,
        }
        return render(request,'user_update.html',context)
    else:
        return redirect(reverse('profile', args=[request.user.id]))
