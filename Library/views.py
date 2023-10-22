from django.http import HttpResponse

def home_page(request):
    print("Home page requested")
    return HttpResponse("Hello, this is my home page!!")

def post_view(request):
    """Renders the post page."""
    return render(request, 'post.html')
