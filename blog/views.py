from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

# READ - Lista todos os posts do banco de dados
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


# READ - Exibe os detalhes de um post específico pelo ID (pk)
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post_detail.html", {"post": post})

# CREATE - Cria um novo post
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form': form})

# UPDATE - Edita um post existente pelo ID (pk)
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

# DELETE - Deleta um post existente pelo ID (pk)
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'post_delete.html', {'post': post})