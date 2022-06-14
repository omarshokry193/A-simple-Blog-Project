from django.http import *
from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
)
def LikeView(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('core:article-detail',args=[str(pk)]))
def CategoryView(request,cats):
    category_posts = Post.objects.filter(category=cats)
    # category_posts = str(category_posts).lower()
    return render(request,'core/categorys.html',{'cats':cats.title().replace('-',' '),'category_posts':category_posts})
# def likes_counter(model_name):
#     model_name = Post
#     likes = model_name.pk
#     print(likes)
#     return likes
class HomeView(ListView):
    model = Post
    template_name = 'core/home.html'
    ordering = ['-post_date']
class ArticleDetailView(DetailView):
    model = Post
    def get_context_data(self,*args,**kwargs):
        context = super(ArticleDetailView,self).get_context_data(*args,**kwargs)
        data = get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes = data.total_likes()

        liked = False
        if data.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context
    template_name = 'core/article_details.html'
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'core/add_post.html'
    # fields = '__all__'
class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'core/add_comment.html'
    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('core:home')
class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'core/add_category.html'
    fields = '__all__'
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'core/update_post.html'
    #fields = ['title','title_tag','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'core/delete_post.html'
    success_url = reverse_lazy('core:home')
