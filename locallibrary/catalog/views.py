from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic


class BookDetailView(generic.DetailView):
    model = Book

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2
 
def index(request):
    # keyword
    keyword = 'fiction'
    # Generate count of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count() 
    
    
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # Available books containing the keyword 'magic' in their title, case insensitive
    num_books_with_keyword = Book.objects.filter(title__icontains=keyword).count()
    # Available genres containing the keyword 'magic' in their title, case insensitive
    num_genres_with_keyword = Genre.objects.filter(name__icontains=keyword).count()
    # count of Authors
    # The 'all()' is implied by default
    num_authors = Author.objects.count()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres_with_keyword': num_genres_with_keyword,
        'num_books_with_keyword': num_books_with_keyword,
        
        
    }
    
    # render the HTML template index.html with the data in the context varieble
    return render(request, 'index.html', context=context)
    