from django.contrib import admin
from .models import Author, Book, Genre, BookInstance

class BooksInline(admin.TabularInline):
    model = Book
    extra = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
     list_display = ('title', 'author', 'display_genre')
     inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('book', 'status', 'due_back', 'id') 
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )



# admin.site.register(Author)

# admin.site.register(Book)
admin.site.register(Genre)
# admin.site.register(BookInstance)
# admin.site.register(Language)
       
