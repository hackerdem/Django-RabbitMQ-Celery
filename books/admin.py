from django.contrib import admin
from .models import Author, Publisher, Book
# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','photo',)

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name','address','city','state_province','country','website')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','publisher','publication_date',)
    
