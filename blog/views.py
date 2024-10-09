from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Blog, Comment, Tag
from .forms import CommentForm
from django.core.mail import send_mail
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog_list')
        return render(request, 'home.html')


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('blog_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return response


class AuthView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog_list')
        return render(request, 'login.html', {'error': 'Invalid credentials'})


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('user_login')

class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'blog_list.html'
    paginate_by = 5
    login_url = '/login/'


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.blog = self.object
            comment.author = request.user
            comment.save()
            return redirect('blog_detail', pk=self.object.pk)
        return self.get(request, *args, **kwargs)


class LikeCommentView(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        comment.like_comment()
        return redirect('blog_detail', pk=comment.blog.id)


class ShareBlogView(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, blog_id):
        blog = get_object_or_404(Blog, id=blog_id)
        return render(request, 'share_blog.html', {'blog': blog})

    def post(self, request, blog_id):
        blog = get_object_or_404(Blog, id=blog_id)
        recipient_email = request.POST['email']
        send_mail(
            subject=f"Check out this blog: {blog.title}",
            message=blog.content,
            from_email='abc@example.com', 
            recipient_list=[recipient_email],
        )
        return redirect('blog_detail', pk=blog_id)

class SearchBlogView(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        query = request.GET.get('q', '').strip()
        tag_filter = request.GET.get('tag', '')
        results = Blog.objects.all()
        tags = Tag.objects.all()

        if query:
            results = results.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )

        if tag_filter:
            results = results.filter(tags__name__icontains=tag_filter)

        return render(request, 'search_results.html', {
            'results': results,
            'query': query,
            'tag_filter': tag_filter,
            'tags': tags,
        })
