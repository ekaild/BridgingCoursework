from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils import timezone
from .models import Post
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm

def cv(request):
    return render(request, 'cv.html', {})

def cv_edit(request):
  
    post = get_object_or_404(Post)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('cv', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'cv/cv_edit.html', {'form': form})
    