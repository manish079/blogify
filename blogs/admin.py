from django.contrib import admin
from .models import Blog, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created_at', 'updated_at')
    search_fields = ('category_name',)
    
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'status', 'is_featured', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable = ('status', 'is_featured')
    



