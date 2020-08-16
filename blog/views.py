from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import EditForm, PostForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# def home(request):
#	return render(request, 'home.html', {})

def LikeView(request,pk):
	print("likevie")
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	liked = False
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked = False
	else: 
		post.likes.add(request.user)
		liked = True
	return HttpResponseRedirect(reverse('article-detail',args=[str(pk)]))



class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	ordering = ['-pub_date']
	cats = Category.objects.all()
	success_message = 'List successfully saved!!!!'

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context


def CategoryListView(request):
	cat_menu_list = Category.objects.all()
	return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})


def CategoryView(request, cats):
	category_posts = Post.objects.filter(category=cats.replace('-',' '))
	return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '),'category_posts':category_posts})
	

class ArticleDetail(DetailView):
	model = Post
	template_name = 'article_details.html'

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(ArticleDetail, self).get_context_data(*args, **kwargs)

		stuff = get_object_or_404(Post, id=self.kwargs['pk'])
		total_likes = stuff.total_likes()

		liked = False
		if stuff.likes.filter(id=self.request.user.id).exists():
    			liked = True

		context["cat_menu"] = cat_menu
		context["total_likes"] = total_likes
		context["liked"] = liked
		return context

class AddCommentView(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'add_comment.html'
	# fields = ('title', 'body')
	
	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)

	success_url = reverse_lazy('home')

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'
	# fields = '__all__'
	# fields = ('title', 'body')


class AddCategoryView(CreateView):
	model = Category
	# form_class = PostForm
	template_name = 'add_category.html'
	fields = '__all__'
	# fields = ('title', 'body')


class EditPostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'edit_post.html'
	# fields = ['title', 'body']

class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('home')



