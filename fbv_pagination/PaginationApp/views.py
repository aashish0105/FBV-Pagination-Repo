from django.shortcuts import render
from .models import Posts
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

# Create your views here.

# Create your views here.


def posts_display_view(request):
	posts = Posts.objects.all() # fetching all post objects from database
	p = Paginator(posts, 4) # creating a paginator object
	# getting the desired page number from url
	page_number = request.GET.get('page')
	try:
		page_obj = p.get_page(page_number) # returns the desired page object
	except PageNotAnInteger:
		# if page_number is not an integer then assign the first page
		page_obj = p.page(1)
	except EmptyPage:
		# if page is empty then return last page
		page_obj = p.page(p.num_pages)
	context = {'page_obj': page_obj}
	# sending the page object to pagination_display.html
	return render(request, 'PaginationApp/pagination_display.html', context)
