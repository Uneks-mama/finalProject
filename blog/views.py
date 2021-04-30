from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Post, Profile
from .forms import CommentForm, ContactusForm


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    # 1 posts in each page
    paginate_by = 3


# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'

def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None

    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form}, )


def profile_list(request):
    profiles = Profile.objects.all().order_by('date_published')
    context = {
        'profiles': profiles
    }
    return render(request, 'portfolio.html', context)


def profile_detail(request, pk):
    profile = Profile.objects.get(pk=pk)
    context = {
        'profile': profile
    }
    return render(request, 'portfolio_detail.html', context)


# def redirect_view(request):
#     response = redirect('/redirect-success/')
#     return response


def contact_us(request):
    # new_feedback = None
    # Comment posted
    if request.method == 'POST':
        contactus_form = ContactusForm(data=request.POST)
        if contactus_form.is_valid():
            # Create Comment object but don't save to database
            # new_feedback = contactus_form.save(commit=True)
            # new_feedback.save()
            contactus_form.save()
            return redirect('home')
    else:
        contactus_form = ContactusForm()

    return render(request, 'contact_us.html', {'contactus_form': contactus_form}, )
