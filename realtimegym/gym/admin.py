from django.contrib import admin
from .models import ContactMessage, MembershipEnquiry, Testimonial, BlogPost


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'rating', 'is_active', 'created_at']
    list_filter = ['is_active', 'rating']
    search_fields = ['name']
    list_editable = ['is_active']


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'published', 'created_at']
    list_filter = ['published', 'category']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['published']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email']


@admin.register(MembershipEnquiry)
class MembershipEnquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'plan', 'created_at']
    list_filter = ['plan', 'created_at']
    search_fields = ['name', 'email']
