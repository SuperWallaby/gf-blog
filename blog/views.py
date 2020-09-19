from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment, Gallery, Site, Skill, SubScriber, Contact
from .forms import  CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from .filters import PostFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




# def sendEmail(request):
# 	my_email = Site.objects.get(id=1).email
# 	name = request.POST.get('sendername', '')
# 	senderphone = request.POST.get('senderphone', '')
# 	senderMessage = request.POST.get('sendermessage', '');
# 	from_email = request.POST.get('senderemail', '')
	
# 	if my_email and name and from_email and senderMessage and senderphone:
# 		try:
# 			send_mail(name, senderMessage + senderphone, from_email, [my_email])
# 		except BadHeaderError:
# 			return HttpResponse('Invalid header found.')
# 		return HttpResponseRedirect('/thanks/')
# 	else:
# 		return HttpResponse('Make sure all fields are entered and valid.')

def SubScribeView(request):
	from_email = request.POST.get('email', '')
	SubScriber.objects.create(mail=from_email)
	return HttpResponseRedirect('/thanks/')

def ThanksView(request):
	return render(request, 'thanks.html')

def LikeView(request, slug):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	liked = False
	request_ip = request.META['REMOTE_ADDR']

	if post.like.filter(ip=request_ip).exists():
		post.like.filter(ip=request_ip).delete()
		liked = False
	else: 
		post.like.create(ip=request_ip)
		liked = True

	return HttpResponseRedirect(reverse('article-detail',args=[slug]))

class HomeView(ListView):
	model = Post
	template_name = 'index2.html'
	ordering = ['-pub_date']
	success_message = 'List successfully saved!!!!'
	paginate_by = 8
	paginate_orphans = 5

	def get_context_data(self, *args, **kwargs):
		popular_posts = self.object_list.annotate(num_likes=Count('like')).order_by('-num_likes')[:10]
		pop_posts = self.object_list.filter(pop_in_banner=True)
		cat_menu = Category.objects.all()
		
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		context["pop_posts"] = pop_posts
		context["popular_posts"] = popular_posts
		return context

class SearchView(ListView):
	model = Post
	template_name = 'search.html'
	ordering = ['-pub_date']
	success_message = 'List successfully saved!!!!'
	paginate_orphans = 5

	def get_context_data(self, *args, **kwargs):
		context = super(SearchView, self).get_context_data(*args, **kwargs)
		posts = Post.objects.all()

		myFilter = PostFilter(self.request.GET, queryset=posts)
		paginator = Paginator(myFilter.qs, 8)
		page = self.request.GET.get('page')

		try:
			response = paginator.page(page)
			page_obj = paginator.get_page(page)
		except PageNotAnInteger:
			response = paginator.page(1)
			page_obj = paginator.get_page(1)
		except EmptyPage:
			response = paginator.page(paginator.num_pages)
			page_obj = paginator.get_page(paginator.num_pages)

	

		context['myFilter'] = myFilter
		context['posts'] = response
		context['page_obj'] = page_obj
		
		return context


class TagsView(ListView):
	model = Post
	template_name = 'tags.html'
	ordering = ['-pub_date']
	success_message = 'List successfully saved!!!!'
	paginate_orphans = 5

	def get_context_data(self, *args, **kwargs):
		context = super(TagsView, self).get_context_data(*args, **kwargs)
		tag = self.kwargs['tags']

		posts = Post.objects.filter(tags__name__in=[tag])
		
		paginator = Paginator(posts, 8)
		page = self.request.GET.get('page')

		try:
			response = paginator.page(page)
			page_obj = paginator.get_page(page)
		except PageNotAnInteger:
			response = paginator.page(1)
			page_obj = paginator.get_page(1)
		except EmptyPage:
			response = paginator.page(paginator.num_pages)
			page_obj = paginator.get_page(paginator.num_pages)

		context['tag'] = tag
		context['posts'] = response
		context['page_obj'] = page_obj
		
		return context


class TagsListView(ListView):
	model = Post
	template_name = 'tags.html'

class CategoryListView(ListView):
	model = Category
	template_name = 'cat-list.html'

class BlogView(ListView):
	model = Post
	template_name = 'blog.html'
	ordering = ['-pub_date']
	paginate_by = 8

def CategoryView(request,slug):
	cat = Category.objects.get(slug=slug)
	category_posts = Post.objects.filter(category__slug=slug)

	page_number = request.GET.get('page')
	paginator = Paginator(category_posts, 8)
	page_obj = paginator.get_page(page_number)

	return render(request, 'category_detail.html', {'cat':cat,'category_posts':category_posts,'page_obj':page_obj})

class GalleryListView(ListView):
	model = Gallery
	template_name = 'galleries.html'
	paginate_by = 25
	paginate_orphans = 5

def AboutView(request):
	galleries = Gallery.objects.all()[:8]
	skils = Skill.objects.all()
	return render(request, 'about-2.html',{'galleries': galleries, 'skils': skils})

class ArticleDetail(DetailView):
	model = Post
	template_name = 'single-post.html'

	def get_context_data(self, *args, **kwargs):
		context = super(ArticleDetail, self).get_context_data(*args, **kwargs)
		
		total_likes = self.object.total_likes()
		comment_form = CommentForm()

		self.object.view_count = self.object.view_count +1
		self.object.save()


		next_id = int(self.object.pk) + 1
		prev_id = int(self.object.pk) - 1

		next_post = None
		prev_post = None
		if Post.objects.filter(id=next_id).exists():
			next_post = Post.objects.get(id=next_id)
		if Post.objects.filter(id=prev_id).exists():
			prev_post = Post.objects.get(id=prev_id)

		liked = False
		if self.object.like.filter(ip=self.request.META['REMOTE_ADDR']).exists():
    			liked = True

		context["comments"] = self.object.comments.all()
		context["comment_form"] = comment_form
		context["total_likes"] = total_likes
		context["liked"] = liked
		context["next_post"] = next_post
		context["prev_post"] = prev_post
		return context

def AddCommentView(request,slug):
	model = Comment
	form_class = CommentForm
	template_name = 'add_comment.html'

	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
    			
			post_id = comment_form.data.get("post_id")
			parent_id = comment_form.data.get("parent_id")
			face = comment_form.data.get("face")

			new_comment = comment_form.save(commit=False)
			if parent_id:
				new_comment.parent = Comment.objects.get(id=parent_id)

			# Create Comment object but don't save to database yet
			# Assign the current post to the comment
			new_comment.post = Post.objects.get(id=post_id)
			new_comment.face = face

			# Save the comment to the database
			new_comment.save()
	success_url = reverse_lazy('home')

	return HttpResponseRedirect('/article/{slug}'.format(slug=slug))


def AddContactView(request):
	if request.method == 'POST':
			name = request.POST.get('sendername', '')
			senderphone = request.POST.get('senderphone', '')
			senderMessage = request.POST.get('sendermessage', '');
			from_email = request.POST.get('senderemail', '')

			if name and from_email and senderMessage and senderphone:
				Contact.objects.create(name=name,phone=senderphone,email=from_email,message=senderMessage)
			else:
				return HttpResponse("Sorry we can't receive your message")
	
	return HttpResponseRedirect('/thanks/')



