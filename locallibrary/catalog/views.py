from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin



class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return (
            BookInstance.objects.filter(borrower=self.request.user)
            .filter(status__exact='o')
            .order_by('due_back')
        )

class AuthorDetailView(generic.DetailView):
    model = Author

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2

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

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    num_visits += 1
    request.session['num_visits'] = num_visits
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres_with_keyword': num_genres_with_keyword,
        'num_books_with_keyword': num_books_with_keyword,
        'num_visits': num_visits,
        
        
    }
    
    # render the HTML template index.html with the data in the context varieble
    return render(request, 'index.html', context=context)
    